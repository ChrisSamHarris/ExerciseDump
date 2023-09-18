import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Average World Temperature", layout="centered", page_icon="🌡️")
st.title("Average World Temperature")

df = pd.read_csv("data.txt")
figure = px.line(x=df['date'], y=df['temperature'], labels={"x":'date', "y":'temperature'})
st.plotly_chart(figure)
