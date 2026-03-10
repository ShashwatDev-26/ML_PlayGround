import os,sys
from pathlib import Path
import streamlit as st
Module_path = os.path.join(os.path.dirname(__file__),"..","..","ML_model","src")
sys.path.append(Module_path)
from MLmodels import modelSelection

def auth():
    if not st.session_state.get("authenticated", False):
        st.error("Please login on the home page.")
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

def select_model_dropdown():
    if st.session_state["model_type"]:
        saved_model = Path(Module_path) / ".." / "saved_model" / st.session_state["model_type"]
        model_list  = saved_model.rglob("*.joblib")
        list_path   = {file:str(file.stem) for file in model_list}
        st.selectbox("Choose the model here ",list_path.values(),index=0)
   



st.title("Ⓜ️ Choose your ML lab")
auth()
data_path = dataSelection()

modelDetector(data_path)
select_model_dropdown()





