

#### A brief survey :AI in transportation->case study on (autonomous vehicles->self driving car industry)

-------------

<img src="https://github.com/gopala-kr/a-week-in-wild-ai/blob/master/04-ai-in-transportation/1_EsvRsQAC19pc_wRaXpJ6FA.gif" width="1000" height="400" />

---------------

#### Timeline

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

--------------

#### The why and how

- [The Unintended Ways Self-Driving Cars Will Change Our World](https://medium.com/swlh/the-unintended-ways-self-driving-cars-will-change-our-world-3b15d1db9026)
- [Why do we need self-driving cars?](https://www.quora.com/Why-do-we-need-self-driving-cars-1)
- [Andrew Ng: Do we really need self driving cars?](https://www.quora.com/Andrew-Ng-Do-we-really-need-self-driving-cars)
- [Top 20 Pros and Cons Associated With Self-Driving Cars](https://www.autoinsurancecenter.com/top-20-pros-and-cons-associated-with-self-driving-cars.htm)
- [Why do we need Driverless Cars?](https://www.quora.com/Why-do-we-need-Driverless-Cars)
- [We don't need fully self-driving cars to save lives](https://www.usatoday.com/story/tech/columnist/2018/02/04/we-dont-need-fully-self-driving-cars-save-lives/1085965001/)
- [~$1 trillion of real estate is on the move … here’s why](https://medium.com/99-mph/1-trillion-of-real-estate-is-on-the-move-heres-why-94ee9233e5eb)
- [waymo](https://medium.com/waymo)
- [MIT 6.S094:Deep Learning for Self-Driving Cars 2018 Lecture 1 Notes](https://hackernoon.com/mit-6-s094-deep-learning-for-self-driving-cars-2018-lecture-1-notes-807be1a50893)
- [MIT 6.S094: Deep Learning for Self-Driving Cars 2018 Lecture 2 Notes](https://hackernoon.com/mit-6-s094-deep-learning-for-self-driving-cars-2018-lecture-2-notes-e283b9ec10a0)
- [MIT 6.S094: Deep Learning for Self-Driving Cars 2018 Lecture 3 Notes: Deep Reinforcement Learning](https://hackernoon.com/mit-6-s094-deep-learning-for-self-driving-cars-2018-lecture-3-notes-deep-reinforcement-learning-fe9a8592e14a)
- [MIT 6.S094: Deep Learning for Self-Driving Cars 2018 Lecture 4 Notes: Computer Vision](https://hackernoon.com/mit-6-s094-deep-learning-for-self-driving-cars-2018-lecture-4-notes-computer-vision-f591f14b3b99)
- [MIT 6.S094: Deep Learning for Self-Driving Cars 2018 Lecture 5 Notes: Deep Learning for Human Sensing](https://hackernoon.com/mit-6-s094-deep-learning-for-self-driving-cars-2018-lecture-5-notes-deep-learning-for-human-5cb0f53e4f15)


--------------

<table class="wikitable">
<caption>SAE (J3016) Autonomy Levels
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
<h2><span class="mw-headline" id="Technical_challenges">Technical challenges</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Autonomous_car&amp;action=edit&amp;section=6" title="Edit section: Technical challenges">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<div role="note" class="hatnote navigation-not-searchable">Main article: <a href="/wiki/Hybrid_navigation" title="Hybrid navigation">Hybrid navigation</a></div>
<p>The challenge for driverless car designers is to produce control systems capable of analyzing sensory data in order to provide accurate detection of other vehicles and the road ahead.<sup id="cite_ref-50" class="reference"><a href="#cite_note-50">&#91;50&#93;</a></sup> Modern self-driving cars generally use <a href="/wiki/Bayes%27_theorem" title="Bayes&#39; theorem">Bayesian</a> <a href="/wiki/Simultaneous_localization_and_mapping" title="Simultaneous localization and mapping">simultaneous localization and mapping</a> (SLAM) algorithms,<sup id="cite_ref-IEEE1_51-0" class="reference"><a href="#cite_note-IEEE1-51">&#91;51&#93;</a></sup> which fuse data from multiple sensors and an off-line map into current location estimates and map updates. Google is developing a variant called SLAM, with detection and tracking of other moving objects (DATMO), which also handles obstacles such as cars and pedestrians. Simpler systems may use roadside <a href="/wiki/Real-time_locating_system" title="Real-time locating system">real-time locating system</a> (RTLS) technologies to aid localization. Typical sensors include <a href="/wiki/Lidar" title="Lidar">Lidar</a>, <a href="/wiki/Stereo_vision" class="mw-redirect" title="Stereo vision">stereo vision</a>, <a href="/wiki/GPS" class="mw-redirect" title="GPS">GPS</a> and <a href="/wiki/Inertial_measurement_unit" title="Inertial measurement unit">IMU</a>.<sup id="cite_ref-arxiv_52-0" class="reference"><a href="#cite_note-arxiv-52">&#91;52&#93;</a></sup><sup id="cite_ref-IEEE2_53-0" class="reference"><a href="#cite_note-IEEE2-53">&#91;53&#93;</a></sup> <a href="/wiki/Udacity" title="Udacity">Udacity</a> is developing an open-source software stack.<sup id="cite_ref-54" class="reference"><a href="#cite_note-54">&#91;54&#93;</a></sup> Control systems on autonomous cars may use <a href="/wiki/Sensor_Fusion" class="mw-redirect" title="Sensor Fusion">Sensor Fusion</a>, which is an approach that integrates information from a variety of sensors on the car to produce a more consistent, accurate, and useful view of the environment.<sup id="cite_ref-55" class="reference"><a href="#cite_note-55">&#91;55&#93;</a></sup>
</p><p>Driverless vehicles require some form of <a href="/wiki/Machine_vision" title="Machine vision">machine vision</a> for the purpose of visual object recognition. Autonomous cars are being developed with <a href="/wiki/Deep_neural_networks" class="mw-redirect" title="Deep neural networks">deep neural networks</a>,<sup id="cite_ref-arxiv_52-1" class="reference"><a href="#cite_note-arxiv-52">&#91;52&#93;</a></sup> a type of <a href="/wiki/Deep_learning" title="Deep learning">deep learning</a> architecture with many computational stages, or levels, in which neurons are simulated from the environment that activate the network.<sup id="cite_ref-science_56-0" class="reference"><a href="#cite_note-science-56">&#91;56&#93;</a></sup> The neural network depends on an extensive amount of data extracted from real-life driving scenarios,<sup id="cite_ref-arxiv_52-2" class="reference"><a href="#cite_note-arxiv-52">&#91;52&#93;</a></sup> enabling the neural network to "learn" how to execute the best course of action.<sup id="cite_ref-science_56-1" class="reference"><a href="#cite_note-science-56">&#91;56&#93;</a></sup>
</p><p>In May 2018, researchers from MIT announced that they had built an autonomous car that can navigate unmapped roads.<sup id="cite_ref-57" class="reference"><a href="#cite_note-57">&#91;57&#93;</a></sup> Researchers at their Computer Science and Artificial Intelligence Laboratory (CSAIL) have developed a new system, called MapLite, which allows self-driving cars to drive on roads that they have never been on before, without using 3D maps. The system combines the GPS position of the vehicle, a "sparse topological map" such as <a href="/wiki/OpenStreetMap" title="OpenStreetMap">OpenStreetMap</a>, (i.e. having 2D features of the roads only), and a series of sensors that observe the road conditions.<sup id="cite_ref-58" class="reference"><a href="#cite_note-58">&#91;58&#93;</a></sup>
</p>
<h2><span class="mw-headline" id="Testing">Testing</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Autonomous_car&amp;action=edit&amp;section=7" title="Edit section: Testing">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<p>Testing vehicles with varying degrees of autonomy can be done physically, in closed environments,<sup id="cite_ref-59" class="reference"><a href="#cite_note-59">&#91;59&#93;</a></sup> on public roads (where permitted, typically with a license or permit<sup id="cite_ref-60" class="reference"><a href="#cite_note-60">&#91;60&#93;</a></sup> or adhering to a specific set of operating principles)<sup id="cite_ref-61" class="reference"><a href="#cite_note-61">&#91;61&#93;</a></sup> or virtually, i.e. in computer simulations<sup id="cite_ref-62" class="reference"><a href="#cite_note-62">&#91;62&#93;</a></sup>.
</p><p>When driven on public roads, autonomous vehicles require a person to monitor their proper operation and "take over" when needed.
</p><p>Apple is currently testing self-driven cars, and has increased the number of test vehicles from 3 to 27 in January 2018.<sup id="cite_ref-63" class="reference"><a href="#cite_note-63">&#91;63&#93;</a></sup> This number further increased to 45 in March 2018.<sup id="cite_ref-64" class="reference"><a href="#cite_note-64">&#91;64&#93;</a></sup>
</p><p>One way to assess the progress of autonomous vehicles is to compute the average number of miles driven between "disengagements", when the autonomous system is turned off, typically by a human driver. In 2017, <a href="/wiki/Waymo" title="Waymo">Waymo</a> reported 63 disengagements over 352,545 miles of testing, or 5596 miles on average, the highest among companies reporting such figures. Waymo also traveled more miles in total than any other. Their 2017 rate of 0.18 disengagements per 1000 miles was an improvement from 0.2 disengagements per 1000 miles in 2016 and 0.8 in 2015. In March, 2017, Uber reported an average of 0.67 miles per disengagement. In the final three months of 2017, <a href="/wiki/Cruise_Automation" title="Cruise Automation">Cruise Automation</a> (now owned by <a href="/wiki/General_Motors" title="General Motors">GM</a>) averaged 5224 miles per disruption over 62,689 miles.<sup id="cite_ref-:6_65-0" class="reference"><a href="#cite_note-:6-65">&#91;65&#93;</a></sup> In July 2018, the first electric driverless racing car "Robocar" completed 1.8 kilometers track, using its navigation system, and artificial intelligence.<sup id="cite_ref-66" class="reference"><a href="#cite_note-66">&#91;66&#93;</a></sup> 
</p>
<table class="wikitable">
<caption>Miles per disengagement<sup id="cite_ref-:6_65-1" class="reference"><a href="#cite_note-:6-65">&#91;65&#93;</a></sup>
</caption>
<tbody><tr>
<th rowspan="2">Maker</th>
<th colspan="2">2016
</th></tr>
<tr>
<th>Miles per <br />disengagement</th>
<th>Miles
</th></tr>
<tr>
<td>Google</td>
<td>5,127.9</td>
<td>635,868
</td></tr>
<tr>
<td>BMW</td>
<td>638</td>
<td>638
</td></tr>
<tr>
<td>Nissan</td>
<td>263.3</td>
<td>6,056
</td></tr>
<tr>
<td>Ford</td>
<td>196.6</td>
<td>590
</td></tr>
<tr>
<td>General Motors</td>
<td>54.7</td>
<td>8,156
</td></tr>
<tr>
<td>Delphi Automotive Systems</td>
<td>14.9</td>
<td>2,658
</td></tr>
<tr>
<td>Tesla</td>
<td>2.9</td>
<td>550
</td></tr>
<tr>
<td>Mercedes Benz</td>
<td>2</td>
<td>673
</td></tr>
<tr>
<td>Bosch</td>
<td>0.68</td>
<td>983
</td></tr></tbody></table>

-----------

![cars](https://thumbor.forbes.com/thumbor/960x0/https%3A%2F%2Fblogs-images.forbes.com%2Fniallmccarthy%2Ffiles%2F2018%2F04%2F20180413_SelfDriving_Cars.jpg)

-----------

![868_registered_autonomous_vehicles_to_be_tested_in_california_n](https://infographic.statista.com/normal/chartoftheday_13868_registered_autonomous_vehicles_to_be_tested_in_california_n.jpg)

------------

![13463_autonomous_cars_how_would_you_spend_your_time](https://infographic.statista.com/normal/chartoftheday_13463_autonomous_cars_how_would_you_spend_your_time_n.jpg)

----------

![chartoftheday_13399_is_in_car_advertising_the_future_n](https://infographic.statista.com/normal/chartoftheday_13399_is_in_car_advertising_the_future_n.jpg)

------------

![13988_frequency_of_human_interventions_autonomous_vehicles_n](https://infographic.statista.com/normal/chartoftheday_13988_frequency_of_human_interventions_autonomous_vehicles_n.jpg)

----------

![10879_autonomous_driving_patents_n](https://infographic.statista.com/normal/chartoftheday_10879_autonomous_driving_patents_n.jpg)

------------

![60_americans_expect_driverless_cars_to_be_common_in_10_years_n](https://infographic.statista.com/normal/chartoftheday_13860_americans_expect_driverless_cars_to_be_common_in_10_years_n.jpg)

------------
---------------------
