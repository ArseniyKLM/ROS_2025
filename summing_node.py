#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32

def summing_node():
    rospy.init_node('summing_node')
    
    sum_pub = rospy.Publisher('final_result', Int32, queue_size=10)
    
    def poly_callback(msg):
        poly_results = msg.data
        total_sum = sum(poly_results)
        result_msg = Int32(data=total_sum)
        sum_pub.publish(result_msg)
        rospy.loginfo(f"Polynomial: {poly_results} -> Sum: {total_sum}")
    
    rospy.Subscriber('polynomial_results', Int32MultiArray, poly_callback)
    rospy.spin()

summing_node()
