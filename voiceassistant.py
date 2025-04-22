import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the voice (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first voice in the list
engine.setProperty('rate', 150)  # Set the speaking rate
engine.setProperty('volume', 1.0)  # Set the volume level (0.0 to 1.0)

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()
    def text_to_speech_conversion(input_text):
        """Function to convert input text to speech."""
        if input_text:
            speak(input_text)
        else:
            speak("No text provided to convert to speech.")
    
    def listen_for_command():
        """Function to listen for voice commands and return the recognized text."""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                speak("Sorry, I did not understand that.")
                return None
            except sr.RequestError:
                speak("There seems to be an issue with the speech recognition service.")
                return None
    
    def main():
        """Main function to handle voice commands."""
        speak("Hello! How can I assist you today?")
        while True:
            command = listen_for_command()
            if command:
                command = command.lower()
                if "time" in command:
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"The current time is {current_time}.")
                elif "open browser" in command:
                    speak("Opening the web browser.")
                    webbrowser.open("https://www.google.com")
                elif "play music" in command:
                    music_dir = "C:/Users/Sammy/Music"  # Update with your music directory
                    songs = os.listdir(music_dir)
                    if songs:
                        os.startfile(os.path.join(music_dir, songs[0]))
                        speak("Playing music.")
                    else:
                        speak("No music files found in the directory.")
                elif "exit" in command or "quit" in command:
                    speak("Goodbye!")
                    sys.exit()
                else:
                    speak("Sorry, I didn't understand that command.")
    
    if __name__ == "__main__":
        main()