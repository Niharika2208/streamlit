import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as mpimg

st.set_page_config(
    page_title="Home page",
    page_icon="👋",
    layout="centered")


# SurViZ logo
st.image('logo_ata.png.png')

# Main Description
st.markdown("## 👋 Welcome to the Dimension Detection tool!")
    st.markdown("Developed by the Team Quadratech")
    st.markdown("The app is still under development.")

# Description of the features. 
st.markdown(
        """
        ### Select on the left panel what you want to explore:

        - With 🔭 General info, you will have a short description of what this tool can do and how to use it.
        
        - With 📈CropAssist, you will be able to Upload the drawings and get the dimensions.

        - With 🗺️ DimensionManager, you will be able to get all the detected Dimension organised into the corresponding lengths and widths.
         """

)
