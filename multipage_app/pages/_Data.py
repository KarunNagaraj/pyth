import streamlit as st
import pandas as pd

st.title("Data page")

data=pd.DataFrame({"years":[2015,2016,2017,2018,2019,2020],"sales":[150,200,250,300,350,400],"profit":[15,20,25,30,35,40]})

st.dataframe(data)
st.line_chart(data.set_index("years")["sales"])

