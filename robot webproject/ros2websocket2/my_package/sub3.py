import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg._battery_state import BatteryState
delay = 0 
class Sub3(Node):

    def __init__(self):
        super().__init__('sub3')
        self.subscription = self.create_subscription(
            BatteryState,
            'battery_state',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning




    def listener_callback(self, msg):
        self.get_logger().info('percentage: "%f"' % msg.percentage)

        delay = str(msg.percentage)
        with open('/tmp/myfile.txt', "r+") as myfile:
            myfile.read()
            myfile.seek(0)
            myfile.write(delay)
            myfile.truncate()
        



def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = Sub3()
    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()