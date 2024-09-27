#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

def callback(msg):
    print("x: %s, Y: %s "% (msg.pose.pose.position.x, msg.pose.pose.position.y))

def move_robot():

    vel_msg = Twist()

    # Set the linear velocity in the x-direction (forward)
    vel_msg.linear.x = float(input("Enter x value: "))

    # Set the angular velocity in the z-direction (rotation)
    vel_msg.angular.z =float(input("Enter z value: "))
    # Initialize the ROS node
    rospy.init_node('move_robot_node', anonymous=True)
    # Create Subscriber to /Odom topic
    sub = rospy.Subscriber('/odom', Odometry, callback)
    # Create a publisher to the /cmd_vel topic
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # Create a Twist message
    rospy.loginfo("Moving the robot forward and rotating...")
    # Publish the velocity message for a duration
    while not rospy.is_shutdown():
        rate = rospy.Rate(10)  # 10 Hz
        vel_pub.publish(vel_msg)
        rate.sleep()

#     # Stop the robot
#     vel_msg.linear.x = 0
#     vel_msg.angular.z = 0
#     vel_pub.publish(vel_msg)
#     rospy.loginfo("Robot stopped.")

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass