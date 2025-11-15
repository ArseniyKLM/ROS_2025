#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

pub_even = rospy.Publisher('even_numbers', Int32, queue_size=10)
pub_overflow = rospy.Publisher('overflow_topic', String, queue_size=10)
rospy.init_node('even_publisher_with_overflow', anonymous=True)
rate = rospy.Rate(10)
    
def even_publisher_with_overflow():
    count = 0
    while not rospy.is_shutdown():
        pub_even.publish(count)
        rospy.loginfo("%d", count)
        
        if count >= 100:
            overflow_msg = "Reached 100, Reset"
            pub_overflow.publish(overflow_msg)
            rospy.logwarn(overflow_msg)
            count = 0
        else:
            count += 2        
        rate.sleep()

try:
    even_publisher_with_overflow()
except rospy.ROSInterruptException:
    rospy.loginfo("Exception catched")	
