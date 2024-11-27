import streamlit as st

def test():
    st.header("Search Engine")


    col1, col2 = st.columns([3,1])

    with col1:
        user_input = st.text_input ("Geben Sie ein, wonach Sie suchen möchten:", label_visibility="collapsed", placeholder="Type something...")
    with col2:
        search_button = st.button("Search")
        
    if search_button:
            st.write(f"Suchergebnisse für: {user_input}")
