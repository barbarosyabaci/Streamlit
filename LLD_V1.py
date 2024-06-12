import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    st.write("Techbros IO "
             "  \n"
             "  \n"
             "  \n"
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
    # st.header('TI Number Reporting')
    st.write("This module is a demo for TI number database display/management")

    # st.divider()  # 👈 Draws a horizontal rule
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
    TI_Number_to_update = st.selectbox('Please Select The TI Number to update', TI_numbers_listkey = "second")


    if st.button("Display TI Number information"):
        # document = collection.find_one({"TI_Number": TI_Number_to_display})
        document = collection.find_one({"TI_Number": TI_Number_to_display}, {"_id": 0, "field_to_exclude": 0})
        # document = collection.find_one({"TI_Number": TI_Number_to_display}, {"_id": 0, "field1": 0, "field2": 0})
        # st.write(document)
        st.json(document, expanded=False)

    document = collection.find_one({"TI_Number": TI_Number_to_display}, {"_id": 0, "field_to_exclude": 0})
    json_string = json.dumps(document, indent=4)
    st.download_button(label="Download as JSON", data=json_string, file_name=TI_Number_to_display + '.json', mime="application/json")

    import csv
    import io

    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow(document.keys())
    csv_writer.writerow(document.values())
    csv_string = csv_buffer.getvalue()
    csv_buffer.close()

    st.download_button(label="Download as CSV", data=csv_string, file_name=TI_Number_to_display + '.csv', mime="text/csv")

    if st.button("Update information for TI Number as JSON"):
        document_2 = collection.find_one({"TI_Number": TI_Number_to_update},key = "second")






