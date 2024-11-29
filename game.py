import streamlit as st

def test():
    st.header("Who am I?")

    # Display the logo at the top of the page


    option = st.selectbox(
    "How difficult should be the Game?",
    ("None", "Easy", "Medium", "Hard"),
    index=None,
    placeholder="Select a difficulty level...",
    )

    st.write("You selected:", option)

    #Indiz vor der ersten Frage. Wo?

    # Erste Selectbox mit Vorlagen
    question_template = st.selectbox(
        "Wählen Sie eine Vorlage für Ihre Frage:",
        ["", "Option 1: Fußpräferenz", "Option 2: Position", "Option 3: Alter"]
    )

    # Überprüfung, ob die erste Option gewählt wurde
    if question_template == "Option 1: Fußpräferenz":
        foot_preference = st.selectbox(
            "Wählen Sie die Fußpräferenz:",
            ["Linksfuss", "Rechtsfuss"]
        )
        st.write(f"Sie haben gewählt: {foot_preference}")

    elif question_template == "Option 2: Position":
        position = st.selectbox(
            "Wählen Sie eine Position:",
            ["Torwart", "Verteidiger", "Mittelfeldspieler", "Stürmer"]
        )
        st.write(f"Sie haben gewählt: {position}")

    elif question_template == "Option 3: Alter":
        age_group = st.selectbox(
            "Wählen Sie eine Altersgruppe:",
            ["Unter 20", "20-30", "Über 30"]
        )
        st.write(f"Sie haben gewählt: {age_group}")
