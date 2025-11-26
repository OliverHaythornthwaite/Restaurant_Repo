import rclpy
from rclpy.node import Node
from restaurant_interfaces.srv import TakeOrder
from functools import partial


class Waiter(Node):
    def __init__(self):
        super().__init__('waiter_node')
        self.client = self.create_client(TakeOrder, 'place_order')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for Manager...')
        
        self.timer = self.create_timer(3.0, self.send_order)
        self.count = 0

    def send_order(self):
        self.count += 1
        req = TakeOrder.Request()
        req.item_name = "Burger"
        req.quantity = self.count
        future = self.client.call_async(req)
        future.add_done_callback(partial(self.callback, order_id=self.count))
    
    def callback(self, future, order_id):
        try:
            res = future.result()
            status = "ACCEPTED" if res.accepted else "REJECTED"
            self.get_logger().info(f'Order #{order_id}: {status} - {res.message}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')


def main():
    rclpy.init()
    rclpy.spin(Waiter())
    rclpy.shutdown()