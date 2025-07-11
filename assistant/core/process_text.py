from datetime import datetime
from assistant import logger
from .jarvis import JARVIS_DATA, speakJarvis

def process_text(text):
    # added `jar` cuz it sometime can't detect word `jarvis`
    text = text.lower()

    names = ["jar", "jarv", "jarvi", "jarve", "jarvee", "jarvees", "jarvis", "jervis"]
    listento = None
    for name in names:
        if name in text: listento = name

    if not listento: return

    logger.info(text.replace(listento, "Jarvis"))

    # Logics
    if any(i in text for i in ["hi", "hello"]):
        speakJarvis(JARVIS_DATA.RESPONSE)
    
    elif any(i in text for i in ["time", "time now"]):
        now = datetime.now()
        current_time = now.strftime("%I:%M %p") # Format like "03:45 PM"
        speakJarvis(f"It's {current_time}")
    
    elif any(i in text for i in ["thanks", "thank you"]):
        speakJarvis(JARVIS_DATA.THANKS)
    
    # End the call
    elif any(i in text for i in ["bye", "see you"]):
        speakJarvis(JARVIS_DATA.BYE)
        exit()
    
    elif text.replace(listento, "").strip():
        speakJarvis(JARVIS_DATA.NOFUNC)

    else:
        speakJarvis(JARVIS_DATA.RESPONSE)
