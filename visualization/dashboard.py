import streamlit as st
import pandas as pd

data = pd.DataFrame({"Trend": ["#AI", "#DataScience", "#Tech"], "Frequency": [120, 95, 80]})

st.title("📊 Social Media Trend Analysis Dashboard")
st.bar_chart(data.set_index("Trend"))
