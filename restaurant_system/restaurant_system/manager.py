import rclpy
from rclpy.node import Node
from restaurant_interfaces.srv import TakeOrder
from std_msgs.msg import String

class Manager(Node):
    def __init__(self):
        super().__init__('manager_node')
        self.srv = self.create_service(TakeOrder, 'place_order', self.handle_order)
        self.pub = self.create_publisher(String, 'kitchen_orders', 10)
        self.get_logger().info('Manager Online: Ready to take orders.')

    def handle_order(self, request, response):
        if request.item_name.lower() == 'burger':
            response.accepted = True
            response.message = f"Processing {request.quantity} Burgers."
            # Forward to Kitchen
            msg = String()
            msg.data = f"{request.quantity}x {request.item_name}"
            self.pub.publish(msg)
        else:
            response.accepted = False
            response.message = "We only serve Burgers."
        return response


def main():
    rclpy.init()
    rclpy.spin(Manager())
    rclpy.shutdown()