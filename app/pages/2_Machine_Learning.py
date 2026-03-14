import os,sys
from pathlib import Path
import streamlit as st
Module_path = os.path.join(os.path.dirname(__file__),"..","..","ML_model","src")
sys.path.append(Module_path)
from MLmodels import modelSelection
from Docs import Markdowns

markdowns = Markdowns()

def auth():
    if not st.session_state.get("authenticated", False):
        st.error("Please login @ Home page First")
        st.stop()


# Main File
def dataSelection():
    """
    [Return]
    0 : Path
   """
    Data_path = os.path.join(os.path.dirname(__file__),"..","..","ML_model","Data")

    os.makedirs(Data_path,exist_ok=True)

    file_list = ["-"] + os.listdir(Data_path)
    if len(file_list)==1:
        st.header("Please Creat Dummy DataFrame",anchor=False,text_alignment="justify",divider="gray")
        if st.button("Go to Data_generator",icon="🦋",type="primary"):
            st.switch_page("pages/1_Data_Generator.py")
    else:
        select_file = st.selectbox("Select the file name",file_list,index=0)
        if select_file == "-":
            st.rerun()
        else:
            return os.path.join(Data_path,select_file)
    return Data_path

def modelDetector(filename="-"):
    if not filename == "-":
        modelRecoz = modelSelection(filename)
        modelRecoz.file_and_data()
        modelRecoz.import_Data()
        modelRecoz.model_recognization()
        st.session_state["model_type"] = modelRecoz.model_type
        st.title(f"This is a {modelRecoz.model_type} problem")
        modelRecoz.model_select()
        st.divider()
    else:
        st.rerun()

def select_model_dropdown():
    if st.session_state["model_type"]:
        saved_model = Path(Module_path) / ".." / "saved_model" / st.session_state["model_type"]
        model_list  = saved_model.rglob("*.joblib")
        list_path   = {str(file.stem):file for file in model_list}

        selected_Model_name =    st.selectbox("Choose the model here ",["-"] + list(list_path.keys()),index=0)
        
        if selected_Model_name=="-":
            st.header("🧟‍♀️no-Model is selected yet")
        else:
            st.session_state["selected_path"] = list_path[selected_Model_name]
            st.header(f"🎰 🏇🏻 🤾🏻Go to Trainig Module 🤸🏻‍♂️")
            st.divider()
            st.header("📖 Reading makes coding perfect 📖")
            st.divider()
            st.markdown(markdowns.ML_models(selected_Model_name))
            if st.button(f"_{selected_Model_name}_",icon="⚙️",type="primary"):
                st.switch_page("pages/3_Model_Training.py")
               



st.title("Ⓜ️ Choose Your Machine ")
auth()
data_path = dataSelection()
modelDetector(data_path)
select_model_dropdown()





