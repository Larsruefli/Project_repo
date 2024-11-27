import streamlit as st

def test():
    # Titel der Web-App
    st.title("Who am I?")

    # Sidebar mit Navigationsoptionen
    st.sidebar.title("Navigation")
    option = st.sidebar.radio(
        "Wählen Sie eine Option:",
        ("Start", "Suchmaschine", "Spiel")
    )
