import streamlit as st
import pandas_datareader.data as web
import datetime 
st.header("Estados Unidos", divider= 'rainbow')
col1, col2 = st.columns(2,gap="large")

with col1:
    
    with st.container():
        st.subheader("CPI")
        start = datetime.datetime(2010,1,1)
        cpi = web.DataReader('CPIAUCSL', 'fred', start).pct_change().dropna()
        st.area_chart(cpi)
    with st.container():
        t3mo = web.DataReader('DGS3MO', 'fred', start).dropna()
        st.line_chart(t3mo)

with col2:
    st.subheader("GDP")
    with st.container():
        gdp = web.DataReader('GDP', 'fred', start ).dropna()
        st.line_chart(gdp)