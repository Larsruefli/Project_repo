import streamlit as st


# Titel der Web-App
st.title("Who am I?")

# Sidebar mit Navigationsoptionen
st.sidebar.title("Navigation")
option = st.sidebar.radio(
    "Wählen Sie eine Option:",
    ("Start", "Suchmaschine", "Spiel")
)

# Inhalte je nach gewählter Option
if option == "Start":
    st.header("Willkommen auf der Startseite!")
    st.write("Hier können allgemeine Informationen oder eine Einführung stehen.")

elif option == "Suchmaschine":
    st.header("Suchmaschine")
    st.write("Hier könnte eine Suchmaschine implementiert werden.")
    query = st.text_input("Geben Sie ein, wonach Sie suchen möchten:")
    if st.button("Suchen"):
        st.write(f"Suchergebnisse für: {query}")

elif option == "Spiel":
    st.header("Spielbereich")
    st.write("Hier könnte ein kleines Spiel eingebunden werden.")
    if st.button("Starte ein Spiel"):
        st.write("Spiel gestartet! (Hier könnte später ein Spiel eingebaut werden.)")
