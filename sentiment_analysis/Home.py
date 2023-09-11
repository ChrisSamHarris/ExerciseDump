import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
import glob

st.set_page_config(page_title="Diary analysis", layout="centered", page_icon="📔")

# glob returns a list of the pathnames matching our specified pattern:
files = sorted(glob.glob("diary/*.txt"))
print(files)

analyse = SentimentIntensityAnalyzer()
def sentiment_analysis(list, sentiment):
    if sentiment not in ["pos", "neg"]:
        raise ValueError("Sentiment must equal value 'pos' or 'neg'")
    values = {}
    for i in list:
        # i_tidy = i[8:-4]
        i_tidy = i.strip(".txt").strip("diary/")
        with open(i, "r") as content:
            content = content.read()
        score = analyse.polarity_scores(content)
        values[i_tidy] = score[sentiment]

    return values

st.title("Diary analysis")

st.header("Positivity")
positive_values = sentiment_analysis(files, sentiment="pos")
print(positive_values)
figure = px.line(x=positive_values.keys(), y=positive_values.values(), labels={"x":"Date", "y":"Positivity"})
st.plotly_chart(figure)

st.header("Negativity")
negative_values = sentiment_analysis(files, sentiment="neg")
figure = px.line(x=negative_values.keys(), y=negative_values.values(), labels={"x":"Date", "y":"Positivity"})
st.plotly_chart(figure)