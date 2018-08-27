#### A brief survey : ai in robotics


-----------
> #### Contents

- [Timeline](#timeline)
- [Misc](#misc)
- [Robotic concepts](#robotics-concepts)
  - [ROS](#ros)
  - [Kinematics](#kinematics)
  - [Perception](#perception)
  - [Controls](#controls) 
  - [DL for Robotics](#dl-for-robotics)
  - [SLAM](#slam)
  - [Reinforcement Learning for Robotics](#reinforcement-learning-for-robotics)
  - [Path Planning and Navigation](#path-planning-and-navigation)
- [Libraries](#libraries)
- [Drones](#drones)
- [Automation](#automation)
- [Manufacturing](#manufacturing)
- [Applications](#applications)
- [Literature Review](#literature-review)
- [Startups](#startups)
- [Appendix](#appendix)


[Back to top](#contents)

-----------------

### Timeline

[Back to top](#contents)

- [Outline of robotics](https://en.wikipedia.org/wiki/Outline_of_robotics)
- [History of robots](https://en.wikipedia.org/wiki/History_of_robots)
- [Infographic: The evolution of robotic](https://www.digitalpulse.pwc.com.au/infographic-evolution-robots-ai/)
- [ros history](https://en.wikipedia.org/wiki/Robot_Operating_System)
- [Robotics_middleware](https://en.wikipedia.org/wiki/Robotics_middleware)
- [Outline of automation](https://en.wikipedia.org/wiki/Outline_of_automation)
- [Unmanned aerial vehicle](https://en.wikipedia.org/wiki/Unmanned_aerial_vehicle)
- [List of unmanned aerial vehicle applications](https://en.wikipedia.org/wiki/List_of_unmanned_aerial_vehicle_applications)

----------------------------

### Misc

[Back to top](#contents)

- [sTANFORD: Artificial Intelligence and Economic Growth
](https://web.stanford.edu/~chadj/AI.pdf)
- [On AI and Robotics
Developing policy for the Fourth Industrial Revolution](https://policyatmanchester.shorthandstories.com/on_ai_and_robotics/index.html)
- [deloitte: AI, robotics, and automation: Put humans in the loop](https://www2.deloitte.com/insights/us/en/focus/human-capital-trends/2018/ai-robotics-intelligent-machines.html)
- [Views of AI, robots, and automation based on internet search data](https://www.brookings.edu/research/views-of-ai-robots-and-automation-based-on-internet-search-data/)
- [The Evolution Of AI And Robotics Will Be Amazing (And Painful)](https://www.forbes.com/sites/forbestechcouncil/2017/12/28/the-evolution-of-ai-and-robotics-will-be-amazing-and-painful/#272396af4597)
- [Artificial Intelligence And Robotics Will Lead To More Jobs, If We Do It Right](https://www.forbes.com/sites/forbesbusinessdevelopmentcouncil/2018/03/08/artificial-intelligence-and-robotics-will-lead-to-more-jobs-if-we-do-it-right/#4be2eec24190)
- [Global Competition Rises for AI Industrial Robotics](https://www.techemergence.com/global-competition-rises-ai-industrial-robotics/)
- [What is the role of Artificial Intelligence (AI) in Robotics?](https://www.quora.com/What-is-the-role-of-Artificial-Intelligence-AI-in-Robotics)
- [Infographics show jobs most likely to be lost to robots](https://bigthink.com/robby-berman/infographics-show-jobs-most-likely-to-be-lost-to-robots)
- [Stanford: Introduction to Robotics](https://see.stanford.edu/Course/CS223A)
- [Robot Hall of Fame](https://en.wikipedia.org/wiki/Robot_Hall_of_Fame)
- [Competitions in artificial intelligence](https://en.wikipedia.org/wiki/Competitions_and_prizes_in_artificial_intelligence)
- [MIT-TR: All Robotics stories](https://www.technologyreview.com/c/robotics/)
- [spectrum.ieee.robotics](https://spectrum.ieee.org/robotics)
- [letsmakerobots](https://www.robotshop.com/letsmakerobots/)
- [How do I learn Robotics?](https://www.quora.com/Whats-the-best-way-to-start-learning-robotics?redirected_qid=770465)
- [Free NXT Lego MindStorms NXT-G code tutorials](http://www.drgraeme.net/DrGraeme-free-NXT-G-tutorials/ChV4.htm)
- [47 Programmable Robotics Kits](http://www.intorobotics.com/47-programmable-robotic-kits/)
- [Robotics Couses](http://wiki.ros.org/Courses)
- [ETH Zurich: Institute of Robotics and Intelligent Systems](http://www.iris.ethz.ch/)
- [robotigniteacademy](https://www.robotigniteacademy.com/en/)
- [EDX Robotics courses](https://www.edx.org/course?search_query=robotics)
- [Coursera: Robotics Specialization](https://www.coursera.org/specializations/robotics)
- [Udacity ND: Become A Robotics Software Engineer](https://in.udacity.com/course/robotics-software-engineer--nd209)
- [Udacity ND: Flying Car](https://in.udacity.com/course/flying-car-nanodegree--nd787)
- [Imperial Robotics](http://www.imperial.ac.uk/robotics/)
- [societyofrobots](http://www.societyofrobots.com/)
- [ijrr](http://www.ijrr.org/#)
- [ieee-ras](http://www.ieee-ras.org/)
- [ri.cmu](https://www.ri.cmu.edu/research/)
- [Advanced Robotics: Autonomous
Mobile Robots](https://www.iitk.ac.in/tkic/workshop/robotics/ppt/day5/arshad.pdf)
- [Artificial Intelligence Technology Landscape infographic](https://www.callaghaninnovation.govt.nz/sites/all/files/callaghan-innovation-infographic-artificial-intelligence.pdf)
- [10 Charts That Will Change Your Perspective On Artificial Intelligence's Growth](https://www.forbes.com/sites/louiscolumbus/2018/01/12/10-charts-that-will-change-your-perspective-on-artificial-intelligences-growth/#432485624758)

-------------


### Robotic concepts

#### ROS

[Back to top](#contents)

- [ROS core stacks](https://github.com/ros)
- [ROS package list](http://www.ros.org/browse/list.php)
- [Find a Robot by tags](https://robots.ros.org/tags/)
- [wiki.ros](http://wiki.ros.org/)
- [Core ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
- [A Gentle Introduction to ROS](https://cse.sc.edu/~jokane/agitr/)
- [89-685: Introduction to Robotics](http://u.cs.biu.ac.il/~yehoshr1/89-685/)


<p>ROS areas include:
</p>
<ul><li>a master coordination node</li>
<li>publishing or subscribing to data streams: images, stereo, laser, control, actuator, contact ...</li>
<li>multiplexing information</li>
<li>node creation and destruction</li>
<li>nodes are seamlessly distributed, allowing distributed operation over multi-core, multi-processor, GPUs and clusters</li>
<li>logging</li>
<li>parameter server</li>
<li>test systems</li></ul>
<p>ROS package application areas will include:
</p>
<ul><li>perception</li>
<li>object identification</li>
<li><a href="https://en.wikipedia.org/wiki/Segmentation_(image_processing)" class="mw-redirect" title="Segmentation (image processing)">segmentation</a> and recognition</li>
<li><a href="https://en.wikipedia.org/wiki/Facial_recognition_system" title="Facial recognition system">Face recognition</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gesture_recognition" title="Gesture recognition">gesture recognition</a></li>
<li><a href="https://en.wikipedia.org/wiki/Video_tracking" title="Video tracking">motion tracking</a></li>
<li><a href="https://en.wikipedia.org/wiki/Egomotion" class="mw-redirect" title="Egomotion">egomotion</a></li>
<li><a href="/w/index.php?title=Motion_understanding&amp;action=edit&amp;redlink=1" class="new" title="Motion understanding (page does not exist)">motion understanding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Structure_from_motion" title="Structure from motion">structure from motion</a> (SFM)</li>
<li><a href="https://en.wikipedia.org/wiki/Stereopsis" title="Stereopsis">stereo vision</a>: depth perception via two cameras</li>
<li>motion</li>
<li><a href="https://en.wikipedia.org/wiki/Mobile_robotics" class="mw-redirect" title="Mobile robotics">mobile robotics</a></li>
<li>control</li>
<li>planning</li>
<li>grasping</li></ul>


---------------

#### Kinematics

[Back to top](#contents)

- [Kinematics and Dynamics](https://people.mech.kuleuven.be/~bruyninc/robotics/H06U9B/20170928-KinDyn-nup.pdf)
- [11KinematicsRobot](http://people.ciirc.cvut.cz/~hlavac/TeachPresEn/51Robotics/11KinematicsRobot.pdf)
- [robot-kinematics](https://www.slideshare.net/DamianGordon1/robot-kinematics)
- [Robot Kinematics:
 Forward and Inverse Kinematics]()
- [A Deep Reinforcement Learning Approach for
Dynamically Stable Inverse Kinematics of
Humanoid Robots](https://arxiv.org/pdf/1801.10425.pdf)
- [A Survey of Motion Planning and Control
Techniques for Self-driving Urban Vehicles](https://arxiv.org/pdf/1604.07446.pdf)
- [Kinematic Modeling of Robotic Manipulators](https://www.researchgate.net/publication/282648910_Kinematic_Modeling_of_Robotic_Manipulators)

-------------------

#### Perception

[Back to top](#contents)

- [ETH ZURICH : Perception: Sensors
Autonomous Mobile Robots](https://www.ethz.ch/content/dam/ethz/special-interest/mavt/robotics-n-intelligent-systems/asl-dam/documents/lectures/autonomous_mobile_robots/spring-2015/04_-_Perception_I_-_Sensors.pdf)
- [ori.ox.ac.uk.perception](http://ori.ox.ac.uk/theme/perception/)
- [Robotics: Perception](https://www.coursera.org/learn/robotics-perception)
- [Perception & Sensing
in Robotic Mobility and Manipulation](https://see.stanford.edu/materials/aiircs223a/handout5_Robots_and_Vision.pdf)
- [onrobot.com](https://onrobot.com/)
- [MIT: Perception and Perspective in Robotic](https://people.csail.mit.edu/paulfitz/pub/cogsci03perception.pdf)
- [Sensing/Perception](https://www.cpp.edu/~ftang/courses/CS521/notes/sensing.pdf)
- [Touch and tactile perception
for robots](http://people.ciirc.cvut.cz/~hlavac/TeachPresEn/55AutonomRobotics/140TactileRobotics.pdf)
- [Cognitive architecture for robot perception and learning
based on human-robot interaction](http://vislab.isr.ist.utl.pt/wp-content/uploads/2015/10/IROS2015_workshop_Uriel_Martinez.pdf)
- [Revisiting Active Perception](https://arxiv.org/ftp/arxiv/papers/1603/1603.02729.pdf)
- [Perception: Sensors for Mobile Robots](http://web.eecs.utk.edu/~leparker/Courses/CS594-fall08/Lectures/Sept-16-Perception-1.pdf)
- [Intelligent perception and control for space robotics](http://web.cs.ucla.edu/~dt/papers/mva08/mva08.pdf)

------------

#### Controls

[Back to top](#contents)


- [Control in Robotics](http://ieeecss.org/sites/ieeecss.org/files/documents/IoCT-Part1-04Robotics.pdf)
- [Robot
Manipulator
Control
Theory and Practice](http://www.robot.bmstu.ru/files/books/Robot%20Manipulator%20Control%20Theory%20and%20Practice%20-%20Frank%20L.Lewis.pdf)
- [Robot Contro](https://see.stanford.edu/materials/aiircs223a/handout8_Control.pdf)
- [Robot Dynamics and Control](http://home.deib.polimi.it/gini/robot/docs/spong.pdf)
- [https://pdfs.semanticscholar.org/5bb5/ed04e2d2953b80391bc8f14c680f783ea0c4.pdf](https://pdfs.semanticscholar.org/5bb5/ed04e2d2953b80391bc8f14c680f783ea0c4.pdf)
- [Robot Dynamics and
Control](https://www.cds.caltech.edu/~murray/books/MLS/pdf/mls94-manipdyn_v1_2.pdf)
- [Introduction to Robotics](http://engineering.nyu.edu/mechatronics/smart/Archive/intro_to_rob/Intro2Robotics.pdf)
- [MOTION PLANNING AND CONTROL](https://nptel.ac.in/courses/112108093/module7/lecture.pdf)
- [Handbook-mcontrol](https://users.dimi.uniud.it/~antonio.dangelo/Robotica/2012/helper/Handbook-mcontrol.pdf)
- [Control Theory](https://ipvs.informatik.uni-stuttgart.de/mlr/marc/teaching/13-Robotics/08-controlTheory.pdf)


--------------

#### DL for Robotics

[Back to top](#contents)

- [Deepmind: Deep Learning for Robots](http://raiahadsell.com/uploads/3/6/4/2/36428762/erf2017_keynote_talk.pdf)
- [Deep Learning for Robotics](https://simons.berkeley.edu/sites/default/files/docs/5928/simonsmlbootcamp2017.pdf)
- [stanford: deep learning for robotics](https://www.cs.stanford.edu/people/asaxena/papers/ianlenz_phdthesis.pdf)
- [Deep Learning in Robotics: A Review of Recent Research](https://arxiv.org/ftp/arxiv/papers/1707/1707.07217.pdf)
- [Deep Learning for Robotics - Prof. Pieter Abbeel - NIPS 2017 Keynote](https://www.youtube.com/watch?v=TyOooJC_bLY)
- [The Limits and Potentials of Deep Learning for Robotics](https://arxiv.org/pdf/1804.06557.pdf)
- [NVIDIA’s Deep Learning AI Trains Robots to Copy and Execute Human Actions](https://www.analyticsvidhya.com/blog/2018/05/nvidias-deep-learning-ai-trains-robots-to-copy-and-execute-human-actions/)
- [Deep-learning in Mobile Robotics - from Perception to Control Systems: A Survey on Why and Why not](https://www.researchgate.net/publication/311805526_Deep-learning_in_Mobile_Robotics_-_from_Perception_to_Control_Systems_A_Survey_on_Why_and_Why_not)
- [Machine Learning Application in Robotics](https://www.cs.rpi.edu/twiki/pub/RoboticsWeb/ReadingGroup/ML-Robotics.pdf)
- [Robot Learning - Three case studies in
Robotics and Machine Learning
](https://pdfs.semanticscholar.org/6266/a91ab2d02a1d3afda8b848ecf276757ed7f7.pdf)
- [Intel nervana: Deep Learning for Robotics](https://www.slideshare.net/nervanasys/deep-learning-for-robotics)
- [Statement on Artificial
Intelligence,
Robotics and
‘Autonomous’
Systems 2018](http://ec.europa.eu/research/ege/pdf/ege_ai_statement_2018.pdf)
- [Machine learning powers
autonomous industrial systems ](http://www.ti.com/lit/wp/sszy032/sszy032.pdf)
- [Deep	Learning	for	Robotics
Pieter	Abbeel](https://orfe.princeton.edu/~alaink/SmartDrivingCars/PDFs/2017_12_xx_NIPS-keynote-final.pdf)



-------------

#### SLAM

[Back to top](#contents)

- [Teaching Robots Presence: What You Need to Know About SLAM](https://blog.cometlabs.io/teaching-robots-presence-what-you-need-to-know-about-slam-9bf0ca037553)
- [Robotic Mapping: Simultaneous Localization and Mapping (SLAM)](https://www.gislounge.com/robotic-mapping-simultaneous-localization-and-mapping-slam/)
- [What Does The Future Hold For SLAM Robotics?](https://www.forbes.com/sites/quora/2017/12/22/what-does-the-future-hold-for-slam-robotics/#59ed7dfd1856)
- [simulations](http://blogofrog.com/tag/simulations.html)
- [Robotic mapping](https://en.wikipedia.org/wiki/Robotic_mapping)
- [Matlab Toolbox of Kalman Filtering applied to Simultaneous Localization and Mapping](http://eia.udg.es/~qsalvi/Slam.zip)
- [Simultaneous localization and mapping](https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping)
- [The Cumulative Levels of SLAM Competence](https://medium.com/slamcore-blog/the-cumulative-levels-of-slam-competence-5576f33c1c2a)
- [Probabilistic Robotics](http://www.probabilistic-robotics.org/)
- [SLAM for Dummies ](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-412j-cognitive-robotics-spring-2005/projects/1aslam_blas_repo.pdf)
- [Andrew Davison: Research](http://www.doc.ic.ac.uk/~ajd/index.html)
- [openslam](https://openslam-org.github.io/)
- [FootSLAM and PlaceSLAM ](https://web.archive.org/web/20120313064730/http://www.kn-s.dlr.de/indoornav/footslam_video.html)
- [List of SLAM Methods](https://en.wikipedia.org/wiki/List_of_SLAM_Methods)
- [Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter)
- [Online demo of the Kalman Filter](http://www.data-assimilation.net/Tools/AssimDemo/?method=KF)
- [The Kalman Filter](http://www.cs.unc.edu/~welch/kalman/)
- [Design and use Kalman filters in MATLAB and Simulink](https://in.mathworks.com/discovery/kalman-filter.html)
- [An Introduction to the Kalman Filter](http://www.cs.unc.edu/~tracker/media/pdf/SIGGRAPH2001_CoursePack_08.pdf)
- [How a Kalman filter works, in pictures](http://www.bzarg.com/p/how-a-kalman-filter-works-in-pictures/)


![SLAM_Data_Flow](https://software.intel.com/sites/products/realsense/slam/SLAM_Data_Flow.PNG)

![11409_LT_Mapping](https://www.machinedesign.com/sites/machinedesign.com/files/uploads/2013/09/11409_LT_Mapping-And.jpg)

-----------------

#### Reinforcement Learning for Robotics

[Back to top](#contents)

![landscape](https://github.com/tangzhenyu/Reinforcement-Learning-in-Robotics/blob/master/images/landscape.jpeg)


- [Reinforcement-Learning-in-Robotics](https://github.com/tangzhenyu/Reinforcement-Learning-in-Robotics)
- [Reinforcement learning in robotics](https://vmayoral.github.io/robots,/ai,/deep/learning,/rl,/reinforcement/learning/2016/07/06/rl-intro/)
- [CMU: Reinforcement Learning in Robotics: A Survey](https://www.ri.cmu.edu/publications/reinforcement-learning-in-robotics-a-survey/)
- [Reinforcement Learning in Robotics:
A Survey](https://www.ias.informatik.tu-darmstadt.de/uploads/Publications/Kober_IJRR_2013.pdf)
- [Making a robot learn how to move, part 2 – reinforcement learning in the real, wild world](https://towardsdatascience.com/making-a-robot-learn-how-to-move-part-2-reinforcement-learning-in-the-real-wild-world-9427da7b9b21)
- [Deep Reinforcement Learning for Robotics](http://www.fujitsu.com/us/Images/Panel3_Pieter_Abbeel.pdf)
- [Google: Scalable Deep Reinforcement Learning for Robotic Manipulation](https://ai.googleblog.com/2018/06/scalable-deep-reinforcement-learning.html)
- [Google X’s Deep Reinforcement Learning in Robotics using Vision](https://hackernoon.com/google-xs-deep-reinforcement-learning-in-robotics-using-vision-7a78e87ab171)
- [Overview on Reinforcement Learning for
Robotics](https://openreview.net/pdf?id=rkNzJ4m0-)
- [How Deep Reinforcement Learning Will Make Robots Smarter](https://www.forbes.com/sites/danielnewman/2017/05/11/how-deep-reinforcement-learning-will-make-robots-smarter/#2cd08bdb433a)
- [NVIDIA Webinar — Deep Reinforcement Learning in Robotics with NVIDIA Jetson](https://devtalk.nvidia.com/default/topic/1035408/jetson-tx1/nvidia-webinar-mdash-deep-reinforcement-learning-in-robotics-with-nvidia-jetson/)


------------

#### Path Planning and Navigation

[Back to top](#contents)

- [Planning algorithms](http://planning.cs.uiuc.edu/)
- [Navigation and path planning for robotics](https://pdfs.semanticscholar.org/ddca/e7df6b735b9670ef708acc3cb879d2a0bbad.pdf)
- [Robot Motion Planning](http://ais.informatik.uni-freiburg.de/teaching/ss11/robotics/slides/18-robot-motion-planning.pdf)
- [Reflections on Designing a Virtual Highway Path Planner Part 1](https://medium.com/@mithi/reflections-on-designing-a-virtual-highway-path-planner-part-1-3-937259164650)
- [Reflections on Designing a Virtual Highway Path Planner Part 2](https://medium.com/@mithi/reflections-on-designing-a-virtual-highway-path-planner-part-2-3-392bc6cf11e7)
- [Reflections on Designing a Virtual Highway Path Planner Part 3](https://medium.com/@mithi/reflections-on-designing-a-virtual-highway-path-planner-part-3-3-a36bf629d239)
- [Advanced Robotics
Path Planning & Navigation](http://www.ist.tugraz.at/steinbauer_mediawiki/images/8/86/Ar13_5_path_planning_navigation.pdf)
- [Navigation Meshes and Real-Time Dynamic Planning for Virtual Worlds](http://graphics.ucmerced.edu/papers/14-sig-navplan-s.pdf)
- [Path Planning Algorithm in Complex
Environment: A Survey](http://tost.unise.org/pdfs/vol3/no1/3131_40.pdf)
- [Advancement in navigational path planning of robots
using various artificial and computing techniques](http://medcraveonline.com/IRATJ/IRATJ-04-00109.pdf)
- [A survey on path planning techniques for autonomous
mobilerobots](http://www.iosrjournals.org/iosr-jmce/papers/ICAET-2014/me/volume-4/16.pdf)
- [Multi-Robot Path Planning](https://www.cpp.edu/~ftang/courses/CS599-DI/notes/path%20planning.pdf)
- [Autonomous Path Planning and Navigation of a Mobile Robot
with Multi-Sensors based on Fuzzy Logic in Dynamic
Environment](https://www.cscjournals.org/manuscript/Journals/IJRA/Volume7/Issue1/IJRA-161.pdf)
- [Evolving A Diverse Collection of Robot Path
Planning Problems](http://eldar.mathstat.uoguelph.ca/dashlock/eprints/DPP-CEC-06.pdf)
- [PATH AND TRAJECTORY PLANNING](http://www.ene.ttu.ee/elektriajamid/oppeinfo/materjal/AAR0040/03_Robotics.pdf)
- [Localization and Mapping with Autonomous Robots](https://www.ru.nl/publish/pages/769526/master_thesis_benjamin_mader.pdf)

-------------

### Libraries

[Back to top](#contents)

- [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) : Python sample codes for robotics algorithms. 
- [highway-path-planning](https://github.com/mithi/highway-path-planning) : path-planning pipeline to navigate a car safely around a virtual highway with other traffic.
- [SLAM_AND_PATH_PLANNING_ALGORITHMS](https://github.com/jfrascon/SLAM_AND_PATH_PLANNING_ALGORITHMS) : 
- [Electric-Vehicle-Route-Planning-on-Google-Map-Reinforcement-Learning](https://github.com/Dungyichao/Electric-Vehicle-Route-Planning-on-Google-Map-Reinforcement-Learning) : User can set up destination for any agent to navigate on Google Map and learn the best route for the agent based on its current condition and the traffic. Our result is 10% less energy consumption than the route provided by Google map
- [scikit-kinematics](https://github.com/thomas-haslwanter/scikit-kinematics) : Python functions for working with 3D kinematics.
- [jrl-umi3218/Tasks](https://github.com/jrl-umi3218/Tasks) - Tasks is library for real time control of robots and kinematic trees using constrained optimization.
- [jrl-umi3218/RBDyn](https://github.com/jrl-umi3218/RBDyn) - RBDyn provides a set of classes and functions to model the dynamics of rigid body systems.
- [ceres-solver](https://github.com/ceres-solver/ceres-solver) - Solve Non-linear Least Squares problems with bounds constraints and general unconstrained optimization problems. Used in production at Google since 2010.
- [orocos_kinematics_dynamics](https://github.com/orocos/orocos_kinematics_dynamics) - Orocos Kinematics and Dynamics C++ library.
- [flexible-collsion-library](https://github.com/flexible-collision-library/fcl) - Performs three types of proximity queries on a pair of geometric models composed of triangles, integrated with ROS. 
- [robot_calibration](https://github.com/mikeferguson/robot_calibration) - generic robot kinematics calibration for ROS
- [jetson-reinforcement](https://github.com/dusty-nv/jetson-reinforcement)
- [Introduction-to-Autonomous-Robots](https://github.com/correll/Introduction-to-Autonomous-Robots/releases/tag/v1.9.1)
- [AutonomousDrivingCookbook](https://github.com/Microsoft/AutonomousDrivingCookbook)
- [NVIDIA-Jetson/redtail](https://github.com/NVIDIA-Jetson/redtail) : Perception and AI components for autonomous mobile robotics.
- [jetson-reinforcement c++](https://github.com/dusty-nv/jetson-reinforcement) : Deep reinforcement learning GPU libraries for NVIDIA Jetson with PyTorch, OpenAI Gym, and Gazebo robotics simulator.

SLAM

- [cartographer](https://github.com/googlecartographer/cartographer) : Cartographer is a system that provides real-time simultaneous localization and mapping (SLAM) in 2D and 3D across multiple platforms and sensor configurations.
- [slambook](https://github.com/gaoxiang12/slambook) : 
- [awesome-slam](https://github.com/kanster/awesome-slam) : 
- [slam](https://github.com/jslee02/awesome-robotics-libraries#slam) : 
- [awesome-SLAM-list](https://github.com/OpenSLAM/awesome-SLAM-list) : 


-------------
### Drones

[Back to top](#contents)

- [how_do_drones_work](https://github.com/tizianofiorenzani/how_do_drones_work)
- [Drones: The Complete Guide | WIRED](https://www.wired.com/story/guide-drones/)
- [TED: A collection of TED Talks (and more) on the topic of drones.](https://www.ted.com/topics/drones)
- [Times Special Report: THE DRONE AGE](http://time.com/collection/drones/)
- [AI and drones are being used to control construction projects](https://www.technologyreview.com/the-download/610545/ai-and-drones-are-being-used-to-control-construction-projects/)
- [5 Ways AI And Drones Are Opening Up A Billion Dollar Market](https://www.forbes.com/sites/mnewlands/2017/08/10/5-ways-ai-and-drones-are-opening-up-a-billion-dollar-market/#535e5da61348)
- [The Future of Drones in Artificial Intelligence](https://dzone.com/articles/the-future-of-drones-in-artificial-intelligence)
- [AI-powered autonomous drone could bring new capabilities to agriculture, logistics, more](https://www.techrepublic.com/article/scientists-create-miniature-drone-that-can-fly-itself-with-ai/)
- [Scientists Develop AI-Enabled Drones That Can Detect Violence in Crowds](https://interestingengineering.com/scientists-develop-ai-enabled-drones-that-can-detect-violence-in-crowds)
- [Artificial Intelligence Gives Drones Abilities We’ve Only Dreamed About](http://blogs.discovermagazine.com/drone360/2017/12/04/artificial-intelligence-drones-abilities-dreamed-about/#.W32Nvugzbcs)
- [airoboticsdrones](https://www.airoboticsdrones.com/)
- [12 Ways AI is Shaping the Drone Industry](https://dronelife.com/2018/07/06/12-ways-ai-is-shaping-the-drone-industry/)
- [The Development of Drones with Artificial Intelligence](https://ems.de/en/mainzer-manager/the-development-of-drones-with-artificial-intelligence/)
- [Pentagon makes massive new AI push for tanks, ships, weapons, drones and networks](http://www.foxnews.com/tech/2018/07/19/pentagon-makes-massive-new-ai-push-for-tanks-ships-weapons-drones-and-networks.html)
- [Cities and Drones](https://web.archive.org/web/20160909214339/http://www.nlc.org/Documents/Find%20City%20Solutions/City-Solutions-and-Applied-Research/NLC%20Drone%20Report.pdf)
- [diydrones](https://diydrones.com/)
- [Robotics: Aerial Robotics](https://www.coursera.org/learn/robotics-flight)
- [Autonomous Navigation for Flying Robots](https://www.edx.org/course/autonomous-navigation-flying-robots-tumx-autonavx-0)
- [Drone Knowledge](https://www.dronezon.com/category/learn-about-drones-quadcopters/)
- [Drone Courses](https://www.udemy.com/topic/drone/)
- [DRONE RESOURCES](https://airdronecraze.com/drone-resources/)
- [The Top Drone News Sites of 2015](https://uavcoach.com/drone-news/)
- [awesome-drone](https://github.com/Pana/awesome-drone)
- [awesome-drones](https://github.com/janesmae/awesome-drones)
- [How Do Drones Work?](http://www.westcoastplacer.com/how-do-drones-work/)
- [Technology: Drones](https://4h.extension.illinois.edu/members/projects/technology-drones)
- [Beginners guide to drone autopilots (flight controllers) and how they work](https://www.dronetrest.com/t/beginners-guide-to-drone-autopilots-flight-controllers-and-how-they-work/1380)
- [List of unmanned aerial vehicles](https://en.wikipedia.org/wiki/List_of_unmanned_aerial_vehicles)


-------------

### Automation

[Back to top](#contents)

- [automation-ai](https://www.computerscienceonline.org/cutting-edge/automation-ai/)
- [Automation](https://en.wikipedia.org/wiki/Automation)
- [Why Are There Still So Many Jobs?
The History and Future of Workplace
Automation†](https://economics.mit.edu/files/11563)
- [What is the difference between Automation and Artificial Intelligence?](https://www.quora.com/What-is-the-difference-between-Automation-and-Artificial-Intelligence)
- [5 Applications & Benefits of Artificial Intelligence in Automation](https://www.newgenapps.com/blog/artificial-intelligence-in-automation-applications-benefits-uses)
- [Deloitte: https://www.newgenapps.com/blog/artificial-intelligence-in-automation-applications-benefits-uses](https://www2.deloitte.com/content/dam/Deloitte/lu/Documents/operations/lu-intelligent-automation-business-world.pdf)
- [Artificial Intelligence and Automation](https://link.springer.com/chapter/10.1007/978-3-540-78831-7_14)
- [How AI is Already Changing Test Automation: 6 Examples](https://www.joecolantonio.com/how-ai-is-changing-test-automation/)
- [What’s now and next in analytics, AI, and automation](https://www.mckinsey.com/featured-insights/digital-disruption/whats-now-and-next-in-analytics-ai-and-automation)
- [So, What’s the Real Difference Between AI and Automation?](https://medium.com/@daveevansap/so-whats-the-real-difference-between-ai-and-automation-3c8bbf6b8f4b)
- [The Real Story of Automation Beginning with One Simple Chart](https://medium.com/basic-income/the-real-story-of-automation-beginning-with-one-simple-chart-8b95f9bad71b)
- [Best Automation Testing Tools for 2018 (Top 10 reviews)](https://medium.com/@briananderson2209/best-automation-testing-tools-for-2018-top-10-reviews-8a4a19f664d2)
- [Automation and the “Creation of a New World”](https://hackernoon.com/automation-and-the-creation-of-a-new-world-494996b66932)
- [Seize The Means Of Automation](https://medium.com/@caityjohnstone/seize-the-means-of-automation-88811b800d9c)
- [Google cofounder Sergey Brin talks about AI and automation](https://medium.freecodecamp.org/google-cofounder-sergey-brin-talks-about-ai-and-automation-afd4075fada)
- [The Next Phase of Marketing Automation: Why HubSpot is Acquiring Motion AI](https://medium.com/@HubSpot/the-next-phase-of-marketing-automation-why-hubspot-is-acquiring-motion-ai-b5e6adbffe4d)
- [We Are All Creatives: A Manifesto of Humanity in the Age of Automation](https://medium.com/@MikeSturm/we-are-all-creatives-a-manifesto-of-humanity-in-the-age-of-automation-5f1ef55804f4)
- [An Argument for Automation](https://blog.kentcdodds.com/an-argument-for-automation-fce8394c14e2)
- [What is Codeless Automation Testing and why it is the Future!](https://medium.com/@sarahelson81/what-is-codeless-automation-testing-and-why-it-is-the-future-bad9e8f9b8af)
- [Why Automation Testing Is Important In Agile Development?](https://medium.com/@sarahelson81/why-automation-testing-is-important-in-agile-development-919e8f185c06)
- [Top 15 Interview Questions For Test Automation Engineers](https://medium.com/@sarahelson81/top-15-interview-questions-for-test-automation-engineers-e6c20842910)
- [Automation Is the Next Phase of the Collaborative Economy](https://medium.com/newco/automation-is-the-next-phase-of-the-collaborative-economy-55ccf31c8834)
- [How Basic Income is an Automation Economy Fraud](https://medium.com/@Michael_Spencer/how-basic-income-is-an-automation-economy-fraud-b9873359584f)
- [If Work-Hours & the Value of Automation Were Distributed Fairly in the US Today](https://extranewsfeed.com/if-work-hours-the-value-of-automation-were-distributed-fairly-in-the-us-today-86d293ce0b6f)

----------------

### Manufacturing

[Back to top](#contents)

- [manufacturing-ai-perspective](https://www.infosys.com/human-amplification/Documents/manufacturing-ai-perspective.pdf)
- [intel: manufacturing](https://www.intel.in/content/www/in/en/manufacturing.html)
- [Artificial Intelligence Transforms Manufacturing](https://www.asme.org/engineering-topics/articles/manufacturing-design/artificial-intelligence-transforms-manufacturing)
- [The power of Artificial Intelligence in manufacturing](https://www.themanufacturer.com/articles/power-artificial-intelligence-manufacturing/)
- [Machine Learning in Manufacturing – Present and Future Use-Cases](https://www.techemergence.com/machine-learning-in-manufacturing/)
- [How AI Builds A Better Manufacturing Process](https://www.forbes.com/sites/insights-intelai/2018/07/17/how-ai-builds-a-better-manufacturing-process/)
- [aimanufacturingconference](http://aimanufacturingconference.com/)
- [AI, Making Manufacturing Great Again](https://www.roboticsbusinessreview.com/ai/ai-making-manufacturing-great-again/)
- [Future Factories: How AI enables smart manufacturing](https://medium.com/topbots/future-factories-how-ai-enables-smart-manufacturing-c1405f4ec0e6)
- [THE IMPACT OF ARTIFICIAL INTELLIGENCE (AI) ON OUR MANUFACTURING WORKFORCE](https://www.majentasolutions.com/blog/the-impact-of-ai-on-our-manufacturing-workforce/)
- [ROI on AI investments could take up to 5 years, 56% of manufacturing CEOs say]()
- [Adaptive Intelligent Apps for Manufacturing](https://cloud.oracle.com/ai-apps-for-manufacturing)
- [What does AI mean for the future of manufacturing?](https://www.telegraph.co.uk/business/social-innovation/artificial-intelligence-future-of-manufacture/)
- [AI and Its Applications in
Manufacturing](https://pdfs.semanticscholar.org/presentation/e4d2/91bb18d1f66b743e3fa1043f2546e2fca22f.pdf)
- [Industrial artificial intelligence](https://en.wikipedia.org/wiki/Industrial_artificial_intelligence)
- [AI in the Factory of the Future](https://www.bcg.com/en-in/publications/2018/artificial-intelligence-factory-future.aspx)

-------------

### Applications

[Back to top](#contents)

<ul><li><a href="https://en.wikipedia.org/wiki/Military_robot" title="Military robot">Military robots</a></li>
<li><a href="https://en.wikipedia.org/wiki/Caterpillar_Inc." title="Caterpillar Inc.">Caterpillar</a> plans to develop remote controlled machines and expects to develop fully autonomous heavy robots by 2021.  Some <a href="https://en.wikipedia.org/wiki/Crane_(machine)" title="Crane (machine)">cranes</a> already are remote controlled.</li>
<li>It was demonstrated that a robot can perform a <a href="https://en.wiktionary.org/wiki/herding" class="extiw" title="wikt:herding">herding</a> task.</li>
<li>Robots are increasingly used in manufacturing (since the 1960s). In the auto industry, they can amount for more than half of the "labor". There are even "<a href="https://en.wikipedia.org/wiki/Lights_out_(manufacturing)" title="Lights out (manufacturing)">lights off</a>" factories such as an IBM keyboard manufacturing factory in Texas that is 100% automated.</li>
<li>Robots such as HOSPI are used as <a href="https://en.wikipedia.org/wiki/Courier" title="Courier">couriers</a> in hospitals (<a href="/w/index.php?title=Hospital_robot&amp;action=edit&amp;redlink=1" class="new" title="Hospital robot (page does not exist)">hospital robot</a>). Other hospital tasks performed by robots are receptionists, guides and porters helpers.</li>
<li>Robots can serve as <a href="https://en.wikipedia.org/wiki/Waiter" class="mw-redirect" title="Waiter">waiters</a> and cooks, also at home.  <a href="/w/index.php?title=Boris_(robot)&amp;action=edit&amp;redlink=1" class="new" title="Boris (robot) (page does not exist)">Boris</a> is a robot that can load a <a href="https://en.wikipedia.org/wiki/Dishwasher" title="Dishwasher">dishwasher</a>. <a href="https://en.wikipedia.org/wiki/Rotimatic" title="Rotimatic">Rotimatic</a> is a robotics kitchen appliance that cooks <a href="https://en.wikipedia.org/wiki/Flatbread" title="Flatbread">flatbreads</a> automatically.</li>
<li><a href="https://en.wikipedia.org/wiki/Robot_combat" title="Robot combat">Robot combat</a> for sport – hobby or sport event where two or more robots fight in an arena to disable each other. This has developed from a hobby in the 1990s to several TV series worldwide.</li>
<li>Cleanup of contaminated areas, such as toxic waste or nuclear facilities.</li>
<li><a href="https://en.wikipedia.org/wiki/Agricultural_robot" title="Agricultural robot">Agricultural robots</a>  (AgRobots).</li>
<li><a href="https://en.wikipedia.org/wiki/Domestic_robot" title="Domestic robot">Domestic robots</a>, cleaning and caring for the elderly</li>
<li><a href="https://en.wikipedia.org/wiki/Medical_robot" title="Medical robot">Medical robots</a> performing low-invasive surgery</li>
<li><a href="https://en.wikipedia.org/wiki/Household_robot" class="mw-redirect" title="Household robot">Household robots</a> with full use.</li>
<li><a href="https://en.wikipedia.org/wiki/Nanorobot" class="mw-redirect" title="Nanorobot">Nanorobots</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swarm_robotics" title="Swarm robotics">Swarm robotics</a></li></ul>


---------------------------

### Literature Review

[Back to top](#contents)


#### Surveys


- [Artificial Intelligence and Robotics](https://arxiv.org/ftp/arxiv/papers/1803/1803.10813.pdf), 2018.
- [Artificial Intelligence for Long-Term Robot Autonomy: A Survey](https://arxiv.org/pdf/1807.05196.pdf), 2018.
- [Artificial Intelligence-Based Techniques for Emerging Robotics Communication: A Survey and Future Perspectives](https://arxiv.org/ftp/arxiv/papers/1804/1804.09671.pdf), 2018.
- [A Survey of Knowledge Representation and Retrieval for Learning in Service Robotics](https://arxiv.org/pdf/1807.02192.pdf), 2018.
- [A Survey of Deep Learning Techniques for Mobile Robot Applications](https://arxiv.org/pdf/1803.07608.pdf), 2018.
- [A Survey of Deep Network Solutions for Learning Control in Robotics: From Reinforcement to Imitation](https://arxiv.org/pdf/1612.07139v4.pdf), 2018.
- [Embodied Evolution in Collective Robotics: A Review](https://arxiv.org/abs/1709.08992v2), 2018.
- [Autonomous development and learning in artificial intelligence and robotics: Scaling up deep learning to human--like learning](https://arxiv.org/abs/1712.01626v1), 2017.
- [Towards Lifelong Self-Supervision: A Deep Learning Direction for Robotics](https://arxiv.org/abs/1611.00201v1), 2018.


#### RL

 - [Multi-Goal Reinforcement Learning: Challenging Robotics Environments and Request for Research](https://arxiv.org/abs/1802.09464v2), 2018.
  - Policy Gradient Reinforcement Learning for Fast Quadrupedal Locomotion (Kohl, ICRA 2004) [[Paper]](http://www.cs.utexas.edu/~pstone/Papers/bib2html-links/icra04.pdf)
  - Robot Motor SKill Coordination with EM-based Reinforcement Learning (Kormushev, IROS 2010) [[Paper]](http://kormushev.com/papers/Kormushev-IROS2010.pdf) [[Video]](https://www.youtube.com/watch?v=W_gxLKSsSIE)
  - Generalized Model Learning for Reinforcement Learning on a Humanoid Robot (Hester, ICRA 2010) [[Paper]](https://ccc.inaoep.mx/~mdprl/documentos/Hester_2010.pdf) [[Video]](https://www.youtube.com/watch?v=mRpX9DFCdwI&list=PL5nBAYUyJTrM48dViibyi68urttMlUv7e&index=12)
  - Autonomous Skill Acquisition on a Mobile Manipulator (Konidaris, AAAI 2011) [[Paper]](http://lis.csail.mit.edu/pubs/konidaris-aaai11b.pdf) [[Video]](https://www.youtube.com/watch?v=yUICAkSQTZY)
  - PILCO: A Model-Based and Data-Efficient Approach to Policy Search (Deisenroth, ICML 2011) [[Paper]](http://mlg.eng.cam.ac.uk/pub/pdf/DeiRas11.pdf)
  - Incremental Semantically Grounded Learning from Demonstration (Niekum, RSS 2013) [[Paper]](http://people.cs.umass.edu/~sniekum/pubs/NiekumRSS2013.pdf)
  - Efficient Reinforcement Learning for Robots using Informative Simulated Priors (Cutler, ICRA 2015) [[Paper]](http://markjcutler.com/papers/Cutler15_ICRA.pdf) [[Video]](https://www.youtube.com/watch?v=kKClFx6l1HY)
  - Robots that can adapt like animals (Cully, Nature 2015) [[Paper](https://arxiv.org/abs/1407.3501)] [[Video](https://www.youtube.com/watch?v=T-c17RKh3uE)] [[Code](https://github.com/resibots/cully_2015_nature)]
  - Black-Box Data-efficient Policy Search for Robotics (Chatzilygeroudis, IROS 2017) [[Paper](https://arxiv.org/abs/1703.07261)] [[Video](https://www.youtube.com/watch?v=kTEyYiIFGPM)] [[Code](https://github.com/resibots/blackdrops)]
  - An Application of Reinforcement Learning to Aerobatic Helicopter Flight (Abbeel, NIPS 2006) [[Paper]](http://heli.stanford.edu/papers/nips06-aerobatichelicopter.pdf) [[Video]](https://www.youtube.com/watch?v=VCdxqn0fcnE)
  - Autonomous helicopter control using Reinforcement Learning Policy Search Methods (Bagnell, ICRA 2001) [[Paper]](http://repository.cmu.edu/cgi/viewcontent.cgi?article=1082&context=robotics)

 
 Drones/UAV
 
 - [Multi-tier Drone Architecture for 5G/B5G Cellular
Networks: Challenges, Trends, and Prospects](https://arxiv.org/pdf/1711.08407.pdf)
 - [Amateur Drone Monitoring: State-of-the-Art
Architectures, Key Enabling Technologies, and
Future Research Directions](https://arxiv.org/ftp/arxiv/papers/1710/1710.02382.pdf)
 - [Economics of UAV-aided Mobile Services Deployment](https://arxiv.org/pdf/1805.08357.pdf)
 - [DroNet: Efficient convolutional neural network detector for real-time UAV applications](https://arxiv.org/pdf/1807.06789.pdf)
 - [Disaster Monitoring using Unmanned Aerial Vehicles and Deep Learning](https://arxiv.org/abs/1807.11805v2)
 - [Google Map Aided Visual Navigation for UAVs in GPS-denied Environment](https://arxiv.org/abs/1703.10125v1)
 - [Fast and Accurate, Convolutional Neural Network Based Approach for Object Detection from UAV](https://arxiv.org/abs/1808.05756v1)
 - [Automatic classification of trees using a UAV onboard camera and deep learning](https://arxiv.org/abs/1804.10390v1)
 - [Radiation Search Operations using Scene Understanding with Autonomous UAV and UGV](https://arxiv.org/abs/1609.00017v1)
 - [A Unified Framework for Joint Mobility Prediction and Object Profiling of Drones in UAV Networks](https://arxiv.org/abs/1808.00058v1)
 
 
--------------


![ai_r](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/05-ai-in-robotics/ai_r.JPG)


------------------
### Startups

[Back to top](#contents)

- [Robotics Startups - AngelList](https://angel.co/robotics)
- [Know Your Industries: 90+ Market Maps Covering Fintech, CPG, Auto Tech, Healthcare, And More](https://www.cbinsights.com/research/industry-market-map-landscape/)
- [Robotics Market Map: 80+ Robot Startups Working In Factories, Homes, And Hospitals](https://www.cbinsights.com/research/robotics-startups-market-map-company-list/)
- [Mining Companies Have Led On Autonomous Vehicle Adoption. Now They’re Going After The Next Phase Of Automation.](https://www.cbinsights.com/research/mining-companies-autonomous-vehicles-automation-expert-intelligence/)
- [Anti-Drone Technology: 4 Solutions Keeping Unmanned Aircrafts From Flying Where They’re Not Welcome](https://www.cbinsights.com/research/anti-drone-tech-expert-intelligence/)
- [Mr. Robot At Home: 50+ Consumer Robot Startups Helping To Clean, Cook, And More](https://www.cbinsights.com/research/robots-consumer-startups-market-map/)
- [How Google, Foxconn, GE, And Other Corporate Investors Are Betting On Robotics Startups](https://www.cbinsights.com/research/robotics-startups-corporate-investing/)
- [Robotics M&A: Acquisitions Reach New High In 2015 Boosted By Flurry Of Industrial Deals](https://www.cbinsights.com/research/top-acquirers-robotics-startups-ma-timeline/)
- [Robotics Market Map: 80+ Robot Startups Working In Factories, Homes, And Hospitals](https://www.cbinsights.com/research/robotics-startups-market-map-company-list/)
- [AI, Robotics, And The Future Of Precision Agriculture](https://www.cbinsights.com/research/ai-robotics-agriculture-tech-startups-future/)
- [Future Factory: How Technology Is Transforming Manufacturing](https://www.cbinsights.com/research/future-factory-manufacturing-tech-trends/)
- [drones-startup-market-map](https://www.cbinsights.com/research/drones-startup-market-map/)
- [The Robotics Ecosystem: Startup Funding By Category Broken Down In One Infographic](https://www.cbinsights.com/research/robotics-deals-consumer-enterprise-medical/)

--------------------------------------


### Appendix

[Back to top](#contents)


![Rise-of-robotics-1](http://usblogs.pwc.com/emerging-technology/wp-content/uploads/2017/03/Rise-of-robotics-1.png)

----------------

![Rise-of-robotics-2-1](http://usblogs.pwc.com/emerging-technology/wp-content/uploads/2017/03/Rise-of-robotics-2-1.png)

------------

![robot_planet_2016_2](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2017/01/robot_planet_2016_2.png)

------------

![Robotics_corporates_BSG_q316](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2016/09/Robotics_corporates_BSG_q316.png)

-------------------

![robotics_MnA_20160818-2](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2016/08/robotics_MnA_20160818-2.png)

----------------

![AI_robotics_Agriculture1](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2017/07/AI_robotics_Agriculture1.png)

----------------

![robots3](https://s3.amazonaws.com/cbi-research-portal-uploads/2018/03/15191614/robots3.png)


--------------

![RnD](https://s3.amazonaws.com/cbi-research-portal-uploads/2018/03/13120644/RnD.png)

--------------

![180405-Future-Factory-V4](https://s3.amazonaws.com/cbi-research-portal-uploads/2018/04/05171259/180405-Future-Factory-V4.png)

---------------

![Drones-Market-Map-High-Resolution](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2017/06/Drones-Market-Map-High-Resolution.png)

-----------

![consumer_robots_map_q3-16](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2016/10/consumer_robots_map_q3-16.png)


-------------

![robotics_treemap_2016_2](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2016/10/robotics_treemap_2016_2.png)

------------

![robotics_deals_category_2016_1](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2016/10/robotics_deals_category_2016_1.png)

--------------

![automation-jobs-likely-to-be-automated](https://content.creditloan.com/media/automation-jobs-likely-to-be-automated.png)

------------

![automation-visualizing-the-time](https://content.creditloan.com/media/automation-visualizing-the-time.png)


--------------

![automation-the-value-of-person-hours](https://www.creditloan.com/media/automation-the-value-of-person-hours.png)


--------------

![automation-job-automation-by-education-level](https://www.creditloan.com/media/automation-job-automation-by-education-level.png)


--------------

![11409_LT_Robotics](https://www.machinedesign.com/sites/machinedesign.com/files/uploads/2013/09/11409_LT_Robotics%20Sy.jpg)

-------------

![image1_20120327143946](http://www.ni.com/cms/images/devzone/tut/image1_20120327143946.png)

Source: [A Layered Approach to Designing Robot Software](http://www.ni.com/white-paper/13929/en/#toc2)

-----------------

![Automation_Briefing](https://www.mckinsey.com/~/media/McKinsey/Featured%20Insights/Digital%20Disruption/Whats%20now%20and%20next%20in%20analytics%20automation/SVGZ_Insights_Analytics-AI-Automation_Briefing%20note_ex8.ashx)

-----------

![AI_Technology](http://analystpov.com/wp-content/uploads/2017/08/AI_Technology-Landscape.png)

-----------------
----------
