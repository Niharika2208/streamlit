
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib.image as mpimg

st.set_page_config(
    page_title="Home page",
    page_icon="👋",
    layout="centered")


# SurViZ logo
#st.image('surviz_black_long.png')

# Main Description
st.markdown("## 👋 Welcome to the Dimension Detection tool!")
st.markdown("Developed by the Team Quadratech")
st.markdown("The app is still under development.")

# Description of the features. 
st.markdown(
    """
    ### Select on the left panel what you want to explore:

    - With 🔭 General info, you will have a short description of what this tool can do and how to use it.
    
    - With 🎨 Filters, you will explore the spectral bands of each telescopes' instruments.

    - With 👁️ FOV, you will be able to explore the Field of View of each telescope.

    - With 📈characteristics, you will explore the capacity of the missions regarding filters, resolution and depth.
    
    - With 🌌 Galaxy, you will explore the surveys and instruments' image quality (resolution and PSF) in a TNG galaxy.

    - With ✨ Galaxy fields, you will explore the surveys and instruments' depths in a simulated galaxy field.

    - With 🗺️ Survey footprint, you will visualise the sizes and positions of the various surveys.

    - With 🪞 Mirror , you will explore the size of the telescopes' primary mirror.
    \n  
    
    More information can be found by clicking in the READMEs of each tab.
    """
)

# Mission logos
st.image('data/logos/logos.jpeg')
