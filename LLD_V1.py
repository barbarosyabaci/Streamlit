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
        "LLD Documentation",
        "LLD Database Model",
        "LLD Database Update",
        "LLD Database Reports"
        # "path layer"
        ], menu_icon="cast", default_index=0)

if selected == "LLD Database Model":
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
        # document = collection.find_one({"TI_Number": TI_Number_to_display}).values()
        document = collection.find_one({"TI_Number": TI_Number_to_display})
        # st.table(document)
        # st.write(type(document))
        # st.write(document)

        def display_dict_old(d, level=0):
            if isinstance(d, dict):
                if d:
                    tabs = st.tabs(list(d.keys()))
                    for key, value in d.items():
                        with tabs[list(d.keys()).index(key)]:
                            st.write(f"**{key}:**")
                            if isinstance(value, dict):
                                display_dict(value, level + 1)
                            else:
                                st.write(value)
                else:
                    st.write("Empty dictionary")
            else:
                st.write(d)

        st.divider()
        def display_dict(d, level=0):
            if isinstance(d, dict):
                if d:
                    for key, value in d.items():
                        st.write(f"**{key}:**")
                        if isinstance(value, dict):
                            display_dict(value, level + 1)
                        else:
                            st.write(value)
                else:
                    st.write("Empty dictionary")
            else:
                st.write(d)

        # display_dict(document)
        display_dict_old(document)

        # display_dict(document)

if selected == "CDR Reporting":
    import pandas as pd, zipfile,CDR_functions_old as cdrf

    st.title('CDR Reporting')
    st.header('Drive Test Statistical Report Module - Data')
    st.write("This module is a demo for CDR Statistical Reporting. ")
    uploaded_file = st.file_uploader("Choose input zip file to process", type="zip", accept_multiple_files=True)

    if st.button('Process uploaded files'):

        with zipfile.ZipFile(uploaded_file[0], 'r') as zip_ref:
            csv_file_name = zip_ref.namelist()[0]
            zip_ref.extract(csv_file_name)

        df = pd.read_csv(csv_file_name, low_memory=False).head(100000)

        df_sel = cdrf.data_preprocessing(df)
        df_total_stats = cdrf.calculate_general_stats(df_sel)
        df_sel = cdrf.add_distances(df_sel)
        df_result = cdrf.Calculating_pivot(df_sel)
        merged_df = cdrf.merge_type_table(df_result)
        df_Vdf = cdrf.excel_report(df_total_stats, merged_df)
        cdrf.add_dataframe_excel('template_cdr.xlsx', 'output_file_2.xlsx', 'Vodafone', df_Vdf)

        merged_df.to_csv('Pivot.csv', mode='w', header=True, index=False)
        st.download_button(label="Download Pivot", key=5, data=open('Pivot.csv', 'rb').read(), file_name="Pivot.csv")
        st.download_button(label="Download Excel_report", key=6, data=open('output_file.xlsx', 'rb').read(), file_name='output_file.xlsx')
        st.download_button(label="Download CDR_report_V1", key=7, data=open('output_file_2.xlsx', 'rb').read(), file_name='CDR_V1.xlsx')
        st.dataframe(merged_df)

    st.divider()  # 👈 Draws a horizontal rule
    st.header('Drive Test Statistical Report Module - Voice')
    uploaded_file = st.file_uploader("Choose input zip file to process", type="zip", accept_multiple_files=True,key = 1)
    if st.button('Process uploaded files', key = 2):

        with zipfile.ZipFile(uploaded_file[0], 'r') as zip_ref:
            csv_file_name = zip_ref.namelist()[0]
            zip_ref.extract(csv_file_name)


        # Script start

        # path = "C:/08_2024_DT/HiDrive-CDR/Master Data/O2_CDR_DATA_RATINGEN_20240207/"
        # csv_file_name = path + "Metric Group 1.csv"
        df = pd.read_csv(csv_file_name, low_memory=False)

if selected == "CDR Reports Historical Comparison":
    st.title('Comparison Module for Drive Tests')
    st.header('Drive Test Statistical Report Module')
    st.write("This module is a demo for DR Reports Historical Comparison ")

if selected == "View Historical Reports":
    st.title('Report Module for Historical Drive Tests')
    st.header('Historical Reports viewing Module')
    st.write("This module is a demo for CDR Reports Historical Vieving ")

if selected == "View on Map":
    st.title('Map Module for Historical Drive Tests')
    st.header('Historical Reports Map viewing Module')
    st.write("This module is a demo for CDR Reports Map Vieving ")



    uploaded_file_2 = st.file_uploader("Choose input zip file to process", type="zip", accept_multiple_files=True)

    if st.button('Process uploaded files'):
        import pandas as pd
        import pydeck as pdk
        import zipfile

        with zipfile.ZipFile(uploaded_file_2[0], 'r') as zip_ref:
            csv_file_name = zip_ref.namelist()[0]
            zip_ref.extract(csv_file_name)


        df = pd.read_csv(csv_file_name, low_memory=False).head(50000)

        sel_columns = ["Time", "Date", "Latitude", "Longitude", "Grouping", "Grouping_with_Direction", "Grouping_with_Direction_HTTP", "Grouping_with_Direction_Ping", "Operator", "Task_Type", "Technology", "HTTP_URL", "Streaming_URL", "Ping_Address", "Serving Cell RS SINR (dB)", "Serving Cell RSRP (dBm)", "Serving Cell RSRQ (dB)", "HTTP_Download_Average_Throughput", "HTTP_Download_Service_Average_Throughput", "HTTP_Download_Session_Failure_Ratio", "HTTP_Download_Session_Success_Ratio",
            "HTTP_Outcome", "HTTP_Download_Data_Transfer_Failure_Ratio_Method_A", "HTTP_Download_Data_Transfer_Success_Ratio_Method_A", "HTTP_Download_Data_Transfer_Time_sec_Method_A", "HTTP_Download_IP_Service_Access_Failure_Ratio_Method_A", "HTTP_Download_IP_Service_Setup_Success_Ratio_Method_A", "HTTP_Download_IP_Service_Setup_Time_sec_Method_A", "HTTP_Download_Mean_Data_Rate_kbps_Method_A", "HTTP_Download_Transfer_Start_Delay_Method_A", "HTTP_Download_Data_Transfer_Failure_Ratio_Method_B",
            "HTTP_Download_Data_Transfer_Success_Ratio_Method_B", "HTTP_Download_Data_Transfer_Time_sec_Method_B", "HTTP_Download_IP_Service_Access_Failure_Ratio_Method_B", "HTTP_Download_IP_Service_Setup_Success_Ratio_Method_B", "HTTP_Download_IP_Service_Setup_Time_sec_Method_B", "HTTP_Download_Mean_Data_Rate_kbps_Method_B", "HTTP_Upload_Average_Throughput", "HTTP_Upload_Service_Average_Throughput", "HTTP_Upload_Service_Transfer_Time", "HTTP_Upload_Session_Failure_Ratio",
            "HTTP_Upload_Session_Success_Ratio", "HTTP_Upload_Data_Transfer_Failure_Ratio_Method_A"]

        # for i in sel_columns:
        # print(i)

        df_sel = df[sel_columns]

        # st.write(df_sel.columns)

        lon_cen_1 = df_sel["Longitude"].mean()
        lat_cen_1 = df_sel["Latitude"].mean()

        view_state = pdk.ViewState(latitude=lat_cen_1, longitude=lon_cen_1, zoom=10)

        st.pydeck_chart(pdk.Deck(map_style=None, initial_view_state=view_state,
            layers=[
            pdk.Layer('ScatterplotLayer',
                data=df_sel,
                get_position='[Longitude, Latitude]',
                get_color='[200, 30, 0, 160]',
                pickable=True,
                tooltip=True,
                radiusScale=2,
                radiusMinPixels=2,
                radiusMaxPixels=2) # get_radius=50,
            ],
            # tooltip={"Name: {name}"}
            tooltip={"text": "HTTP_Download_Service_Average_Throughput: {HTTP_Download_Service_Average_Throughput}"}
        ))





