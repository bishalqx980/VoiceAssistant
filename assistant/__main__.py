from datetime import datetime
import speech_recognition as sr
from . import logger, recognizer
from .core.jarvis import JARVIS_DATA, speakJarvis

def main():
    # Starting Message from JARVIS
    speakJarvis(JARVIS_DATA.GREET)

    while True:
        # Use microphone as source
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source) # Reduce background noise
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio).lower()
                logger.info(f"ME: {text}")

                # added `jar` cuz it sometime can't detect word `jarvis`
                if "jar" not in text and "jarvis" not in text:
                    continue

                # Logics
                if "time" in text:
                    now = datetime.now()
                    current_time = now.strftime("%I:%M %p") # Format like "03:45 PM"
                    speakJarvis(f"The current time is {current_time}")
                
                elif "thanks" in text or "thank you" in text:
                    speakJarvis(JARVIS_DATA.THANKS)
                
                # End the call
                elif "bye" in text:
                    speakJarvis(JARVIS_DATA.BYE)
                    break
                
                else:
                    speakJarvis(JARVIS_DATA.RESPONSE)
                
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                logger.error(e)


if __name__ == "__main__":
    main()
