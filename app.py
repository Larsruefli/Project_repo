import streamlit as st
from Search_Engine import test

# Titel der Web-App
def test():    
    st.title("Who am I?")

    # Sidebar mit Navigationsoptionen
    st.sidebar.title("Navigation")
    option = st.sidebar.radio(
        "Wählen Sie eine Option:",
        ("Start", "Suchmaschine", "Spiel")
    )

    # Für jede Option in der Navigation Inhalte widergeben
    if option == "Start":
        st.header("Willkommen auf der Startseite!")
        st.write("Hier können allgemeine Informationen oder eine Einführung stehen.")

    elif option == "Suchmaschine":
        search_engine.app()
    elif option == "Spiel":
        st.header("Spielbereich")
        st.write("Hier könnte ein kleines Spiel eingebunden werden.")
        if st.button("Starte ein Spiel"):
            st.write("Spiel gestartet! (Hier könnte später ein Spiel eingebaut werden.)")
test()

