#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

def move(side: float, repetitions: int):
    rospy.wait_for_service('/move_bb8_in_square_custom')
    try:
        move_service = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
        resp1 = move_service(side, repetitions)
        return resp1.success
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
rospy.init_node('service_move_bb8_in_square_custom_client') 

laps = [(1,7),(1.5,5),(2,3)]
for i in laps:
    print(i)
    print(move(i[0],i[1]))



# rospy.spin() # mantain the service open.

