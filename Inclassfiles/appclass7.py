import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time

st.title("stramlu wlemeents and widgets demo")
st.header("an overview of streamlits features")
st.subheader("streamlit is an amazing tool")
st.text("this is simile text output")
st.write("you can also use write rto rrender markdown dataframes or other objects")

st.markdown("### markdown support")
st.markdown("streamlit supports **Markdown**, including: \n -*Italic* \n- **Bold** \n -**Code blocks**")

st.code("st.title('Streamlit App')",language='python')

#Metrics
st.markdown("### Metrics widget")
st.metric(label="Revenue",value="$120,000",delta="$5000",delta_color="normal")
st.metric(label="User growth",value="25000",delta="-200",delta_color="normal")

st.subheader("selection widgrts")

agree=st.checkbox("I agree")

feedback=st.feedback("thumbs")

tags=st.pills("Tags",["sports","politivs","education"])

choice_radio=st.radio("Pick one",["cats","DOgs"])

shopping=st.multiselect("Buy",["Milk","Apples","Potaties"])

st.subheader("Sliders and inputs")

number=st.slider("Pick a number",0,100)

size=st.select_slider("Pick a size",["S","M","L"])

name=st.text_input("First name")
num_input=st.number_input("Pick a number",0,10)

text=st.text_area("TEXT TO TRANSLATE")

st.subheader("Date and time")
birthday=st.date_input("Your birthday")
meeting_time=st.time_input("Meeting time",time(9,0))

st.subheader("file and media")

uploaded_file=st.file_uploader("Upload a csv")
if uploaded_file:
    df_uploaded=pd.read_csv(uploaded_file)
    st.dataframe(df_uploaded)

audio=st.audio_input("record a voice message    ")

#photo=st.camera_input("Take a picture")

color=st.color_picker("Pick a color")

st.subheader("user input summary")
st.write({
    "agree":agree,
    "feedback":feedback,
    "tags":tags,
    "choice_radio":choice_radio,
    "shopping":shopping,
    "number":number,
    "size":size,
    "name":name,
    "num_input":num_input,
    "text":text,
    "birthday":birthday,
    "meeting_time":meeting_time,
    "uploaded_file":uploaded_file,
    "audio":audio,
    "color":color
})
