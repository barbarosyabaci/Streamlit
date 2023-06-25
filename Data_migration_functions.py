def Atoll_to_planet_MS(file_list):
    import os
    import webbrowser
    import pandas as pd

    # Planet_column_names = list(pd.read_csv("input\Planet API Column Names.csv", index_col=False)["Column Name"])
    Planet_column_names = ['MCC', 'MNC', 'Cell Name', 'Technology', 'Cell ID', 'Site ID', 'Band Name',
                             'Downlink ARFCN', 'eNodeB ID', 'gNodeB ID', 'Site UID', 'Longitude', 'Latitude',
                             'Description', 'Height (m)', 'Azimuth', 'Mechanical Tilt', 'Antenna File',
                             'Electrical Tilt', 'Electrical Azimuth', 'Electrical Beamwidth',
                             'Downlink Antenna Ports', 'Uplink Antenna Ports', 'Propagation Model',
                             'PA Power (dBm)', 'Physical Cell ID', 'Antenna Algorithm', 'Distance (km)',
                             'Radials', 'Output Resolution (m)', 'Outer Area Resolution (m)', 'Inner Area Radius (m)',
                             'Downlink Cable Loss (dB)', 'Uplink Cable Loss (dB)', 'BTS Noise Figure (dB)',
                             'P0,PUCCH (dBm)',
                             'PUSCH Pathloss Compensation Factor (alpha)', 'First Zadoff Chu Sequence',
                             'PUSCH Noise Rise (dB)', 'Downlink Load (%)', 'Uplink Load (%)',
                             'PDSCH Power Per RE (dBm)',
                             'PDCCH Power Per RE (dBm)', 'Beamforming', 'Beamforming Configuration',
                             'Reference Signal Power Per RE (dBm)', 'Synchronization Signal Power Per RE (dBm)',
                             'TAC', 'P0,PUSCH (dBm)', 'Broadcast Channel Power Per RE (dBm)', 'PSS Power Per RE (dBm)',
                             'SSS Power Per RE (dBm)', 'DM-RS Power Per RE (dBm)', 'CSI-RS Power Per RE (dBm)',
                             'Automatic Powers', 'P0,PUSCH - 15 kHz (dBm)', 'PBCH Power Per RE (dBm)',
                             'Apply Beamforming To Control Channels/Signals', 'Custom: AREA_CATEGORY', 'Custom: Active',
                             'Custom: backhaulType', 'Custom: cdcCode', 'Custom: cityCode', 'Custom: cityJpn',
                             'Custom: cucpId', 'Custom: cuupId', 'Custom: gcCode', 'Custom: object',
                             'Custom: prefectureJpn', 'Custom: phase', 'Custom: rdcCode', 'Custom: geographyL1',
                             'Custom: geographyL2', 'Custom: geographyL3', 'Custom: geographyL4', 'Custom: ruId',
                             'Custom: sarfid', 'Custom: subRegion', 'Custom: siteStatus', 'Custom: vcuId',
                             'Custom: vduId', 'Custom: zeroCorrelationZone', 'Custom: bandwidth',
                             'Custom: siteTypeIndoorOutdoor', 'Custom: siteToRdcMapping',
                             'Custom: siteToGnbIdMapping', 'Custom: rsi', 'Custom: ulGroupAssignmentPusch',
                             'Custom: ulPuschCyclicShiftCell', 'Custom: riuId'
                           ]

    # Creating Planet Cell Tables from column List

    df_planet_Cell_File_lte = pd.DataFrame(columns=Planet_column_names)
    df_planet_Cell_File_nr = pd.DataFrame(columns=Planet_column_names)

    # Filling the cell tables for LTE and NR cells

    df_planet_Cell_File_lte = Create_LTE_cells_table(file_list)
    df_planet_Cell_File_nr = Create_NR_cells_table(file_list)
    # df_planet_Cell_File_mm = apc.Create_MM_cells_table(file_list,df_planet_Cell_File_mm)

    # Combining the cell files for NR and LTE

    df = df_planet_Cell_File_lte.append(df_planet_Cell_File_nr)
    # df = df_planet_Cell_File_nr
    df['Cell ID'] = df['Cell ID'].astype('Int64')
    df['TAC'] = df['TAC'].astype('Int64')
    df['First Zadoff Chu Sequence'] = df['First Zadoff Chu Sequence'].astype('Int64')

    df_all = df

    #This part will be used for if only some columns are needed, all mandatory columns are selected

    #df_new = df_all[["Cell Name",
    #                 "Technology",
    #                 "Downlink ARFCN",
    #                 "Longitude",
    #                 "Latitude",
    #                 "Height (m)",
    #                 "Antenna File",
    #                 "Propagation Model",
    #                 "PA Power (dBm)",
    #                 "Distance (km)",
    #                 "Output Resolution (m)",
    #                 "Outer Area Resolution (m)",
    #                 "Inner Area Radius (m)"]]
    # export_csv = df_new.to_csv("output\Planet Microservices Cell File.csv", index=None, header=True,encoding='cp932')

    # try:
    #     os.mkdir('output')
    # except:
    #     a = 1
    #
    # try:
    #     os.mkdir('output\\10000')
    # except:
    #     print(" ")

    return df_all
    # try:
        # df_all.to_csv("output\Planet Microservices Cell File.csv", index=None, header=True, encoding='UTF-8')
        # n = len(df_all) // 10000 + 1
        # print(n)
        # for i in range(0, n):
            # print(i * 10000, (i + 1) * 10000)
            # df_part = df_all.iloc[(i * 10000):((i + 1) * 10000)]
            # df_part['Cell ID'] = df_part['Cell ID'].astype('Int64')
            # df_part['TAC'] = df_part['TAC'].astype('Int64')
            # df_part.to_csv("output\\10000\Planet Microservices Cell File" + str((i + 1) * 10000) + ".csv",
                                        # index=None, header=True, encoding='UTF-8')
        # success_message = "Import file Planet Microservices Cell File.csv succesfully created in output folder \n\n"\
                          # "Import files divided by 100000 cells succesfully created in output/10000 folder  \n\n"\
                          # "Please Check output folder located in the executable file folder \n\n"
        # webbrowser.open("output\Planet Microservices Cell File.csv")
        # return df_all # success_message
    # except:
        # a = 1
        # return "Please close the import file(s) if it is open, export file cannot be created"



    # Dividing and exporting the cell data, this part will be used if required

    # This part will be used for if only some columns are needed, all mandatory columns are selected
    # n = len(df_new) // 10000 + 1
    # print(n)
    # for i in range(0, n):
    #   print(i*10000, (i+1)*10000)
    #   df_part = df_new.iloc[(i*10000):((i+1)*10000)]
    #   export_csv = df_part.to_csv("output\\10000\\Planet Microservices Cell File" + str((i+1)*10000) + ".csv", index=None, header=True,encoding='cp932')

def Create_LTE_cells_table(file_list):
    import pandas as pd

    print("creating LTE cells table")

    # filename_lte_cells = file_list[0]
    # filename_sites = file_list[2]
    # filename_transmitters = file_list[3]
    # filename_bf_antennas = file_list[4]
    # filename_lte_cells_details = file_list[5]

    # Reading tables as pandas df
    df_atoll_lte_cells = file_list[0]# pd.read_csv(filename_lte_cells, low_memory=False, index_col=False, encoding='cp932')
    df_atoll_sites = file_list[2] # pd.read_csv(filename_sites, low_memory=False, index_col=False, encoding='cp932')  # CP932 is japanese character encoding
    df_atoll_transmitters = file_list[3] #  pd.read_csv(filename_transmitters, low_memory=False, index_col=False,encoding='cp932')
    df_atoll_bf_antennas_list = file_list[4] # pd.read_csv(filename_bf_antennas, low_memory=False, index_col=False, encoding='cp932')['Beamforming Antenna List'].tolist()
    df_atoll_lte_cells_details = file_list[5] # pd.read_csv(filename_lte_cells_details, low_memory=False, index_col=False)#, encoding='cp932')

    # df_atoll_lte_cells = pd.read_csv(filename_lte_cells, low_memory=False, index_col=False, encoding='UTF-8')
    # df_atoll_sites = pd.read_csv(filename_sites, low_memory=False, index_col=False, encoding='UTF-8')  # CP932 is japanese character encoding
    # df_atoll_transmitters = pd.read_csv(filename_transmitters, low_memory=False, index_col=False, encoding='UTF-8')
    # df_atoll_bf_antennas_list = pd.read_csv(filename_bf_antennas, low_memory=False, index_col=False, encoding='UTF-8')['Beamforming Antenna List'].tolist()


    # Adding data from transmitter table

    column_list = ['Transmitter', 'Height (m)', 'Frequency Band', 'Azimuth (°)', 'Mechanical Downtilt (°)', 'Antenna',
                   'Main Calculation Radius (m)','Noise Figure (dB)',"Main Calculation Radius (m)","VDU_Id","RU_Id",
                   "Extended Calculation Radius (m)", "Main Calculation Radius (m)", "Main Resolution (m)","Transmission losses (dB)",
                   "Reception losses (dB)","Extended Resolution (m)","Additional Electrical Downtilt (°)","RRH_Number","RIU_Id",
                   "Transmitter Type","Number of Transmission Antennas","Number of Reception Antennas","Latitude", "Longitude"]

    df_atoll_lte_cells = pd.merge(df_atoll_lte_cells, df_atoll_transmitters[column_list], on='Transmitter', how='left')

    # df_atoll_lte_cells.to_csv("output\df_atoll_lte_cells.csv", index=None, header=True)

    MS_fields = ["MCC", "MNC", "Cell Name", "Technology", "Cell ID", "Site ID", "Band Name", "Downlink ARFCN",
                 "eNodeB ID", "gNodeB ID", "Site UID", "Longitude", "Latitude", "Description", "Height (m)", "Azimuth",
                 "Mechanical Tilt", "Antenna File", "Electrical Tilt", "Electrical Azimuth", "Electrical Beamwidth",
                 "Downlink Antenna Ports", "Uplink Antenna Ports", "Propagation Model", "PA Power (dBm)",
                 "Physical Cell ID", "Antenna Algorithm", "Base Station Type", "Distance (km)", "Radials",
                 "Output Resolution (m)", "Outer Area Resolution (m)", "Inner Area Radius (m)",
                 "Downlink Cable Loss (dB)", "Uplink Cable Loss (dB)", "BTS Noise Figure (dB)", "P0,PUCCH (dBm)",
                 "PUSCH Pathloss Compensation Factor (alpha)", "First Zadoff Chu Sequence", "PUSCH Noise Rise (dB)",
                 "Downlink Load (%)", "Uplink Load (%)", "PDSCH Power Per RE (dBm)", "PDCCH Power Per RE (dBm)",
                 "Beamforming", "Beamforming Configuration", "Reference Signal Power Per RE (dBm)",
                 "Synchronization Signal Power Per RE (dBm)", "TAC", "P0,PUSCH (dBm)",
                 "Broadcast Channel Power Per RE (dBm)", "PSS Power Per RE (dBm)", "SSS Power Per RE (dBm)",
                 "DM-RS Power Per RE (dBm)", "CSI-RS Power Per RE (dBm)", "Automatic Powers", "P0,PUSCH - 15 kHz (dBm)",
                 "PBCH Power Per RE (dBm)", "Apply Beamforming To Control Channels/Signals", "Optimize Azimuth",
                 "Azimuth Cost", "Azimuth Precision", "Azimuth Range", "Min Azimuth (Degrees)", "Max Azimuth (Degrees)",
                 "Optimize Downtilt", "Downtilt Cost", "Downtilt Precision", "Downtilt Range", "Min Downtilt (Degrees)",
                 "Max Downtilt (Degrees)", "Optimize Power", "Power Cost", "Power Precision", "Power Range",
                 "Min Power", "Max Power", "Optimize Electrical Tilt", "Electrical Tilt Cost",
                 "Electrical Tilt Range", "Min Electrical Tilt (Degrees)", "Max Electrical Tilt (Degrees)",
                 "Optimize Electrical Azimuth", "Electrical Azimuth Cost", "Electrical Azimuth Range",
                 "Min Electrical Azimuth (Degrees)", "Max Electrical Azimuth (Degrees)",
                 "Optimize Electrical Beamwidth", "Electrical Beamwidth Cost", "Electrical Beamwidth Range",
                 "Min Electrical Beamwidth (Degrees)", "Max Electrical Beamwidth (Degrees)", "Optimize Antenna Height",
                 "Antenna Height Cost", "Antenna Height (m) 1", "Cable Length (m) 1", "Antenna Height (m) 2",
                 "Cable Length (m) 2", "Antenna Height (m) 3", "Cable Length (m) 3", "Antenna Height (m) 4",
                 "Cable Length (m) 4", "Antenna Height (m) 5", "Cable Length (m) 5", "Antenna Height (m) 6",
                 "Cable Length (m) 6", "Antenna Height (m) 7", "Cable Length (m) 7", "Antenna Height (m) 8",
                 "Cable Length (m) 8", "Antenna Height (m) 9", "Cable Length (m) 9", "Antenna Height (m) 10",
                 "Cable Length (m) 10", "Optimize Antenna Pattern", "Antenna Pattern Files", "Antenna Pattern Cost",
                 "Site Access Cost", "Custom: areaCategory", "Custom: active", "Custom: backhaulType",
                 "Custom: bandwidth", "Custom: cdcCode", "Custom: cityCode", "Custom: cityJpn", "Custom: cucpId",
                 "Custom: cuupId", "Custom: gcCode", "Custom: object", "Custom: prefectureJpn", "Custom: phase",
                 "Custom: rdcCode", "Custom: riuId", "Custom: rsi", "Custom: ruId", "Custom: sarfid",
                 "Custom: subRegion", "Custom: siteTypeIndoorOutdoor", "Custom: siteToRdcMapping",
                 "Custom: siteToGnbIdMapping", "Custom: ulGroupAssignmentPusch",
                 "Custom: ulPuschCyclicShiftCell", "Custom: vcuId", "Custom: vduId",
                 "Custom: zeroCorrelationZone", "Custom: geographyL1", "Custom: geographyL2", "Custom: geographyL3",
                 "Custom: geographyL4", "Custom: siteStatus"]
                 # ,"Custom: PCI","Custom: TI_Flag","Custom: TI_DATE",
                 # "Custom: Leased_Flag","Custom: MIMO Path","Custom: RetTilt","Custom: RRH No",
                 # "Custom: Transmitter type","Custom: Neighbour LTE Anchor"]

    df_planet_lte_cells = pd.DataFrame(columns=MS_fields)

    print(df_atoll_lte_cells.columns)

    # Creating Planet lte cells table
    df_planet_lte_cells["Cell Name"] = df_atoll_lte_cells["Name"].str[:-3]
    df_planet_lte_cells["Site ID"] = df_atoll_lte_cells["Name"].str[:-5]
    df_planet_lte_cells["Technology"] = "LTE_FDD"
    df_planet_lte_cells.loc[df_atoll_lte_cells["Carrier"] == 'Band 3 - 20MHz (0)', 'Downlink ARFCN'] = 1500
    df_planet_lte_cells.loc[df_atoll_lte_cells["Carrier"] == 'Band 3 - 5MHz (0)', 'Downlink ARFCN'] = 1425
    df_planet_lte_cells["Height (m)"] = df_atoll_lte_cells["Height (m)"]
    df_planet_lte_cells["Band Name"] = df_atoll_lte_cells["Frequency Band"]
    df_planet_lte_cells["Azimuth"] = df_atoll_lte_cells["Azimuth (°)"]
    df_planet_lte_cells["Mechanical Tilt"] = df_atoll_lte_cells["Mechanical Downtilt (°)"]
    df_planet_lte_cells["Electrical Tilt"] = df_atoll_lte_cells["Antenna"].str[-3:-1]
    # df_planet_lte_cells["Electrical Tilt"] = df_planet_lte_cells["Electrical Tilt"].str.strip()
    # df_planet_lte_cells["Electrical Tilt"] = df_planet_lte_cells["Electrical Tilt"].astype('Int64')
    df_planet_lte_cells["Physical Cell ID"] = df_atoll_lte_cells["Physical Cell ID"]
    df_planet_lte_cells["Downlink Load (%)"] = df_atoll_lte_cells["Traffic Load (DL) (%)"]
    df_planet_lte_cells["Uplink Load (%)"] = df_atoll_lte_cells['Traffic Load (UL) (%)']
    df_planet_lte_cells["PUSCH Noise Rise (dB)"] = df_atoll_lte_cells["UL Noise Rise (dB)"]
    df_planet_lte_cells["PA Power (dBm)"] = df_atoll_lte_cells["Max Power (dBm)"]

    df_planet_lte_cells["Radials"] = "1080"
    df_planet_lte_cells["Antenna File"] = df_atoll_lte_cells["Antenna"].str[:-4]+".pafx"
    df_planet_lte_cells["MCC"] = ""
    df_planet_lte_cells["MNC"] = ""
    df_planet_lte_cells["eNodeB ID"] = ""

    df_planet_lte_cells["Cell ID"] = df_atoll_lte_cells["Cellid"]
    df_planet_lte_cells["Propagation Model"] = "P3M-Rakuten-1900MHz.pmf"
    df_planet_lte_cells["Custom: vduId"] = df_atoll_lte_cells['VDU_Id']
    df_planet_lte_cells["Custom: ruId"] = df_atoll_lte_cells['RU_Id']
    df_planet_lte_cells["Custom: zeroCorrelationZone"] = df_atoll_lte_cells['ZeroCorrelationZone']
    df_planet_lte_cells["Custom: active"] = df_atoll_lte_cells['Active']
    # print(df_planet_lte_cells["Custom: active"])
    df_planet_lte_cells.loc[df_planet_lte_cells["Custom: active"] == True, "Custom: active"] = 'true'
    df_planet_lte_cells.loc[df_planet_lte_cells["Custom: active"] == False, "Custom: active"] = 'false'
    df_planet_lte_cells["BTS Noise Figure (dB)"] = df_atoll_lte_cells['Noise Figure (dB)']
    df_planet_lte_cells["P0,PUSCH - 15 kHz (dBm)"] = ""
    df_planet_lte_cells["Antenna Algorithm"] = "MIMO"

    df_planet_lte_cells["Downlink Cable Loss (dB)"] = df_atoll_lte_cells["Transmission losses (dB)"]
    df_planet_lte_cells["Uplink Cable Loss (dB)"] = df_atoll_lte_cells["Reception losses (dB)"]

    # Power settings mappings

    column_list_2 = ["Name","PDSCH EPRE (CE) (dBm)",
"PDCCH EPRE (CE) (dBm)",
"RS EPRE (CE) (dBm)",
"SS EPRE (dBm)",
"PBCH EPRE (dBm)"]

    df_atoll_lte_cells = pd.merge(df_atoll_lte_cells, df_atoll_lte_cells_details[column_list_2], on='Name', how='left')

    df_planet_lte_cells["PDSCH Power Per RE (dBm)"] = df_atoll_lte_cells["PDSCH EPRE (CE) (dBm)"]
    df_planet_lte_cells["PDCCH Power Per RE (dBm)"] = df_atoll_lte_cells["PDCCH EPRE (CE) (dBm)"]
    df_planet_lte_cells["P0,PUCCH (dBm)"] = -65
    df_planet_lte_cells["Reference Signal Power Per RE (dBm)"] = df_atoll_lte_cells["RS EPRE (CE) (dBm)"]
    df_planet_lte_cells["Synchronization Signal Power Per RE (dBm)"] = df_atoll_lte_cells["SS EPRE (dBm)"]
    df_planet_lte_cells["P0,PUSCH (dBm)"] = -65
    df_planet_lte_cells["Broadcast Channel Power Per RE (dBm)"] = df_atoll_lte_cells["PBCH EPRE (dBm)"]
    # df_planet_lte_cells["PUSCH Pathloss Compensation Factor (alpha)"] = df_atoll_lte_cells["Fractional Power Control Factor"]
    df_planet_lte_cells["PUSCH Pathloss Compensation Factor (alpha)"] = 1

    # Arranging Antenna Ports

    df_planet_lte_cells["Downlink Antenna Ports"] = df_atoll_lte_cells["Number of Transmission Antennas"]
    df_planet_lte_cells["Uplink Antenna Ports"] = df_atoll_lte_cells["Number of Reception Antennas"]

    df_planet_lte_cells.loc[df_planet_lte_cells["Downlink Antenna Ports"] == 2, "Downlink Antenna Ports"] = '["Port 1","Port 2"]'
    df_planet_lte_cells.loc[
        df_planet_lte_cells["Downlink Antenna Ports"] == 4, "Downlink Antenna Ports"] = '["Port 1","Port 2","Port 3","Port 4"]'

    df_planet_lte_cells.loc[df_planet_lte_cells["Uplink Antenna Ports"] == 2, "Uplink Antenna Ports"] = '["Port 1","Port 2"]'
    df_planet_lte_cells.loc[
        df_planet_lte_cells["Uplink Antenna Ports"] == 4, "Uplink Antenna Ports"] = '["Port 1","Port 2","Port 3","Port 4"]'
    # adding data from sites table

    del df_atoll_lte_cells['Comments']

    df_sites_selected_fields = df_atoll_sites[["Name","TAC","Sarf Status",
        "PHASE","AREA_CATEGORY","REGION","SUB_REGION","PREFECTURE",
        "PREFECTURE_JPN","CITY_CODE","CITY","CITY_JPN","OBJECT","RDC_Code","GC_Code",
        "CDC_Code","VCU_Id","CUCP_Id","CUUP_Id","Backhaul_Type","BANDWIDTH","INOUT","Cluster Name",
        "LTE SARF ID","Site to RDC Mapping","Site to gNB ID Mapping",'Site_Type_Class',
                                               "Property Address",
                                               "Property Name",
                                               "Entrance_GC",
                                               "Destination_GC",
                                               "FREE_NUM_1",
                                               "FREE_NUM_2",
                                               "ONAIR_DATE",
                                               "DF_Ready_Actual",
                                               "GC_Ready_Actual",
                                               "TI_Ready_Actual",
                                               "GC Application Status",
                                               "Co-location_Frequency_Band",
                                               "Co-location_SARF ID_3.7GHz",
                                               "Co-location_SARF ID_28GHz",
                                               "BS_Ready_Actual",
                                               "Project",
                                               "LL_ID",
                                               "Comments"
                                               ]]

    # "TI Flag", "TI Date", "Leased Flag", "MIMO Path",

    df_atoll_lte_cells["Site ID"] = df_atoll_lte_cells["Name"].str[:-5]
    df_atoll_lte_cells = pd.merge(df_atoll_lte_cells, df_sites_selected_fields, left_on='Site ID', right_on='Name',how='left')

    df_planet_lte_cells["Latitude"] = df_atoll_lte_cells['Latitude']
    df_planet_lte_cells["Longitude"] = df_atoll_lte_cells['Longitude']
    df_planet_lte_cells["TAC"] = df_atoll_lte_cells['TAC']
    df_planet_lte_cells["Base Station Type"] = df_atoll_lte_cells["Radio Equipment"]
    df_planet_lte_cells["Custom: siteStatus"] = df_atoll_lte_cells["Sarf Status"]
    df_planet_lte_cells["Custom: sarfid"] = df_atoll_lte_cells["Site ID"]
    df_planet_lte_cells["Custom: phase"] = df_atoll_lte_cells["PHASE"]
    df_planet_lte_cells["Custom: areaCategory"] = df_atoll_lte_cells["AREA_CATEGORY"]
    df_planet_lte_cells["Custom: geographyL1"] = df_atoll_lte_cells["REGION"]
    df_planet_lte_cells["Custom: subRegion"] = df_atoll_lte_cells["SUB_REGION"]
    df_planet_lte_cells["Custom: geographyL2"] = df_atoll_lte_cells["PREFECTURE"]
    df_planet_lte_cells["Custom: prefectureJpn"] = df_atoll_lte_cells["PREFECTURE_JPN"] + " "
    df_planet_lte_cells["Custom: cityCode"] = df_atoll_lte_cells["CITY_CODE"]
    df_planet_lte_cells["Custom: geographyL3"] = df_atoll_lte_cells["CITY"]
    df_planet_lte_cells["Custom: geographyL4"] = df_atoll_lte_cells["Cluster Name"]
    df_planet_lte_cells["Custom: cityJpn"] = df_atoll_lte_cells["CITY_JPN"]+ " "
    df_planet_lte_cells["Custom: object"] = df_atoll_lte_cells["OBJECT"]
    df_planet_lte_cells["Custom: rdcCode"] = df_atoll_lte_cells["RDC_Code"]
    df_planet_lte_cells["Custom: gcCode"] = df_atoll_lte_cells["GC_Code"]
    df_planet_lte_cells["Custom: cdcCode"] = df_atoll_lte_cells["CDC_Code"]
    df_planet_lte_cells["Custom: vcuId"] = df_atoll_lte_cells["VCU_Id"]

    df_planet_lte_cells["Custom: bandwidth"] = df_atoll_lte_cells["BANDWIDTH"]
    df_planet_lte_cells["Custom: siteTypeIndoorOutdoor"] = df_atoll_lte_cells["INOUT"]
    df_planet_lte_cells["Custom: siteToRdcMapping"] = df_atoll_lte_cells["Site to RDC Mapping"]
    df_planet_lte_cells["Custom: siteToGnbIdMapping"] = df_atoll_lte_cells["Site to gNB ID Mapping"]
    df_planet_lte_cells["Custom: rsi"] = df_atoll_lte_cells["RSI_4G"]
    df_planet_lte_cells["Custom: ulGroupAssignmentPusch"] = df_atoll_lte_cells["UL Group Assignment PUSCH"]
    df_planet_lte_cells["Custom: ulPuschCyclicShiftCell"] = df_atoll_lte_cells["UL PUSCH Cyclic Shift"]
    df_planet_lte_cells["Custom: riuId"] = df_atoll_lte_cells["RIU_Id"]

    # df_planet_lte_cells["Custom: PCI"] = df_atoll_lte_cells["PCI_4G"]
    df_planet_lte_cells["Custom: tiFlag"] = "null"# df_atoll_lte_cells["TI Flag"]
    df_planet_lte_cells["Custom: tiDate"] = "null"# df_atoll_lte_cells["TI Date"]
    df_planet_lte_cells["Custom: leasedFlag"] = "null"# df_atoll_lte_cells["Leased Flag"]
    df_planet_lte_cells["Custom: mimoPath"] = "null"# df_atoll_lte_cells["MIMO Path"]
    df_planet_lte_cells["Custom: retTilt"] = df_atoll_lte_cells["Additional Electrical Downtilt (°)"]
    df_planet_lte_cells["Custom: rrhNo"] = df_atoll_lte_cells["RRH_Number"]
    df_planet_lte_cells["Custom: transmitterType"] = df_atoll_lte_cells["Transmitter Type"]
    # df_planet_lte_cells["Custom: Neighbour LTE Anchor"] = df_atoll_lte_cells["LTE SARF ID"]
    df_planet_lte_cells["Custom: siteTypeClass"] = df_atoll_lte_cells["Site_Type_Class"]

    df_planet_lte_cells["Custom: free1"] = 'null'
    df_planet_lte_cells["Custom: free2"] = 'null'
    df_planet_lte_cells["Custom: free3"] = 'null'
    df_planet_lte_cells["Custom: free4"] = 'null'
    df_planet_lte_cells["Custom: free5"] = 'null'
    df_planet_lte_cells["Custom: free6"] = 'null'

    df_planet_lte_cells["Custom: propertyAddress"] = df_atoll_lte_cells["Property Address"]
    df_planet_lte_cells["Custom: propertyName"] = df_atoll_lte_cells["Property Name"]
    df_planet_lte_cells["Custom: entranceGc"] = df_atoll_lte_cells["Entrance_GC"]
    df_planet_lte_cells["Custom: destinationGc"] = df_atoll_lte_cells["Destination_GC"]
    df_planet_lte_cells["Custom: freeNum1"] = df_atoll_lte_cells["FREE_NUM_1"]
    df_planet_lte_cells["Custom: freeNum2"] = df_atoll_lte_cells["FREE_NUM_2"]
    df_planet_lte_cells["Custom: onairDate"] = df_atoll_lte_cells["ONAIR_DATE"]
    df_planet_lte_cells["Custom: dfReadyActual"] = df_atoll_lte_cells["DF_Ready_Actual"]
    df_planet_lte_cells["Custom: gcReadyActual"] = df_atoll_lte_cells["GC_Ready_Actual"]
    df_planet_lte_cells["Custom: tiReadyActual"] = df_atoll_lte_cells["TI_Ready_Actual"]
    df_planet_lte_cells["Custom: gcApplicationStatus"] = df_atoll_lte_cells["GC Application Status"]
    df_planet_lte_cells["Custom: coLocationFrequencyBand"] = df_atoll_lte_cells["Co-location_Frequency_Band"]
    df_planet_lte_cells["Custom: coLocationSarfId37GHz"] = df_atoll_lte_cells["Co-location_SARF ID_3.7GHz"]
    df_planet_lte_cells["Custom: coLocationSarfId28GHz"] = df_atoll_lte_cells["Co-location_SARF ID_28GHz"]
    df_planet_lte_cells["Custom: bsReadyActual"] = df_atoll_lte_cells["BS_Ready_Actual"]
    df_planet_lte_cells["Custom: llid"] = df_atoll_lte_cells["LL_ID"]
    df_planet_lte_cells["Custom: comments"] = df_atoll_lte_cells["Comments"]
    df_planet_lte_cells["Custom: project"] = df_atoll_lte_cells["Project"]

    df_planet_lte_cells["Beamforming"] = False
    df_planet_lte_cells["Beamforming Configuration"] = ''
    df_planet_lte_cells["Apply Beamforming To Control Channels/Signals"] = ''

    # for i in df_atoll_bf_antennas_list:
        # df_planet_lte_cells.loc[df_atoll_lte_cells["Antenna"] == i, "Beamforming"] = True

    df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'E_KINKI', "REGION"] = 'E_KANSAI'
    df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'B_SHINETSU', "REGION"] = 'A_KANTO'
    # df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'D_HOKURIKU', "REGION"] = 'E_KANSAI'
    # df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'G_SHIKOKU', "REGION"] = 'F_CHUGOKU'
    df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'O_OKINAWA', "REGION"] = 'H_KYUSHU'
    df_atoll_lte_cells["Frequency Band"] = df_atoll_lte_cells["Frequency Band"].str.replace(' ','_')
    df_atoll_lte_cells["Frequency Band"] = df_atoll_lte_cells["Frequency Band"].str.replace('-_', '')

    # df_planet_lte_cells["Propagation Model"] = "P3M_"+df_atoll_lte_cells["REGION"].str[2:] +"_LTE_FDD" +"_"+ df_atoll_lte_cells["Frequency Band"]+'.pmf'
    df_planet_lte_cells["Propagation Model"] = "P3M_"+df_atoll_lte_cells["REGION"].str[2:] +"_LTE_FDD_Band_3" +'.pmf'

    df_planet_lte_cells["Propagation Model"].fillna("P3M-Rakuten-1900MHz.pmf",inplace = True)

    df_planet_lte_cells["Custom: geographyL1"] = df_planet_lte_cells["Custom: geographyL1"].str[2:]

    columns_to_fill_null = ["Custom: areaCategory",
                            "Custom: active",
                            "Custom: backhaulType",
                            "Custom: bandwidth",
                            "Custom: cdcCode",
                            "Custom: cityCode",
                            "Custom: cityJpn",
                            "Custom: cucpId",
                            "Custom: cuupId",
                            "Custom: gcCode",
                            "Custom: object",
                            "Custom: prefectureJpn",
                            "Custom: phase",
                            "Custom: rdcCode",
                            "Custom: riuId",
                            "Custom: rsi",
                            "Custom: ruId",
                            "Custom: sarfid",
                            "Custom: subRegion",
                            "Custom: siteTypeIndoorOutdoor",
                            "Custom: siteToRdcMapping",
                            "Custom: siteToGnbIdMapping",
                            "Custom: ulGroupAssignmentPusch",
                            "Custom: ulPuschCyclicShiftCell",
                            "Custom: vcuId",
                            "Custom: vduId",
                            "Custom: zeroCorrelationZone",
                            "Custom: geographyL1",
                            "Custom: geographyL2",
                            "Custom: geographyL3",
                            "Custom: geographyL4",
                            "Custom: siteStatus",
                            "Custom: tiFlag",
                            "Custom: tiDate",
                            "Custom: leasedFlag",
                            "Custom: mimoPath",
                            "Custom: retTilt",
                            "Custom: rrhNo",
                            "Custom: transmitterType",
                            "Custom: siteTypeClass",
                            "Custom: free1",
                            "Custom: free2",
                            "Custom: free3",
                            "Custom: free4",
                            "Custom: free5",
                            "Custom: free6",
                            "Custom: propertyAddress",
                            "Custom: propertyName",
                            "Custom: entranceGc",
                            "Custom: destinationGc",
                            "Custom: freeNum1",
                            "Custom: freeNum2",
                            "Custom: onairDate",
                            "Custom: dfReadyActual",
                            "Custom: gcReadyActual",
                            "Custom: tiReadyActual",
                            "Custom: gcApplicationStatus",
                            "Custom: coLocationFrequencyBand",
                            "Custom: coLocationSarfId37GHz",
                            "Custom: coLocationSarfId28GHz",
                            "Custom: bsReadyActual",
                            "Custom: llid",
                            "Custom: comments",
                            "Custom: project"
    ]


    for column in columns_to_fill_null:
        df_planet_lte_cells[column].fillna("null", inplace=True)

    # df_planet_lte_cells["Custom: geographyL1"].fillna("null",inplace = True)
    # df_planet_lte_cells["Custom: geographyL2"].fillna("null",inplace = True)
    # df_planet_lte_cells["Custom: geographyL3"].fillna("null",inplace = True)
    # df_planet_lte_cells["Custom: geographyL4"].fillna("null",inplace = True)

    df_planet_lte_cells["First Zadoff Chu Sequence"] = df_atoll_lte_cells["Prachconfigindex"]

    # df_planet_lte_cells["Distance (km)"] = df_atoll_lte_cells["Extended Calculation Radius (m)"]/1000

    # Radius and resolution settings
    df_planet_lte_cells["Distance (km)"] = df_atoll_lte_cells["Extended Calculation Radius (m)"]/1000
    df_planet_lte_cells["Inner Area Radius (m)"] = df_atoll_lte_cells["Main Calculation Radius (m)"]
    df_planet_lte_cells["Output Resolution (m)"] = df_atoll_lte_cells["Main Resolution (m)"]
    df_planet_lte_cells["Outer Area Resolution (m)"] = df_atoll_lte_cells["Extended Resolution (m)"]

    df_planet_lte_cells.loc[df_atoll_lte_cells["Extended Resolution (m)"].isnull(), "Distance (km)"] = df_planet_lte_cells["Inner Area Radius (m)"]/1000
    df_planet_lte_cells.loc[df_atoll_lte_cells["Extended Resolution (m)"].isnull(), "Outer Area Resolution (m)"] = df_planet_lte_cells["Output Resolution (m)"]

    # print(df_planet_lte_cells[["Cell Name","Extended Resolution (m)","Distance (km)"]].head(10))

    # df_planet_lte_cells = df_planet_lte_cells_rural_urban_class(df_planet_lte_cells,file_list)

    # del df_planet_lte_cells["MCC","MNC"]
    return df_planet_lte_cells

def Create_NR_cells_table(file_list):
    import pandas as pd

    print("Creating NR cells table")

    filename_NR_cells = file_list[1]
    filename_sites = file_list[2]
    filename_transmitters = file_list[3]
    filename_bf_antennas = file_list[4]
    filename_NR_cells_details = file_list[5]

    # Reading tables as pandas df
    df_atoll_sites = file_list[2] # pd.read_csv(filename_sites, low_memory=False, index_col=False, encoding='cp932')  # CP932 is japanese character encoding
    df_atoll_transmitters = file_list[3]# pd.read_csv(filename_transmitters, low_memory=False, index_col=False, encoding='cp932')
    df_atoll_NR_cells = file_list[1] # pd.read_csv(filename_NR_cells, low_memory=False, index_col=False, encoding='cp932')
    df_atoll_bf_antennas_list = file_list[4] # pd.read_csv(filename_bf_antennas, low_memory=False, index_col=False, encoding='cp932')['Beamforming Antenna List'].tolist()
    df_atoll_NR_cells_details = file_list[5] # pd.read_csv(filename_NR_cells_details, low_memory=False, index_col=False)#, encoding='cp932')
    # df_atoll_sites = pd.read_csv(filename_sites, low_memory=False, index_col=False, encoding='UTF-8')  # CP932 is japanese character encoding
    # df_atoll_transmitters = pd.read_csv(filename_transmitters, low_memory=False, index_col=False, encoding='UTF-8')
    # df_atoll_NR_cells = pd.read_csv(filename_NR_cells, low_memory=False, index_col=False, encoding='UTF-8')
    # df_atoll_bf_antennas_list = pd.read_csv(filename_bf_antennas, low_memory=False, index_col=False, encoding='UTF-8')['Beamforming Antenna List'].tolist()


    # Adding data from transmitter table

    column_list = ['Transmitter', 'Height (m)', 'Frequency Band', 'Azimuth (°)', 'Mechanical Downtilt (°)', 'Antenna',
                   'Main Calculation Radius (m)', 'Noise Figure (dB)','Beamforming Model',"VDU_Id","RU_Id","RRH_Number",
                   "Extended Calculation Radius (m)", "Main Calculation Radius (m)", "Main Resolution (m)",
                   "Extended Resolution (m)","Additional Electrical Downtilt (°)","Transmitter Type","RIU_Id",
                   "Transmission losses (dB)","Reception losses (dB)","Number of Transmission Antennas","Number of Reception Antennas","Latitude", "Longitude"
                   ]
    df_atoll_NR_cells = pd.merge(df_atoll_NR_cells, df_atoll_transmitters[column_list], on='Transmitter', how='left')

    # Creating Planet NR cells table

    MS_fields = ["MCC", "MNC", "Cell Name", "Technology", "Cell ID", "Site ID", "Band Name", "Downlink ARFCN",
                 "eNodeB ID", "gNodeB ID", "Site UID", "Longitude", "Latitude", "Description", "Height (m)", "Azimuth",
                 "Mechanical Tilt", "Antenna File", "Electrical Tilt", "Electrical Azimuth", "Electrical Beamwidth",
                 "Downlink Antenna Ports", "Uplink Antenna Ports", "Propagation Model", "PA Power (dBm)",
                 "Physical Cell ID", "Antenna Algorithm", "Base Station Type", "Distance (km)", "Radials",
                 "Output Resolution (m)", "Outer Area Resolution (m)", "Inner Area Radius (m)",
                 "Downlink Cable Loss (dB)", "Uplink Cable Loss (dB)", "BTS Noise Figure (dB)", "P0,PUCCH (dBm)",
                 "PUSCH Pathloss Compensation Factor (alpha)", "First Zadoff Chu Sequence", "PUSCH Noise Rise (dB)",
                 "Downlink Load (%)", "Uplink Load (%)", "PDSCH Power Per RE (dBm)", "PDCCH Power Per RE (dBm)",
                 "Beamforming", "Beamforming Configuration", "Reference Signal Power Per RE (dBm)",
                 "Synchronization Signal Power Per RE (dBm)", "TAC", "P0,PUSCH (dBm)",
                 "Broadcast Channel Power Per RE (dBm)", "PSS Power Per RE (dBm)", "SSS Power Per RE (dBm)",
                 "DM-RS Power Per RE (dBm)", "CSI-RS Power Per RE (dBm)", "Automatic Powers", "P0,PUSCH - 15 kHz (dBm)",
                 "PBCH Power Per RE (dBm)", "Apply Beamforming To Control Channels/Signals", "Optimize Azimuth",
                 "Azimuth Cost", "Azimuth Precision", "Azimuth Range", "Min Azimuth (Degrees)", "Max Azimuth (Degrees)",
                 "Optimize Downtilt", "Downtilt Cost", "Downtilt Precision", "Downtilt Range", "Min Downtilt (Degrees)",
                 "Max Downtilt (Degrees)", "Optimize Power", "Power Cost", "Power Precision", "Power Range",
                 "Min Power", "Max Power", "Optimize Electrical Tilt", "Electrical Tilt Cost",
                 "Electrical Tilt Range", "Min Electrical Tilt (Degrees)", "Max Electrical Tilt (Degrees)",
                 "Optimize Electrical Azimuth", "Electrical Azimuth Cost", "Electrical Azimuth Range",
                 "Min Electrical Azimuth (Degrees)", "Max Electrical Azimuth (Degrees)",
                 "Optimize Electrical Beamwidth", "Electrical Beamwidth Cost", "Electrical Beamwidth Range",
                 "Min Electrical Beamwidth (Degrees)", "Max Electrical Beamwidth (Degrees)", "Optimize Antenna Height",
                 "Antenna Height Cost", "Antenna Height (m) 1", "Cable Length (m) 1", "Antenna Height (m) 2",
                 "Cable Length (m) 2", "Antenna Height (m) 3", "Cable Length (m) 3", "Antenna Height (m) 4",
                 "Cable Length (m) 4", "Antenna Height (m) 5", "Cable Length (m) 5", "Antenna Height (m) 6",
                 "Cable Length (m) 6", "Antenna Height (m) 7", "Cable Length (m) 7", "Antenna Height (m) 8",
                 "Cable Length (m) 8", "Antenna Height (m) 9", "Cable Length (m) 9", "Antenna Height (m) 10",
                 "Cable Length (m) 10", "Optimize Antenna Pattern", "Antenna Pattern Files", "Antenna Pattern Cost",
                 "Site Access Cost", "Custom: areaCategory", "Custom: active", "Custom: backhaulType",
                 "Custom: bandwidth", "Custom: cdcCode", "Custom: cityCode", "Custom: cityJpn", "Custom: cucpId",
                 "Custom: cuupId", "Custom: gcCode", "Custom: object", "Custom: prefectureJpn", "Custom: phase",
                 "Custom: rdcCode", "Custom: riuId", "Custom: rsi", "Custom: ruId", "Custom: sarfid",
                 "Custom: subRegion", "Custom: siteTypeIndoorOutdoor", "Custom: siteToRdcMapping",
                 "Custom: siteToGnbIdMapping", "Custom: ulGroupAssignmentPusch",
                 "Custom: ulPuschCyclicShiftCell", "Custom: vcuId", "Custom: vduId",
                 "Custom: zeroCorrelationZone", "Custom: geographyL1", "Custom: geographyL2", "Custom: geographyL3",
                 "Custom: geographyL4", "Custom: siteStatus"]
                 # ,"Custom: PCI","Custom: TI_Flag","Custom: TI_DATE",
                 # "Custom: Leased_Flag","Custom: MIMO Path","Custom: RetTilt","Custom: RRH No",
                 # "Custom: Transmitter type","Custom: Neighbour LTE Anchor"]

    df_planet_NR_cells = pd.DataFrame(columns=MS_fields)

    df_planet_NR_cells["Cell Name"] = df_atoll_NR_cells["Name"].str[:-3]
    df_planet_NR_cells["Site ID"] = df_atoll_NR_cells["Name"].str[:-5]
    df_planet_NR_cells["Technology"] = "NR"
    df_planet_NR_cells.loc[df_atoll_NR_cells["Carrier"] == "n77 - 100MHz (0)", 'Downlink ARFCN'] = 656666 # asked values to Mikuni San 2065832 and 656667
    df_planet_NR_cells.loc[df_atoll_NR_cells["Carrier"] == "n257 - 400MHz (0)", 'Downlink ARFCN'] = 2065833
    df_planet_NR_cells["Height (m)"] = df_atoll_NR_cells["Height (m)"]
    df_planet_NR_cells["Band Name"] = df_atoll_NR_cells["Frequency Band"]
    df_planet_NR_cells["Azimuth"] = df_atoll_NR_cells["Azimuth (°)"]
    df_planet_NR_cells["Mechanical Tilt"] = df_atoll_NR_cells["Mechanical Downtilt (°)"]
    df_planet_NR_cells["Electrical Tilt"] = df_atoll_NR_cells["Antenna"].str[-3:-1]
    df_planet_NR_cells["Physical Cell ID"] = df_atoll_NR_cells["Physical Cell ID"]
    df_planet_NR_cells["Downlink Load (%)"] = df_atoll_NR_cells["Traffic Load (DL) (%)"]
    df_planet_NR_cells["Uplink Load (%)"] = df_atoll_NR_cells['Traffic Load (UL) (%)']
    df_planet_NR_cells["PUSCH Noise Rise (dB)"] = df_atoll_NR_cells["UL Noise Rise (dB)"]
    df_planet_NR_cells["PA Power (dBm)"] = df_atoll_NR_cells["Max Power (dBm)"]
    df_planet_NR_cells["Propagation Model"] = "P3M-Rakuten-1900MHz.pmf"
    df_planet_NR_cells["Radials"] = "1080"
    # df_planet_NR_cells["Antenna File"] = df_atoll_NR_cells["Beamforming Model"] +".pafx"
    df_planet_NR_cells["Antenna File"] = df_atoll_NR_cells["Antenna"].str[:-4] +".pafx"
    df_planet_NR_cells["MCC"] = ""
    df_planet_NR_cells["MNC"] = ""
    df_planet_NR_cells["eNodeB ID"] = ""
    df_planet_NR_cells["Cell ID"] = df_atoll_NR_cells["Cellid"]
    df_planet_NR_cells["Custom: vduId"] = df_atoll_NR_cells['VDU_Id']
    df_planet_NR_cells["Custom: ruId"] = df_atoll_NR_cells['RU_Id']
    df_planet_NR_cells["Custom: zeroCorrelationZone"] = df_atoll_NR_cells['ZeroCorrelationZone']
    df_planet_NR_cells["Custom: active"] = df_atoll_NR_cells['Active']
    df_planet_NR_cells.loc[df_planet_NR_cells["Custom: active"] == True, "Custom: active"] = "true"
    df_planet_NR_cells.loc[df_planet_NR_cells["Custom: active"] == False, "Custom: active"] = "false"
    df_planet_NR_cells["BTS Noise Figure (dB)"] = df_atoll_NR_cells['Noise Figure (dB)']
    df_planet_NR_cells["P0,PUSCH - 15 kHz (dBm)"] = "-65"
    df_planet_NR_cells["Antenna Algorithm"] = "MIMO"
    df_planet_NR_cells["P0,PUCCH (dBm)"] = -65
    df_planet_NR_cells["P0,PUSCH (dBm)"] = -65
    df_planet_NR_cells["PUSCH Pathloss Compensation Factor (alpha)"] = 1

    df_planet_NR_cells["Downlink Cable Loss (dB)"] = df_atoll_NR_cells["Transmission losses (dB)"]
    df_planet_NR_cells["Uplink Cable Loss (dB)"] = df_atoll_NR_cells["Reception losses (dB)"]

    # Power settings

    column_list_2 = ["Name", "PDSCH EPRE (CE) (dBm)", "PDCCH EPRE (CE) (dBm)"]

    df_atoll_NR_cells = pd.merge(df_atoll_NR_cells, df_atoll_NR_cells_details[column_list_2], on='Name', how='left')

    df_planet_NR_cells["PDSCH Power Per RE (dBm)"] = df_atoll_NR_cells["PDSCH EPRE (CE) (dBm)"]
    df_planet_NR_cells["PDCCH Power Per RE (dBm)"] = df_atoll_NR_cells["PDCCH EPRE (CE) (dBm)"]

    # df_planet_NR_cells["PUSCH Pathloss Compensation Factor (alpha)"] = df_atoll_NR_cells["Fractional Power Control Factor"]

    df_planet_NR_cells["Automatic Powers"] = False

    df_planet_NR_cells["SSS Power Per RE (dBm)"] = df_atoll_NR_cells["SSS EPRE (dBm)"]

    # Arranging Antenna Ports

    df_planet_NR_cells["Downlink Antenna Ports"] = df_atoll_NR_cells["Number of Transmission Antennas"]
    df_planet_NR_cells["Uplink Antenna Ports"] = df_atoll_NR_cells["Number of Reception Antennas"]

    # print(df_planet_NR_cells["Downlink Antenna Ports"])

    df_planet_NR_cells.loc[df_planet_NR_cells["Downlink Antenna Ports"] == 32, "Downlink Antenna Ports"] = '["Port 1","Port 2"]'
    df_planet_NR_cells.loc[df_planet_NR_cells["Downlink Antenna Ports"] == 128, "Downlink Antenna Ports"] = '["Port 1","Port 2","Port 3","Port 4"]'
    df_planet_NR_cells.loc[df_planet_NR_cells["Downlink Antenna Ports"] == 4, "Downlink Antenna Ports"] = '["Port 1","Port 2","Port 3","Port 4"]'

    df_planet_NR_cells.loc[df_planet_NR_cells["Uplink Antenna Ports"] == 32, "Uplink Antenna Ports"] = '["Port 1","Port 2"]'
    df_planet_NR_cells.loc[df_planet_NR_cells["Uplink Antenna Ports"] == 128, "Uplink Antenna Ports"] = '["Port 1","Port 2","Port 3","Port 4"]'
    df_planet_NR_cells.loc[df_planet_NR_cells["Uplink Antenna Ports"] == 4, "Uplink Antenna Ports"] = '["Port 1","Port 2","Port 3","Port 4"]'

    # adding data from sites table
    del df_atoll_NR_cells['Comments']

    df_sites_selected_fields = df_atoll_sites[["Name","TAC","Sarf Status",
        "PHASE","AREA_CATEGORY","REGION","SUB_REGION","PREFECTURE",
        "PREFECTURE_JPN","CITY_CODE","CITY","CITY_JPN","OBJECT","RDC_Code","GC_Code",
        "CDC_Code","VCU_Id","CUCP_Id","CUUP_Id","Backhaul_Type","BANDWIDTH","INOUT",
        "Cluster Name",
        #"TI Flag","TI Date","Leased Flag","MIMO Path",
        "LTE SARF ID",
        "Site to RDC Mapping","Site to gNB ID Mapping","Site_Type_Class",
                                               "Property Address",
                                               "Property Name",
                                               "Entrance_GC",
                                               "Destination_GC",
                                               "FREE_NUM_1",
                                               "FREE_NUM_2",
                                               "ONAIR_DATE",
                                               "DF_Ready_Actual",
                                               "GC_Ready_Actual",
                                               "TI_Ready_Actual",
                                               "GC Application Status",
                                               "Co-location_Frequency_Band",
                                               "Co-location_SARF ID_3.7GHz",
                                               "Co-location_SARF ID_28GHz",
                                               "BS_Ready_Actual",
                                               "Project",
                                               "LL_ID",
                                               "Comments"
                                               ]]

    df_atoll_NR_cells["Site ID"] = df_atoll_NR_cells["Name"].str[:-5]
    df_atoll_NR_cells = pd.merge(df_atoll_NR_cells, df_sites_selected_fields, left_on='Site ID', right_on='Name',how='left')

    df_planet_NR_cells["Latitude"] = df_atoll_NR_cells['Latitude']
    df_planet_NR_cells["Longitude"] = df_atoll_NR_cells['Longitude']
    df_planet_NR_cells["TAC"] = df_atoll_NR_cells['TAC']
    df_planet_NR_cells["Base Station Type"] = "NR_BTS_1" # df_atoll_NR_cells["Radio Equipment"]
    df_planet_NR_cells["Custom: siteStatus"] = df_atoll_NR_cells["Sarf Status"]
    df_planet_NR_cells["Custom: sarfid"] = df_atoll_NR_cells["Site ID"]
    df_planet_NR_cells["Custom: phase"] = df_atoll_NR_cells["PHASE"]
    df_planet_NR_cells["Custom: areaCategory"] = df_atoll_NR_cells["AREA_CATEGORY"]
    df_planet_NR_cells["Custom: geographyL1"] = df_atoll_NR_cells["REGION"]
    df_planet_NR_cells["Custom: subRegion"] = df_atoll_NR_cells["SUB_REGION"]
    df_planet_NR_cells["Custom: geographyL2"] = df_atoll_NR_cells["PREFECTURE"]
    df_planet_NR_cells["Custom: prefectureJpn"] = df_atoll_NR_cells["PREFECTURE_JPN"]+ " "
    df_planet_NR_cells["Custom: cityCode"] = df_atoll_NR_cells["CITY_CODE"]
    df_planet_NR_cells["Custom: geographyL3"] = df_atoll_NR_cells["CITY"]
    df_planet_NR_cells["Custom: geographyL4"] = df_atoll_NR_cells["Cluster Name"]
    df_planet_NR_cells["Custom: cityJpn"] = df_atoll_NR_cells["CITY_JPN"]+ " "
    df_planet_NR_cells["Custom: object"] = df_atoll_NR_cells["OBJECT"]
    df_planet_NR_cells["Custom: rdcCode"] = df_atoll_NR_cells["RDC_Code"]
    df_planet_NR_cells["Custom: gcCode"] = df_atoll_NR_cells["GC_Code"]
    df_planet_NR_cells["Custom: cdcCode"] = df_atoll_NR_cells["CDC_Code"]
    df_planet_NR_cells["Custom: vcuId"] = df_atoll_NR_cells["VCU_Id"]

    df_planet_NR_cells["Custom: bandwidth"] = df_atoll_NR_cells["BANDWIDTH"]
    df_planet_NR_cells["Custom: siteTypeIndoorOutdoor"] = df_atoll_NR_cells["INOUT"]
    df_planet_NR_cells["Custom: siteToRdcMapping"] = ""
    df_planet_NR_cells["Custom: siteToGnbIdMapping"] = ""
    df_planet_NR_cells["Custom: rsi"] = df_atoll_NR_cells["RSI_5G"]
    df_planet_NR_cells["Custom: ulGroupAssignmentPusch"] = df_atoll_NR_cells["Site to RDC Mapping"]
    df_planet_NR_cells["Custom: ulPuschCyclicShiftCell"] = df_atoll_NR_cells["Site to gNB ID Mapping"]
    df_planet_NR_cells["Custom: riuId"] = df_atoll_NR_cells["RIU_Id"]

    # df_planet_NR_cells["Custom: PCI"] = df_atoll_NR_cells["PCI_5G"]
    df_planet_NR_cells["Custom: tiFlag"] = "null"# df_atoll_NR_cells["TI Flag"]
    df_planet_NR_cells["Custom: tiDate"] = "null"# df_atoll_NR_cells["TI Date"]
    df_planet_NR_cells["Custom: leasedFlag"] = "null"# df_atoll_NR_cells["Leased Flag"]
    df_planet_NR_cells["Custom: mimoPath"] = "null"# df_atoll_NR_cells["MIMO Path"]
    df_planet_NR_cells["Custom: retTilt"] = df_atoll_NR_cells["Additional Electrical Downtilt (°)"]
    df_planet_NR_cells["Custom: rrhNo"] = df_atoll_NR_cells["RRH_Number"]
    df_planet_NR_cells["Custom: transmitterType"] = df_atoll_NR_cells["Transmitter Type"]
    # df_planet_NR_cells["Custom: Neighbour LTE Anchor"] = df_atoll_NR_cells["LTE SARF ID"]
    df_planet_NR_cells["Custom: siteTypeClass"] = df_atoll_NR_cells["Site_Type_Class"]

    df_planet_NR_cells["Custom: free1"] = 'null'
    df_planet_NR_cells["Custom: free2"] = 'null'
    df_planet_NR_cells["Custom: free3"] = 'null'
    df_planet_NR_cells["Custom: free4"] = 'null'
    df_planet_NR_cells["Custom: free5"] = 'null'
    df_planet_NR_cells["Custom: free6"] = 'null'

    df_planet_NR_cells["Custom: propertyAddress"] = df_atoll_NR_cells["Property Address"]
    df_planet_NR_cells["Custom: propertyName"] = df_atoll_NR_cells["Property Name"]
    df_planet_NR_cells["Custom: entranceGc"] = df_atoll_NR_cells["Entrance_GC"]
    df_planet_NR_cells["Custom: destinationGc"] = df_atoll_NR_cells["Destination_GC"]
    df_planet_NR_cells["Custom: freeNum1"] = df_atoll_NR_cells["FREE_NUM_1"]
    df_planet_NR_cells["Custom: freeNum2"] = df_atoll_NR_cells["FREE_NUM_2"]
    df_planet_NR_cells["Custom: onairDate"] = df_atoll_NR_cells["ONAIR_DATE"]
    df_planet_NR_cells["Custom: dfReadyActual"] = df_atoll_NR_cells["DF_Ready_Actual"]
    df_planet_NR_cells["Custom: gcReadyActual"] = df_atoll_NR_cells["GC_Ready_Actual"]
    df_planet_NR_cells["Custom: tiReadyActual"] = df_atoll_NR_cells["TI_Ready_Actual"]
    df_planet_NR_cells["Custom: gcApplicationStatus"] = df_atoll_NR_cells["GC Application Status"]
    df_planet_NR_cells["Custom: coLocationFrequencyBand"] = df_atoll_NR_cells["Co-location_Frequency_Band"]
    df_planet_NR_cells["Custom: coLocationSarfId37GHz"] = df_atoll_NR_cells["Co-location_SARF ID_3.7GHz"]
    df_planet_NR_cells["Custom: coLocationSarfId28GHz"] = df_atoll_NR_cells["Co-location_SARF ID_28GHz"]
    df_planet_NR_cells["Custom: bsReadyActual"] = df_atoll_NR_cells["BS_Ready_Actual"]
    df_planet_NR_cells["Custom: llid"] = df_atoll_NR_cells["LL_ID"]
    df_planet_NR_cells["Custom: comments"] = df_atoll_NR_cells["Comments"]
    df_planet_NR_cells["Custom: project"] = df_atoll_NR_cells["Project"]

    df_planet_NR_cells["Beamforming"] = False
    df_planet_NR_cells["Beamforming Configuration"] = ''
    df_planet_NR_cells["Apply Beamforming To Control Channels/Signals"] = False

    # for i in df_atoll_bf_antennas_list:
        # df_planet_NR_cells.loc[df_atoll_NR_cells["Beamforming Model"] == i, "Beamforming"] = True

    df_atoll_NR_cells.loc[df_atoll_NR_cells["REGION"] == 'E_KINKI', "REGION"] = 'E_KANSAI'
    df_atoll_NR_cells.loc[df_atoll_NR_cells["REGION"] == 'B_SHINETSU', "REGION"] = 'A_KANTO'
    # df_atoll_NR_cells.loc[df_atoll_NR_cells["REGION"] == 'D_HOKURIKU', "REGION"] = 'E_KANSAI'
    # df_atoll_NR_cells.loc[df_atoll_NR_cells["REGION"] == 'G_SHIKOKU', "REGION"] = 'F_CHUGOKU'
    df_atoll_NR_cells.loc[df_atoll_NR_cells["REGION"] == 'O_OKINAWA', "REGION"] = 'H_KYUSHU'
    df_atoll_NR_cells["Frequency Band"] = df_atoll_NR_cells["Frequency Band"].str.replace(' ','_')
    df_atoll_NR_cells["Frequency Band"] = df_atoll_NR_cells["Frequency Band"].str.replace('-_', '')
    # df_planet_NR_cells["Propagation Model"] = "P3M_"+df_atoll_NR_cells["REGION"].str[2:] +"_NR_Band" +"_"+df_atoll_NR_cells["Frequency Band"].str[:-7]+'.pmf'
    df_planet_NR_cells["Propagation Model"] = "P3M_"+df_atoll_NR_cells["REGION"].str[2:] +"_mmW_" +"Macro"+'.pmf'

    df_planet_NR_cells.loc[df_planet_NR_cells["Custom: object"] == "Utility_Pole","Propagation Model"] =  "P3M_" + df_atoll_NR_cells["REGION"].str[2:] + "_mmW_" + "Pole"+'.pmf'
    df_planet_NR_cells.loc[df_planet_NR_cells["Band Name"] == "n77 - 100MHz", "Propagation Model"] = "P3M_" + df_atoll_NR_cells["REGION"].str[2:] + "_Sub6"+ '.pmf'


    df_planet_NR_cells["Propagation Model"].fillna("P3M-Rakuten-1900MHz.pmf",inplace = True)

    df_planet_NR_cells["Custom: geographyL1"] = df_planet_NR_cells["Custom: geographyL1"].str[2:]

    # df_planet_NR_cells["Custom: geographyL1"].fillna("null",inplace = True)
    # df_planet_NR_cells["Custom: geographyL2"].fillna("null",inplace = True)
    # df_planet_NR_cells["Custom: geographyL3"].fillna("null",inplace = True)
    # df_planet_NR_cells["Custom: geographyL4"].fillna("null",inplace = True)

    columns_to_fill_null = ["Custom: areaCategory",
                            "Custom: active",
                            "Custom: backhaulType",
                            "Custom: bandwidth",
                            "Custom: cdcCode",
                            "Custom: cityCode",
                            "Custom: cityJpn",
                            "Custom: cucpId",
                            "Custom: cuupId",
                            "Custom: gcCode",
                            "Custom: object",
                            "Custom: prefectureJpn",
                            "Custom: phase",
                            "Custom: rdcCode",
                            "Custom: riuId",
                            "Custom: rsi",
                            "Custom: ruId",
                            "Custom: sarfid",
                            "Custom: subRegion",
                            "Custom: siteTypeIndoorOutdoor",
                            "Custom: siteToRdcMapping",
                            "Custom: siteToGnbIdMapping",
                            "Custom: ulGroupAssignmentPusch",
                            "Custom: ulPuschCyclicShiftCell",
                            "Custom: vcuId",
                            "Custom: vduId",
                            "Custom: zeroCorrelationZone",
                            "Custom: geographyL1",
                            "Custom: geographyL2",
                            "Custom: geographyL3",
                            "Custom: geographyL4",
                            "Custom: siteStatus",
                            "Custom: tiFlag",
                            "Custom: tiDate",
                            "Custom: leasedFlag",
                            "Custom: mimoPath",
                            "Custom: retTilt",
                            "Custom: rrhNo",
                            "Custom: transmitterType",
                            "Custom: siteTypeClass",
                            "Custom: free1",
                            "Custom: free2",
                            "Custom: free3",
                            "Custom: free4",
                            "Custom: free5",
                            "Custom: free6",
                            "Custom: propertyAddress",
                            "Custom: propertyName",
                            "Custom: entranceGc",
                            "Custom: destinationGc",
                            "Custom: freeNum1",
                            "Custom: freeNum2",
                            "Custom: onairDate",
                            "Custom: dfReadyActual",
                            "Custom: gcReadyActual",
                            "Custom: tiReadyActual",
                            "Custom: gcApplicationStatus",
                            "Custom: coLocationFrequencyBand",
                            "Custom: coLocationSarfId37GHz",
                            "Custom: coLocationSarfId28GHz",
                            "Custom: bsReadyActual",
                            "Custom: llid",
                            "Custom: comments",
                            "Custom: project"
                            ]
    for column in columns_to_fill_null:
        df_planet_NR_cells[column].fillna("null", inplace=True)


    df_planet_NR_cells["First Zadoff Chu Sequence"] = df_atoll_NR_cells["Prachconfigindex"]

    # Radius and resolution settings
    df_planet_NR_cells["Distance (km)"] = df_atoll_NR_cells["Extended Calculation Radius (m)"]/1000
    df_planet_NR_cells["Inner Area Radius (m)"] = df_atoll_NR_cells["Main Calculation Radius (m)"]
    df_planet_NR_cells["Output Resolution (m)"] = df_atoll_NR_cells["Main Resolution (m)"]
    df_planet_NR_cells["Outer Area Resolution (m)"] = df_atoll_NR_cells["Extended Resolution (m)"]

    df_planet_NR_cells.loc[df_atoll_NR_cells["Extended Resolution (m)"].isnull(), "Distance (km)"] = df_planet_NR_cells["Inner Area Radius (m)"]/1000
    df_planet_NR_cells.loc[df_atoll_NR_cells["Extended Resolution (m)"].isnull(), "Outer Area Resolution (m)"] = df_planet_NR_cells["Output Resolution (m)"]


    # df_planet_NR_cells_rural_urban_class(df_planet_NR_cells,file_list)

    return df_planet_NR_cells
    # export_csv = df_planet_NR_cells.to_csv("Planet NR Cell File.csv", index=None, header=True)

def point_check_P(p1,gdf_reg):
    # print(gdf_reg['geometry'])
    # iterating polygons inside the multipolygon
    a = 'no'
    for k in gdf_reg['geometry']:
        # print(k)
        if p1.within(k):
            a = 'urban'
            break
        else:
            a = 'rural'
    return a

def df_planet_lte_cells_rural_urban_class(df_planet_lte_cells,file_list):
    import fiona
    import geopandas as gpd
    from shapely.geometry import Point, Polygon
    import pandas as pd
    import webbrowser
    import numpy as np
    import os
    import time


    df_tab_file = gpd.read_file(file_list[7], driver="MapInfo File")

    start = time.time()
    local_time = time.ctime(start)
    print("Local time:", local_time)

    gdf_reg = df_tab_file.explode()
    df_planet_lte_cells['Urban_Rural'] = df_planet_lte_cells.apply(lambda x: point_check_P((Point(x['Longitude'], x['Latitude'])),gdf_reg), axis=1)

    df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "urban", "Propagation Model"] = df_planet_lte_cells["Propagation Model"].str[ :-4] + "_urban.pmf"
    df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "rural", "Propagation Model"] = df_planet_lte_cells["Propagation Model"].str[ :-4] + "_rural.pmf"

    # df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "urban", "Distance (km)"] = 3
    # df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "rural", "Distance (km)"] = 10
    del df_planet_lte_cells["Urban_Rural"]
    end = time.time()
    print(end - start)

    return df_planet_lte_cells

def df_planet_NR_cells_rural_urban_class(df_planet_NR_cells,file_list):
    import fiona
    import geopandas as gpd
    from shapely.geometry import Point, Polygon
    import pandas as pd
    import webbrowser
    import numpy as np
    import os
    import time

    df_tab_file = gpd.read_file(file_list[7], driver="MapInfo File")

    start = time.time()
    local_time = time.ctime(start)
    print("Local time:", local_time)

    gdf_reg = df_tab_file.explode()
    df_planet_NR_cells['Urban_Rural'] = df_planet_NR_cells.apply(lambda x: point_check_P((Point(x['Longitude'], x['Latitude'])),gdf_reg), axis=1)

    # df_planet_NR_cells.loc[df_planet_NR_cells["Urban_Rural"] == "urban", "Distance (km)"] = 3
    # df_planet_NR_cells.loc[df_planet_NR_cells["Urban_Rural"] == "rural", "Distance (km)"] = 10

    end = time.time()
    print(end - start)

    del df_planet_NR_cells["Urban_Rural"]

    return df_planet_NR_cells

def Check_Input_Data(file_list):
    import pandas as pd

    lte_cells = file_list[0]
    NR_cells = file_list[1]
    sites = file_list[2]
    transmitters = file_list[3]

    df_atoll_transmitters = pd.read_csv(transmitters, low_memory=False, index_col=False, encoding='cp932')
    df = pd.read_csv(lte_cells, low_memory=False, index_col=False, encoding='CP932')
    df_NR = pd.read_csv(NR_cells, low_memory=False, index_col=False, encoding='CP932')

    df_atoll_sites = pd.read_csv(sites, low_memory=False, index_col=False, encoding='cp932')

    column_list = ['Transmitter', 'Height (m)', 'Frequency Band', 'Azimuth (°)', 'Mechanical Downtilt (°)', 'Antenna',
                   'Main Calculation Radius (m)','Noise Figure (dB)']
    df = pd.merge(df, df_atoll_transmitters[column_list], on='Transmitter', how='left')
    df.loc[df["Carrier"] == 'Band 3 - 20MHz (0)', 'Downlink ARFCN'] = 1500
    df.loc[df["Carrier"] == 'Band 3 - 5MHz (0)', 'Downlink ARFCN'] = 1425
    df["Electrical Tilt"] = df["Antenna"].str[-3:-1]
    df["Electrical Tilt"] = df["Electrical Tilt"].astype(float)

    df_NR = pd.merge(df_NR, df_atoll_transmitters[column_list], on='Transmitter', how='left')
    df_NR.loc[df_NR["Carrier"] == 'n77 - 100MHz (0)', 'Downlink ARFCN'] = 656666
    df_NR.loc[df_NR["Carrier"] == 'n257 - 400MHz (0)', 'Downlink ARFCN'] = 2065833
    df_NR["Electrical Tilt"] = df_NR["Antenna"].str[-3:-1]
    df_NR["Electrical Tilt"] = df_NR["Electrical Tilt"].astype(float)

    df = df.append(df_NR)

    df_atoll_sites["Site ID"] = df_atoll_sites["Name"]
    df_sites = df_atoll_sites[["Site ID","Latitude", "Longitude","TAC","Sarf Status",
        "PHASE","AREA_CATEGORY","REGION","SUB_REGION","PREFECTURE",
        "PREFECTURE_JPN","CITY_CODE","CITY","CITY_JPN","OBJECT","RDC_Code","GC_Code",
        "CDC_Code","VCU_Id","CUCP_Id","CUUP_Id","Backhaul_Type"]]


    df["Site ID"] = df["Name"].str[:-5]
    df["Distance (km)"] = df['Main Calculation Radius (m)'].div(1000)
    df = pd.merge(df, df_sites, left_on='Site ID', right_on='Site ID',how='left')

    import os
    try:
        os.mkdir('output')
    except:
        a = 1

    error_log = "output\Atoll_data_errors.csv"
    file_1 = open(error_log, "w")
    file_1.close()

    df_1 = df.loc[ df["Height (m)"] > 300000 ]
    df_2 = df.loc[ df["Height (m)"] < 0]
    error_height = pd.concat([df_1,df_2])
    if len(error_height) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Height error \n\n")
        file_1.close()
        error_height.to_csv(error_log, mode='a', index=True)
        # webbrowser.open(error_log)

    df_1 = df.loc[df["Mechanical Downtilt (°)"] < -90]
    df_2 = df.loc[df["Mechanical Downtilt (°)"] > 90]
    error_Mtilt = pd.concat([df_1, df_2])
    if len(error_Mtilt) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Mechanical Downtilt error \n\n")
        file_1.close()
        error_Mtilt.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Electrical Tilt"] < -90]
    df_2 = df.loc[df["Electrical Tilt"] > 90]
    error_Etilt = pd.concat([df_1, df_2])
    if len(error_Etilt) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Electrical Tilt error \n\n")
        file_1.close()
        error_Etilt.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Distance (km)"] < 0.01]
    df_2 = df.loc[df["Distance (km)"] > 1000]
    error_Distance = pd.concat([df_1, df_2])
    if len(error_Distance) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Distance error \n\n")
        file_1.close()
        error_Distance.to_csv(error_log, mode='a', index=True)


    df_1 = df.loc[df["Noise Figure (dB)"] < 0]
    df_2 = df.loc[df["Noise Figure (dB)"] > 100]
    error_Noise_Figure = pd.concat([df_1, df_2])
    if len(error_Noise_Figure) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Noise Figure error \n\n")
        file_1.close()
        error_Noise_Figure.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Max Power (dBm)"] < -20]
    df_2 = df.loc[df["Max Power (dBm)"] > 100]
    error_Max_Power = pd.concat([df_1, df_2])
    if len(error_Max_Power) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Max_Power error \n\n")
        file_1.close()
        error_Max_Power.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Traffic Load (DL) (%)"] < 0]
    df_2 = df.loc[df["Traffic Load (DL) (%)"] > 100]
    error_TrafficLoadDL = pd.concat([df_1, df_2])
    if len(error_TrafficLoadDL) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n TrafficLoadDL error \n\n")
        file_1.close()
        error_TrafficLoadDL.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Traffic Load (UL) (%)"] < 0]
    df_2 = df.loc[df["Traffic Load (UL) (%)"] > 100]
    error_TrafficLoadUL = pd.concat([df_1, df_2])
    if len(error_TrafficLoadUL) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n TrafficLoadUL error \n\n")
        file_1.close()
        error_TrafficLoadUL.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["UL Noise Rise (dB)"] < 0]
    df_2 = df.loc[df["UL Noise Rise (dB)"] > 40]
    error_ULNoiseRisedB = pd.concat([df_1, df_2])
    if len(error_ULNoiseRisedB) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n UL Noise Rise (dB) error \n\n")
        file_1.close()
        error_ULNoiseRisedB.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[ df["Name"].str.len() > 255 ]
    df_2 = df.loc[ df["Name"].isnull()]
    error_CellName = pd.concat([df_1,df_2])
    if len(error_CellName) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Cell Name error \n\n")
        file_1.close()
        error_CellName.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Site ID"].str.len() > 130]
    error_Site_ID = df_1
    if len(error_Site_ID) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Site ID error \n\n")
        file_1.close()
        error_Site_ID.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Frequency Band"].str.len() > 255]
    error_Band_Name = df_1
    if len(error_Band_Name) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n * Frequency Band Name error \n\n")
        file_1.close()
        error_Band_Name.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[df["Antenna"].str.len() > 251]
    error_Antenna_File = df_1
    if len(error_Antenna_File) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Antenna Name error \n\n")
        file_1.close()
        error_Antenna_File.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[~df["Cellid"].isin(list(range(255)))& ~(df["Cellid"].isnull())]
    error_Cellid = df_1
    if len(error_Cellid) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Cellid error \n\n")
        file_1.close()
        error_Cellid.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[~df["Downlink ARFCN"].isin(list(range(3279167)))| (df["Downlink ARFCN"].isnull())]
    error_Downlink_ARFCN = df_1
    if len(error_Downlink_ARFCN) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Cellid error \n\n")
        file_1.close()
        error_Downlink_ARFCN.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[ ~df["Physical Cell ID"].isin(list(range(1007))) & ~(df["Physical Cell ID"].isnull())]
    error_Physical_Cell_ID = df_1
    if len(error_Physical_Cell_ID) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Physical Cell ID error \n\n")
        file_1.close()
        error_Physical_Cell_ID.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[ ~df["TAC"].isin(list(range(65535))) & ~(df["TAC"].isnull()) ]
    error_TAC = df_1
    if len(error_TAC) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n TAC error \n\n")
        file_1.close()
        error_TAC.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[ df["Longitude"].isnull()]
    error_longitude = df_1
    if len(error_longitude) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Longitude value error \n\n")
        file_1.close()
        error_longitude.to_csv(error_log, mode='a', index=True)

    df_1 = df.loc[ df["Latitude"].isnull()]
    error_latitude = df_1
    if len(error_latitude) > 0:
        file_1 = open(error_log, "a")
        file_1.write("\n Latitude value error \n\n")
        file_1.close()
        error_latitude.to_csv(error_log, mode='a', index=True)


    my_dict_errors = {
        # Float Constraints
        " Height (m)" : len(error_height),
        " Mechanical Downtilt (°) " : len(error_Mtilt),
        " Electrical Tilt " : len(error_Etilt),
        " Distance (km) ": len(error_Distance),
        " Noise Figure (dB) ": len(error_Noise_Figure),
        " Max Power (dBm) ": len(error_Max_Power),
        " Traffic Load (DL) (%) ": len(error_TrafficLoadDL),
        " Traffic Load (UL) ": len(error_TrafficLoadUL),
        " UL Noise Rise (dB) ": len(error_ULNoiseRisedB),

        # String Constraints,
        " Cell Name ": len(error_CellName),
        " Site ID ": len(error_Site_ID),
        " Band Name ": len(error_Band_Name),
        " Antenna File ": len(error_Antenna_File),

       # # Integer Constraints,
         " Cellid ": len(error_Cellid),
         " Downlink ARFCN ": len(error_Downlink_ARFCN),
         " Physical Cell ID ": len(error_Physical_Cell_ID),
         " TAC ": len(error_TAC),

        # Other Constraints
         " Longitude" : len(error_longitude),
         " Latitude": len(error_latitude)
        # latitude

    }

    errors = {}
    for keys, values in my_dict_errors.items():
        errors.update({keys: values})
        # print(keys,values)
    no_of_errors = pd.Series(errors.values()).sum()

    return(errors,no_of_errors)

class Planet_cellfile_methods:
    def __init__(self, file_list):
        self.__Cells_LTE = file_list[0]
        self.__Sites = file_list[2]
        self.__Cells_NR = file_list[1]
        self.__Transmitters = file_list[3]
        self.__Cells_LTE_Details = file_list[5]
        self.__Cells_NR_Details = file_list[6]
        self.__Urban_Boundary = file_list[7]

    def sites(self):
        print("Creating sites table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sites").columns
        column_list = ['Site ID', 'Site UID', 'Longitude', 'Latitude', 'Description',
                       'Site Name', 'Site Name 2', 'Candidate Priority']
        df_planet_sites = pd.DataFrame(columns=column_list)

        df_atoll_sectors_1 = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors_2 = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors = df_atoll_sectors_1.append(df_atoll_sectors_2)

        site_list = df_atoll_sectors["Name"].str[:-5]

        df_atoll_sites = pd.read_csv(self.__Sites, low_memory=False, index_col=False, encoding='cp932')
        df_planet_sites["Site ID"] = df_atoll_sites["Name"]
        df_planet_sites["Longitude"] = df_atoll_sites["Longitude"]
        df_planet_sites["Latitude"] = df_atoll_sites["Latitude"]
        df_planet_sites["Candidate Priority"] = 1

        df_planet_sites = df_planet_sites[df_planet_sites["Site ID"].isin(site_list)]

        return df_planet_sites
    def sectors_LTE(self,file_list):
        print("Creating LTE sectors table")
        import pandas as pd
        import webbrowser

        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sectors").columns
        column_list = ['Site ID', 'BTS Name', 'Sector ID', 'Relay', 'Sector UID', 'Technology',
       'Band Name', 'Antenna Algorithm', 'Propagation Model', 'Distance (km)',
       'Radials', 'Prediction Mode', 'Interpolation Distance (m)',
       'Display Scheme']

        df_planet_sectors = pd.DataFrame(columns=column_list)
        df_atoll_sectors = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_sites = pd.read_csv(self.__Sites, low_memory=False, index_col=False, encoding='cp932')
        df_planet_sectors["Sector ID"] = df_atoll_sectors["Name"].str[-4:-3]
        df_planet_sectors["BTS Name"] = "LTE FDD_" + df_atoll_sectors["Carrier"].str[:-4]
        df_planet_sectors["Site ID"] = df_atoll_sectors["Name"].str[:-5]
        df_planet_sectors["Band Name"] = df_atoll_sectors["Carrier"].str[:-4]
        df_planet_sectors["Distance (km)"] = 10
        df_planet_sectors["Radials"] = 1080
        df_planet_sectors["Relay"] = "FALSE"
        df_planet_sectors["Technology"] = "LTE FDD"
        df_planet_sectors["Antenna Algorithm"] = "LTE\MIMO.ALGR"
        df_planet_sectors["Propagation Model"] = "<Generic>"
        df_planet_sectors["Prediction Mode"] = "Modeled"
        df_planet_sectors["Interpolation Distance (m)"] = 200
        df_planet_sectors["Display Scheme"] = "N/A"


        df_sites_selected_fields = df_atoll_sites[["Name", "Latitude", "Longitude","TAC","Sarf Status",
        "PHASE","AREA_CATEGORY","REGION","SUB_REGION","PREFECTURE",
        "PREFECTURE_JPN","CITY_CODE","CITY","CITY_JPN","OBJECT","RDC_Code","GC_Code",
        "CDC_Code","VCU_Id","CUCP_Id","CUUP_Id","Backhaul_Type","BANDWIDTH","INOUT","Cluster Name",
        "LTE SARF ID","Site to RDC Mapping","Site to gNB ID Mapping",'Site_Type_Class']]
        df_atoll_sectors["Site ID"] = df_atoll_sectors["Name"].str[:-5]
        df_atoll_sectors = pd.merge(df_atoll_sectors, df_sites_selected_fields, left_on='Site ID', right_on='Name',
                                      how='left')

        df_planet_sectors["Longitude"] = df_atoll_sectors["Longitude"]
        df_planet_sectors["Latitude"] = df_atoll_sectors["Latitude"]

        df_atoll_sectors.loc[df_atoll_sectors["REGION"] == 'E_KINKI', "REGION"] = 'E_KANSAI'
        df_atoll_sectors.loc[df_atoll_sectors["REGION"] == 'B_SHINETSU', "REGION"] = 'A_KANTO'
        # df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'D_HOKURIKU', "REGION"] = 'E_KANSAI'
        # df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'G_SHIKOKU', "REGION"] = 'F_CHUGOKU'
        df_atoll_sectors.loc[df_atoll_sectors["REGION"] == 'O_OKINAWA', "REGION"] = 'H_KYUSHU'
        # df_atoll_sectors["Frequency Band"] = df_atoll_sectors["Frequency Band"].str.replace(' ', '_')
        # df_atoll_sectors["Frequency Band"] = df_atoll_sectors["Frequency Band"].str.replace('-_', '')

        df_planet_sectors["Propagation Model"] = "P3M_" + df_atoll_sectors["REGION"].str[2:] + "_LTE_FDD_Band_3" + '.pmf'

        df_planet_sectors["Propagation Model"].fillna("P3M-Rakuten-1900MHz.pmf", inplace=True)


        df_planet_sectors = df_planet_lte_cells_rural_urban_class(df_planet_sectors,file_list)
        del df_planet_sectors["Longitude"]
        del df_planet_sectors["Latitude"]

        return (df_planet_sectors)
    def sectors_NR(self,file_list):
        print("Creating NR sectors table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sectors").columns
        column_list = ['Site ID', 'BTS Name', 'Sector ID', 'Relay', 'Sector UID', 'Technology',
         'Band Name', 'Antenna Algorithm', 'Propagation Model', 'Distance (km)',
         'Radials', 'Prediction Mode', 'Interpolation Distance (m)',
         'Display Scheme']
        df_planet_sectors = pd.DataFrame(columns=column_list)
        df_atoll_sectors = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sites = pd.read_csv(self.__Sites, low_memory=False, index_col=False, encoding='cp932')

        df_planet_sectors["Sector ID"] = df_atoll_sectors["Name"].str[-4:-3]
        df_planet_sectors["Site ID"] = df_atoll_sectors["Name"].str[:-5]
        df_planet_sectors["BTS Name"] = "NR_" + df_atoll_sectors["Carrier"].str[:-4]
        df_planet_sectors["Band Name"] = df_atoll_sectors["Carrier"].str[:-4]
        df_planet_sectors["Distance (km)"] = 10
        df_planet_sectors["Radials"] = 1080
        df_planet_sectors["Relay"] = "FALSE"
        df_planet_sectors["Technology"] = "NR"
        df_planet_sectors["Antenna Algorithm"] = "NR\MIMO.ALGR"
        df_planet_sectors["Propagation Model"] = "<Generic>"
        df_planet_sectors["Prediction Mode"] = "Modeled"
        df_planet_sectors["Interpolation Distance (m)"] = 200
        df_planet_sectors["Display Scheme"] = "N/A"

        df_sites_selected_fields = df_atoll_sites[["Name", "Latitude", "Longitude","TAC","Sarf Status",
        "PHASE","AREA_CATEGORY","REGION","SUB_REGION","PREFECTURE",
        "PREFECTURE_JPN","CITY_CODE","CITY","CITY_JPN","OBJECT","RDC_Code","GC_Code",
        "CDC_Code","VCU_Id","CUCP_Id","CUUP_Id","Backhaul_Type","BANDWIDTH","INOUT","Cluster Name",
        "LTE SARF ID","Site to RDC Mapping","Site to gNB ID Mapping",'Site_Type_Class']]
        df_atoll_sectors["Site ID"] = df_atoll_sectors["Name"].str[:-5]
        df_atoll_sectors = pd.merge(df_atoll_sectors, df_sites_selected_fields, left_on='Site ID', right_on='Name',
                                      how='left')

        # df_planet_NR_cells["Custom: object"] = df_atoll_NR_cells[]
        df_planet_sectors["Custom: object"] = df_atoll_sectors["OBJECT"]

        df_planet_sectors["Longitude"] = df_atoll_sectors["Longitude"]
        df_planet_sectors["Latitude"] = df_atoll_sectors["Latitude"]

        df_atoll_sectors.loc[df_atoll_sectors["REGION"] == 'E_KINKI', "REGION"] = 'E_KANSAI'
        df_atoll_sectors.loc[df_atoll_sectors["REGION"] == 'B_SHINETSU', "REGION"] = 'A_KANTO'
        # df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'D_HOKURIKU', "REGION"] = 'E_KANSAI'
        # df_atoll_lte_cells.loc[df_atoll_lte_cells["REGION"] == 'G_SHIKOKU', "REGION"] = 'F_CHUGOKU'
        df_atoll_sectors.loc[df_atoll_sectors["REGION"] == 'O_OKINAWA', "REGION"] = 'H_KYUSHU'
        # df_atoll_sectors["Frequency Band"] = df_atoll_sectors["Frequency Band"].str.replace(' ', '_')
        # df_atoll_sectors["Frequency Band"] = df_atoll_sectors["Frequency Band"].str.replace('-_', '')

        df_planet_sectors["Propagation Model"] = "P3M_" + df_atoll_sectors["REGION"].str[2:] + "_mmW_" + "Macro" + '.pmf'

        df_planet_sectors.loc[df_planet_sectors["Custom: object"] == "Utility_Pole", "Propagation Model"] = "P3M_" + df_atoll_sectors["REGION"].str[2:] + "_mmW_" + "Pole" + '.pmf'
        df_planet_sectors.loc[df_planet_sectors["Band Name"] == "n77 - 100MHz", "Propagation Model"] = "P3M_" + df_atoll_sectors["REGION"].str[2:] + "_Sub6" + '.pmf'

        df_planet_sectors["Propagation Model"].fillna("P3M-Rakuten-1900MHz.pmf", inplace=True)

        df_planet_sectors = df_planet_NR_cells_rural_urban_class(df_planet_sectors,file_list)

        del df_planet_sectors["Longitude"]
        del df_planet_sectors["Latitude"]

        return (df_planet_sectors)
    def antennas(self):
        print("Creating antenna table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antennas").columns
        column_list = ['Site ID', 'Antenna ID', 'Longitude', 'Latitude', 'Antenna File',
       'Height (m)', 'Azimuth', 'Mechanical Tilt', 'Twist', 'Donor Antenna',
       'Terrain Height (m)', 'Sectors', 'Number of Corrections',
       'Correction (dB) at -180 degrees', 'Correction (dB) at -150 degrees',
       'Correction (dB) at -120 degrees', 'Correction (dB) at -90 degrees',
       'Correction (dB) at -60 degrees', 'Correction (dB) at -30 degrees',
       'Correction (dB) at 0 degrees', 'Correction (dB) at 30 degrees',
       'Correction (dB) at 60 degrees', 'Correction (dB) at 90 degrees',
       'Correction (dB) at 120 degrees', 'Correction (dB) at 150 degrees']

        df_planet_antennas = pd.DataFrame(columns=column_list)
        df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_sectors_1 = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors_2 = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors = df_atoll_sectors_1.append(df_atoll_sectors_2)
        site_list = df_atoll_sectors["Name"].str[:-5]

        df_planet_antennas["Site ID"] = df_atoll_Transmitters["Site"]
        df_planet_antennas["Antenna ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_antennas["Longitude"] = df_atoll_Transmitters["Longitude"]
        df_planet_antennas["Latitude"] = df_atoll_Transmitters["Latitude"]
        df_planet_antennas["Antenna File"] = df_atoll_Transmitters["Antenna"].str[:-4] + ".pafx"
        # df_planet_antennas["Antenna File"] = "<Generic>"
        df_planet_antennas["Height (m)"] = df_atoll_Transmitters["Height (m)"]
        df_planet_antennas["Azimuth"] = df_atoll_Transmitters["Azimuth (°)"]
        df_planet_antennas["Mechanical Tilt"] = df_atoll_Transmitters["Mechanical Downtilt (°)"]
        df_planet_antennas["Twist"] = 0
        df_planet_antennas["Donor Antenna"] = "FALSE"
        df_planet_antennas["Terrain Height (m)"] = "0"
        df_planet_antennas["Sectors"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_antennas["Number of Corrections"] = 12
        df_planet_antennas["Correction (dB) at -180 degrees"] = 0
        df_planet_antennas["Correction (dB) at -150 degrees"] = 0
        df_planet_antennas["Correction (dB) at -120 degrees"] = 0
        df_planet_antennas["Correction (dB) at -90 degrees"] = 0
        df_planet_antennas["Correction (dB) at -60 degrees"] = 0
        df_planet_antennas["Correction (dB) at -30 degrees"] = 0
        df_planet_antennas["Correction (dB) at 0 degrees"] = 0
        df_planet_antennas["Correction (dB) at 30 degrees"] = 0
        df_planet_antennas["Correction (dB) at 60 degrees"] = 0
        df_planet_antennas["Correction (dB) at 90 degrees"] = 0
        df_planet_antennas["Correction (dB) at 120 degrees"] = 0
        df_planet_antennas["Correction (dB) at 150 degrees"] = 0

        df_planet_antennas = df_planet_antennas[df_planet_antennas["Site ID"].isin(site_list)]

        return (df_planet_antennas)
    def sector_antennas(self):
        print("Creating sector antennas table")
        import pandas as pd

        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sector_Antennas").columns
        column_list = ['Site ID', 'Sector ID', 'Antenna ID', 'MIMO Group',
       'Horizontal Beamwidth', 'Vertical Beamwidth', 'Link Configuration ID',
       'Cable Length (m)', 'Power Split (%)',
       'Downlink Beamforming Configuration',
       'Uplink Beamforming Configuration', 'Pattern List: PSS/SSS/BCH',
       'Pattern List: CSI-RS', 'Pattern List: PDCCH', 'Pattern List: PDSCH',
       'Pattern List: PUCCH', 'Pattern List: PUSCH', 'Pattern List: PRACH']

        df_planet_sector_antennas = pd.DataFrame(columns=column_list)
        df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_lte_sectors = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]
        df_atoll_nr_sectors = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]

        df_atoll_sectors = df_atoll_lte_sectors.append(df_atoll_nr_sectors)

        df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters, on="Transmitter", how='left')

        df_planet_sector_antennas["Site ID"] = df_atoll_Transmitters["Site"]
        df_planet_sector_antennas["Sector ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_sector_antennas["Antenna ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_sector_antennas["MIMO Group"] = 1
        df_planet_sector_antennas["Link Configuration ID"] = "Default"
        df_planet_sector_antennas["Cable Length (m)"] = df_atoll_Transmitters["Transmission losses (dB)"]/100
        df_planet_sector_antennas["Power Split (%)"] = 100
        df_planet_sector_antennas["Downlink Beamforming Configuration"] = "None"
        df_planet_sector_antennas["Uplink Beamforming Configuration"] = "None"

        return (df_planet_sector_antennas)
    def sector_antenna_ports(self):
        print("Creating sector antenna ports table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sector_Antenna_Ports").columns
        column_list = ['Site ID', 'Sector ID', 'Antenna ID', 'Port Name', 'Downlink', 'Uplink','Number Of Ports']

        df_planet_sector_antenna_ports = pd.DataFrame(columns=column_list)
        df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_lte_sectors = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]

        df_atoll_nr_sectors = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]

        df_atoll_sectors = df_atoll_lte_sectors.append(df_atoll_nr_sectors)
        df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters, on="Transmitter", how='left')

        df_planet_sector_antenna_ports["Site ID"] = df_atoll_Transmitters["Site"]
        df_planet_sector_antenna_ports["Sector ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_sector_antenna_ports["Antenna ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_sector_antenna_ports["Port Name"] = "Port 1"

        df_planet_sector_antenna_ports["no_of_ports"] = df_atoll_Transmitters["Number of Transmission Antennas"]
        # 4 by 4 mimo port assignments LTE
        df_2 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 4]
        df_2["Port Name"] = "Port 2"
        df_3 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 4]
        df_3["Port Name"] = "Port 3"
        df_4 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 4]
        df_4["Port Name"] = "Port 4"

        df_2 = df_2.append(df_3)
        df_2 = df_2.append(df_4)
        df_planet_sector_antenna_ports = df_planet_sector_antenna_ports.append(df_2)

        # 4 by 4 mimo port assignments NR
        dfn1_2 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 128]
        dfn1_2["Port Name"] = "Port 2"
        dfn1_3 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 128]
        dfn1_3["Port Name"] = "Port 3"
        dfn1_4 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 128]
        dfn1_4["Port Name"] = "Port 4"

        dfn1_2 = dfn1_2.append(dfn1_3)
        dfn1_2 = dfn1_2.append(dfn1_4)
        df_planet_sector_antenna_ports = df_planet_sector_antenna_ports.append(dfn1_2)

        # 4 by 4 mimo port assignments NR
        dfn2_2 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 32]
        dfn2_2["Port Name"] = "Port 2"
        dfn2_3 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 32]
        dfn2_3["Port Name"] = "Port 3"
        dfn2_4 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 32]
        dfn2_4["Port Name"] = "Port 4"

        # print(df_2.head(10).columns)
        dfn2_2 = dfn2_2.append(dfn2_3)
        dfn2_2 = dfn2_2.append(dfn2_4)
        df_planet_sector_antenna_ports = df_planet_sector_antenna_ports.append(dfn2_2)


        # 2 by 2 mimo port assignments

        df_5 = df_planet_sector_antenna_ports[df_planet_sector_antenna_ports["no_of_ports"] == 2]
        df_5["Port Name"] = "Port 2"
        df_planet_sector_antenna_ports = df_planet_sector_antenna_ports.append(df_5)

        del df_planet_sector_antenna_ports["no_of_ports"]
        df_planet_sector_antenna_ports["Downlink"] = "TRUE"
        df_planet_sector_antenna_ports["Uplink"] = "TRUE"
        df_planet_sector_antenna_ports["Number Of Ports"] = 1


        return (df_planet_sector_antenna_ports)
    def sector_antenna_ports_original(self):
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sector_Antenna_Ports").columns
        column_list = ['Site ID', 'Sector ID', 'Antenna ID', 'Port Name', 'Downlink', 'Uplink','Number Of Ports']

        df_planet_sector_antenna_ports = pd.DataFrame(columns=column_list)
        df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_lte_sectors = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]
        df_atoll_nr_sectors = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]

        df_atoll_sectors = df_atoll_lte_sectors.append(df_atoll_nr_sectors)
        df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters, on="Transmitter", how='left')

        df_planet_sector_antenna_ports["Site ID"] = df_atoll_Transmitters["Site"]
        df_planet_sector_antenna_ports["Sector ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_sector_antenna_ports["Antenna ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_sector_antenna_ports["Port Name"] = "Port 1"
        df_planet_sector_antenna_ports["Downlink"] = "TRUE"
        df_planet_sector_antenna_ports["Uplink"] = "TRUE"
        df_planet_sector_antenna_ports["Number Of Ports"] = 1

        return (df_planet_sector_antenna_ports)
    def LTE_FDD_Sectors(self):
        import pandas as pd


        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "LTE_FDD_Sectors").columns
        column_list = ['Site ID', 'Sector ID', 'Cellular Layer', 'Transmit Mask',
       'Receive Filter', 'Limit Best Server Coverage (km)',
       'Maximum Number of Subscribers', 'Maximum Uplink Noise Rise (dB)',
       'Maximum Number Of Users Per TTI', 'PA Power (dBm)', 'Total EIRP (dBm)',
       'Reference Signal Power Boosting (dB)',
       'Synchronization and broadcast power boosting (dB)', 'Power Recycling',
       'Number Of Selected Downlink Ports', 'Number Of Selected Uplink Ports',
       'Recycle Power From All Antenna Ports', 'Reference Signal Power (dBm)',
       'Synchronization Signal Power (dBm)',
       'Reference Signal Power Per RE (dBm)',
       'Synchronization Signal Power Per RE (dBm)',
       'Broadcast Channel Power Per RE (dBm)', 'PDSCH Power Per RE (dBm)',
       'Downlink Other Systems Interference (dBm)',
       'NB-IoT Carrier Power Boosting (dB)', 'NB Reference Signal Power (dBm)',
       'NB Synchronization Signal Power (dBm)',
       'NB Reference Signal Power Per RE (dBm)', 'NPDSCH Power Per RE (dBm)',
       'PUSCH Power Control Scheme', 'P0,PUSCH (dBm)',
       'PUSCH Pathloss Compensation Factor (alpha)',
       'PUCCH Power Control Scheme', 'P0,PUCCH (dBm)',
       'PUCCH Format 1/1A Power Offset (dB)',
       'PUCCH Format 1B Power Offset (dB)', 'PUCCH Format 2 Power Offset (dB)',
       'PUCCH Format 3 Power Offset (dB)',
       'Average PRACH interference power (dBm)',
       'Uplink Other Systems Interference (dBm)',
       'Average NPRACH Interference Power (dBm)',
       'NPUSCH Power Control Scheme', 'P0,NPUSCH (dBm)',
       'NPUSCH Pathloss Compensation Factor (alpha)', 'Beamforming',
       'Frame Configuration', 'Physical Cell ID', 'Physical Cell ID Group',
       'Physical Layer ID', 'Cyclic Shift Configuration', 'Cyclic Shift Set',
       'Cyclic Shift (Ncs)', 'Zadoff Chu Sequences Needed',
       'Reserved Zadoff Chu Sequences', 'First Zadoff Chu Sequence',
       'CE Mode A Level 0/1 Threshold (dBm)', 'CE Mode A/B Threshold (dBm)',
       'Number of Required Carriers', 'A3 Handover Threshold (dB)',
       'Number Of NB-IoT Carriers Per LTE Carrier', 'Inner Cell Threshold',
       'Inner Cell RSRQ threshold (dB)', 'Inner Cell CQI Threshold',
       'Outer Cell Resource Block Group', 'Outer Cell Power Boost (dB)',
       'Outer Cell Resource Elements Usage (%)',
       'Cell Selection Offset - Release 8 (dB)',
       'Cell Selection Offset - Release 9 (dB)',
       'Cell Selection Offset - Release 10 (dB)',
       'Cell Selection Offset - Release 11 (dB)',
       'Cell Selection Offset - Release 12 (dB)',
       'Cell Selection Offset - Release 13 (dB)', 'Cross-Carrier Scheduling',
       'Almost Blank Subframes (eICIC)', 'Carrier: Band 3 - 20MHz_SB1_1',
       'Carrier: Band 3 - 5MHz_SB1_1', 'Carrier: LTE_FDD_Band_SB1_1',
       'Carrier: LTE_FDD_Band_SB1_2']

        df_planet_LTE_FDD_Sectors = pd.DataFrame(columns=column_list)

        df_atoll_Cells_LTE = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_Cells_LTE_details = pd.read_csv(self.__Cells_LTE_Details, low_memory=False, index_col=False)
        # print(df_atoll_Cells_LTE_details .columns)

        column_list_2 = [
            "Name",
            "RS EPRE (CE) (dBm)",
            "SS EPRE (dBm)",
            "PBCH EPRE (dBm)",
            "PDCCH EPRE (CE) (dBm)",
            "PDSCH EPRE (CE) (dBm)"
        ]

        df_atoll_Cells_LTE = pd.merge(df_atoll_Cells_LTE, df_atoll_Cells_LTE_details[column_list_2], on='Name', how='left')

        df_planet_LTE_FDD_Sectors["Reference Signal Power Per RE (dBm)"] = df_atoll_Cells_LTE["RS EPRE (CE) (dBm)"]
        df_planet_LTE_FDD_Sectors["Synchronization Signal Power Per RE (dBm)"] = df_atoll_Cells_LTE["SS EPRE (dBm)"]
        df_planet_LTE_FDD_Sectors["Broadcast Channel Power Per RE (dBm)"] = df_atoll_Cells_LTE["PBCH EPRE (dBm)"]
        df_planet_LTE_FDD_Sectors["PDCCH Power Per RE (dBm)"] = df_atoll_Cells_LTE["PDCCH EPRE (CE) (dBm)"]
        df_planet_LTE_FDD_Sectors["PDSCH Power Per RE (dBm)"] = df_atoll_Cells_LTE["PDSCH EPRE (CE) (dBm)"]

        df_planet_LTE_FDD_Sectors["Site ID"] = df_atoll_Cells_LTE["Name"].str[:-5]
        df_planet_LTE_FDD_Sectors["Sector ID"] = df_atoll_Cells_LTE["Transmitter"].str[-1:]
        df_planet_LTE_FDD_Sectors["Limit Best Server Coverage (km)"] = 35
        df_planet_LTE_FDD_Sectors["Maximum Number of Subscribers"] = 100
        df_planet_LTE_FDD_Sectors["Maximum Uplink Noise Rise (dB)"] = 15
        df_planet_LTE_FDD_Sectors["Maximum Number Of Users Per TTI"] = 100
        df_planet_LTE_FDD_Sectors["PA Power (dBm)"] = df_atoll_Cells_LTE["Max Power (dBm)"]
        df_planet_LTE_FDD_Sectors["Total EIRP (dBm)"] = 59.4426575
        df_planet_LTE_FDD_Sectors["Reference Signal Power Boosting (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Synchronization and broadcast power boosting (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Power Recycling"] = "Reference Signal Resource Elements"
        df_planet_LTE_FDD_Sectors["Number Of Selected Downlink Ports"] = 1
        df_planet_LTE_FDD_Sectors["Number Of Selected Uplink Ports"] = 1
        df_planet_LTE_FDD_Sectors["Recycle Power From All Antenna Ports"] = "TRUE"
        df_planet_LTE_FDD_Sectors["Reference Signal Power (dBm)"] = 38.2184868
        df_planet_LTE_FDD_Sectors["Synchronization Signal Power (dBm)"] = 33.1684456
        df_planet_LTE_FDD_Sectors["Reference Signal Power Per RE (dBm)"] = 15.2081871
        df_planet_LTE_FDD_Sectors["Synchronization Signal Power Per RE (dBm)"] = 15.2445307
        df_planet_LTE_FDD_Sectors["Broadcast Channel Power Per RE (dBm)"] = 15.236372
        df_planet_LTE_FDD_Sectors["PDSCH Power Per RE (dBm)"] = 15.21029
        df_planet_LTE_FDD_Sectors["Downlink Other Systems Interference (dBm)"] = -200
        df_planet_LTE_FDD_Sectors["PUSCH Power Control Scheme"] = "Fractional"
        df_planet_LTE_FDD_Sectors["P0,PUSCH (dBm)"] = -65
        df_planet_LTE_FDD_Sectors["PUSCH Pathloss Compensation Factor (alpha)"] = 1
        df_planet_LTE_FDD_Sectors["PUCCH Power Control Scheme"] = "Fractional"
        df_planet_LTE_FDD_Sectors["P0,PUCCH (dBm)"] = -65
        df_planet_LTE_FDD_Sectors["PUCCH Format 1/1A Power Offset (dB)"] = 0
        df_planet_LTE_FDD_Sectors["PUCCH Format 1B Power Offset (dB)"] = 0
        df_planet_LTE_FDD_Sectors["PUCCH Format 2 Power Offset (dB)"] = 0
        df_planet_LTE_FDD_Sectors["PUCCH Format 3 Power Offset (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Average PRACH interference power (dBm)"] = -200
        df_planet_LTE_FDD_Sectors["Uplink Other Systems Interference (dBm)"] = -200

        df_planet_LTE_FDD_Sectors["Automatic Powers"] = "FALSE"

        df_planet_LTE_FDD_Sectors["Cyclic Shift Configuration"] = 8
        df_planet_LTE_FDD_Sectors["Cyclic Shift Set"] = "Restricted"
        df_planet_LTE_FDD_Sectors["Cyclic Shift (Ncs)"] = 68
        df_planet_LTE_FDD_Sectors["Zadoff Chu Sequences Needed"] = 6
        df_planet_LTE_FDD_Sectors["First Zadoff Chu Sequence"] = 0
        df_planet_LTE_FDD_Sectors["Number of Required Carriers"] = 1
        df_planet_LTE_FDD_Sectors["A3 Handover Threshold (dB)"] = 6
        df_planet_LTE_FDD_Sectors["Inner Cell Threshold"] = "RSRQ"
        df_planet_LTE_FDD_Sectors["Inner Cell RSRQ threshold (dB)"] = -10
        df_planet_LTE_FDD_Sectors["Inner Cell CQI Threshold"] = 5
        df_planet_LTE_FDD_Sectors["Outer Cell Resource Block Group"] = 1
        df_planet_LTE_FDD_Sectors["Outer Cell Power Boost (dB)"] = 3
        df_planet_LTE_FDD_Sectors["Outer Cell Resource Elements Usage (%)"] = 100
        df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 8 (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 9 (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 10 (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 11 (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 12 (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 13 (dB)"] = 0
        df_planet_LTE_FDD_Sectors["Cross-Carrier Scheduling"] = "FALSE"
        df_planet_LTE_FDD_Sectors["Almost Blank Subframes (eICIC)"] = "FALSE"
        df_planet_LTE_FDD_Sectors["Carrier: Band 3 - 20MHz_SB1_1"] = df_atoll_Cells_LTE["Carrier"]
        df_planet_LTE_FDD_Sectors["Carrier: Band 3 - 5MHz_SB1_1"] = df_atoll_Cells_LTE["Carrier"]
        # df.loc[df['First Season'] > 1990, 'First Season'] = 1
        df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                          "Carrier: Band 3 - 5MHz_SB1_1"] == "Band 3 - 5MHz (0)", "Frame Configuration"] = "Frame Configuration (Band 3 - 5MHz)"
        df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                          "Carrier: Band 3 - 20MHz_SB1_1"] == "Band 3 - 20MHz (0)", "Frame Configuration"] = "Frame Configuration (Band 3 - 20MHz)"

        df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                          "Carrier: Band 3 - 20MHz_SB1_1"] == "Band 3 - 20MHz (0)", "Carrier: Band 3 - 20MHz_SB1_1"] = "Allocated"
        df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                          "Carrier: Band 3 - 20MHz_SB1_1"] == "Band 3 - 5MHz (0)", "Carrier: Band 3 - 20MHz_SB1_1"] = "Unused"

        df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                          "Carrier: Band 3 - 5MHz_SB1_1"] == "Band 3 - 20MHz (0)", "Carrier: Band 3 - 5MHz_SB1_1"] = "Unused"
        df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                          "Carrier: Band 3 - 5MHz_SB1_1"] == "Band 3 - 5MHz (0)", "Carrier: Band 3 - 5MHz_SB1_1"] = "Allocated"

        df_planet_LTE_FDD_Sectors["Carrier: LTE_FDD_Band_SB1_1"] = "Unused"
        df_planet_LTE_FDD_Sectors["Carrier: LTE_FDD_Band_SB1_2"] = "Unused"

        return (df_planet_LTE_FDD_Sectors)
    def LTE_FDD_Sector_Carriers(self):
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "LTE_FDD_Sector_Carriers").columns
        column_list = ['Site ID', 'Sector ID', 'Carrier Name', 'NB-IoT In-band Carrier',
         'Cell ID', 'Carrier Aggregation', 'Secondary Cell Selection',
         'Top N Neighbors', 'Cell Name', 'E-UTRAN Cell ID', 'TAC',
         'Downlink Load (%)', 'Maximum Uplink Load (%)',
         'Maximum Downlink Load (%)', 'Uplink Load (%)',
         'Downlink Traffic (Mbps)', 'Uplink Traffic (Mbps)',
         'PUSCH Noise Rise (dB)', 'PUCCH Noise Rise (dB)', 'FFR Usage (%)',
         'Almost Blank Subframes (%)', 'NPUSCH Noise Rise (dB)',
         'Maximum Number Of Downlink Co-Scheduled Users',
         'Maximum Number Of Uplink Co-Scheduled Users']

        df_planet_LTE_FDD_Sector_Carriers = pd.DataFrame(columns=column_list)
        df_atoll_sectors = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')

        df_planet_LTE_FDD_Sector_Carriers["Site ID"] = df_atoll_sectors["Name"].str[:-5]
        df_planet_LTE_FDD_Sector_Carriers["Sector ID"] = df_atoll_sectors["Transmitter"].str[-1]
        df_planet_LTE_FDD_Sector_Carriers["Carrier Name"] = df_atoll_sectors["Carrier"].str[:-4] + "_SB1_1"
        df_planet_LTE_FDD_Sector_Carriers["Carrier Aggregation"] = "TRUE"
        df_planet_LTE_FDD_Sector_Carriers["Secondary Cell Selection"] = "AllCells"
        df_planet_LTE_FDD_Sector_Carriers["TAC"] = 0
        df_planet_LTE_FDD_Sector_Carriers["Downlink Load (%)"] = 50
        df_planet_LTE_FDD_Sector_Carriers["Maximum Uplink Load (%)"] = 100
        df_planet_LTE_FDD_Sector_Carriers["Maximum Downlink Load (%)"] = 100
        df_planet_LTE_FDD_Sector_Carriers["Uplink Load (%)"] = 0
        df_planet_LTE_FDD_Sector_Carriers["Downlink Traffic (Mbps)"] = 10
        df_planet_LTE_FDD_Sector_Carriers["Uplink Traffic (Mbps)"] = 10
        df_planet_LTE_FDD_Sector_Carriers["PUSCH Noise Rise (dB)"] = 3
        df_planet_LTE_FDD_Sector_Carriers["PUCCH Noise Rise (dB)"] = 3
        df_planet_LTE_FDD_Sector_Carriers["FFR Usage (%)"] = 0
        return df_planet_LTE_FDD_Sector_Carriers
    def NR_Sectors(self):
        import pandas as pd

        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "NR_Sectors").columns

        column_list = ['Site ID', 'Sector ID', 'Limit Best Server Coverage (km)',
         'PA Power (dBm)', 'Total EIRP (dBm)',
         'Number Of Selected Downlink Ports', 'Number Of Selected Uplink Ports',
         'Automatic Powers', 'PSS Power Per RE (dBm)', 'SSS Power Per RE (dBm)',
         'PBCH Power Per RE (dBm)', 'DM-RS Power Per RE (dBm)',
         'CSI-RS Power Per RE (dBm)', 'PDCCH Power Per RE (dBm)',
         'PDSCH Power Per RE (dBm)', 'Downlink Other Systems Interference (dBm)',
         'PUSCH Power Control Scheme', 'P0,PUSCH - 15 kHz (dBm)',
         'PUSCH Pathloss Compensation Factor (alpha)',
         'PUCCH Power Control Scheme', 'P0,PUCCH (dBm)',
         'Average PRACH interference power (dBm)',
         'Uplink Other Systems Interference (dBm)', 'Beamforming',
         'Apply Beamforming To Control Channels/Signals', 'Frame Configuration',
         'Physical Cell ID', 'Physical Cell ID Group', 'Physical Layer ID',
         'Cyclic Shift Configuration', 'Cyclic Shift Set', 'Cyclic Shift (Ncs)',
         'Zadoff Chu Sequences Needed', 'Reserved Zadoff Chu Sequences',
         'First Zadoff Chu Sequence', 'Number of Required Carriers',
         'Handover Threshold (dB)', 'Maximum Uplink Noise Rise (dB)',
         'Maximum Number of Subscribers', 'Carrier: n257 - 400MHz_SB1_1',
         'Carrier: n77 - 100MHz_SB1_1', 'Carrier: NR_Band_SB1_1']

        df_planet_NR_Sectors = pd.DataFrame(columns=column_list)
        df_atoll_Cells_NR = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_Cells_NR_details = pd.read_csv(self.__Cells_NR_Details, low_memory=False, index_col=False)  # , encoding='cp932')

        column_list_2 = [
                        "Name",
                        # "SSS EPRE (dBm)",
                        "PSS EPRE (dBm)",
                        "PBCH EPRE (dBm)",
                        "PDCCH EPRE (dBm)",
                        "PDSCH EPRE (dBm)" ]

        df_atoll_Cells_NR = pd.merge(df_atoll_Cells_NR, df_atoll_Cells_NR_details[column_list_2], on='Name', how='left')
        # print(df_atoll_Cells_NR.columns)

        df_planet_NR_Sectors["SSS Power Per RE (dBm)"] = df_atoll_Cells_NR["SSS EPRE (dBm)"]
        df_planet_NR_Sectors["PSS Power Per RE (dBm)"] = df_atoll_Cells_NR["PSS EPRE (dBm)"]
        df_planet_NR_Sectors["PBCH Power Per RE (dBm)"] = df_atoll_Cells_NR["PBCH EPRE (dBm)"]
        df_planet_NR_Sectors["PDCCH Power Per RE (dBm)"] = df_atoll_Cells_NR["PDCCH EPRE (dBm)"]
        df_planet_NR_Sectors["PDSCH Power Per RE (dBm)"] = df_atoll_Cells_NR["PDSCH EPRE (dBm)"]

        df_planet_NR_Sectors["Site ID"] = df_atoll_Cells_NR["Name"].str[:-5]
        df_planet_NR_Sectors["Sector ID"] = df_atoll_Cells_NR["Transmitter"].str[-1:]
        df_planet_NR_Sectors["Limit Best Server Coverage (km)"] = 35
        df_planet_NR_Sectors["PA Power (dBm)"] = df_atoll_Cells_NR["Max Power (dBm)"]
        df_planet_NR_Sectors["Total EIRP (dBm)"] = 59.4426575
        df_planet_NR_Sectors["Number Of Selected Downlink Ports"] = 1
        df_planet_NR_Sectors["Number Of Selected Uplink Ports"] = 1
        df_planet_NR_Sectors["Automatic Powers"] = "FALSE"
        df_planet_NR_Sectors["Downlink Other Systems Interference (dBm)"] = -200
        df_planet_NR_Sectors["PUSCH Power Control Scheme"] = "Fractional"
        df_planet_NR_Sectors["PUCCH Power Control Scheme"] = "Fractional"
        df_planet_NR_Sectors["Average PRACH interference power (dBm)"] = -200
        df_planet_NR_Sectors["Uplink Other Systems Interference (dBm)"] = -200
        df_planet_NR_Sectors["P0,PUCCH (dBm)"] = -65
        df_planet_NR_Sectors["P0,PUSCH - 15 kHz (dBm)"] = -65
        df_planet_NR_Sectors['PUSCH Pathloss Compensation Factor (alpha)'] = 1

        df_planet_NR_Sectors["Cyclic Shift Configuration"] = 6
        df_planet_NR_Sectors["Cyclic Shift Set"] = "Not Applicable"
        df_planet_NR_Sectors["Cyclic Shift (Ncs)"] = 12
        df_planet_NR_Sectors["Zadoff Chu Sequences Needed"] = 6
        df_planet_NR_Sectors["First Zadoff Chu Sequence"] = 0
        df_planet_NR_Sectors["Number of Required Carriers"] = 1
        df_planet_NR_Sectors["Handover Threshold (dB)"] = 6
        df_planet_NR_Sectors["Maximum Uplink Noise Rise (dB)"] = 15
        df_planet_NR_Sectors["Maximum Number of Subscribers"] = 100

        df_planet_NR_Sectors["Carrier: n257 - 400MHz_SB1_1"] = df_atoll_Cells_NR["Carrier"]
        df_planet_NR_Sectors["Carrier: n77 - 100MHz_SB1_1"] = df_atoll_Cells_NR["Carrier"]

        df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                     "Carrier: n257 - 400MHz_SB1_1"] == "n257 - 400MHz (0)", "Frame Configuration"] = "Frame Configuration_1 (n257 - 400MHz)"
        df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                     "Carrier: n77 - 100MHz_SB1_1"] == "n77 - 100MHz (0)", "Frame Configuration"] = "Frame Configuration_1 (n77 - 100MHz)"

        df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                     "Carrier: n257 - 400MHz_SB1_1"] == "n257 - 400MHz (0)", "Carrier: n257 - 400MHz_SB1_1"] = "Allocated"
        df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                     "Carrier: n257 - 400MHz_SB1_1"] == "n77 - 100MHz (0)", "Carrier: n257 - 400MHz_SB1_1"] = "Unused"

        df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                     "Carrier: n77 - 100MHz_SB1_1"] == "n257 - 400MHz (0)", "Carrier: n77 - 100MHz_SB1_1"] = "Unused"
        df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                     "Carrier: n77 - 100MHz_SB1_1"] == "n77 - 100MHz (0)", "Carrier: n77 - 100MHz_SB1_1"] = "Allocated"

        df_planet_NR_Sectors["Carrier: NR_Band_SB1_1"] = "Unused"
        return df_planet_NR_Sectors
    def NR_Sector_Carriers(self):
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "NR_Sector_Carriers").columns

        column_list = ['Site ID', 'Sector ID', 'Carrier Name', 'Cell ID',
       'Carrier Aggregation', 'Secondary Cell Selection', 'Top N Neighbors',
       'Downlink Load (%)', 'Downlink Traffic (Mbps)', 'Uplink Traffic (Mbps)',
       'PUSCH Noise Rise (dB)', 'PUCCH Noise Rise (dB)', 'Uplink Load (%)',
       'Maximum Downlink Load (%)', 'Maximum Uplink Load (%)',
       'Maximum Number Of Downlink Co-Scheduled Users',
       'Maximum Number Of Uplink Co-Scheduled Users']

        df_planet_NR_Sector_Carriers = pd.DataFrame(columns=column_list)
        df_atoll_sectors = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')

        df_planet_NR_Sector_Carriers["Site ID"] = df_atoll_sectors["Name"].str[:-5]
        df_planet_NR_Sector_Carriers["Sector ID"] = df_atoll_sectors["Transmitter"].str[-1]
        df_planet_NR_Sector_Carriers["Carrier Name"] = df_atoll_sectors["Carrier"].str[:-4] + "_SB1_1"
        df_planet_NR_Sector_Carriers["Carrier Aggregation"] = "TRUE"
        df_planet_NR_Sector_Carriers["Secondary Cell Selection"] = "AllCells"
        df_planet_NR_Sector_Carriers["Downlink Load (%)"] = 50
        df_planet_NR_Sector_Carriers["Downlink Traffic (Mbps)"] = 10
        df_planet_NR_Sector_Carriers["Uplink Traffic (Mbps)"] = 10
        df_planet_NR_Sector_Carriers["PUSCH Noise Rise (dB)"] = 3
        df_planet_NR_Sector_Carriers["PUCCH Noise Rise (dB)"] = 3
        df_planet_NR_Sector_Carriers["Uplink Load (%)"] = 0
        df_planet_NR_Sector_Carriers["Maximum Downlink Load (%)"] = 100
        df_planet_NR_Sector_Carriers["Maximum Uplink Load (%)"] = 100

        return df_planet_NR_Sector_Carriers
    def Antenna_Electrical_Parameters(self):
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antenna_Electrical_Parameters").columns
        column_list = ['Site ID', 'Antenna ID', 'Electrical Controller', 'Electrical Tilt','Electrical Azimuth', 'Electrical Beamwidth']

        df_planet_Antenna_Electrical_Parameters = pd.DataFrame(columns=column_list)
        df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_lte_sectors = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]
        df_atoll_nr_sectors = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')["Transmitter"]

        df_atoll_sectors = df_atoll_lte_sectors.append(df_atoll_nr_sectors)
        df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters, on="Transmitter", how='left')

        # df_planet_Antenna_Electrical_Parameters["Antenna_File"] = df_atoll_Transmitters["Antenna"].str[:-4] + ".pafx"
        df_planet_Antenna_Electrical_Parameters["Site ID"] = df_atoll_Transmitters["Site"]
        df_planet_Antenna_Electrical_Parameters["Antenna ID"] = df_atoll_Transmitters["Transmitter"].str[-1:]
        df_planet_Antenna_Electrical_Parameters["Electrical Controller"] = 'All bands'
        df_planet_Antenna_Electrical_Parameters["Electrical Tilt"] = df_atoll_Transmitters["Antenna"].str[-3:-1]
        df_planet_Antenna_Electrical_Parameters["Electrical Azimuth"] = "0"
        df_planet_Antenna_Electrical_Parameters["Electrical Beamwidth"] = "70"

        # indexNames = df[(df['Antenna_File'] == 'KMW_ANT_65_16dBi.pafx') | (df['Antenna_File'] == 'KMW_RRA - I_ANT_65_16dBi.pafx')].index
        # df.drop(indexNames, inplace=True)

        # df.drop('Antenna_File', axis='columns', inplace=True)
        # del df['Antenna_File']

        # delete all rows with column 'Age' has value 30 to 40
        return df_planet_Antenna_Electrical_Parameters
    def LTE_FDD_Base_Stations(self):
        import pandas as pd
        column_list = [
            "Site ID",
            "BTS Name",
            "MCC",
            "MNC",
            "Downlink Maximum Pooled Throughput(Mbps)",
            "Uplink Maximum Pooled Throughput(Mbps)",
            "eNodeB ID",
            "Base Station Type",
            "MME Code",
            "MME Group ID",
            "MME Identity"
        ]

        df_planet_LTE_FDD_Base_Stations = pd.DataFrame(columns=column_list)
        df_atoll_sites = pd.read_csv(self.__Sites, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors_LTE = pd.read_csv(self.__Cells_LTE, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors_LTE["Site ID"] = df_atoll_sectors_LTE["Name"].str[:-5]

        df_sectors_selected_fields = df_atoll_sectors_LTE[["Site ID", "Radio Equipment","Carrier"]]

        df_atoll_sites = pd.merge(df_atoll_sites, df_sectors_selected_fields, right_on='Site ID', left_on='Name',how='left')

        site_list = df_atoll_sectors_LTE["Name"].str[:-5]

        df_atoll_sites = df_atoll_sites[df_atoll_sites["Name"].isin(site_list)]

        df_planet_LTE_FDD_Base_Stations["Site ID"] = df_atoll_sites["Name"]
        df_planet_LTE_FDD_Base_Stations["BTS Name"] = "LTE FDD_" + df_atoll_sites["Carrier"].str[:-4]
        df_planet_LTE_FDD_Base_Stations["MCC"] = 0
        df_planet_LTE_FDD_Base_Stations["MNC"] = 0
        df_planet_LTE_FDD_Base_Stations["Downlink Maximum Pooled Throughput(Mbps)"] = 500
        df_planet_LTE_FDD_Base_Stations["Uplink Maximum Pooled Throughput(Mbps)"] = 500
        df_planet_LTE_FDD_Base_Stations["eNodeB ID"] = " "
        df_planet_LTE_FDD_Base_Stations["Base Station Type"] = df_atoll_sites["Radio Equipment"]
        df_planet_LTE_FDD_Base_Stations["MME Code"] = 1
        df_planet_LTE_FDD_Base_Stations["MME Group ID"] = 0
        df_planet_LTE_FDD_Base_Stations["MME Identity"] = 1

        return df_planet_LTE_FDD_Base_Stations

    def NR_Base_Stations(self):
        import pandas as pd
        column_list = [
            "Site ID",
            "BTS Name",
            "MCC",
            "MNC",
            "gNodeB ID",
            "gNodeB ID Length(bits)",
            "Master eNodeB IDs",
            "Downlink Maximum Pooled Throughput(Mbps)",
            "Uplink Maximum Pooled Throughput(Mbps)",
            "Base Station Type",
            "MME Code",
            "MME Group ID",
            "MME Identity",
            "AMF Region ID",
            "AMF Set ID",
            "AMF Pointer ID",
            "AMF Identity"
        ]

        df_planet_NR_Base_Stations = pd.DataFrame(columns=column_list)
        df_atoll_sites = pd.read_csv(self.__Sites, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors_NR = pd.read_csv(self.__Cells_NR, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_sectors_NR["Site ID"] = df_atoll_sectors_NR["Name"].str[:-5]

        df_sectors_selected_fields = df_atoll_sectors_NR[["Site ID", "Radio Equipment","Carrier"]]

        df_atoll_sites = pd.merge(df_atoll_sites, df_sectors_selected_fields, right_on='Site ID', left_on='Name',how='left')

        site_list = df_atoll_sectors_NR["Name"].str[:-5]

        df_atoll_sites = df_atoll_sites[df_atoll_sites["Name"].isin(site_list)]

        df_planet_NR_Base_Stations["Site ID"]=df_atoll_sites["Name"]
        df_planet_NR_Base_Stations["BTS Name"] = "NR_" + df_atoll_sites["Carrier"].str[:-4]
        df_planet_NR_Base_Stations["MCC"]=0
        df_planet_NR_Base_Stations["MNC"]=0
        df_planet_NR_Base_Stations["gNodeB ID"]=""
        df_planet_NR_Base_Stations["gNodeB ID Length(bits)"]="28"
        df_planet_NR_Base_Stations["Master eNodeB IDs"]=""
        df_planet_NR_Base_Stations["Downlink Maximum Pooled Throughput(Mbps)"]=500
        df_planet_NR_Base_Stations["Uplink Maximum Pooled Throughput(Mbps)"]=500
        df_planet_NR_Base_Stations["Base Station Type"]=df_atoll_sites["Radio Equipment"]
        df_planet_NR_Base_Stations["MME Code"]=1
        df_planet_NR_Base_Stations["MME Group ID"]=0
        df_planet_NR_Base_Stations["MME Identity"]=1
        df_planet_NR_Base_Stations["AMF Region ID"]=""
        df_planet_NR_Base_Stations["AMF Set ID"]=""
        df_planet_NR_Base_Stations["AMF Pointer ID"]=""
        df_planet_NR_Base_Stations["AMF Identity"]=""

        return df_planet_NR_Base_Stations

    def flags(self):
        import pandas as pd
        df_atoll_Sites = pd.read_csv(self.__Sites, low_memory=False, index_col=False, encoding='cp932')

        df_planet_flag1 = pd.DataFrame(columns=['Name', 'Condition Name', 'Active'])
        df_planet_flag1['Condition Name'] = df_atoll_Sites.PHASE.unique()
        df_planet_flag1['Name'] = "PHASE"

        df_planet_flag2 = pd.DataFrame(columns=['Name', 'Condition Name', 'Active'])
        df_planet_flag2['Condition Name'] = df_atoll_Sites['Sarf Status'].unique()
        df_planet_flag2['Name'] = "Sarf_Status"

        df_planet_flag3 = pd.DataFrame(columns=['Name', 'Condition Name', 'Active'])
        df_planet_flag3['Condition Name'] = df_atoll_Sites['AREA_CATEGORY'].unique()
        df_planet_flag3['Name'] = "AREA_CATEGORY"

        df_planet_flag4 = pd.DataFrame(columns=['Name', 'Condition Name', 'Active'])
        df_planet_flag4['Condition Name'] = df_atoll_Sites['REGION'].unique()
        df_planet_flag4['Name'] = "REGION"

        df_planet_flag5 = pd.DataFrame(columns=['Name', 'Condition Name', 'Active'])
        df_planet_flag5['Condition Name'] = df_atoll_Sites['SUB_REGION'].unique()
        df_planet_flag5['Name'] = "SUB_REGION"

        df_planet_flag6 = pd.DataFrame(columns=['Name', 'Condition Name', 'Active'])
        df_planet_flag6['Condition Name'] = df_atoll_Sites['PREFECTURE'].unique()
        df_planet_flag6['Name'] = "PREFECTURE"

        # df_planet_flag7 = pd.DataFrame(columns=['Name','Condition Name','Active'])
        # df_planet_flag7['Condition Name'] = df_atoll_Sites['CITY'].unique()
        # df_planet_flag7['Name'] = "CITY"

        df_planet_flags = df_planet_flag1.append(df_planet_flag2)
        df_planet_flags = df_planet_flags.append(df_planet_flag3)
        df_planet_flags = df_planet_flags.append(df_planet_flag4)
        df_planet_flags = df_planet_flags.append(df_planet_flag5)
        df_planet_flags = df_planet_flags.append(df_planet_flag6)
        # df_planet_flags = df_planet_flags.append(df_planet_flag7)

        df_planet_flags['Active'] = "FALSE"
        df_planet_flags = df_planet_flags.dropna()

        return df_planet_flags

def Atoll_to_planet_Desktop_excel(file_list):
    import webbrowser
    import pandas as pd
    import os

    df = Planet_cellfile_methods(file_list)

    import os
    try:
        os.mkdir('output')
    except:
        a = 1
    # try:
    with pd.ExcelWriter('output\Planet_import_file_desktop.xlsx') as writer:
        df.sites().to_excel(writer, sheet_name="Sites", index=False)
        sectors = df.sectors_LTE().append(df.sectors_NR())
        sectors.to_excel(writer, sheet_name="Sectors", index=False)
        df.antennas().to_excel(writer, sheet_name="Antennas", index=False)
        df.Antenna_Electrical_Parameters().to_excel(writer, sheet_name="Antenna_Electrical_Parameters", index=False)
        df.sector_antennas().to_excel(writer, sheet_name="Sector_Antennas", index=False)
        df.sector_antenna_ports().to_excel(writer, sheet_name="Sector_Antenna_Ports", index=False)
        df.LTE_FDD_Sectors().to_excel(writer, sheet_name="LTE_FDD_Sectors", index=False)
        df.LTE_FDD_Sector_Carriers().to_excel(writer, sheet_name="LTE_FDD_Sector_Carriers", index=False)
        df.NR_Sectors().to_excel(writer, sheet_name="NR_Sectors", index=False)
        df.NR_Sector_Carriers().to_excel(writer, sheet_name="NR_Sector_Carriers", index=False)
    message = "The import file 'Planet_import_file_desktop.xlsx' created in output folder"
    # webbrowser.open("output\Planet_import_file_desktop.xlsx")
    return message

    # except:
        # message = "The import file cannot be created, please close the file 'Planet_import_file_desktop.xlsx' if it is open"
        # return message

def Atoll_to_planet_Desktop(file_list):
    import webbrowser
    import pandas as pd
    import os

    df = Planet_cellfile_methods(file_list)

    import os

    try:
        os.mkdir('output')
    except:
        a = 1

    try:
        os.mkdir('output/planet_desktop_csv')
        # os.mkdir('output_deneme')
    except:
        a = 1
    # try:

    df.sites().to_csv('output/planet_desktop_csv/Sites.csv', index = False, header=True)
    sectors = df.sectors_LTE(file_list).append(df.sectors_NR(file_list))
    sectors.to_csv('output/planet_desktop_csv/Sectors.csv', index = False , header=True)
    df.antennas().to_csv('output/planet_desktop_csv/Antennas.csv', index = False, header=True)
    df.Antenna_Electrical_Parameters().to_csv('output/planet_desktop_csv/Antenna_Electrical_Parameters.csv', index=False, header=True)
    df.sector_antennas().to_csv('output/planet_desktop_csv/Sector_Antennas.csv', index=False, header=True)
    df.sector_antenna_ports().to_csv('output/planet_desktop_csv/Sector_Antenna_Ports.csv', index=False, header=True)
    df.LTE_FDD_Sectors().to_csv('output/planet_desktop_csv/LTE_FDD_Sectors.csv', index=False, header=True)
    df.LTE_FDD_Sector_Carriers().to_csv('output/planet_desktop_csv/LTE_FDD_Sector_Carriers.csv', index=False, header=True)
    df.NR_Sectors().to_csv('output/planet_desktop_csv/NR_Sectors.csv', index=False, header=True)
    df.NR_Sector_Carriers().to_csv('output/planet_desktop_csv/NR_Sector_Carriers.csv', index=False, header=True)
    df.LTE_FDD_Base_Stations().to_csv('output/planet_desktop_csv/LTE_FDD_Base_Stations.csv', index=False, header=True)
    df.NR_Base_Stations().to_csv('output/planet_desktop_csv/NR_Base_Stations.csv', index=False, header=True)

    #with pd.ExcelWriter('output/Planet_import_file_desktop.xlsx') as writer:
    message = "The import files created in output folder"
    # webbrowser.open("output\Planet_import_file_desktop.xlsx")
    return message

    # except:
        # message = "The import file cannot be created, please close the file 'Planet_import_file_desktop.xlsx' if it is open"
        # return message

def Create_sectors_flags_tab(df_planet_sectors,Sites):
    import pandas as pd

    df_atoll_sites = pd.read_csv(Sites, low_memory=False, index_col=False,
                                 encoding='CP932')  # CP932 is japanese character encoding

    # adding data from sites table
    df_sites_selected_fields = df_atoll_sites[
        ["Name", "PHASE", "Sarf Status", "AREA_CATEGORY", "REGION", "SUB_REGION", "PREFECTURE"]]

    df_planet_sectors_new = pd.merge(df_planet_sectors, df_sites_selected_fields, left_on='Site ID',
                                     right_on='Name', how='left')
    dict = {"PHASE": "Flag: PHASE",
            "Sarf Status": "Flag: Sarf_Status",
            "AREA_CATEGORY": "Flag: AREA_CATEGORY",
            "REGION": "Flag: REGION",
            "SUB_REGION": "Flag: SUB_REGION",
            "PREFECTURE": "Flag: PREFECTURE",
            }

    df_planet_sectors_new.rename(columns=dict, inplace=True)

    del df_planet_sectors_new['Name']

    return df_planet_sectors_new

def Atoll_to_planet_destop_create_flags(file_list):
    import pandas as pd
    import webbrowser

    Cells_LTE = file_list[0]
    Cells_NR = file_list[1]
    Sites = file_list[2]
    transmitters = file_list[3]
    filename_bf_antennas = file_list[4]

    df_planet_sectors_LTE = Create_sectors_LTE_tab(Cells_LTE)
    df_planet_sectors_NR = Create_sectors_NR_tab(Cells_NR)
    df_planet_sectors = df_planet_sectors_LTE.append(df_planet_sectors_NR)

    df_planet_flags = create_flags_tab(Sites)
    df_planet_sectors_with_flags = Create_sectors_flags_tab(df_planet_sectors,Sites)

    with pd.ExcelWriter('Planet_import_file_with_flags.xlsx') as writer:
        df_planet_flags.to_excel(writer, sheet_name="Flags", index=False)
        df_planet_sectors_with_flags.to_excel(writer, sheet_name="Sectors", index=False)

    webbrowser.open("Planet_import_file_with_flags.xlsx")

def Create_sectors_LTE_tab(Cells_LTE):
    import pandas as pd
    column_list = pd.read_excel('Planet_import_template.xlsx', "Sectors").columns
    df_planet_sectors = pd.DataFrame(columns=column_list)
    df_atoll_sectors = pd.read_csv(Cells_LTE, low_memory=False, index_col=False, encoding='cp932')
    df_planet_sectors["Sector ID"] = df_atoll_sectors["Name"].str[-4:-3]
    df_planet_sectors["BTS Name"] = "LTE FDD"
    df_planet_sectors["Site ID"] = df_atoll_sectors["Name"].str[:-5]
    df_planet_sectors["Band Name"] = df_atoll_sectors["Carrier"].str[:-4]
    df_planet_sectors["Distance (km)"] = 10
    df_planet_sectors["Radials"] = 1080
    df_planet_sectors["Relay"] = "FALSE"
    df_planet_sectors["Technology"] = "LTE FDD"
    df_planet_sectors["Antenna Algorithm"] = "None"
    df_planet_sectors["Propagation Model"] = "<Generic>"
    df_planet_sectors["Prediction Mode"] = "Modeled"
    df_planet_sectors["Interpolation Distance (m)"] = 200
    df_planet_sectors["Display Scheme"] = "N/A"

    return (df_planet_sectors)

def Create_sectors_NR_tab(Cells_NR):
    import pandas as pd
    column_list = pd.read_excel('Planet_import_template.xlsx', "Sectors").columns
    df_planet_sectors = pd.DataFrame(columns=column_list)
    df_atoll_sectors = pd.read_csv(Cells_NR, low_memory=False, index_col=False, encoding='cp932')
    df_planet_sectors["Sector ID"] = df_atoll_sectors["Name"].str[-4:-3]
    df_planet_sectors["Site ID"] = df_atoll_sectors["Name"].str[:-5]
    df_planet_sectors["BTS Name"] = "NR"
    df_planet_sectors["Band Name"] = df_atoll_sectors["Carrier"].str[:-4]
    df_planet_sectors["Distance (km)"] = 10
    df_planet_sectors["Radials"] = 1080
    df_planet_sectors["Relay"] = "FALSE"
    df_planet_sectors["Technology"] = "NR"
    df_planet_sectors["Antenna Algorithm"] = "None"
    df_planet_sectors["Propagation Model"] = "<Generic>"
    df_planet_sectors["Prediction Mode"] = "Modeled"
    df_planet_sectors["Interpolation Distance (m)"] = 200
    df_planet_sectors["Display Scheme"] = "N/A"
    return (df_planet_sectors)

def create_flags_tab(Sites):
    import pandas as pd
    df_atoll_Sites= pd.read_csv(Sites, low_memory=False, index_col=False, encoding='cp932')

    df_planet_flag1 = pd.DataFrame(columns=['Name','Condition Name','Active'])
    df_planet_flag1['Condition Name'] = df_atoll_Sites.PHASE.unique()
    df_planet_flag1['Name'] = "PHASE"

    df_planet_flag2 = pd.DataFrame(columns=['Name','Condition Name','Active'])
    df_planet_flag2['Condition Name'] = df_atoll_Sites['Sarf Status'].unique()
    df_planet_flag2['Name'] = "Sarf_Status"

    df_planet_flag3 = pd.DataFrame(columns=['Name','Condition Name','Active'])
    df_planet_flag3['Condition Name'] = df_atoll_Sites['AREA_CATEGORY'].unique()
    df_planet_flag3['Name'] = "AREA_CATEGORY"

    df_planet_flag4 = pd.DataFrame(columns=['Name','Condition Name','Active'])
    df_planet_flag4['Condition Name'] = df_atoll_Sites['REGION'].unique()
    df_planet_flag4['Name'] = "REGION"

    df_planet_flag5 = pd.DataFrame(columns=['Name','Condition Name','Active'])
    df_planet_flag5['Condition Name'] = df_atoll_Sites['SUB_REGION'].unique()
    df_planet_flag5['Name'] = "SUB_REGION"

    df_planet_flag6 = pd.DataFrame(columns=['Name','Condition Name','Active'])
    df_planet_flag6['Condition Name'] = df_atoll_Sites['PREFECTURE'].unique()
    df_planet_flag6['Name'] = "PREFECTURE"

    # df_planet_flag7 = pd.DataFrame(columns=['Name','Condition Name','Active'])
    # df_planet_flag7['Condition Name'] = df_atoll_Sites['CITY'].unique()
    # df_planet_flag7['Name'] = "CITY"

    df_planet_flags = df_planet_flag1.append(df_planet_flag2)
    df_planet_flags = df_planet_flags.append(df_planet_flag3)
    df_planet_flags = df_planet_flags.append(df_planet_flag4)
    df_planet_flags = df_planet_flags.append(df_planet_flag5)
    df_planet_flags = df_planet_flags.append(df_planet_flag6)
    # df_planet_flags = df_planet_flags.append(df_planet_flag7)

    df_planet_flags['Active'] = "FALSE"
    df_planet_flags = df_planet_flags.dropna()

    return df_planet_flags

def Atoll_bf_to_normal_pattern_creator(pattern_file_name,min_freq,max_freq,comment):
    import pandas as pd
    import webbrowser
    import os

    # df_bf = pd.read_csv(pattern_file_name, low_memory=False, index_col=False, sep='\t',encoding='CP932')
    df_bf = pd.read_csv(pattern_file_name, low_memory=False, index_col=False) #

    print(df_bf.columns)
    file_name = os.path.basename(pattern_file_name)
    df_bf.to_csv("Atoll_" + file_name[:-4] + ".csv", index=None, header=True)

    # df = pd.read_csv("input\Atoll Antennas.txt", low_memory=False, index_col=False, sep='\t', encoding='CP932')
    # print(df.columns)

    antenna_column_names = ["Name", "Gain (dBi)", "Manufacturer", "Comments", "Pattern", "Pattern Electrical Tilt (°)",
                            "Physical Antenna", "Half-power Beamwidth", "Min Frequency (MHz)", "Max Frequency (MHz)",
                            "Pattern Electrical Azimuth (°)"]

    df_antenna = pd.DataFrame(columns=antenna_column_names)

    # export_csv = df.to_csv("output\Atoll Antennas.csv", index=None, header=True)
    # webbrowser.open("output\Atoll Antennas.csv")

    # export_csv = df_bf.to_csv(pattern_file_name[:-4] + '.csv', index=None, header=True)
    # webbrowser.open('output\\' + pattern_file_name + '.csv')

    df_antenna['Name'] = df_bf['Beamforming Model']
    df_antenna['Gain (dBi)'] = df_bf['Boresight Gain (dBi)']
    df_antenna['Manufacturer'] = 'NEC'
    df_antenna['Comments'] = comment # '3.5 GHz band: 50 MHz (3.490 - 3.540 MHz)'
    df_antenna['Pattern'] = df_bf['Beam Pattern']
    df_antenna['Pattern Electrical Tilt (°)'] = df_bf['Beam Index']#df_bf['Pattern Electrical Tilt (��)']
    df_antenna['Physical Antenna'] = pattern_file_name
    df_antenna['Half-power Beamwidth'] = df_bf['Half-power Beamwidth']
    df_antenna['Min Frequency (MHz)'] = min_freq # 3490
    df_antenna['Max Frequency (MHz)'] =max_freq # 3540
    df_antenna['Pattern Electrical Azimuth (°)'] = df_bf['Pattern Electrical Azimuth (��)']
    file_name = os.path.basename(pattern_file_name)

    import os
    try:
        os.mkdir('output')
    except:
        a = 1

    df_antenna.to_csv("output\Planet_" + file_name[:-4] + ".txt", index=None, header=True, sep='\t')


    webbrowser.open("output\Planet_" + file_name[:-4] + ".txt")

def Convert_MS_cellfile_to_desktop(MScellfile_name):
    import pandas as pd
    import webbrowser
    # df_MS_cellfile = pd.read_csv(MScellfile_name, low_memory=False, index_col=False ,encoding='cp932')
    df_MS_cellfile = pd.read_csv(MScellfile_name, low_memory=False, index_col=False)

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sites").columns
    column_list = ['Site ID', 'Site UID', 'Longitude', 'Latitude', 'Description', 'Site Name', 'Site Name 2',
                   'Candidate Priority']

    df_planet_sites = pd.DataFrame(columns=column_list)
    df_planet_sites["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_sites["Longitude"] = df_MS_cellfile["Longitude"]
    df_planet_sites["Latitude"] = df_MS_cellfile["Latitude"]
    df_planet_sites["Candidate Priority"] = 1

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sectors").columns
    column_list = ['Site ID', 'BTS Name', 'Sector ID', 'Relay', 'Sector UID', 'Technology', 'Band Name',
                   'Antenna Algorithm', 'Propagation Model', 'Distance (km)', 'Radials', 'Prediction Mode',
                   'Interpolation Distance (m)', 'Display Scheme']

    df_planet_sectors = pd.DataFrame(columns=column_list)

    df_planet_sectors["Sector ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_sectors["BTS Name"] = df_MS_cellfile["Technology"]
    df_planet_sectors["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_sectors["Band Name"] = df_MS_cellfile["Band Name"]
    df_planet_sectors["Distance (km)"] = df_MS_cellfile["Distance (km)"]
    df_planet_sectors["Radials"] = df_MS_cellfile["Radials"]
    df_planet_sectors["Relay"] = "FALSE"
    df_planet_sectors["Technology"] = df_MS_cellfile["Technology"]
    df_planet_sectors["Antenna Algorithm"] = df_MS_cellfile["Antenna Algorithm"]
    df_planet_sectors["Propagation Model"] = df_MS_cellfile["Propagation Model"]
    df_planet_sectors["Prediction Mode"] = "Modeled"
    df_planet_sectors["Interpolation Distance (m)"] = 200
    df_planet_sectors["Display Scheme"] = "N/A"

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antennas").columns
    column_list = ['Site ID', 'Antenna ID', 'Longitude', 'Latitude', 'Antenna File',
                   'Height (m)', 'Azimuth', 'Mechanical Tilt', 'Twist', 'Donor Antenna',
                   'Terrain Height (m)', 'Sectors', 'Number of Corrections',
                   'Correction (dB) at -180 degrees', 'Correction (dB) at -150 degrees',
                   'Correction (dB) at -120 degrees', 'Correction (dB) at -90 degrees',
                   'Correction (dB) at -60 degrees', 'Correction (dB) at -30 degrees',
                   'Correction (dB) at 0 degrees', 'Correction (dB) at 30 degrees',
                   'Correction (dB) at 60 degrees', 'Correction (dB) at 90 degrees',
                   'Correction (dB) at 120 degrees', 'Correction (dB) at 150 degrees']

    df_planet_antennas = pd.DataFrame(columns=column_list)
    df_planet_antennas["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_antennas["Antenna ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_antennas["Longitude"] = df_MS_cellfile["Longitude"]
    df_planet_antennas["Latitude"] = df_MS_cellfile["Latitude"]
    df_planet_antennas["Antenna File"] = df_MS_cellfile["Antenna File"]
    df_planet_antennas["Height (m)"] = df_MS_cellfile["Height (m)"]
    df_planet_antennas["Azimuth"] = df_MS_cellfile["Azimuth"]
    df_planet_antennas["Mechanical Tilt"] = df_MS_cellfile["Mechanical Tilt"]
    df_planet_antennas["Twist"] = 0
    df_planet_antennas["Donor Antenna"] = "FALSE"
    df_planet_antennas["Terrain Height (m)"] = "0"
    df_planet_antennas["Sectors"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_antennas["Number of Corrections"] = 12
    df_planet_antennas["Correction (dB) at -180 degrees"] = 0
    df_planet_antennas["Correction (dB) at -150 degrees"] = 0
    df_planet_antennas["Correction (dB) at -120 degrees"] = 0
    df_planet_antennas["Correction (dB) at -90 degrees"] = 0
    df_planet_antennas["Correction (dB) at -60 degrees"] = 0
    df_planet_antennas["Correction (dB) at -30 degrees"] = 0
    df_planet_antennas["Correction (dB) at 0 degrees"] = 0
    df_planet_antennas["Correction (dB) at 30 degrees"] = 0
    df_planet_antennas["Correction (dB) at 60 degrees"] = 0
    df_planet_antennas["Correction (dB) at 90 degrees"] = 0
    df_planet_antennas["Correction (dB) at 120 degrees"] = 0
    df_planet_antennas["Correction (dB) at 150 degrees"] = 0

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antenna_Electrical_Parameters").columns
    column_list = ['Site ID', 'Antenna ID', 'Electrical Controller', 'Electrical Tilt','Electrical Azimuth',
                   'Electrical Beamwidth']

    df_planet_Antenna_Electrical_Parameters = pd.DataFrame(columns=column_list)
    df_planet_Antenna_Electrical_Parameters["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_Antenna_Electrical_Parameters["Antenna ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_Antenna_Electrical_Parameters["Electrical Controller"] = 'All bands'
    df_planet_Antenna_Electrical_Parameters["Electrical Tilt"] = df_MS_cellfile["Electrical Tilt"]
    df_planet_Antenna_Electrical_Parameters["Electrical Azimuth"] = "0"
    df_planet_Antenna_Electrical_Parameters["Electrical Beamwidth"] = "70"

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sector_Antennas").columns
    column_list = ['Site ID', 'Sector ID', 'Antenna ID', 'MIMO Group',
                   'Horizontal Beamwidth', 'Vertical Beamwidth', 'Link Configuration ID',
                   'Cable Length (m)', 'Power Split (%)',
                   'Downlink Beamforming Configuration',
                   'Uplink Beamforming Configuration', 'Pattern List: PSS/SSS/BCH',
                   'Pattern List: CSI-RS', 'Pattern List: PDCCH', 'Pattern List: PDSCH',
                   'Pattern List: PUCCH', 'Pattern List: PUSCH', 'Pattern List: PRACH']
    df_planet_sector_antennas = pd.DataFrame(columns=column_list)

    df_planet_sector_antennas["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_sector_antennas["Sector ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_sector_antennas["Antenna ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_sector_antennas["MIMO Group"] = 1
    df_planet_sector_antennas["Link Configuration ID"] = "Default"
    df_planet_sector_antennas["Cable Length (m)"] = 25
    df_planet_sector_antennas["Power Split (%)"] = 100
    df_planet_sector_antennas["Downlink Beamforming Configuration"] = "None"
    df_planet_sector_antennas["Uplink Beamforming Configuration"] = "None"

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sector_Antenna_Ports").columns
    column_list = ['Site ID', 'Sector ID', 'Antenna ID', 'Port Name', 'Downlink', 'Uplink', 'Number Of Ports']

    df_planet_sector_antenna_ports = pd.DataFrame(columns=column_list)

    df_planet_sector_antenna_ports["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_sector_antenna_ports["Sector ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_sector_antenna_ports["Antenna ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_sector_antenna_ports["Port Name"] = "Port 1"
    df_planet_sector_antenna_ports["Downlink"] = "TRUE"
    df_planet_sector_antenna_ports["Uplink"] = "TRUE"
    df_planet_sector_antenna_ports["Number Of Ports"] = 1

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "LTE_FDD_Sectors").columns
    column_list = ['Site ID', 'Sector ID', 'Cellular Layer', 'Transmit Mask',
                   'Receive Filter', 'Limit Best Server Coverage (km)',
                   'Maximum Number of Subscribers', 'Maximum Uplink Noise Rise (dB)',
                   'Maximum Number Of Users Per TTI', 'PA Power (dBm)', 'Total EIRP (dBm)',
                   'Reference Signal Power Boosting (dB)',
                   'Synchronization and broadcast power boosting (dB)', 'Power Recycling',
                   'Number Of Selected Downlink Ports', 'Number Of Selected Uplink Ports',
                   'Recycle Power From All Antenna Ports', 'Reference Signal Power (dBm)',
                   'Synchronization Signal Power (dBm)',
                   'Reference Signal Power Per RE (dBm)',
                   'Synchronization Signal Power Per RE (dBm)',
                   'Broadcast Channel Power Per RE (dBm)', 'PDSCH Power Per RE (dBm)',
                   'Downlink Other Systems Interference (dBm)',
                   'NB-IoT Carrier Power Boosting (dB)', 'NB Reference Signal Power (dBm)',
                   'NB Synchronization Signal Power (dBm)',
                   'NB Reference Signal Power Per RE (dBm)', 'NPDSCH Power Per RE (dBm)',
                   'PUSCH Power Control Scheme', 'P0,PUSCH (dBm)',
                   'PUSCH Pathloss Compensation Factor (alpha)',
                   'PUCCH Power Control Scheme', 'P0,PUCCH (dBm)',
                   'PUCCH Format 1/1A Power Offset (dB)',
                   'PUCCH Format 1B Power Offset (dB)', 'PUCCH Format 2 Power Offset (dB)',
                   'PUCCH Format 3 Power Offset (dB)',
                   'Average PRACH interference power (dBm)',
                   'Uplink Other Systems Interference (dBm)',
                   'Average NPRACH Interference Power (dBm)',
                   'NPUSCH Power Control Scheme', 'P0,NPUSCH (dBm)',
                   'NPUSCH Pathloss Compensation Factor (alpha)', 'Beamforming',
                   'Frame Configuration', 'Physical Cell ID', 'Physical Cell ID Group',
                   'Physical Layer ID', 'Cyclic Shift Configuration', 'Cyclic Shift Set',
                   'Cyclic Shift (Ncs)', 'Zadoff Chu Sequences Needed',
                   'Reserved Zadoff Chu Sequences', 'First Zadoff Chu Sequence',
                   'CE Mode A Level 0/1 Threshold (dBm)', 'CE Mode A/B Threshold (dBm)',
                   'Number of Required Carriers', 'A3 Handover Threshold (dB)',
                   'Number Of NB-IoT Carriers Per LTE Carrier', 'Inner Cell Threshold',
                   'Inner Cell RSRQ threshold (dB)', 'Inner Cell CQI Threshold',
                   'Outer Cell Resource Block Group', 'Outer Cell Power Boost (dB)',
                   'Outer Cell Resource Elements Usage (%)',
                   'Cell Selection Offset - Release 8 (dB)',
                   'Cell Selection Offset - Release 9 (dB)',
                   'Cell Selection Offset - Release 10 (dB)',
                   'Cell Selection Offset - Release 11 (dB)',
                   'Cell Selection Offset - Release 12 (dB)',
                   'Cell Selection Offset - Release 13 (dB)', 'Cross-Carrier Scheduling',
                   'Almost Blank Subframes (eICIC)', 'Carrier: Band 3 - 20MHz_SB1_1',
                   'Carrier: Band 3 - 5MHz_SB1_1', 'Carrier: LTE_FDD_Band_SB1_1',
                   'Carrier: LTE_FDD_Band_SB1_2']

    df_planet_LTE_FDD_Sectors = pd.DataFrame(columns=column_list)

    df_planet_LTE_FDD_Sectors["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_LTE_FDD_Sectors["Sector ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_LTE_FDD_Sectors["Limit Best Server Coverage (km)"] = 35
    df_planet_LTE_FDD_Sectors["Maximum Number of Subscribers"] = 100
    df_planet_LTE_FDD_Sectors["Maximum Uplink Noise Rise (dB)"] = 15
    df_planet_LTE_FDD_Sectors["Maximum Number Of Users Per TTI"] = 100
    df_planet_LTE_FDD_Sectors["PA Power (dBm)"] = df_MS_cellfile["PA Power (dBm)"]
    # df_planet_LTE_FDD_Sectors["Total EIRP (dBm)"] =
    df_planet_LTE_FDD_Sectors["Reference Signal Power Boosting (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Synchronization and broadcast power boosting (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Power Recycling"] = "None"
    df_planet_LTE_FDD_Sectors["Number Of Selected Downlink Ports"] = 1
    df_planet_LTE_FDD_Sectors["Number Of Selected Uplink Ports"] = 1
    df_planet_LTE_FDD_Sectors["Recycle Power From All Antenna Ports"] = "FALSE"
    # df_planet_LTE_FDD_Sectors["Reference Signal Power (dBm)"] = 38.2184868
    # df_planet_LTE_FDD_Sectors["Synchronization Signal Power (dBm)"] = 33.1684456
    # df_planet_LTE_FDD_Sectors["Reference Signal Power Per RE (dBm)"] = 15.2081871
    # df_planet_LTE_FDD_Sectors["Synchronization Signal Power Per RE (dBm)"] = 15.2445307
    # df_planet_LTE_FDD_Sectors["Broadcast Channel Power Per RE (dBm)"] = 15.236372
    # df_planet_LTE_FDD_Sectors["PDSCH Power Per RE (dBm)"] = 15.21029
    df_planet_LTE_FDD_Sectors["Downlink Other Systems Interference (dBm)"] = -200
    df_planet_LTE_FDD_Sectors["PUSCH Power Control Scheme"] = "Fractional"
    df_planet_LTE_FDD_Sectors["P0,PUSCH (dBm)"] = -65
    df_planet_LTE_FDD_Sectors["PUSCH Pathloss Compensation Factor (alpha)"] = 1
    df_planet_LTE_FDD_Sectors["PUCCH Power Control Scheme"] = "Fractional"
    df_planet_LTE_FDD_Sectors["P0,PUCCH (dBm)"] = -65
    df_planet_LTE_FDD_Sectors["PUCCH Format 1/1A Power Offset (dB)"] = 0
    df_planet_LTE_FDD_Sectors["PUCCH Format 1B Power Offset (dB)"] = 0
    df_planet_LTE_FDD_Sectors["PUCCH Format 2 Power Offset (dB)"] = 0
    df_planet_LTE_FDD_Sectors["PUCCH Format 3 Power Offset (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Average PRACH interference power (dBm)"] = -200
    df_planet_LTE_FDD_Sectors["Uplink Other Systems Interference (dBm)"] = -200

    df_planet_LTE_FDD_Sectors["Cyclic Shift Configuration"] = 8
    df_planet_LTE_FDD_Sectors["Cyclic Shift Set"] = "Restricted"
    df_planet_LTE_FDD_Sectors["Cyclic Shift (Ncs)"] = 68
    df_planet_LTE_FDD_Sectors["Zadoff Chu Sequences Needed"] = 6
    df_planet_LTE_FDD_Sectors["First Zadoff Chu Sequence"] = 0
    df_planet_LTE_FDD_Sectors["Number of Required Carriers"] = 1
    df_planet_LTE_FDD_Sectors["A3 Handover Threshold (dB)"] = 6
    df_planet_LTE_FDD_Sectors["Inner Cell Threshold"] = "RSRQ"
    df_planet_LTE_FDD_Sectors["Inner Cell RSRQ threshold (dB)"] = -10
    df_planet_LTE_FDD_Sectors["Inner Cell CQI Threshold"] = 5
    df_planet_LTE_FDD_Sectors["Outer Cell Resource Block Group"] = 1
    df_planet_LTE_FDD_Sectors["Outer Cell Power Boost (dB)"] = 3
    df_planet_LTE_FDD_Sectors["Outer Cell Resource Elements Usage (%)"] = 100
    df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 8 (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 9 (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 10 (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 11 (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 12 (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Cell Selection Offset - Release 13 (dB)"] = 0
    df_planet_LTE_FDD_Sectors["Cross-Carrier Scheduling"] = "FALSE"
    df_planet_LTE_FDD_Sectors["Almost Blank Subframes (eICIC)"] = "FALSE"
    df_planet_LTE_FDD_Sectors["Carrier: Band 3 - 20MHz_SB1_1"] = df_MS_cellfile["Band Name"]
    df_planet_LTE_FDD_Sectors["Carrier: Band 3 - 5MHz_SB1_1"] = df_MS_cellfile["Band Name"]

    df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                      "Carrier: Band 3 - 5MHz_SB1_1"] == "Band 3 - 5MHz", "Frame Configuration"] = "Frame Configuration (Band 3 - 5MHz)"
    df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                      "Carrier: Band 3 - 20MHz_SB1_1"] == "Band 3 - 20MHz", "Frame Configuration"] = "Frame Configuration (Band 3 - 20MHz)"

    df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                      "Carrier: Band 3 - 20MHz_SB1_1"] == "Band 3 - 20MHz", "Carrier: Band 3 - 20MHz_SB1_1"] = "Allocated"
    df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                      "Carrier: Band 3 - 20MHz_SB1_1"] == "Band 3 - 5MHz", "Carrier: Band 3 - 20MHz_SB1_1"] = "Unused"

    df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                      "Carrier: Band 3 - 5MHz_SB1_1"] == "Band 3 - 20MHz", "Carrier: Band 3 - 5MHz_SB1_1"] = "Unused"
    df_planet_LTE_FDD_Sectors.loc[df_planet_LTE_FDD_Sectors[
                                      "Carrier: Band 3 - 5MHz_SB1_1"] == "Band 3 - 5MHz", "Carrier: Band 3 - 5MHz_SB1_1"] = "Allocated"

    df_planet_LTE_FDD_Sectors["Carrier: LTE_FDD_Band_SB1_1"] = "Unused"
    df_planet_LTE_FDD_Sectors["Carrier: LTE_FDD_Band_SB1_2"] = "Unused"

    df_planet_LTE_FDD_Sectors = df_planet_LTE_FDD_Sectors[df_planet_LTE_FDD_Sectors["Frame Configuration"].notnull()]

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "LTE_FDD_Sector_Carriers").columns
    column_list = ['Site ID', 'Sector ID', 'Carrier Name', 'NB-IoT In-band Carrier',
                   'Cell ID', 'Carrier Aggregation', 'Secondary Cell Selection',
                   'Top N Neighbors', 'Cell Name', 'E-UTRAN Cell ID', 'TAC',
                   'Downlink Load (%)', 'Maximum Uplink Load (%)',
                   'Maximum Downlink Load (%)', 'Uplink Load (%)',
                   'Downlink Traffic (Mbps)', 'Uplink Traffic (Mbps)',
                   'PUSCH Noise Rise (dB)', 'PUCCH Noise Rise (dB)', 'FFR Usage (%)',
                   'Almost Blank Subframes (%)', 'NPUSCH Noise Rise (dB)',
                   'Maximum Number Of Downlink Co-Scheduled Users',
                   'Maximum Number Of Uplink Co-Scheduled Users']
    df_planet_LTE_FDD_Sector_Carriers = pd.DataFrame(columns=column_list)

    df_planet_LTE_FDD_Sector_Carriers["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_LTE_FDD_Sector_Carriers["Sector ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_LTE_FDD_Sector_Carriers["Carrier Name"] = df_MS_cellfile["Band Name"] + "_SB1_1"
    df_planet_LTE_FDD_Sector_Carriers["Carrier Aggregation"] = "TRUE"
    df_planet_LTE_FDD_Sector_Carriers["Secondary Cell Selection"] = "AllCells"
    df_planet_LTE_FDD_Sector_Carriers["TAC"] = 0
    df_planet_LTE_FDD_Sector_Carriers["Downlink Load (%)"] = 50
    df_planet_LTE_FDD_Sector_Carriers["Maximum Uplink Load (%)"] = 100
    df_planet_LTE_FDD_Sector_Carriers["Maximum Downlink Load (%)"] = 100
    df_planet_LTE_FDD_Sector_Carriers["Uplink Load (%)"] = 0
    df_planet_LTE_FDD_Sector_Carriers["Downlink Traffic (Mbps)"] = 10
    df_planet_LTE_FDD_Sector_Carriers["Uplink Traffic (Mbps)"] = 10
    df_planet_LTE_FDD_Sector_Carriers["PUSCH Noise Rise (dB)"] = 3
    df_planet_LTE_FDD_Sector_Carriers["PUCCH Noise Rise (dB)"] = 3
    df_planet_LTE_FDD_Sector_Carriers["FFR Usage (%)"] = 0

    df_planet_LTE_FDD_Sector_Carriers = df_planet_LTE_FDD_Sector_Carriers[df_planet_LTE_FDD_Sector_Carriers["Carrier Name"] != "n257 - 400MHz_SB1_1"]
    df_planet_LTE_FDD_Sector_Carriers = df_planet_LTE_FDD_Sector_Carriers[df_planet_LTE_FDD_Sector_Carriers["Carrier Name"] != "n77 - 100MHz_SB1_1"]

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "NR_Sectors").columns
    column_list = ['Site ID', 'Sector ID', 'Limit Best Server Coverage (km)',
                   'PA Power (dBm)', 'Total EIRP (dBm)',
                   'Number Of Selected Downlink Ports', 'Number Of Selected Uplink Ports',
                   'Automatic Powers', 'PSS Power Per RE (dBm)', 'SSS Power Per RE (dBm)',
                   'PBCH Power Per RE (dBm)', 'DM-RS Power Per RE (dBm)',
                   'CSI-RS Power Per RE (dBm)', 'PDCCH Power Per RE (dBm)',
                   'PDSCH Power Per RE (dBm)', 'Downlink Other Systems Interference (dBm)',
                   'PUSCH Power Control Scheme', 'P0,PUSCH - 15 kHz (dBm)',
                   'PUSCH Pathloss Compensation Factor (alpha)',
                   'PUCCH Power Control Scheme', 'P0,PUCCH (dBm)',
                   'Average PRACH interference power (dBm)',
                   'Uplink Other Systems Interference (dBm)', 'Beamforming',
                   'Apply Beamforming To Control Channels/Signals', 'Frame Configuration',
                   'Physical Cell ID', 'Physical Cell ID Group', 'Physical Layer ID',
                   'Cyclic Shift Configuration', 'Cyclic Shift Set', 'Cyclic Shift (Ncs)',
                   'Zadoff Chu Sequences Needed', 'Reserved Zadoff Chu Sequences',
                   'First Zadoff Chu Sequence', 'Number of Required Carriers',
                   'Handover Threshold (dB)', 'Maximum Uplink Noise Rise (dB)',
                   'Maximum Number of Subscribers', 'Carrier: n257 - 400MHz_SB1_1',
                   'Carrier: n77 - 100MHz_SB1_1', 'Carrier: NR_Band_SB1_1']

    df_planet_NR_Sectors = pd.DataFrame(columns=column_list)

    df_planet_NR_Sectors["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_NR_Sectors["Sector ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_NR_Sectors["Limit Best Server Coverage (km)"] = 35
    df_planet_NR_Sectors["PA Power (dBm)"] = df_MS_cellfile["PA Power (dBm)"]
    df_planet_NR_Sectors["Total EIRP (dBm)"] = 59.4426575
    df_planet_NR_Sectors["Number Of Selected Downlink Ports"] = 1
    df_planet_NR_Sectors["Number Of Selected Uplink Ports"] = 1
    df_planet_NR_Sectors["Automatic Powers"] = "FALSE"
    df_planet_NR_Sectors["Downlink Other Systems Interference (dBm)"] = -200
    df_planet_NR_Sectors["PUSCH Power Control Scheme"] = "Fractional"
    df_planet_NR_Sectors["PUCCH Power Control Scheme"] = "Fractional"
    df_planet_NR_Sectors["Average PRACH interference power (dBm)"] = -200
    df_planet_NR_Sectors["Uplink Other Systems Interference (dBm)"] = -200

    df_planet_NR_Sectors["Cyclic Shift Configuration"] = 6
    df_planet_NR_Sectors["Cyclic Shift Set"] = "Not Applicable"
    df_planet_NR_Sectors["Cyclic Shift (Ncs)"] = 12
    df_planet_NR_Sectors["Zadoff Chu Sequences Needed"] = 6
    df_planet_NR_Sectors["First Zadoff Chu Sequence"] = 0
    df_planet_NR_Sectors["Number of Required Carriers"] = 1
    df_planet_NR_Sectors["Handover Threshold (dB)"] = 6
    df_planet_NR_Sectors["Maximum Uplink Noise Rise (dB)"] = 15
    df_planet_NR_Sectors["Maximum Number of Subscribers"] = 100

    df_planet_NR_Sectors["Carrier: n257 - 400MHz_SB1_1"] = df_MS_cellfile["Band Name"]
    df_planet_NR_Sectors["Carrier: n77 - 100MHz_SB1_1"] = df_MS_cellfile["Band Name"]

    df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                 "Carrier: n257 - 400MHz_SB1_1"] == "n257 - 400MHz", "Frame Configuration"] = "Frame Configuration_1 (n257 - 400MHz)"
    df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                 "Carrier: n77 - 100MHz_SB1_1"] == "n77 - 100MHz", "Frame Configuration"] = "Frame Configuration_1 (n77 - 100MHz)"

    df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                 "Carrier: n257 - 400MHz_SB1_1"] == "n257 - 400MHz", "Carrier: n257 - 400MHz_SB1_1"] = "Allocated"
    df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                 "Carrier: n257 - 400MHz_SB1_1"] == "n77 - 100MHz", "Carrier: n257 - 400MHz_SB1_1"] = "Unused"

    df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                 "Carrier: n77 - 100MHz_SB1_1"] == "n257 - 400MHz", "Carrier: n77 - 100MHz_SB1_1"] = "Unused"
    df_planet_NR_Sectors.loc[df_planet_NR_Sectors[
                                 "Carrier: n77 - 100MHz_SB1_1"] == "n77 - 100MHz", "Carrier: n77 - 100MHz_SB1_1"] = "Allocated"

    df_planet_NR_Sectors["Carrier: NR_Band_SB1_1"] = "Unused"

    df_planet_NR_Sectors = df_planet_NR_Sectors[df_planet_NR_Sectors["Frame Configuration"].notnull()]

    # column_list = pd.read_excel('input\Planet_import_template.xlsx', "NR_Sector_Carriers").columns
    column_list = ['Site ID', 'Sector ID', 'Carrier Name', 'Cell ID',
                   'Carrier Aggregation', 'Secondary Cell Selection', 'Top N Neighbors',
                   'Downlink Load (%)', 'Downlink Traffic (Mbps)', 'Uplink Traffic (Mbps)',
                   'PUSCH Noise Rise (dB)', 'PUCCH Noise Rise (dB)', 'Uplink Load (%)',
                   'Maximum Downlink Load (%)', 'Maximum Uplink Load (%)',
                   'Maximum Number Of Downlink Co-Scheduled Users',
                   'Maximum Number Of Uplink Co-Scheduled Users']

    df_planet_NR_Sector_Carriers = pd.DataFrame(columns=column_list)

    df_planet_NR_Sector_Carriers["Site ID"] = df_MS_cellfile["Site ID"]
    df_planet_NR_Sector_Carriers["Sector ID"] = df_MS_cellfile["Cell Name"].str[-1:]
    df_planet_NR_Sector_Carriers["Carrier Name"] = df_MS_cellfile["Band Name"] + "_SB1_1"
    df_planet_NR_Sector_Carriers["Carrier Aggregation"] = "TRUE"
    df_planet_NR_Sector_Carriers["Secondary Cell Selection"] = "AllCells"
    df_planet_NR_Sector_Carriers["Downlink Load (%)"] = 50
    df_planet_NR_Sector_Carriers["Downlink Traffic (Mbps)"] = 10
    df_planet_NR_Sector_Carriers["Uplink Traffic (Mbps)"] = 10
    df_planet_NR_Sector_Carriers["PUSCH Noise Rise (dB)"] = 3
    df_planet_NR_Sector_Carriers["PUCCH Noise Rise (dB)"] = 3
    df_planet_NR_Sector_Carriers["Uplink Load (%)"] = 0
    df_planet_NR_Sector_Carriers["Maximum Downlink Load (%)"] = 100
    df_planet_NR_Sector_Carriers["Maximum Uplink Load (%)"] = 100

    df_planet_NR_Sector_Carriers = df_planet_NR_Sector_Carriers[df_planet_NR_Sector_Carriers["Carrier Name"] != "Band 3 - 20MHz_SB1_1"]
    df_planet_NR_Sector_Carriers = df_planet_NR_Sector_Carriers[df_planet_NR_Sector_Carriers["Carrier Name"] != "Band 3 - 5MHz_SB1_1"]

    import os
    try:
        os.mkdir('output')
    except:
        a = 1

    with pd.ExcelWriter('output\Planet_import_file_desktop_from_MS.xlsx') as writer:
        df_planet_sites.to_excel(writer, sheet_name="Sites", index=False)
        df_planet_sectors.to_excel(writer, sheet_name="Sectors", index=False)
        df_planet_antennas.to_excel(writer, sheet_name="Antennas", index=False)
        df_planet_Antenna_Electrical_Parameters.to_excel(writer, sheet_name="Antenna_Electrical_Parameters", index=False)
        df_planet_sector_antennas.to_excel(writer, sheet_name="Sector_Antennas", index=False)
        df_planet_sector_antenna_ports.to_excel(writer, sheet_name="Sector_Antenna_Ports", index=False)
        df_planet_LTE_FDD_Sectors.to_excel(writer, sheet_name="LTE_FDD_Sectors", index=False)
        df_planet_LTE_FDD_Sector_Carriers.to_excel(writer, sheet_name="LTE_FDD_Sector_Carriers", index=False)
        df_planet_NR_Sectors.to_excel(writer, sheet_name="NR_Sectors", index=False)
        df_planet_NR_Sector_Carriers.to_excel(writer, sheet_name="NR_Sector_Carriers", index=False)
    webbrowser.open("output\Planet_import_file_desktop_from_MS.xlsx")
    success_message = "Import file Planet_import_file_desktop_from_MS.xlsx succesfully created in output folder \n\n"

    return success_message

def Compare_MS_cellfile(First,Second):
    import pandas as pd
    import webbrowser
    df_MS_cellfile_1 = pd.read_csv(First, low_memory=False, index_col=False)
    df_MS_cellfile_2 = pd.read_csv(Second, low_memory=False, index_col=False)

    # print(len(df_MS_cellfile_1['Cell Name']))
    # print(len(df_MS_cellfile_2['Cell Name']))

    df_common = pd.merge(df_MS_cellfile_1['Cell Name'], df_MS_cellfile_2['Cell Name'], how='inner', on=None, left_on='Cell Name', right_on='Cell Name',left_index=False, right_index=False, sort=True)
    df_outer = pd.merge(df_MS_cellfile_1['Cell Name'], df_MS_cellfile_2['Cell Name'], how='outer', on=None, left_on='Cell Name', right_on='Cell Name',left_index=False, right_index=False, sort=True, indicator=True)

    df_first = df_outer[df_outer['_merge'] == 'left_only']['Cell Name']
    df_second = df_outer[df_outer['_merge'] == 'right_only']['Cell Name']

    import os
    try:
        os.mkdir('output')
    except:
        a = 1

    df_common.to_csv("output\common.csv", index=None, header=True)
    df_first.to_csv("output\only_in_first.csv", index=None, header=True)
    df_second.to_csv("output\only_in_second.csv", index=None, header=True)
    # webbrowser.open("output\common.csv")
    # webbrowser.open("output\only_in_first.csv")
    # webbrowser.open("output\only_in_second.csv")

    success_message = "Result files from compare process succesfully created in output folder \n\n"
    return success_message

def Daily_Auto_Report(wspace,user,pw):

    import http.client as hcl
    from base64 import b64encode
    import requests
    import pandas as pd
    import webbrowser
    import json
    import datetime as dt

    user_pw_text = user + ':' + pw
    user_pw = user_pw_text.encode('ascii')


    c = hcl.HTTPSConnection("http://localhost:8080")
    # userAndPass = b64encode(b"planet:planet123").decode("ascii")
    userAndPass = b64encode(user_pw).decode('ascii')
    headers = {"accept": "text/plain", 'Authorization': 'Basic %s' % userAndPass}

    url_text = "https://localhost:8080/planning/cells/file?workspace=" + wspace
    r = requests.post(url=url_text, verify=False, headers=headers)

    a = str(dt.datetime.now().strftime('20%y%m%d%H%M%S'))

    import os

    try:
        os.mkdir('output\\archive_wspace_cells')
    except:
        no_need = 1

    file_name = "output\\archive_wspace_cells\\"+ a + "_"+wspace +".csv"

    f = open(file_name , "w", encoding='utf')
    f.write(r.text)
    f.close()

    # webbrowser.open(file_name)

    df_MS_CF = pd.read_csv(file_name, low_memory=False, index_col=False)

    a = df_MS_CF.groupby(['Technology']).count()
    Cells_number = len(df_MS_CF["Cell Name"])
    Tech_count = a['Cell Name'].reset_index()

    b = df_MS_CF.groupby(['Beamforming']).count()
    Bf_count = b['Cell Name'].reset_index()

    Custom_Col_No = len(df_MS_CF.columns[df_MS_CF.columns.str.startswith('Custom:')])
    return Cells_number,Tech_count,Bf_count, len(df_MS_CF.columns), Custom_Col_No,file_name

def Convert_Repeater_cellfile_to_MS(Rep_cellfile_name,file_list):
    import pandas as pd
    import webbrowser
    # df_MS_cellfile = pd.read_csv(MScellfile_name, low_memory=False, index_col=False ,encoding='cp932')
    Atoll_repeaters = pd.read_csv(Rep_cellfile_name, low_memory=False, index_col=False)

    Transmitters = file_list[3]
    Sites = file_list[2]

    df_Transmitters = pd.read_csv(Transmitters, low_memory=False, index_col=False)
    df_Sites = pd.read_csv(Sites, low_memory=False, index_col=False, encoding='cp932')

    Repeater_columns = [
        "Repeater ID",
        "Site ID",
        "Technology",
        "Active",
        "Donor Cell Name",
        "Donor Type",
        "Donor Longitude",
        "Donor Latitude",
        "Donor Antenna File",
        "Donor Propagation Model",
        "Donor Masked Pathloss (dB)",
        "Donor Downlink Antenna Ports",
        "Donor Uplink Antenna Ports",
        "Donor Electrical Tilt",
        "Donor Electrical Azimuth",
        "Donor Electrical Beamwidth",
        "Donor Height (m)",
        "Donor Azimuth",
        "Donor Mechanical Tilt",
        "Longitude",
        "Latitude",
        "Antenna File",
        "Service Propagation Model",
        "Additional Isolation (dB)",
        "Downlink Antenna Ports",
        "Uplink Antenna Ports",
        "Electrical Tilt",
        "Electrical Azimuth",
        "Electrical Beamwidth",
        "Height (m)",
        "Azimuth",
        "Mechanical Tilt",
        "Downlink Cable Loss (dB)",
        "Uplink Cable Loss (dB)",
        "BTS Noise Figure (dB)",
        "Donor Downlink Cable Loss (dB)",
        "Donor Uplink Cable Loss (dB)",
        "Donor BTS Noise Figure (dB)",
        "Service Distance (km)",
        "Service Radials",
        "Output Resolution (m)",
        "Outer Area Resolution (m)",
        "Inner Area Radius (m)",
        "Optimize Azimuth",
        "Azimuth Cost",
        "Azimuth Precision",
        "Azimuth Range",
        "Min Azimuth (Degrees)",
        "Max Azimuth (Degrees)",
        "Optimize Downtilt",
        "Downtilt Cost",
        "Downtilt Precision",
        "Downtilt Range",
        "Min Downtilt (Degrees)",
        "Max Downtilt (Degrees)",
        "Optimize Power",
        "Power Cost",
        "Power Precision",
        "Power Range",
        "Min Power",
        "Max Power",
        "Optimize Electrical Tilt",
        "Electrical Tilt Cost",
        "Electrical Tilt Range",
        "Min Electrical Tilt (Degrees)",
        "Max Electrical Tilt (Degrees)",
        "Optimize Electrical Azimuth",
        "Electrical Azimuth Cost",
        "Electrical Azimuth Range",
        "Min Electrical Azimuth (Degrees)",
        "Max Electrical Azimuth (Degrees)",
        "Optimize Electrical Beamwidth",
        "Electrical Beamwidth Cost",
        "Electrical Beamwidth Range",
        "Min Electrical Beamwidth (Degrees)",
        "Max Electrical Beamwidth (Degrees)",
        "Optimize Antenna Height",
        "Antenna Height Cost",
        "Antenna Height (m) 1",
        "Cable Length (m) 1",
        "Antenna Height (m) 2",
        "Cable Length (m) 2",
        "Antenna Height (m) 3",
        "Cable Length (m) 3",
        "Antenna Height (m) 4",
        "Cable Length (m) 4",
        "Antenna Height (m) 5",
        "Cable Length (m) 5",
        "Antenna Height (m) 6",
        "Cable Length (m) 6",
        "Antenna Height (m) 7",
        "Cable Length (m) 7",
        "Antenna Height (m) 8",
        "Cable Length (m) 8",
        "Antenna Height (m) 9",
        "Cable Length (m) 9",
        "Antenna Height (m) 10",
        "Cable Length (m) 10",
        "Optimize Antenna Pattern",
        "Antenna Pattern Files",
        "Antenna Pattern Cost",
        "Site Access Cost",
        "Repeater Gain (dB)",
        "System Losses (dB)",
        "Downlink Maximum Power per Carrier (dBm)"
    ]

    df_repeaters = pd.DataFrame(columns=Repeater_columns)

    df_repeaters["Repeater ID"] = Atoll_repeaters["Name"]
    df_repeaters["Active"] = Atoll_repeaters["Active"]
    df_repeaters["Donor Cell Name"] = Atoll_repeaters["Donor transmitter"]
    df_repeaters["Donor Antenna File"] = Atoll_repeaters["Antenna (donor side)"].str[:-4] + ".pafx"

    df_repeaters["Donor Masked Pathloss (dB)"] = Atoll_repeaters["Losses due to the Link with the Donor (dB)"]
    df_repeaters["Donor Height (m)"] = Atoll_repeaters["Height (m) (donor side)"]
    df_repeaters["Donor Azimuth"] = Atoll_repeaters["Azimuth (��) (donor side)"]
    df_repeaters["Donor Mechanical Tilt"] = Atoll_repeaters["Mechanical Downtilt (��) (donor side)"]
    df_repeaters["Longitude"] = Atoll_repeaters["Longitude (coverage side)"]
    df_repeaters["Latitude"] = Atoll_repeaters["Latitude (coverage side)"]
    df_repeaters["Antenna File"] = Atoll_repeaters["Antenna (coverage side)"].str[:-4] + ".pafx"
    df_repeaters["Service Propagation Model"] = Atoll_repeaters["Main Propagation Model (coverage side)"]
    df_repeaters["Electrical Tilt"] = Atoll_repeaters["Additional Electrical Downtilt (��) (coverage side)"]
    df_repeaters["Height (m)"] = Atoll_repeaters["Height (m) (coverage side)"]
    df_repeaters["Azimuth"] = Atoll_repeaters["Azimuth (��) (coverage side)"]
    df_repeaters["Mechanical Tilt"] = Atoll_repeaters["Mechanical Downtilt (��) (coverage side)"]
    df_repeaters["Downlink Cable Loss (dB)"] = Atoll_repeaters["Miscellaneous Transmission Losses (dB) (coverage side)"]
    df_repeaters["Uplink Cable Loss (dB)"] = Atoll_repeaters["Miscellaneous Reception Losses (dB) (coverage side)"]
    df_repeaters["Donor Downlink Cable Loss (dB)"] = 0
    df_repeaters["Donor Uplink Cable Loss (dB)"] = 0
    df_repeaters["Service Distance (km)"] = Atoll_repeaters["Main Calculation Radius (m) (coverage side)"]/1000
    df_repeaters["Output Resolution (m)"] = Atoll_repeaters["Main Resolution (m) (coverage side)"]
    df_repeaters["Outer Area Resolution (m)"] = Atoll_repeaters["Extended Resolution (m) (coverage side)"]
    df_repeaters["Inner Area Radius (m)"] = Atoll_repeaters["Main Calculation Radius (m) (coverage side)"]
    df_repeaters["Repeater Gain (dB)"] = Atoll_repeaters["Amplifier gain (dB)"]  # Atoll_repeaters["Total Gain (dB)"]]


    # df_Transmitters.rename(columns=dict_rename, inplace=True)

    # print(df_Transmitters.columns)

    column_list_sites = [
        "Name_sites",
        "Longitude",
        "Latitude",
        "Technology",
        "REGION",
        "LL_ID",
        "PHASE",
        "Sarf Status",
        "AREA_CATEGORY",
        "SUB_REGION",
        "PREFECTURE",
        "PREFECTURE_JPN",
        "CITY_CODE",
        "CITY",
        "CITY_JPN",
        "Property Address",
        "Property Name",
        "OBLIGATION_FY",
        "Difficult_Area_by_Level",
        "Difficult_Area_Type",
        "OBJECT",
        "RAN",
        "FREQUENCY_BAND",
        "BANDWIDTH",
        "Data_Source",
        "TAC",
        "VENDOR",
        "Cluster Name",
        "Residential Population",
        "Peak Population",
        "Site_Equipment",
        "Backhaul_Type",
        "Site_Type_Class",
        "Generation"
    ]
    df_Sites.rename(columns={"Name":"Name_sites"}, inplace=True)
    column_list_transmitters = [
        "Site",
        "Transmitter",
        "Main Propagation Model",
        "Noise Figure (dB)"
    ]



    Atoll_repeaters = pd.merge(Atoll_repeaters, df_Transmitters[column_list_transmitters], left_on='Site',
                               right_on='Site', how='left')

    Atoll_repeaters = pd.merge(Atoll_repeaters, df_Sites[column_list_sites], left_on='Site',right_on='Name_sites', how='left')


    df_repeaters["Custom: llId"] = Atoll_repeaters["LL_ID"]
    df_repeaters["Custom: phase"] = Atoll_repeaters["PHASE"]
    df_repeaters["Custom: sarfStatus"] = Atoll_repeaters["Sarf Status"]
    df_repeaters["Custom: areaCategory"] = Atoll_repeaters["AREA_CATEGORY"]
    df_repeaters["Custom: geographyL1"] = Atoll_repeaters["REGION"].str[2:]
    df_repeaters["Custom: subRegion"] = Atoll_repeaters["SUB_REGION"]
    df_repeaters["Custom: geographyL2"] = Atoll_repeaters["PREFECTURE"]
    df_repeaters["Custom: prefectureJpn"] = Atoll_repeaters["PREFECTURE_JPN"]
    df_repeaters["Custom: cityCode"] = Atoll_repeaters["CITY_CODE"]
    df_repeaters["Custom: geographyL3"] = Atoll_repeaters["CITY"]
    df_repeaters["Custom: cityJpn"] = Atoll_repeaters["CITY_JPN"]
    df_repeaters["Custom: propertyAddress"] = Atoll_repeaters["Property Address"]
    df_repeaters["Custom: propertyName"] = Atoll_repeaters["Property Name"]
    df_repeaters["Custom: obligationFy"] = Atoll_repeaters["OBLIGATION_FY"]
    df_repeaters["Custom: difficultAreaByLevel"] = Atoll_repeaters["Difficult_Area_by_Level"]
    df_repeaters["Custom: difficultAreaType"] = Atoll_repeaters["Difficult_Area_Type"]
    df_repeaters["Custom: object"] = Atoll_repeaters["OBJECT"]
    df_repeaters["Custom: ran"] = Atoll_repeaters["RAN"]
    df_repeaters["Custom: frequencyBand"] = Atoll_repeaters["FREQUENCY_BAND"]
    df_repeaters["Custom: bandwidth"] = Atoll_repeaters["BANDWIDTH"]
    df_repeaters["Custom: dataSource"] = Atoll_repeaters["Data_Source"]
    df_repeaters["Custom: tac"] = Atoll_repeaters["TAC"]
    df_repeaters["Custom: vendor"] = Atoll_repeaters["VENDOR"]
    df_repeaters["Custom: geographyL4"] = Atoll_repeaters["Cluster Name"]
    df_repeaters["Custom: residentialPopulation"] = Atoll_repeaters["Residential Population"]
    df_repeaters["Custom: peakPopulation"] = Atoll_repeaters["Peak Population"]
    df_repeaters["Custom: siteEquipment"] = Atoll_repeaters["Site_Equipment"]
    df_repeaters["Custom: backhaulType"] = Atoll_repeaters["Backhaul_Type"]
    df_repeaters["Custom: siteTypeClass"] = Atoll_repeaters["Site_Type_Class"]
    df_repeaters["Custom: generation"] = Atoll_repeaters["Generation"]
    df_repeaters["Custom: equipment"] = Atoll_repeaters["Equipment"]
    df_repeaters["Custom: totalEirpRepeater"] = Atoll_repeaters["Total Gain (dB)"]
    df_repeaters["Custom: feederEquipmentDonor"] = Atoll_repeaters["Feeder Equipment (donor side)"]
    df_repeaters["Custom: transmissionFeederLengthMDonorSide"] = Atoll_repeaters["Transmission Feeder Length (m) (donor side)"]
    df_repeaters["Custom: receptionFeederLengthMDonorSide"] = Atoll_repeaters["Reception Feeder Length (m) (donor side)"]
    df_repeaters["Custom: feederEquipmentCoverageSide"] = Atoll_repeaters["Feeder Equipment (coverage side)"]
    df_repeaters["Custom: transmissionFeederLengthCoverageSide"] = Atoll_repeaters["Transmission Feeder Length (coverage side)"]
    df_repeaters["Custom: receptionFeederLengthMCoverageSide"] = Atoll_repeaters["Reception Feeder Length (m) (coverage side)"]
    df_repeaters["Custom: extendedPropagationModelCoverageSide"] = Atoll_repeaters["Extended Propagation Model (coverage side)"]
    df_repeaters["Custom: commentsCoverageSide"] = Atoll_repeaters["Comments (coverage side)"]
    df_repeaters["Custom: sarfId"] = Atoll_repeaters["Site"]

    columns_to_fill_null = [
        "Custom: llId",
        "Custom: phase",
        "Custom: siteStatus",
        "Custom: areaCategory",
        "Custom: geographyL1",
        "Custom: subRegion",
        "Custom: geographyL2",
        "Custom: prefectureJpn",
        "Custom: cityCode",
        "Custom: geographyL3",
        "Custom: cityJpn",
        "Custom: propertyAddress",
        "Custom: propertyName",
        "Custom: obligationFy",
        "Custom: difficultAreaByLevel",
        "Custom: difficultAreaType",
        "Custom: object",
        "Custom: ran",
        "Custom: frequencyBand",
        "Custom: bandwidth",
        "Custom: dataSource",
        "Custom: tac",
        "Custom: vendor",
        "Custom: geographyL4",
        "Custom: residentialPopulation",
        "Custom: peakPopulation",
        "Custom: siteEquipment",
        "Custom: backhaulType",
        "Custom: siteTypeClass",
        "Custom: generation",
        "Custom: equipment",
        "Custom: totalEirpRepeater",
        "Custom: feederEquipmentDonor",
        "Custom: transmissionFeederLengthMDonorSide",
        "Custom: receptionFeederLengthMDonorSide",
        "Custom: feederEquipmentCoverageSide",
        "Custom: transmissionFeederLengthCoverageSide",
        "Custom: receptionFeederLengthMCoverageSide",
        "Custom: extendedPropagationModelCoverageSide",
        "Custom: commentsCoverageSide",
        "Custom: sarfId",
    ]

    for column in columns_to_fill_null:
        df_repeaters[column].fillna("null", inplace=True)

    df_repeaters["Technology"] = "LTE_FDD"  # Atoll_repeaters["Technology"]
    df_repeaters["Donor Type"] = "RF" #Atoll_repeaters["Link Type with the Donor"]
    df_repeaters["Donor Longitude"] = Atoll_repeaters["Longitude"]
    df_repeaters["Donor Latitude"] = Atoll_repeaters["Latitude"]
    df_repeaters["Donor Downlink Antenna Ports"] = ""
    df_repeaters["Donor Uplink Antenna Ports"] = ""
    df_repeaters["Donor Electrical Tilt"] = "" # Atoll_repeaters["Donor Electrical Tilt"]
    df_repeaters["Service Propagation Model"] = Atoll_repeaters["Main Propagation Model"]
    df_repeaters["Site ID"] = Atoll_repeaters["Name_sites"]
    df_repeaters["Donor BTS Noise Figure (dB)"] = Atoll_repeaters["Noise Figure (dB)"]
    df_repeaters["Donor Propagation Model"] = Atoll_repeaters["Main Propagation Model"] # P3M_KANTO_LTE_FDD_Band_3_urban.pmf"

    Atoll_repeaters.loc[Atoll_repeaters["REGION"] == 'E_KINKI', "REGION"] = 'E_KANSAI'
    Atoll_repeaters.loc[Atoll_repeaters["REGION"] == 'B_SHINETSU', "REGION"] = 'A_KANTO'
    Atoll_repeaters.loc[Atoll_repeaters["REGION"] == 'O_OKINAWA', "REGION"] = 'H_KYUSHU'


    df_repeaters["Propagation Model"] = "P3M_" + Atoll_repeaters["REGION"].str[2:] + "_LTE_FDD_Band_3" + '.pmf'

    df_repeaters["Propagation Model"].fillna("P3M-Rakuten-1900MHz.pmf", inplace=True)


    df_repeaters = df_planet_lte_cells_rural_urban_class(df_repeaters,file_list)

    df_repeaters["Donor Propagation Model"] = df_repeaters["Propagation Model"]
    df_repeaters["Service Propagation Model"] = df_repeaters["Propagation Model"]

    del df_repeaters["Propagation Model"]

    import os
    try:
        os.mkdir('output')
    except:
        a = 1

    df_repeaters.to_csv("output\Repeater_MS_cellfile.csv", index=False, header=True,encoding='UTF-8')
    webbrowser.open("output\Repeater_MS_cellfile.csv")
    success_message = "Import file Repeater_MS_cellfile succesfully created in output folder \n\n"

    return success_message

def Convert_Repeater_cellfile_to_Desktop(Rep_cellfile_name,Transmitters,Sites):
    import pandas as pd
    import webbrowser

    import os

    try:
        os.mkdir('output')
    except:
        a = 1

    try:
        os.mkdir('output/planet_desktop_reps_csv')
        # os.mkdir('output_deneme')
    except:
        a = 1
    # try:



    df = Planet_repeater_cellfile_methods(Rep_cellfile_name,Transmitters,Sites)
    df.sites().to_csv('output/planet_desktop_reps_csv/Sites.csv', index=False, header=True)
    df.Antenna_Electrical_Parameters().to_csv('output/planet_desktop_reps_csv/Antenna_Electrical_Parameters.csv', index=False, header=True)
    df.Antennas().to_csv('output/planet_desktop_reps_csv/Antennas.csv', index=False, header=True)
    df.LTE_FDD_Repeaters().to_csv('output/planet_desktop_reps_csv/LTE_FDD_Repeaters.csv', index=False, header=True)
    df.Repeater_Antennas().to_csv('output/planet_desktop_reps_csv/Repeater_Antennas.csv', index=False, header=True)
    df.Repeaters().to_csv('output/planet_desktop_reps_csv/Repeaters.csv', index=False, header=True)
    success_message = "Import files succesfully created in output folder \n\n"

    return success_message

class Planet_repeater_cellfile_methods:
    def __init__(self, Rep_cellfile_name,Transmitters,Sites):
        self.__Repeaters = Rep_cellfile_name
        self.__Sites = Sites
        self.__Transmitters = Transmitters
    def sites(self):
        print("Creating sites table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Sites").columns
        column_list = ['Site ID', 'Site UID', 'Longitude', 'Latitude', 'Description',
                       'Site Name', 'Site Name 2', 'Candidate Priority']
        df_planet_sites = pd.DataFrame(columns=column_list)

        df_atoll_repeaters = pd.read_csv(self.__Repeaters, low_memory=False, index_col=False, encoding='cp932')

        site_list = df_atoll_repeaters["Name"].str[:-2]

        df_atoll_sites = pd.read_csv(self.__Sites, low_memory=False, index_col=False, encoding='cp932')
        df_planet_sites["Site ID"] = df_atoll_sites["Name"]
        df_planet_sites["Longitude"] = df_atoll_sites["Longitude"]
        df_planet_sites["Latitude"] = df_atoll_sites["Latitude"]
        df_planet_sites["Candidate Priority"] = 1

        df_planet_sites = df_planet_sites[df_planet_sites["Site ID"].isin(site_list)]

        return df_planet_sites
    def Antenna_Electrical_Parameters(self):
        import pandas as pd
        print("Creating Antenna_Electrical_Parameters table")
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antenna_Electrical_Parameters").columns
        column_list = ['Site ID', 'Antenna ID', 'Electrical Controller', 'Electrical Tilt','Electrical Azimuth', 'Electrical Beamwidth']

        df_planet_Antenna_Electrical_Parameters = pd.DataFrame(columns=column_list)
        df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')
        df_atoll_repeaters = pd.read_csv(self.__Repeaters, low_memory=False, index_col=False, encoding='cp932')
        del df_atoll_Transmitters["Site"]
        df_atoll_sectors = df_atoll_repeaters
        df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters,  left_on="Name",right_on="Transmitter", how='left')

        # df_planet_Antenna_Electrical_Parameters["Antenna_File"] = df_atoll_Transmitters["Antenna"].str[:-4] + ".pafx"
        df_planet_Antenna_Electrical_Parameters["Site ID"] = df_atoll_Transmitters["Site"]
        df_planet_Antenna_Electrical_Parameters["Antenna ID"] = df_atoll_Transmitters["Name"].str[-1:]
        df_planet_Antenna_Electrical_Parameters["Electrical Controller"] = 'All bands'
        df_planet_Antenna_Electrical_Parameters["Electrical Tilt"] = df_atoll_Transmitters["Antenna (coverage side)"].str[-3:-1]
        df_planet_Antenna_Electrical_Parameters["Electrical Azimuth"] = "0"
        df_planet_Antenna_Electrical_Parameters["Electrical Beamwidth"] = "70"

        # indexNames = df[(df['Antenna_File'] == 'KMW_ANT_65_16dBi.pafx') | (df['Antenna_File'] == 'KMW_RRA - I_ANT_65_16dBi.pafx')].index
        # df.drop(indexNames, inplace=True)

        # df.drop('Antenna_File', axis='columns', inplace=True)
        # del df['Antenna_File']

        # delete all rows with column 'Age' has value 30 to 40
        return df_planet_Antenna_Electrical_Parameters
    def Antennas(self):
        print("Creating antenna table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antennas").columns
        column_list = [
            "Site ID",
            "Antenna ID",
            "Longitude",
            "Latitude",
            "Antenna File",
            "Azimuth",
            "Mechanical Tilt"
            ]

        df_planet_antennas = pd.DataFrame(columns=column_list)
        df_planet_antennas2 = pd.DataFrame(columns=column_list)
        # df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_repeaters = pd.read_csv(self.__Repeaters, low_memory=False, index_col=False, encoding='cp932')

        # site_list = df_atoll_sectors["Name"].str[:-5]

        # df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters,  left_on="Name",right_on="Transmitter", how='left')



        df_planet_antennas["Site ID"] = df_atoll_repeaters["Name"].str[:-2]
        df_planet_antennas["Antenna ID"] = 2 # df_atoll_repeaters["Name"].str[-1:]
        df_planet_antennas["Longitude"] = df_atoll_repeaters["Longitude (coverage side)"]
        df_planet_antennas["Latitude"] = df_atoll_repeaters["Latitude (coverage side)"]
        df_planet_antennas["Antenna File"] = df_atoll_repeaters["Antenna (coverage side)"].str[:-4] + ".pafx"

        # df_planet_antennas["Height(m)"] = df_atoll_repeaters["Height (m) (coverage side)"]
        df_planet_antennas["Azimuth"] = df_atoll_repeaters["Azimuth (°) (coverage side)"]
        df_planet_antennas["Mechanical Tilt"] = df_atoll_repeaters["Mechanical Downtilt (°) (coverage side)"]

        df_planet_antennas2["Site ID"] = df_atoll_repeaters["Name"].str[:-2]
        df_planet_antennas2["Antenna ID"] = 1 # df_atoll_repeaters["Name"].str[-1:]
        df_planet_antennas2["Longitude"] = df_atoll_repeaters["Longitude (coverage side)"]
        df_planet_antennas2["Latitude"] = df_atoll_repeaters["Latitude (coverage side)"]
        df_planet_antennas2["Antenna File"] = df_atoll_repeaters["Antenna (donor side)"].str[:-4] + ".pafx"

        # df_planet_antenn2as["Height(m)"] = df_atoll_repeaters["Height (m) (coverage side)"]
        df_planet_antennas2["Azimuth"] = df_atoll_repeaters["Azimuth (°) (coverage side)"]
        df_planet_antennas2["Mechanical Tilt"] = df_atoll_repeaters["Mechanical Downtilt (°) (coverage side)"]

        df_planet_antennas = df_planet_antennas.append(df_planet_antennas2)

        # df_planet_antennas = df_planet_antennas[df_planet_antennas["Site ID"].isin(site_list)]

        return (df_planet_antennas)
    def LTE_FDD_Repeaters(self):
        print("Creating LTE FDD Repeaters table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antennas").columns
        column_list = [
            "Site ID",
            "Repeater ID",
            "Total EIRP (dBm)",
            "Repeater Gain (dB)",
            "Carrier: Band 3 - 20MHz_SB1_1",
            "Carrier: Band 3 - 5MHz_SB1_1",
            "Carrier: LTE_FDD_Band_SB1_1",
            "Carrier: LTE_FDD_Band_SB1_2",
            ]

        LTE_FDD_Repeaters = pd.DataFrame(columns=column_list)
        # df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_repeaters = pd.read_csv(self.__Repeaters, low_memory=False, index_col=False, encoding='cp932')

        # site_list = df_atoll_sectors["Name"].str[:-5]

        # df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters,  left_on="Name",right_on="Transmitter", how='left')



        LTE_FDD_Repeaters["Site ID"] = df_atoll_repeaters["Name"].str[:-2]
        LTE_FDD_Repeaters["Repeater ID"] = df_atoll_repeaters["Name"]# .str[-1:]
        LTE_FDD_Repeaters["Repeater Gain (dB)"] = df_atoll_repeaters["Amplifier gain (dB)"]
        LTE_FDD_Repeaters["Total EIRP (dBm)"] = df_atoll_repeaters["Total Gain (dB)"]
        LTE_FDD_Repeaters["Carrier: Band 3 - 20MHz_SB1_1"] = "FALSE"
        LTE_FDD_Repeaters["Carrier: Band 3 - 5MHz_SB1_1"] = "FALSE"
        LTE_FDD_Repeaters["Carrier: LTE_FDD_Band_SB1_1"] = "FALSE"
        LTE_FDD_Repeaters["Carrier: LTE_FDD_Band_SB1_2"] = "FALSE"



        # df_planet_antennas = df_planet_antennas[df_planet_antennas["Site ID"].isin(site_list)]

        return (LTE_FDD_Repeaters)
    def Repeater_Antennas(self):
        print("Repeater antennas table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antennas").columns
        column_list = [
            "Site ID",
            "Repeater ID",
            "Antenna ID",
            "Horizontal Beamwidth",
            "Vertical Beamwidth",
            "Link Configuration ID",
            "Power Split (%)",
            "Pattern List: PSS/SSS/BCH",
            "Pattern List: CSI-RS",
            "Pattern List: PDCCH",
            "Pattern List: PDSCH",
            "Pattern List: PUCCH",
            "Pattern List: PUSCH",
            "Pattern List: PRACH"
            ]

        LTE_FDD_Repeaters = pd.DataFrame(columns=column_list)
        # df_atoll_Transmitters = pd.read_csv(self.__Transmitters, low_memory=False, index_col=False, encoding='cp932')

        df_atoll_repeaters = pd.read_csv(self.__Repeaters, low_memory=False, index_col=False, encoding='cp932')

        # site_list = df_atoll_sectors["Name"].str[:-5]

        # df_atoll_Transmitters = pd.merge(df_atoll_sectors, df_atoll_Transmitters,  left_on="Name",right_on="Transmitter", how='left')



        LTE_FDD_Repeaters["Site ID"] = df_atoll_repeaters["Name"].str[:-2]
        LTE_FDD_Repeaters["Repeater ID"] = df_atoll_repeaters["Name"]
        LTE_FDD_Repeaters["Antenna ID"] = 2# df_atoll_repeaters["Donor transmitter"].str[-1:]+1
        LTE_FDD_Repeaters["Horizontal Beamwidth"] = ""
        LTE_FDD_Repeaters["Vertical Beamwidth"] = ""
        LTE_FDD_Repeaters["Link Configuration ID"] = "Default"
        LTE_FDD_Repeaters["Power Split (%)"] = 100
        LTE_FDD_Repeaters["Pattern List: PSS/SSS/BCH"] = ""
        LTE_FDD_Repeaters["Pattern List: CSI-RS"] = ""
        LTE_FDD_Repeaters["Pattern List: PDCCH"] = ""
        LTE_FDD_Repeaters["Pattern List: PDSCH"] = ""
        LTE_FDD_Repeaters["Pattern List: PUCCH"] = ""
        LTE_FDD_Repeaters["Pattern List: PUSCH"] = ""
        LTE_FDD_Repeaters["Pattern List: PRACH"] = ""



        # df_planet_antennas = df_planet_antennas[df_planet_antennas["Site ID"].isin(site_list)]

        return (LTE_FDD_Repeaters)
    def Repeaters(self):
        print("Creating Repeaters table")
        import pandas as pd
        # column_list = pd.read_excel('input\Planet_import_template.xlsx', "Antennas").columns
        column_list = [
        "Site ID",
        "Repeater ID",
        "Donor Site ID",
        "Donor Sector ID",
        "Technology",
        "Active",
        "Donor Type",
        "Donor Antenna ID",
        "Donor Link Configuration ID",
        "Donor Propagation Model",
        "Donor Masked Pathloss (dB)",
        "Service Propagation Model",
        "Service Distance (km)",
        "Service Radials",
            ]
        LTE_FDD_Repeaters = pd.DataFrame(columns=column_list)

        df_atoll_repeaters = pd.read_csv(self.__Repeaters, low_memory=False, index_col=False, encoding='cp932')

        LTE_FDD_Repeaters["Site ID"] = df_atoll_repeaters["Name"].str[:-2]
        LTE_FDD_Repeaters["Repeater ID"] = df_atoll_repeaters["Name"]
        LTE_FDD_Repeaters["Donor Site ID"] = df_atoll_repeaters["Donor transmitter"].str[:-2]
        LTE_FDD_Repeaters["Donor Sector ID"] = df_atoll_repeaters["Donor transmitter"].str[-1:]
        LTE_FDD_Repeaters["Technology"] = "LTE FDD"
        LTE_FDD_Repeaters["Active"] = "TRUE"
        LTE_FDD_Repeaters["Donor Type"] = "RF"
        LTE_FDD_Repeaters["Donor Antenna ID"] = df_atoll_repeaters["Name"].str[-1:]
        LTE_FDD_Repeaters["Donor Link Configuration ID"] = "Default"
        LTE_FDD_Repeaters["Donor Propagation Model"] = ""
        LTE_FDD_Repeaters["Donor Masked Pathloss (dB)"] = df_atoll_repeaters["Losses due to the Link with the Donor (dB)"]
        LTE_FDD_Repeaters["Service Propagation Model"] = ""
        LTE_FDD_Repeaters["Service Distance (km)"] = df_atoll_repeaters["Main Calculation Radius (m) (coverage side)"]/1000
        LTE_FDD_Repeaters["Service Radials"] = 60


        # df_planet_antennas = df_planet_antennas[df_planet_antennas["Site ID"].isin(site_list)]

        return (LTE_FDD_Repeaters)

def Check_cell_geolocation(cellfile,mapfile):
    import fiona
    import geopandas as gpd
    from shapely.geometry import Point, Polygon
    import pandas as pd
    import webbrowser
    import numpy as np
    import time

    df_all_japan = gpd.read_file(mapfile,driver="MapInfo File")
    df_cells_all = pd.read_csv(cellfile, low_memory=False, index_col=False)

    df_cells_all['coords'] = list(zip(df_cells_all['Longitude'], df_cells_all['Latitude']))

    df_cells_all['coords'] = df_cells_all['coords'].apply(Point)
    points = gpd.GeoDataFrame(df_cells_all, geometry='coords', crs=df_all_japan.crs)

    start = time.time()
    local_time = time.ctime(start)
    print("Start:", local_time)

    pointInPolys = gpd.tools.sjoin(points, df_all_japan, how='left')

    end = time.time()
    print("Processing time",round(end - start)/60)

    # result = pointInPolys[['Cell Name','Custom: geographyL1','Region','Longitude','Latitude']]
    result = pointInPolys
    result['Region'] = result['Region'].str[2:]

    Prob = result[result["Region"] != result["Custom: geographyL1"]]
    Prob = Prob[Prob["Region"] != "KANTO_ISLANDS"]

    Kanto_Island = result[result["Region"] == "KANTO_ISLANDS"]
    Kanto_Island["Custom: geographyL1"] = Kanto_Island["Region"]

    result = result[~result["Region"].isnull()]
    result = result[result["Region"] == result["Custom: geographyL1"]]
    result = result.append(Kanto_Island)

    result.drop('Region', axis='columns', inplace=True)
    Prob.drop('Region', axis='columns', inplace=True)

    import os
    try:
        os.mkdir('output')
    except:
        a = 1

    result.to_csv("output/Planet Microservices Cell File_geolocation_checked.csv", index=None, header=True, encoding='UTF-8')
    Prob.to_csv("output/Planet Microservices Cell File_problematic_cells.csv", index=None, header=True, encoding='UTF-8')
    Kanto_Island.to_csv("output/Planet Microservices Cell File_Kanto_Island_cells.csv", index=None, header=True, encoding='UTF-8')
    # print(df_cells_all)

    # webbrowser.open("output\\result_region.csv")
    # webbrowser.open("output\\problematic_region.csv")

    return "Check Completed, Please Check output folder for 3 result files"

