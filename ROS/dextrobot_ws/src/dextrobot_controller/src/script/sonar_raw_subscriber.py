#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import Range
import math


pubFront = None
pubLeft = None
pubRight = None
pubBack = None

def composeRangeMessage(distance):
    sensor_range = Range()

    # compose the message
    sensor_range.header.frame_id = "sonar_ranger"
    sensor_range.header.stamp = rospy.Time.now()
    sensor_range.radiation_type = Range.ULTRASOUND
    sensor_range.field_of_view = 0.26
    sensor_range.min_range = 0
    sensor_range.max_range = 2
    sensor_range.range = distance/100

    return sensor_range


def callbackFront(data):
    global pubFront
    distance = float(data.data)

    # compose the message
    sensor_range_front = composeRangeMessage(distance)

    # publish the composed message
    pubFront.publish(sensor_range_front)

def callbackLeft(data):
    global pubLeft
    distance = float(data.data)

    # compose the message
    sensor_range_left = composeRangeMessage(distance)

    # publish the composed message
    pubLeft.publish(sensor_range_left)

def callbackRight(data):
    global pubRight
    distance = float(data.data)

    # compose the message
    sensor_range_right = composeRangeMessage(distance)

    # publish the composed message
    pubRight.publish(sensor_range_right)

def callbackBack(data):
    global pubBack
    distance = float(data.data)

    # compose the message
    sensor_range_back = composeRangeMessage(distance)

    # publish the composed message
    pubBack.publish(sensor_range_back)

    
def configure():
    global pubFront, pubLeft, pubRight, pubBack
    rospy.init_node('range_cleaner', anonymous=True)

    rospy.Subscriber("range_front_raw", Float32, callbackFront)
    pubFront = rospy.Publisher("range_front", Range, queue_size=10)
    rospy.Subscriber("range_left_raw", Float32, callbackLeft)
    pubLeft = rospy.Publisher("range_left", Range, queue_size=10)
    rospy.Subscriber("range_right_raw", Float32, callbackRight)
    pubRight = rospy.Publisher("range_right", Range, queue_size=10)
    rospy.Subscriber("range_back_raw", Float32, callbackBack)
    pubBack = rospy.Publisher("range_back", Range, queue_size=10)

    # simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    configure()