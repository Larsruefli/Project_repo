import streamlit as st

def test():
    st.header("Search Engine")
    st.write("Hier könnte eine Suchmaschine implementiert werden.")
    query = st.text_input("Geben Sie ein, wonach Sie suchen möchten:")
    if st.button("Suchen"):
        st.write(f"Suchergebnisse für: {query}")
        