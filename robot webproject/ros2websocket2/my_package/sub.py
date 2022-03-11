import rclpy
from rclpy.node import Node
from sensor_msgs.msg._battery_state import BatteryState

from std_msgs.msg import String, Float32   # add
import asyncio                             # add
import websockets                          # add
import random                              # add
ready = 0
testData = 0

class Sub(Node):

    def __init__(self):
        super().__init__('sub')
        self.subscription = self.create_subscription(
            BatteryState,
            'battery_state',
            self.listener_callback,
            10)
        self.subscription  

        
        start_server = websockets.serve(self.accept, "localhost", 9998)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    def listener_callback(self, msg):
        global testData
        global ready
        print("aaaa")
        #self.get_logger().info('Received: "%f"' % msg.percentage)
        ready=1
        testData += 1

    async def accept(self, websocket, msg):
      global ready
      global testData
      testaaa = 1
      while True:
        while ready==0:
            pass
        ready = 0

        num = random.randrange(1,6)
        redata = "%d\n" % num
        testaaa += 1
        await websocket.send("echo : %d" % testaaa); 
        # await websocket.send("echo : "%f"" % redata )     


        ## redata = "%f\n" % msg.percentage
        #await websocket.send("echo : "%f"" % msg.percentage )     
        ## msg = Float32()
        ## msg.data = data
        ## self.publisher_.publish(msg)c

def main(args=None):
    rclpy.init(args=args)
    basic_subcriber = Sub()
    rclpy.spin(basic_subcriber)

    basic_subcriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()