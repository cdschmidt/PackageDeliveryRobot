#! /usr/bin/env python

from struct import pack
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import tf

rospy.init_node('turtle_tf_listener', anonymous=True)
listener = tf.TransformListener()
rate = rospy.Rate(10.0)
trans = 0
while not rospy.is_shutdown():
    try:
        (trans,rot) = listener.lookupTransform('camera_rgb_optical_frame', 'tag_1', rospy.Time(0))
        print(trans)
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        print(trans)
        continue

    rate.sleep()