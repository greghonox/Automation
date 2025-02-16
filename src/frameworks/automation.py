from pyautogui import click, doubleClick, rightClick, moveTo, write


class Automation:

    @staticmethod
    def click(x: int, y: int) -> None:
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
