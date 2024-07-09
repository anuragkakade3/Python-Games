import streamlit as st
import streamlit_authenticator as stauth
from dependancies import sign_up, fetch_users
import json
import time

import requests
import streamlit as st
from PIL import Image
import streamlit_authenticator as stauth
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Gaming-Dashboard', page_icon=':game_die:', initial_sidebar_state='collapsed',layout="wide")

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            
local_css(r"style.css")



try:
    users = fetch_users()
    emails = []
    usernames = []
    passwords = []
            
    
    for user in users:
        emails.append(user['key'])
        usernames.append(user['username'])
        passwords.append(user['password'])

    credentials = {'usernames': {}}
    for index in range(len(emails)):
        credentials['usernames'][usernames[index]] = {'name': emails[index], 'password': passwords[index]}

    Authenticator = stauth.Authenticate(credentials, cookie_name='Streamlit', key='abcdef', cookie_expiry_days=4)

    email, authentication_status, username = Authenticator.login(':green[Login]', 'main')

    info, info1 = st.columns(2)

    if not authentication_status:
        sign_up()

    if username:
        if username in usernames:
            if authentication_status:
                # let User see app
                st.sidebar.subheader(f'Welcome {username}')
                Authenticator.logout('Log Out', 'sidebar')
                                    
                # ---- LOAD ASSETS ----
                img_contact_form = Image.open(r"Golf Game.png")
                img_snake_form = Image.open(r"Game.png")
                img_chess_form = Image.open(r"Chess.png")
                img_snakegame_form = Image.open(r"Snake Game.png")
                img_word_form= Image.open(r"Word Game.png")

                # --- Game Links ---
                chess_link= "https://pmp-p.github.io/pygame-pychess-wasm/index.html"
                Alien_Dimension_link= "https://pmp-p.github.io/pygame-alien-dimension-wasm/"
                Golf_game_Download_link= "https://mega.nz/file/TtMX1RoA#0zM4OOvFqsZ_3qj_LZJj4cz0hm0a3yqsvbiYPN4XoJc"
                snake_game_Download_link = "https://mega.nz/file/a5EzkagA#nE_o0ezwmewZNWB6Wj1rNOWeqgZeM07v8bArp1FlJzI"
                word_game_Downlode_game_link = "https://mega.nz/file/Xg932biI#JW7Eza9JzOps7kj0u4CJ00mjmTUXI1GZs-HnLim8Vi0"

                # ---- HEADER SECTION ----
                with st.container():
                    st.subheader("Welcome to the Playground")
                    st.title("Hello!! Gamers :game_die:")
                    st.write(
                        "I'm a Gamer. Not because I don't have a life. But because I choose to have many."
                            )
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
                    
                        """)
                with right_column:
                    with open(r'gaming.json') as source:
                        gaming=json.load(source)
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
                
                    st.markdown(
                        f'<a href={Alien_Dimension_link} class="button">👉 Play Game</a>',
                        unsafe_allow_html=True,
                    )

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
                    
                    st.markdown(
                        f'<a href={Golf_game_Download_link} class="button">👉 Download Game</a>',
                        unsafe_allow_html=True,
                    )
                
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
                    
                    st.markdown(
                        f'<a href={snake_game_Download_link} class="button">👉 Download Game</a>',
                        unsafe_allow_html=True,
                    )
                    
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
                    st.markdown(
                        f'<a href={chess_link} class="button">👉 Play Game</a>',
                        unsafe_allow_html=True,
                    )
                    
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
                    st.markdown(
                        f'<a href={word_game_Downlode_game_link} class="button">👉 Download Game</a>',
                        unsafe_allow_html=True,
                    )
                    
                # ---- CONTACT ----
                with st.container():
                    st.write("---")
                    st.header("📩 Get In Touch With Us!")
                    st.write("##")

                    # Documention: https://formsubmit.co/
                    contact_form = """
                    <form action="https://formsubmit.co/gamingsquad5262@gmail.com" method="POST">
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

                                
                    def main():
                        login()
                        # Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
                    st.set_page_config(page_title="Gaming-Website", page_icon=":bulb:", layout="wide")

            elif not authentication_status:
                with info:
                    st.error('Incorrect Password or username')
            else:
                with info:
                    st.warning('Please feed in your credentials')
        else:
            with info:
                st.warning('Username does not exist, Please Sign up')
except:
    st.success('Refresh Page')
