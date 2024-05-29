import streamlit as st

def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.markdown("### Navigation")
    st.sidebar.markdown("[Home](pages/Home.py)")
    st.sidebar.markdown("[General Information](pages/1_General_Information.py)")
    st.sidebar.markdown("[Crop Assist](pages/Crop_Assist.py)")
    st.sidebar.markdown("[Dimension Manager](pages/Dimension_Manager.py)")
    st.sidebar.markdown("[Sign Out](Sign_In.py)")

def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.markdown("[Sign In/Sign Up](Sign_In.py)")

def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()

def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "role" not in st.session_state or st.session_state.role is None:
        st.experimental_set_query_params(page="Sign_In")
        st.experimental_rerun()
    menu()
