import pytest
from automation.automation import Automation


@pytest.fixture
def automation() -> Automation:
    return Automation()


def test_click(automation: Automation) -> None:
    automation.click(100, 100)


def test_double_click(automation: Automation) -> None:
    automation.double_click(100, 100)


def test_right_click(automation: Automation) -> None:
    automation.right_click(100, 100)


def test_move_to(automation: Automation) -> None:
    automation.move_to(100, 100)


def test_type_text(automation: Automation) -> None:
    automation.type_text("Hello, World!")


def test_click_locate_screen(automation: Automation) -> None:
    automation.click_locate_screen("/tmp/test.png")
