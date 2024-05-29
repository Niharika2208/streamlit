import streamlit as st

def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.markdown("### Navigation")
    st.sidebar.markdown("[Home](Home)")
    st.sidebar.markdown("[General Information](1_General_Information)")
    st.sidebar.markdown("[Crop Assist](Crop_Assist)")
    st.sidebar.markdown("[Dimension Manager](Dimension_Manager)")

def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.markdown("[Sign In/Sign Up](Sign_In)")

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
