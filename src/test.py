#!/usr/bin/env python
import sys
import rospy
from open_manipulator_msgs.srv import *

def set_position_client(x, y, z, time):
    service_name = 'goal_task_space_path'
    print('Waiting for service!')
    rospy.wait_for_service(service_name)
    print('Not Waiting for service!')

    try:
        set_position = rospy.ServiceProxy(service_name, SetKinematicsPose)
        arg = SetKinematicsPoseRequest()
        arg.end_effector_name = 'gripper'
        arg.kinematics_pose.pose.position.x = 0.194
        arg.kinematics_pose.pose.position.y = 0.000
        arg.kinematics_pose.pose.position.z = 0.304
        # arg.kinematics_pose.pose.orientation.w = 1
        
        arg.kinematics_pose.pose.orientation.x = 0
        arg.kinematics_pose.pose.orientation.y = 0
        arg.kinematics_pose.pose.orientation.z = 0
        arg.kinematics_pose.pose.orientation.w = 1
        arg.kinematics_pose.tolerance = 100
        arg.kinematics_pose
        arg.path_time = time
        print('Called service!')
        resp1 = set_position(arg)
        print('Service done!')
        return resp1
    except:
        print("error")
        

def usage():
    return "%s [x y z]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        z = float(sys.argv[3])
        time = float(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting [%s, %s, %s]"%(x, y, z))
    response = set_position_client(x, y, z, time)
    print("[%s %s %s] returns [%s]"%(x, y, z, response))