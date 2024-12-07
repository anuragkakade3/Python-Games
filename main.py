import streamlit as st
import json
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Gaming-Dashboard', page_icon=':game_die:', initial_sidebar_state='collapsed', layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(r"style.css")

# ---- LOAD ASSETS ----
img_contact_form = Image.open(r"Golf Game.png")
img_snake_form = Image.open(r"Game.png")
img_chess_form = Image.open(r"Chess.png")
img_snakegame_form = Image.open(r"Snake Game.png")
img_word_form = Image.open(r"Word Game.png")

# --- Game Links ---
chess_link = "https://pmp-p.github.io/pygame-pychess-wasm/index.html"
Alien_Dimension_link = "https://pmp-p.github.io/pygame-alien-dimension-wasm/"
Golf_game_Download_link = "https://mega.nz/folder/rw8WQDAY#ia_GcCq5Cc7BSo1HL3HHgA"
snake_game_Download_link = "https://mega.nz/file/DlkiyBBR#4iAk9cm3e4HB2WLoBEgC4619FO6my4qHesse1txkRKc"
word_game_Downlode_game_link = "https://mega.nz/file/noF0RS7I#I6oAu7eJh7lPxZjfNvI5xkdLgPmDkqHzsMD85_EsQuk"

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Welcome to the Playground")
    st.title("Hello!! Gamers :game_die:")
    st.write("I'm a Gamer. Not because I don't have a life. But because I choose to have many.")

# ---- WHAT I DO ----
with st.container():
    st.write("----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(":warning: RULES :warning:")
        st.write("#")
        st.write(
            """
            1. Follow the game rules: Follow the rules of the game and play fairly, avoid using cheats or hacks.\n
            2. Protect your account: Keep your account and password secure, and avoid sharing your personal information with other players.\n
            3. Avoid cheating: Do not use third-party software or bots to gain an unfair advantage over other players.\n
            4. Play responsibly: Play the game in moderation and avoid excessive gaming that can negatively impact your health and well-being.\n
            5. Do not spam or advertise: Avoid spamming or advertising in the game, and only use the chat function for game-related communication.\n
            """
        )
    with right_column:
        with open(r'gaming.json') as source:
            gaming = json.load(source)
        st_lottie(gaming, height=400)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("🎳 Our Games 🎳 ")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_snake_form)
    with text_column:
        st.subheader("Alien-Dimension")
        st.write(
            """
            Alien-Dimension is an action-packed video game set in a hostile alien dimension.
            As a space explorer, your mission is to navigate treacherous landscapes, defeat powerful alien creatures,
            and uncover hidden secrets to progress through the levels.
            """
        )
        st.markdown(f'<a href={Alien_Dimension_link} class="button">👉 Play Game</a>', unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Golf Game")
        st.write(
            """
            The Golf Game is a virtual sports game that lets players experience
            the thrill of playing golf in stunningly realistic environments.
            """
        )
        st.markdown(f'<a href={Golf_game_Download_link} class="button">👉 Download Game</a>', unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_snakegame_form)
    with text_column:
        st.subheader("Snake Game")
        st.write(
            """
            The Golf Game is a virtual sports game that lets players experience
            the thrill of playing golf in stunningly realistic environments.
            """
        )
        st.markdown(f'<a href={snake_game_Download_link} class="button">👉 Download Game</a>', unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_chess_form)
    with text_column:
        st.subheader("Chess Game")
        st.write(
            """
            Chess is a classic board game that has been enjoyed for centuries,
            and now it's available as a virtual game for players to enjoy online.
            The game is played on a board with 64 squares, and each player controls 16
            pieces that move across the board in different ways.
            """
        )
        st.markdown(f'<a href={chess_link} class="button">👉 Play Game</a>', unsafe_allow_html=True)

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_word_form)
    with text_column:
        st.subheader("Word Game")
        st.write(
            """
            Chess is a classic board game that has been enjoyed for centuries,
            and now it's available as a virtual game for players to enjoy online.
            The game is played on a board with 64 squares, and each player controls 16
            pieces that move across the board in different ways.
            """
        )
        st.markdown(f'<a href={word_game_Downlode_game_link} class="button">👉 Download Game</a>', unsafe_allow_html=True)

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("📩 Get In Touch With Us!")
    st.write("##")

    # Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/anurag.kakade20@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
