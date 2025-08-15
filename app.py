import streamlit as st
import base64

# Path to your image file
image_path = "anime-night-sky-illustration_23-2151684328.avif"

# Read and encode image to base64
with open(image_path, "rb") as f:
    encoded_img = base64.b64encode(f.read()).decode()

# CSS to set background
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/avif;base64,{encoded_img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

[data-testid="stHeader"], [data-testid="stToolbar"] {{
    background: rgba(0, 0, 0, 0);
}}

.css-1v0mbdj, .stTextInput > div > div > input, .stButton button {{
    background-color: rgba(255, 255, 255, 0.85);
    color: black;
}}

.stTextInput input {{
    border-radius: 5px;
}}

</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ----------------------------------------------

# Dummy user credentials (stored in session)
if "users" not in st.session_state:
    st.session_state.users = {"admin": "admin123"}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

if "mode" not in st.session_state:
    st.session_state.mode = "login"  # or "register"

# --- Registration Page ---
def register_page():
    st.title("Register New User")
    new_user = st.text_input("Choose Username")
    new_pass = st.text_input("Choose Password", type="password")
    confirm_pass = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if new_user in st.session_state.users:
            st.error("Username already exists.")
        elif new_pass != confirm_pass:
            st.error("Passwords do not match.")
        elif new_user == "" or new_pass == "":
            st.error("All fields are required.")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("Registration successful. You can now log in.")
            st.session_state.mode = "login"

    if st.button("Back to Login"):
        st.session_state.mode = "login"
        st.experimental_rerun()

# --- Login Page ---
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful.")
            st.switch_page("pages/1_Concerts.py")
        else:
            st.error("Invalid username or password.")

    if st.button("Register New User"):
        st.session_state.mode = "register"
        st.experimental_rerun()

# --- Main Control ---
if st.session_state.logged_in:
    st.switch_page("pages/1_Concerts.py")
elif st.session_state.mode == "register":
    register_page()
else:
    login_page()
