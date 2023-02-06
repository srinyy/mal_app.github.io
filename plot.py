import streamlit as st
import pandas as pd

st.title("Enter your number")
name = st.text_input("Enter your name")
st.write(f"Hello {name}")

st.sidebar("Home":home, "About":about)
x = st.slider ("Selectr an Integer x", 0,10,1)
y = st.slider("Selectr an Integer y", 0,10,1)
df = pd.DataFrame( {"x": [x],"y": [y],"x + y": [x +y]}, index= ["addition row"])


#df = pd.DataFrame ({“x”: [x], “y”: [y] , “x + y”: [x + y]}, index = [“addition row”])
st.write(df)