import random
from datetime import datetime
from assistant import logger, tts_engine

class JARVIS_DATA:
    GREET = []
    BYE = ["See you sir!", "Have a good day sir!", "Bye sir!"]
    RESPONSE = ["Hi sir!", "I'm here sir!", "At your service sir!"]
    THANKS = ["Always at your service sir!", "Ohh, don't thank me sir! It's my JOB sir!", "Appreciate it sir!"]


def speakJarvis(text):
    """
    :param text: Cloud be any `text` or `JARVIS_DATA` e.g. JARVIS_DATA.GREET
    """

    if text in [JARVIS_DATA.GREET, JARVIS_DATA.BYE, JARVIS_DATA.RESPONSE, JARVIS_DATA.THANKS]:
        if text in [JARVIS_DATA.GREET]:
            # day time calculator
            hour = datetime.now().hour
            if 0 <= hour <= 11:
                daytime = "Morning"
            elif 12 <= hour <= 15:
                daytime = "Noon"
            elif 16 <= hour <= 17:
                daytime = "Afternoon"
            elif 18 <= hour <= 23:
                daytime = "Evening"
            
            text.append(f"Good {daytime} sir!")
        
        text = random.choice(text)
    
    try:
        logger.info(f"J.A.R.V.I.S: {text}")
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        logger.error(e)

        # Speak out if any error occured
        try:
            tts_engine.say(f"An error occured sir: {e}")
            tts_engine.runAndWait()
        except:
            pass
