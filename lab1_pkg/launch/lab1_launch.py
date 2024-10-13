from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([

        # Launch talker node
        Node(
            package='lab1_pkg',
            executable='talker',
            name='talker',
            output='screen',
            parameters=[{
                'v': 2,
                'd': 1
            }]
        ),

        # Launch relay node
        Node(
            package='lab1_pkg',
            executable='relay',
            name='relay',
            output='screen'
        )
    ])
