import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Planning & Optimization Modules",[
        "Geolocation Based RAN Planning",
        "Geolocation Based RAN Infrastructure Planning",
        "Radio Frequency (RF) Planning and Optimization",
        "Database Migration",
        "Machine Learning / AI use case design optimization projects",
        "Performance Monitoring and Optimization",
        "Reporting and Analytics",
        "Database Management",
        "Toolkit",
        ], menu_icon="cast", default_index=0)

if selected == "Geolocation Based RAN Planning":
    import pandas as pd
    import GC_functions as gc
    import numpy as np

    st.title('Virtual RAN Planning')
    st.header('Virtual RAN Group Center Virtual Control Unit Planning from Database')
    # st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
    # st.header('This is a header')
    # st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')

    max_dist_allowed = 3 # 1.7
    gc_df = []
    site_df =[]

    city_list = ["Dusseldorf", "Essen", "Frankfurt", "Cologne", "Tokyo","Osaka","London","Manchester","Birmingham","Tel_Aviv","Jerusalem", "Istanbul","Haifa"]
    option = st.selectbox('Please Select The City', city_list)
    if st.button("Process from online database"):
        import pandas as pd
        import numpy as np
        from pymongo.mongo_client import MongoClient
        from pymongo.server_api import ServerApi
        import pydeck as pdk

        db_name_read = "Sites"  # st.text_input('dB name to read')


        collection_name = option

        # st.text_input('Collection name to read')
        # if st.button('Read Collection'):

        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        db = cluster[db_name_read]
        all_data_from_db = db[collection_name].find({})
        site_df_1 = pd.DataFrame(list(all_data_from_db)).head(1000)  # st.write(df_tokyo_mongodb)
        site_df_2 = site_df_1[["index","Site Name","lat","lon"]]
        site_df_2["GC_Name"] = "G" + site_df_2["Site Name"].str[:2]
        site_df_2.rename(columns={'Site Name': 'Sarf'}, inplace=True)
        site_df = site_df_2.head(3000)
        # st.write(site_df)


        # del site_df["_id"]
        # del site_df["Unnamed: 0"]
        del site_df["index"]

        collection_name = "gc_list_2"
        gc_data_from_db = db[collection_name].find({})
        gc_df = pd.DataFrame(list(gc_data_from_db))

        del gc_df["_id"]
        del gc_df["Unnamed: 0"]
        del gc_df["index"]
        # st.write(gc_df)

    st.divider()
    st.header('Virtual RAN Group Center Virtual Control Unit Planning from csv file')

    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True)
    # st.write(len(uploaded_file))
    # if len(uploaded_file) != 2:
        # st.write("Please upload 2 files only")

    if st.button('Process uploaded files'):
    # if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        for i in range(len(uploaded_file)):
            # st.write(uploaded_file[i].name)
            if uploaded_file[i].name == "gc_list.csv":
                gc_df = pd.read_csv(uploaded_file[i],  index_col=0)
            if uploaded_file[i].name == "site_data.csv":
                site_df = pd.read_csv(uploaded_file[i],  index_col=0).head(1000)

    # st.write(site_df)
    # st.write(gc_df)
    #

    Total_output = pd.DataFrame(columns=['Sarf','lat','lon','GC_Name','group','size'])
    Total_output.loc[0, ['lat', 'lon','size','Sarf','GC_Name','group']] = [1, 1,20,"Deneme","GC",3]
    # st.write(Total_output)
    st.divider()
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

    st.table(chart_data.head(20))

    st.divider()  # 👈 Draws a horizontal rule
    st.header('VDU RIU RRH Planning')
    uploaded_file_2 = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "second")
    st.divider()  # 👈 Draws a horizontal rule
    st.header('DAY 1 Format Preparation')
    uploaded_file_3 = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "third")

    csv = convert_df(Total_output)
    st.download_button(label="Download Result File", data=csv, file_name='Total_output.csv', mime='text/csv', )

if selected == "Geolocation Based RAN Infrastructure Planning":
    import pandas as pd
    import pydeck as pdk
    # import fiona
    import geopandas as gpd
    # from shapely.geometry import Point, Polygon
    import numpy as np

    st.title('Geolocation Based Transport Infrastructure Planning')
    st.header('Fiber optical line distance analysis')
    # uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "first")

    city_list = ["Dusseldorf", "Essen", "Frankfurt", "Cologne", "Tokyo", "Osaka", "London", "Manchester", "Birmingham", "Tel_Aviv", "Jerusalem", "Istanbul","Haifa"]
    option = st.selectbox('Please Select The City to view fiber optical lines', city_list)
    dir = "C:/Users/barba/Downloads/data/fiber/"

    File_Name = option[:3]+"_fiber.tab"
    File_Name_2 = option[:3] + "_fiber_2.tab"
    File_Name_3 = option[:3] + "_fiber_3.tab"
    # File_Name = "C:/Users/barba/Downloads/data/fiber/Mainz.tab"
    def hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i: i + 2], 16) for i in (0, 2, 4))
    def path_line_dist(df_tab_file, point):
        from geopy.distance import geodesic
        import geopandas as gpd
        def closest_pair(point, a, b):
            c = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)

            d1 = [geodesic(point, a).m, a]
            d2 = [geodesic(point, b).m, b]
            d3 = [geodesic(point, c).m, c]

            sorted_list = sorted([d1, d2, d3], key=lambda sublist: sublist[0])
            return sorted_list[0], sorted_list[1]

        def point_line_dist(line_start, line_end, point):
            x = closest_pair(point, line_start, line_end)
            # print(x)
            for i in range(10):
                x = closest_pair(point, x[0][1], x[1][1])  # print(x)
            return x

        line_parts = df_tab_file['geometry'].apply(lambda line: list(line.coords))
        shortest_dist = []
        for parts in line_parts:
            # print(parts)
            for i in range(len(parts) - 1):
                line_start = (parts[i][1], parts[i][0])
                line_end = (parts[i + 1][1], parts[i + 1][0])
                shortest_dist.append(point_line_dist(line_start, line_end, point)[0])
        return min(shortest_dist)  # for i in range(len(line_parts[0])-1):  #     line_start = (line_parts[0][i][1] , line_parts[0][i][0])  #     line_end = (line_parts[0][i+1][1] , line_parts[0][i+1][0])  #     # print(point_line_dist(line_start, line_end, point)[0][1])  #     # shortest_dist.append(point_line_dist(line_start, line_end, point)[0][0])
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')
    if st.button("Process from online database"):
        df_tab_file = gpd.read_file(File_Name, driver="MapInfo File")
        df_tab_file_2 = gpd.read_file(File_Name_2, driver="MapInfo File")
        df_tab_file_3 = gpd.read_file(File_Name_3, driver="MapInfo File")
        tab_files = [df_tab_file, df_tab_file_2, df_tab_file_3]
        # Reading from online db


        # End - reading from online dB


        df_news =[0,1,2]
        # tab file start
        j = 0
        color_list = ["#ed1c24","#0246ff","#ffcc33"]
        for df_tab_file in tab_files:
            # st.write(df_tab_file)
            df_tab_file['path'] = df_tab_file.apply(lambda x: [y for y in x['geometry'].coords], axis=1)
            df_tab_file.to_dict('records')

            for i in range(len(df_tab_file)):
                tuples = df_tab_file['path'][i]
                lists = [list(t) for t in tuples]
                # lists = [[t[1], t[0]] for t in tuples]
                df_tab_file['path'][i] = lists

            df_tab_file.rename(columns={"Name": "name"}, inplace=True)

            df_new = pd.DataFrame(columns=['name', 'color', 'path'])
            df_new["name"] = df_tab_file["name"]
            df_new["color"] = color_list[j]
            df_new["path"] = df_tab_file["path"]

            df_new["color"] = df_new["color"].apply(hex_to_rgb)
            lon_cen_1 = df_new["path"][0][0][0]
            lat_cen_1 = df_new["path"][0][0][1]
            df_news[j] = df_new
            j = j +1

        view_state = pdk.ViewState(latitude= lat_cen_1, longitude=lon_cen_1, zoom=10)

        df_news_0 = df_news[0]
        df_news_1 = df_news[1]
        df_news_2 = df_news[2]


    # Reading sites from database to plan

        from pymongo.mongo_client import MongoClient
        from pymongo.server_api import ServerApi

        db_name_read = "Sites"
    # option = st.selectbox('Please Select The City', city_list)
        collection_name = option  # st.text_input('Collection name to read')

        uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
        cluster = MongoClient(uri, server_api=ServerApi('1'))
        db = cluster[db_name_read]
        all_data_from_db = db[collection_name].find({})
        df_tokyo_mongodb = pd.DataFrame(list(all_data_from_db)).head(30)

    # Uploaded sites list

        uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True)



    # Calculating fiber distances

        df_result = pd.DataFrame(columns=["Point", "Min_Distance"])
        df_points = df_tokyo_mongodb
        points = []
        min_results_own = []
        min_results_V1 = []
        min_results_V2 = []


        for i in range(len(df_points)):
            point = (df_points.iloc[i].lat, df_points.iloc[i].lon)
            min_distance_1 = path_line_dist(df_tab_file,point)
            min_distance_2 = path_line_dist(df_tab_file_2,point)
            min_distance_3 = path_line_dist(df_tab_file_3,point)
            points.append(point)
            min_results_own.append(min_distance_1[0])
            min_results_V1.append(min_distance_2[0])
            min_results_V2.append(min_distance_3[0])

        df_result["Point"] = points
        df_result["Site Name"] = df_tokyo_mongodb["Site Name"]
        df_result["Min_Distance_Own"] = min_results_own
        df_result["Min_Distance_V1"] = min_results_V1
        df_result["Min_Distance_V2"] = min_results_V2
        # df_result["Min_Distance"] = df_result.apply(lambda row: min(row["Min_Distance_Own"],row["Min_Distance_V1"],row["Min_Distance_V2"]), axis=1)
        # df['min_value'] = df.apply(lambda row: min(row['col1'], row['col2'], row['col3']), axis=1)
        df_result["Min_Distance"]  = df_result[["Min_Distance_Own", "Min_Distance_V1", "Min_Distance_V2"]].min(axis=1)
        csv = convert_df(df_result)

        st.download_button(label="Download Result File", data=csv, file_name='Result_output.csv', mime='text/csv', )

        # Displaying maps

        st.pydeck_chart(pdk.Deck(
            map_style=None,
            initial_view_state= view_state,
            layers=[
                pdk.Layer(
                    type="PathLayer",
                    data=df_news_0,
                    pickable=True,
                    get_color="color",
                    width_scale=5,
                    width_min_pixels=2,
                    get_path="path",
                    get_width=2
                ),
                pdk.Layer(type="PathLayer",
                    data=df_news_1,
                    pickable=True,
                    get_color="color",
                    width_scale=5,
                    width_min_pixels=2,
                    get_path="path",
                    get_width=2),
                pdk.Layer(type="PathLayer",
                    data=df_news_2,
                    pickable=True,
                    get_color="color",
                    width_scale=5,
                    width_min_pixels=2,
                    get_path="path",
                    get_width=2),
                pdk.Layer('ScatterplotLayer',
                    data=df_tokyo_mongodb,
                    get_position='[lon, lat]',
                    get_color='[200, 30, 0, 160]',
                    pickable=True,
                    tooltip=True,
                    radiusScale=2,
                    radiusMinPixels=2,
                    radiusMaxPixels=2, # get_radius=50,
        ),
            ],
            # tooltip={"Name: {name}"}
            tooltip = {"text": "Site Name: {Site Name}"}
        ))

        st.dataframe(df_result)

    if st.button('Process uploaded files'):
        df_tokyo_mongodb = pd.read_csv(uploaded_file, index_col=0)

    st.divider()  # 👈 Draws a horizontal rule
    st.header('Site candidate Fiber cost opex/capex analysis')
    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "second")
    st.divider()  # 👈 Draws a horizontal rule
    st.header('Multi vendor Fiber cost opex/capex analysis')
    uploaded_file = st.file_uploader("Choose input CSV files to process",type= "csv",accept_multiple_files=True,key = "third")
    st.divider()  # 👈 Draws a horizontal rule

if selected == "Database Migration":
    import pandas as pd
    import GC_functions as gc
    import numpy as np
    import Data_migration_functions as cpf

    st.title('Data Migration From Atoll to Planet Microservices')
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
        from PIL import Image
        st.title('Machine Learning Network Performance Booster Toools')
        st.divider()  # 👈 Draws a horizontal rule
        st.header('KPI Anomaly Heat-Map')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="1")
        picture = Image.open(r'Picture1.png')
        st.image(picture,use_column_width=True)
        st.divider()  # 👈 Draws a horizontal rule
        st.header('Silent Issue detection')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="2")
        st.divider()  # 👈 Draws a horizontal rule
        st.header('Load Balance/Mobility load balance parameter optimization')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="3")
        st.divider()  # 👈 Draws a horizontal rule
        st.header('Energy Efficiency Management')
        uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True,key="4")
        picture2 = Image.open(r'Picture2.png')
        st.image(picture2,use_column_width=True)

if selected == "Database Management":
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import pandas as pd

    st.title('Database Management')
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
    st.header('Create Collection with CSV file')
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
        db = cluster["Sites"]
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

if selected == "Performance Monitoring and Optimization":
    import pandas as pd
    import numpy as np
    import pydeck as pdk
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi

    st.title('Site information')
    st.header('Map and table views')

    db_name_read = "Sites" # st.text_input('dB name to read')
    city_list = ["Dusseldorf", "Essen", "Frankfurt", "Cologne", "Tokyo", "Osaka", "London", "Manchester", "Birmingham", "Tel_Aviv", "Jerusalem", "Istanbul","Haifa" ]
    option_1 = st.selectbox('Please Select The City', city_list,key=1)
    collection_name = option_1 # st.text_input('Collection name to read')
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
        tooltip={"text": "Site: {labels}\nPower: {Power}\nHeight: {Height}\nAzimuths: {Site azimths}\n5G Bands: {5G_Bands}\n4G Bands: {4G_Bands}"}
    ))


    st.divider()  # 👈 Draws a horizontal rule

    st.header('Region Statistics and Performance')
    region_list = ["Region_1","Region_2","Region_3","Region_4","Region_5","Region_6","REgion_7","Region_8"]

    option_2 = st.selectbox('Select Regions to see statistics and information', region_list,key = "third")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.bar_chart(chart_data)

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Network Configuration')

    uploaded_file = st.file_uploader("Choose files",accept_multiple_files=True)

    st.divider()  # 👈 Draws a horizontal rule

    st.header('RAN Analytics')

    option = st.selectbox('Select Site to see statistics and information', site_list,key = "4")

    st.divider()  # 👈 Draws a horizontal rule
    st.header('Site Statistics')

    option = st.selectbox('Select Site to see statistics and information', site_list, key="5")

    st.divider()  # 👈 Draws a horizontal rule

if selected == "Toolkit":
    import pandas as pd
    import numpy as np
    import pydeck as pdk

    st.title('Sites')
    center_lat = 51.512696
    center_lon = -0.122940
    total_numbers = 10000

    df_tokyo_gen = pd.DataFrame(np.random.randn(total_numbers, 2) / [20, 20] + [center_lat,center_lon ], columns=['lat', 'lon'])


    def point_check_P(p1, gdf_reg):
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

    def df_planet_lte_cells_rural_urban_class(df_planet_lte_cells, tab_file):
        import fiona
        import geopandas as gpd
        from shapely.geometry import Point, Polygon
        import pandas as pd
        import webbrowser
        import numpy as np
        import os
        import time

        df_tab_file = gpd.read_file(tab_file, driver="MapInfo File")

        start = time.time()
        local_time = time.ctime(start)
        print("Local time:", local_time)

        gdf_reg = df_tab_file.explode()
        df_planet_lte_cells['Urban_Rural'] = df_planet_lte_cells.apply(lambda x: point_check_P((Point(x['Longitude'], x['Latitude'])), gdf_reg), axis=1)

        # df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "urban", "Propagation Model"] = df_planet_lte_cells["Propagation Model"].str[:-4] + "_urban.pmf"
        # df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "rural", "Propagation Model"] = df_planet_lte_cells["Propagation Model"].str[:-4] + "_rural.pmf"

        # df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "urban", "Distance (km)"] = 3
        # df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "rural", "Distance (km)"] = 10
        # df_planet_lte_cells["Urban_Rural"]
        df_planet_lte_cells = df_planet_lte_cells.loc[df_planet_lte_cells["Urban_Rural"] == "urban"]
        # df.loc[df['column_name'] != some_value]

        end = time.time()
        print(end - start)

        return df_planet_lte_cells

    tab_file = "London.tab"

    df_tokyo_gen["Longitude"] = df_tokyo_gen["lon"]
    df_tokyo_gen["Latitude"] = df_tokyo_gen["lat"]

    df_tokyo_gen = df_planet_lte_cells_rural_urban_class(df_tokyo_gen, tab_file)

    def convert_df(df):
        return df.to_csv(index=None).encode('utf-8')


    column_names = ["Site Name","lat","lon","Site azimths","Height","Power","labels","5G_Bands","4G_Bands"]
    result_df = pd.DataFrame(columns=column_names)
    result_df["lat"] = df_tokyo_gen["lat"]
    result_df["lon"] = df_tokyo_gen["lon"]
    result_df["Site azimths"] = "0,120,240"
    result_df["Height"] = 25
    result_df["Power"] = 45
    result_df["5G_Bands"] = "XXXXX"
    result_df["4G_Bands"] = "YYYYY"
    result_df["Site Name"] = range(1, len(result_df) + 1)
    result_df['Site Name'] = result_df['Site Name'].apply(lambda x: 'LON_' + str(x))
    result_df["labels"] = result_df['Site Name']
    csv = convert_df(result_df)
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

if selected == "Reporting and Analytics":
    import pandas as pd
    import numpy as np
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import pydeck as pdk

    st.title('RAN information')
    st.header('Site view')

    db_name_read = "Sites" # st.text_input('dB name to read')
    city_list = ["Dusseldorf", "Essen", "Frankfurt", "Cologne", "Tokyo", "Osaka", "London", "Manchester", "Birmingham", "Tel_Aviv", "Jerusalem", "Istanbul","Haifa"]
    option = st.selectbox('Please Select The City', city_list,key = 25)
    collection_name = option # st.text_input('Collection name to read')
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
    option = st.selectbox('Select Site to see statistics and information', site_list, key = 26 )

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
        tooltip={"text": "Site: {labels}\n"
                         "Power: {Power}\n"
                         "Height: {Height}\n"
                         "Azimuths: {Site azimths}\n"
                         "5G Bands: {5G_Bands}\n"
                         "4G Bands: {4G_Bands}"
                        }
    ))

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Site Statistics')

    option_2 = st.selectbox('Select Site to see statistics and information', site_list,key = 27)

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Site Configuration Statistics')

if selected == "Radio Frequency (RF) Planning and Optimization":
    import pandas as pd
    import numpy as np
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi
    import pydeck as pdk

    st.title('Radio Frequency (RF) Planning and Optimization')
    st.header('Site view')

    db_name_read = "Sites" # st.text_input('dB name to read')
    city_list = ["Dusseldorf", "Essen", "Frankfurt", "Cologne", "Tokyo", "Osaka", "London", "Manchester", "Birmingham", "Tel_Aviv", "Jerusalem", "Istanbul","Haifa"]
    option = st.selectbox('Please Select The City', city_list,key = 25)
    collection_name = option # st.text_input('Collection name to read')
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
    option = st.selectbox('Select Site to see statistics and information', site_list, key = 26 )

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
        tooltip={"text": "Site: {labels}\n"
                         "Power: {Power}\n"
                         "Height: {Height}\n"
                         "Azimuths: {Site azimths}\n"
                         "5G Bands: {5G_Bands}\n"
                         "4G Bands: {4G_Bands}"
                        }
    ))

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Site Statistics')

    option_2 = st.selectbox('Select Site to see statistics and information', site_list,key = 27)

    st.divider()  # 👈 Draws a horizontal rule

    st.header('Site Configuration Statistics')

