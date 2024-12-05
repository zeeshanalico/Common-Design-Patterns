from abc import ABC, abstractmethod

# Abstract Handler
class Logger(ABC):
    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next(self, logger):
        self.next_logger = logger
        return logger

    def handle(self, level, message):
        if self.level == level:
            self.log_message(message)
        elif self.next_logger:
            self.next_logger.handle(level, message)

    @abstractmethod
    def log_message(self, message):
        pass

# Concrete Handlers
class InfoLogger(Logger):
    def log_message(self, message):
        print(f"[INFO]: {message}")

class DebugLogger(Logger):
    def log_message(self, message):
        print(f"[DEBUG]: {message}")

class ErrorLogger(Logger):
    def log_message(self, message):
        print(f"[ERROR]: {message}")

def get_logger_chain():
    error_logger = ErrorLogger("ERROR")
    debug_logger = DebugLogger("DEBUG")
    info_logger = InfoLogger("INFO")

    # Building the chain: INFO -> DEBUG -> ERROR
    info_logger.set_next(debug_logger).set_next(error_logger)
    return info_logger

logger_chain = get_logger_chain()
logger_chain.handle("INFO", "This is an info message.")
logger_chain.handle("ERROR", "This is an error message.")
logger_chain.handle("DEBUG", "This is a debug message.")
