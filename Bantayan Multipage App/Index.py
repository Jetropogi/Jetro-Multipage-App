import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="")

st.title("Welcome to my Portfolio")

st.write("""
Navigate through my portfolio using the sidebar👌

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "About Me", "Skills", "Contacts"])

Sections included:
-🏠 Dashboard
-🤓 About Me
-😘 Skills
-📱 Contacts
""")

st.success("Simple Portfolio  Multipage App using Streamlit 🦾")
