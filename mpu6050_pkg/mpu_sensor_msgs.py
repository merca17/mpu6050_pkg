#!usr/bin/env python3
# @autor: Juan Sebastian Mercado Allende
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
#from math import pi as mpi
from rclpy import qos
from mpu6050 import mpu6050
#import math as m
mpu = mpu6050(0x68)


class MpuMsgsNode(Node):
    def __init__(self):
        super().__init__("mpu_sensor_msgs")
        self.mpu6050_sensor_pub_ = self.create_publisher(Imu, "/imu",qos_profile=qos.qos_profile_sensor_data)
        self.timer_ = self.create_timer(0.5,self.send_imu_command)
        self.get_logger().info("mpu6050 to imu Msgs node has been started")
    def send_imu_command(self):
        msg = Imu()
        # This is a message to hold data from an IMU (Inertial Measurement Unit)

        #

        # Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec

        #

        # If the covariance of the measurement is known, it should be filled in (if all you know is the

        # variance of each measurement, e.g. from the datasheet, just put those along the diagonal)

        # A covariance matrix of all zeros will be interpreted as "covariance unknown", and to use the

        # data a covariance will have to be assumed or gotten from some other source

        #

        # If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an

        # orientation estimate), please set element 0 of the associated covariance matrix to -1

        # If you are interpreting this message, please check for a value of -1 in the first element of each

        # covariance matrix, and disregard the associated estimate.                
        msg.header.stamp = Node.get_clock(self).now().to_msg()
        msg.header.frame_id = 'mpu6050'
        gyro_data = mpu.get_gyro_data()
        msg.angular_velocity.x = gyro_data['x']
        msg.angular_velocity.y = gyro_data['y']
        msg.angular_velocity.z = gyro_data['z']
        accel_data = mpu.get_accel_data()
        msg.linear_acceleration.x = accel_data['x']
        msg.linear_acceleration.y = accel_data['y']
        msg.linear_acceleration.z = accel_data['z']

     
            

        #publishing
        self.mpu6050_sensor_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MpuMsgsNode()
    rclpy.spin(node)
    rclpy.shutdown()