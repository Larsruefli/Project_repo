def return_even(x): 
    return [i for i in x if i%2 ==0]
import streamlit as st

#gehört in ein neues Dokument, welches mit Streamlit verbunden ist
from Feature_01 import return_even
from Feature_02 import return_odd

original_list = [i for i in range(10)]

even_list = return_even(original_list)

odd_list = return_odd(original_list)

st.write("we connected everything")

st.write(even_list)

st.write(odd_list)

