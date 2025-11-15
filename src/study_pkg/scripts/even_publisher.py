#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('even_publisher', anonymous=True)
pub = rospy.Publisher('even_numbers', Int32, queue_size=10)
rate = rospy.Rate(10)

def even_publisher():
    count = 0
    while not rospy.is_shutdown():
        pub.publish(count)
        rospy.loginfo("%d", count)
        count += 2
        rate.sleep()

try:
    even_publisher()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.loginfo("Exception catched")
