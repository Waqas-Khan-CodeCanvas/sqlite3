from datetime import datetime

class Logger:
    def __init__(self, name="APP"):
        self.name = name

    def _log(self, level, message):
        timestamp = datetime.now().strftime("%A %d-%B-%Y %H:%M:%S %p")
        print(f"[{timestamp}] [{self.name}-{level}] {message}")

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
        