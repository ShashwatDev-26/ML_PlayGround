import streamlit as st

def auth():
    if not st.session_state.get("authenticated", False):
        st.error("Please login @ Home page First")
        st.stop()

st.title("Welcome to Model Training Module")
st.write("A hard bolt will screw up how is this metaphor")
st.divider()
auth()