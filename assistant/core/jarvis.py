from assistant import logger, tts_engine

def speakJarvis(text=None):
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
