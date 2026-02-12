import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="App Class 8", layout="wide")
st.sidebar.title("App Class 8 Sidebar")
option=st.sidebar.selectbox("Select a section",["Home","Data Visualization","About"])

st.title("Streamlit layout and page configuration")
st.subheader("columns layout")

data=pd.DataFrame({"Years":[2015,2016,2017,2018,2019,2020],"Sales":[150,200,250,300,350,400],"Profit":[15,20,25,30,35,40]})

st.dataframe(data)
col1,col2,col3=st.columns(3)

with col1:
    st.header("Sales Over Years")
    fig1, ax1=plt.subplots()
    ax1.plot(data["Years"],data["Sales"],marker='o',color='b')
    ax1.set_xlabel("Years")
    ax1.set_ylabel("Sales")
    ax1.set_title("Sales from 2015 to 2020")
    st.pyplot(fig1)

with col2:
    st.header("Profit Over Years")
    fig2, ax2=plt.subplots()
    ax2.plot(data["Years"],data["Profit"],marker='s',color='g')
    ax2.set_xlabel("Years")
    ax2.set_ylabel("Profit")
    ax2.set_title("Profit from 2015 to 2020")
    st.pyplot(fig2)
with col3:
    st.header("Sales vs Profit")
    fig3, ax3=plt.subplots()
    ax3.plot(data["Years"],data["Sales"],marker='o',label='Sales',color='b')
    ax3.plot(data["Years"],data["Profit"],marker='s',label='Profit',color='g')
    ax3.set_xlabel("Years")
    ax3.set_ylabel("Values")
    ax3.set_title("Sales and Profit Comparison")
    ax3.legend()
    st.pyplot(fig3)


st.subheader("Tabs example")
tab1, tab2, tab3=st.tabs(["Overview","Data","Summary"])


with tab1:
   st.write("This is the Overview tab.")


with tab2:
    st.write("This is the Data tab.")
    st.dataframe(data)

with tab3:
    st.write("This is the Summary tab.")
    st.write(f"Total Sales: {data['Sales'].sum()}")
    st.write(f"Total Profit: {data['Profit'].sum()}")

#create 3 tabs, one is for voice recording, second for image capturing and third for form entry
st.subheader("Media and Form Tabs")
tab_voice, tab_image, audio_form=st.tabs(["Voice Recording","Image Capture","Audio player"])
with tab_voice:
    st.write("Voice Recording Tab")
    audio_data=st.audio_input("Record your voice")
   

with tab_image:
    st.write("Image Capture Tab")
    img_file=st.file_uploader("Upload an image", type=["png","jpg","jpeg"])
    if img_file is not None:
        st.image(img_file, caption="Uploaded Image", use_column_width=True)

with audio_form:
    st.write("Audio Player Tab")
    st.audio(audio_data, format="audio/wav")

st.subheader("Container Example")
with st.container():
    st.write("Enter student details:")
    student_name=st.text_input("Student Name")
    student_age=st.number_input("Student Age",0,100)
    department=st.selectbox("Department",["Science","Arts","Commerce"])
    agree=st.checkbox("I agree to the terms and conditions")
    if st.button("Submit"):
        st.write("Student Details Submitted:")
        st.write(f"Name: {student_name}, Age: {student_age}, Department: {department}, Agreed: {agree}")

st.subheader("Expander Example")
with st.expander("feedvack form"):
    feedback=st.text_area("Provide your feedback here")
    rating=st.slider("Rate our app",1,5,3)
    feedback=st.text_area("Additional Comments")
    recommend=st.radio("Would you recommend us?",("Yes","No"))
    color=st.color_picker("Pick your favorite color","#00f900")
    if st.button("Submit Feedback"):
        st.write("Thank you for your feedback!")
        st.write(feedback)

st.subheader("Information")
st.write({
    "Name":student_name,
    "Age":student_age,
    "Department":department,
    "Agreed":agree,
    "Rating":rating if 'rating' in locals() else None,
    "Recommend":recommend if 'recommend' in locals() else None,
})

st.markdown("---")
st.write("selected option from sidebar:", option )