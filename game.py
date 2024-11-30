import streamlit as st

def test():
    st.header("Who am I?")

    # Display the logo at the top of the page
    st.image("logo.png", width = 100)

    option = st.selectbox(
    "How difficult should the Game be?",
    ("None", "Easy", "Medium", "Hard"),
    index=None,
    placeholder="Select a difficulty level...",
    )

    st.write("You selected:", option)

    

    #Indiz vor der ersten Frage. Wo?

    # Erste Selectbox mit Fragen

    col1, col2, col3 = st.columns([2,2,1], vertical_alignment="bottom")

    container = st.container(border= True)

    with col1:
        question_template = st.selectbox(
            "Choose a question:",
            ["I am currently playing for ...(club)", "I play in ... (league)", "I am from ...(nationality)", "I used to play for ...(club)", "I am a ... winner (achievement)", "I am older than ...(age)", "I am younger than ...(age)", "I play as ...(position)", "I wear the shirt number ... at my current club (shirt number)", "I am taller than ...(height)", "I am shorter than ...(height)"]
        )

    # Weiterführende Auswahl von Kriterien durch if Funktion
    with col2:
        selected = None
        if question_template == "I am currently playing for ...(club)":
            current_club = st.selectbox(
                "Choose my club:",
                ["Real Madrid", "Arsenal", "Liverpool"] #!!!!!
            )
            selected = current_club
            
            

        elif question_template == "I play in ... (league)":
            league = st.selectbox(
                "Choose my league:",
                ["Premier League", "Bundesliga", "Eredivise", "LaLiga", "Serie A", "Ligue 1", "Liga Portugal", "Süper Lig", "Jupiler Pro League"]
            )
            selected = league

        elif question_template == "I am from ...(nationality)":
            nationality = st.selectbox(
                "Choose my country:",
                ["Germany", "Switzerland", "Spain"]
            )

        elif question_template == "I used to play for ...(club)":
            past_club = st.selectbox(
                "Choose a club:",
                ["Real Mardid", "Arsenal", "Liverpool"]
            )

        elif question_template == "I am a ... winner (achievement)":
            achievements = st.selectbox(
                "Choose my achievements:",
                ["Top 5 league", "Champions League", "World Cup", "European championship", "Europa League"]
            )

        elif question_template == "I am older than ...(age)":
            age = st.slider("",
                min_value=15, max_value=45, value=30, step=1
            )

        elif question_template == "I am younger than ...(age)":
            age = st.slider("",
                min_value=15, max_value=45, value=30, step=1
            )

        elif question_template == "I play as ...(position)":
            position = st.selectbox(
                "Choose a position:",
                ["GK", "Defender", "Midfielder", "Striker"]
            )

        elif question_template == "I wear the shirt number ... at my current club (shirt number)":
            shirt_number = st.selectbox(
                "Write a shirt number:",
                ["Unter 20", "20-30", "Über 30"]
            )

        elif question_template == "I am taller than ...(height)":
            height = st.slider(
                "Select my height:",
                min_value=1.50, max_value=2.20, value=1.85, step=0.01
            )
            selected = f"taller than {height} cm"

        elif question_template == "I am shorter than ...(height)":
            height = st.selectbox(
                "Select my height:",
                min_value=1.50, max_value=2.20, value=1.85, step=0.01
            )

    with col3:
        if st.button("Ask Question"):
            with container:
                if selected:
                    st.write(f"{question_template.replace('...', selected)}")
                else:
                    st.warning("Please provide an additional input to complete the question.")
        





    
        
 