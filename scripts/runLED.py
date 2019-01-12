#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import roslib
import rospy
import time
import subprocess, os

#main
if __name__ == '__main__':
    ### init io port ###
    rospy.init_node('ledflash')

    while not rospy.is_shutdown():

        os.system("echo 1 > /dev/myled0")
        time.sleep(1)
        os.system("echo 2 > /dev/myled0")
        time.sleep(1)

        
    os.system("echo 0 > /dev/myled0")
    print '\rStopped'
