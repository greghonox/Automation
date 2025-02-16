from pytesseract import image_to_boxes, pytesseract
from typing import Tuple, Callable, Optional
from .logger import LogPerformance


pytesseract.tesseract_cmd = r"/usr/bin/tesseract"


class ValidationInputs:
    def __init__(self) -> None:
        self.log = LogPerformance()

    @classmethod
    def check_typing(
        cls,
        text: str,
        func: Callable,
        box: Optional[Tuple[int, int, int, int]] = None,
        last_check: Optional[bool] = False,
    ) -> None:
        func(text)
        if not last_check:
            cls().log.info(f"Check typing: {text}")
            text_screen = image_to_boxes(box)
            text_screen == text, "Typing failed"
