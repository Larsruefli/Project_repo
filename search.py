import streamlit as st
from players_data import players

def test():
    st.header("Search Engine")


    col1, col2 = st.columns([3,1])

    with col1:
        user_input = st.text_input ("Geben Sie ein, wonach Sie suchen möchten:", label_visibility="collapsed", placeholder="Type something...")
    with col2:
        search_button = st.button("Search")
        
    if search_button:
            st.write(f"Suchergebnisse für: {user_input}")

    # Calling results from a players llist // Attention on what should be displayed and how (in line 22): Name, ...!!!
    if user_input:
        results = [item for item in players if user_input.lower() in item["Name"].lower()]
        if results:
             for result in results:
                  st.write(f"Name: {result['Name']}")
        else:
            st.write("No results found")

