import streamlit as st
import random

# Add custom CSS for a pink aesthetic background
st.markdown("""
    <style>
        body {
            background-color: #fcd2f4;  /* Light pink background */
            color: #5c2d92;  /* Purple text color */
        }
        .css-18e3th9 {
            background-color: #fcd2f4 !important;  /* Ensure sidebar background matches */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #5c2d92;  /* Purple headers */
        }
        .stButton>button {
            background-color: #ff80ab;  /* Pink button */
            color: white;
            border-radius: 12px;
            border: none;
        }
        .stTextInput>div>input {
            border-radius: 12px;
            border: 2px solid #ff80ab;
        }
        .stTextInput>div>input:focus {
            border-color: #ff4081;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("✨ End of 2024 Celebration for My Bestie ✨")
st.markdown("Welcome, bestie! Let's celebrate the end of 2024 with laughter and joy. 💖")

# Aesthetic image
st.image("https://source.unsplash.com/500x300/?aesthetic,coquette", caption="Aesthetic vibes for us! 🌸", use_column_width=True)

# Section: Fun Messages for Bestie
st.subheader("Fun Messages for My Bestie 💌")
fun_messages = [
    "May you always be the star in the sky, not just in my stories 😜🌟",
    "We’re probably best friends because we both love drama, but also hate being involved in it 😂🎭",
    "Always stunning and amazing, here's to laughing more together and dealing with less drama in 2024 🙆‍♀️✨",
    "If we’ve survived together until the end of the year, we can face anything in 2024! 💪💖",
    "New year, new energy, but still besties for life! 💫💖"
]

st.write(random.choice(fun_messages))

# Section: Coquette Quotes
st.subheader("Coquette Quotes for the New Year 💋")
coquette_quotes = [
    "I hope your 2024 is as beautiful as you are. 😘",
    "Don't let anyone dull your sparkle. Keep shining in 2024! ✨",
    "Life's too short to be serious. Let's laugh our way through 2024! 🥂",
    "You and I make the perfect duo—let's make more memories in 2024! 💕",
    "Keep being the gorgeous queen you are, darling. 2024 is your year! 👑"
]

st.write(f"💖 **{random.choice(coquette_quotes)}** 💖")

# Section: Aesthetic Moodboard
st.subheader("Aesthetic Moodboard for the New Year 🎨")
st.image("https://source.unsplash.com/500x300/?coquette,aesthetic,pastel", caption="Vibes for us in 2024! 🌸✨", use_column_width=True)

# Section: Button for suggestions and wishes for 2024
st.subheader("Suggestions and Wishes for 2024 🌈")
if st.button("Leave a suggestion for your bestie in 2024!"):
    suggestion = st.text_input("Write a funny wish or suggestion for your bestie in the upcoming year:")
    if suggestion:
        st.write(f"💌 **Your wish for your bestie:** {suggestion} 💖")

# Footer with emojis and closing message
st.markdown("---")
st.markdown("Thank you for celebrating 2024 with us! May the coming year be even brighter, happier, and more joyful! 💖✨")
st.markdown("Goodbye 2024, and hello 2025! 🎉💋")
