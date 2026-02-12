import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time

st.set_page_config(page_title="App Class S6", layout="wide")
"""st.title("Welcome to App Class S6")
st.write("This is a simple Streamlit application for demonstration purposes.")
st.button("Click Me!")#it is a widget

data=pd.DataFrame({
    'Name':['Alice','Bob','Charlie','David'],
    'Age':[24,30,22,35],
    'Department':['HR','Finance','IT','Marketing']
}   )
st.subheader("Employee Data")
st.dataframe(data)"""

df=pd.read_csv('C:\\Users\\KARUN NAGARAJ\\Downloads\\advanced python\\MortalityDataset.csv')

st.subheader("Mortality Data")
st.dataframe(df)

st.subheader("Editable Mortality Data")
edited_data=st.data_editor(df)

#question: create a page import dataset display as a table.
# Identify one column, create a selection button to filter it.

options= st.multiselect("select a mortality type", df['MORT'].unique())
st.dataframe(df[df['MORT'].isin(options)])

#sliding bar option button
age=st.slider("Select Age",df['AGE'].min(),df['AGE'].max())
st.dataframe(df[df['AGE']<age])

#create a calculator with two sliding bars to choose two numbers then crate radio buttons to perform operations of add etc
st.subheader("Simple Calculator")
num1=st.slider("Select first number",0.0,100.0,25.0)
num2=st.slider("Select second number",0.0,100.0,75.0)
operation=st.radio("Select Operation",('Add','Subtract','Multiply','Divide'))
if operation=='Add':
    res=num1+num2
elif operation=='Subtract':
    res=num1-num2
elif operation=='Multiply':
    res=num1*num2
elif operation=='Divide':
    res=num1/num2 if num2!=0 else 0
st.write("The result of {} {} {} is {}".format(num1,operation,num2,res))