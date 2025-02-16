# pylint: disable=no-member
from frameworks import Automation
from frameworks import LogPerformance


class RobotBase(Automation):
    def __init__(self) -> None:
        self.log = LogPerformance()
        self.log.info("RobotBase initialized")

    @LogPerformance().log_performance
    def perform_click(self, x: int, y: int) -> None:
        super().click(x, y)

    @LogPerformance().log_performance
    def perform_double_click(self, x: int, y: int) -> None:
        super().double_click(x, y)

    @LogPerformance().log_performance
    def perform_right_click(self, x: int, y: int) -> None:
        super().right_click(x, y)

    @LogPerformance().log_performance
    def navigate_to(self, x: int, y: int) -> None:
        super().move_to(x, y)

    @LogPerformance().log_performance
    def send_text(self, text: str) -> None:
        super().type_text(text)
