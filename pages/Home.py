import streamlit as st
import matplotlib.image as mpimg
from pages import General_Information, Crop_Assist, Dimension_Manager

def main():
    # Create the sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "General Information", "Crop Assist", "Dimension Manager"])

    # Load the selected page
    if page == "Home":
        home_app()
    elif page == "General Information":
        General_Information.app()
   # elif page == "Crop Assist":
    #    Crop_Assist.app()
    #elif page == "Dimension Manager":
    #    Dimension_Manager.app()

def home_app():
    # SurViZ logo
    st.image('logo_ata.png')

    # Main Description
    st.markdown("## 👋 Welcome to the Dimension Detection tool!")
    st.markdown("Developed by the Team Quadratech")
    st.markdown("The app is still under development.")

    # Description of the features
    st.markdown(
        """
        ### Select on the left panel what you want to explore:

        - With 🔭 General info, you will have a short description of what this tool can do and how to use it.
        
        - With 📈CropAssist, you will be able to Upload the drawings and get the dimensions.

        - With 🗺️ DimensionManager, you will be able to get all the detected Dimension organised into the corresponding lengths and widths.
        """
    )

if __name__ == "__main__":
    main()
