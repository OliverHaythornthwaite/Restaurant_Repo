from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='restaurant_system',
            executable='chef',
            name='chef'
        ),
        Node(
            package='restaurant_system',
            executable='manager',
            name='manager'
        ),
        Node(
            package='restaurant_system',
            executable='waiter',
            name='waiter'
        ),
    ])