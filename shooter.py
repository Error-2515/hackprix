import math
import keyinput  # Assuming keyinput is correctly implemented elsewhere
import cv2
import mediapipe as mp
import streamlit as st
import numpy as np

# Initialize session state variables
if "start_wheel" not in st.session_state:
    st.session_state.start_wheel = False
if "result" not in st.session_state:
    st.session_state.result = None

def shooter():
    st.markdown("""
                <style>
        div.stButton > button {
            height: 70px;
            font-size: 30px;
        }
        </style>""", unsafe_allow_html=True)
    st.sidebar.title("Cam-X Controller :video_game:")
    home_button=st.sidebar.button("Home",use_container_width=True,type="primary")
     

    if home_button:
        st.session_state.page="web"
        st.rerun()
    
    st.title("Virtual Steering Wheel")
    st.session_state.start_wheel = False
    st.session_state.result=None
    btn_ph=st.empty()
    # Button to start the virtual wheel
    if not st.session_state.start_wheel:
        start_wheel = btn_ph.button("Start Virtual Wheel", type="primary", use_container_width=True)

    if start_wheel:
        st.session_state.start_wheel = True
        btn_ph.empty()
        home_button=st.button("Exit Controller",type="primary",use_container_width=True)
        
        
        
        
        
        if st.session_state.page=="web":
            st.rerun()
        
        
