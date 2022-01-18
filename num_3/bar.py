import streamlit as st
import pandas as pd
st.set_page_config(layout = "wide")
data = pd.read_csv("https://github.com/iilyazakos/python_ex_2/blob/914413817b9bca86353093cab810ac467900ea38/num_3/bar_data.csv?raw=true")
st.write(data)
with st.container() as one_data:
    one, two = st.columns(2)
    with one:
        data_html = data.to_html()
        st.download_button(
            label = "Cкачать исходную таблицу в html",
            data = data_html,
            file_name = 'table.html')
    with two:
        param = st.radio("Выберите по какому столбцу сортировать?", ('one', 'two', 'three', 'four'))
        if param == "one": a = data.sort_values(by = 'Первая_марка')
        if param == "two": a = data.sort_values(by = 'Вторая_марка')
        if param == "three": a = data.sort_values(by = 'Третья_марка')
        if param == "four": a = data.sort_values(by = 'Четвёртая_марка')
st.write(a)
with st.container() as download:
    three, four = st.columns(2)
    with three:
        data_html_up = a.to_html()
        st.download_button(
            label="Cкачать отсортированную таблицу в html",
            data=data_html_up,
            file_name='table.html')
