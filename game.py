import streamlit as st

def test():
    st.header("Who am I?")

    # Display the logo at the top of the page
    st.image("logo.png", width = 100)

    if "questions" not in st.session_state:
        st.session_state.questions = []


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

   

    with col1:
        question_template = st.selectbox(
            "Choose a question:",
            ["I am currently playing for ...", "I play in ...", "I am from ...", "I used to play for ...", "I am a ... winner", "I am older than ...", "I am younger than ...", "I play as ...", "I wear the shirt number ... at my current club", "I am taller than ...", "I am shorter than ..."]
        )

    # Weiterführende Auswahl von Kriterien durch if Funktion
    with col2:
        selected = None
        if question_template == "I am currently playing for ...":
            current_club = st.selectbox(
                "Choose my club:",
                ["Real Madrid", "Arsenal", "Liverpool"] #!!!!!
            )
            selected = current_club
            
        
        elif question_template == "I play in ...":
            league = st.selectbox(
                "Choose my league:",
                ["Premier League", "Bundesliga", "Eredivise", "LaLiga", "Serie A", "Ligue 1", "Liga Portugal", "Süper Lig", "Jupiler Pro League"]
            )
            selected = league

        elif question_template == "I am from ...":
            nationality = st.selectbox(
                "Choose my country:",
                ["Germany", "Switzerland", "Spain"]
            )
            selected = nationality


        elif question_template == "I used to play for ...":
            past_club = st.selectbox(
                "Choose a club:",
                ["Real Mardid", "Arsenal", "Liverpool"]
            )
            selected = past_club

        elif question_template == "I am a ... winner":
            achievements = st.selectbox(
                "Choose my achievements:",
                ["Top 5 league", "Champions League", "World Cup", "European championship", "Europa League"]
            )
            selected = achievements

        elif question_template == "I am older than ...":
            age = st.slider("",
                min_value=15, max_value=45, value=30, step=1
            )
            selected = f"older than {age}"

        elif question_template == "I am younger than ...":
            age = st.slider("",
                min_value=15, max_value=45, value=30, step=1
            )
            selected = f"younger than {age}"

        elif question_template == "I play as ...":
            position = st.selectbox(
                "Choose a position:",
                ["GK", "Defender", "Midfielder", "Striker"]
            )
            selected = position

        elif question_template == "I wear the shirt number ... at my current club":
            shirt_number = st.selectbox(
                "Write a shirt number:",
                ["Unter 20", "20-30", "Über 30"]
            )
            selected = shirt_number

        elif question_template == "I am taller than ...":
            height = st.slider(
                "",
                min_value=150, max_value=220, value=185, step=1
            )
            selected = f"taller than {height} cm"

        elif question_template == "I am shorter than ...":
            height = st.slider(
                "",
                min_value=150, max_value=220, value=185, step=1
            )
            selected = f"shorter than {height} cm"

 # Ask Question Button
    with col3:
        if st.button("Ask Question"):
            # Add the question to the session state list
            if selected:
                full_question = question_template.replace("...", selected)
                st.session_state.questions.append(full_question)
            else:
                st.warning("Please provide an additional input to complete the question.")

    # Display all questions asked so far
    st.subheader("Questions Asked:")
    for i, question in enumerate(st.session_state.questions, start=1):
        st.write(f"{i}. {question}")
        





    
        
 