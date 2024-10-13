import rclpy
from rclpy import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
	def __init__(self):
		super().__init__()
 		self.publisher = self.create_publisher(AckemannDriveStamped, 'driver', 10)
		self.declare_parameter('v', 0)
		self.declare_parameter('d', 0)
		self.timer = self.create_timer(0.001, self.timer_callback)

	def timer_callback(self):
		v_val = self.get_parameter('v').get_parameter_value().string_value
		d_val = self.get_parameter('d').get_parameter_value().string_value
		ack_msg = AckermannDriveStamped()
                ack_msg.drive.steering_angle = d
                ack_msg.drive.speed = v
                self.publisher.publish(ack_msg)

def main():
	rclpy.init()
	talker = Talker()
	try:
		rclpy.spin(talker)
	except KeyboardInterrupt:
		pass
	talker.destroy_node()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
