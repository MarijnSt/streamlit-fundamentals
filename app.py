import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Hello World")

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.write(f"Counter: {st.session_state.counter}")

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

st.write("Streamlit has a bunch of widgets to interact with the user:")

if st.button("Say hello"):
    st.write("Why hello there")

x = st.slider("x")
st.write(x, "squared is", x * x)

st.text_input("Your name", key="name")
if st.session_state.name:
    st.write(f"Hello {st.session_state.name}")

if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['a', 'b', 'c']
    )
    chart_data


df_selection = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})

option = st.selectbox(
    "Which number do you like best?",
    df_selection["first column"]
)

st.write("You selected:", option)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

add_slider = st.sidebar.slider(
    "Select a range of values",
    0, 100, (25, 75)
)

# Use column layout
left_column, right_column = st.columns(2)

left_column.button("Press me!")

with right_column:
    chosen_house = st.radio(
        "Sorting Hat",
        ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")
    )
    st.write(f"You chose {chosen_house} house!")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

st.write("Done!")
