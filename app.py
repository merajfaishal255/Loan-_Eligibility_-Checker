import streamlit as st

st.set_page_config(page_title="🎓 Grade Predictor", page_icon="📘")

st.markdown("""
    <h1 style='text-align:center; color:#4B0082;'>🎓 Student Grade Predictor</h1>
    <p style='background-color:yellow; padding:5px; font-weight:bold;'>Enter student's marks to predict grade</p>
""", unsafe_allow_html=True)

marks = st.number_input("Enter Marks (0-100):", min_value=0, max_value=100)

if st.button("Predict Grade"):
    if marks >= 90:
        grade = "A 🌟"
    elif marks >= 75:
        grade = "B 👍"
    elif marks >= 60:
        grade = "C 🙂"
    elif marks >= 40:
        grade = "D 😐"
    else:
        grade = "Fail ❌"

    st.markdown(f"<h2 style='color:#FF1493;'>Grade: {grade}</h2>", unsafe_allow_html=True)

    # Developer Name Section
    st.markdown("""
        <p style='color:#008B8B; font-size:18px; text-align:center; margin-top:20px;'>
            ⭐ Developed by <strong>Faishal Meraj</strong> ⭐
        </p>
    """, unsafe_allow_html=True)
