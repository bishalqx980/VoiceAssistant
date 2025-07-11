import speech_recognition as sr
from . import logger
from .core.jarvis import JARVIS_DATA, speakJarvis
from .core.process_text import process_text

def main():
    recognizer = sr.Recognizer()

    # Greeting from JARVIS
    speakJarvis(JARVIS_DATA.GREET)

    while True:
        # Use microphone as source
        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source) # Reduce background noise
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio).lower()
                if text: process_text(text)

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                logger.error(e)
            except Exception as e:
                logger.error(e)


if __name__ == "__main__":
    main()
