import streamlit as st

def main():
    st.title("Dimension Manager")
    st.write("This is the Dimension Manager page.")
    dimensions = st.sidebar.multiselect(
    "Select the Dimension",
     ["Length", "Width"]
    )

if __name__ == "__main__":
    main()
