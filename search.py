import streamlit as st

def test():
    st.header("Search Engine")


    col1, col2 = st.columns([3,1])

    with col1:
        st.text_input("Geben Sie ein, wonach Sie suchen möchten:", placeholder="Type something...")
    with col2:
        if st.button("Suchen"):
            st.write(f"Suchergebnisse für: {query}")
