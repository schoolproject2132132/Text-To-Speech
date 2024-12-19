import os
import sys

def text_to_speech(text):
    if sys.platform.startswith('linux'):
        os.system(f'espeak "{text}"')
    elif sys.platform == 'darwin':
        os.system(f'say "{text}"')
    elif sys.platform == 'win32':
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print("Unsupported OS.")
        return

def main():
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)

if __name__ == "__main__":
    main()
