# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/foxy/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

<<<<<<< HEAD
Answer: `source /opt/ros/foxy/setup.bash` sets up the environment such that ROS2 commands and dependencies are recognized. On the other hand, `source install/local_setup.bash` is meant for local dependencies, nodes, and packages that are defined 
or included by the user.

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: The queue_size argument controls how many messages can be stored in the queue for the publisher and subscribers. A larger queue size means that more messages can be stored, which allows for faster communication without blocking.
If the max queue sized is reached, the oldest messages could be dropped, or if the publisher/subscriber process is blocking, the message will not be added to the queue until there is space.

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: If ros2 launch is in the same directory as the launch file, (I think) the changes are immediately recognized, so there is no need to call colcon build again, but the same is not true if you are calling colcon build outside of the 
directory where the launch file is defined.
>>>>>>> b4a39f2 (Initial commit)
