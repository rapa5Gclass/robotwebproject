import rclpy
from rclpy.node import Node

from sensor_msgs.msg._battery_state import BatteryState

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('sub2')
        self.subscription = self.create_subscription(
            BatteryState,
            'battery_state',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('percentage: "%f"' % msg.percentage)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()