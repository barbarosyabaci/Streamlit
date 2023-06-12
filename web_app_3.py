import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Training Calculator"], menu_icon="cast", default_index=0)


if selected == "Training Calculator":

    list_1 = []
    max = st.slider("Select a value",min_value=10, max_value=300)
    for no_of_reps in range(1, 20):
        weight = max / (1 + (0.0333 * no_of_reps))
        list_1.append((no_of_reps, round(weight)))
    st.write(list_1[0],	list_1[1],	list_1[2],	list_1[3],	list_1[4],	list_1[5],	list_1[6],	list_1[7],	list_1[8],	list_1[9],	list_1[10],	list_1[11],	list_1[12],	list_1[13],	list_1[14],	list_1[15],	list_1[16]
)
