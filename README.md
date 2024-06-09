Cam-X Controller

Overview
The Cam-X Controller project is a virtual controller system that uses computer vision to create virtual steering wheels and virtual guns. This system leverages technologies like OpenCV and MediaPipe to provide an immersive experience where users can control applications with intuitive gestures.

Streamlit App
The Streamlit app provides a web interface for the Cam-X Controller. It allows users to switch between different modes (About, Developers, Steering, and Web) and start the virtual controllers.

Main Application
The main script initializes the Streamlit application and manages the page navigation and layout.

Table of Contents
1.Overview
2.Repository Structure
3.Key Input Simulation
4.Classes and Data Structures
5.Functions
6.Streamlit App
7.Main Application
8.Virtual Steering Wheel
9.Setup
10.Usage
11.Contributors
12.Repository Structure

This repository contains the following key components:

Key Input Simulation: A Python script using the ctypes library to simulate keyboard inputs.
Streamlit App: A Streamlit-based web interface to interact with the virtual controllers.
Virtual Steering Wheel: Code to implement a virtual steering wheel using hand tracking.
Virtual Gun: Code to implement a virtual gun controller (details not provided).
Key Input Simulation
The keyinput.py file contains the following classes and functions to simulate key presses:

Classes and Data Structures
KeyBdInput: Represents a keyboard input event.
HardwareInput: Represents a hardware input event.
MouseInput: Represents a mouse input event.
Input_I: A union representing different types of input events.
Input: Represents an input event, containing the type and the event data.
Functions
press_key(key): Simulates pressing a key.
release_key(key): Simulates releasing a key.
