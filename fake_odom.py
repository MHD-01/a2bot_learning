import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class FakeOdom(Node):
    def __init__(self):
        super().__init__('fake_odom')

        # Robot pose
        self.x = 0.0
        self.y = 0.0
        self.th = 0.0

        # Robot size (match your URDF)
        self.wheel_radius = 0.033
        self.wheel_separation = 0.20

        # Remember last wheel angles
        self.last_left  = 0.0
        self.last_right = 0.0
        self.started    = False

        # Subscribe to wheel angles, publish TF
        self.create_subscription(JointState, 'joint_states', self.joint_cb, 10)
        self.tf_broadcaster = TransformBroadcaster(self)

    def joint_cb(self, msg):
        # Get the wheel angles from the message
        left = msg.position[msg.name.index('left_wheel_joint')]
        right = msg.position[msg.name.index('right_wheel_joint')]

        # Skip the very first message (nothing to compare against yet)
        if not self.started:
            self.last_left, self.last_right = left, right
            self.started = True
            return

        # How much each wheel turned since last time
        dl = (left - self.last_left) * self.wheel_radius
        dr = (right - self.last_right) * self.wheel_radius
        self.last_left, self.last_right = left, right

        # Update robot pose using differential drive math
        self.x  += (dl + dr) / 2.0 * math.cos(self.th)
        self.y  += (dl + dr) / 2.0 * math.sin(self.th)
        self.th += (dr - dl) / self.wheel_separation

        # Publish odom -> base_link transform
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'
        t.transform.translation.x = self.x
        t.transform.translation.y = self.y
        t.transform.rotation.z = math.sin(self.th / 2.0)
        t.transform.rotation.w = math.cos(self.th / 2.0)
        self.tf_broadcaster.sendTransform(t)


def main():
    rclpy.init()
    rclpy.spin(FakeOdom())
    rclpy.shutdown()


if __name__ == '__main__':
    main()