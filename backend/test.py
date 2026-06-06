import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

print("JARVIS Voice Layer Initialized.")

# Make it speak
engine.say("Hello. Systems are online. How can I help you today?")
engine.runAndWait()
