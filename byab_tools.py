import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu",[
        "Geolocation Based RAN Planning",
        "Geolocation Based RAN Infrastructure Planning",
        "Performance Analysis Tools",
        "Data Migration Tools",
        "Machine Learning / AI use case design optimization projects",
        "RAN Monitoring Tools",
        "Database Monitoring Tools",
        "dB Management Tools"
    ], menu_icon="cast", default_index=0)

if selected == "Geolocation Based RAN Planning":
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    st.title('Virtual RAN Planning Tools')
    st.header('Virtual RAN Group Center Virtual Control Unit Planning')
    # st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
    # st.header('This is a header')
    # st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

    max_dist_allowed = 3 # 1.7
    gc_df = []
    site_df =[]
    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True)
    # st.write(len(uploaded_file))
    if len(uploaded_file) != 2:
        st.write("Please upload 2 files only")

    if st.button('Process'):
    # if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        for i in range(len(uploaded_file)):
            # st.write(uploaded_file[i].name)
            if uploaded_file[i].name == "gc_list.csv":
                gc_df = pd.read_csv(uploaded_file[i],  index_col=0)
            if uploaded_file[i].name == "site_data.csv":
                site_df = pd.read_csv(uploaded_file[i],  index_col=0)

    #

    Total_output = pd.DataFrame(columns=['Sarf','lat','lon','GC_Name','group','size'])
    Total_output.loc[0, ['lat', 'lon','size','Sarf','GC_Name','group']] = [1, 1,20,"Deneme","GC",3]
    # st.write(Total_output)

    for i in range(0, len(gc_df)):
        # print(gc_df.iloc[i,0])
        gc_name = gc_df.iloc[i, 0]
        # print(gc_name)
        # st.write("Processing Group Center...",gc_name, "...ok")
        site_df_temp = site_df.loc[site_df['GC_Name'] == gc_name]
        # print(site_df)
        # st.write(site_df_temp)
        Duo_table = gc.creating_duos(site_df_temp, max_dist_allowed)

        Group_table = gc.creating_groups(Duo_table, max_dist_allowed)

        # export_csv = Group_table.to_csv(r'data/Group_table.csv', index=None, header=True)

        Output_Format = gc.Output_format(Group_table, len(site_df_temp))

        Output_table = pd.merge(Output_Format, site_df_temp, on='Sarf', how='right')

        Total_output = Total_output.append(Output_table)
        Output_table = Output_table.reindex(['Sarf', 'lat', 'lon', 'GC_Name', 'group'], axis='columns')

        # st.write(Output_table)
    Total_output["size"] = 10
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')


    if len(Total_output) != 1:
        Total_output = Total_output.iloc[1:]


    max_lat = Total_output["lat"].max()
    min_lat = Total_output["lat"].min()
    max_lon = Total_output["lon"].max()
    min_lon = Total_output["lon"].min()
    lat_center = (max_lat + min_lat) / 2,
    lon_center = (max_lon + min_lon) / 2,

    # st.write(max_lat, min_lat,max_lon,min_lon)

    # st.map(Total_output)
    # # chart_data = pd.DataFrame(columns=['lat', 'lon'])
    # labels = Total_output.Sarf
    # fig = px.scatter_mapbox(data_frame = Total_output, lat="lat", lon="lon", zoom=3, hover_name = labels,size = "size")
    # fig.update_layout(mapbox_style="open-street-map")
    # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    # st.plotly_chart(fig)

    Total_output = Total_output.reset_index()
    import pydeck as pdk

    Total_output["labels"] =  Total_output["GC_Name"].str[0:3]+ "_" + Total_output["group"].astype(str)
    csv = convert_df(Total_output)
    st.download_button(label="Download Result File", data=csv, file_name='Total_output.csv', mime='text/csv', )

    chart_data = Total_output[["lat","lon","Sarf","GC_Name","labels"]]# ,"Power","Height","Site Azimuths"]]
    # chart_data["Labels"] = Output_table["GC_Name"] + "_" + Output_table["group"].astype(str)

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=(max_lat + min_lat)/2,
            longitude=(max_lon + min_lon)/2,
            zoom=11,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=20,
                pickable=True,
                tooltip=True,
            ),
            pdk.Layer(type="TextLayer",
                data=chart_data,
                pickable=False,
                get_position=["lon", "lat"],
                get_text="labels",
                get_size=12,
                get_color=[0, 0, 0],
                get_angle=0, # Note that string constants in pydeck are explicitly passed as strings
                # This distinguishes them from columns in a data set
                getTextAnchor='"middle"',
                get_alignment_baseline='"bottom"'
            ),

        ],
        tooltip={"text": "Site: {Sarf}\nlat: {lat}\nlon: {lon}"}
    ))

    st.divider()  # 👈 Draws a horizontal rule
    st.header('VDU RIU RRH Planning')
    uploaded_file_2 = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "second")
    st.divider()  # 👈 Draws a horizontal rule
    st.header('DAY 1 Format Preparation')
    uploaded_file_3 = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "third")

if selected == "Geolocation Based RAN Infrastructure Planning":
    st.title('Geolocation Based Transport Infrastructure Planning')
    st.header('Fiber optical line distance analysis')
    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "first")
    st.divider()  # 👈 Draws a horizontal rule
    st.header('Site candidate Fiber cost opex/capex analysis')
    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "second")
    st.divider()  # 👈 Draws a horizontal rule
    st.header('Multi vendor Fiber cost opex/capex analysis')
    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "third")
    st.divider()  # 👈 Draws a horizontal rule

if selected == "Data Migration Tools":
    import pandas as pd
    import GC_functions as gc
    import numpy as np
    import Data_migration_functions as cpf

    st.title('Data Migration Tools From Atoll to Planet Microservices')
    st.divider()  # 👈 Draws a horizontal rule
    st.header('Convert Atoll Files to Planet Microservices Format')

    uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True)

    # st.write(len(uploaded_file))
    # if len(uploaded_file) != 8:
        # st.write("Please upload all files")

    if st.button('Process'):
    # if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:

        for i in range(len(uploaded_file)):
            st.write(uploaded_file[i].name)
            if uploaded_file[i].name == "Cells_LTE_subset.csv":
                Cells_LTE = pd.read_csv(uploaded_file[i],  index_col=False)
                # st.write(Cells_LTE)
            if uploaded_file[i].name == "Cells_NR_subset.csv":
                Cells_NR = pd.read_csv(uploaded_file[i],  index_col=False)
            if uploaded_file[i].name == "Sites.csv":
                Sites = pd.read_csv(uploaded_file[i], index_col=False, encoding='cp932')
            if uploaded_file[i].name == "Transmitters_fixed.csv":
                Transmitters = pd.read_csv(uploaded_file[i], index_col=False, encoding='cp932')
            if uploaded_file[i].name == "Beamforming_Antenna_List.csv":
                bf_antennas = pd.read_csv(uploaded_file[i], index_col=False)
            if uploaded_file[i].name == "Cells_Details_LTE.csv":
                Cells_details_LTE = pd.read_csv(uploaded_file[i], index_col=False)
            if uploaded_file[i].name == "Cells_Details_NR.csv":
                Cells_details_NR = pd.read_csv(uploaded_file[i], index_col=False)
            if uploaded_file[i].name == "5m_Area_Polygon_All_Japan.tab":
                Urban_Boundary  = pd.read_csv(uploaded_file[i], index_col=False)

        file_list = [Cells_LTE, Cells_NR, Sites, Transmitters, bf_antennas, Cells_details_LTE, Cells_details_NR] # , Urban_Boundary]

        df_all = cpf.Atoll_to_planet_MS(file_list)

        def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')


        csv = convert_df(df_all)
        st.download_button(label="Download Result File", data=csv, file_name='Result_file.csv', mime='text/csv', )

            # st.write(message)

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Convert Atoll Files to Planet Desktop Format')

    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "second")

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Create Beamforming Antenna From Atoll Format')

    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "third")

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Update MS Sandbox with CellFiles')

    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "fourth")

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Check Atoll Data for inconsistencies')

if selected == "Machine Learning / AI use case design optimization projects":
        st.title('Machine Learning Network Performance Booster Toools')
        st.divider()  # 👈 Draws a horizontal rule
        st.header('KPI Anomaly Heat-Map')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="1")
        st.divider()  # 👈 Draws a horizontal rule
        st.header('Silent Issue detection')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="2")
        st.divider()  # 👈 Draws a horizontal rule
        st.header('Load Balance/Mobility load balance parameter optimization')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="3")
        st.divider()  # 👈 Draws a horizontal rule
        st.header('Energy Efficiency Management')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="4")

if selected =="dB Management Tools":
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import pandas as pd

    st.title('Database Management Tools')
    st.header('Database Connection')

    if st.button('Connect dB'):
        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        try:
            cluster.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    st.divider()  # 👈 Draws a horizontal rule
    st.header('List Databases in cluster')

    # cl_name = st.text_input('Cluster name:')
    if st.button('List Databases in cluster'):
        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        try:
            cluster.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        df_1 = pd.DataFrame(list(cluster.list_databases()))
        # for i in df_1[]
        st.write(df_1)

    st.divider()  # 👈 Draws a horizontal rule
    st.header('List Collections in Databases')

    db_name = st.text_input('Database name:')

    if st.button("List Collection names"):
        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        try:
            cluster.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        db = cluster[db_name]
        # collections_df = pd.DataFrame(list(db.list_collection_names()))

        collection_names = db.list_collection_names()
        collection_numbers = []

        for i in collection_names:
            print(i, db[i].count_documents({}))
            collection_numbers.append(db[i].count_documents({}))

        collections_df = pd.DataFrame(columns=['Names', 'Number of Docs'])
        collections_df['Names'] = collection_names
        collections_df['Number of Docs'] = collection_numbers

        st.write(collections_df)

    st.divider()  # 👈 Draws a horizontal rule
    st.header('Update Sites Collection with CSV file')
    db_name_update = st.text_input('Collection name to update')
    uploaded_file = st.file_uploader("Choose input CSV file to process", type="csv", accept_multiple_files=False)

    if st.button('Update Sites Collection'):
        import pandas as pd
        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        db = cluster["Sites"]

        df_tokyo = pd.read_csv(uploaded_file, index_col=False)
        df_tokyo["_id"] = df_tokyo["Site Name"]
        df_tokyo.reset_index(inplace=True)

        df_tokyo_dict = df_tokyo.to_dict("records")
        db[db_name_update].insert_many(df_tokyo.to_dict('records'))

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Create a Database')
    db_name = st.text_input('dB name to create')
    if st.button('Create dB'):
        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        st.write('dB Created:', db_name)
        db = cluster["UserData"]
        collection = db[db_name]
        collection.insert_one({"_id": "Temp", "user_name": "byabaci"})

    st.divider()  # 👈 Draws a horizontal rule
    st.header('Delete Collection')

    db_name_del = st.text_input('dB name:')
    collection_name_del = st.text_input('Collection name:')

    if st.button('delete dB'):
        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        db = cluster[db_name_del]
        st.write("Collection Deleted:", collection_name_del)
        db[collection_name_del].drop()

    st.divider()  # 👈 Draws a horizontal rule
    st.header('Read Collection')

    db_name_read = st.text_input('dB name to read')
    collection_name = st.text_input('Collection name to read')
    if st.button('Read Collection'):
        import pandas as pd
        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        db = cluster[db_name_read]
        all_data_from_db = db[collection_name].find({})
        df = pd.DataFrame(list(all_data_from_db))
        st.write(df)
if selected == "Database Monitoring Tools":
        st.title('Database Monitoring Tools')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="1")
if selected == "Performance Analysis Tools":

    import pandas as pd
    import numpy as np
    import pydeck as pdk

    st.title('Site information tools')
    st.header('Map and table views')

    # st.write(os.getcwd())
    df_tokyo_1 = pd.read_csv("Random_Tokyo.csv",  index_col=False)


    max_lat = df_tokyo_1["lat"].max()
    min_lat = df_tokyo_1["lat"].min()
    max_lon = df_tokyo_1["lon"].max()
    min_lon = df_tokyo_1["lon"].min()
    zoom_level = 15
    # symrad = 30

    site_list = list(df_tokyo_1["Site Name"])#
    # site_list.insert(0, "     ")
    option = st.selectbox('Select Site to see statistics and information', site_list)

    selected = df_tokyo_1.loc[df_tokyo_1['Site Name'] == option]
    lat = selected["lat"].iloc[0]
    lon = selected["lon"].iloc[0]
    del selected["labels"]
    st.table(selected)

    if st.button('View Entire Layer'):
        zoom_level = 11
        lat = (max_lat + min_lat)/2
        lon = (max_lon + min_lon)/2
    else:
        pass

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude= lat, # (max_lat + min_lat)/2,
            longitude=lon, #(max_lon + min_lon)/2,
            zoom=zoom_level,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df_tokyo_1,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                pickable = True,
                tooltip = True,
                radiusScale= 5,
                radiusMinPixels=5,
                radiusMaxPixels= 5
            ),
            pdk.Layer(type="TextLayer",
                data=df_tokyo_1,
                pickable=False,
                get_position=["lon", "lat"],
                get_text="labels",
                get_size=12,
                get_color=[0, 0, 0],
                get_angle=0, # Note that string constants in pydeck are explicitly passed as strings
                # This distinguishes them from columns in a data set
                getTextAnchor='"middle"',
                get_alignment_baseline='"bottom"'

            )

        ],
        tooltip = {"text": "Site: {labels}\nPower: {Power}\nHeight: {Height}\nAzimuths: {Site azimths}"}
    )
    )

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Site Statistics')

    option = st.selectbox('Select Site to see statistics and information', site_list,key = "second")

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Site Statistics')

    option_2 = st.selectbox('Select Site to see statistics and information', site_list,key = "third")

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Site Configuration Statistics')

    uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True)
if selected == "RAN Monitoring Tools":
    import pandas as pd
    import numpy as np
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import pydeck as pdk

    st.title('Site view from MongodB database')

    db_name_read = "Sites" # st.text_input('dB name to read')
    collection_name = "Tokyo_Random_Sites" # st.text_input('Collection name to read')
    # if st.button('Read Collection'):

    uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
    cluster = MongoClient(uri, server_api=ServerApi('1'))
    db = cluster[db_name_read]
    all_data_from_db = db[collection_name].find({})
    df_tokyo_mongodb = pd.DataFrame(list(all_data_from_db))
    # st.write(df_tokyo_mongodb)

    zoom_level = 15
    # symrad = 30

    site_list = list(df_tokyo_mongodb["Site Name"])#
    # site_list.insert(0, "     ")
    option = st.selectbox('Select Site to see statistics and information', site_list)

    max_lat = df_tokyo_mongodb["lat"].max()
    min_lat = df_tokyo_mongodb["lat"].min()
    max_lon = df_tokyo_mongodb["lon"].max()
    min_lon = df_tokyo_mongodb["lon"].min()

    selected = df_tokyo_mongodb.loc[df_tokyo_mongodb['Site Name'] == option]
    lat = selected["lat"].iloc[0]
    lon = selected["lon"].iloc[0]
    del selected["labels"]
    st.table(selected)

    if st.button('View Entire Layer'):
        zoom_level = 11
        lat = (max_lat + min_lat)/2
        lon = (max_lon + min_lon)/2
    else:
        pass

    # chart_data = df_tokyo_mongodb[["lat","lon"]]


    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude= lat,# (max_lat + min_lat)/2,
            longitude=lon, # (max_lon + min_lon)/2,
            zoom=zoom_level,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df_tokyo_mongodb,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                pickable=True,
                tooltip=True, radiusScale=5,
                radiusMinPixels=5,
                radiusMaxPixels=5,
                # get_radius=50,
            ),
            pdk.Layer(type="TextLayer",
                data=df_tokyo_mongodb,
                pickable=False,
                get_position=["lon", "lat"],
                get_text="labels",
                get_size=12,
                get_color=[0, 0, 0],
                get_angle=0, # Note that string constants in pydeck are explicitly passed as strings
                # This distinguishes them from columns in a data set
                getTextAnchor='"middle"',
                get_alignment_baseline='"bottom"'
            ),
        ],
        tooltip={"text": "Site: {labels}\nPower: {Power}\nHeight: {Height}\nAzimuths: {Site azimths}"}
    ))

    st.divider()  # 👈 Draws a horizontal rule

    st.title('Random site generation')

    df_tokyo_gen = pd.DataFrame(np.random.randn(10000, 2) / [20, 20] + [35.690459, 139.695575], columns=['lat', 'lon'])

    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(df_tokyo_gen)
    st.download_button(label="Download Result File", data=csv, file_name='Total_output.csv', mime='text/csv', )

    # chart_data = df_tokyo[["lat","lon"]]

    max_lat = df_tokyo_gen["lat"].max()
    min_lat = df_tokyo_gen["lat"].min()
    max_lon = df_tokyo_gen["lon"].max()
    min_lon = df_tokyo_gen["lon"].min()

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=(max_lat + min_lat)/2,
            longitude=(max_lon + min_lon)/2,
            zoom=11,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df_tokyo_gen,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=50,
            ),
            pdk.Layer(type="TextLayer",
                data=df_tokyo_gen,
                pickable=False,
                get_position=["lon", "lat"],
                get_text="labels",
                get_size=12,
                get_color=[0, 0, 0],
                get_angle=0, # Note that string constants in pydeck are explicitly passed as strings
                # This distinguishes them from columns in a data set
                getTextAnchor='"middle"',
                get_alignment_baseline='"bottom"'
            ),
        ],
    ))
