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

