import json
import pyaudio
from vosk import Model, KaldiRecognizer

from . import logger
from .core.jarvis import JARVIS_DATA, speakJarvis
from .core.process_text import process_text

def main():
    mic = pyaudio.PyAudio()
    stream = mic.open(
        rate=16000,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=8192
    )
    stream.start_stream()

    recognizer = KaldiRecognizer(Model("assistant/utils/vosk-model"), 16000)

    # Greeting from JARVIS
    speakJarvis(JARVIS_DATA.GREET)

    while True:
        try:
            data = stream.read(4096, False)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                data = json.loads(result)
                text = data.get("text")

                if text:
                    logger.info(f"ME: {text}")
                    process_text(text)
        except Exception as e:
            logger.error(e)
            exit()


if __name__ == "__main__":
    main()
