import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Chef(Node):
    def __init__(self):
        super().__init__('chef_node')
        self.sub = self.create_subscription(String, 'kitchen_orders', self.cook, 10)
        self.get_logger().info('Chef Online: Waiting for tickets...')

    def cook(self, msg):
        self.get_logger().info(f'Starting to cook: {msg.data} ')

    def main():
        rclpy.init()
        rclpy.spin(Chef())
        rclpy.shutdown()