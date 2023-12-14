

Project Documentation: Voice Assistant (Eddy)


Table of Contents

Introduction

Overview
    • 
    • Purpose  
    • Features
    • Technologies Used  
    • Setup and install
    • Prerequisites
    • Installation Steps
    • Functionality
    • Voice Recognition
    • Text-to-Speech
    • YouTube Video Playback
    • Date and Time Information
    • Wikipedia Search
    • Project Structure
    • File Structure
    • Modules and Dependencies
    • Usage
    
Running the Voice Assistant
Code Explanation

  talk Function
  input_instruction Function
  play_Eddy Function
  Error Handling

Handling Speech Recognition Errors
Handling Exceptions
Customization
Adding New Functionalities
Modifying Activation Word
Known Issues and Future Improvements
Potential Improvements
Contributing
Guidelines for Contributions



1. Introduction
Overview

The Voice Assistant project, named Eddy, is designed to perform various tasks through voice commands. Users can interact with Eddy by speaking commands, and the assistant responds accordingly. The project incorporates speech recognition, text-to-speech conversion, and integration with external APIs to provide functionalities like playing YouTube videos, retrieving date and time information, and searching Wikipedia.

Purpose

The purpose of Eddy is to create a simple and customizable voice assistant that can assist users with everyday tasks using natural language commands.

Features

    • Speech recognition for user input
    • Text-to-speech for responses
    • YouTube video playback
    • Date and time information retrieval
    • Wikipedia search capabilities
    • Technologies Used
    • Python
    • SpeechRecognition library
    • pyttsx3 library
    • pywhatkit library
    • datetime module
    • Wikipedia API
    
2. Setup and Installation
Prerequisites
Python installed (version 3.10 0r later)
Internet connection for some functionalities
Installation Steps
Clone the repository: git clone https://github.com/896ma/AI Assistant.git
Navigate to the project directory: cd voice-assistant
Install dependencies: pip install -r requirements.txt

3. Functionality
Voice Recognition
 -Eddy uses the SpeechRecognition library to capture and interpret voice commands from the user.

Text-to-Speech
-The assistant employs pyttsx3 for converting text responses into spoken words.

YouTube Video Playback
-Users can command Eddy to play YouTube videos using the pywhatkit library.
By simply  saying “Eddy Play” and then followed by what the user want to play.

Date and Time Information
-Eddy can provide the current date and time upon user request.

Wikipedia Search
 -The assistant can search Wikipedia and provide a summary of the requested topic.

4. Project Structure

File Structure
 -main.py: Main script containing the voice assistant functionalities.
 -requirements.txt: File listing required dependencies.
 -Modules and Dependencies
 -speech_recognition: For voice recognition.
 -pyttsx3: For text-to-speech conversion.
-pywhatkit: For YouTube video playback.
-datetime: For working with date and time.
-wikipedia: For searching Wikipedia.

5. Usage
Running the Voice Assistant
-Execute the main.py script to start Eddy. Speak the activation word ("Eddy") followed by your command.

6. Code Explanation
talk Function
-The talk function takes a text input and uses pyttsx3 to convert it into speech.

input_instruction Function
-The input_instruction function captures user voice input, recognizes it using Google's speech recognition, and returns the interpreted instruction.

play_Eddy Function
-The play_Eddy function processes the user's instruction and executes the corresponding functionality based on predefined commands.

7. Error Handling
Handling Speech Recognition Errors
The project includes error handling for potential issues during speech recognition, such as unknown values and request errors.

Handling Exceptions
-Various exceptions are handled, providing appropriate messages to the user for a better experience.

8. Customization
Adding New Functionalities
To add new functionalities, extend the conditional statements in the play_Eddy function.

Modifying Activation Word
 -Modify the activation word by changing the keyword in the if "Eddy" in instruction statement.


Exit  Application
- the program can come to a stop  by implementing the python  quit() function when the key words exit program are mentioned.


