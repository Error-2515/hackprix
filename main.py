import streamlit as st
import about as ab
import settings as se

if "page" not in st.session_state:
    st.session_state.page = 'web'

st.set_page_config(
    page_title="Cam-X",
    page_icon=":video_game:",
    layout="centered",
    initial_sidebar_state="collapsed",  
)

if st.session_state.page == 'web':
    st.sidebar.title("Cam-X Controller :video_game:")
    About_button=st.sidebar.button("About",use_container_width=True)
    settings_button=st.sidebar.button("Settings",use_container_width=True)
    
    if About_button:
        st.session_state.page="about"
        st.rerun()
    if settings_button:
        st.session_state.page="settings"
        st.rerun()

    # Use st.markdown to render the custom HTML and CSS for video background

    st.markdown("<center><h1>Cam-X Controller</h1></center>", unsafe_allow_html=True)
    st.markdown("""---""")
    col1,col2 = st.columns(2)
    st.markdown("""
                <style>
        div.stButton > button {
            height: 70px;
            font-size: 30px;
        }
        </style>""", unsafe_allow_html=True)
    with col1:
        st.subheader("Virtual Wheel:")
        st.button("Start Virtual Wheel", type="primary",use_container_width=True)
        st.markdown("""<p>Take control with our virtual steering
                    wheel, crafted using advanced technology
                    like OpenCV and MediaPipe. Navigate
                    through digital realms effortlessly
                    as you steer through immersive
                    experiences with intuitive
                    gestures.</p>""",unsafe_allow_html=True)
        

    with col2:
        st.markdown("<div style='text-align: right;'><h3>:Virtual Gun</h3></div>", unsafe_allow_html=True)
        st.button("Start Virtual Gun", type="primary",use_container_width=True)
        st.markdown("""<p>Step into the action with our virtual gun,
                    leveraging the latest in OpenCV and MediaPipe technology.
                    Immerse yourself in dynamic gameplay as you wield
                    virtual firepower with precision and realism, bringing gaming
                    to a whole new level of immersion.</p>""",unsafe_allow_html=True)
        
if st.session_state.page=="about":
    ab.about()

if st.session_state.page=="settings":
    se.settings()
        


