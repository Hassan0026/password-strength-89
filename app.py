import re
import streamlit as st

st.set_page_config(page_title="Password Strength Checker by Hassan Jamshed", page_icon="🔑", layout="centered")
#custom css
st.markdown(""" 
<style>
    .main {text-align:center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px; }
    .stButton button:hover { background-color: #45a049;}
</style>
""", unsafe_allow_html=True)

#page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

#function
def check_password_strenght(password):
    score = 0
    feedback = []
    
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
        with st.expander("🔍 Improve Your Password"):
            for item in feedback:
                st.write(item)
    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")
    
    #button working
    if st.button("Check Strength"):
        if password:
            check_password_strenght(password)
        else:
            st.warning("⚠️ Please enter a password first!")