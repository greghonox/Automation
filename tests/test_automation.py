from frameworks import Automation
from typing import Tuple, Optional
from threading import Thread
from time import sleep
from PIL import Image
import pytest

def test_click(auto: Automation) -> None:
    auto.click(1, 1)


def test_double_click(auto: Automation) -> None:
    auto.double_click(1, 1)


def test_right_click(auto: Automation) -> None:
    auto.right_click(1, 1)


def test_move_to(auto: Automation) -> None:
    auto.move_to(1, 1)


def test_type_text(auto: Automation) -> None:
    auto.type_text("Hello, World!")


@pytest.mark.parametrize(
    "box",[
        None,
        (100, 100, 100, 100)
    ]
)
def test_get_screen_on_region(box:Optional[Tuple], auto: Automation) -> None:
    img = auto.get_screen_on_region(box)
    assert isinstance(img.size[0], int)
    assert isinstance(img.size[1], int)
    
    
def test_get_locate_screen(auto: Automation) -> None:
    img = auto.get_screen_on_region((0, 0, 100, 100))
    screen = auto.get_locate_screen(img)
    assert screen.top == 0
    assert screen.left == 0
    assert screen.height == 100
    assert screen.width == 100
    
def test_get_locate_screen_with_image(auto: Automation, get_image: Image) -> None:
    th = Thread(target=auto.alert_prompt, args=("Pytest com Jesus",), daemon=True)
    th.start()
    sleep(1)
    screen = auto.get_locate_screen(get_image)
    assert isinstance(screen.height, int)