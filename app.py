import streamlit as st
from games import guess_number, guess_word, tic_tac_toe, mail


def init():
    st.session_state.project = False
    st.session_state.game = False
    st.session_state.page = 'Homepage'
    st.session_state.pages = {
        'Homepage': home,
        'About me': about,
        'Message me': mail.main,
        'Guess Number': guess_number.main,
        'Guess Word': guess_word.main,
        'Tic Tac Toe': tic_tac_toe.main
    }


def home():

    st.write(
        '''
        # Welcome to My Web App! 👋

        ---

        #### Intro

        I made this web app to finish a project assigned by my professor. 
        While that's the main purpose of why I made this. 
        The real purpose was to improve my coding skill, 
        and I learned a lot while making this web app.
        
        This web app is written purely in Python.
        It contains three games. The games are:

        1. Guess Number
        2. Guess Word
        3. Tic Tac Toe

        All of them can be accessed on the sidebar.
        As for the source code, I will share it when all is finished.
        '''
    )


def about():
    
    st.write(
        '''
        # Coming soon...

        ---
        '''
    )


def draw_style():
    st.set_page_config(
        page_title='fingar-fingar',
        page_icon='🖕'
    )

    style = """
        <style>
            header {visibility: visible;}
            footer {visibility: hidden;}
        </style>
    """

    st.markdown(style, unsafe_allow_html=True)


def load_page():
    st.session_state.pages[st.session_state.page]()


def set_page(loc=None, reset=False):
    if not st.session_state.page == 'Homepage':
        for key in list(st.session_state.keys()):
            if key not in ('project', 'pages', 'page', 'set', 'game'):
                st.session_state.pop(key)

    if loc:
        st.session_state.page = loc
    else:
        st.session_state.page = st.session_state.set

    if reset:
        st.session_state.project = False
    elif st.session_state.page in ('Message me', 'About me'):
        st.session_state.project = True
        st.session_state.game = False
    else:
        pass


def change_button():
    set_page('Guess Number')
    st.session_state.game = True
    st.session_state.project = True


def main():
    if 'page' not in st.session_state:
        init()

    draw_style()

    with st.sidebar:
        project, about, source = st.columns([1, .8, 1])

        if not st.session_state.project:
            project.button('📌 Project', on_click=change_button)
        else:
            project.button('🏠 Homepage', on_click=set_page, args=('Homepage', True))

        if st.session_state.project and st.session_state.game:
            st.selectbox('Page contents', ['Guess Number', 'Guess Word', 'Tic Tac Toe'], key='set', on_change=set_page)

        about.button('About me', on_click=set_page, args=('About me', ))
        source.button('🐍 Source code', on_click=set_page, args=('About me', ))

        contact = st.columns([.2, 1])
        contact[1].button('✉️ Send me a message', on_click=set_page, args=('Message me', ))

        if st.session_state.page == 'Homepage':
            st.image('https://c.tenor.com/-420uI8y-RkAAAAd/anime-welcome.gif', 'moshi-moshi!')

    load_page()


if __name__ == '__main__':
    main()
