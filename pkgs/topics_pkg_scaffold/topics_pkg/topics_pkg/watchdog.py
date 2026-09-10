"""
Module 3 exercise, node 2 of 2: the watchdog.

Fill in the TODOs below, following along with the slides. Run this ALONGSIDE
distance_sensor (in a second terminal):

    ros2 run topics_pkg watchdog

Then go back to the distance_sensor terminal and press Ctrl-C to kill it.
Count the seconds until this node prints a warning.
"""

import time

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

TIMEOUT_S = 3.0


class Watchdog(Node):
    def __init__(self):
        super().__init__('watchdog')
        self.last_seen = time.time()

        # TODO 1: subscribe to '/distance' (message type Float32, queue
        # size 10), calling self.on_reading for every message received.
        # self.create_subscription(...)

        # TODO 2: create a timer that calls self.check every 1.0 seconds.
        # self.create_timer(...)
        pass

    def on_reading(self, msg):
        # TODO 3: record that a message just arrived. Update self.last_seen
        # to the current time (hint: time.time()).
        pass

    def check(self):
        # TODO 4: compute how long it's been since the last message
        # (current time minus self.last_seen). If that gap is greater than
        # TIMEOUT_S, log a warning with self.get_logger().warn(...).
        pass


def main():
    rclpy.init()
    rclpy.spin(Watchdog())


if __name__ == '__main__':
    main()
