"""
Module 2 exercise: your first ROS 2 node — COMPLETED REFERENCE SOLUTION.

This is the instructor/answer-key version of heartbeat.py, with the TODOs
from the student scaffold filled in. Do not distribute this to students
before the session — hand out the stubbed version (my_first_pkg_scaffold.zip)
instead, and use this only to check answers or to re-derive the stub if it's
ever lost.

    colcon build --symlink-install
    source install/setup.bash
    ros2 run my_first_pkg heartbeat

Then in a second terminal:

    ros2 topic echo /heartbeat
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Heartbeat(Node):
    def __init__(self):
        super().__init__('heartbeat')

        # TODO 1 (solved): a publisher on '/heartbeat', message type String,
        # queue size 10.
        self.pub = self.create_publisher(String, '/heartbeat', 10)

        # TODO 2 (solved): a timer that calls self.tick every 1.0 seconds.
        self.create_timer(1.0, self.tick)

    def tick(self):
        # TODO 3 (solved): build and publish a String message.
        msg = String()
        msg.data = 'I am alive'
        self.pub.publish(msg)


def main():
    rclpy.init()
    rclpy.spin(Heartbeat())


if __name__ == '__main__':
    main()