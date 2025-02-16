import pytest
from frameworks import Automation


@pytest.fixture
def auto() -> Automation:
    return Automation()


def test_click(auto: Automation) -> None:
    auto.click(100, 100)


def test_double_click(auto: Automation) -> None:
    auto.double_click(100, 100)


def test_right_click(auto: Automation) -> None:
    auto.right_click(100, 100)


def test_move_to(auto: Automation) -> None:
    auto.move_to(100, 100)


def test_type_text(auto: Automation) -> None:
    auto.type_text("Hello, World!")
