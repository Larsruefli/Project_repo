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

    