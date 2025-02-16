import pytest
from domain.robot_base import RobotBase


@pytest.fixture
def robot_base() -> RobotBase:
    return RobotBase()


def test_click(robot_base: RobotBase) -> None:
    robot_base.perform_click(1, 1)


def test_double_click(robot_base: RobotBase) -> None:
    robot_base.perform_double_click(1, 1)


def test_right_click(robot_base: RobotBase) -> None:
    robot_base.perform_right_click(1, 1)


def test_move_to(robot_base: RobotBase) -> None:
    robot_base.navigate_to(1, 1)


def test_type_text(robot_base: RobotBase) -> None:
    robot_base.send_text("Hello")
