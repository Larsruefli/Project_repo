import streamlit as st

def test():
    st.header("Search Engine")
    
    query = st.text_input("Geben Sie ein, wonach Sie suchen möchten:")
    if st.button("Suchen"):
        st.write(f"Suchergebnisse für: {query}")
