from frameworks import ValidationInputs
from domain import RobotBase
from threading import Thread
from time import sleep
from PIL import Image


def test_validation_without_check(robot_base: RobotBase, validation_inputs: ValidationInputs) -> None:
    text = "Jesus"
    func = robot_base.send_text
    validation_inputs.check_typing(text, func)


def test_validation_with_check(robot_base: RobotBase, validation_inputs: ValidationInputs, get_image: Image) -> None:
    text = "Test Jesus"
    th = Thread(target=robot_base.alert_prompt, args=("Pytest com Jesus",), daemon=True)
    th.start()
    sleep(1)
    screen = robot_base.get_locate_screen(get_image)
    robot_base.perform_click(screen_shot=screen)
    sleep(1)
    validation_inputs.check_typing(text, robot_base.send_text, screen)
    assert True