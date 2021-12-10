import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")
st.header('Статистика перевода')
with st.container() as one:
    col_1, col_2 = st.columns(2)
    with col_1:
        text = st.text_input(label = 'Исходный текст', value= '783953 71849', max_chars= 16)
        text = str(text)
    with col_2:
        out = ''
        glas = 0
        soglas = 0
        st.write('Декодированный текст')
        for i in text:
            if i == '1':
                out+=str('А')
                glas+=1
            if i == '2':
                out+=str('Е')
                glas+=1
            if i == '3':
                out+=str('О')
                glas+=1
            if i == '4':
                out+=str('У')
                glas+=1
            if i == '5':
                out+=str('Т')
                soglas+=1
            if i == '6':
                out += str('Л')
                soglas+=1
            if i == '7':
                out += str('П')
                soglas+=1
            if i == '8':
                out+=str('Р')
                soglas+=1
            if i == '9':
                out+=str('С')
                soglas+=1
            if i == ' ':out+=str(' ')
        st.write(out)
with st.container() as glasn:
    title, col_1 = st.columns(2)
    with title:
        st.write('Количество гласных букв')
    with col_1:
        st.metric(label='', value=glas)
with st.container() as soglasn:
    title, col_1 = st.columns(2)
    with title:
        st.write('Количество согласных букв')
    with col_1:
        st.metric(label='', value=soglas)