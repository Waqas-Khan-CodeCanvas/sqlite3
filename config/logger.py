from datetime import datetime

class Logger:
    def __init__(self, name="APP"):
        self.name = name

    def _log(self, level, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time}] [{self.name}] [{level}] {message}")

    def info(self, message):
        self._log("INFO", message)

    def success(self, message):
        self._log("SUCCESS", message)

    def warning(self, message):
        self._log("WARNING", message)

    def error(self, message):
        self._log("ERROR", message)

    def debug(self, message):
        self._log("DEBUG", message)
        
        
        
# usecase 
# from logger import Logger

# log = Logger("MY_APP")

# log.info("Application started")
# log.success("Data loaded successfully")
# log.warning("This is a warning")
# log.error("Something went wrong")
# log.debug("Debugging details here") 