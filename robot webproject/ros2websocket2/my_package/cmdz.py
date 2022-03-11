import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg._twist import Twist

class Cmdz(Node):

    def __init__(self):
        super().__init__('cmdx')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning




    def listener_callback(self, msg):
        self.get_logger().info('angular.z: "%f" ' % msg.angular.z)
        # self.get_logger().info('linear.x: "%f" ,angular.z: "%f"' % (msg.linear.x,msg.angular.z))

        # lin = str(msg.linear.x)

        ang = str(msg.angular.z)

        # ans = "linear.x: " + lin + " angular.z: " + ang

        with open('/tmp/cmdz.txt', "r+") as myfile:
            myfile.read()
            myfile.seek(0)
            myfile.write(ang)
            myfile.truncate()
        



def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = Cmdz()
    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()