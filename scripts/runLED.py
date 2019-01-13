#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import roslib
import rospy
from std_msgs.msg import String
import time
import subprocess, os

def Lchika(msg):

    if msg.data == "1":
        os.system("echo 1 > /dev/myled0")
    elif msg.data == "2":
        os.system("echo 2 > /dev/myled0")
    else:
        os.system("echo 0 > /dev/myled0")


if __name__ == '__main__':
    ### init io port ###
    rospy.init_node('ledflash')
    rospy.Subscriber('keys', String, Lchika)

    rospy.spin()

    os.system("echo 0 > /dev/myled0")
    print '\rStopped'
