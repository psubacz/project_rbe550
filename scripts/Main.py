##Subacz - RBE550 - Baxter Dual Arm Manipulator

## http://wiki.ros.org/ROS/Tutorials/CreatingPackage

## http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29


## Baxter API: http://api.rethinkrobotics.com/baxter_interface/html/index.html

## Examples: http://sdk.rethinkrobotics.com/wiki/Examples#Simulator

##Steps for success
##1.0 - Starting the Baxter Sim:
##     1.1 - Open a terminal and enter './baxter.sh sim'
##     1.2 - Next enter "roslaunch baxter_gazebo baxter_world.launch", it might take a few minutes be patient!!!
##     1.3 - (Optional) Test to make sure the sim is installed and running correcty, Open a new terminal
##     1.3.1 - "rosnode list",  should show similiar results as http://sdk.rethinkrobotics.com/wiki/Simulator_Architecture#Ros_Nodes
##     1.3.2 - "rostopic list", should show similiar results as http://sdk.rethinkrobotics.com/wiki/Simulator_Architecture#Ros_Topics
##     1.3.3 - "rostopic echo /robot/state",The print message should show:
##          enabled: False
##          stopped: False
##          error: False
##          estop_button: 0
##          estop_source: 0
##

## To enable the robot, enter "rosrun baxter_tools enable_robot.py -e"
## to disable the robot, enter "rosrun baxter_tools enable_robot.py -d"
import argparse
import os
import sys
import rospy

def main():
    # print("yeet")
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--state', const='state',
                        dest='actions', action='append_const',
                        help='Print current robot state')
    parser.add_argument('-e', '--enable', const='enable',
                        dest='actions', action='append_const',
                        help='Enable the robot')
    parser.add_argument('-d', '--disable', const='disable',
                        dest='actions', action='append_const',
                        help='Disable the robot')
    parser.add_argument('-r', '--reset', const='reset',
                        dest='actions', action='append_const',
                        help='Reset the robot')
    parser.add_argument('-S', '--stop', const='stop',
                        dest='actions', action='append_const',
                        help='Stop the robot')
    args = parser.parse_args(rospy.myargv()[1:])

    if args.actions == None:
        parser.print_usage()
        parser.exit(0, "No action defined")

    rospy.init_node('rsdk_robot_enable')
    rs = baxter_interface.RobotEnable(CHECK_VERSION)

    try:
        for act in args.actions:
            if act == 'state':
                print (rs.state())
            elif act == 'enable':
                rs.enable()
            elif act == 'disable':
                rs.disable()
            elif act == 'reset':
                rs.reset()
            elif act == 'stop':
                rs.stop()
    except Exception, e:
        rospy.logerr(e.strerror)

    return 0

if __name__ == '__main__':
    sys.exit(main())
    