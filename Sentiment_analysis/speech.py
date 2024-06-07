import speech_recognition as sr

def transcribe_audio_to_text(file_path):

    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text






