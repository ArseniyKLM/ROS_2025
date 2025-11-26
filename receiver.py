#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("I heard %s", msg.data)
    topic_name = rospy.get_param('topic_name', 'default_topic')

rospy.init_node('receiver')
rospy.Subscriber('topic_name', String, callback, queue_size=10)
rospy.spin()
