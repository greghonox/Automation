from pyautogui import click, doubleClick, rightClick, moveTo, write, locateOnScreen, screenshot, prompt, press
from typing import Optional, Tuple


class Automation:

    @staticmethod
    def click(x: Optional[int], y: Optional[int], screen_shot: Optional[screenshot]) -> None:
        if screen_shot:
            click(screen_shot)
            return
        click(x, y)

    @staticmethod
    def double_click(x: int, y: int) -> None:
        doubleClick(x, y)

    @staticmethod
    def right_click(x: int, y: int) -> None:
        rightClick(x, y)

    @staticmethod
    def move_to(x: int, y: int) -> None:
        moveTo(x, y)

    @staticmethod
    def type_text(text: str) -> None:
        write(text)

    @staticmethod
    def get_screen_on_region(region:Optional[Tuple[int, int, int, int]]=False) -> screenshot:
        return screenshot(region=region) if region else screenshot()

    @staticmethod
    def get_locate_screen(img: screenshot) -> locateOnScreen:
        return locateOnScreen(img, 60)
    
    @staticmethod
    def alert_prompt(title:str) -> str:
        return prompt(title)
    
    @staticmethod
    def press_key(key: str) -> None:
        press(key)