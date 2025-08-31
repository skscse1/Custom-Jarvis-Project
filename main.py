"""
Voice Assistant (Alexa-like) using SpeechRecognition, OpenAI, and gTTS.
Author: Sukesh
Description: Listens for voice commands, executes tasks (open sites, play music, fetch news),
             or answers general questions using OpenAI GPT.
"""

import os
import webbrowser
import requests
import pygame
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
from openai import OpenAI
import musiclibrary  # Custom module with music links

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def ai_process(command: str) -> str:
    """
    Send user command to OpenAI GPT and return the response.
    """
    client = OpenAI(
        api_key="YOUR_API_KEY_HERE"  # ⚠️ Best Practice: load from env var instead of hardcoding
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",  # Change to "gpt-4o-mini" if you want cheaper/faster
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Alexa, skilled in general tasks like Google cloud. "
                           "Give short responses."
            },
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content


def speak_old(text: str):
    """
    Speak text using pyttsx3 (offline).
    """
    engine.say(text)
    engine.runAndWait()


def speak(text: str):
    """
    Speak text using Google Text-to-Speech (gTTS) and pygame.
    """
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    # Wait until playback finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def process_command(command: str):
    """
    Process voice command and perform relevant action.
    """
    c = command.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open insta" in c:
        webbrowser.open("https://instagram.com")

    elif "open stack overflow" in c:
        webbrowser.open("https://stackoverflow.com")

    elif c.startswith("play"):
        # Play song from custom music library
        try:
            song = c.split(" ")[1]
            link = musiclibrary.music[song]
            webbrowser.open(link)
        except Exception:
            speak("Sorry, I could not find that song.")

    elif "news" in c:
        # Fetch top news headlines
        try:
            req = requests.get(
                "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY"
            )
            if req.status_code == 200:
                data = req.json()
                articles = data.get("articles", [])
                for article in articles[:5]:  # Limit to 5 headlines
                    speak(article["title"])
        except Exception:
            speak("Sorry, I couldn't fetch the news right now.")

    else:
        # Default: send to AI
        result = ai_process(c)
        print("AI:", result)
        speak(result)


if __name__ == "__main__":
    speak("Initializing Alexa...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            print("Recognizing...")
            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if "alexa" in word.lower():
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Alexa Active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                process_command(command)

        except Exception as e:
            print(f"Error: {e}")
