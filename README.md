# 📊 Student Academic Improvement Dashboard

This is a **Streamlit** web app for analyzing and visualizing student academic improvement using **Polynomial Regression**. The app provides insights into weekly test scores, calculates score growth, and categorizes students based on their performance.  

✨ Features:
- Beautiful **animated title** and **result box pop effect**
- **Glass-effect cards** for input forms and results
- **Background image** for a modern look
- **Interactive graphs** showing performance trends
- Calculates **score growth** and **average score**
- Provides detailed **reason analysis** based on academic inputs

---

## 🔗 Live Demo

You can access the live app here:  
[Student Improvement Dashboard](https://studentimprovementproject-tharini.streamlit.app/)

---

## 🛠 Technologies Used

- Python 3.x
- [Streamlit](https://streamlit.io/)  
- NumPy & Matplotlib for computations & plotting
- Scikit-learn for Polynomial Regression
- HTML & CSS for animations and glass-effect styling

---

## 📁 Project Structure

student_improvement_project/
│
├─ main.py # Main Streamlit app
├─ requirements.txt # Dependencies
├─ README.md # Project overview
├─ data/ # CSV files or datasets (optional)
├─ results/ # Graphs or exported outputs (optional)
└─ src/ # Optional scripts or modules

---

## ⚡ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/student_improvement_project.git
cd student_improvement_project
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
```
🔧 How it Works

Enter student details (Name & Roll Number).

Provide academic inputs:

Semester Percentage

Attendance Percentage

Homework Completion

Average Study Hours

Enter weekly test scores for 5 weeks.

Click Analyze Improvement.

The app shows:

Improvement category (High, Moderate, Low)

Average score and score growth

Reason analysis

Performance trend graph

👩‍💻 Author

Tharini PS
Student Academic Improvement Project
