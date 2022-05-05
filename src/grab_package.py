#! /usr/bin/env python

from struct import pack
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import tf


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface', anonymous=True)
listener = tf.TransformListener()

package_location = 0
rate = rospy.Rate(10.0)
trans = 0
while not rospy.is_shutdown():
    try:
        (trans,rot) = listener.lookupTransform('camera_rgb_optical_frame', 'tag_1', rospy.Time(0))
        print(trans[0] + .1191)
        print(trans[1] + .064)
        print(trans[2] - .325)
        break
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        print(trans)
        continue

    rate.sleep()


robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

print ("Robot Groups:")
print (robot.get_group_names())
print ("Current Joint Values:")
print (group.get_current_joint_values())
print ("Current Pose:")
print (group.get_current_pose())


pose_target = geometry_msgs.msg.Pose()
# pose_target.orientation.w = 1.0
# pose_target.orientation.x = -1.174
# pose_target.orientation.y = 2.588
# pose_target.orientation.z = 4.538
# pose_target.position.x = trans[0] + .1191
# pose_target.position.y = trans[1] + .064
# pose_target.position.z = trans[2] - .325
pose_target.position.x = 0.146
pose_target.position.y = 1.143
pose_target.position.z = 0.345
group.set_pose_target(pose_target)

plan1 = group.plan()

rospy.sleep(5)

group.go(wait=True)

moveit_commander.roscpp_shutdown()