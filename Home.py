import streamlit as st
#criar um arquivo venv para as bibliotecas, ai quando entrar denovo, é só ativar o venv e rodar o codigo Home.py
st.set_page_config(layout="wide")

st.header("Economics", divider="rainbow")

col1, col2 = st.columns(2,gap="large")

with col1:
    st.subheader("A cat")
    st.container(height = 200)
with col2:
    st.subheader("Taxa de juros")
    st.container(height = 200)



st.write("### Metric")

col1, col2, col3 = st.columns(3, gap = "large")

with col1:
    with st.container(height = 200):
        st.subheader("eua")
        st.metric("Temperature", "70 F", "1.2 F")

with col2:
    with st.container(height = 200):
        st.subheader("juros")
        st.metric("Temperature", "70 F", "1.2 F")

with col3:
    with st.container(height = 200):
        st.subheader("moeda")
        st.metric("Temperature", "70 F", "1.2 F")