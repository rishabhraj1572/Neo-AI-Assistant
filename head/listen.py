import speech_recognition as sr

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")

        while True:
            try:
                audio = r.listen(source, phrase_time_limit=5)
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-us')
                # print("You said:", query)
                return query

            except sr.UnknownValueError:
                print("AI : Sorry, I could not understand what you said. Please speak again.")

            except sr.RequestError as e:
                print(f"Request failed; {e}")
                return "-"

# if __name__ == "__main__":
#     command = take_command()
#     print("Command:", command)
