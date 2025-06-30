from datetime import datetime
import speech_recognition as sr
from . import logger, recognizer
from .core.jarvis import speakJarvis

# Starting Message from JARVIS
speakJarvis("I'm here for you Sir.")

while True:
    # Use microphone as source
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source) # Reduce background noise
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio).lower()
            logger.info(f"ME: {text}")

            if "jarvis" not in text:
                continue

            if "time" in text:
                now = datetime.now()
                current_time = now.strftime("%I:%M %p") # Format like "03:45 PM"
                speakJarvis(f"The current time is {current_time}")
            
            else:
                speakJarvis("At your service sir.")
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            logger.error(e)
