import streamlit as st

def settings():
    st.markdown("""
                <style>
        div.stButton > button {
            height: 70px;
            font-size: 30px;
        }
        </style>""", unsafe_allow_html=True)
    st.sidebar.title("Cam-X Controller :video_game:")
    home_button=st.sidebar.button("Home",use_container_width=True,type="primary")
    about_button=st.sidebar.button("About",use_container_width=True)

    if home_button:
        st.session_state.page="web"
        st.rerun()
    if about_button:
        st.session_state.page="about"
        st.rerun()
    st.title("Settings page")