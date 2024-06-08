import streamlit as st
st.set_page_config(
    page_title="Cam-X",
    page_icon=":video_game:",
    layout="centered",
    initial_sidebar_state="expanded",
    
)
background_image_style = """
    <style>
    .body {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url('https://www.w3schools.com/w3images/lights.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        z-index: -1;
    }
    .content {
        position: relative;
        z-index: 1;
        color: white;
        text-align: center;
        padding-top: 50px;
    }
    </style>
    <body><div class="bg-image-container"></div></body>
    """

vertical_line_style = """
    <style>
    .column-divider {
        border-left: 1px solid #ccc;
        height: 100%;
        margin: 0 10px;
    }
    </style>
"""
# st.sidebar()

# Use st.markdown to render the custom HTML and CSS for video background
st.markdown(background_image_style, unsafe_allow_html=True)

st.markdown("<center><h1>Cam-X</h1></center>", unsafe_allow_html=True)
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
    


