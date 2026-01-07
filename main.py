import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import datetime

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Student Academic Improvement",
    layout="centered"
)

# ================= BACKGROUND IMAGE =================
bg_image_url = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f"

st.markdown(f"""
<style>
.stApp {{
    background-image: url("{bg_image_url}");
    background-size: cover;
    background-attachment: fixed;
}}

.block-container {{
    background-color: rgba(255, 255, 255, 0.18);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(14px);
}}

@keyframes fadeIn {{
    from {{opacity: 0; transform: translateY(-20px);}}
    to {{opacity: 1; transform: translateY(0);}}
}}

@keyframes pop {{
    0% {{transform: scale(0.8); opacity: 0;}}
    100% {{transform: scale(1); opacity: 1;}}
}}
</style>
""", unsafe_allow_html=True)

# ================= ANIMATED TITLE =================
st.markdown("""
<h1 style="text-align:center; animation: fadeIn 2s;">
📊 Student Academic Improvement Analysis<br>
<span style="font-size:20px;">By Tharini PS</span>
</h1>
""", unsafe_allow_html=True)

st.caption("Polynomial Regression based student performance tracking")

# ================= FORM =================
with st.form("student_form"):

    st.subheader("👤 Student Details")
    name = st.text_input("Enter Student Name")
    roll_no = st.text_input("Enter Roll Number")

    st.subheader("📘 Academic Inputs")
    semester_pct = st.number_input("Semester Percentage (%)", 0.0, 100.0, 70.0)
    attendance_pct = st.number_input("Attendance Percentage (%)", 0.0, 100.0, 80.0)
    homework_pct = st.number_input("Homework Completion Percentage (%)", 0.0, 100.0, 75.0)
    study_hours = st.number_input("Average Study Hours per Day", 0.0, 12.0, 2.0)

    st.subheader("📅 Weekly Test Scores")
    weeks = np.array([1, 2, 3, 4, 5])
    scores = []

    for i in range(5):
        scores.append(st.number_input(f"Week {i+1} Test Score", 0, 100, 0))

    submit = st.form_submit_button("Analyze Improvement")

# ================= PROCESS =================
if submit:

    if not name or not roll_no:
        st.error("Please enter both Name and Roll Number")
        st.stop()

    y = np.array(scores)
    X = weeks.reshape(-1, 1)

    # Polynomial Regression
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)

    avg_score = np.mean(y)
    score_growth = y[-1] - y[0]

    # ================= CATEGORY LOGIC =================
    if avg_score >= 90 and score_growth == 0:
        category = "High Consistent Performance"
        bg = "#007bff"

    elif score_growth >= 15:
        category = "High Improvement"
        bg = "#28a745"

    elif score_growth >= 5:
        category = "Moderate Improvement"
        bg = "#ffc107"

    else:
        category = "Low Improvement"
        bg = "#dc3545"

    # ================= REASONS =================
    reasons = []

    if category == "High Consistent Performance":
        reasons.append("Consistently high scores across all weeks")

    elif category == "High Improvement":
        reasons.append("Strong upward trend in weekly test scores")

    elif category == "Moderate Improvement":
        reasons.append("Gradual improvement with minor fluctuations")

    else:
        reasons.append("Minimal improvement across weeks")

    if semester_pct >= 75:
        reasons.append("Good overall semester performance")
    else:
        reasons.append("Semester performance needs improvement")

    if attendance_pct >= 85:
        reasons.append("Consistent class attendance")
    else:
        reasons.append("Attendance inconsistency affected learning")

    if homework_pct >= 80:
        reasons.append("Regular homework completion")
    else:
        reasons.append("Homework practice needs improvement")

    if study_hours >= 3:
        reasons.append("Sufficient daily study hours")
    else:
        reasons.append("Insufficient daily study time")

    # ================= ANIMATED RESULT BOX =================
    st.markdown(
        f"""
        <div style="
            background-color:{bg};
            padding:20px;
            border-radius:15px;
            animation: pop 0.8s ease;
            box-shadow: 0 12px 30px rgba(0,0,0,0.3);
            color:white;
        ">
        <h4>📌 Improvement Category: {category}</h4>
        <b>Name:</b> {name}<br>
        <b>Roll No:</b> {roll_no}<br>
        <b>Average Score:</b> {avg_score:.2f}<br>
        <b>Score Growth:</b> {score_growth}<br>
        <b>Generated On:</b> {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("📋 Reason Analysis")
    for r in reasons:
        st.write("•", r)

    # ================= PREMIUM GRAPH =================
    X_plot = np.linspace(1, 5, 100).reshape(-1, 1)
    y_plot = model.predict(poly.transform(X_plot))

    fig, ax = plt.subplots()
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")

    ax.scatter(X, y, s=80)
    ax.plot(X_plot, y_plot, linewidth=3)

    ax.set_xlabel("Week")
    ax.set_ylabel("Test Score")
    ax.set_title("Academic Performance Trend")

    st.pyplot(fig)
