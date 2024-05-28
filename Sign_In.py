import streamlit as st
from menu import menu
from firebase_admin import auth, credentials, initialize_app
import requests

# Initialize Firebase
try:
    cred = credentials.Certificate('ata-project-a5bd3-b43dda61efbe.json')
    initialize_app(cred)
except ValueError:
    pass
   


# Firebase API endpoint for client-side authentication
FIREBASE_API_KEY = "AIzaSyBDHSIurYQP9JZcGz5v0vBOkydT9cPChFg"
FIREBASE_AUTH_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
FIREBASE_SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"

st.set_option("client.showSidebarNavigation", False)

# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role

def login_user(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(FIREBASE_AUTH_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        id_token = data["idToken"]
        user_info = auth.verify_id_token(id_token)
        st.session_state.user = user_info
        st.session_state.logged_in = True
        st.session_state.role = "user"  # Default role, customize as needed
        return True
    else:
        return False

def register_user(email, password):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(FIREBASE_SIGNUP_URL, json=payload)
    if response.status_code == 200:
        return login_user(email, password)
    else:
        return False

def redirect_to_home():
    # Redirect to Home page
    st.page_link("pages/Home.py", label="Home")
if not st.session_state.logged_in:
    st.title("Login or Register")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.page_link("pages/Home.py", label="Login"):
            if login_user(email, password):
                st.success("Logged in successfully!")
                #redirect_to_home()
            else:
                st.error("Invalid email or password")

    with tab2:
        new_email = st.text_input("New Email")
        new_password = st.text_input("New Password", type="password")
        if st.button("Register"):
            if register_user(new_email, new_password):
                st.success("Registered and logged in successfully!")
                redirect_to_home()
            else:
                st.error("Registration failed")

else:
    st.selectbox(
        "Select your role:",
        [None, "user", "admin"],
        key="_role",
        on_change=set_role,
    )

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.role = None
        st.success("Logged out successfully!")

#menu()  # Render the dynamic menu!
