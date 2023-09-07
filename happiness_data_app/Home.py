#GDP Happiness Generosity 
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Happiness", layout="centered", page_icon="😊")

st.title("In Search for Happiness")
x_axis = st.selectbox("Select data for the x-axis:",('GDP','Happiness', 'Generosity'), help="Choose the data to be used as comparison in the x-axis")
y_axis = st.selectbox("Select data for the y-axis:",('Happiness','GDP','Generosity'), help="Choose the data to be used as comparison in the y-axis")

st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv('happy.csv')

figure = px.scatter(x=df[x_axis.lower()], y=df[y_axis.lower()], labels={"x":x_axis, "y":y_axis})
st.plotly_chart(figure)


# def get_data(days):
#     fake_dates = ["07-09-2023", "08-09-2023","09-09-2023","10-09-2023","11-09-2023"]
#     fake_temp = [10, 15, 16, 18, 12]
#     fake_temp = [days * i for i in fake_temp]
#     return fake_dates, fake_temp   

# d, t = get_data(num_days)

