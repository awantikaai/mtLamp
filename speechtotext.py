import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please speak something...")
    # Adjust for ambient noise to improve accuracy
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

# Recognize and convert speech to text
try:
    # Use Google Web Speech API for recognition
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")


