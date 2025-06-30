import pyttsx3
import speech_recognition as sr
from .utils.logger import setup_logging

# Required Preps
logger = setup_logging()

# Main func
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Optional
tts_engine.setProperty('rate', 150)  # Speed of speech
tts_engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

logger.info("""

     ██╗    █████╗    ██████╗   ██╗   ██╗  ██╗   ███████╗
     ██║   ██╔══██╗   ██╔══██╗  ██║   ██║  ██║   ██╔════╝
     ██║   ███████║   ██████╔╝  ██║   ██║  ██║   ███████╗
██   ██║   ██╔══██║   ██╔══██╗  ╚██╗ ██╔╝  ██║   ╚════██║
╚█████╔╝██╗██║  ██║██╗██║  ██║██╗╚████╔╝██╗██║██╗███████║
 ╚════╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝ ╚═══╝ ╚═╝╚═╝╚═╝╚══════╝
                                            by @bishalqx980
""")
