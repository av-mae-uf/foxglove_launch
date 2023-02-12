import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    ld = LaunchDescription()

    foxglove = ExecuteProcess(
        cmd=[
            "xdg-open",
            "foxglove://open?ds=rosbridge-websocket&ds.url=ws%3A%2F%2F192.168.0.100%3A9090",
        ],
    )
    ld.add_action(foxglove)

    return ld
