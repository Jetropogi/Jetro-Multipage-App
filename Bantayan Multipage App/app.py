import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="")

st.title("Welcome to my Portfolio")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "About Me", "Skills", "Contacts"])

if page == "Dashboard":
    st.title("🏠 Dashboard")

elif page == "About Me":
    st.title("🙋 About Me")

elif page == "Skills":
    st.title("🎨 Skills")

elif page == "Contacts":
    st.title("📱 Contacts")

st.write("""
Navigate through my portfolio using the sidebar👌

Sections included:
-🏠 Dashboard
-🤓 About Me
-😘 Skills
-📱 Contacts
""")

st.success("Simple Portfolio  Multipage App using Streamlit 🦾")
