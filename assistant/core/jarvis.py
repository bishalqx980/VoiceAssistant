import random
from datetime import datetime
from assistant import logger, tts_engine

class JARVIS_DATA:
    GREET = []
    BYE = ["See you sir!", "Have a good day sir!", "Bye sir!"]
    THANKS = ["Always at your service sir!", "Ohh, don't thank me sir! It's my JOB sir!", "Appreciate it sir!"]

    RESPONSE = ["Hi sir!", "I'm here sir!", "At your service sir!"]
    NOFUNC = ["This function wasn't added sir!"]


def speakJarvis(text):
    """
    :param text: Cloud be any `text` or `JARVIS_DATA` e.g. JARVIS_DATA.GREET
    """
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
    
    else:
        jarvis_responses = {
            name: value
            for name, value in vars(JARVIS_DATA).items()
        }

        for response_list in jarvis_responses.items():
            if text in response_list:
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
