import streamlit as st

st.set_page_config(layout="wide")

st.title("📊 Interactive Dashboard")


menu = st.sidebar.selectbox("Menu", ["Home", "Profile", "Settings"])

if menu == "Home":
    st.subheader("Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Users", "120")
    col2.metric("Tasks", "75")
    col3.metric("Progress", "60%")

    if st.button("Refresh Data"):
        st.success("Data refreshed!")

elif menu == "Profile":
    st.subheader("User Profile")

    name = st.text_input("Name")
    role = st.selectbox("Role", ["Student", "Developer", "Designer"])

    if st.button("Save Profile"):
        st.success(f"Saved! Hello {name}")


elif menu == "Settings":
    st.subheader("Settings")

    dark_mode = st.toggle("Dark Mode")
    notifications = st.checkbox("Enable Notifications")

    st.write("Dark Mode:", dark_mode)
    st.write("Notifications:", notifications)