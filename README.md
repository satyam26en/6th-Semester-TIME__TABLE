### README.md
# 📚 Student Time Table Generator

A comprehensive and user-friendly application that generates personalized class timetables for students based on their roll numbers. The project integrates core and elective course data to create visually appealing timetables that can be viewed, exported, and shared through a web interface.

## ✨ Features

- **🎯 Personalized Timetables**: Generate customized timetables based on student roll numbers
- **📊 Data Integration**: Seamlessly combine core and elective course data into unified schedules
- **🎨 Visual Representation**: Clean, tabular format visualization using Plotly
- **💾 Export Functionality**: Save timetables as JPG images for sharing and archiving
- **🌐 Web Application**: Interactive Streamlit-based web interface
- **☁️ Cloud Hosting**: Deployed on Streamlit Cloud for easy access
- **🛡️ Error Handling**: Robust data processing with validation and error management

## 🌐 Live Demo

[🌐 Access the Live Application](https://studenttimetable-pkmnmkpzgjykajfm5guvhq.streamlit.app/)

## 📸 Screenshots

### Application Interface
![Application Interface](screenshots/image1.png)
*Main interface showing the roll number input and timetable generation*

### Generated Timetable
![Generated Timetable](screenshots/image2.png)
*Example of a generated student timetable with core and elective subjects*

## 🛠️ Technologies Used

- **Python 3.7+**
- **Pandas** - Data manipulation and analysis
- **Plotly** - Interactive data visualization
- **NumPy** - Numerical computing
- **Streamlit** - Web application framework

## 📁 Project Structure

```
Student__Time__Table/
├── data/
│   ├── SECTION.csv                    # Roll number to section mapping
│   ├── Elective_TIME_TABLE.csv        # Elective subjects timetable
│   └── CORE_TIME_TABLE_2-Sheet1.csv   # Core subjects timetable
├── scripts/
│   └── generate_timetable.py          # Main application script
├── screenshots/
│   ├── image1.png                     # Application interface screenshot
│   └── image2.png                     # Generated timetable screenshot
├── output/                            # Generated timetable images and files
├── requirements.txt                   # Project dependencies
├── streamlit_app.py                   # Streamlit web application
└── README.md                          # Project documentation
```

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/satyam26en/Student__Time__Table.git
   cd Student__Time__Table
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Local Execution

1. **Run the main script**
   ```bash
   python scripts/generate_timetable.py
   ```

2. **Enter student roll number** when prompted

3. **View results**:
   - Timetable displayed in console
   - Interactive Plotly visualization opens in browser
   - JPG image saved in `output/` directory

### Web Application

1. **Run Streamlit app locally**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the application** at `http://localhost:8501`

3. **Enter roll number** in the web interface to generate timetable

## 📊 Data Format

### SECTION.csv
Maps student roll numbers to their respective sections:
```csv
Roll_Number,Core_Section,Elective_Section
12345,A1,E1
12346,A2,E2
```

### Core and Elective Timetable Files
Contain schedule information with time slots and subjects:
```csv
Time,Monday,Tuesday,Wednesday,Thursday,Friday
09:00-10:00,Subject1,Subject2,Subject3,Subject4,Subject5
10:00-11:00,Subject6,Subject7,Subject8,Subject9,Subject10
```

## 🌐 Deployment

### Streamlit Cloud Deployment

1. **Fork this repository** to your GitHub account

2. **Sign up** for [Streamlit Cloud](https://streamlit.io/)

3. **Connect your GitHub account** and select this repository

4. **Deploy** with the following settings:
   - **Main file path**: `streamlit_app.py`
   - **Python version**: 3.9+

5. **Share** your deployed application URL

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Satyam** - [@satyam26en](https://github.com/satyam26en)

## 🙏 Acknowledgments

- Thanks to the open-source community for the amazing libraries
- Inspired by the need for efficient student schedule management
- Special thanks to contributors and users providing feedback

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/satyam26en/Student__Time__Table/issues) page
2. Create a new issue if your problem isn't already addressed
3. Provide detailed information about your environment and the issue

## 🔄 Version History

- **v1.0.0** - Initial release with core functionality
- **v1.1.0** - Added Streamlit web interface
- **v1.2.0** - Implemented cloud deployment and export features

---

⭐ **Star this repository if you found it helpful!**
