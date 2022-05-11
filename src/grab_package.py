#! /usr/bin/env python

from multiprocessing.connection import wait
from operator import ge
from struct import pack
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import tf

def move_to_home_position():    
    joint_goal = group.get_current_joint_values()  
    joint_goal[0] = 0 
    joint_goal[1] = -1
    joint_goal[2] = .3
    joint_goal[3] = .7
    group.go(joint_goal, wait=True)
    group.stop()

def move_to_package():
    xyz = [0] * 3
    xyz[0] = trans[2] + .06
    xyz[1] = -trans[0]
    xyz[2] = -trans[1] + .1
    group.set_position_target(xyz)

    plan1 = group.plan()
    rospy.sleep(5)
    group.go(wait=True)

def open_grasper():
    joint_goal = gripper_group.get_current_joint_values()
    joint_goal[0] = .019
    gripper_group.go(joint_goal, wait=True)
    gripper_group.stop()
    return

def close_grasper():
    joint_goal = gripper_group.get_current_joint_values()
    joint_goal[0] = -.01
    gripper_group.go(joint_goal, wait=True)
    gripper_group.stop()
    rospy.sleep(1.0)
    return

moveit_commander.roscpp_initialize(sys.argv)
rospy.sleep(0.4)
rospy.init_node('move_group_python_interface', anonymous=True)
listener = tf.TransformListener()

rate = rospy.Rate(10.0)
trans = 0
while not rospy.is_shutdown():
    try:
        (trans,rot) = listener.lookupTransform('camera_rgb_optical_frame', 'tag_1', rospy.Time(0))
        print(trans[0])
        print(trans[1])
        print(trans[2])
        break
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        print("Transform not found")
        continue

    rate.sleep()


robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
rospy.sleep(0.1)
group = moveit_commander.MoveGroupCommander("arm")
gripper_group = moveit_commander.MoveGroupCommander("gripper")

display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)
rospy.sleep(0.1)


move_to_home_position()
open_grasper()
move_to_package()
close_grasper()

move_to_home_position()

moveit_commander.roscpp_shutdown()