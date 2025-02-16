from pytesseract import image_to_boxes, pytesseract
from typing import Tuple, Callable, Optional
from .logger import LogPerformance
from pyautogui import screenshot


pytesseract.tesseract_cmd = r"C:\Users\honoragr\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


class ValidationInputs:
    def __init__(self) -> None:
        self.log = LogPerformance()

    @classmethod
    def check_typing(
        cls,
        text: str,
        func: Callable,
        last_check: Optional[bool] = False,
        screen: Optional[screenshot] = None,
    ) -> None:
        func(text)
        if last_check:
            cls().log.info(f"Check typing: {text}")
            captured_text = image_to_boxes(screen)
            captured_text == text, "Typing failed"
