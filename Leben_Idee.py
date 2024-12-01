import streamlit as st

# Beispiel-Datensatz mit Spielernamen und zugehörigen Bildern
players_data = {
    "Lionel Messi": "messi.jpg",
    "Cristiano Ronaldo": "ronaldo.jpg",
    "Neymar Jr": "neymar.jpg",
}

# Initialisiere Session-State für Leben und erratene Spieler
if "lives" not in st.session_state:
    st.session_state.lives = 3  # Spieler startet mit 3 Leben
if "guessed_players" not in st.session_state:
    st.session_state.guessed_players = []

def main():
    st.header("Guess the Player!")

    # Obere rechte Ecke: Lebensanzeige
    with st.sidebar:
        st.markdown("### Lives Remaining:")
        lives_display = "⚽ " * st.session_state.lives + "❌ " * (3 - st.session_state.lives)
        st.write(lives_display)

    # Layout: Input-Feld und Button
    col1, col2 = st.columns([3, 1])  # Input-Feld größer als der Button
    with col1:
        user_input = st.text_input("Enter the player's name:", label_visibility="collapsed", placeholder="Type a player's name...")
    with col2:
        button_clicked = st.button("Submit")

    # Überprüfung bei Button-Klick
    if button_clicked:
        if st.session_state.lives > 0:
            if user_input in players_data and user_input not in st.session_state.guessed_players:
                # Spieler korrekt erraten
                st.success("🎉 You guessed the player correctly!")
                st.image(players_data[user_input], caption=f"{user_input}", width=200)
                st.session_state.guessed_players.append(user_input)
            elif user_input in st.session_state.guessed_players:
                st.warning("You already guessed this player!")
            else:
                # Spieler nicht korrekt erraten
                st.session_state.lives -= 1
                if st.session_state.lives > 0:
                    st.error(f"❌ Wrong guess! You have {st.session_state.lives} lives left.")
                else:
                    st.error("❌ Game over! You've used up all your lives.")
        else:
            st.error("❌ No lives left! Restart the app to try again.")
