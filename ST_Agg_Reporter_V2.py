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
    st.header('Drive Test Statistical Report Module - Data')
    st.write("This module is a demo for CDR Statistical Reporting. ")


    uploaded_file = st.file_uploader("Choose input zip file to process", type="zip", accept_multiple_files=True)

    if st.button('Process uploaded files'):

        with zipfile.ZipFile(uploaded_file[0], 'r') as zip_ref:
            csv_file_name = zip_ref.namelist()[0]
            zip_ref.extract(csv_file_name)


        # Script start

        # path = "C:/08_2024_DT/HiDrive-CDR/Master Data/O2_CDR_DATA_RATINGEN_20240207/"
        # csv_file_name = path + "Metric Group 1.csv"
        df = pd.read_csv(csv_file_name, low_memory=False).head(100000)

        sel_columns = ["Time", "Date", "Latitude", "Longitude", "Grouping", "Grouping_with_Direction", "Grouping_with_Direction_HTTP", "Grouping_with_Direction_Ping", "Operator", "Task_Type", "Technology", "HTTP_URL", "Streaming_URL", "Ping_Address", "Serving Cell RS SINR (dB)", "Serving Cell RSRP (dBm)", "Serving Cell RSRQ (dB)", "HTTP_Download_Average_Throughput", "HTTP_Download_Service_Average_Throughput", "HTTP_Download_Session_Failure_Ratio", "HTTP_Download_Session_Success_Ratio",
            "HTTP_Outcome", "HTTP_Download_Data_Transfer_Failure_Ratio_Method_A", "HTTP_Download_Data_Transfer_Success_Ratio_Method_A", "HTTP_Download_Data_Transfer_Time_sec_Method_A", "HTTP_Download_IP_Service_Access_Failure_Ratio_Method_A", "HTTP_Download_IP_Service_Setup_Success_Ratio_Method_A", "HTTP_Download_IP_Service_Setup_Time_sec_Method_A", "HTTP_Download_Mean_Data_Rate_kbps_Method_A", "HTTP_Download_Transfer_Start_Delay_Method_A", "HTTP_Download_Data_Transfer_Failure_Ratio_Method_B",
            "HTTP_Download_Data_Transfer_Success_Ratio_Method_B", "HTTP_Download_Data_Transfer_Time_sec_Method_B", "HTTP_Download_IP_Service_Access_Failure_Ratio_Method_B", "HTTP_Download_IP_Service_Setup_Success_Ratio_Method_B", "HTTP_Download_IP_Service_Setup_Time_sec_Method_B", "HTTP_Download_Mean_Data_Rate_kbps_Method_B", "HTTP_Upload_Average_Throughput", "HTTP_Upload_Service_Average_Throughput", "HTTP_Upload_Service_Transfer_Time", "HTTP_Upload_Session_Failure_Ratio",
            "HTTP_Upload_Session_Success_Ratio", "HTTP_Upload_Data_Transfer_Failure_Ratio_Method_A", "HTTP_Upload_Data_Transfer_Success_Ratio_Method_A", "HTTP_Upload_Data_Transfer_Time_sec_Method_A", "HTTP_Upload_IP_Service_Access_Failure_Ratio_Method_A", "HTTP_Upload_IP_Service_Setup_Success_Ratio_Method_A", "HTTP_Upload_IP_Service_Setup_Time_sec_Method_A", "HTTP_Upload_Mean_Data_Rate_kbps_Method_A", "Streaming_Outcome_Type", "Aborted_by_User", "Streaming_Average_Session_Resolution",
            "Streaming_Average_Throughput", "Streaming_Completion_Rate", "Streaming_Duration", "Streaming_HD_Resolution", "Streaming_HD_Resolution_Ratio", "Streaming_Impairment_Free", "Streaming_Impairment_Free_Video_Session_Ratio", "Streaming_Maximum_Duration_Of_Video_Session_Interruptions", "Streaming_Number_Of_Video_Session_Interruptions", "Streaming_Player_Size_kB", "Streaming_Reproduction_Cutoff_Ratio", "Streaming_Reproduction_Start_Delay_sec", "Streaming_Reproduction_Start_Failure_Ratio",
            "Streaming_Service_Access_Time_ms", "Streaming_Service_Access_Time_sec", "Streaming_Session_Failure_Ratio", "Streaming_Session_Qualified", "Streaming_Session_Qualified_Ratio", "Streaming_Session_Video_Interruption_Duration", "Streaming_Session_Without_Interruption_Rate", "Streaming_Setup_Success_Rate", "Streaming_State_Prebuffering_to_Reproducing_Delay", "Streaming_State_Request_to_Prebuffering_Delay", "Streaming_State_Request_to_Reproducing_Delay", "Streaming_Success_Rate",
            "Streaming_Throughput_Filtered", "Streaming_Total_Duration_Of_Video_Session_Interruptions", "Streaming_Video_Buffer_Size_kB", "Streaming_Video_IP_Service_Access_Time_ms", "Streaming_Video_IP_Service_Access_Time_sec", "Streaming_Video_Play_Start_Failure_Ratio", "Streaming_Video_Play_Start_Time_sec", "Streaming_Video_Session_Cutoff_Ratio", "Streaming_Video_Session_Failure_Ratio", "Streaming_Video_Session_Success_Ratio", "Streaming_Video_Session_Time_sec", "Streaming_Video_Size_kB",
            "SessionTime", "SessionTime_Upload", "ThroughputCountOver1MBit", "ThroughputCountOver3MBit", "ThroughputPercentageOver3MBit", "TCP_Handshake_Time_sec", "Ping_Count_Attempts", "Ping_Count_Failed", "Ping_Count_Success", "Ping_Delay_ms_Avg", "Ping_Delay_ms_Max", "Ping_Delay_ms_Min", "Ping_Packet_Loss_Rate", "Ping_Packet_Success_Rate", "Ping_Roundtrip_Time_ms", "Ping_Roundtrip_Time_sec", "Ping_Size", "Data_Radio_Bearer", "Fixed_Duration", "IP_Interruption_Time_ms", "Is_Multi_RAB",
            "LTE_Serving_Cell_Count_Average", "Radio_Access_Technology", "Service_Bearer", "FTP_Download_Average_Throughput_Not_Completed_Session", "FTP_Download_Bearer", "FTP_Download_Error_Cause", "FTP_Download_Outcome", "FTP_Download_Session_Failure_Ratio", "FTP_Download_Session_Success_Ratio", "FTP_Server_File", "Seconds_Start_to_End_FTP_Download", "FTP_Download_Data_Transfer_Cutoff_Ratio_Method_A", "FTP_Download_Data_Transfer_Success_Ratio_Method_A",
            "FTP_Download_IP_Service_Access_Failure_Ratio_Method_A", "FTP_Download_IP_Service_Setup_Success_Ratio_Method_A", "FTP_Download_IP_Service_Setup_Time_sec_Method_A", "FTP_Download_Transfer_Start_Delay_Method_A", "FTP_Download_Data_Transfer_Cutoff_Ratio_Method_B", "FTP_Download_Data_Transfer_Success_Ratio_Method_B", "FTP_Download_IP_Service_Access_Failure_Ratio_Method_B", "FTP_Download_IP_Service_Setup_Success_Ratio_Method_B", "FTP_Download_IP_Service_Setup_Time_sec_Method_B",
            "Seconds_Start_to_End_FTP_Upload", "FTP_Upload_Bearer", "FTP_Upload_Outcome", "FTP_Upload_IP_Service_Access_Failure_Ratio_Method_A", "FTP_Upload_IP_Service_Setup_Success_Ratio_Method_A", "FTP_Upload_IP_Service_Setup_Time_sec_Method_A", "FTP_Upload_Transfer_Start_Delay_Method_A", "FTP_Upload_IP_Service_Access_Failure_Ratio_Method_B", "FTP_Upload_IP_Service_Setup_Success_Ratio_Method_B", "FTP_Upload_IP_Service_Setup_Time_sec_Method_B", "Seconds_Start_to_End_UDP_Download",
            "UDP_Download_Error_Cause", "Seconds_Start_to_End_UDP_Upload", "UDP_Upload_Error_Cause", "DNS_Client", "DNS_Domain_Name", "DNS_First_In_Session", "DNS_Host_Name_Resolution_Failure_Ratio", "DNS_Host_Name_Resolution_Time_sec", "DNS_Host_Name_Total_Resolution_Time_sec", "DNS_Resolved_Address", "DNS_Server_Address"]
        # for i in sel_columns:
        # print(i)

        df_sel = df[sel_columns]

        # Combining 3 columns to determinte test ID's
        columns_to_combine = ["HTTP_URL", "Streaming_URL", "Ping_Address"]

        # df_sel['CombinedColumn'] = df_sel[columns_to_combine].apply(lambda row: ' '.join(str(value) for value in row if pd.notna(value)), axis=1)
        df_sel.loc[:, 'CombinedColumn'] = df_sel[columns_to_combine].apply(lambda row: ' '.join(str(value) for value in row if pd.notna(value)), axis=1)
        df_sel.loc[df_sel['CombinedColumn'] == '', 'CombinedColumn'] = np.nan

        # Calculating Session ID's
        n_e_r = df_sel.index[df_sel['Ping_Address'].notna()].tolist() + [len(df_sel)]  # n_e_r = non empty rows on ping address
        labels = list(range(1, len(n_e_r) + 1))  # Numbering Session ID's
        df_sel['Session_ID'] = pd.cut(df_sel.index, bins=[0] + n_e_r, labels=labels, right=False)

        # Calculating Test ID's
        n_e_r_2 = df_sel.index[df_sel['CombinedColumn'].notna()].tolist() + [len(df_sel)]  # n_e_r_2 = non empty rows combined column
        labels_2 = list(range(1, len(n_e_r_2) + 1))  # Numbering test id's
        labels_3 = ["8.8.8.8"] + list(df_sel.loc[n_e_r_2[:-1], 'CombinedColumn'])  # First test comes from an empty row so 8.8.8.8 added
        df_sel['Test_ID'] = pd.cut(df_sel.index, bins=[0] + n_e_r_2, labels=labels_2, right=False)

        # Test Types are same as test numbering
        df_sel['Test_type'] = pd.cut(df_sel.index, bins=[0] + n_e_r_2, labels=labels_3, right=False, ordered=False)

        # Changing test type names
        my_dict = {"8.8.8.8": "PING", "URI: https://ash-speed.hetzner.com/1GB.bin": "FDTT http DL MT", "URI: http://d26kjwdsl72dzf.cloudfront.net/upload": "FDTT http UL MT", "URI: https://www.google.de/": "Google.de", "URI: http://press21deq5.s3.dualstack.eu-central-1.amazonaws.com/Kepler_mobile/index.html": "Kepler", "URI: https://www.gmx.net/": "gmx.de", "URI: https://de.m.wikipedia.org/wiki/Europa": "Wikipedia", "URI: https://www.chip.de/": "Chip.de",
            "Source Uri: https://www.youtube.com/watch?v=BQwC_DJSdfE": "youtube", "URI: https://www.instagram.com/": "instagram", "URI: https://www.amazon.de/": "Amazon.de", "URI: http://212.183.159.230/5MB.zip": "FDFS http DL ST", "URI: http://press21deq5.s3.dualstack.eu-central-1.amazonaws.com/upload/": "FDFS http UL ST", }
        df_sel['Test_type'] = df_sel['Test_type'].replace(my_dict)

        Total_Stats = {}

        FDFS_DL_Attempts = df_sel['HTTP_Outcome'].count()
        Total_Stats.update({"FDFS_DL_Attempts": FDFS_DL_Attempts})
        FDFS_DL_Success = len(df_sel[df_sel['HTTP_Outcome'] == 'Service Status: Succeeded'])
        Total_Stats.update({"FDFS_DL_Success": FDFS_DL_Success})
        FDFS_DL_Failure = len(df_sel[df_sel['HTTP_Outcome'] == 'Service Status: Failed'])
        Total_Stats.update({"FDFS_DL_Failure": FDFS_DL_Failure})
        FDFS_DL_Success_Ratio = "{:.2%}".format(FDFS_DL_Success / FDFS_DL_Attempts)
        Total_Stats.update({"FDFS_DL_Success_Ratio": FDFS_DL_Success_Ratio})
        FDFS_UL_Attempts = df_sel['HTTP_Upload_Session_Success_Ratio'].count()
        Total_Stats.update({"FDFS_UL_Attempts": FDFS_UL_Attempts})
        FDFS_UL_Success = len(df_sel[df_sel['HTTP_Upload_Session_Success_Ratio'] == 100])
        Total_Stats.update({"FDFS_UL_Success": FDFS_UL_Success})
        FDFS_UL_Failure = len(df_sel[df_sel['HTTP_Upload_Session_Success_Ratio'] == 0])
        Total_Stats.update({"FDFS_UL_Failure": FDFS_UL_Failure})
        FDFS_UL_Success_Ratio = "{:.2%}".format(FDFS_UL_Failure / FDFS_UL_Attempts)
        Total_Stats.update({"FDFS_UL_Success_Ratio": FDFS_UL_Success_Ratio})

        df_total_stats = pd.DataFrame(list(Total_Stats.items()), columns=['Statistic', 'Value'])
        print(df_total_stats)

        agg_str = lambda x: ','.join(filter(lambda s: pd.notna(s), x))

        agg_list = {'CombinedColumn': agg_str, 'Serving Cell RS SINR (dB)': 'mean', 'Serving Cell RSRP (dBm)': 'mean', 'Serving Cell RSRQ (dB)': 'mean', 'HTTP_URL': agg_str, 'HTTP_Download_Average_Throughput': 'mean', 'HTTP_Download_Service_Average_Throughput': 'mean', 'HTTP_Download_Session_Failure_Ratio': 'mean', 'HTTP_Download_Session_Success_Ratio': 'mean', 'HTTP_Outcome': agg_str, "HTTP_Download_Data_Transfer_Failure_Ratio_Method_A": 'mean',
            "HTTP_Download_Data_Transfer_Success_Ratio_Method_A": 'mean', "HTTP_Download_Data_Transfer_Time_sec_Method_A": 'mean', "HTTP_Download_IP_Service_Access_Failure_Ratio_Method_A": 'mean', "HTTP_Download_IP_Service_Setup_Success_Ratio_Method_A": 'mean', "HTTP_Download_IP_Service_Setup_Time_sec_Method_A": 'mean', "HTTP_Download_Mean_Data_Rate_kbps_Method_A": 'mean', "HTTP_Download_Transfer_Start_Delay_Method_A": 'mean', "HTTP_Download_Data_Transfer_Failure_Ratio_Method_B": 'mean',
            "HTTP_Download_Data_Transfer_Success_Ratio_Method_B": 'mean', "HTTP_Download_Data_Transfer_Time_sec_Method_B": 'mean', "HTTP_Download_IP_Service_Access_Failure_Ratio_Method_B": 'mean', "HTTP_Download_IP_Service_Setup_Success_Ratio_Method_B": 'mean', "HTTP_Download_IP_Service_Setup_Time_sec_Method_B": 'mean', "HTTP_Download_Mean_Data_Rate_kbps_Method_B": 'mean', "HTTP_Upload_Average_Throughput": 'mean', "HTTP_Upload_Service_Average_Throughput": 'mean',
            "HTTP_Upload_Service_Transfer_Time": 'mean', "HTTP_Upload_Session_Failure_Ratio": 'mean', "HTTP_Upload_Session_Success_Ratio": 'mean', "HTTP_Upload_Data_Transfer_Failure_Ratio_Method_A": 'mean', "HTTP_Upload_Data_Transfer_Success_Ratio_Method_A": 'mean', "HTTP_Upload_Data_Transfer_Time_sec_Method_A": 'mean', "HTTP_Upload_IP_Service_Access_Failure_Ratio_Method_A": 'mean', "HTTP_Upload_IP_Service_Setup_Success_Ratio_Method_A": 'mean',
            "HTTP_Upload_IP_Service_Setup_Time_sec_Method_A": 'mean', "HTTP_Upload_Mean_Data_Rate_kbps_Method_A": 'mean', "Streaming_URL": agg_str, "Streaming_Outcome_Type": agg_str, "Aborted_by_User": 'mean', "Streaming_Average_Session_Resolution": 'mean', "Streaming_Average_Throughput": 'mean', "Streaming_Completion_Rate": 'mean', "Streaming_Duration": 'mean', "Streaming_HD_Resolution": agg_str, "Streaming_HD_Resolution_Ratio": 'mean', "Streaming_Impairment_Free": agg_str,
            "Streaming_Impairment_Free_Video_Session_Ratio": 'mean', "Streaming_Maximum_Duration_Of_Video_Session_Interruptions": 'mean', "Streaming_Number_Of_Video_Session_Interruptions": 'mean', "Streaming_Player_Size_kB": 'mean', "Streaming_Reproduction_Cutoff_Ratio": 'mean', "Streaming_Reproduction_Start_Delay_sec": 'mean', "Streaming_Reproduction_Start_Failure_Ratio": 'mean', "Streaming_Service_Access_Time_ms": 'mean', "Streaming_Service_Access_Time_sec": 'mean',
            "Streaming_Session_Failure_Ratio": 'mean', "Streaming_Session_Qualified": agg_str, "Streaming_Session_Qualified_Ratio": 'mean', "Streaming_Session_Video_Interruption_Duration": 'mean', "Streaming_Session_Without_Interruption_Rate": 'mean', "Streaming_Setup_Success_Rate": 'mean', "Streaming_State_Prebuffering_to_Reproducing_Delay": 'mean', "Streaming_State_Request_to_Prebuffering_Delay": 'mean', "Streaming_State_Request_to_Reproducing_Delay": 'mean', "Streaming_Success_Rate": 'mean',
            "Streaming_Throughput_Filtered": 'mean', "Streaming_Total_Duration_Of_Video_Session_Interruptions": 'mean', "Streaming_Video_Buffer_Size_kB": 'mean', "Streaming_Video_IP_Service_Access_Time_ms": 'mean', "Streaming_Video_IP_Service_Access_Time_sec": 'mean', "Streaming_Video_Play_Start_Failure_Ratio": 'mean', "Streaming_Video_Play_Start_Time_sec": 'mean', "Streaming_Video_Session_Cutoff_Ratio": 'mean', "Streaming_Video_Session_Failure_Ratio": 'mean',
            "Streaming_Video_Session_Success_Ratio": 'mean', "Streaming_Video_Session_Time_sec": 'mean', "Streaming_Video_Size_kB": 'mean', "SessionTime": 'mean', "SessionTime_Upload": 'mean', "ThroughputCountOver1MBit": 'mean', "ThroughputCountOver3MBit": 'mean', "ThroughputPercentageOver3MBit": 'mean', "TCP_Handshake_Time_sec": 'mean', "Ping_Address": agg_str, "Ping_Count_Attempts": 'mean', "Ping_Count_Failed": 'mean', "Ping_Count_Success": 'mean', "Ping_Delay_ms_Avg": 'mean',
            "Ping_Delay_ms_Max": 'mean', "Ping_Delay_ms_Min": 'mean', "Ping_Packet_Loss_Rate": 'mean', "Ping_Packet_Success_Rate": 'mean', "Ping_Roundtrip_Time_ms": 'mean', "Ping_Roundtrip_Time_sec": 'mean', "Ping_Size": 'mean', "Data_Radio_Bearer": agg_str, "Fixed_Duration": 'mean', "IP_Interruption_Time_ms": 'mean', "Is_Multi_RAB": agg_str, "LTE_Serving_Cell_Count_Average": 'mean', "Radio_Access_Technology": agg_str, "Service_Bearer": agg_str,
            "FTP_Download_Average_Throughput_Not_Completed_Session": 'mean', "FTP_Download_Bearer": agg_str, "FTP_Download_Error_Cause": 'mean', "FTP_Download_Outcome": 'mean', "FTP_Download_Session_Failure_Ratio": 'mean', "FTP_Download_Session_Success_Ratio": 'mean', "FTP_Server_File": agg_str, "Seconds_Start_to_End_FTP_Download": 'mean', "FTP_Download_Data_Transfer_Cutoff_Ratio_Method_A": 'mean', "FTP_Download_Data_Transfer_Success_Ratio_Method_A": 'mean',
            "FTP_Download_IP_Service_Access_Failure_Ratio_Method_A": 'mean', "FTP_Download_IP_Service_Setup_Success_Ratio_Method_A": 'mean', "FTP_Download_IP_Service_Setup_Time_sec_Method_A": 'mean', "FTP_Download_Transfer_Start_Delay_Method_A": 'mean', "FTP_Download_Data_Transfer_Cutoff_Ratio_Method_B": 'mean', "FTP_Download_Data_Transfer_Success_Ratio_Method_B": 'mean', "FTP_Download_IP_Service_Access_Failure_Ratio_Method_B": 'mean',
            "FTP_Download_IP_Service_Setup_Success_Ratio_Method_B": 'mean', "FTP_Download_IP_Service_Setup_Time_sec_Method_B": 'mean', "Seconds_Start_to_End_FTP_Upload": 'mean', "FTP_Upload_Bearer": agg_str, "FTP_Upload_Outcome": agg_str, "FTP_Upload_IP_Service_Access_Failure_Ratio_Method_A": 'mean', "FTP_Upload_IP_Service_Setup_Success_Ratio_Method_A": 'mean', "FTP_Upload_IP_Service_Setup_Time_sec_Method_A": 'mean', "FTP_Upload_Transfer_Start_Delay_Method_A": 'mean',
            "FTP_Upload_IP_Service_Access_Failure_Ratio_Method_B": 'mean', "FTP_Upload_IP_Service_Setup_Success_Ratio_Method_B": 'mean', "FTP_Upload_IP_Service_Setup_Time_sec_Method_B": 'mean', "Seconds_Start_to_End_UDP_Download": 'mean', "UDP_Download_Error_Cause": agg_str, "Seconds_Start_to_End_UDP_Upload": 'mean', "UDP_Upload_Error_Cause": agg_str, "DNS_Client": agg_str, "DNS_Domain_Name": agg_str, "DNS_First_In_Session": agg_str, "DNS_Host_Name_Resolution_Failure_Ratio": 'mean',
            "DNS_Host_Name_Resolution_Time_sec": 'mean', "DNS_Host_Name_Total_Resolution_Time_sec": 'mean', "DNS_Resolved_Address": agg_str, "DNS_Server_Address": agg_str}

        # for i in list(agg_list.keys()):
        # print(i)

        pivot_result = pd.pivot_table(df_sel, index=["Session_ID", "Test_ID", "Test_type"], values=list(agg_list.keys()), aggfunc=agg_list)
        df_pivot = pivot_result.reset_index()


        def clear_duplicate_values_in_cell(cell_value):
            values = cell_value.split(',')
            unique_values = list(set(values))
            return ','.join(unique_values)


        def clear_duplicate_values_in_column(dataframe, column_name):
            df_copy = dataframe.copy()
            df_copy[column_name] = df_copy[column_name].apply(clear_duplicate_values_in_cell)
            return df_copy


        str_metrics = ["HTTP_URL", "HTTP_Outcome", "Streaming_URL", "Streaming_Outcome_Type", "Streaming_HD_Resolution", "Streaming_Impairment_Free", "Streaming_Session_Qualified", "Ping_Address", "Data_Radio_Bearer", "Is_Multi_RAB", "Radio_Access_Technology", "Service_Bearer", "FTP_Download_Bearer", "FTP_Server_File", "FTP_Upload_Bearer", "FTP_Upload_Outcome", "UDP_Download_Error_Cause", "UDP_Upload_Error_Cause", "DNS_Client", "DNS_Domain_Name", "DNS_First_In_Session", "DNS_Resolved_Address",
            "DNS_Server_Address"]

        df_result = clear_duplicate_values_in_column(df_pivot, "DNS_Client")
        df_result = clear_duplicate_values_in_column(df_result, "DNS_Domain_Name")
        df_result = clear_duplicate_values_in_column(df_result, "DNS_Resolved_Address")
        df_result = clear_duplicate_values_in_column(df_result, "DNS_Server_Address")
        df_result = clear_duplicate_values_in_column(df_result, "CombinedColumn")

        df_result = df_result.rename(columns={'CombinedColumn': 'Grouping_All_URL'})

        Grouping_All_Url = ["8.8.8.8", "Source Uri: https://www.youtube.com/watch?v=BQwC_DJSdfE", "URI: http://212.183.159.230/5MB.zip", "URI: http://d26kjwdsl72dzf.cloudfront.net/upload", "URI: http://press21deq5.s3.dualstack.eu-central-1.amazonaws.com/Kepler_mobile/index.html", "URI: http://press21deq5.s3.dualstack.eu-central-1.amazonaws.com/upload/", "URI: https://ash-speed.hetzner.com/1GB.bin", "URI: https://de.m.wikipedia.org/wiki/Europa", "URI: https://www.amazon.de/",
            "URI: https://www.chip.de/", "URI: https://www.gmx.net/", "URI: https://www.google.de/", "URI: https://www.instagram.com/"]
        Direction_Test = ["PING", "DL", "DL", "UL", "DL", "UL", "DL", "DL", "DL", "DL", "DL", "DL", "DL"]
        Test_Name = ["PING", "Streaming YT", "FDFS HTTP DL ST", "FDTT HTTP UL MT", "Kepler", "FDFS HTTP UL ST", "FDTT HTTP DL MT", "Wikipedia", "Amazon.de", "Chip.de", "Gmx.net", "Google.de", "Instagram.com"]
        Type_of_Test = ["PING", "Streaming YT", "FDFS DL", "FDTT UL ", "HTTP Browsing", "FDFS UL", "FDTT DL", "HTTP Browsing", "HTTP Browsing", "HTTP Browsing", "HTTP Browsing", "HTTP Browsing", "HTTP Browsing"]
        Thread_info = ["PING", "Live 4K", "ST", "MT", "MT", "ST", "MT", "MT", "MT", "MT", "MT", "MT", "MT"]

        data = {'Grouping_All_URL': Grouping_All_Url, 'Direction_Test': Direction_Test, 'Test_Name': Test_Name, 'Type_of_Test': Type_of_Test, 'Thread_info': Thread_info}
        df_gr = pd.DataFrame(data)

        merged_df = pd.merge(df_result, df_gr, on='Grouping_All_URL', how='left')

        columns_to_move = ['Grouping_All_URL', 'Direction_Test', 'Test_Name', 'Type_of_Test', 'Thread_info']
        new_positions = [3, 4, 5, 6, 7]  # 0-indexed positions

        # Move each column to its new position
        for column_name, new_position in zip(columns_to_move, new_positions):
            column_to_move = merged_df.pop(column_name)
            merged_df.insert(new_position, column_name, column_to_move)

        # Presenting results
        merged_df.to_csv('Agg_Results.csv', mode='w', header=True, index=False)
        # webbrowser.open("Pivot.csv")


        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(merged_df)
        st.download_button(label="Download Result File", data=csv, file_name="Agg_Results.csv", mime='text/csv')
        st.dataframe(df_total_stats)
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
