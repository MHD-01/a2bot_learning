import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import adafruit_dht
import board

class DHT11Node(Node):
    def __init__(self):
        super().init('dht11_node')
        self.pub = self.create_publisher(Float32MultiArray, 'dht11/data', 10)
        self.dht = adafruit_dht.DHT11(board.D10)  # GPIO 10
        self.timer = self.create_timer(2.0, self.read_sensor)

    def read_sensor(self):
        try:
            temperature = self.dht.temperature
            humidity = self.dht.humidity
            if temperature is not None and humidity is not None:
                msg = Float32MultiArray()
                msg.data = [float(temperature), float(humidity)]
                self.pub.publish(msg)
                self.get_logger().info(f'Temp: {temperature}C  Humidity: {humidity}%')
        except RuntimeError as e:
            self.get_logger().warn(f'Read error: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = DHT11Node()
    rclpy.spin(node)
    node.dht.exit()
    node.destroy_node()
    rclpy.shutdown()