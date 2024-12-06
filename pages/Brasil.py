import streamlit as st
import pandas as pd
from bcb import sgs

st.header("Brasil")
st.subheader("Inflação", divider="rainbow")

with st.container():
    st.write("IPCA mensal")
    opcoes = ["3","6","12","36","120"]
    
    selection = st.pills("",opcoes, selection_mode="single")
    codigo = {"IPCA": 433}
    dados = sgs.get(codigo, last = selection).dropna()
    
    st.line_chart(dados)