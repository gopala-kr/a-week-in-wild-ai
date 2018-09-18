#### A brief survey: ai in surveillance


--------
> ##### Contents

- [Surveillance Architectures](#surveillance-architectures)
- [AI Use Cases in surveillance](#ai-use-cases-in-surveillance)
  - [Face recognition](#face-recognition)
  - [Video Analytics](#video-analytics)
  - [Audio Analytics](#audio-analytics)
- [Internet of Things](#internet-of-things)
  - [IoT platforms and Analytics](#iot-platforms-and-analytics)
- [Libraries](#libraries)
- [Literature Reviews](#literature-reviews)
  - [Surveillance](#surveillance)
  - [IoT](#iot)
- [Ethical issues of surveillance](#ethical-issues-of-surveillance)
- [Startups](#startups)
- [Misc](#misc)
- [Appendix](#appendix)

-----------

#### Surveillance Architectures and components


- [Deep Learning Architectures for Face Recognition in Video Surveillance](https://arxiv.org/pdf/1802.09990v2.pdf)
- [IBM: Components of the monitoring architecture](https://www.ibm.com/support/knowledgecenter/en/SSTFXA_6.3.0.2/com.ibm.itm.doc_6.3fp2/install/overview_components.htm)
- [Architecture of video surveillance systems based on IP networks](https://www.dipolnet.com/architecture_of_video_surveillance_systems_based_on_ip_networks_bib701.htm)
- [IP Video Surveillance 1.0 Solution Overview](https://www.cisco.com/c/en/us/td/docs/solutions/Enterprise/Video/ipvideosurvover.pdf)
- [A flexible and scalable component-based system architecture for video surveillance as a service, running on infrastructure as a service](https://www.researchgate.net/publication/224674311_Scalable_Surveillance_Software_Architecture)
- [Mobile Video Surveillance Systems:
an Architectural Overview](http://imagelab.ing.unimore.it/imagelab/pubblicazioni/soas2010_Gualdi.pdf)
- [Google: Peer to peer surveillance architecture](https://patents.google.com/patent/US9661276)
- [A CLOUD-BASED ARCHITECTURE FOR SMART VIDEO SURVEILLANCE](https://www.int-arch-photogramm-remote-sens-spatial-inf-sci.net/XLII-4-W3/99/2017/isprs-archives-XLII-4-W3-99-2017.pdf)
- [Surveillance
Dell EMC Surveillance Networking](https://www.emc.com/collateral/technical-documentation/h16965-dellemc-storage-ra-network.pdf)
- [Video Sensor Architecture for Surveillance Applications](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3304125/)
- [Architectural Improvements for Mobile
Ubiquitous Surveillance Systems](https://www.vtt.fi/inf/pdf/publications/2008/P691.pdf)
- [Networked IP Video Surveillance Architecture: Distributed or Centralized?](https://www.mistralsolutions.com/articles/networked-ip-video-surveillance-architecture-distributed-centralized/)
- [An Architecture for Video Surveillance Service Based on P2P and Cloud Computing](https://ieeexplore.ieee.org/document/6332063/)
- [Safe cities architecture
for India
](https://www.pwc.in/assets/pdfs/publications/2015/safe-cities-architecture-in-india.pdf)
- [Dell Technologies IoT Solution |
Surveillance
](https://www.delltechnologies.com/content/dam/delltechnologies/assets/solutions/resources/h17382-iot-surveillance-ra.pdf)
- [Intelligent IP video
management platform](https://www.downloads.siemens.com/download-center/Download.aspx?pos=download&fct=getasset&id1=A6V10705643)
- [Video Surveillance Solutions with NetApp
E-Series Storage](https://www.netapp.com/us/media/tr-4196.pdf)
- [Implementation and Evaluation of Large-Scale Video Surveillance System Based on P2P Architecture and Cloud Computing](http://journals.sagepub.com/doi/full/10.1155/2014/375871)
- [Software Architecture and Design for
Airport Scene Surveillance Radar Data Processing System ](http://dbmanagement.info/Books/MIX/3557a382_Software_Architecture_and_Design_for_Airport_Scene_Surveillance_Radar_Data_Processing_System.pdf)
- [Fully Distributed Secure Video Surveillance Via
Portable Device with User Awareness
](https://hal.inria.fr/hal-01506692/document)
- [Report on Video Surveillance
Hardware Platforms](https://crises-deim.urv.cat/vipp/VIPP_D01.pdf)
- [Secure System Architecture for Wide Area Surveillance Using Security, Trust and Privacy (STP) Framework](https://www.sciencedirect.com/science/article/pii/S187770581202601X)
- [A Smart Camera Mote Architecture for Distributed
Intelligent Surveillance 
](https://pdfs.semanticscholar.org/62d1/a707ef36e34b03ee5925d96b48936ddd16b9.pdf)
- [The SfinX Video Surveillance System](https://users.cs.fiu.edu/~raju/WWW/publications/icme2004/paper.pdf)
- [A Microservice-enabled Architecture for Smart
Surveillance using Blockchain Technology](https://arxiv.org/pdf/1807.07487.pdf)
- [https://pervasive.aau.at/BR/dsc06/CR/dsc06_p10_cr.pdf](https://pervasive.aau.at/BR/dsc06/CR/dsc06_p10_cr.pdf)
- [Video Surveillance for Sensor Platforms: Algorithms and Architectures](https://books.google.co.in/books?id=KKu8BAAAQBAJ&printsec=frontcover&dq=Surveillance+Architectures+and+components&hl=en&sa=X&ved=0ahUKEwjctu_I98PdAhUV148KHZBnDgkQ6AEIJjAA#v=onepage&q=Surveillance%20Architectures%20and%20components&f=false)
- [Digital Video Surveillance and Security](https://books.google.co.in/books?id=rAnUAgAAQBAJ&printsec=frontcover&dq=Surveillance+Architectures+and+components&hl=en&sa=X&ved=0ahUKEwjctu_I98PdAhUV148KHZBnDgkQ6AEIPTAE#v=onepage&q=Surveillance%20Architectures%20and%20components&f=false)
- [Event-Driven Surveillance: Possibilities and Challenges](https://books.google.co.in/books?id=BAIs9C8PyiYC&pg=PA26&dq=Surveillance+Architectures+and+components&hl=en&sa=X&ved=0ahUKEwjctu_I98PdAhUV148KHZBnDgkQ6AEIQzAF#v=onepage&q=Surveillance%20Architectures%20and%20components&f=false)
- [Advanced Video-Based Surveillance Systems](https://books.google.co.in/books?id=S1_VBwAAQBAJ&printsec=frontcover&dq=Surveillance+Architectures+and+components&hl=en&sa=X&ved=0ahUKEwjak4fb98PdAhVBv48KHX3zB5g4ChDoAQglMAA#v=onepage&q=Surveillance%20Architectures%20and%20components&f=false)
- [Intelligent Network Video: Understanding Modern Video Surveillance Systems ...](https://books.google.co.in/books?id=y6WiDQAAQBAJ&printsec=frontcover&dq=Surveillance+Architectures+and+components&hl=en&sa=X&ved=0ahUKEwjak4fb98PdAhVBv48KHX3zB5g4ChDoAQhLMAg#v=onepage&q=Surveillance%20Architectures%20and%20components&f=false)

---------

#### AI Use Cases in surveillance

- [How to Automate Surveillance Easily with Deep Learning](https://medium.com/nanonets/how-to-automate-surveillance-easily-with-deep-learning-4eb4fa0cd68d)
- [AI for Crime Prevention and Detection – Current Applications](https://www.techemergence.com/ai-crime-prevention-5-current-applications/)
- [Artificial Intelligence and Security: Current Applications and Tomorrow’s Potentials](https://www.techemergence.com/artificial-intelligence-and-security-applications/)
- [ai-cameras-use](https://futurism.com/ai-cameras-use/)

-----------


#### Video Analytics

- [Video Surveillance](http://www.bostonanalytics.com/images/Introduction_Video%20Surveillance%20Whitepaper_2014.pdf)
- [NVIDIA INTELLIGENT VIDEO ANALYTICS (IVA)](https://www.nvidia.com/en-us/autonomous-machines/intelligent-video-analytics-platform/)
- [Intelligent Video Analytics](https://www.intelli-vision.com/wp-content/uploads/2017/12/IntelliVision_IntelligentVideoAnalytics_datasheet1117.pdf)
- [IBM Intelligent Video Analytics
with Power AI Vision](https://public.dhe.ibm.com/common/ssi/ecm/10/en/10018810usen/ibm-intelligent-video-analytics-and-power-ai_10018810USEN.pdf?aliId=15463486)
- [VIDEO ANALYTICS
PLATFORM FOR BIG DATA](http://avidbeam.com/wp-content/uploads/2018/01/Vide-Analytics-Scalability-White-Paper.pdf)

----------

#### Audio Analytics

- [The Forrester New Wave™: AI-Fueled Speech Analytics Solutions, Q2 2018](https://reprints.forrester.com/#/assets/2/162/RES142606/reports)
- [Getting Started with Audio Data Analysis using Deep Learning (with case study)](https://www.analyticsvidhya.com/blog/2017/08/audio-voice-processing-deep-learning/)
- [CALLMINER WHITEPAPERS](https://learn.callminer.com/whitepapers)



-------

#### Internet of Things

- [Designing the Internet of Things](https://books.google.co.in/books?id=iYkKAgAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEIMjAC#v=onepage&q=internet%20of%20things&f=false)
- [Internet of Things: Evolutions and Innovations](https://books.google.co.in/books?id=MXs6DwAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEIQTAF#v=onepage&q=internet%20of%20things&f=false)
- [Building the Internet of Things: Implement New Business Models, Disrupt ...](https://books.google.co.in/books?id=HfB4DQAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEIRzAG#v=onepage&q=internet%20of%20things&f=false)
- [The Internet of Things and Business](https://books.google.co.in/books?id=LCglDwAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEITTAH#v=onepage&q=internet%20of%20things&f=false)
- [The Internet of Things: Breakthroughs in Research and Practice ...](https://books.google.co.in/books?id=7RshDgAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEIUzAI#v=onepage&q=internet%20of%20things&f=false)
- [Internet of Things: Converging Technologies for Smart Environments and ...](https://books.google.co.in/books?id=rHYGZ0wxLP0C&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEIWDAJ#v=onepage&q=internet%20of%20things&f=false)
- [Cognitive Hyperconnected Digital Transformation: Internet of Things ](https://books.google.co.in/books?id=nPIxDwAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEIPTAE#v=onepage&q=internet%20of%20things&f=false)
- [Internet of Things: Principles and Paradigms](https://books.google.co.in/books?id=_k11CwAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwi7kemW-sPdAhVEfCsKHfIED74Q6AEIOTAD#v=onepage&q=internet%20of%20things&f=false)
- [Rethinking the Internet of Things: A Scalable Approach to Connecting Everything](https://books.google.co.in/books?id=mPgFAwAAQBAJ&printsec=frontcover&dq=internet+of+things&hl=en&sa=X&ved=0ahUKEwjJnqav-sPdAhULfn0KHTTEBbs4ChDoAQg6MAQ#v=onepage&q=internet%20of%20things&f=false)


#### IoT platforms and Analytics

- [iotschool.microsoft](https://iotschool.microsoft.com/learning-paths)
- [Google's Infrastructure and Specific IoT Services](https://www.slideshare.net/IntelSoftware/googles-infrastructure-and-specific-iot-services)
- [AWS IoT](http://www.semiconwest.org/sites/semiconwest.org/files/data15/docs/1_TomJones_Amazon_presentation.pdf)
- [AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-dg.pdf)
- [AWS internet_of_things](http://www.pragtech.co.in/whitepaper/internet_of_things.pdf)
- [Microsoft & IoT](https://www.microsoft.com/en-in/internet-of-things/products)
- [Internet of things (IoT) with Azure](https://www.slideshare.net/VinothRajagopalan/io-t-with-azure)
- [Introduction to Azure IoT](http://events17.linuxfoundation.org/sites/events/files/slides/OpenIoT%20Summit%20-%20Introduction%20to%20Azure%20IoT.pdf)
- [IBM Internet of Things](http://users.jyu.fi/~olkhriye/IBM/IBM_IoT.pdf)
- [IBM Internet of Things Offerings](https://www.slideshare.net/IBMIoT/ibm-internet-of-things-offerings)
- [Watson
IoT](https://www.ibm.com/internet-of-things/common/pdf/watson-iot-point-of-view.pdf)
- [Watson	IoT](https://www.ibm.com/internet-of-things/nl-nl/watson-comes-to-you-2017/pdf/IoT_for_Manufacturing.pdf)
- [IBM Internet of Things Point
of View and Strategy. ](http://toronto.ieee.ca/files/2016/02/TOR-IEEE-IBM-IoT-Jan-28-2016-Final.pdf)
- [https://www.aiia.com.au/documents/event-presentations/2014/Davyd_Norris-IBM_Watson.pdf](http://toronto.ieee.ca/files/2016/02/TOR-IEEE-IBM-IoT-Jan-28-2016-Final.pdf)
- [IBM Watson IoT Platform
Analytics & IoT Real-Time Insights
(RTI)](http://www.fmmug.com/sites/default/files/Kim%20Woodbury%20-%20Watson%20IoT%20Analytics%20&%20RTI.pdf)
- [The Internet of Things](https://www.iotone.com/files/pdf/vendor/IBM_Internet_of_things_2013.pdf)
- [Die IBM Watson IoT Plattform](https://www.salzburgresearch.at/wp-content/uploads/2016/05/IoT-Talks-2-Watson-IoT-Plattform-IBM.pdf)
- [TEXAS INSTRUMENTS: The Evolution of the
Internet of Things](http://www.ti.com/lit/ml/swrb028/swrb028.pdf)
- [scalable-secure-iot-strategy](https://www.intel.com/content/dam/www/public/us/en/documents/white-papers/scalable-secure-iot-strategy-white-paper.pdf)
- [INTERNET	OF	THINGS:	
TRENDS,	DIRECTIONS,	OPPORTUNITIES,	CHALLENGES](https://bwn.ece.gatech.edu/presentations/IoT%20Trends%202017-04.pdf)
- [Cognitive Internet of Things](http://web.stanford.edu/class/archive/ee/ee392b/ee392b.1166/lecture/apr26/IBM.pdf)
- [Artificial intelligence and IoT](https://www.slideshare.net/VeselinPizurica/aiiot-presentation)
- [When IoT Meets Artificial Intelligence](https://www.slideshare.net/VeselinPizurica/when-iot-meets-artificial-intelligence)
- [AI in IoT: Use Cases and Challenges](https://www.slideshare.net/code_zombie/ai-in-iot-use-cases-and-challenges)
- [Artificial Intelligence Plus the Internet of Things (IoT) – 3 Examples Worth Learning From](https://www.techemergence.com/artificial-intelligence-plus-the-internet-of-things-iot-3-examples-worth-learning-from/)
- [Combined Artificial Intelligence and
IoT for Smart Sustainable Cities](https://www.itu.int/en/ITU-T/Workshops-and-Seminars/gsw/201804/Documents/Manasseh_Presentations.pdf)
- [Intelligent IoT](https://www2.deloitte.com/insights/us/en/focus/signals-for-strategists/intelligent-iot-internet-of-things-artificial-intelligence.html)
- [Artificial Intelligence (AI) Delivering
Breakthroughs in Industrial IoT](http://www.hitachinext.com/en-us/pdf/artificial-intelligence-delivering-breakthroughs-in-industrial-iot.pdf)
- [Using Artificial Intelligence in the
Internet of Things](http://wwwen.zte.com.cn/endata/magazine/ztecommunications/2015/2/201507/P020150724567382942663.pdf)
- [ARTIFICIAL INTELLIGENCE: A REAL BOON FOR IOT SECURITY](https://blog.econocom.com/en/blog/artificial-intelligence-a-real-boon-for-iot-security/)
- [The Convergence
of 5G, AI and IoT](https://t3chfest.uc3m.es/2018/static/resources/events_slides/2018-03-01_T3chfest_-_The_Convergence_of_5G_AI_and_IoT_v4.pdf?q=1519913894)
- [CISCO: Internet of Things](https://pdfs.semanticscholar.org/presentation/3059/1c06af2c37cc952b6e6233036079c5c99b1a.pdf)
- [Cisco Smart+Connected Lighting](https://iotevent.eu/wp-content/uploads/2016/09/Cisco-Smart-Connected-Lighting-IoT-AI-Workshop-LpS-2016.pdf)
- [Smart Applications in Contemporary Cities
for the Benefit of Citizens and Businesses](http://cyprusconferences.org/5thsmc/gr/presentations/5thSMC_May17_0910_Nikos_Lambrogeorgos-Smart_City.pdf)
- [Cisco SP IoT Architecture](https://www.cisco.com/c/dam/m/fr_fr/events/2015/cisco_day/pdf/7-ciscoday-10june2016-sp-iot.pdf)
- [The Internet of Things
Vertical Solutions ](https://www.cisco.com/web/offer/emear/38586/images/Presentations/P11.pdf)
- [Enabling the Internet of Everything: Cisco’s IoT Architecture](https://www.slideshare.net/Cisco/enabling-the-internet-of-everything-ciscos-iot-architecture)
- [What is Salesforce and what do we do?](https://www2.deloitte.com/content/dam/Deloitte/is/Documents/technology/04%20Salesforce%20Clouds%20_%20Dreamforce.pdf)
- [Salesforce Intro to the Internet of Things](https://www.slideshare.net/davescruggs/salesforce-intro-to-the-internet-of-things)
- [IoT Cloud: How TeMeDa & Hexagon Metrology Unlock the Power of Connected](https://www.slideshare.net/Dreamforce/iot-cloud-how-temeda-hexagon-metrology-unlock-the-power-of-connected)
- [SAP Cloud Platform Internet of Things](https://assets.dm.ux.sap.com/de-leonardolive/pdfs/50988_sap_br5_3.pdf)
- [Sap Leonardo IoT Overview](https://www.slideshare.net/PierreErasmus/sap-leonardo-iot-overview)
- [SAP and The Internet of Things](https://www.slideshare.net/jpenninkhof/sap-and-the-internet-of-things)
- [SAP Cloud Platform](https://www.sapstore.com/medias/SAP-cloud-platform.pdf?context=bWFzdGVyfHBkZnN8MTQ1MTkzMDF8YXBwbGljYXRpb24vcGRmfHBkZnMvaGU0L2g3Ny84ODg2NjQ2MTQ1MDU0LnBkZnwwZWExNjI5NTc4Y2Q0N2VhNzg0ZGY2OWM5MmQ3ZDQzMWNjMWQ1MmYxMjYyYjE3YTE5ODlmZWU5NjM5MzJhMzE4)
- [SAP HANA Cloud Platform for the Internet of Things](http://ec.europa.eu/information_society/newsroom/image/document/2015-44/16_kubach_11953.pdf)
- [SAP Cloud Strategy and Leonardo:
Enabling innovation and extension of the digital core](https://static1.squarespace.com/static/5777f3c78419c2849232f1b4/t/5980b69c725e25d62c22391d/1501607585045/SAP_Cloud+Strategy+and+Leonardo+-+Enabling+innovation+and+extension+of+the+digital+core_7.27.17.pdf)
- [Urgency of Doing –
Staying connected with IoT](http://www.sapsa.se/wp-content/uploads/2017/11/Tanja_Rueckert_SUGEN_Urgency-of-Doing-Staying-Connected-with-IoT.pdf)
- [SAP Cloud Platform IoT Services 4.0 ](https://www.inwerken.de/wp-content/uploads/2017/02/SAP-Cloud-Platform-IoT-Services-4.0-beta_public.pdf)
- [DEV102 – SAP HANA Cloud Platform:
A Guided T](http://www.sapevents.edgesuite.net/TechEd/TechEd_Vegas2015/pdfs/DEV102.pdf)
- [Samsung_ARTIK_Overview](https://static.artik.io/files/Samsung_ARTIK_Overview.pdf)
- [ARTIKTM
The Ultimate Platform Solution for IoT](https://www.tizen.org/sites/default/files/event/a1_tdc15_artik_-_the_ultimate_platform_solution_for_iot.pdf)
- [IoT and the Role of Platforms](https://www.slideshare.net/TieChapterBangalore/iot-and-the-role-of-platforms)
- [ARTIK_530_PB_1](https://media.digikey.com/pdf/Data%20Sheets/Samsung%20PDFs/ARTIK_530_PB_1-10-17.pdf)

--------

#### Libraries

- [DeepVideoAnalytics](https://github.com/AKSHAYUBHAT/DeepVideoAnalytics)
- [VisualSearchServer](https://github.com/AKSHAYUBHAT/VisualSearchServer)
- [TensorFace](https://github.com/AKSHAYUBHAT/TensorFace)
- [YUView](https://github.com/IENT/YUView)
- [videojs-ga](https://github.com/mickey/videojs-ga)
- [video-stream-analytics](https://github.com/baghelamit/video-stream-analytics)
- [ozonebase](https://github.com/ozonesecurity/ozonebase)
- [Video-Analytics-OpenCV](https://github.com/intel-iot-devkit/Video-Analytics-OpenCV)
- [VIAME](https://github.com/Kitware/VIAME)
- [azure-serverless-video-analytics](https://github.com/yokawasa/azure-serverless-video-analytics)
- [video-analytics-with-AWS](https://github.com/arjun9916/video-analytics-with-AWS)


----------

#### Literature Reviews


Surveillance

- [A Comparison of CNN-based Face and Head Detectors for Real-Time Video Surveillance Applications](https://arxiv.org/pdf/1809.03336v1.pdf)
- [Sparse Camera Network for Visual Surveillance -- A Comprehensive Survey](https://arxiv.org/pdf/1302.0446v1.pdf)
- [Human Action Recognition and Prediction: A Survey](https://arxiv.org/pdf/1806.11230v2.pdf)
- [Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey](https://arxiv.org/pdf/1801.00553v3.pdf)
- [A Survey on Resilient Machine Learning](https://arxiv.org/ftp/arxiv/papers/1707/1707.03184.pdf)
- [A Survey of Recent Advances in CNN-based Single Image Crowd Counting and Density Estimation](https://arxiv.org/pdf/1707.01202v1.pdf)
- [Going Deeper into Action Recognition: A Survey](https://arxiv.org/pdf/1605.04988v2.pdf)
- [Advances in Human Action Recognition: A Survey](https://arxiv.org/pdf/1501.05964v1.pdf)
- [Audio Surveillance: a Systematic Review](https://arxiv.org/pdf/1409.7787v1.pdf)
- [A Survey of Appearance Models in Visual Object Tracking](https://arxiv.org/pdf/1303.4803v1.pdf)
- [A Comparison of CNN-based Face and Head Detectors for Real-Time Video Surveillance Applications](https://arxiv.org/pdf/1809.03336v1.pdf)
- [CNNs for Surveillance Footage Scene Classification](https://arxiv.org/pdf/1809.02766v1.pdf)
- [Surveillance Face Recognition Challenge](https://arxiv.org/pdf/1804.09691v6.pdf)
- [Probabilistic Semantic Retrieval for Surveillance Videos with Activity Graphs](https://arxiv.org/pdf/1712.06204v2.pdf)
- [Vehicle Traffic Driven Camera Placement for Better Metropolis Security Surveillance](https://arxiv.org/pdf/1705.08508v4.pdf)
- [Face Recognition in Low Quality Images: A Survey](https://arxiv.org/abs/1805.11519v2)
- [Survey on Deep Learning Techniques for Person Re-Identification Tas](https://arxiv.org/pdf/1807.05284v3.pdf)
- [Robustness Analysis of Pedestrian Detectors for Surveillance](https://arxiv.org/pdf/1807.04562v2.pdf)
- [A nonconvex approach to low-rank and sparse matrix decomposition with application to video surveillance](https://arxiv.org/pdf/1807.01276v1.pdf)
- [Deployment of Customized Deep Learning based Video Analytics On Surveillance Cameras](https://arxiv.org/pdf/1805.10604v2.pdf)
- [A Comparison of Machine Learning Algorithms for the Surveillance of Autism Spectrum Disorder](https://arxiv.org/ftp/arxiv/papers/1804/1804.06223.pdf)
- [Eye in the Sky: Real-time Drone Surveillance System (DSS) for Violent Individuals Identification using ScatterNet Hybrid Deep Learning Network](https://arxiv.org/pdf/1806.00746v1.pdf)
- [Intelligent Surveillance as an Edge Network Service: from Harr-Cascade, SVM to a Lightweight CNN](https://arxiv.org/pdf/1805.00331v1.pdf)
- [Survey of Face Detection on Low-quality Images](https://arxiv.org/pdf/1804.07362v1.pdf)
- [Evaluation of Object Trackers in Distorted Surveillance Videos](https://arxiv.org/pdf/1804.01624v1.pdf)
- [Real-world Anomaly Detection in Surveillance Videos](https://arxiv.org/pdf/1801.04264v2.pdf)
- [Image Set Classification for Low Resolution Surveillance](https://arxiv.org/pdf/1803.09470v1.pdf)
- [Moving Vehicle Detection Using AdaBoost and Haar-Like Feature in Surveillance Videos](https://arxiv.org/ftp/arxiv/papers/1801/1801.01698.pdf)
- [ReMotENet: Efficient Relevant Motion Event Detection for Large-scale Home Surveillance Videos](https://arxiv.org/pdf/1801.02031v1.pdf)
- [Lost in Time: Temporal Analytics for Long-Term Video Surveillance](https://arxiv.org/pdf/1712.07322v1.pdf)
- [Human Detection and Tracking for Video Surveillance A Cognitive Science Approach](https://arxiv.org/ftp/arxiv/papers/1709/1709.00726.pdf)
- [Generative Adversarial Models for People Attribute Recognition in Surveillance](https://arxiv.org/pdf/1707.02240v1.pdf)
- [Long-Term Identity-Aware Multi-Person Tracking for Surveillance Video Summarization](https://arxiv.org/pdf/1604.07468v2.pdf)
- [Surveillance Video Parsing with Single Frame Supervision](https://arxiv.org/pdf/1611.09587v1.pdf)
- [Ear Recognition: More Than a Survey](https://arxiv.org/pdf/1611.06203v1.pdf)
- [A Scalable and Robust Framework for Intelligent Real-time Video Surveillance](https://arxiv.org/pdf/1610.09590v1.pdf)
- [Automatic detection of moving objects in video surveillance](https://arxiv.org/ftp/arxiv/papers/1608/1608.03617.pdf)
- [A Survey of the Trends in Facial and Expression Recognition Databases and Methods](https://arxiv.org/ftp/arxiv/papers/1511/1511.02407.pdf)



IoT

- [Machine learning for Internet of Things data analysis: A survey](https://arxiv.org/pdf/1802.06305v1.pdf)
- [Deep Learning for IoT Big Data and Streaming Analytics: A Survey](https://arxiv.org/pdf/1712.04301v2.pdf)
- [A Survey of Machine and Deep Learning
Methods for Internet of Things (IoT) Security](https://arxiv.org/ftp/arxiv/papers/1807/1807.11023.pdf)
- [Detection of Unauthorized IoT Devices Using Machine Learning Techniques](https://arxiv.org/pdf/1709.04647v1.pdf)
- [Big IoT and social networking data for smart cities: Algorithmic improvements on Big Data Analysis in the context of RADICAL city applications](https://arxiv.org/ftp/arxiv/papers/1607/1607.00509.pdf)
- [Automation of Feature Engineering for IoT Analytics](https://arxiv.org/pdf/1707.04067v1.pdf)
- [Towards an Intelligent Edge: Wireless Communication Meets Machine Learning](https://arxiv.org/ftp/arxiv/papers/1809/1809.00343.pdf)
- [Deploying Deep Neural Networks in the Embedded Space](https://arxiv.org/pdf/1806.08616v1.pdf)
- [Ultra Low Power Deep-Learning-powered Autonomous Nano Drones](https://arxiv.org/pdf/1805.01831v1.pdf)
- [Machine Learning DDoS Detection for Consumer Internet of Things Devices](https://arxiv.org/pdf/1804.04159v1.pdf)
- [Deep Learning for Signal Authentication and Security in Massive Internet of Things Systems](https://arxiv.org/pdf/1803.00916v1.pdf)
- [Secure Mobile Crowdsensing with Deep Learning](https://arxiv.org/pdf/1801.07379v1.pdf)
- [Automated flow for compressing convolution neural networks for efficient edge-computation with FPGA](https://arxiv.org/pdf/1712.06272v1.pdf)
- [Applying Chatbots to the Internet of Things: Opportunities and Architectural Elements](https://arxiv.org/ftp/arxiv/papers/1611/1611.03799.pdf)
- [Internet of Things Applications: Animal Monitoring with Unmanned Aerial Vehicle](https://arxiv.org/pdf/1610.05287v2.pdf)
- [Towards an Intelligent Edge:
Wireless Communication Meets Machine Learning ](https://arxiv.org/ftp/arxiv/papers/1809/1809.00343.pdf)
- [Threat analysis of IoT networks Using Artificial
Neural Network Intrusion Detection System](https://arxiv.org/ftp/arxiv/papers/1704/1704.02286.pdf)
- [An IoT Endpoint System-on-Chip for Secure
and Energy-Efficient Near-Sensor Analytics](https://arxiv.org/pdf/1612.05974v3.pdf)
- [An IoT Real-Time Biometric Authentication
System Based on ECG Fiducial Extracted
Features Using Discrete Cosine Transform ](https://arxiv.org/ftp/arxiv/papers/1708/1708.08189.pdf)
- [Efficient Licence Plate Detection By Unique Edge
Detection Algorithm and Smarter Interpretation
Through IoT.](https://arxiv.org/ftp/arxiv/papers/1710/1710.10418.pdf)
- [CIoTA: Collaborative IoT Anomaly
Detection via Blockchain](https://arxiv.org/pdf/1803.03807v2.pdf)
- [IoT2Vec: Identification of Similar IoT Devices via
Activity Footprints](https://arxiv.org/ftp/arxiv/papers/1805/1805.07907.pdf)
- [Deploy Large-Scale Deep Neural Networks in
Resource Constrained IoT Devices with Local
Quantization Region](https://arxiv.org/ftp/arxiv/papers/1805/1805.09473.pdf)
- [AI-based Two-Stage Intrusion Detection for
Software Defined IoT Networks](https://arxiv.org/pdf/1806.02566v1.pdf)
- [A Machine Learning Driven IoT Solution
for Noise Classification in Smart Cities](https://arxiv.org/pdf/1809.00238v1.pdf)

-----------

#### Ethical issues of surveillance


- [Data gathering, surveillance and human rights: recasting the debate](https://www.tandfonline.com/doi/full/10.1080/23738871.2016.1228990?src=recsys)
- [The effectiveness of surveillance technology: What intelligence officials are saying](https://www.tandfonline.com/doi/full/10.1080/01972243.2017.1414721)

---------

#### Startups

IOT

- [10 Charts That Will Challenge Your Perspective Of IoT's Growth](https://www.forbes.com/sites/louiscolumbus/2018/06/06/10-charts-that-will-challenge-your-perspective-of-iots-growth/#5e1eb63f3ecc)
- [Human-machine
interactions that
unlock possibilities](https://www.ey.com/Publication/vwLUAssets/ey-m-e-internet-of-things/%24FILE/ey-m-e-internet-of-things.pdf)
- [Where IoT Can Deliver The Most Value In 2018](https://www.forbes.com/sites/louiscolumbus/2018/03/18/where-iot-can-deliver-the-most-value-in-2018/#760aee7d42fa)
- [Internet of Things (IoT) 2018 –
Market Statistics, Use Cases and Trends](http://asiandatascience.com/wp-content/uploads/2017/12/eBook-Internet-of-Things-IoT-2018-Market-Statistics-Use-Cases-and-Trends.pdf)
- [Leverage Cloud-Native
IoT Software Platform
To Accelerate Digital
Transformation](https://www.huawei.com/minisite/iot/img/hw_iot_tlp_whte_paper_en.pdf)
- [Gartner Insights on How to Lead
in a Connected World](https://www.gartner.com/imagesrv/books/iot/iotEbook_digital.pdf)
- [GE Digital
Industrial Evolution Index
](https://www.ge.com/digital/sites/default/files/GE-Digital-Industrial-Evolution-Index-Executive-Summary.pdf)
- [IDC MarketScape: Worldwide IoT Platforms (Software Vendors)
2017 Vendor Assessment](https://www.ge.com/de/sites/www.ge.com.de/files/IDC%20MarketScape_Worldwide%20IoT%20Platforms_Software%20Vendors_US42033517%5B1%5D.pdf)
- [Transforming Manufacturing w ith the
Internet of Things](https://www.cognizant.com/InsightsWhitepapers/transforming-manufacturing-with-the-Internet-of-Things.pdf)
- [The Top 10 IoT Segments in 2018 – based on 1,600 real IoT projects](https://iot-analytics.com/top-10-iot-segments-2018-real-iot-projects/)
- [Intel & Cisco Relationship](https://www.cisco.com/c/dam/assets/global/GR/connect2014/pdfs/Intel_Nikos_Botinis.pdf)
- [State of the Market:
Internet of Things 2017](https://www.verizon.com/about/sites/default/files/Verizon-2017-State-of-the-Market-IoT-Report.pdf)
- [The Next Economic
Growth Engine
Scaling Fourth Industrial
Revolution Technologies
in Production](http://www3.weforum.org/docs/WEF_Technology_and_Innovation_The_Next_Economic_Growth_Engine.pdf)
- [THE INTERNET OF THINGS
CONNECTING THE DOTS](https://ww2.frost.com/files/7314/8233/2176/IoTBrochure_UK.pdf)
- [Zinnov Zones for IoT Services 2017](https://www.slideshare.net/zinnov/zinnov-zones-for-iot-services)
- [AN IOT PLATFORMS MATCH : MICROSOFT AZURE IOT VS AMAZON AWS IOT](https://paolopatierno.wordpress.com/2015/10/13/an-iot-platforms-match-microsoft-azure-iot-vs-amazon-aws-iot/)
- [10 BEST IOT PLATFORMS IN 2018. IOT TECHNOLOGY FORECAST](https://da-14.com/blog/10-best-iot-platforms-iot-technology-forecast)
- [IoT and Payments: Current Market
Landscape](https://www.securetechalliance.org/wp-content/uploads/IoT-Payments-WP-Final-Nov-2017.pdf)
- [CBinsihts: The Industrial Internet of Things](https://www.cbinsights.com/research-iiot-trends)
- [IoT Cloud Platform Landscape](https://www.postscapes.com/internet-of-things-platforms/)
- [IoT Investment Funding](https://www.postscapes.com/internet-of-things-investment/)
- [IoT-Platforms-Vendor-Comparison-June-2018-SAMPLE](https://iot-analytics.com/wp/wp-content/uploads/2018/06/IoT-Platforms-Vendor-Comparison-June-2018-SAMPLE-vf.pdf)
- [Growing Pains: The 2018 Internet of Things Landscape](http://mattturck.com/iot2018/)
- [Interoperability & Security in the IoT
Landscape](https://www2.gov.bc.ca/assets/gov/british-columbians-our-governments/services-policies-for-government/information-management-technology/information-security/information-security-awareness/its_7am_do_you_know_whats_on_your_network_forescout.pdf)
- [The surveillance landscape in Europe](https://www.fp7-risksur.eu/sites/default/files/documents/PDF_various/RISKSUR_Deliverable%207.3.1_ANNEX%208a.pdf)
- [Global Intelligent Video Analytics Market 2018-2023: Evaluating the Demand & Supply Side Challenges](https://www.prnewswire.com/fi/lehdistotiedotteet/global-intelligent-video-analytics-market-2018-2023-evaluating-the-demand--supply-side-challenges-300710474.html)



---------


#### Misc


- [Artificial intelligence for video surveillance](https://en.wikipedia.org/wiki/Artificial_intelligence_for_video_surveillance)
- [ARTIFICIAL INTELLIGENCE IS GOING TO SUPERCHARGE SURVEILLANCE](https://www.theverge.com/2018/1/23/16907238/artificial-intelligence-surveillance-cameras-security)
- [INDECT](https://en.wikipedia.org/wiki/INDECT)
- [Artificial Intelligence in Analysing Surveillance Sensor Data](https://www.mistralsolutions.com/articles/artificial-intelligence-analysing-surveillance-sensor-data/)
- [This Japanese AI security camera shows the future of surveillance will be automated](https://www.theverge.com/2018/6/26/17479068/ai-guardman-security-camera-shoplifter-japan-automated-surveillance)
- [Smart vision: This startup AI-powers CCTV surveillance cameras to understand what it sees](https://economictimes.indiatimes.com/small-biz/startups/features/this-startup-ai-powers-cctv-surveillance-cameras-to-understand-what-it-sees-uncanny-vision/articleshow/62424609.cms)
- [Artificial Intelligence in Analysing Surveillance Sensor Data](https://www.mistralsolutions.com/articles/artificial-intelligence-analysing-surveillance-sensor-data/)
- [how-much-artificial-intelligence-surveillance-is-too-much](https://www.voanews.com/a/how-much-artificial-intelligence-surveillance-is-too-much-/4465586.html)
- [The age of AI surveillance is here](https://qz.com/1060606/the-age-of-ai-surveillance-is-here/)
- [AI/Deep Learning-Based
Video Analytics
for Smart Cameras](https://www.intelli-vision.com/wp-content/uploads/2018/04/IntelliVision_Brochure_0418.1.pdf)
- [AI Cameras Are Here. Here Are Three Ways We Could Use Them.](https://futurism.com/ai-cameras-use/)
- [Fighting AI Surveillance with Scarves and Face Paint](https://medium.com/s/story/fighting-ai-surveillance-with-scarves-and-face-paint-6b634ef174a1)
- [Privacy under AI surveillance: China’s extreme use raises alarm](http://www.asahi.com/ajw/articles/AJ201807130017.html)
- [CHINA’S TERRIFYING SURVEILLANCE STATE LOOKS A LOT LIKE AMERICA’S FUTURE](https://www.vanityfair.com/news/2018/07/china-surveillance-state-artificial-intelligence)
- [Inside China’s Dystopian Dreams: A.I., Shame and Lots of Cameras](https://www.nytimes.com/2018/07/08/business/china-surveillance-technology.html)
- [Google Pledges Not to Use AI for Weapons or Surveillance](https://www.nbcchicago.com/news/business/Google-Pledges-No-AI-for-Weapons-Surveillance-484918741.html)
- [Artificial Intelligence delivers cost-effective video surveillance for 24,000 Real Estate cameras](https://blog.camio.com/artificial-intelligence-delivers-cost-effective-video-surveillance-for-24-000-real-estate-cameras-8e74b046616)
- [artificial-intelligence-is-poised-to-change-the-face-of-video-surveillance](https://www.infoworld.com/article/3232370/artificial-intelligence/artificial-intelligence-is-poised-to-change-the-face-of-video-surveillance.html)
- [How will AI surveillance change the American workplace?](https://www.infoworld.com/article/3264348/artificial-intelligence/how-will-ai-surveillance-change-the-american-workplace.html)
- [Amazon and law enforcement are using cloud-based AI for surveillance](https://www.businessinsider.com/amazon-and-law-enforcement-are-using-cloud-based-ai-for-surveillance-2018-5?IR=T)
- [Orwellian surveillance is changing us, and it's powered by AI](https://www.axios.com/ai-geopolitics-surveillance-nightmare-db613f44-0d3f-4496-8442-905c9a297658.html)
- [Google promises not to use A.I. for weapons or surveillance, for the most part](https://www.cnbc.com/2018/06/07/google-ai-ethical-principles.html)
- [Why AI will be an inevitable part of your video surveillance solution](https://www.asmag.com/showpost/24924.aspx)
- [Using Drones and AI For Automated Crowd Surveillance](https://dronelife.com/2018/06/07/drones-ai-crowd-surveillance/)
- [AI & Cloud Services Making Video Surveillance Increasingly Smart & Affordable](https://www.memoori.com/ai-cloud-services-making-intelligent-video-surveillance-increasingly-smart-affordable/)
- [The New Eyes of Surveillance: Artificial Intelligence and Humanizing Technology](https://www.wired.com/insights/2014/08/the-new-eyes-of-surveillance-artificial-intelligence-and-humanizing-technology/)
- ['Surveillance society': has technology at the US-Mexico border gone too far?](https://www.theguardian.com/technology/2018/jun/13/mexico-us-border-wall-surveillance-artificial-intelligence-technology)
- [Video Analysis to Detect Suspicious Activity Based on Deep Learning](https://dzone.com/articles/video-analysis-to-detect-suspicious-activity-based)
- [Deep Speech and Vision - Xavier Giro-i-Nieto - UPC Barcelona 2018](https://www.slideshare.net/xavigiro/deep-speech-and-vision-xavier-giroinieto-upc-barcelona-2018)
- [INTELLIGENT VIDEO SURVEILLANCE SYSTEM
ARCHITECTURE FOR ABNORMAL ACTIVITY DETECTION ](https://pdfs.semanticscholar.org/132d/e62629836c2ee88552db207429a815b4dc20.pdf)
- [Deep Surveillance](https://towardsdatascience.com/deep-surveillance-6b389abeaf95)
- [Bookmark and Share
Vision-Based Artificial Intelligence Brings Awareness to Surveillance](https://www.embedded-vision.com/platinum-members/embedded-vision-alliance/embedded-vision-training/documents/pages/security)
- [ROLE OF SURVEILLANCE
IN SECURING CITIES](http://asappinfoglobal.com/images/SSCI.pdf)
- [Surveillance of Chronic Diseases:
Challenges and Strategies for India](http://icrier.org/pdf/Working_Paper_322.pdf)
- [Trends and IoT in Video Surveillance](https://www.slideshare.net/Ivideon/trends-and-iot-in-video-surveillance?next_slideshow=1)
- [IP Surveillance 101](https://www.youtube.com/watch?v=NRS0Rsd6zxw)
- [Dispelling the Top 10
Myths of IP Surveillance](https://www.axis.com/files/articles/ar_10myths_secinfowatch_us_0512.pdf)
- [An End-to-End Solution Provider for Your Security Needs](http://www.dlink.co.in/products/end-to-end-surveillance/)
- [In video surveillance, India is not too far from Chinese comrades, says Seagate](https://tech.economictimes.indiatimes.com/news/technology/in-video-surveillance-india-is-not-too-far-from-chinese-comrades-says-seagate/52318365)
- [How to stand out as an IoT Platform Vendor](https://iot-analytics.com/how-to-stand-out-as-an-iot-platform-vendor/)

-------------

### Appendix:



-----------
----------------
