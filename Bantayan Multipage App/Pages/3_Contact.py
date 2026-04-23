import streamlit as st

st.title("Contact")

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Message")

if st.button("Send"):
    st.success("Message sent!")