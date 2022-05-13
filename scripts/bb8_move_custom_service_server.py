#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist
import math as math
def move_side(l):
    twist = Twist()
    twist.linear.x = l / 1
    my_pub.publish(twist)
    rate.sleep()
    stop()


    
def move_corner():
    twist = Twist()
    twist.angular.z = math.pi / 2 

    my_pub.publish(twist)
    rate.sleep()

    stop()
    


def stop():
    twist = Twist()
    my_pub.publish(twist)

    


def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_square_custom has been called")

    # move_circle.linear.x = 0.2
    # move_circle.angular.z = 0.2
    # i = 0
    # while i <= request.repetitions :
    #     my_pub.publish(move_circle)
    #     rate.sleep()
    #     i=i+1
        
    # move_circle.linear.x = 0
    # move_circle.angular.z = 0
    # my_pub.publish(move_circle)
    rospy.loginfo("Finished service move_bb8_in_square_custom")
    
    response = BB8CustomServiceMessageResponse()
    for i in range(request.repetitions):
        move_side(request.side)
        move_corner()
        move_side(request.side)
        move_corner()
        move_side(request.side)
        move_corner()
        move_side(request.side)
        move_corner()
        stop()
    response.success = True
    return response # the service Response class, in this case EmptyResponse

rospy.init_node('service_move_bb8_in_square_custom_server') 
move_bb8_in_square_custom = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback) # create the Service called move_bb8_in_circle with the defined callback
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rate = rospy.Rate(1)
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin() # mantain the service open.

