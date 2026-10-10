import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="World Cities App",
    page_icon="🌍",
    layout="wide"
)

# Add title and welcome text
st.title("🌍 Welcome to World Cities")
st.write("Explore cities around the world and discover fascinating information about them.")

# Add a button to navigate to the app page
if st.button("Go to App", key="main_button", use_container_width=True):
    st.switch_page("pages/app.py")

# Optional: Add some additional welcome content
st.markdown("---")
st.subheader("About This App")
st.write("""
This multipage Streamlit application allows you to explore world cities.
Click the button above to get started!
""")
