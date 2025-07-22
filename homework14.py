import datetime
import random
from gtts import gTTS
import speech_recognition as sr
from bs4 import BeautifulSoup
import requests

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    current_time = datetime.datetime.now().strftime("%H:%M")
    text = f"The current time is {current_time}"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What do you call a fake noodle? An impasta!"
    ]
    
    joke = random.choice(jokes)
    tts = gTTS(text=joke, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    today = datetime.datetime.now()
    date_str = today.strftime("%A, %B %d, %Y")
    month = today.month
    year = today.year
    
    tts = gTTS(text=f"Today is {date_str}", lang=lang)
    tts.save(audiofile)
    
    return f"https://www.timeanddate.com/calendar/?year={year}&month={month}"

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)
        
    try:
        text = recognizer.recognize_google(audio).lower()
        print(f"You said: {text}")
        
        if "time" in text:
            what_time_is_it(lang, filename)
        elif "day" in text:
            what_day_is_it(lang, filename)
        elif "joke" in text:
            tell_me_a_joke(lang, filename)
        else:
            tts = gTTS(text="I didn't understand your request", lang=lang)
            tts.save(filename)
            
    except sr.UnknownValueError:
        tts = gTTS(text="Sorry, I couldn't understand you", lang=lang)
        tts.save(filename)
    except sr.RequestError:
        tts = gTTS(text="Sorry, there was an error with the speech recognition service", lang=lang)
        tts.save(filename)
    except Exception as e:
        tts = gTTS(text="Sorry, something went wrong", lang=lang)
        tts.save(filename)
