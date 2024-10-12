import streamlit as st
import pandas as pd


st.write("# Learning Text Classification using Median")
column_names = ["id", "TITLE", "URL", "PUBLISHER", "CATEGORY", "STORY", "HOSTNAME", "TIMESTAMP"]
data_df = pd.read_csv("./data/newsCorpora.csv", header=None, delimiter="\t", index_col=False, names=column_names)


data_df["TIMESTAMP"] = pd.to_datetime(data_df["TIMESTAMP"])
print(data_df.dtypes)
data_df["MONTHS"] = data_df["TIMESTAMP"].apply(lambda date: date.month)
print(data_df)

st.write(data_df)
