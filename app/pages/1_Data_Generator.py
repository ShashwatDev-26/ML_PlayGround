import os,sys
import streamlit as st
Module_path = os.path.join(os.path.dirname(__file__),"..","..","ML_model","src")
sys.path.append(Module_path)
from Import_data import dummyData

st.title("🎲 Data Generation Lab")

if not st.session_state.get("authenticated", False):
    st.error("Please login on the home page.")
    st.stop()

# UI Inputs
col1, col2, col3 = st.columns(3)
s = col1.number_input("Samples", 20, 10000, 100)
f = col2.number_input("Features", 1, 50, 5)
c = col3.number_input("Classes", 0, 10, 2)
fname = st.text_input("Save as:", "Dummy")

if st.button("Generate & Save"):
    engine = dummyData(s, f, c)
    engine.independent_data()
    engine.dependent_data()
    

    save_path,df = engine.export_data(fname)
    st.success(f"File saved @ {save_path}")
    st.dataframe(df.head())