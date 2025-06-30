import random
from assistant import logger, tts_engine

class JARVIS_DATA:
    GREET = ["Hi sir!", "Greeting sir!", "I'm here sir!", "At your service sir!"]
    BYE = ["See you sir!", "Have a good day sir!", "Bye sir!"]
    THANKS = ["Always at your service sir!", "Ohh, don't thank me sir! It's my JOB sir!", "Appreciate it sir!"]


def speakJarvis(text):
    """
    :param text: Cloud be any `text` or `JARVIS_DATA` e.g. JARVIS_DATA.GREET
    """

    if text in [JARVIS_DATA.GREET, JARVIS_DATA.BYE, JARVIS_DATA.THANKS]:
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
