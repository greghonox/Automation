import pytest
from domain.robot_base import RobotBase


@pytest.fixture
def robot_base() -> RobotBase:
    return RobotBase()


def test_click(robot_base: RobotBase) -> None:
    robot_base.click(100, 200)


def test_double_click(robot_base: RobotBase) -> None:
    robot_base.double_click(100, 200)


def test_right_click(robot_base: RobotBase) -> None:
    robot_base.right_click(100, 200)


def test_move_to(robot_base: RobotBase) -> None:
    robot_base.move_to(100, 200)


def test_type_text(robot_base: RobotBase) -> None:
    robot_base.type_text("Hello")
