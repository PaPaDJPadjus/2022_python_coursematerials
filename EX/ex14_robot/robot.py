"""Virtual robot..."""

from FollowerBot import FollowerBot


def test_run(robot: FollowerBot()):
    """
    Make the robot move, doesn't matter how much, just as long as it has moved from the starting position.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(30)
    robot.sleep(2)
    robot.set_wheels_speed(0)
    robot.done()


def drive_to_line(robot: FollowerBot):
    """
    Drive the robot until it meets a perpendicular black line, then drive forward 25cm.

    There are 100 pixels in a meter.

    :param FollowerBot robot: instance of the robot that you need to make move
    """
    robot.set_wheels_speed(25)
    robot.sleep(1)
    robot.set_wheels_speed(0)
    for value in robot.get_line_sensors():
        if value == 0:
            robot.done()
        drive_to_line(robot)
