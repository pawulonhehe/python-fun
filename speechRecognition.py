import speech_recognition as sr

def recognize_speech_from_microphone():
    # obiekt rozpozniania mowy
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Powiedz coś")
        try:
            # dostosowanie poziomu hałasu otoczenia
            recognizer.adjust_for_ambient_noise(source, duration=5)
            print("Nasluchuję...")

            # nagrywanie dzwieku
            audio = recognizer.listen(source)

            # rozpoznawanie mowy
            print("Przetwarzanie...")
            text = recognizer.recognize_google(audio, language="pl-PL")
            print("Rozpoznany tekst:", text)
        except sr.UnknownValueError:
            print("Nie udało się rozpoznać mowy.")
        except sr.RequestError as e:
            print(f"Błąd usługi Google Speech Recognition: {e}")

# wywolanie funkcji
if __name__ == "__main__":
    recognize_speech_from_microphone()
