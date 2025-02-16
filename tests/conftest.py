import numpy as np
import pytest
from frameworks import Automation
from domain.robot_base import RobotBase


@pytest.fixture
def auto() -> Automation:
    return Automation()


@pytest.fixture
def robot_base() -> RobotBase:
    return RobotBase()
