#!/usr/bin/env python3
import rospy
import sys
import threading
from std_msgs.msg import Int32MultiArray, Int32

class RequestNode:
    def __init__(self, numbers):
        rospy.init_node('request_node', anonymous=True)
        
        self.numbers = numbers
        self.received_result = None
        self.result_received = False
        self.result_event = threading.Event()
        
# Подписчик
        rospy.Subscriber('final_result', Int32, self.result_callback)
        
# Публикатор
        self.input_pub = rospy.Publisher('input_numbers', Int32MultiArray, queue_size=10, latch=True)
        
    def result_callback(self, msg):
        self.received_result = msg.data
        self.result_received = True
        self.result_event.set()  # результат получен
    
    def send_request(self):
# Ждем подписчик
        rospy.sleep(2)
        
# Отправляем числа
        input_msg = Int32MultiArray(data=self.numbers)
        self.input_pub.publish(input_msg)
        
        rospy.loginfo(f"Sent request with numbers: {self.numbers}")
        
# Ждем результат с таймаутом
        if self.result_event.wait(timeout=10.0):  # Ждем
            return self.received_result
        else:
            rospy.logwarn("no result")
            return None

def main():
    try:
        numbers = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]
    except ValueError:
        return
    
    node = RequestNode(numbers)
    result = node.send_request()
    
    if result is not None:
        print(f"{numbers} -> {result}")
    else:
        print("No result")

main()
