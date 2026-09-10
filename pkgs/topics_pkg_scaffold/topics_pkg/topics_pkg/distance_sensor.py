"""
Module 3 exercise, node 1 of 2: the distance sensor.

Fill in the TODOs below, following along with the slides. When it works:

    colcon build --symlink-install
    source install/setup.bash
    ros2 run topics_pkg distance_sensor

Then in a second terminal, watch it publish:

    ros2 topic echo /distance
"""

import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')

        # TODO 1: create a publisher.
        #   - message type:  Float32
        #   - topic name:    '/distance'
        #   - queue size:    10
        # self.pub = self.create_publisher(...)

        # TODO 2: create a timer that calls self.tick every 1.0 seconds.
        # self.create_timer(...)
        pass

    def tick(self):
        # TODO 3: build a Float32 message with msg.data set to a random
        # value between 0.1 and 5.0 (hint: random.uniform(0.1, 5.0)),
        # publish it with self.pub.publish(msg), and log it with
        # self.get_logger().info(...) so you can see it in the terminal too.
        pass


def main():
    rclpy.init()
    rclpy.spin(DistanceSensor())


if __name__ == '__main__':
    main()
