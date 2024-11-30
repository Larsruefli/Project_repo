import streamlit as st

def test():
    st.header("Who am I?")

    # Display the logo at the top of the page


    option = st.selectbox(
    "How difficult should the Game be?",
    ("None", "Easy", "Medium", "Hard"),
    index=None,
    placeholder="Select a difficulty level...",
    )

    st.write("You selected:", option)

    #Indiz vor der ersten Frage. Wo?

    # Erste Selectbox mit Vorlagen
    question_template = st.selectbox(
        "Wählen Sie eine Vorlage für Ihre Frage:",
        ["", "Option 1: I am currently playing for ...(club)", "Option 2: I play in ... (league)", "Option 3: I am from ...(nationality)", "Option 4: I used to play for ...(club)", "Option 5: I am a ... winner", "Option 6: I am older than ...(age)", "Option 7: I am younger than ...(age)", "Option 8: I play as ...(position)", "Option 9: I wear the shirt number ... at my current club (shirt number)", "Option 10: I am taller than ...(height)", "Option 11: I am shorter than ...(height)"]
    )

    # Überprüfung, ob die erste Option gewählt wurde
    if question_template == "I am currently playing for ...(club)":
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
