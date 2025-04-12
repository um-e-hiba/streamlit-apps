import streamlit as st
import re
import time

st.set_page_config(
    page_title="Password Strength Checker 🔐",
    page_icon="🛡️",
    layout="centered"
)

def colored_progress_bar(percent, color):
    st.markdown(f"""
        <div style="margin-bottom: 10px;">
            <div style="height: 15px; width: 100%; background-color: #e0e0e0; border-radius: 12px;">
                <div style="height: 100%; width: {percent}%; background-color: {color}; border-radius: 12px; text-align: right; padding-right: 10px; line-height: 20px; color: white; font-size: 0;">
                    {percent}%
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def check_password_strength(password):
    score = 0
    suggestions = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Use at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Use at least one lowercase letter")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Use at least one special character (!@#$%^&*).")
    
    return score, suggestions

 # Map score to label and progress percentage
score_map = {
    0: ("Very Weak", 0),
    1: ("Weak", 20),
    2: ("Weak-Moderate", 40),
    3: ("Moderate", 60),
    4: ("Stong", 80),
    5: ("Very Strong", 100)
}
color_map = {
    0: "#ff4d4f",   # red
    1: "#ff7a45",   # orange-red
    2: "#ffa940",   # orange
    3: "#ffc53d",   # yellow
    4: "#73d13d",   # green
    5: "#008000"    # blue
}

st.title("Password Strength Meter")
st.subheader("Enter Your Credentials")


# Inputs
username = st.text_input("User Name", placeholder="Enter Username")
password = st.text_input("Password", type="password", placeholder="Enter Password")


if password:
    score, suggestions = check_password_strength(password)
    label, progress = score_map[score]
    color = color_map[score]
    st.markdown(f"**Password Strength:** {label}")
    # Progress bar
    #st.progress(int((score / 5) * 100))
    colored_progress_bar(progress, color)

    if suggestions:
        st.markdown("**Suggestions to improve your password:**")
        for suggestion in suggestions:
            st.write(f'- {suggestion}')

if st.button("Submit"):
    with st.spinner("Checking password strength..."):
        time.sleep(1.5)  # fake processing time
    if not username and not password:
        st.warning("‼ Please fill in both username and password.")
    elif score < 5:
        st.error("✖ Your password is too weak. Please improve it before submitting.")
    else:
        st.success("✔ Form submitted!")
#st.snow()