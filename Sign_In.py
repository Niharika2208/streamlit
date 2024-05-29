import streamlit as st

# Retrieve query parameters
query_params = st.experimental_get_query_params()

# Check if the 'page' parameter is set to 'home'
if query_params.get("page") == ["home"]:
    # Load the Home page content
    import pages.Home
    pages.Home.main()  # Assuming you have a `main()` function in Home.py
else:
    # Load the default login/register page
    import login_register  # Assuming this script is saved as login_register.py
    login_register.login_app()  # Assuming the login logic is in a function `login_app()`
