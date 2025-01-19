import speech_recognition as sr

def recognize_speech_from_microphone():
    # Obiekt rozpoznawania mowy
    recognizer = sr.Recognizer()
    
    # Użycie mikrofonu jako źródła dźwięku
    with sr.Microphone() as source:
        print("Adapting microphone to enviroment...")
        # Automat dostosujacy do halasu otoczenia
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        
        try:
            # Nasłuchiwanie mowy do momentu ciszy
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=20)
            print("Processing...")

            # Google Speech Recognition
            text = recognizer.recognize_google(audio, language="pl-PL")
            print("Recognized speech:", text)
        except sr.UnknownValueError:
            print("Couldn't recognize speech.")
        except sr.RequestError as e:
            print(f"Google Speech Recognition error: {e}")

# Wywołanie funkcji
if __name__ == "__main__":
    recognize_speech_from_microphone()