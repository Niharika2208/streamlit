import streamlit as st

def main():
    st.title("Crop Assist")
    st.write("This is the Crop Assist page.")
    dimensions = st.sidebar.multiselect(
    "Select the Dimension",
     ["Length", "Width"]
    )

if __name__ == "__main__":
    main()
