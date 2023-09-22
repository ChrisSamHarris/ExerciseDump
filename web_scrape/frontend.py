import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

connection = sqlite3.connect("temp_data.db")

st.set_page_config(page_title="Average World Temperature", layout="centered", page_icon="🌡️")
st.title("Average World Temperature")

# df = pd.read_csv("data.txt")
cursor = connection.cursor()

cursor.execute("SELECT date FROM temperature")
dates = cursor.fetchall()
dates = [item[0] for item in dates]
print(dates)

cursor.execute("SELECT temperature FROM temperature")
temps = cursor.fetchall()
temps = [item[0] for item in temps]
print(temps)


figure = px.line(x=dates, y=temps, 
                 labels={"x":'date', "y":'temperature'})
st.plotly_chart(figure)
