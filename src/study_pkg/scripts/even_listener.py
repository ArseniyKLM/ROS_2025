#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def even_callback(msg):
    rospy.loginfo("Я услышал число: %d", msg.data)

def even_listener():
    rospy.init_node('even_numbers_listener')
    rospy.Subscriber('even_numbers', Int32, even_callback)
    rospy.spin()


even_listener()
