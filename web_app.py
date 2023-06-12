import streamlit as st
from  PIL import Image


from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Upload", "Tasks",'Maps', 'Settings', 'About'], icons=['house', 'gear'], menu_icon="cast", default_index=1)

if selected == "Home":
    x = st.slider("Select a value")
    st.write(x, "squared is", x * x)
    no_of_sets = 3
    max = 50
    no_of_reps = 12

    # https://www.masterclass.com/articles/one-rep-max-calculator
    # dict_1 = {}
    list_1 = []

    site_list = (
    "City1_1",
    "City1_2",
    "City1_3",
    "City1_4",
    "City1_5",
    "City1_6",
    "City1_7",
    "City1_8",
    "City1_9",
    "City1_10",
    "City1_11",
    "City1_12",
    "City1_13",
    "City1_14",
    "City1_15",
    "City1_16",
    "City1_17",
    "City1_18",
    "City1_19",
    "City1_20",
    "City1_21",
    "City1_22",
    "City1_23",
    "City1_24",
    "City1_25",
    "City1_26",
    "City1_27",
    "City1_28",
    "City1_29",
    "City1_30",
    "City1_31",
    "City1_32",
    "City1_33",
    "City2_1",
    "City2_2",
    "City2_3",
    "City2_4",
    "City2_5",
    "City2_6",
    "City2_7",
    "City2_8",
    "City2_9",
    "City2_10",
    "City2_11",
    "City2_12",
    "City2_13",
    "City2_14",
    "City2_15",
    "City2_16",
    "City2_17",
    "City2_18",
    "City2_19",
    "City2_20",
    "City2_21",
    "City2_22",
    "City2_23",
    "City2_24",
    "City3_1",
    "City3_2",
    "City3_3",
    "City3_4",
    "City3_5",
    "City3_6",
    "City3_7",
    "City3_8",
    "City3_9",
    "City3_10",
    "City3_11",
    "City3_12",
    "City3_13",
    "City3_14",
    "City3_15",
    "City3_16",
    "City3_17",
    "City3_18",
    "City3_19",
    "City3_20",
    "City3_21",
    "City3_22",
    "City3_23",
    "City3_24",
    "City3_25",
    "City3_26",
    "City3_27",
    "City3_28",
    "City3_29",
    "City3_30",
    "City3_31",
    "City3_32",
    "City3_33",
    "City3_34",
    "City3_35",
    "City3_36",
    "City3_37",
    "City3_38",
    "City3_39",
    "City3_40",
    "City3_41",
    "City3_42",
    "City3_43",
    "City3_44",
    "City3_45",
    "City3_46",
    "City3_47",
    "City3_48",
    "City3_49",
    "City3_50",
    "City3_51",
    "City3_52",
    "City3_53",
    "City3_54",
    "City3_55",
    "City3_56",
    "City3_57",
    "City3_58",
    "City3_59",
    "City3_60",
    )
    option = st.selectbox(
        'Select Site?',
        site_list)

    for no_of_reps in range(1,31):
        weight = max/(1 + (0.0333 * no_of_reps))
        Volume = weight * no_of_sets * no_of_reps
        list_1.append((no_of_reps,round(weight), round(Volume),"abc"))

    st.write(list_1[1][1])

    import pandas as pd
    import numpy as np

    df = pd.DataFrame(
       np.random.randn(5, 5),
       columns=('col %d' % i for i in range(5)))

    st.dataframe(df)  # Same as st.write(df)

    df = pd.DataFrame(
        [
           {"command": "selectbox", "rating": 4, "is_widget": True},
           {"command": "balloons", "rating": 5, "is_widget": False},
           {"command": "time_input", "rating": 3, "is_widget": True},
       ]
    )
    edited_df = st.data_editor(df)


    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"])

    st.bar_chart(chart_data)




    st.write('You selected:', option)



    # favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    # st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

logo = Image.open(r'C:\Users\barba\PycharmProjects\pythonProject\2023_works\1.jpg')
profile = Image.open(r'C:\Users\barba\PycharmProjects\pythonProject\2023_works\2.jpg')

if selected == "About":
    col1, col2 = st.columns([0.8, 0.2])
    with col1:  # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)
    with col2:  # To display brand log
        st.image(logo, width=130)

    st.write("Seyhun Barbaros YABACI")
    st.image(profile, width=700)

if selected == "Maps":
    st.write("To view Maps")
    import pydeck as pdk
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(
        np.random.randn(150, 2) / [50, 50] + [32.10, 34.80],
        columns=['lat', 'lon'])

    st.map(df)
    chart_data = pd.DataFrame(
       np.random.randn(100, 2) / [50, 50] + [32.10, 34.80],
       columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=32.10,
            longitude=34.80,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HexagonLayer',
               data=chart_data,
               get_position='[lon, lat]',
               radius=100,
               elevation_scale=4,
               elevation_range=[50, 300],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))


if selected == "Upload":
    st.write("Place for files to upload")

if selected == "Tasks":
    st.write("To run various Tasks")

if selected == "Settings":
    st.write("For various settings")