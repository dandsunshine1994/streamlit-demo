import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Streamlit Cloud Demo", layout="wide")
st.title("Hello Streamlit Cloud 👋")

df = pd.DataFrame({"A":[1,3,2,4], "B":[4,2,3,1]})
st.dataframe(df)

fig = go.Figure()
for c in df.columns:
    fig.add_scatter(x=df.index, y=df[c], mode="lines", name=c)
st.plotly_chart(fig, use_container_width=True)

st.success("部署成功后，你会在 URL 上看到这个页面。")
