import streamlit as st
from adaptive_engine import (
    determine_level,
    get_adaptive_message,
    get_adaptive_hint,
)

# ---------------------------------------------------------
# Application Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Adaptive Learning Assistant",
    page_icon="🎓",
    layout="centered",
)

st.title("🎓 Adaptive Learning Assistant")

st.write(
    "This application adapts the learning experience based "
    "on your performance and interactions."
)

# ---------------------------------------------------------
# Question Data
# ---------------------------------------------------------

questions = [
    {
        "question": "What does AI stand for?",
        "options": [
            "Automated Information",
            "Artificial Intelligence",
            "Advanced Internet",
        ],
        "answer": "Artificial Intelligence",
        "explanation": (
            "AI stands for Artificial Intelligence, which refers "
            "to computer systems designed to perform tasks that "
            "normally require human intelligence."
        ),
    },
    {
        "question": "What is Machine Learning?",
        "options": [
            "A method that allows computers to learn from data",
            "A computer hardware component",
            "A type of Internet connection",
        ],
        "answer": "A method that allows computers to learn from data",
        "explanation": (
            "Machine learning enables computer systems to identify "
            "patterns and improve performance using data."
        ),
    },
    {
        "question": "What does HCI stand for?",
        "options": [
            "Human-Computer Interaction",
            "High Computing Intelligence",
            "Human Communication Internet",
        ],
        "answer": "Human-Computer Interaction",
        "explanation": (
            "HCI stands for Human-Computer Interaction and focuses "
            "on how people interact with computer systems."
        ),
    },
    {
        "question": "What is an adaptive user interface?",
        "options": [
            "An interface that changes based on user behavior",
            "An interface that never changes",
            "A computer operating system",
        ],
        "answer": "An interface that changes based on user behavior",
        "explanation": (
            "An adaptive user interface modifies aspects of the "
            "interaction based on user behavior, performance, "
            "preferences, or context."
        ),
    },
    {
        "question": "How can AI improve user experience?",
        "options": [
            "By providing personalized experiences",
            "By preventing users from interacting with applications",
            "By making every interface identical",
        ],
        "answer": "By providing personalized experiences",
        "explanation": (
            "AI can improve user experience through personalization, "
            "recommendations, adaptive assistance, and other "
            "context-sensitive features."
        ),
    },
]

# ---------------------------------------------------------
# Session State
# Stores user progress while Streamlit reruns the application
# ---------------------------------------------------------

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = 0

if "answered_questions" not in st.session_state:
    st.session_state.answered_questions = 0

if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False

if "last_correct" not in st.session_state:
    st.session_state.last_correct = False

# ---------------------------------------------------------
# Topic Selection
# ---------------------------------------------------------

topic = st.selectbox(
    "Select a learning topic:",
    [
        "Artificial Intelligence & HCI",
        "Adaptive User Interfaces",
        "AI and User Experience",
    ],
)

st.caption(f"Current topic: {topic}")

# ---------------------------------------------------------
# Current Performance
# ---------------------------------------------------------

if st.session_state.answered_questions == 0:
    current_score = 0
else:
    current_score = (
        st.session_state.correct_answers
        / st.session_state.answered_questions
    ) * 100

# Determine the adaptive level only after the user
# has answered at least one question.
if st.session_state.answered_questions == 0:
    current_level = "Not Assessed"
else:
    current_level = determine_level(current_score)

st.subheader("Current Learning Profile")

col1, col2 = st.columns(2)

with col1:
    if st.session_state.answered_questions == 0:
        st.metric("Current Score", "Not Available")
    else:
        st.metric("Current Score", f"{current_score:.0f}%")

with col2:
    st.metric("Adaptive Level", current_level)

# ---------------------------------------------------------
# Adaptive Assistance
# ---------------------------------------------------------

if current_level == "Not Assessed":
    st.info("📝 Assessment Not Started")
    st.write(
        "Answer the questions below so the system can "
        "adapt the learning experience to your performance."
    )

elif current_level == "Beginner":
    st.warning("🌱 Beginner Mode")
    st.write(
        "The interface is providing additional explanations "
        "and detailed hints."
    )

elif current_level == "Intermediate":
    st.info("📘 Intermediate Mode")
    st.write(
        "The interface is providing moderate learning assistance."
    )

else:
    st.success("🚀 Advanced Mode")
    st.write(
        "The interface has reduced assistance and recommends "
        "more challenging material."
    )

# ---------------------------------------------------------
# Progress
# ---------------------------------------------------------

progress = st.session_state.question_index / len(questions)

st.progress(progress)

st.caption(
    f"Question {min(st.session_state.question_index + 1, len(questions))} "
    f"of {len(questions)}"
)

# ---------------------------------------------------------
# Quiz
# ---------------------------------------------------------

if st.session_state.question_index < len(questions):

    current_question = questions[st.session_state.question_index]

    st.divider()

    st.subheader(
        f"Question {st.session_state.question_index + 1}"
    )

    st.write(current_question["question"])

    # Adaptive hint changes according to user performance
    with st.expander("💡 Adaptive Hint"):
        if current_level == "Not Assessed":
            st.write(
                "Complete the first question to begin receiving "
                "personalized hints."
                )
        else:
            st.write(get_adaptive_hint(current_level))

    selected_answer = st.radio(
        "Choose your answer:",
        current_question["options"],
        index=None,
        key=f"question_{st.session_state.question_index}",
    )

    if not st.session_state.show_feedback:

        if st.button("Submit Answer", type="primary"):

            if selected_answer is None:
                st.warning("Please select an answer before submitting.")

            else:
                st.session_state.answered_questions += 1

                if selected_answer == current_question["answer"]:
                    st.session_state.correct_answers += 1
                    st.session_state.last_correct = True
                else:
                    st.session_state.last_correct = False

                st.session_state.show_feedback = True
                st.rerun()

    else:

        if st.session_state.last_correct:
            st.success("Correct! Great job.")
        else:
            st.error("That answer is incorrect.")

        # Beginners receive more detailed explanations
        if current_level == "Beginner":
            st.info(
                "Additional Explanation: "
                + current_question["explanation"]
            )

        elif current_level == "Intermediate":
            st.info(
                "Explanation: "
                + current_question["explanation"]
            )

        else:
            st.success(
                "You demonstrated strong understanding of this concept."
            )

        st.write(get_adaptive_message(current_level))

        if st.button("Next Question"):

            st.session_state.question_index += 1
            st.session_state.show_feedback = False
            st.rerun()

# ---------------------------------------------------------
# Final Results
# ---------------------------------------------------------

else:

    final_score = (
        st.session_state.correct_answers / len(questions)
    ) * 100

    final_level = determine_level(final_score)

    st.progress(1.0)

    st.divider()

    st.header("🎯 Learning Assessment Complete")

    st.metric("Final Score", f"{final_score:.0f}%")

    if final_level == "Beginner":
        st.warning("🌱 Final Adaptive Level: Beginner")
        st.write(
            "The system recommends additional explanations, "
            "guided practice, and beginner-level learning materials."
        )

    elif final_level == "Intermediate":
        st.info("📘 Final Adaptive Level: Intermediate")
        st.write(
            "The system recommends moderate-level learning "
            "activities and continued practice."
        )

    else:
        st.success("🚀 Final Adaptive Level: Advanced")
        st.write(
            "The system recommends advanced learning materials "
            "and more challenging activities."
        )

    st.write(get_adaptive_message(final_level))

    if st.button("🔄 Restart Learning Session"):

        st.session_state.question_index = 0
        st.session_state.correct_answers = 0
        st.session_state.answered_questions = 0
        st.session_state.show_feedback = False
        st.session_state.last_correct = False

        st.rerun()