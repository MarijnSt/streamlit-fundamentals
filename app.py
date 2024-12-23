import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})

st.write("Here's our first attempt at using data to create a table:")
st.dataframe(df)

st.write("Let's make a table with random numbers using numpy:")
np_df = np.random.randn(10, 10)
st.dataframe(np_df)

st.write("We can use Pandas Styler object to highlight some elements in the table:")
df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=("col %d" % i for i in range(20))
)
st.dataframe(df.style.highlight_max(axis=0))
