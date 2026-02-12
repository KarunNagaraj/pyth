import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time

st.set_page_config(page_title="App Class 7 Pt2", layout="wide")

st.title("data display and visualizations in streamlit")

data=pd.DataFrame({"Months":["Jan","Feb","Mar","Apr","May","Jun"],
                   "Sales":[200,400,300,500,700,600],
                   "Profit":[20,40,30,50,70,60]})

st.subheader("Dataframe Display")

st.write("using st.write() ")
st.write(data)

st.write("using st.dataframe() ")
st.dataframe(data)

st.write("using st.table() ")
st.table(data)

st.subheader("Built in streamlit charts")

st.write("using st.line_chart() ")
st.line_chart(data.set_index("Months")[["Sales"]])
st.bar_chart(data.set_index("Months")[["Profit"]])
st.area_chart(data.set_index("Months")[["Sales","Profit"]])

st.subheader("Matplotlib Visualization")

import matplotlib.pyplot as plt

fig, ax=plt.subplots()
ax.plot(data["Months"],data["Sales"],marker='o',label='Sales')
ax.plot(data["Months"],data["Profit"],marker='s',label='Profit')
ax.set_xlabel("Months")
ax.set_ylabel("Profits")
ax.set_title("Sales and Profit over Months")
ax.legend()

st.pyplot(fig)

st.header("forms and input handling")

with st.form("my_form"):
    
    name=st.text_input("Enter your name")
    age=st.number_input("Enter your age",0,100)
    submitted=st.form_submit_button("Submit")
    if submitted:
        st.write("form submitted")
        st.write(f"Name: {name}, Age: {age}")
        st.success("Form submitted successfully!")