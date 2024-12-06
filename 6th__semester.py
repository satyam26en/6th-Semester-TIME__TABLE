import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
from io import BytesIO
from PIL import Image
import requests
import re

# Set page configuration
st.set_page_config(
    page_title="🎓 Student Timetable Viewer",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Define background images
background_images = [
    {"url": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1950&q=80"},
    {"url": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=1950&q=80"},
    {"url": "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=1950&q=80"},
    {"url": "https://images.unsplash.com/photo-1496307042754-b4aa456c4a2d?auto=format&fit=crop&w=1950&q=80"},
    {"url": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=1950&q=80"},
    {"url": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1950&q=80"},
    {"url": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=1950&q=80"},
    {"url": "https://www.rollingstone.com/wp-content/uploads/2023/05/taylor-swift-metlife-opening.jpg?w=1581&h=1054&crop=1"}
]

# Define themes
themes = [
    {
        'name': 'Motivational',
        'color_scheme': {
            'header_fill': '#1abc9c',
            'header_text': 'white',
            'time_fill': '#16a085',
            'time_text': 'white',
            'day_fill_1': '#ecf0f1',
            'day_fill_2': '#bdc3c7',
            'day_text': '#2c3e50'
        },
        'background_image': background_images[0]['url']
    },
    {
        'name': 'Academic',
        'color_scheme': {
            'header_fill': '#e74c3c',
            'header_text': 'white',
            'time_fill': '#c0392b',
            'time_text': 'white',
            'day_fill_1': '#fdfefe',
            'day_fill_2': '#dfe6e9',
            'day_text': '#2d3436'
        },
        'background_image': background_images[1]['url']
    },
    {
        'name': 'Lecture',
        'color_scheme': {
            'header_fill': '#8E44AD',
            'header_text': 'white',
            'time_fill': '#732D91',
            'time_text': 'white',
            'day_fill_1': '#f5f6f4',
            'day_fill_2': '#dcdde1',
            'day_text': '#2c3e50'
        },
        'background_image': background_images[2]['url']
    },
    {
        'name': 'Study',
        'color_scheme': {
            'header_fill': '#27AE60',
            'header_text': 'white',
            'time_fill': '#1e8449',
            'time_text': 'white',
            'day_fill_1': '#f8f9fa',
            'day_fill_2': '#dfe6e9',
            'day_text': '#2c3e50'
        },
        'background_image': background_images[3]['url']
    },
    {
        'name': 'Collaboration',
        'color_scheme': {
            'header_fill': '#F39C12',
            'header_text': 'white',
            'time_fill': '#D68910',
            'time_text': 'white',
            'day_fill_1': '#FDEBD0',
            'day_fill_2': '#F5CBA7',
            'day_text': '#A04000'
        },
        'background_image': background_images[4]['url']
    },
    {
        'name': 'Vibrant',
        'color_scheme': {
            'header_fill': '#E74C3C',
            'header_text': 'white',
            'time_fill': '#C0392B',
            'time_text': 'white',
            'day_fill_1': '#F1948A',
            'day_fill_2': '#EC7063',
            'day_text': '#641E16'
        },
        'background_image': background_images[5]['url']
    },
    {
        'name': 'Graduation',
        'color_scheme': {
            'header_fill': '#2ECC71',
            'header_text': 'white',
            'time_fill': '#27AE60',
            'time_text': 'white',
            'day_fill_1': '#A9DFBF',
            'day_fill_2': '#2ECC71',
            'day_text': '#145A32'
        },
        'background_image': background_images[6]['url']
    },
    {
        'name': 'Taylor Swift',
        'color_scheme': {
            'header_fill': '#FF69B4',
            'header_text': 'white',
            'time_fill': '#FF1493',
            'time_text': 'white',
            'day_fill_1': '#ffe4e1',
            'day_fill_2': '#ffb6c1',
            'day_text': '#2c3e50'
        },
        'background_image': background_images[7]['url']
    }
]

def select_random_theme(themes_list):
    return random.choice(themes_list)

selected_theme = select_random_theme(themes)
color_scheme = selected_theme['color_scheme']
background_image = selected_theme['background_image']

@st.cache_data(ttl=3600)
def load_data(url):
    try:
        df = pd.read_csv(url)
        return df
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Network error loading data from {url}: {e}")
    except pd.errors.ParserError as e:
        st.error(f"❌ Parsing error in data from {url}: {e}")
    except Exception as e:
        st.error(f"❌ Unexpected error loading data from {url}: {e}")
    return None

# URLs for CSV data
section_url = 'https://raw.githubusercontent.com/satyam26en/6th-Semester-TIME__TABLE/main/section_list_6Th_semester%20-%20Sheet1.csv'
elective_url = 'https://raw.githubusercontent.com/satyam26en/TIME_TABLE_KIIT/main/Professional_Elective%20-%20Sheet1.csv'
core_url = 'https://raw.githubusercontent.com/satyam26en/6th-Semester-TIME__TABLE/main/section_time_table%20-%20Sheet1.csv'

# Load data
section_df = load_data(section_url)
elective_df = load_data(elective_url)
core_df = load_data(core_url)

# Stop if any data fails to load
if section_df is None or elective_df is None or core_df is None:
    st.stop()

# Clean Roll No. column
if 'Roll No.' in section_df.columns:
    section_df['Roll No.'] = section_df['Roll No.'].astype(str).str.strip()
else:
    st.error("❌ 'Roll No.' column not found in section data.")
    st.stop()

# Define days and times
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
times = ['8 TO 9', '9 TO 10', '10 TO 11', '11 TO 12', '12 TO 1', '1 TO 2', '2 TO 3', '3 TO 4', '4 TO 5']

# Mapping from abbreviated day to full day
day_mapping = {
    'MON': 'Monday',
    'TUE': 'Tuesday',
    'WED': 'Wednesday',
    'THU': 'Thursday',
    'FRI': 'Friday',
    'SAT': 'Saturday'
}

def calculate_average_brightness(image):
    grayscale_image = image.convert("L").resize((100, 100))
    pixels = list(grayscale_image.getdata())
    return sum(pixels) / len(pixels)

@st.cache_data
def fetch_background_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        st.error(f"❌ Failed to load background image from {url}: {e}")
        return None

def add_background_and_set_text_color(selected_background):
    img = fetch_background_image(selected_background)
    if img is None:
        return "#FFFFFF"
    avg_brightness = calculate_average_brightness(img)
    text_color = "#000000" if avg_brightness > 127 else "#FFFFFF"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{selected_background}");
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .table-container {{
            overflow-x: auto;
            padding: 0;
            margin: 0;
        }}
        @media only screen and (max-width: 600px) {{
            .stApp h1 {{
                font-size: 24px !important;
            }}
            .stApp h3 {{
                font-size: 18px !important;
            }}
            table {{
                font-size: 10px !important;
            }}
        }}
        @media only screen and (min-width: 601px) and (max-width: 1024px) {{
            .stApp h1 {{
                font-size: 28px !important;
            }}
            .stApp h3 {{
                font-size: 20px !important;
            }}
            table {{
                font-size: 12px !important;
            }}
        }}
        @media only screen and (min-width: 1025px) {{
            .stApp h1 {{
                font-size: 32px !important;
            }}
            .stApp h3 {{
                font-size: 22px !important;
            }}
            table {{
                font-size: 14px !important;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    return text_color

text_color = add_background_and_set_text_color(background_image)

def standardize_time_slot(time_slot):
    """
    Standardizes various time slot formats to match the predefined 'times' list.
    Example mappings:
        '8-9' -> '8 TO 9'
        '08:00-09:00' -> '8 TO 9'
        '8 to 9' -> '8 TO 9'
    """
    time_slot = time_slot.upper().replace(':', '').replace('-', ' TO ').replace('TO', ' TO ').replace(' TO  ', ' TO ').strip()
    match = re.match(r'(\d{1,2})\s*TO\s*(\d{1,2})', time_slot)
    if match:
        start, end = match.groups()
        standardized_slot = f"{int(start)} TO {int(end)}"
        return standardized_slot
    return time_slot  # Return as is if it doesn't match expected patterns

def generate_timetable_df(roll_number):
    student_section = section_df[section_df['Roll No.'] == roll_number]
    if student_section.empty:
        st.error("❌ Roll number not found. Please check and try again.")
        return None
    
    # Extract sections
    core_section = student_section['Core Section'].values[0]
    elective_1_section = student_section['Professional Elective 1'].values[0]
    elective_2_section = student_section['Professional Elective 2'].values[0]
    
    # Fetch timetables
    elective_1_timetable = elective_df[elective_df['Section(DE)'] == elective_1_section]
    elective_2_timetable = elective_df[elective_df['Section(DE)'] == elective_2_section]
    core_timetable = core_df[core_df['Section'] == core_section]
    
    # Initialize timetable matrix
    timetable_matrix = pd.DataFrame(index=times, columns=days, data='')
    
    def fill_timetable(timetable_df, timetable_matrix):
        if timetable_df.empty:
            st.warning("⚠️ Timetable data is empty for the selected section.")
            return
        # Identify columns that contain 'ROOM' and 'TIME'
        room_columns = sorted([col for col in timetable_df.columns if 'ROOM' in col], key=lambda x: int(re.findall(r'\d+', x)[0]))
        time_columns = sorted([col for col in timetable_df.columns if 'TIME' in col], key=lambda x: int(re.findall(r'\d+', x)[0]))
        
        # Ensure that each ROOM has a corresponding TIME
        if len(room_columns) != len(time_columns):
            st.warning("⚠️ Mismatch between ROOM and TIME columns.")
            return
        
        for _, row in timetable_df.iterrows():
            day_abbr = row.get('DAY', '').upper()
            day = day_mapping.get(day_abbr, 'Unknown')
            if day == 'Unknown':
                st.warning(f"⚠️ Unrecognized day abbreviation: {day_abbr}")
                continue
            for room_col, time_col in zip(room_columns, time_columns):
                room_number = row.get(room_col, '').strip()
                time_slot_raw = row.get(time_col, '').strip()
                if not time_slot_raw:
                    st.warning(f"⚠️ Missing time slot for {room_col}")
                    continue
                time_slot = standardize_time_slot(time_slot_raw)
                if time_slot not in times:
                    st.warning(f"⚠️ Time slot '{time_slot}' does not match predefined slots.")
                    continue
                subject = row.get(time_col, '').strip()
                if isinstance(subject, str) and subject.lower() != 'x' and subject != '':
                    existing_entry = timetable_matrix.at[time_slot, day]
                    new_entry = f"{subject} ({room_number})"
                    if existing_entry:
                        timetable_matrix.at[time_slot, day] = f"{existing_entry}<br>{new_entry}"
                    else:
                        timetable_matrix.at[time_slot, day] = new_entry
    
    # Fill timetable with core and electives
    fill_timetable(core_timetable, timetable_matrix)
    fill_timetable(elective_1_timetable, timetable_matrix)
    fill_timetable(elective_2_timetable, timetable_matrix)
    
    # Replace NaNs with empty strings and ensure correct order
    timetable_matrix = timetable_matrix.fillna('')
    timetable_matrix = timetable_matrix.reindex(times)
    
    return timetable_matrix

def visualize_timetable(timetable_matrix, color_scheme):
    if timetable_matrix is None:
        return None
    bold_time_slots = [f"<b>{time}</b>" for time in timetable_matrix.index]
    # Prepare cell values
    cell_values = [bold_time_slots] + [timetable_matrix[day].tolist() for day in days]
    # Define fill colors
    fill_colors = [
        [color_scheme['time_fill']] * len(times)
    ]
    for i in range(len(days)):
        fill = [color_scheme['day_fill_1']] * len(times) if i % 2 == 0 else [color_scheme['day_fill_2']] * len(times)
        fill_colors.append(fill)
    
    # Define font colors
    font_colors = [
        color_scheme['time_text']
    ]
    for _ in days:
        font_colors.append([color_scheme['day_text']] * len(times))
    
    fig = go.Figure(data=[go.Table(
        columnwidth=[100] + [120]*6,
        header=dict(
            values=['<b>TIME</b>'] + [f'<b>{day.upper()}</b>' for day in days],
            fill_color=color_scheme['header_fill'],
            align='center',
            font=dict(color=color_scheme['header_text'], size=14, family='Arial Black'),
            height=50
        ),
        cells=dict(
            values=cell_values,
            fill=dict(color=fill_colors),
            align='center',
            font=dict(
                color=font_colors,
                size=12,
                family='Arial'
            ),
            height=40,
            line_color='rgba(0,0,0,0.1)',
            line_width=1
        )
    )])
    fig.update_layout(
        autosize=True,
        title=dict(
            text='📅 Student Timetable',
            x=0.5,
            xanchor='center',
            font=dict(size=24, family='Arial Black', color='teal')
        ),
        margin=dict(l=20, r=20, t=60, b=20),
        height=700,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Arial')
    )
    return fig

def save_timetable_as_image(fig, filename='timetable.jpg'):
    if fig is None:
        st.error("❌ No figure to save.")
        return
    try:
        img_bytes = fig.to_image(format='jpg')
        return img_bytes
    except Exception as e:
        st.error(f"❌ Error saving image: {e}")
        return None

def create_download_button(img_bytes, filename='timetable.jpg'):
    if not img_bytes:
        st.error("❌ No image to download.")
        return
    st.download_button(
        label="📥 Download Timetable as JPG",
        data=img_bytes,
        file_name=filename,
        mime="image/jpg",
        key='download-button'
    )

def validate_roll_number(roll_number):
    pattern = r'^[A-Za-z0-9]{5,10}$'  # Example pattern: 5-10 alphanumeric characters
    return re.match(pattern, roll_number) is not None

def main():
    # Header
    st.markdown(
        f"<h1 style='text-align: center; color: {text_color};'>🎓 Student Timetable Viewer</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3 style='text-align: center; color: {text_color};'><b>Enter Your Roll Number</b></h3>",
        unsafe_allow_html=True
    )
    
    # Sidebar for Debugging
    with st.sidebar:
        show_debug = st.checkbox("🔍 Show Debug Information", value=False)
    
    # Center the input and button using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        roll_number = st.text_input("", max_chars=10, key='roll_number_input')
        download = st.checkbox("📥 Download timetable as JPG image")
        generate_button = st.button("🔍 Generate Timetable")
    
    if generate_button:
        if roll_number.strip():
            if validate_roll_number(roll_number.strip()):
                timetable_df = generate_timetable_df(roll_number.strip())
                if timetable_df is not None:
                    fig = visualize_timetable(timetable_df, color_scheme)
                    if fig:
                        st.markdown('<div class="table-container">', unsafe_allow_html=True)
                        st.plotly_chart(fig, use_container_width=True)
                        if download:
                            img_bytes = save_timetable_as_image(fig)
                            if img_bytes:
                                create_download_button(img_bytes)
                        st.markdown('</div>', unsafe_allow_html=True)
                    else:
                        st.error("❌ Failed to generate the timetable visualization.")
            else:
                st.error("❌ Invalid roll number format. Please enter a valid roll number (5-10 alphanumeric characters).")
        else:
            st.error("❌ Please enter a valid roll number.")
    
    # Conditional Debugging Information
    if 'show_debug' in locals() and show_debug:
        st.sidebar.markdown("### 🛠️ Debug Information")
        st.sidebar.write("#### DataFrames:")
        st.sidebar.write("**Section DataFrame:**")
        st.sidebar.write(section_df.head())
        st.sidebar.write("**Elective DataFrame:**")
        st.sidebar.write(elective_df.head())
        st.sidebar.write("**Core DataFrame:**")
        st.sidebar.write(core_df.head())
    
    # Hide Streamlit footer
    hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
