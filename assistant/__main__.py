import speech_recognition as sr
from . import logger, recognizer
from .core.jarvis import JARVIS_DATA, speakJarvis
from .core.process_text import process_text

def main():
    # Greeting from JARVIS
    speakJarvis(JARVIS_DATA.GREET)

    while True:
        # Use microphone as source
        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source) # Reduce background noise
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio).lower()
                logger.info(f"ME: {text}")

                if text: process_text(text)

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                logger.error(e)
            except Exception as e:
                logger.error(e)


if __name__ == "__main__":
    main()
