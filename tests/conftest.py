import numpy as np
import pytest
from frameworks import Automation, ValidationInputs
from domain import RobotBase
from PIL import Image
from os.path import join
from os import getcwd

@pytest.fixture
def auto() -> Automation:
    return Automation()


@pytest.fixture
def robot_base() -> RobotBase:
    return RobotBase()


@pytest.fixture
def validation_inputs() -> ValidationInputs:
    return ValidationInputs()


@pytest.fixture
def get_image() -> Image:
    return Image.open(join(getcwd(), "tests","asserts", "test_validation.png"))
    