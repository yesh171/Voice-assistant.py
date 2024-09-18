import speech_recognition as sr
import webbrowser

r = sr.Recognizer()
r.energy_threshold = 5000

with sr.Microphone() as source:
    print("Speak!")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        
        # Use Google search URL format
        search_url = "https://www.google.com/search?q=" + text.replace(" ", "+")
        webbrowser.open(search_url)
    except sr.UnknownValueError:
        print("Couldn't understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
