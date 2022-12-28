#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
#from math import pi as mpi
from rclpy import qos

class MpuSubNode(Node):
    def __init__(self):
        super().__init__("mpu6050_sub")
        self.mpu6050_sub_ = self.create_subscription(Imu,"/mpu",self.mpu_callback,qos_profile=qos.qos_profile_sensor_data)
    def mpu_callback(self,msg: Imu):
        self.get_logger().info(str(msg))
def main(args=None):
    rclpy.init(args=args)
    node = MpuSubNode()
    rclpy.spin(node)
    rclpy.shutdown()
