

### A brief survey : Autonomous Vehicles

------------
> #### Contents

- [Timeline](#timeline)
- [The why](#the-why)
- [Autonomy Levels](#autonomy-levels)
- [Autonomous vehicle enabling technologies](#autonomous-vehicle-enabling-technologies)
  - [Sensors and Cameras](#sensors-and-cameras)
  - [Local Data Processors](#local-data-processors)
  - [High-performance GPS](#high-performance-gps)
  - [Radar](#radar)
  - [LIDAR](#lidar)
  - [Smart Technologies](#smart-technologies)
  - [Connectivity to the Internet of Things](#connectivity-to-the-internet-of-things)
  - [Cloud-Based Data Processing & Management](#cloud-based-data-processing-and-management)
  - [Artificial Intelligence](#artificial-intelligence)
  - [Machine Learning](#machine-learning)
- [Autonomous vehicle architecture](#autonomous-vehicle-architecture)
- [Literature review](#literature-review)
  - [General](#general)
  - [Localization  and Mapping](#localization-and-mapping)
  - [Perception](#perception)
  - [Navigation and Planning](#navigation-and-planning)
  - [Control](#control)
  - [Simulation](#simulation)
  - [Software Engineering](#software-engineering)
  - [Human-Machine Interaction](#human-machine-interaction)
  - [Infrastructure](#infrastructure)
  - [Law and Society](#law-and-society)
- [Datasets](#datasets)
- [Implementations and libraries](#implementations-and-libraries)
- [Startups](#startups)
- [Appendix](#appendix)

[Back to top](#contents)

-------------

#### Timeline


[Back to top](#contents)

- [History of autonomous cars](https://en.wikipedia.org/wiki/History_of_autonomous_cars)
- [Intelligent transportation system](https://en.wikipedia.org/wiki/Intelligent_transportation_system)
- [A Timeline of the Automobile Industry](https://www.scaruffi.com/politics/cars.html)
- [History of the Automotive Industry](https://www.preceden.com/timelines/263578-history-of-the-automotive-industry)
- [The Evolution of the Auto industry](https://www.timetoast.com/timelines/1201032)
- [Timeline of motor vehicle brands](https://en.wikipedia.org/wiki/Timeline_of_motor_vehicle_brands)
- [List of automobile manufacturers](https://en.wikipedia.org/wiki/List_of_automobile_manufacturers)
- [List of current automobile manufacturers by country](https://en.wikipedia.org/wiki/List_of_current_automobile_manufacturers_by_country)
- [List of current automobile manufacturers (alphabetical)](https://en.wikipedia.org/wiki/List_of_current_automobile_manufacturers_(alphabetical))
- [Autonomous car](https://en.wikipedia.org/wiki/Autonomous_car)
- [The Self-Driving Car Timeline – Predictions from the Top 11 Global Automakers](https://www.techemergence.com/self-driving-car-timeline-themselves-top-11-automakers/)
- [The Evolution of Self-Driving Cars](https://nytjournal.org/articles/ai_articles/evolution_of_self_driving_cars.php)
- [Evolution of Self Driving Autonomous Car](http://robotglobe.org/evolution-of-self-driving-autonomous-car/)
- [sae.org](https://www.sae.org)

--------------

#### The why


[Back to top](#contents)

- [73 Mind-Blowing Implications of Driverless Cars and Trucks](https://medium.com/@DonotInnovate/73-mind-blowing-implications-of-a-driverless-future-58d23d1f338d)
- [The Unintended Ways Self-Driving Cars Will Change Our World](https://medium.com/swlh/the-unintended-ways-self-driving-cars-will-change-our-world-3b15d1db9026)
- [Why do we need self-driving cars?](https://www.quora.com/Why-do-we-need-self-driving-cars-1)
- [Andrew Ng: Do we really need self driving cars?](https://www.quora.com/Andrew-Ng-Do-we-really-need-self-driving-cars)
- [Top 20 Pros and Cons Associated With Self-Driving Cars](https://www.autoinsurancecenter.com/top-20-pros-and-cons-associated-with-self-driving-cars.htm)
- [Why do we need Driverless Cars?](https://www.quora.com/Why-do-we-need-Driverless-Cars)
- [We don't need fully self-driving cars to save lives](https://www.usatoday.com/story/tech/columnist/2018/02/04/we-dont-need-fully-self-driving-cars-save-lives/1085965001/)
- [~$1 trillion of real estate is on the move … here’s why](https://medium.com/99-mph/1-trillion-of-real-estate-is-on-the-move-heres-why-94ee9233e5eb)

--------------

#### Autonomy Levels

SAE (J3016)

[Back to top](#contents)

<table class="wikitable">
<caption>
</caption>
<tbody><tr>
<th>SAE Level</th>
<th>Name</th>
<th colspan="2">Narrative definition</th>
<th>Execution of<br />steering and<br />acceleration/<br />deceleration</th>
<th>Monitoring of driving environment</th>
<th>Fallback performance of dynamic driving task</th>
<th>System capability (driving modes)
</th></tr>
<tr>
<td colspan="8"><i><b>Human driver monitors the driving environment</b></i>
</td></tr>
<tr>
<td>0</td>
<td>No Automation</td>
<td colspan="2">The full-time performance by the human driver of all aspects of the dynamic driving task, even when "enhanced by warning or intervention systems"</td>
<td>Human driver</td>
<td rowspan="3">Human driver</td>
<td rowspan="3">Human driver</td>
<td>n/a
</td></tr>
<tr>
<td>1</td>
<td>Driver Assistance</td>
<td>The driving mode-specific execution by a driver assistance system of "either steering or acceleration/deceleration"</td>
<td rowspan="2">using information about the driving environment and with the expectation that the human driver performs all remaining aspects of the dynamic driving task</td>
<td>Human driver and system</td>
<td rowspan="2">Some driving modes
</td></tr>
<tr>
<td>2</td>
<td>Partial Automation</td>
<td>The driving mode-specific execution by one or more driver assistance systems of <i>both steering and acceleration/deceleration</i></td>
<td>System
</td></tr>
<tr>
<td colspan="8"><i><b>Automated driving system monitors the driving environment</b></i>
</td></tr>
<tr>
<td>3</td>
<td>Conditional Automation</td>
<td rowspan="3">The driving mode-specific performance by an automated driving system of all aspects of the dynamic driving task</td>
<td>with the expectation that the <i>human driver will respond appropriately to a request to intervene</i></td>
<td rowspan="3">System</td>
<td rowspan="3">System</td>
<td>Human driver</td>
<td>Some driving modes
</td></tr>
<tr>
<td>4</td>
<td>High Automation</td>
<td><i>even if a human driver does not respond appropriately to a request to intervene</i></td>
<td rowspan="3">System</td>
<td>Many driving modes
</td></tr>
<tr>
<td>5</td>
<td>Full Automation</td>
<td><i>under all roadway and environmental conditions</i> that can be managed by a human driver</td>
<td>All driving modes
</td></tr></tbody></table>


> **Note: _As of today, no car manufacturer has achieved level 3 or higher in production, although several have produced demonstration vehicles._**
 
 ![Hecht-img2](https://www.osa-opn.org/opn/media/Images/Articles/2018/1801/Features/Hecht-img2.jpg?width=1200)
 
---------------------

#### Autonomous vehicle enabling technologies

[Back to top](#contents)

- [The Building Blocks of Autonomous Control](https://s3.amazonaws.com/visionsystemsintelligence/pdfs/VSI%20AUVSI%20Presentation_July_2016.pdf)
- [Autonomous Vehicles – Risk or Opportunity?](https://higherlogicdownload.s3.amazonaws.com/AUVSI/14c12c18-fde1-4c1d-8548-035ad166c766/UploadedImages/documents/Com/ComSeries-Full.pdf)
- [Autonomous Car](https://www.slideshare.net/asertseminar/autonomous-car-32512833)
- [Machine Learning for Self-Driving Cars](https://www.slideshare.net/jwiegelmann/machine-learning-for-selfdriving-cars)
- [Autonomous Vehicle Implementation Predictions
Implications for Transport Planning](https://www.vtpi.org/avip.pdf)
- [GM: 2018
SELF-DRIVING
SAFETY REPORT](https://www.gm.com/content/dam/gm/en_us/english/selfdriving/gmsafetyreport.pdf)
- [Towards Autonomous Driving](https://s21.q4cdn.com/600692695/files/doc_presentations/2018/CES-2018-final-MBLY.pdf)
- [Measurements Systems and Sensors for
Autonomous Vehicle and Smart Mobility](http://vancouver.ieee.ca/files/2017/12/IEEE-DL-Saponara.pdf)
- [Three Sensor Types Drive Autonomous Vehicles](https://www.sensorsmag.com/components/three-sensor-types-drive-autonomous-vehicles)
- [Industry 4.0: the fourth industrial revolution – guide to Industrie 4.0](https://www.i-scoop.eu/industry-4-0/)

----------


- [How Sensor Fusion Works for Self-Driving Cars](https://readbackline.com/self-driving-cars/how-sensor-fusion-works-self-driving-cars/)
- [Autonomous Driving](https://www.quora.com/topic/Autonomous-Driving)
- [What sensors do driverless cars have?](https://www.quora.com/What-sensors-do-driverless-cars-have)
- [MEMS and Sensors in Automotive Applications on the Road to Autonomous Vehicles: HUD and ADAS](https://www.slideshare.net/MicroVision/mems-and-sensors-in-automotive-applications-on-the-road-to-autonomous-vehicles-hud-and-adas)
- [SENSOR FUSION: A COMPARISON OF SENSING
CAPABILITIES OF HUMAN DRIVERS AND
HIGHLY AUTOMATED VEHICLES](http://umich.edu/~umtriswt/PDF/SWT-2017-12.pdf)
- [Cameras vs. LiDAR for Self-Driving Cars]()
- [Lidar for Self-Driving Cars](https://www.osa-opn.org/home/articles/volume_29/january_2018/features/lidar_for_self-driving_cars/)

------------


![sd-tech](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/sd-tech.JPG)


Source: [MIT-TR](https://www.technologyreview.com/s/609674/whats-driving-autonomous-vehicles/)

--------

#### Sensors and Cameras

[Back to top](#contents)

![cs](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/c_s.JPG)

--------------

#### Local Data Processors

[Back to top](#contents)

![ldp](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/ldp.JPG)



---------------

#### High-performance GPS

[Back to top](#contents)

 ![gps](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/gps.JPG) 


----------------------

#### Radar

[Back to top](#contents)

  ![radar](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/radar.JPG)


----------------------

#### LIDAR

[Back to top](#contents)

  
![lidar](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/lidar.JPG)


-----------------

#### Smart Technologies

[Back to top](#contents)

![smart](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/smart.JPG)


------------------------

#### Connectivity to the Internet of Things

[Back to top](#contents)

 ![iot1](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/iot1.JPG) 


----------------------

#### Cloud-Based Data Processing and Management

[Back to top](#contents)

![cloud](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/cloud.JPG)


-------------------------

#### Artificial Intelligence

[Back to top](#contents)

  
![ai](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/ai.JPG)



-------------------------

#### Machine Learning

[Back to top](#contents)


![ml](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/ml.JPG)

-------------------------


#### Autonomous vehicle architecture

working mechanism of AV's

[Back to top](#contents)





![gm](https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/img/gm.JPG)

--------




![NMg896FbXQ](https://cdn-images-1.medium.com/max/800/1*wCauTmBeevs-NMg896FbXQ.png)

-----------

**Computer Vision and Deep Learning**
- Traffic Sign Classifier
- Behavioural Cloning
- Advanced Lane Finding
- Vehicle Detection and Tracking

**Sensor Fusion, Localisation and Control**
- Extended Kalman Filter Project
- Unscented Kalman Filter Project
- Kidnapped Vehicle Project
- PID Controller Project
- Model Predictive Control Project

**Path planning, Concentrations and Systems**
- Path Planning Project
- Semantic Segmentation
- Programming a Real Self-Driving Car

---------------

- [Self-Driving Car Engineer](https://s3-us-west-2.amazonaws.com/udacity-email/Documents/Self-Driving+Car+Nanodegree+Handbook.pdf?utm_medium=email&utm_campaign=2017-03-16_carnd_march_term1_firstday&utm_source=blueshift&utm_content=2017-03-16_carnd_firstday_march&bsft_eid=4e53e27f-c6f3-4c3e-941b-c64061a308bc&bsft_clkid=95d74df9-11dd-45c2-b9c6-6ccc210694f4&bsft_uid=80aad2e4-4b0a-4fc1-bfa8-a9be4bf316c9&bsft_mid=33fd9f5f-b427-4d33-9b26-8496c6b93fab)
- [In-Depth on Udacity’s Self-Driving Car Curriculum](https://medium.com/self-driving-cars/term-1-in-depth-on-udacitys-self-driving-car-curriculum-ffcf46af0c08)
- [The New Udacity Self-Driving Car Engineer Nanodegree Program Syllabus](https://medium.com/udacity/the-new-udacity-self-driving-car-engineer-nanodegree-program-syllabus-87b9b1fd7c65)
- [Term 2: In-Depth on Udacity’s Self-Driving Car Curriculum](https://medium.com/udacity/term-2-in-depth-on-udacitys-self-driving-car-curriculum-775130aae502)
- [Term 3: In-Depth on Udacity’s Self-Driving Car Curriculum](https://medium.com/udacity/term-3-in-depth-on-udacitys-self-driving-car-curriculum-15d03e45d7ea)
- [Perception Projects from the Self-Driving Car Nanodegree Program](https://medium.com/udacity/perception-projects-from-the-self-driving-car-nanodegree-program-51fb88a38ff9)
- [Udacity Self-Driving Car Engineer Nanodegree Projects](https://medium.com/udacity/udacity-self-driving-car-engineer-nanodegree-projects-12823ff1cd21)
- [Udacity and Baidu’s New Course: Introduction to Apollo](https://medium.com/udacity/udacity-and-baidus-new-course-introduction-to-apollo-4eb244313e8c)
- [A common systems architecture for
autonomous vehicles](https://pdfs.semanticscholar.org/presentation/cd7b/6813d5e804010742be02099eaaf2a1ba2728.pdf)
- [Creating autonomous vehicle systems](https://www.oreilly.com/ideas/creating-autonomous-vehicle-systems)
- [The vehicle architecture of automated driving level 2/3](http://www.embedded-computing.com/embedded-computing-design/the-vehicle-architecture-of-automated-driving-level-2-3)
- [The Architectural Implications of Autonomous
Driving: Constraints and Acceleration](https://web.eecs.umich.edu/~shihclin/papers/AutonomousCar-ASPLOS18.pdf)
- [Towards a Functional System Architecture for
Automated Vehicles](https://arxiv.org/pdf/1703.08557.pdf)
- [A functional architecture for autonomous driving](https://sagar.se/files/wasa2015.pdf)
- [Introduction to Software Architecture for
Autonomous Systems](http://wasp-sweden.org/custom/uploads/2017/03/01_Introduction-to-Software-Architecture-for-Autonomous-Systems-Pellicione.pdf)
- [Autonomous Vehicles that Interact with Pedestrians: A Survey of Theory and Practice](https://arxiv.org/abs/1805.11773v1)
- [Computer Science > Computers and Society
MIT Autonomous Vehicle Technology Study: Large-Scale Deep Learning Based Analysis of Driver Behavior and Interaction with Automation](https://arxiv.org/abs/1711.06976v1)
- [A Systematic Comparison of Deep Learning Architectures in an Autonomous Vehicle](https://arxiv.org/abs/1803.09386v1)
- [Infrastructure Enabled Autonomy: A Distributed
Intelligence Architecture for Autonomous Vehicles](https://arxiv.org/pdf/1802.04112.pdf)
- [Architecting Autonomous Automotive Systems](https://www.diva-portal.org/smash/get/diva2:615888/FULLTEXT02.pdf)
- [A Functional Reference Architecture for Autonomous Driving](https://www.researchgate.net/publication/288918943_A_Functional_Reference_Architecture_for_Autonomous_Driving)
- [Automated Vehicle System Architecture with Performance Assessment](https://www.researchgate.net/publication/320324052_Automated_Vehicle_System_Architecture_with_Performance_Assessment)
- [An Integrated Architecture for Autonomous Vehicles
Simulation](https://web.fe.up.pt/~niadr/PUBLICATIONS/2012/2_ACM-SAC_056_1886.pdf)


------------------

#### Literature Review

[Back to top](#contents)

#### General

[Back to top](#contents)

* **[2016]** _Combining Deep Reinforcement Learning and Safety Based Control for Autonomous Driving_. [[ref](https://arxiv.org/abs/1612.00147)]
* **[2015]** _An Empirical Evaluation of Deep Learning on Highway Driving_. [[ref](https://arxiv.org/abs/1504.01716)]
* **[2015]** _Self-Driving Vehicles: The Challenges and Opportunities Ahead_. [[ref](http://dl.acm.org/citation.cfm?id=2823464)]
* **[2014]** _Making Bertha Drive - An Autonomous Journey on a Historic Route_. [[ref](https://www.semanticscholar.org/paper/Making-Bertha-Drive-An-Autonomous-Journey-on-a-Ziegler-Bender/ec26d7b1cb028749d0d6972279cf4090930989d8)]
* **[2014]** _Towards Autonomous Vehicles_. [[ref](https://www.semanticscholar.org/paper/Towards-Autonomous-Vehicles-Schwarz-Thomas/88712e686e1bcad21f0836e9d31400dab2b7fa8f)]
* **[2013]** _Towards a viable autonomous driving research platform_. [[ref](https://www.semanticscholar.org/paper/Towards-a-viable-autonomous-driving-research-Wei-Snider/da5cee7a6eb817bbbf4721c64c756bd8b7122359)]
* **[2013]** _An ontology-based model to determine the automation level of an automated vehicle for co-driving_. [[ref](https://www.semanticscholar.org/paper/An-ontology-based-model-to-determine-the-Pollard-Morignot/25239ec7fb6159166dfe15adf229fc2415f071df)]
* **[2013]** _Autonomous Vehicle Navigation by Building 3d Map and by Detecting Human Trajectory Using Lidar_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Vehicle-Navigation-by-Building-3d-Map-Kagami-Thompson/81b14341e3e063d819d032b6ce0bc0be0917c867)]
* **[2012]** _Autonomous Ground Vehicles - Concepts and a Path to the Future_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Ground-Vehicles-Concepts-and-a-Path-to-Luettel-Himmelsbach/5e8d51a1f6ba313a38a35af414a00bcfd3b5c0ae)]
* **[2011]** _Experimental Evaluation of Autonomous Driving Based on Visual Memory and Image-Based Visual Servoing_. [[ref](https://www.semanticscholar.org/paper/Experimental-Evaluation-of-Autonomous-Driving-Diosi-Segvic/2aeb9aa42e8e2048e15453759ec12411486a2619)]
* **[2011]** _Learning to Drive: Perception for Autonomous Cars_. [[ref](https://www.semanticscholar.org/paper/Learning-to-Drive-Perception-for-Autonomous-Cars-Stavens-Thrun/be25d7bff3b5928adf6c0a7f5495d47113f80997)]
* **[2010]** _Toward robotic cars_. [[ref](http://dl.acm.org/citation.cfm?id=1721679)]
* **[2009]** _Autonomous Driving in Traffic: Boss and the Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Driving-in-Traffic-Boss-and-the-Urban-Urmson-Baker/4657a350e4822bc567256f9b9dc5d922237a71be)]
* **[2009]** _Mapping, navigation, and learning for off-road traversal_. [[ref](https://www.semanticscholar.org/paper/Mapping-navigation-and-learning-for-off-road-Konolige-Agrawal/57d7396b92ad31b386dfce4f8799149f5ced2160)]
* **[2008]** _Autonomous Driving in Urban Environments: Boss and the Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Driving-in-Urban-Environments-Boss-and-Urmson-Anhalt/1c0fb6b1bbfde0f9bab6268f5609cce2bd3bc5bd)]
* **[2008]** _Caroline: An autonomously driving vehicle for urban environments_. [[ref](https://www.semanticscholar.org/paper/Caroline-An-autonomously-driving-vehicle-for-urban-Rauskolb-Berger/08f4e164291942fc78bd6945215b2c672b17edd5)]
* **[2008]** _Design of an Urban Driverless Ground Vehicle_. [[ref](https://www.semanticscholar.org/paper/Design-of-an-Urban-Driverless-Ground-Vehicle-Benenson-Parent/852a672c3d4a2fca3ff7b215d9c096b0be54feb7)]
* **[2008]** _Little Ben: The Ben Franklin Racing Team's Entry in the 2007 DARPA Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/Little-Ben-The-Ben-Franklin-Racing-Team-s-Entry-in-Bohren-Foote/b6d5e01cdb76284ee6c42b0dda6c36f121c573f0)]
* **[2008]** _Odin: Team VictorTango's Entry in the DARPA Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/Odin-Team-VictorTango-s-Entry-in-the-DARPA-Urban-Reinholtz-Hong/aaeaa58bedf6fa9b42878bf5914f55f48cf26209)]
* **[2008]** _Robosemantics: How Stanley the Volkswagen Represents the World_. [[ref](https://www.semanticscholar.org/paper/Robosemantics-How-Stanley-the-Volkswagen-Parisien-Thagard/9f2186df45a387ab600414968090fe3da37591ca)]
* **[2008]** _Team AnnieWAY's autonomous system for the 2007 DARPA Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/Team-AnnieWAY-s-Autonomous-System-Stiller-Kammel/56972aa9f9d3cce7c77d402602bc8f3af94d57c9)]
* **[2008]** _The MIT-Cornell collision and why it happened_. [[ref](https://www.semanticscholar.org/paper/The-MIT-Cornell-collision-and-why-it-happened-Fletcher-Teller/0df4f3ef7356fe56547ac3145d7c0229163bc7a5)]
* **[2007]** _Self-Driving Cars - An AI-Robotics Challenge_. [[ref](https://www.semanticscholar.org/paper/Self-Driving-Cars-An-AI-Robotics-Challenge-Thrun/31d17c77d2ea18f71d570741665f0fd3030caa94)]
* **[2007]** _2007 DARPA Urban Challenge: The Ben Franklin Racing Team Team B156 Technical Paper_. [[ref](https://www.semanticscholar.org/paper/2007-Darpa-Urban-Challenge-the-Ben-Franklin-Racing-Franklin-Lee/510b0fa02d6bdd1061cf73373f197ba624692ad0)]
* **[2007]** _Team Mit Urban Challenge Technical Report_. [[ref](https://www.semanticscholar.org/paper/Team-Mit-Urban-Challenge-Technical-Report-Leonard-Barrett/6ac15e819701cd0d077d8157711c4c402106722c)]
* **[2007]** _DARPA Urban Challenge Technical Report Austin Robot Technology_ [[ref](https://www.semanticscholar.org/paper/Darpa-Urban-Challenge-Technical-Report-Executive-Technology-Tuttle/37e78b1bd135df5c5a1fcbf2a8debd260d28a55c)]
* **[2007]** _Spirit of Berlin: an Autonomous Car for the Darpa Urban Challenge Hardware and Software Architecture_. [[ref](https://www.semanticscholar.org/paper/Spirit-of-Berlin-an-Autonomous-Car-for-the-Darpa-Berlin-Rojo/8c96cbc752dfcde3673440cf7ca1fb19218426bf)]
* **[2007]** _Team Case and the 2007 Darpa Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/Team-Case-and-the-2007-Darpa-Urban-Challenge-Newman-Lead/e68c745b7807e77ccf67fea325a241136a568eeb)]
* **[2006]** _A Personal Account of the Development of Stanley, the Robot That Won the DARPA Grand Challenge_. [[ref](https://www.semanticscholar.org/paper/A-Personal-Account-of-the-Development-of-Stanley-Thrun/74a4de58be068d2dc38bb31cf54c3c49bdc0d4e4)]
* **[2006]** _Stanley: The robot that won the DARPA Grand Challenge_. [[ref](https://www.semanticscholar.org/paper/Stanley-The-robot-that-won-the-DARPA-Grand-Thrun-Montemerlo/298500897243b17fa2ebe7bde0a1b8ebc00ea07f)]

#### Localization and Mapping

[Back to top](#contents)

* **[2016]** _MultiCol-SLAM - A Modular Real-Time Multi-Camera SLAM System._ [[ref](https://arxiv.org/abs/1610.07336)]
* **[2016]** _Image Based Camera Localization: an Overview_. [[ref](https://arxiv.org/abs/1610.03660)]
* **[2016]** _Ubiquitous real-time geo-spatial localization_ [[ref](http://dl.acm.org/citation.cfm?id=3005426)]
* **[2016]** _Robust multimodal sequence-based loop closure detection via structured sparsity_. [[ref](http://www.roboticsproceedings.org/rss12/p43.pdf)]
* **[2016]** _SRAL: Shared Representative Appearance Learning for Long-Term Visual Place Recognition_. [[ref](http://ieeexplore.ieee.org/document/7839213/)], [[code](https://github.com/hanfeiid/SRAL)]
* **[2015]** _Precise Localization of an Autonomous Car Based on Probabilistic Noise Models of Road Surface Marker Features Using Multiple Cameras_. [[ref](https://www.semanticscholar.org/paper/Precise-Localization-of-an-Autonomous-Car-Based-on-Jo-Jo/27251099b78185f9ddf59c9ed0c5868af4ef1e80)]
* **[2013]** _Planar Segments Based Three-dimensional Robotic Mapping in Outdoor Environments_. [[ref](https://www.semanticscholar.org/paper/Planar-Segments-Based-Three-dimensional-Robotic-Xiao/ebddeb22f3b5c38422987c3fe51aaf847ad444e7)]
* **[2013]** _Vehicle Localization along a Previously Driven Route Using Image Database_. [[ref](https://www.semanticscholar.org/paper/Vehicle-Localization-along-a-Previously-Driven-Kume-Supp%C3%A9/e5a7ac37d542349ae19281f1e2a571f7030b789c)]
* **[2012]** _Can priors be trusted? Learning to anticipate roadworks_. [[ref](https://www.semanticscholar.org/paper/Can-priors-be-trusted-Learning-to-anticipate-Mathibela-Osborne/0a7e502779ed2cf9ee2677d0310386481a51fc12)]
* **[2009]** _Laser Scanner Based Slam in Real Road and Traffic Environment_. [[ref](https://www.semanticscholar.org/paper/Laser-Scanner-Based-Slam-in-Real-Road-and-Traffic-Garcia-Favrot-Parent/2accb1d9f7ce3f08aa1cde735dcca2578887c545)]
* **[2007]** _Map-Based Precision Vehicle Localization in Urban Environments_. [[ref](https://www.semanticscholar.org/paper/Map-Based-Precision-Vehicle-Localization-in-Urban-Levinson-Montemerlo/924f7268d592d327f97ad4e96f48ad774d982ef3)]

#### Perception

[Back to top](#contents)


* **[2016]** _VisualBackProp: visualizing CNNs for autonomous driving_. [[ref](https://arxiv.org/abs/1611.05418)]
* **[2016]** _Driving in the Matrix: Can Virtual Worlds Replace Human-Generated Annotations for Real World Tasks?_. [[ref](https://arxiv.org/abs/1610.01983)]
* **[2016]** _Lost and Found: Detecting Small Road Hazards for Self-Driving Vehicles_. [[ref](https://arxiv.org/abs/1609.04653)]
* **[2016]** _Image segmentation of cross-country scenes captured in IR spectrum_. [[ref](https://arxiv.org/abs/1604.02469)]
* **[2016]** _Traffic-Sign Detection and Classification in the Wild_. [[ref](https://www.semanticscholar.org/paper/Traffic-Sign-Detection-and-Classification-in-the-Zhu-Liang/d463499b7a82e3cad81d2471b52a198b857aa75b)]
* **[2016]** _Persistent self-supervised learning principle: from stereo to monocular vision for obstacle avoidance_. [[ref](https://www.semanticscholar.org/paper/Persistent-self-supervised-learning-principle-from-Hecke-Croon/a48c4c6707fca20ae64b044b6e8f7f37891186fc)]
* **[2016]** _Deep Multispectral Semantic Scene Understanding of Forested Environments Using Multimodal Fusion_. [[ref](https://www.semanticscholar.org/paper/Deep-Multispectral-Semantic-Scene-Understanding-of-Valada-Oliveira/8be99dd94bff76c75594a15e114268841a2656a7)]
* **[2016]** _Joint Attention in Autonomous Driving (JAAD)_. [[ref](https://www.semanticscholar.org/paper/Joint-Attention-in-Autonomous-Driving-JAAD--Kotseruba-Rasouli/1e6a26deea0a38310368d9c2a6dadc317b50bdf8), [data](http://data.nvision2.eecs.yorku.ca/JAAD_dataset/)]
* **[2016]** _Perception for driverless vehicles: design and implementation_. [[ref](https://www.semanticscholar.org/paper/Perception-for-driverless-vehicles-design-and-Benenson-Suarez/bf1c728e3e893670244591f720b453245c3363f6)]
* **[2016]** _Robust multimodal sequence-based loop closure detection via structured sparsity_. [[ref](http://www.roboticsproceedings.org/rss12/p43.pdf)]
* **[2016]** _SRAL: Shared Representative Appearance Learning for Long-Term Visual Place Recognition_. [[ref](http://ieeexplore.ieee.org/document/7839213/)], [[code](https://github.com/hanfeiid/SRAL)]
* **[2015]** _Pixel-wise Segmentation of Street with Neural Networks_. [[ref](https://arxiv.org/abs/1511.00513)]
* **[2015]** _Deep convolutional neural networks for pedestrian detection_. [[ref](https://arxiv.org/abs/1510.03608)]
* **[2015]** _Fast Algorithms for Convolutional Neural Networks_. [[ref](https://arxiv.org/abs/1509.09308)]
* **[2015]** _Fusion of color images and LiDAR data for lane classification_. [[ref](http://dl.acm.org/citation.cfm?id=2820859)]
* **[2015]** _Environment Perception for Autonomous Vehicles in Challenging Conditions Using Stereo Vision_. [[ref](https://www.semanticscholar.org/paper/Environment-Perception-for-Autonomous-Vehicles-in-Gal%C3%A1n-Hayet/8f56fd10f37382292f474c441f92432b34b58db5)]
* **[2015]** _Intention-aware online POMDP planning for autonomous driving in a crowd_. [[ref](https://www.semanticscholar.org/paper/Intention-aware-online-POMDP-planning-for-Bai-Cai/481aa2882a5816686a5bea7db755862cded42081)]
* **[2015]** _Survey on Vanishing Point Detection Method for General Road Region Identification_. [[ref](https://www.semanticscholar.org/paper/Survey-on-Vanishing-Point-Detection-Method-for-Patel-Mistry/39c6be1e7723b93f06be2bb4199066d4efdadbc9)]
* **[2015]** _Visual road following using intrinsic images_. [[ref](https://www.semanticscholar.org/paper/Visual-road-following-using-intrinsic-images-Krajn%C3%ADk-Blazicek/2298f9e3c1235526d55cf78bfc80c505d100540f)]
* **[2014]** _Rover – a Lego* Self-driving Car_. [[ref](https://www.semanticscholar.org/paper/Rover-a-Lego-Self-driving-Car-Tan-Wojtczyk-Wojtczyk/6e24123ef558ffb9888d28f992f8afe76622830e)]
* **[2014]** _Classification and Tracking of Dynamic Objects with Multiple Sensors for Autonomous Driving in Urban Environments_. [[ref](https://www.semanticscholar.org/paper/Classification-and-Tracking-of-Dynamic-Objects-Darms-Rybski/6c9ce40060fa3efea7d04a4a0e36609592ed6ddf)]
* **[2014]** _Generating Omni-directional View of Neighboring Objects for Ensuring Safe Urban Driving_. [[ref](https://www.semanticscholar.org/paper/Generating-Omni-directional-View-of-Neighboring-Seo/29e53add392de54d439a6002c67e8af6e9baadeb)]
* **[2014]** _Autonomous Visual Navigation and Laser-Based Moving Obstacle Avoidance_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Visual-Navigation-and-Laser-Based-Cherubini-Spindler/089fa5a7babc906dc46a58f986c5ac8c46aa9017)]
* **[2014]** _Extending the Stixel World with online self-supervised color modeling for road-versus-obstacle segmentation_. [[ref](https://www.semanticscholar.org/paper/Extending-the-Stixel-World-with-online-self-Sanberg-Dubbelman/6dd60e0484931b284f49ab8204b011d153ff4967)]
* **[2014]** _Modeling Human Plan Recognition Using Bayesian Theory of Mind_. [[ref](https://www.semanticscholar.org/paper/Plan-Activity-and-Intent-Recognition-Baker-Tenenbaum/4cbb1ea46c09d11b0b986a7baaac7215006504f8)]
* **[2013]** _Focused Trajectory Planning for autonomous on-road driving_. [[ref](https://www.semanticscholar.org/paper/Focused-Trajectory-Planning-for-autonomous-on-road-Gu-Snider/03bf26d72d8cc0cf401c31e31c242e1894bd0890)]
* **[2013]** _Avoiding moving obstacles during visual navigation_. [[ref](https://www.semanticscholar.org/paper/Avoiding-moving-obstacles-during-visual-navigation-Cherubini-Grechanichenko/7c0e580c0f914086e9c918aef1df561253a71044)]
* **[2013]** _Mobile robot navigation system in outdoor pedestrian environment using vision-based road recognition_. [[ref](https://www.semanticscholar.org/paper/Mobile-robot-navigation-system-in-outdoor-Siagian-Chang/7163764c33c3d87c313568c056d50d1bedb25696)]
* **[2013]** _Obstacle detection and mapping in low-cost, low-power multi-robot systems using an Inverted Particle Filter_. [[ref](https://www.semanticscholar.org/paper/Obstacle-detection-and-mapping-in-low-cost-low-Kleppe-Skavhaug/646cc0e592b77d553cc77806e90d99420fb79a8e)]
* **[2013]** _Real-time estimation of drivable image area based on monocular vision_. [[ref](https://www.semanticscholar.org/paper/Real-time-estimation-of-drivable-image-area-based-Neto-Victorino/c50a769c2038e29d9e64077cd4749b6f8d389806)]
* **[2013]** _Road model prediction based unstructured road detection_. [[ref](https://www.semanticscholar.org/paper/Road-model-prediction-based-unstructured-road-Zuo-Yao/b8b2d3da341042d148ed2988216dbb3ddb6081ed)]
* **[2013]** _Selective Combination of Visual and Thermal Imaging for Resilient Localization in Adverse Conditions: Day and Night, Smoke and Fire_. [[ref](https://www.semanticscholar.org/paper/Selective-Combination-of-Visual-and-Thermal-Brunner-Peynot/85b4b1a9780a4bc22f84904a1cfc3eeeb605c9bd)]
* **[2012]** _Road Tracking Method Suitable for Both Unstructured and Structured Roads_. [[ref](https://www.semanticscholar.org/paper/International-Journal-of-Advanced-Robotic-Systems-Proch%C3%A1zka/4819fda4bc778454701f2a4b30db46ec56aa45bc)]
* **[2012]** _Autonomous Navigation and Sign Detector Learning_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Navigation-and-Sign-Detector-Learning-Ellis-Pugeault/0cffe50112452ecdcdaf0d11b33e12cf3c67213e)]
* **[2012]** _Design of a Multi-Sensor Cooperation Travel Environment Perception System for Autonomous Vehicle_. [[ref](https://www.semanticscholar.org/paper/Design-of-a-Multi-Sensor-Cooperation-Travel-Chen-Li/f5feb2a151c54ec9699924d401a66c193ddd3c8b)]
* **[2012]** _Learning in Reality: a Case Study of Stanley, the Robot That Won the Darpa Challenge_. [[ref](https://www.semanticscholar.org/paper/Learning-in-Reality-a-Case-Study-of-Stanley-the-Glaser-Hennig/01c1f49f5e7f4e7f5d005844aa9443769a2d9306)]
* **[2012]** _Portable and Scalable Vision-Based Vehicular Instrumentation for the Analysis of Driver Intentionality_. [[ref](https://www.semanticscholar.org/paper/Portable-and-Scalable-Vision-Based-Vehicular-Beauchemin-Bauer/c76b5bc64ffd6e13a6c22641b3926a803e5209d5)]
* **[2012]** _What could move? Finding cars, pedestrians and bicyclists in 3D laser data_. [[ref](https://www.semanticscholar.org/paper/What-could-move-Finding-cars-pedestrians-and-Wang-Posner/f56b01df806bc224d5babb71994915df4a08cb44)]
* **[2012]** _The Stixel World_. [[ref](https://www.semanticscholar.org/paper/The-Stixel-World-N-Im/5307f5e2ff2f0403a92b63418ca5812965dcfb90)]
* **[2011]** _Stereo-based road boundary tracking for mobile robot navigation_. [[ref](https://www.semanticscholar.org/paper/Stereo-based-road-boundary-tracking-for-mobile-Chiku-Miura/8bcbb1f13f2ab7f974ba30a0d68aeccf49082759)]
* **[2009]** _Autonomous Information Fusion for Robust Obstacle Localization on a Humanoid Robot_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Information-Fusion-for-Robust-Obstacle-Sridharan-Li/2365b361fb0e5cb801b22900a4c4a421c35ea639)]
* **[2009]** _Learning long-range vision for autonomous off-road driving_. [[ref](https://www.semanticscholar.org/paper/Learning-long-range-vision-for-autonomous-off-road-Hadsell-Sermanet/2d8f527d1a96b0dae209daa6a241cf3255a6ec0d)]
* **[2009]** _On-line road boundary modeling with multiple sensory features, flexible road model, and particle filter_. [[ref](https://www.semanticscholar.org/paper/On-line-road-boundary-modeling-with-multiple-Matsushita-Miura/0fcac22dceb7a7d49a8c792760ae47c500a804d9)]
* **[2008]** _The Area Processing Unit of Caroline - Finding the Way through DARPA's Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/The-Area-Processing-Unit-of-Caroline-Finding-the-Berger-Lipski/4b9db808c06635b784ce6c1409603c0487bcd684)]
* **[2008]** _Vehicle detection and tracking for the Urban Challenge_. [[ref](https://www.semanticscholar.org/paper/Vehicle-detection-and-tracking-for-the-Urban-Darms-Baker/757fbaa9881b9075409a9962819fda64d51307e1)]
* **[2007]** _Low cost sensing for autonomous car driving in highways_. [[ref](https://www.semanticscholar.org/paper/Low-cost-sensing-for-autonomous-car-driving-in-Gon%C3%A7alves-Godinho/b7f302bc8eb37220ba76c2d55325d218a7e03128)]
* **[2007]** _Stereo and Colour Vision Techniques for Autonomous Vehicle Guidance _. [[ref](https://www.semanticscholar.org/paper/Stereo-and-Colour-Vision-Techniques-for-Autonomous-Mark-Proefschrift/97325201f48351df5ef614a01a55f3da818aae0e)]
* **[2000]** _Real-time multiple vehicle detection and tracking from a moving vehicle_. [[ref](https://www.semanticscholar.org/paper/Real-time-multiple-vehicle-detection-and-tracking-Betke-Haritaoglu/864a7068c346ecbc4ef6c4da66e4c8bcc83fe560)]


#### Navigation and Planning

[Back to top](#contents)


* **[2016]** _A Self-Driving Robot Using Deep Convolutional Neural Networks on Neuromorphic Hardware_. [[ref](https://arxiv.org/abs/1611.01235)]
* **[2016]** _End to End Learning for Self-Driving Cars_. [[ref](https://arxiv.org/abs/1604.07316)]
* **[2016]** _A Survey of Motion Planning and Control Techniques for Self-driving Urban Vehicles_. [[ref](https://arxiv.org/abs/1604.07446)]
* **[2016]** _A Convex Optimization Approach to Smooth Trajectories for Motion Planning with Car-Like Robots_. [[ref](https://www.semanticscholar.org/paper/A-Convex-Optimization-Approach-to-Smooth-Zhu-Schmerling/785b22bbdb04f2ddd4233a4c40d798ed3194374f)]
* **[2016]** _Routing Autonomous Vehicles in Congested Transportation Networks: Structural Properties and Coordination Algorithms_. [[ref](https://arxiv.org/abs/1603.00939)]
* **[2016]** _Machine Learning for Visual Navigation of Unmanned Ground Vehicles_. [[ref](https://www.semanticscholar.org/paper/Machine-Learning-for-Visual-Navigation-of-Unmanned-Lenskiy-Lee/9b21934ec4f08ed3cd54a7e3a3c7c25b311e1ced)]
* **[2016]** _Real-time self-driving car navigation and obstacle avoidance using mobile 3D laser scanner and GNSS_. [[ref](https://www.semanticscholar.org/paper/Real-time-self-driving-car-navigation-and-obstacle-Li-Bao/4e8b5a99ae628eea43d7e7410cdfa7f8a2e847d5)]
* **[2016]** _Watch this: Scalable cost-function learning for path planning in urban environments_. [[ref](https://www.semanticscholar.org/paper/Watch-this-Scalable-cost-function-learning-for-Wulfmeier-Wang/d1e51c7e374dca4465a91300e98bfb27335be463)]
* **[2015]** _DeepDriving: Learning Affordance for Direct Perception in Autonomous Driving_. [[ref](https://www.semanticscholar.org/paper/DeepDriving-Learning-Affordance-for-Direct-Chen-Seff/3ba79761192aa4bddd3342db03aa8187516c0fab?citingPapersSort=is-influential&citingPapersLimit=10&citingPapersOffset=0&citedPapersSort=is-influential&citedPapersLimit=10&citedPapersOffset=0), [data](http://deepdriving.cs.princeton.edu/), [code](http://deepdriving.cs.princeton.edu/)]
* **[2015]** _Automatic Driving on Ill-defined Roads: An Adaptive, Shape-constrained, Color-based Method_. [[ref](https://www.semanticscholar.org/paper/Automatic-Driving-on-Ill-defined-Roads-An-Adaptive-Ososinski-Labrosse/36cfe2e94b7b99653e6565642236e0127d43ef5a), [data](http://www.aber.ac.uk/en/cs/research/ir/dss/#road-driving)]
* **[2015]** _A Framework for Applying Point Clouds Grabbed by Multi-Beam LIDAR in Perceiving the Driving Environment_. [[ref](https://www.semanticscholar.org/paper/A-Framework-for-Applying-Point-Clouds-Grabbed-by-Liu-Liang/907189aacae7bff389d6c6592d6e2586dab5168d)]
* **[2015]** _How Much of Driving Is Preattentive?_. [[ref](https://www.semanticscholar.org/paper/How-Much-of-Driving-Is-Preattentive--Pugeault-Bowden/bb9686ea6f154a64fbdc3551fe223da42663baa9)]
* **[2015]** _Map-building and Planning for Autonomous Navigation of a Mobile Robot_. [[ref](https://www.semanticscholar.org/paper/Map-building-and-Planning-for-Autonomous-G%C3%B3mez-Yu/fc5b5b96334d2a0d12ac2d69fa6d46640897f33e)]
* **[2014]** _A Multiple Attribute-based Decision Making model for autonomous vehicle in urban environment_. [[ref](https://www.semanticscholar.org/paper/A-Multiple-Attribute-based-Decision-Making-model-Chen-Zhao/a045d7008e47d4264e06b5d9f509ed505e100084)]
* **[2014]** _A prediction-based reactive driving strategy for highly automated driving function on freeways_. [[ref](https://www.semanticscholar.org/paper/A-prediction-based-reactive-driving-strategy-for-Bahram-Wolf/77d24bd1e83c23bb7cdf59ab06d575a66c03449a)]
* **[2014]** _An RRT-based navigation approach for mobile robots and automated vehicles_. [[ref](https://www.semanticscholar.org/paper/An-RRT-based-navigation-approach-for-mobile-robots-Garrote-Premebida/56cfb13218175d67bf6dc281686c797b8641a3d0)]
* **[2014]** _Image Feature-based Traversability Analysis for Mobile Robot Navigation in Outdoor Environment_. [[ref](https://www.semanticscholar.org/paper/Image-Feature-based-Traversability-Analysis-for-BEKHTI-KOBAYASHI/9fdf6ba484ee59cfac03a6c73e5177a9a70986c5)]
* **[2014]** _Speed Daemon: Experience-Based Mobile Robot Speed Scheduling_. [[ref](https://www.semanticscholar.org/paper/Speed-Daemon-Experience-Based-Mobile-Robot-Speed-Ostafew-Schoellig/9d3c816fb21bfa00d5a86cbb972a4ab7af59dbfb)]
* **[2014]** _Toward human-like motion planning in urban environments_. [[ref](https://www.semanticscholar.org/paper/Toward-human-like-motion-planning-in-urban-Gu-Dolan/30005949ebde80ebe3cd0b96b84a8dcb8b7f919a)]
* **[2013]** _Motion Estimation for Self-Driving Cars with a Generalized Camera_. [[ref](https://www.semanticscholar.org/paper/Motion-Estimation-for-Self-Driving-Cars-with-a-Lee-Fraundorfer/f7f775a4f484706ffbc524accb351cb564469f6a)]
* **[2013]** _Development of a Navigation Control System for an Autonomous Formula Sae-electric Race Car_. [[ref](https://www.semanticscholar.org/paper/Development-of-a-Navigation-Control-System-for-an-Drage/f55796a5f33836017de2cd8023b57efda9882c26)]
* **[2013]** _Low speed automation: Technical feasibility of the driving sharing in urban areas_. [[ref](https://www.semanticscholar.org/paper/Low-speed-automation-Technical-feasibility-of-the-Resende-Pollard/a34161c17343e8f41e200fe5288e2a4aaeafa25a)]
* **[2013]** _Path selection based on local terrain feature for unmanned ground vehicle in unknown rough terrain environment_. [[ref](https://www.semanticscholar.org/paper/Path-selection-based-on-local-terrain-feature-for-Kondo-Sunaga/e58506ef0f6721729d2f72c61e6bb46565b887de)]
* **[2013]** _Stereo-based Autonomous Navigation and Obstacle Avoidance_. [[ref](https://www.semanticscholar.org/paper/Stereo-based-Autonomous-Navigation-and-Obstacle-C%C3%A9sar-Mendes/be6789bd46d16afa45c8962560a56a89a9089355)]
* **[2012]** _Development of an Autonomous Vehicle for High-Speed Navigation and Obstacle Avoidance._ [[ref](https://www.semanticscholar.org/paper/Development-of-an-Autonomous-Vehicle-for-High-Ryu-Ogay/0941bcd18fdf52d9e25984ff067eebe6834ad7c6)]
* **[2012]** _Fast Vanishing-Point Detection in Unstructured Environments_. [[ref](https://www.semanticscholar.org/paper/Fast-Vanishing-Point-Detection-in-Unstructured-Moghadam-Starzyk/c02f52b8b80db037f92facbb605c5715513935fb)]
* **[2012]** _Navigation of an Autonomous Car Using Vector Fields and the Dynamic Window Approach_. [[ref](https://www.semanticscholar.org/paper/Navigation-of-an-Autonomous-Car-Using-Vector-Lima-Augusto/92411ee829021f09cb30186435d888547e00dd0f)]
* **[2012]** _Road direction detection based on vanishing-point tracking_. [[ref](https://www.semanticscholar.org/paper/Road-direction-detection-based-on-vanishing-point-Moghadam-Feng/d2691eb5a030a1b017a944c7fce319ccd4477730)]
* **[2012]** _Self-supervised learning to visually detect terrain surfaces for autonomous robots operating in forested terrain_. [[ref](https://www.semanticscholar.org/paper/Self-supervised-learning-to-visually-detect-Zhou-Xi/617740b12065ee88049ca9086695ba78ccd3f110)]
* **[2012]** _Visual Navigation for Mobile Robots_. [[ref](https://www.semanticscholar.org/paper/X-Visual-Navigation-for-Mobile-Robots-Andersen-Andersen/7ac3b3fb12f6b071bdc0d8627225efe415c03104)]
* **[2011]** _A new Approach for Robot Motion Planning using Rapidly-exploring Randomized Trees_. [[ref](https://www.semanticscholar.org/paper/A-new-Approach-for-Robot-Motion-Planning-using-Krammer-Granzer/7e084820c195b65e45e9138415f6cac7762f18dc)]
* **[2011]** _Driving me around the bend: Learning to drive from visual gist_. [[ref](https://www.semanticscholar.org/paper/Driving-me-around-the-bend-Learning-to-drive-from-Pugeault-Bowden/2cf7bddfe52d6ca8f5309c3b42d620065126b445)]
* **[2011]** _Optimized route network graph as map reference for autonomous cars operating on German autobahn_. [[ref](https://www.semanticscholar.org/paper/Optimized-route-network-graph-as-map-reference-for-Czerwionka-Wang/644b76b47c88335d40702b3045d4d3743fc13861)]
* **[2011]** _Template-based autonomous navigation and obstacle avoidance in urban environments_. [[ref](https://www.semanticscholar.org/paper/Template-based-autonomous-navigation-and-obstacle-Souza-Sales/65414da8f4a9beaac1df4d5ca0736f474e001096)]
* **[2010]** _Vision-Based Autonomous Navigation System Using ANN and FSM Control_ [[ref](https://www.semanticscholar.org/paper/Vision-Based-Autonomous-Navigation-System-Using-Sales-Shinzato/e1fcccdbc373c9bbd5bd970c34368e7e1aa56424)]
* **[2010]** _An optimal-control-based framework for trajectory planning, threat assessment, and semi-autonomous control of passenger vehicles in hazard avoidance scenarios_. [[ref](https://www.semanticscholar.org/paper/An-Optimal-control-based-Framework-for-Trajectory-Anderson-Peters/50c955ab0ca25d49204fe0b115669303508b41d0)]
* **[2010]** _Perception for Urban Driverless Vehicles: Design and Implementation_. [[ref](https://www.semanticscholar.org/paper/Perception-for-Urban-Driverless-Vehicles-Design-Benenson-Suarez/0f68760469015de7cf0b21f2b5ed2b0194bb6b81)]
* **[2009]** _Autonomous Offroad Navigation Under Poor GPS Conditions_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Offroad-Navigation-Under-Poor-GPS-Luettel-Himmelsbach/5168a3824d4b90399e16c42f2293c3bf66113d8a)]
* **[2009]** _Autonomous robot navigation in outdoor cluttered pedestrian walkways_. [[ref](https://www.semanticscholar.org/paper/Autonomous-robot-navigation-in-outdoor-cluttered-Saiki-Carballo/7f81a0e925124e9d5738a51fe41c001a908c68f6)]
* **[2009]** _Fast Path Planning in Uncertain Environments: Theory and Experiments_. [[ref](https://www.semanticscholar.org/paper/Fast-Path-Planning-in-Uncertain-Environments-Xu-Kurdila/88228325b82ff3bcd875628c31e34e9018179d3d)]
* **[2009]** _Trajectory Based Autonomous Vehicle following Using a Robotic Driver_. [[ref](https://www.semanticscholar.org/paper/Trajectory-Based-Autonomous-Vehicle-following-Spencer-Jones/f4f6dc62fe8c5fd309f45ebf5240f9c1c1c0b80a)]
* **[2008]** _A Robust Motion Planning Approach for Autonomous Driving in Urban Areas_. [[ref](https://www.semanticscholar.org/paper/A-Robust-Motion-Planning-Approach-for-Autonomous-Fiore-Yoshi/d3660d2f49958841d6d8486467213512772f9aac)]
* **[2008]** _Motion Planning in Urban Environments_. [[ref](https://www.semanticscholar.org/paper/Motion-Planning-in-Urban-Environments-Ferguson-Howard/8fa74131756a50c1562ebf1f03552779803aed67)]
* **[2008]** _Motion planning in urban environments: Part II_. [[ref](https://www.semanticscholar.org/paper/Motion-planning-in-urban-environments-Part-II-Ferguson-Howard/3c33381fa5dfecd02e4f935957831c3d2926bb0f)]
* **[2008]** _Planning Long Dynamically Feasible Maneuvers for Autonomous Vehicles_. [[ref](https://www.semanticscholar.org/paper/Planning-Long-Dynamically-Feasible-Maneuvers-for-Likhachev-Ferguson/1f8ca38a1fa455db3388c617697cc91300c59bc6)]
* **[2009]** _Anticipatory Driving for a Robot-Car Based on Supervised Learning_. [[ref](https://www.semanticscholar.org/paper/Anticipatory-Driving-for-a-Robot-Car-Based-on-Markelic-Kulvicius/ee9adb395ed68a2ce4c2a3909dc6d5a0fbf4e0f0)]
* **[2007]** _Online Speed Adaptation Using Supervised Learning for High-Speed, Off-Road Autonomous Driving_.[[ref](https://www.semanticscholar.org/paper/Online-Speed-Adaptation-Using-Supervised-Learning-Stavens-Hoffmann/9db82954df3f4ae829459dcb8719b8a8ed9f4bee)]
* **[2007]** _Predictive Active Steering Control for Autonomous Vehicle Systems_. [[ref](https://www.semanticscholar.org/paper/Predictive-Active-Steering-Control-for-Autonomous-Falcone-Borrelli/abd354d708b98fb60e0d827a41157491289e8d3c)]
* **[2006]** _Probabilistic Terrain Analysis For High-Speed Desert Driving_.[[ref](https://www.semanticscholar.org/paper/Probabilistic-Terrain-Analysis-For-High-Speed-Thrun-Montemerlo/b23a7882b35d0252e5f3011bff15c6dca46ef84e)]

#### Control

[Back to top](#contents)


* **[2016]** _Predictive Control for Autonomous Driving with Experimental Evaluation on a Heavy-duty Construction Truck_. [[ref](https://www.semanticscholar.org/paper/Predictive-Control-for-Autonomous-Driving-with-Lima-Se/de87a5d5fbae0733806ba965b2d70fd04596f6e9)]
* **[2015]** _Model Predictive Control of Autonomous Mobility-on-Demand Systems_. [[ref](https://arxiv.org/abs/1509.03985)]
* **[2015]** _Toward integrated motion planning and control using potential fields and torque-based steering actuation for autonomous driving_. [[ref](https://www.semanticscholar.org/paper/Toward-integrated-motion-planning-and-control-Galceran-Eustice/7b2f163eac946fac7351b0861c2b37fb19ffbaa5)]
* **[2013]** _Strategic decision making for automated driving on two-lane, one way roads using model predictive control_. [[ref](https://www.semanticscholar.org/paper/Strategic-decision-making-for-automated-driving-on-Nilsson-Sj%C3%B6berg/0055ca2e60a2ab5cb66c4191d09563dd7f3edd00)]
* **[2012]** _Autonomous vehicles control in the VisLab Intercontinental Autonomous Challenge_. [[ref](https://www.semanticscholar.org/paper/Autonomous-vehicles-control-in-the-VisLab-Broggi-Medici/708fdf9bfd3f7d671ced85221012ef27209b92bb)]
* **[2012]** _Optimal Planning and Control for Hazard Avoidance of Front-wheel Steered Ground Vehicles_. [[ref](https://www.semanticscholar.org/paper/Optimal-Planning-and-Control-for-Hazard-Avoidance-Peters/5d5a066547d60a673328cf6db34325910787ba48)]
* **[2009]** _Automatic Steering Methods for Autonomous Automobile Path Tracking_. [[ref](https://www.semanticscholar.org/paper/Automatic-Steering-Methods-for-Autonomous-Snider/18520721525ed81a6ffa6d8b1c7dcbd771e4a64b)]
* **[2009]** _Comparison of Three Control Methods for an Autonomous Vehicle_. [[ref](https://www.semanticscholar.org/paper/Comparison-of-Three-Control-Methods-for-an-Deshpande-Mathur/8fc0580499b0775db60096f52cd2f0ad2c6d24b5)]

#### Simulation

[Back to top](#contents)

* **[2016]** _Learning a Driving Simulator_. [[ref](https://arxiv.org/abs/1608.01230)]
* **[2014]** _From a Competition for Self-Driving Miniature Cars to a Standardized Experimental Platform: Concept, Models, Architecture, and Evaluation_. [[ref](https://arxiv.org/abs/1406.7768)]
* **[2014]** _Technical evaluation of the Carolo-Cup 2014 - A competition for self-driving miniature cars_. [[ref](https://www.semanticscholar.org/paper/Technical-evaluation-of-the-Carolo-Cup-2014-A-Zug-Steup/4f57643b95e854bb05fa0c037cbf8898accdbdef)]
* **[2014]** _Crowdsourcing as a methodology to obtain large and varied robotic data sets_. [[ref](https://www.semanticscholar.org/paper/Crowdsourcing-as-a-methodology-to-obtain-large-and-Croon-Gerke/8bdcb90d72eb0494f8f2635dad8ef05a66b8e445)]
* **[2014]** _Efficient Learning of Pre-attentive Steering in a Driving School Framework_. [[ref](https://www.semanticscholar.org/paper/Efficient-Learning-of-Pre-attentive-Steering-in-a-Rudzits-Pugeault/6a65272403a8bb999bc4e86eee3f919e3fbe813d)]
* **[2007]** _A Simulation and Regression Testing Framework for Autonomous Vehicles_. [[ref](https://www.semanticscholar.org/paper/A-Simulation-and-Regression-Testing-Framework-for-Miller-Cenk/c50ef42740ce03e5af9292f9ce1387b83bee8fed)]
* **[2006]** _Robot Competitions Ideal Benchmarks for Robotics Research_. [[ref](https://www.semanticscholar.org/paper/Robot-Competitions-Ideal-Benchmarks-for-Robotics-Behnke/71e5e9e8be8c870b22cadf58338f634ddd856050)]

#### Software Engineering

[Back to top](#contents)

1. **[2016]** _Evaluation of Sandboxed Software Deployment for Real-time Software on the Example of a Self-Driving Heavy Vehicle_. [[ref](https://arxiv.org/abs/1608.06759)]
* **[2014]** _Engineering the Hardware/Software Interface for Robotic Platforms - A Comparison of Applied Model Checking with Prolog and Alloy_. [[ref](https://arxiv.org/abs/1401.3985)]
* **[2014]** _Comparison of Architectural Design Decisions for Resource-Constrained Self-Driving Cars - A Multiple Case-Study_. [[ref](https://www.semanticscholar.org/paper/Comparison-of-Architectural-Design-Decisions-for-Berger-Dukaczewski/c89f47c93c62c107e6bd75acde89ee7417ebf244)]
* **[2014]** _(Re)liability of Self-driving Cars. An Interesting Challenge!_. [[ref](http://onlinelibrary.wiley.com/doi/10.1002/qre.1707/full)]
* **[2014]** _Explicating, Understanding, and Managing Technical Debt from Self-Driving Miniature Car Projects_. [[ref](http://ieeexplore.ieee.org/document/6974884/)]
* **[2014]** _Towards Continuous Integration for Cyber-Physical Systems on the Example of Self-Driving Miniature Cars_. [[ref](https://www.semanticscholar.org/paper/Towards-Continuous-Integration-for-Cyber-Physical-Berger/2ac2aa0285984f2ce57efa77aab4e372bbc3ee6c)]
* **[2014]** _Saving virtual testing time for CPS by analyzing code coverage on the example of a lane-following algorithm_. [[ref](http://dl.acm.org/citation.cfm?id=2593466)]
* **[2013]** _Parallel scheduling for cyber-physical systems: analysis and case study on a self-driving car_[[ref](http://dl.acm.org/citation.cfm?id=2502530)]
* **[2012]** _SAFER: System-level Architecture for Failure Evasion in Real-time Applications_. [[ref](https://www.semanticscholar.org/paper/SAFER-System-level-Architecture-for-Failure-Kim-Bhatia/ff05797dcc041d04f9ed277269916ad6ff92f1f0)]
* **[2011]** _A Flexible Real-Time Control System for Autonomous Vehicles_. [[ref](https://www.semanticscholar.org/paper/A-Flexible-Real-Time-Control-System-for-Autonomous-Meyer-Strobel/f07956d0031ff046c5c719296f7916d7897fdd21)]
* **[2010]** _Automating acceptance tests for sensor- and actuator-based systems on the example of autonomous vehicles_. [[ref](https://www.semanticscholar.org/paper/Automating-acceptance-tests-for-sensor-and-Berger/3bc567143118f8fb34e0460cc3424701683c2511)]
* **[2007]** _Software & Systems Engineering Process and Tools for the Development of Autonomous Driving Intelligence_ [[ref](https://www.semanticscholar.org/paper/Software-Systems-Engineering-Process-and-Tools-for-Basarke-Berger/c564b62cd7df2ed47bb9a6266cc19c83024bc390)]

#### Human Machine Interaction

[Back to top](#contents)

* **[2015]** _User interface considerations to prevent self-driving carsickness_. [[ref](http://dl.acm.org/citation.cfm?id=2809754)]
* **[2014]** _Public Opinion about Self-driving Vehicles_. [[ref](https://www.semanticscholar.org/paper/Public-Opinion-about-Self-driving-Vehicles-Schoettle-Sivak/4984ed8ae3355d58cfad2bd27cb2bc2488cb0e6a)]
* **[2014]** _Setting the Stage for Self-driving Cars: Exploration of Future Autonomous Driving Experiences_. [[ref](https://www.semanticscholar.org/paper/Setting-the-Stage-for-Self-driving-Cars-Pettersson/df428d8015b92902416d07379fb3415a12d64e3f)]
* **[2014]** _Three Decades of Driver Assistance Systems: Review and Future Perspectives_. [[ref](https://www.semanticscholar.org/paper/Three-Decades-of-Driver-Assistance-Systems-Review-Bengler-Dietmayer/2c6d7bcf2ae79b73ad5888f591e159a3d994322b)]
* **[2013]** _Review Article Automotive Technology and Human Factors Research: Past, Present, and Future_. [[ref](https://www.semanticscholar.org/paper/Review-Article-Automotive-Technology-and-Human-Akamatsu-Green/dfe6df56cd5418ce9d6df938858542097157d3e8)]
* **[2012]** _Safe semi-autonomous control with enhanced driver modeling_. [[ref](https://www.semanticscholar.org/paper/Safe-semi-autonomous-control-with-enhanced-driver-Vasudevan-Shia/8e36ebbb6e5409aa911e4121ca37c455ff157218)]
* **[2012]** _Semi-autonomous Car Control Using Brain Computer Interfaces_. [[ref](https://www.semanticscholar.org/paper/Semi-autonomous-Car-Control-Using-Brain-Computer-G%C3%B6hring-Latotzky/e35864047f5b4ac3398ad6f242d2f1407c965f37)]
* **[2011]** _iDriver - Human Machine Interface for Autonomous Cars_. [[ref](https://www.semanticscholar.org/paper/iDriver-Human-Machine-Interface-for-Autonomous-Reuschenbach-Wang/3d7107cdd11af698790736ba5fc9f23cc3f52d04)]
* **[2010]** _Driving an Autonomous Car with Eye Tracking Driving an Autonomous Car with Eye Tracking_. [[ref](https://www.semanticscholar.org/paper/Driving-an-Autonomous-Car-with-Eye-Tracking-Wang-Latotzky/b3aa092b84ae6c9b924ed1a0d9681bbb342249b3)]
* **[2010]** _Remote Controlling an Autonomous Car with an Iphone_. [[ref](https://www.semanticscholar.org/paper/Remote-Controlling-an-Autonomous-Car-with-an-Wang-Ganjineh/a0032e1fbedf61b2a74cfd5f4a9a3edb52689064)]
* **[2009]** _Car-driver Cooperation in Future Vehicles I. Adas and Autonomuos Vehicle_. [[ref](https://www.semanticscholar.org/paper/Car-driver-Cooperation-in-Future-Vehicles-I-Adas-Broggi-Mazzei/c2cc8ad2087d753cc67061d490f966de2c1373a1)]
* **[2009]** _Driver Inattention Detection based on Eye Gaze - Road Event Correlation_. [[ref](https://www.semanticscholar.org/paper/Driver-Inattention-Detection-based-on-Eye-Gaze-Fletcher-Zelinsky/b46f706a9df142f36a58cd7a84c88962f85d93b5)]

#### Infrastructure

[Back to top](#contents)

* **[2014]** _Control of Robotic Mobility-On-Demand Systems: a Queueing-Theoretical Perspective_. [[ref](https://arxiv.org/abs/1404.4391)]
* **[2014]** _Priority-based Intersection Control Framework for Self-Driving Vehicles: Agent-based Model Development and Evaluation_. [[ref](https://www.researchgate.net/publication/271738793_Priority-based_Intersection_Control_Framework_for_Self-Driving_Vehicles_Agent-based_Model_Development_and_Evaluation)]
* **[2014]** _A lattice-based approach to multi-robot motion planning for non-holonomic vehicles_. [[ref](https://www.semanticscholar.org/paper/A-lattice-based-approach-to-multi-robot-motion-Cirillo-Uras/74ec451f463c4931c73f35cf327893ac2595e876)]
* **[2005]** _Cooperative autonomous driving: intelligent vehicles sharing city roads_. [[ref](https://www.semanticscholar.org/paper/Cooperative-autonomous-driving-intelligent-Baber-Kolodko/a42f42fa95d8ee6498dff905ed4848437a8f0084)]
* **[2014]** _Achieving Integrated Convoys: Cargo Unmanned Ground Vehicle Development and Experimentation_. [[ref](https://www.semanticscholar.org/paper/Achieving-Integrated-Convoys-Cargo-Unmanned-Ground-Zych-Silver/364ecf6f5af89c7b3e3d11d2269581b420edb003)]
* **[2014]** _Priority-based coordination of mobile robots_. [[ref](https://www.semanticscholar.org/paper/Priority-based-coordination-of-mobile-robots-Gregoire/5fdd722822fe2722d8c90e35461538dbfca10a5e)]
* **[2012]** _Exploration and Mapping with Autonomous Robot Teams Results from the Magic 2010 Competition_. [[ref](https://www.semanticscholar.org/paper/Exploration-and-Mapping-with-Autonomous-Robot-Olson-Strom/9bf0e62b5b2343a0b509a1ac7a658be587a5c37d)]
* **[2012]** _Progress toward multi-robot reconnaissance and the MAGIC 2010 competition_. [[ref](https://www.semanticscholar.org/paper/Progress-toward-multi-robot-reconnaissance-and-the-Olson-Strom/617943baefd909bbf06787fcb8b18b943820c87e)]

#### Law and Society

[Back to top](#contents)

* **[2016]** _Autonomous Vehicle Technology: A Guide for Policymakers_. [[ref](https://www.semanticscholar.org/paper/Autonomous-Vehicle-Technology-A-Guide-for-Anderson-Kalra/a0231f6ab2a9feaef92d5481149cdb2142aaeb02)]
* **[2014]** _**WHITE PAPER** Self-driving Vehicles: Current Status of Autonomous Vehicle Development and Minnesota Policy Implications Preliminary White Paper_. [[ref](https://www.semanticscholar.org/paper/Self-driving-Vehicles-Current-Status-of-Autonomous-Lari-Douma/581075c89f6a3945fa43d61aac1329d1e43f9fa3)]
* **[2014]** _Are We Ready for Driver-less Vehicles? Security vs. Privacy- A Social Perspective_. [[ref](https://www.semanticscholar.org/paper/Are-We-Ready-for-Driver-less-Vehicles-Security-vs-Acharya/ec5b5c434f9d0bfc3954c212226d436e32bcf7d5)]
* **[2014]** _A Survey of Public Opinion about Autonomous and Self-driving_.[[ref](https://www.semanticscholar.org/paper/A-Survey-of-Public-Opinion-about-Autonomous-and-Schoettle-Sivak/5d983c2d2160b9c159b2cdcfcfaded01a4ce2ad6)]
* **[2013]** _Autonomous vehicle social behavior for highway entrance ramp management_. [[ref](https://www.semanticscholar.org/paper/Autonomous-vehicle-social-behavior-for-highway-Wei-Dolan/86482726040d4a924ee339043e4606625a8f64fd)]

---------------
#### Datasets

[Back to top](#contents)

* **[2018-March]** _The ApolloScape Dataset for Autonomous Driving_. [[ref](https://arxiv.org/pdf/1803.06184.pdf)]
* **[2016-Oct]** _Udacity Open Sourcing 223GB of Driving Data_. [[ref](https://medium.com/udacity/open-sourcing-223gb-of-mountain-view-driving-data-f6b5593fbfa5)] [[dataset](https://github.com/udacity/self-driving-car/tree/master/datasets)]
* **[2016-08-02]** _comma.ai driving dataset_. [[ref](https://archive.org/details/comma-dataset)]
* [Oxford's Robotic Car](http://robotcar-dataset.robots.ox.ac.uk/)
* [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/raw_data.php)
* [University of Michigan North Campus Long-Term Vision and LIDAR Dataset](http://robots.engin.umich.edu/nclt/)
* [University of Michigan Ford Campus Vision and Lidar Data Set](http://robots.engin.umich.edu/SoftwareData/Ford)
* [DIPLECS Autonomous Driving Datasets (2015)](http://cvssp.org/data/diplecs/)
* [Velodyne SLAM Dataset from Karlsruhe Institute of Technology](http://www.mrt.kit.edu/z/publ/download/velodyneslam/dataset.html)
* [SYNTHetic collection of Imagery and Annotations (SYNTHIA)](http://synthia-dataset.net/)
* [Cityscape Dataset](https://www.cityscapes-dataset.com/)
* [CSSAD Dataset](http://aplicaciones.cimat.mx/Personal/jbhayet/ccsad-dataset)
* [Daimler Urban Segmetation Dataset](http://www.6d-vision.com/scene-labeling)
* [Self Racing Cars - XSens/Fairchild Dataset](http://data.selfracingcars.com/)
* [MIT AGE Lab](http://lexfridman.com/automated-synchronization-of-driving-data-video-audio-telemetry-accelerometer/)
* [Yet Another Computer Vision Index To Datasets (YACVID)](http://yacvid.hayko.at/)
* [KUL Belgium Traffic Sign Dataset](http://www.vision.ee.ethz.ch/~timofter/traffic_signs/)
* [LISA: Laboratory for Intelligent & Safe Automobiles, UC San Diego Datasets](http://cvrr.ucsd.edu/LISA/datasets.html)
* [Multisensory Omni-directional Long-term Place Recognition (MOLP) dataset for autonomous driving](http://hcr.mines.edu/code/MOLP.html)  [paper](https://arxiv.org/abs/1704.05215)



-------------------

#### Implementations and libraries

[Back to top](#contents)


- [self-driving-car](https://github.com/udacity/self-driving-car) : The Udacity open source self-driving car project https://udacity.com/self-driving-car
- [self-driving-car-sim](https://github.com/udacity/self-driving-car-sim) : A self-driving car simulator built with Unity
- [vehicle-detection](https://github.com/tatsuyah/vehicle-detection) :Vehicle detection using machine learning and computer vision techniques for Udacity's self-driving car course.
- [donkey](https://github.com/wroscoe/donkey) : a python self driving library
- [awesome-autonomous-vehicles](https://github.com/takeitallsource/awesome-autonomous-vehicles) : Curated List of Self-Driving Cars and Autonomous Vehicles Resources
- [DeepGTAV](https://github.com/aitorzip/DeepGTAV) : A plugin for GTAV that transforms it into a vision-based self-driving car research environment.
- [self-driving-car](https://github.com/ndrplz/self-driving-car) : 
Udacity Self-Driving Car Engineer Nanodegree projects.
- [udacity/CarND-LaneLines-P1](https://github.com/udacity/CarND-LaneLines-P1) : Lane Finding Project for Self-Driving Car ND
- [self-driving-toy-car](https://github.com/experiencor/self-driving-toy-car) : A self driving toy car using end-to-end learning
- [stanford_self_driving_car_code](https://github.com/emmjaykay/stanford_self_driving_car_code) : 
Stanford Code From Cars That Entered DARPA Grand Challenges
- [self-driving-car-nd](https://github.com/jessicayung/self-driving-car-nd) : Udacity's Self-Driving Car Nanodegree project files and notes.
- [How_to_simulate_a_self_driving_car](https://github.com/llSourcell/How_to_simulate_a_self_driving_car) : This is the code for "How to Simulate a Self-Driving Car" by Siraj Raval on Youtube
- [Cherry-Autonomous-Racecar](https://github.com/DJTobias/Cherry-Autonomous-Racecar) : Implementation of the CNN from End to End Learning for Self-Driving Cars on a Nvidia Jetson TX1 using Tensorflow and ROS
- [sdsandbox](https://github.com/tawnkramer/sdsandbox) : This provides a sandbox simulator for training a self-driving car. This uses Unity for simulation and Python with Keras and Tensorflow for training. Recently updated to work on Python 3.4+ and Keras 2+
- [Self-Driving-Car-AI](https://github.com/JianyangZhang/Self-Driving-Car-AI) : A simple self-driving car AI python script using the deep Q-learning algorithm
- [self-driving-car](https://github.com/gtarobotics/self-driving-car) : Self Driving Car development tools and technologies from GTA Robotics Community members https://meetup.com/gta-robotics
- [Behavioral-Cloning](https://github.com/upul/Behavioral-Cloning) : Third Project of the Udacity Self-Driving Car Nanodegree Program
- [Autopilot](https://github.com/akshaybahadur21/Autopilot) : A self driving car model for humans.
- [metacar](https://github.com/thibo73800/metacar) :  reinforcement learning environment for self-driving cars in the browser. https://www.metacar-project.com/
- [gym-duckietown](https://github.com/duckietown/gym-duckietown) : Self-driving car simulator for the Duckietown universe http://duckietown.org
- [SDCND-Prerequisites](https://github.com/ncondo/SDCND-Prerequisites) : A list of recommended prerequisites for Udacity's Self Driving Car Nanodegree
- [CarND-Extended-Kalman-Filter-Project](https://github.com/udacity/CarND-Extended-Kalman-Filter-Project) : 
Self-Driving Car Nanodegree Program Starter Code for the Extended Kalman Filter Project
- [SDC-P5](https://github.com/diyjac/SDC-P5) : Udacity Self-Driving Car Project 5: Vehicle Detection and Tracking
- [deepdrive-universe](https://github.com/OSSDC/deepdrive-universe) : Run self-driving car agents in GTAV Universe
- [CarND-TensorFlow-Lab](https://github.com/udacity/CarND-TensorFlow-Lab) : TensorFlow Lab for Self-Driving Car ND
- [Self-Driving-Car-Demo](https://github.com/llSourcell/Self-Driving-Car-Demo) : Self Driving Car Demo for Fresh Machine Learning #6
- [Self-Driving-Car-3D-Simulator-With-CNN](https://github.com/sagar448/Self-Driving-Car-3D-Simulator-With-CNN) :
- [self_driving_cars_explained](https://github.com/llSourcell/self_driving_cars_explained) : This is the code for "Self Driving Cars Explaioned" by Siraj Raval on Youtube
- [awesome-self-driving-cars](https://github.com/philbort/awesome-self-driving-cars) : An awesome list of self-driving cars
- [DRL_based_SelfDrivingCarControl](https://github.com/MLJejuCamp2017/DRL_based_SelfDrivingCarControl) : Deep Reinforcement Learning (DQN) based Self Driving Car Control with Vehicle Simulator
- [self-driving](https://github.com/BoltzmannBrain/self-driving) : Machine learning models for self-driving cars
- [Self-Driving-Car-Vehicle-Detection](https://github.com/JamesLuoau/Self-Driving-Car-Vehicle-Detection) : Self Driving Car Vehicle Detection
- [behavioral-cloning](https://github.com/navoshta/behavioral-cloning) : 
Behavioral cloning: end-to-end learning for self-driving cars. 
- [keras-steering-angle-visualizations](https://github.com/jacobgil/keras-steering-angle-visualizations) : Visualizations for understanding the regressed wheel steering angle for self driving cars
- [CarND-Traffic-Sign-Classifier-Project](https://github.com/jeremy-shannon/CarND-Traffic-Sign-Classifier-Project) : 
My work-through of the Jupyter notebook for the Udacity Self-Driving Car Nanodegree program Project 2 - Traffic Sign Classifier
- [Udacity-SDC-Radar-Driver-Micro-Challenge](https://github.com/diyjac/Udacity-SDC-Radar-Driver-Micro-Challenge) : Udacity Self-Driving Car Radar Driver Micro Challenge
- [CarND-Vehicle-Detection](https://github.com/jeremy-shannon/CarND-Vehicle-Detection) : https://github.com/jeremy-shannon/CarND-Vehicle-Detection
- [SDC-System-Integration](https://github.com/diyjac/SDC-System-Integration) : Self Driving Car Engineer Nanodegree System Integration Capstone Project
- [MIT-6.S094](https://github.com/Carmezim/MIT-6.S094) : 
MIT-6.S094: Deep Learning for Self-Driving Cars Assignments solutions
- [selfdriving-robot-car](https://github.com/bdjukic/selfdriving-robot-car) : Raspberry Pi based robot car which is capable of autonomous driving using Deep Neural network.
- [Road-Semantic-Segmentation](https://github.com/NikolasEnt/Road-Semantic-Segmentation) : Udacity Self-Driving Car Engineer Nanodegree. Project: Road Semantic Segmentation
- [brahms](https://github.com/spicavigo/brahms) : Udacity's Self Driving Car Simulator (Challenge #2)
- [End-to-End-Learning-for-Self-Driving-Cars](https://github.com/ymshao/End-to-End-Learning-for-Self-Driving-Cars) : End-to-End learning to train a simulated car keep on the track without crash
- [Vehicle-Detection-and-Tracking](https://github.com/NikolasEnt/Vehicle-Detection-and-Tracking) : 
Udacity Self-Driving Car Engineer Nanodegree. Project: Vehicle Detection and Tracking
- [galvaneye](https://github.com/pseudoyim/galvaneye) : Self-driving RC car using OpenCV and Keras
- [CarND-Behavioral-Cloning-Project](https://github.com/jeremy-shannon/CarND-Behavioral-Cloning-Project) : My solution to the Udacity Self-Driving Car Engineer Nanodegree behavioral cloning project.
- [Lane-Detection](https://github.com/davidawad/Lane-Detection) : Using OpenCV to detect Lane lines on Roads
- [Semantic_Segmentation_for_Autonomous_Driving](https://github.com/TheMoskowitz/Semantic_Segmentation_for_Autonomous_Driving) : Various networks that could be the basis of a vision system for self-driving cars
- [MIT-6.S094-Deep-Learning-for-Self-Driving-Cars](https://github.com/init27/MIT-6.S094-Deep-Learning-for-Self-Driving-Cars) :

---------------

#### Startups

[Back to top](#contents)

- [44 Corporations Working On Autonomous Vehicles](https://drivinghacks.quora.com/Quicklook-44-Corporations-Working-On-Autonomous-Vehicles)
- [Moving Bits and Atoms at Scale – Uber Marketplace Architecture](https://docs.google.com/presentation/d/1aAkDp5JViza6UVT9Dbi02MI0ByE8iOu8UNMcotXR0cM/pub?start=false&loop=false&delayms=3000&slide=id.g1db52c1b40_0_232)
- [9 Startups In India Working On Self Driving Technology](https://analyticsindiamag.com/9-startups-india-working-self-driving-technology/)
- [mapped-top-263-companies-racing-toward-autonomous-cars](https://www.wired.com/2017/05/mapped-top-263-companies-racing-toward-autonomous-cars/)

------

[Back to top](#contents)

- Volkswagen Group of America
- Mercedes Benz
- [Google](https://www.google.com/selfdrivingcar/)
- Delphi Automotive
- [Tesla Motors](https://www.tesla.com/autopilot)
- Bosch
- Nissan
- GM Cruise LLC
- BMW
- Honda
- Ford
- Zoox, Inc.
- [Drive.ai](https://www.drive.ai/)
- Faraday & Future Inc.
- Baidu USA LLC
- Wheego Electric Cars Inc.
- Valeo North America, Inc.
- NextEV USA, Inc.
- Telenav, Inc.
- NVIDIA Corporation
- AutoX Technologies Inc
- Subaru
- [Udacity, Inc](https://in.udacity.com/course/self-driving-car-engineer-nanodegree--nd013)
- [Navya Inc](http://navya.tech/en/).
- Renovo Motors Inc
- UATC LLC (Uber)
- PlusAi Inc
- [Nuro, Inc](https://nuro.ai/)
- CarOne LLC
- Apple Inc.

-----------

Reaserch labs

* [Center for Automotive Research at Stanford](https://cars.stanford.edu/) 
* [SAIL-TOYOTA Center for AI Research at Stanford](http://aicenter.stanford.edu/research/)
* [Berkeley DeepDrive](http://bdd.berkeley.edu/)
* [Princeton Autonomous Vehicle Engineering](http://pave.princeton.edu/)
* [University of Maryland Autonomous Vehicle Laboratory](http://www.avl.umd.edu/)
* [University of Waterloo WAVE Laboratory](http://wavelab.uwaterloo.ca/)
* [Oxford Robotics Institute – Autonomous Systems](http://mrg.robots.ox.ac.uk/)
* [Autonomous Lab - Freie Universität Berlin](http://autonomos-labs.com/)
* [Honda Research Institute - USA](http://usa.honda-ri.com/Pages/Research%20Area/Detail.aspx?listId=2)
* [Toyota-CSAIL Research Center at MIT](http://toyota.csail.mit.edu/)
* [Princeton Vision & Robotics](http://vision.princeton.edu/research.html)
* [CMU The Robotic Institute Vision and Autonomous Systems Center (VASC)](http://www.ri.cmu.edu/research_center_detail.html?type=aboutcenter&center_id=4&menu_id=262)


---------

![AVSmartMobilityLandscape_](https://sudocat.sh/wp-content/uploads/2018/06/AVSmartMobilityLandscape_.png)
[Back to top](#contents)

---------------
---------------


#### Appendix 

reference images

[Back to top](#contents)

----

![swift_autonomousvehicles](https://www.swiftnav.com/sites/default/files/swift_autonomousvehicles.jpg)

-----------

![bec963b2213dc3d11cdec4eb265c62fb](https://www.osa-opn.org/opn/media/Images/Articles/2018/1801/Features/Hecht-img4.jpg?width=1200)

---------

![UBER-SELFDRIVING-SENSORS](https://fingfx.thomsonreuters.com/gfx/rngs/UBER-SELFDRIVING-SENSORS/010061BR2TH/UBER-SELFDRIVING-SENSORS.jpg)

----------

![autonomous-infographic-](https://www.intel.ie/content/dam/www/public/emea/xe/en/images/it-managers/autonomous-infographic-16x9.jpg.rendition.intel.web.1648.927.jpg)

source: [Intel – Autonomous Cars](https://www.intel.ie/content/www/ie/en/it-managers/autonomous-cars.html)

---------

![Future-of-Transportation-Stack_V3-TA](https://media.wired.com/photos/592652fb8d4ebc5ab8069db7/master/w_1132,c_limit/Future-of-Transportation-Stack_V3-TA.jpg)

---------

![1-unbundling-car](https://cbi-blog.s3.amazonaws.com/blog/wp-content/uploads/2016/05/1-unbundling-car.png)

-----------

![Where_In_The_World_Are_Self_Driving_Cars_Final-1024x857](https://insuranceblog.accenture.com/wp-content/uploads/2017/01/Where_In_The_World_Are_Self_Driving_Cars_Final-1024x857.png)




------

![car-infographic-1024x716](https://b-i.forbesimg.com/chunkamui/files/2013/05/car-infographic-1024x716.jpg)

---------

![csm_20170302_2025AD_Infographic_Sensors_7338bee200](https://www.2025ad.com/fileadmin/_processed_/a/a/csm_20170302_2025AD_Infographic_Sensors_7338bee200.jpg)


----------

![Impact_e714e59576](https://www.2025ad.com/fileadmin/_processed_/7/2/csm_240518_2025AD_Infographic_Economic-Impact_e714e59576.jpg)

---------

![Development_final_cb5d6a9d5d](https://www.2025ad.com/fileadmin/_processed_/8/1/csm_2025AD_Infographic_Urban-Development_final_cb5d6a9d5d.jpg)


-----------

![csm_20171025_2025AD_Blog_Infographic_Ethics_and_autonomous_vehicles_cae6a85d5a](https://www.2025ad.com/fileadmin/_processed_/c/0/csm_20171025_2025AD_Blog_Infographic_Ethics_and_autonomous_vehicles_cae6a85d5a.jpg)



----------
------------
