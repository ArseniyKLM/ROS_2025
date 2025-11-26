#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

def polynomial_node():
    rospy.init_node('polynomial_node')
    
    poly_pub = rospy.Publisher('polynomial_results', Int32MultiArray, queue_size=10)
    
    def input_callback(msg):
        numbers = msg.data
        if len(numbers) != 3:
            rospy.logwarn("Expected 3 numbers")
            return
        
        results = [numbers[0]**3, numbers[1]**2, numbers[2]**1]
        result_msg = Int32MultiArray(data=results)
        poly_pub.publish(result_msg)
        rospy.loginfo(f"{numbers} -> {results}")
    
    rospy.Subscriber('input_numbers', Int32MultiArray, input_callback)
    rospy.spin()

polynomial_node()
