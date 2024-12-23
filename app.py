import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})

st.write("Here's our first attempt at using data to create a table:")
st.table(df)

st.write("Let's make a table with random numbers using numpy:")
np_df = np.random.randn(10, 10)
st.dataframe(np_df)

st.write("We can use Pandas Styler object to highlight some elements in the table:")
df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=("col %d" % i for i in range(20))
)
st.dataframe(df.style.highlight_max(axis=0))

st.write("Let's generate a line chart with st.line_chart:")

line_chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(line_chart_data)


st.write("Plot a map with st.map:")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)