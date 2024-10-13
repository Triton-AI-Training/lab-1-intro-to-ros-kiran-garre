import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Relay(Node):
	def __init__(self):
		super().__init__()
		self.subscription = self.create_subscription(AckermannDriveStamped, 'drive', self.listener_callback, 10)
		self.publisher = self.create_publisher(AckermannDriveStamped, 'drive_relay', 10)

	def listener_callback(self, msg):
		ack_msg = AckermannDriveStamped()
		ack_msg.drive.speed = msg.drive.speed * 3
		ack_msg.drive.steering_angle = msg.drive.steering_angle * 3

		self.publisher.publish(ack_msg)

def main():
	rclpy.init()
	relay = Relay()
	try:
		rclpy.spin(relay)
	except KeyboardInterrupt:
		pass
	relay.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
