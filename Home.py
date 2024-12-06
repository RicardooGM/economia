import streamlit as st
#criar um arquivo venv para as bibliotecas, ai quando entrar denovo, é só ativar o venv e rodar o codigo Home.py
st.header("Economics", divider="rainbow")

col1, col2 = st.columns(2,gap="large")

with col1:
    st.subheader("A cat")
    st.container(height = 200)
with col2:
    st.subheader("Taxa de juros")
    st.container(height = 200)