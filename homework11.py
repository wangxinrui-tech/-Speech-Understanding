import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    '''
    Use sr.Recognizer.AudioFile(filename) as the source,
    recognize from that source,
    and return the recognized text.
    
    @params:
    filename (str) - the filename from which to read the audio
    language (str) - the language of the audio (optional; default is English)
    
    @returns:
    text (str) - the recognized speech
    '''
    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)  # Read the entire audio file

    try:
        text = recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        text = "[Unrecognized speech]"
    except sr.RequestError as e:
        text = f"[Recognition error: {e}]"

    return text
