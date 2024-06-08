import streamlit as st

def about():
    st.markdown("""
                <style>
        div.stButton > button {
            height: 70px;
            font-size: 30px;
        }
        </style>""", unsafe_allow_html=True)
    st.sidebar.title("Cam-X Controller :video_game:")
    home_button=st.sidebar.button("Home",use_container_width=True,type="primary")
    settings_button=st.sidebar.button("Settings",use_container_width=True)

    if home_button:
        st.session_state.page="web"
        st.rerun()
    if settings_button:
        st.session_state.page="settings"
        st.rerun()
    st.title("About page")