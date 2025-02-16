import logging
from time import time
from typing import Callable, Any
import colorlog


class LogPerformance:
    def __init__(self) -> None:
        handler = colorlog.StreamHandler()
        handler.setFormatter(
            colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        logger = colorlog.getLogger(__name__)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        self.logger = logger

    def log_performance(self, func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time()
            result = func(*args, **kwargs)
            end_time = time()
            self.logger.debug(
                "Function %s args %s took %s seconds", func.__name__, str(args[1:]), end_time - start_time
            )
            return result

        return wrapper

    def log_error(self, func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                self.logger.error("Error in %s: %s", func.__name__, e)
                raise

            return result

        return wrapper

    def log_warning(self, func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            self.logger.warning("Warning in %s", func.__name__)
            return result

        return wrapper

    def info(self, message: str) -> None:
        self.logger.info(message)
