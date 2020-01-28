import glob
import os

from setuptools import find_packages
from setuptools import setup

package_name = "turtlebot3_example"

setup(
    name=package_name,
    version="2.0.1",
    packages=find_packages(),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        # To be added
        # ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', 'turtlebot3_interactive_marker.launch.py'))),
        # ('share/' + package_name + '/launch', glob.glob(os.path.join('launch', 'turtlebot3_obstacle_detection.launch.py'))),
        # ('share/' + package_name + '/rviz', glob.glob(os.path.join('rviz', 'turtlebot3_interactive_marker.rviz'))),
    ],
    install_requires=["setuptools", "launch"],
    zip_safe=True,
    author=["Ryan Shim", "Gilbert"],
    author_email=["jhshim@robotis.com", "kkjong@robotis.com"],
    maintainer="Pyo",
    maintainer_email="pyo@robotis.com",
    keywords=["ROS", "ROS2", "examples", "rclpy"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    description=("Examples of Different TurtleBot3 Usage."),
    license="Apache License, Version 2.0",
    entry_points={
        "console_scripts": [
            # To be added
            # 'turtlebot3_interactive_marker = turtlebot3_example.turtlebot3_interactive_marker.main:main',
            "turtlebot3_obstacle_detection = turtlebot3_example.turtlebot3_obstacle_detection.main:main",
            "turtlebot3_patrol_client = turtlebot3_example.turtlebot3_patrol_client.main:main",
            "turtlebot3_patrol_server = turtlebot3_example.turtlebot3_patrol_server.main:main",
            "turtlebot3_position_control = turtlebot3_example.turtlebot3_position_control.main:main",
            "turtlebot3_logging_control = turtlebot3_example.turtlebot3_position_control.logging:main",
        ],
    },
)
