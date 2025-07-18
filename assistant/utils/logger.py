import logging

def setup_logging():
    try:
        open("log.txt", "w")
    except Exception as e:
        print(e)
        exit()
    
    # logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(filename)s - %(message)s"
    # logging_format = "%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
    logging_format = "%(message)s"
    logging_level = logging.INFO

    logging.basicConfig(
        filename="log.txt",
        format=logging_format,
        level=logging_level
    )

    logging.getLogger("httpx").setLevel(logging.WARNING) # To avoid all GET and POST requests being logged
    logging.getLogger('werkzeug').setLevel(logging.ERROR) # Disable Werkzeug logging
    logging.getLogger('comtypes').setLevel(logging.WARNING) # Disabled comtype logging

    console = logging.StreamHandler()
    console.setLevel(logging_level)
    formatter = logging.Formatter(logging_format)
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)

    return logging.getLogger(__name__)
