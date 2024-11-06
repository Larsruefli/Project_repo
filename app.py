import streamlit as st
from Feature_01 import return_even

original_list = [i for i in range(10)]

even_list = return_even(original_list)


st.write("we connected everything")

st.header("My header")

st.write(even_list)
