import streamlit as st

def test():
    st.header("Suchmaschine")
    st.write("Hier könnte eine Suchmaschine implementiert werden.")
    query = st.text_input("Geben Sie ein, wonach Sie suchen möchten:", key="query_input")
    if st.button("Suchen", key="search_button"):
        st.write(f"Suchergebnisse für: {query}")
