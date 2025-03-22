import streamlit as st 
import re

st.set_page_config(page_title="Password Strength Checker by Hassan Jamshed", page_icon="🔐")

st.title("🔐 Password Strength Generator")
st.markdown("""
"## Welcome to the Password Strength Checker!🔐""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password:
    if len(password) >=8:
        score += 1 #increase score by 1
    else:
        feedback.append("❌ Passowrd should be atleast 8 character long.")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Passowrd should include both upper case and lower letters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Passowrd should include atleast one number (0-9).")
        
    #special charaCTER
    if re.search(r"[!@#$%&^*]", password):
        score += 1
    else:
        feedback.append("❌ Passowrd should include atleast one special character.")
        
    #dispaly strength
    if score == 4:
        st.success("✔️ Your password is strong")
    elif score == 3 :
        st.info("⚠️ Moderate Password - Consider improving password by adding more feature")
    else:
        st.error("❌ Week Password - Follow the suggestion below for improve password security")
        
    #feedback
    if feedback:
        st.markdown("## Improvement Suggestion")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to check stregth.")
