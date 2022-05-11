#!/usr/bin/env python
import rospy
from open_manipulator_msgs.msg import *
from control_msgs.msg import FollowJointTrajectoryActionGoal

def callback(data):
    print("called")
    rospy.loginfo(data)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    goalPub = rospy.Publisher('/move_group/display_planned_path', FollowJointTrajectoryActionGoal, queue_size=20)
    rospy.Subscriber("/arm_controller/follow_joint_trajectory/result", FollowJointTrajectoryResult, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
