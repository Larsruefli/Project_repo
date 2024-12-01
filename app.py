import streamlit as st
import start
import search
import game


# Sidebar mit Navigationsoptionen
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Wählen Sie eine Option:",
    ("Start", "Search", "Gane")
)

# Für jede Option in der Navigation Inhalte widergeben
if option == "Start":
    start.test()
elif option == "Search":
    search.test()
elif option == "Game":
    game.test()

