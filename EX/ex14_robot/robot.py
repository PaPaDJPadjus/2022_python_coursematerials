"""Virtual robot..."""

from FollowerBot import FollowerBot


def test_run(robot: FollowerBot):
    """
    Make the robot move, doesn't matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(50)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()