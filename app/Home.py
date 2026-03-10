import streamlit as st

st.set_page_config(page_title="AutoML Platform", layout="centered")


def logout():
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

def login():
    st.title("🔐 Login")
    user = st.text_input("Username")
    pw   = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if user == "root" and pw == "toor": # Change these!
            st.session_state["authenticated"] = True
            st.success("Logged in! Use the sidebar to navigate.")
            st.rerun()
        else:
            st.error("Invalid credentials")



if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    st.title("Welcome to the AutoML Suite")
    st.write("Use the sidebar on the left to generate dummy data or run AutoML.")
    logout()