# pylint: disable=no-member
import logging
from frameworks import Automation
import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

logger = colorlog.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class RobotBase(Automation):
    def __init__(self) -> None:
        super().__init__()
        logger.info("RobotBase initialized")

    def perform_click(self, x: int, y: int) -> None:
        logger.info(f"Click at ({x}, {y})")
        super().click(x, y)

    def perform_double_click(self, x: int, y: int) -> None:
        logger.info(f"Double click at ({x}, {y})")
        super().double_click(x, y)

    def perform_right_click(self, x: int, y: int) -> None:
        logger.info(f"Right click at ({x}, {y})")
        super().right_click(x, y)

    def navigate_to(self, x: int, y: int) -> None:
        logger.info(f"Move to ({x}, {y})")
        super().move_to(x, y)

    def send_text(self, text: str) -> None:
        logger.info(f"Type text: {text}")
        super().type_text(text)
