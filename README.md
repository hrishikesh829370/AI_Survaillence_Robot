# AI surveillance Robot


This project presents an AI-powered surveillance robot with a 2-wheel differential drive system and a caster for stability. The robot is 3D-printed for a customizable and potentially low-cost design.

## Key Features:

* **3D Printed Design:** The robot leverages 3D-printed parts, offering potential for customization and replicability.
* **Gazebo Simulation:** Initial development and testing are conducted within the Gazebo robot simulator. This facilitates safe experimentation and debugging . 
* **Computer Vision Optimization:** Bandwidth is optimized to ensure efficient processing for the robot's computer vision tasks. This optimization ensures smooth operation and real-time performance for the robot's vision system in.
* **Object Detection:** *The robot can identify specific objects within its field of view using computer vision algorithms. 
* **Line Following:** The robot can seamlessly detect and follow lines on a track, enabling autonomous navigation. This enables the robot to navigate predefined paths accurately.

Robot's Vision:
 ![ai_bot](https://github.com/hrishikesh829370/AI_Survaillence_Robot/assets/131910887/511fb011-dbbc-4049-9cb4-835c192d574c)

The robot successfully identifies an object in its field of view.

Line Following:

 ![line_following](https://github.com/hrishikesh829370/AI_Survaillence_Robot/assets/131910887/c3fd8b5b-ee67-44dc-809e-372f31f99f2b)

The robot detects and follows a line on the track accurately.

## Project Structure:

The project code is organized into the following directories and files:

```
├── launch
│   ├── gazebo.launch.py
│   ├── line_following.launch.py
│   ├── qr_maze.launch.py
│   ├── rviz.launch.py
│   └── surveillance_bot.launch.py
├── meshes
│   ├── base.dae
│   ├── caster_holder.dae
│   ├── caster_wheel.dae
│   ├── cover.dae
│   ├── left.png
│   ├── line_to_follow.dae
│   ├── maze.dae
│   ├── qr_codes.dae
│   ├── right.png
│   ├── robot.blend
│   ├── robot.blend1
│   ├── rpi_camera.dae
│   ├── stop.png
│   └── wheel.dae
├── models
│   ├── line_follow_model
│   │   ├── model.config
│   │   └── model.sdf
│   └── maze_qr_codes
│       ├── model.config
│       └── model.sdf
├── package.xml
├── resource
│   ├── aeroplane.jpg
│   ├── bus.jpg
│   ├── car.jpg
│   ├── left.png
│   ├── right.png
│   ├── stop.png
│   ├── vehicle.jpg
│   └── vision_rpi_bot
├── scripts
│   ├── model_test.py
│   └── qr_code.py
├── setup.cfg
├── setup.py
├── urdf
│   ├── vision_rpi_bot_lf.urdf
│   └── vision_rpi_bot.urdf
├── vision_rpi_bot
│   ├── __init__.py
│   ├── line_following_real.py
│   ├── line_following_sim.py
│   ├── publisher.py
│   ├── qr_maze_drive.py
│   ├── subscriber.py
│   └── surveillance_bot.py
└── worlds
    ├── lineFollow.world
    └── qr_maze.world

```

