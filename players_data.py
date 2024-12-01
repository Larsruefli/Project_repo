players = [
    {"Name": "Lionel Messi", "Position": "Forward", "Team": "Inter Miami"}
     ]



# Ask Question Button
with col3:
    # Ask Question Button
    if st.button("Ask Question"):
        if selected:
            full_question = question_template.replace("...", selected)
            st.session_state.questions.append(full_question)

            # Simulate correct input
            is_correct = st.radio(f"Was the answer for '{full_question}' correct?", ["Yes", "No"])
            st.session_state.correctness.append("Yes" if is_correct == "Yes" else "No")
        else:
            st.warning("Please provide additional input to complete the question.")
# Display all questions asked so far with Yes or No answer
    st.subheader("Questions Asked:")
    for i, (question, is_correct) in enumerate(st.session_state.questions, start=1):
        status = f'<span style="color:green;">Yes</span>' if is_correct else f'<span style="color:red;">No</span>'
        st.markdown(f"{i}. {question} - {status}", unsafe_allow_html=True)


   


# Two Columns for the Gussing Input of the User and the Button Guess
    col1, col2 = st.columns([3,1], vertical_alignment="bottom")

    with col1: 
        user_input = st.text_input("Enter your input here:", label_visibility="collapsed", placeholder="Type Player here")

    with col2:
        button_clicked = st.button("Guess")
# When Button clicked it shows either a success Input with a picture of the Player or an error message
        if button_clicked:
            if user_input in players_data:
            # Spieler gefunden
                st.success("🎉 You guessed the player correctly!")
            # Zeige das Bild in der Mitte
                st.image(players_data[user_input], caption=f"{user_input}", width=200)
            else:
            # Spieler nicht gefunden
                st.error("❌ That's the wrong player. Try again!")