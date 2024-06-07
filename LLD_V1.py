import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    st.write("This is a demo software program with some demo modules. "
             "The purpose of the demo is to show the data processing capability of our applications.  \n"
             "  \n"
             "If you need any tailor made software with similar data processing features please contact us.  \n"
             "  \n"
             "")
    selected = option_menu(
        "LLD Modules",[
        "LLD Data",
        "LLD Documentation",
        "LLD Database Update",
        "LLD Database Reports"
        # "path layer"
        ], menu_icon="cast", default_index=0)

if selected == "LLD Data":
    import pandas as pd, zipfile,CDR_functions_old as cdrf
    import pandas as pd
    import numpy as np
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import pydeck as pdk
    import json

    Name = "Barbaros"

    st.title('LLD Database Model')
    st.header('TI Number Reporting')
    st.write("This module is a demo for CDR Statistical Reporting. ")

    st.divider()  # 👈 Draws a horizontal rule
    st.header('LLD Details')

    db_name_read = "JSON_test"  # st.text_input('dB name to read')
    collection_name = "TI_Numbers"

    uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
    cluster = MongoClient(uri, server_api=ServerApi('1'))
    db = cluster[db_name_read]
    collection = db[collection_name]

    all_data_from_db = db[collection_name].find({})
    df_1 = pd.DataFrame(list(all_data_from_db)) # st.write(df_tokyo_mongodb)

    TI_numbers_list = df_1["TI_Number"].to_list()
    TI_Number_to_display = st.selectbox('Please Select The TI Number', TI_numbers_list)

    if st.button("Display TI Number information"):
        # document = collection.find_one({"TI_Number": TI_Number_to_display})
        document = collection.find_one({"TI_Number": TI_Number_to_display}, {"_id": 0, "field_to_exclude": 0})
        # document = collection.find_one({"TI_Number": TI_Number_to_display}, {"_id": 0, "field1": 0, "field2": 0})
        # st.write(document)
        st.json(document, expanded=False)








