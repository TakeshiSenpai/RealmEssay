import pyttsx3

engine = pyttsx3.init()  # Object creation

def run(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def run_and_save(text):
    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(text, 'text.mp3')
    engine.runAndWait()

