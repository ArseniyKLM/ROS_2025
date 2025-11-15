#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def overflow_callback(msg):
    rospy.loginfo("Overflow detected: %s", msg.data)

def overflow_listener():
    rospy.init_node('overflow_listener', anonymous=True)
    rospy.Subscriber('overflow_topic', String, overflow_callback)
    rospy.spin()
overflow_listener()
