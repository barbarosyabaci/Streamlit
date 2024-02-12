import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    st.write("This is a demo software program with some demo modules. "
             "The purpose of the demo is to show the data processing capability of our applications.  \n"
             "  \n"
             "If you need any tailor made software with similar data processing features please contact us.  \n"
             "  \n"
             "")
    selected = option_menu("RAN Modules",[
        "CDR Reporting",
        "CDR Reports Historical Comparison",
        "View Historical Reports",
        "View on Map",
        # "path layer"
        ], menu_icon="cast", default_index=0)

if selected == "CDR Reporting":
    import pandas as pd
    import webbrowser
    import numpy as np
    import zipfile

    st.title('CDR Reporting')
    st.header('Drive Test Statistical Report Module')
    st.write("This module is a demo for CDR Statistical Reporting. ")



    uploaded_file = st.file_uploader("Choose input zip file to process", type="zip", accept_multiple_files=True)

    if st.button('Process uploaded files'):
        path = "C:/08_2024_DT/HiDrive-CDR/Master Data/O2_CDR_DATA_RATINGEN_20240207/"
        file_name = "Metric Group 1.zip"
        csv_file_name = "Metric Group 1.csv"

        with zipfile.ZipFile(uploaded_file[0], 'r') as zip_ref:
            zip_ref.extract(csv_file_name)

        df = pd.read_csv(csv_file_name, low_memory=False)

        sel_columns = pd.read_csv("Columns_to_select.csv")["Columns_to_select"].tolist()
        df_sel = df[sel_columns]

        # Function to concatenate non-NaN values of specific columns
        def combine_values(row, columns_to_combine):
            combined_values = ''.join(str(row[column]) for column in columns_to_combine if pd.notna(row[column]))
            return combined_values if combined_values else np.nan

        columns_to_combine = ["HTTP_URL", "Streaming_URL", "Ping_Address"]

        df_sel['CombinedColumn'] = df_sel.apply(lambda row: combine_values(row, columns_to_combine), axis=1)

        n_e_r = df_sel.index[df_sel['Ping_Address'].notna()].tolist() + [len(df_sel)]  # n_e_r = non empty rows on ping address
        labels = list(range(1, len(n_e_r) + 1))
        df_sel['Session_ID'] = pd.cut(df_sel.index, bins=[0] + n_e_r, labels=labels, right=False)

        n_e_r_2 = df_sel.index[df_sel['CombinedColumn'].notna()].tolist() + [len(df_sel)]  # n_e_r_2 = non empty rows combined column
        labels_2 = list(range(1, len(n_e_r_2) + 1))

        labels_3 = ["8.8.8.8"] + list(df_sel.loc[n_e_r_2[:-1], 'CombinedColumn'])

        df_sel['Test_ID'] = pd.cut(df_sel.index, bins=[0] + n_e_r_2, labels=labels_2, right=False)
        df_sel['Test_type'] = pd.cut(df_sel.index, bins=[0] + n_e_r_2, labels=labels_3, right=False, ordered=False)

        df_rep = pd.read_csv("Test_type.csv")
        my_dict = dict(zip(df_rep.iloc[:, 0], df_rep.iloc[:, 1]))

        df_sel['Test_type'] = df_sel['Test_type'].replace(my_dict)

        new_column_order = pd.read_csv("Columns_order.csv")["Order"].tolist()
        df_rd = df_sel[new_column_order]

        # Filtering rows based on a condition (e.g., age greater than 25)
        filtered_rows = df_rd.loc[df_rd['Test_ID'] == 2]

        df_agg = pd.read_csv("Columns_to_report_functions.csv")
        agg_columns = df_agg.iloc[:, 0].tolist()
        agg_funcs = df_agg.iloc[:, 1].tolist()
        values = [list(map(str, element.split(','))) for element in agg_funcs]
        result_list = dict(zip(agg_columns, values))

        columns_agg = ["Serving Cell RS SINR (dB)", "Serving Cell RSRP (dBm)", "Serving Cell RSRQ (dB)", "HTTP_Download_Average_Throughput", "HTTP_Download_Service_Average_Throughput", "HTTP_Download_Session_Failure_Ratio", "HTTP_Download_Session_Success_Ratio", "HTTP_Upload_Average_Throughput", "HTTP_Upload_Service_Average_Throughput", "HTTP_Upload_Session_Failure_Ratio", "HTTP_Upload_Session_Success_Ratio", "Streaming_Average_Throughput", "Streaming_Session_Failure_Ratio",
            "Streaming_Success_Rate"]
        agg_func = (
        {'Serving Cell RS SINR (dB)': ['mean','sum'], 'Serving Cell RSRP (dBm)': ['mean'], "Serving Cell RSRQ (dB)": 'mean', "HTTP_Download_Average_Throughput": 'mean', "HTTP_Download_Service_Average_Throughput": 'mean', "HTTP_Download_Session_Failure_Ratio": 'mean', "HTTP_Download_Session_Success_Ratio": 'mean', "HTTP_Upload_Average_Throughput": 'mean', "HTTP_Upload_Service_Average_Throughput": 'mean', "HTTP_Upload_Session_Failure_Ratio": 'mean', "HTTP_Upload_Session_Success_Ratio": 'mean',
            "Streaming_Average_Throughput": 'mean', "Streaming_Session_Failure_Ratio": 'mean', "Streaming_Success_Rate": 'mean'})

        # Using pivot_table to calculate multiple columns for the filtered rows
        pivot_result = pd.pivot_table(df_rd, index=["Session_ID","Test_ID","Test_type"], values=agg_columns, aggfunc=result_list)
        df_pivot_pre = pivot_result.reset_index()

        new_column_order_2 = ['Test_ID', 'Test_type', 'Serving Cell RS SINR (dB)', 'Serving Cell RSRP (dBm)', 'Serving Cell RSRQ (dB)', 'HTTP_Download_Average_Throughput', 'HTTP_Download_Service_Average_Throughput', 'HTTP_Download_Session_Failure_Ratio', 'HTTP_Download_Session_Success_Ratio', 'HTTP_Upload_Average_Throughput', 'HTTP_Upload_Service_Average_Throughput', 'HTTP_Upload_Session_Failure_Ratio', 'HTTP_Upload_Session_Success_Ratio', 'Streaming_Average_Throughput',
            'Streaming_Session_Failure_Ratio', 'Streaming_Success_Rate']

        # df_pivot = df_pivot_pre[new_column_order_2]

        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=False).encode('utf-8')

        try:
            df_pivot_pre.to_csv('Aggregate_Results.csv', mode='w', header=True, index=False)
            # webbrowser.open("Aggregate_Results.csv")
            df_rd.to_csv('Selected_Metrics.csv', mode='w', header=True, index=False)
            csv = convert_df(df_pivot_pre)
            st.download_button(label="Download Result File", data=csv, file_name="Aggregate_Results.csv", mime='text/csv')
            st.dataframe(df_pivot_pre)
            # webbrowser.open("Selected_Metrics.csv")
        except:
            print("Cannot export: files are already open")





    st.divider()  # 👈 Draws a horizontal rule

    st.header('Report Statistics')

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
