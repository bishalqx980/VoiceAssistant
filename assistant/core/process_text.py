from datetime import datetime
from .jarvis import JARVIS_DATA, speakJarvis

def process_text(text):
    # added `jar` cuz it sometime can't detect word `jarvis`
    names = ["jar", "jarvis"]
    listento = None
    for name in names:
        if name in text: listento = name

    if not listento: return

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
        exit()
    
    elif text.replace(listento, "").strip():
        speakJarvis(JARVIS_DATA.NOFUNC)

    else:
        speakJarvis(JARVIS_DATA.RESPONSE)
