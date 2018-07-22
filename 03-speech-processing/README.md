### Speech processing: recognition, synthesis + Survey on chatbot platforms and API's

------

- [Timeline of speech and voice recognition](https://en.wikipedia.org/wiki/Timeline_of_speech_and_voice_recognition)
- [List of speech recognition software](https://en.wikipedia.org/wiki/List_of_speech_recognition_software)
- [Survey on Chatbot Design Techniques in Speech
Conversation Systems](https://thesai.org/Downloads/Volume6No7/Paper_12-Survey_on_Chatbot_Design_Techniques_in_Speech_Conversation_Systems.pdf)
- [The 2018 State of Chatbots Report: How Chatbots Are Reshaping Online Experiences](https://blog.drift.com/chatbots-report/)
- [Comparison of speech synthesizers](https://en.wikipedia.org/wiki/Comparison_of_speech_synthesizers)


---------------

Fundamentals of speech recognition

<div id="seq_contents_0"
    aria-labelledby="tab_0"
    aria-hidden="true"
    class="seq_contents tex2jax_ignore asciimath2jax_ignore">
    &lt;div class=&#34;xblock xblock-student_view xblock-student_view-vertical&#34; data-runtime-class=&#34;LmsRuntime&#34; data-init=&#34;VerticalStudentView&#34; data-course-id=&#34;course-v1:Microsoft+DEV287x+2T2018&#34; data-request-token=&#34;8c9b90da8d9011e89497068e1b74f120&#34; data-runtime-version=&#34;1&#34; data-usage-id=&#34;block-v1:Microsoft+DEV287x+2T2018+type@vertical+block@a2e9948d-de71-8029-7f01-afa6ce24179a&#34; data-block-type=&#34;vertical&#34;&gt;
  

  &lt;h2 class=&#34;hd hd-2 unit-title&#34;&gt;Other considerations&lt;/h2&gt;

    



&lt;div class=&#34;bookmark-button-wrapper&#34;&gt;
  &lt;button class=&#34;btn btn-link bookmark-button &#34;
    aria-pressed=&#34;false&#34;
    data-bookmark-id=&#34;gopalakr243,block-v1:Microsoft+DEV287x+2T2018+type@vertical+block@a2e9948d-de71-8029-7f01-afa6ce24179a&#34;
    data-bookmarks-api-url=&#34;/api/bookmarks/v1/bookmarks/&#34;&gt;
     &lt;span class=&#34;bookmark-text&#34;&gt;Bookmark this page&lt;/span&gt;
    &lt;/button&gt;
&lt;/div&gt;


&lt;div class=&#34;vert-mod&#34;&gt;
  &lt;div class=&#34;vert vert-0&#34; data-id=&#34;block-v1:Microsoft+DEV287x+2T2018+type@html+block@50d703c667f84883b94f56fef4e9312c&#34;&gt;
    &lt;div class=&#34;xblock xblock-student_view xblock-student_view-html xmodule_display xmodule_HtmlModule&#34; data-runtime-class=&#34;LmsRuntime&#34; data-init=&#34;XBlockToXModuleShim&#34; data-block-type=&#34;html&#34; data-request-token=&#34;8c9b90da8d9011e89497068e1b74f120&#34; data-runtime-version=&#34;1&#34; data-usage-id=&#34;block-v1:Microsoft+DEV287x+2T2018+type@html+block@50d703c667f84883b94f56fef4e9312c&#34; data-type=&#34;HTMLModule&#34; data-course-id=&#34;course-v1:Microsoft+DEV287x+2T2018&#34;&gt;
  &lt;script type=&#34;json/xblock-args&#34; class=&#34;xblock-json-init-args&#34;&gt;
    {&#34;xmodule-type&#34;: &#34;HTMLModule&#34;}
  &lt;/script&gt;
  &lt;p&gt;Besides accuracy, there may be computational requirements that impact performance, such as processing speed or latency. Decoding speed is usually measured with respect to a real-time factor. A RTF of 1.0 means that the system processes the data in real-time, takes ten seconds to process ten seconds of audio.&lt;/p&gt;
&lt;p&gt;Factors above 1.0 indicate that the system needs more time to process the data. For some applications, this may be acceptable. For instance, when creating a transcription of a meeting or lecture, it may be more important to take more time and produce accurate transcriptions than to get the transcriptions quickly.&lt;/p&gt;
&lt;p&gt;When the RTF is below 1.0, the system processes the data more quickly than it arrives. This can be useful when more than one system runs on the same machine. In that case, multithreading can effectively use one machine to process multiple audio sources in parallel. RTF below 1.0 also indicates that the system can &amp;ldquo;catch up&amp;rdquo; to real-time in online streaming applications. For instance, when performing a remote voice query on the phone, network congestion can cause gaps and delays in receiving the audio at the server. If the ASR system can process data in faster than real-time, it can catch up after the data arrives, hiding the latency behind the speed of the recognition system.&lt;/p&gt;
&lt;p&gt;In general, any ASR system can be tuned to tradeoff speed for accuracy. But, there is a limit. For a given model and test set, the speed-accuracy graph has an asymptote that is impossible to cross, even with unlimited computing power. The remaining errors can be entirely ascribed to modeling errors. Once the search finds the best result according to the model, further processing will not improve the accuracy.&lt;/p&gt;
&lt;/div&gt;

  &lt;/div&gt;
&lt;/div&gt;

&lt;/div&gt;

  </div>
  <div id="seq_contents_1"
    aria-labelledby="tab_1"
    aria-hidden="true"
    class="seq_contents tex2jax_ignore asciimath2jax_ignore">
    &lt;div class=&#34;xblock xblock-student_view xblock-student_view-vertical&#34; data-runtime-class=&#34;LmsRuntime&#34; data-init=&#34;VerticalStudentView&#34; data-course-id=&#34;course-v1:Microsoft+DEV287x+2T2018&#34; data-request-token=&#34;8c9b90da8d9011e89497068e1b74f120&#34; data-runtime-version=&#34;1&#34; data-usage-id=&#34;block-v1:Microsoft+DEV287x+2T2018+type@vertical+block@423e9a2a-7584-816d-6290-a2c8df171f3f&#34; data-block-type=&#34;vertical&#34;&gt;
  

  &lt;h2 class=&#34;hd hd-2 unit-title&#34;&gt;The Fundamental Equation&lt;/h2&gt;

    



&lt;div class=&#34;bookmark-button-wrapper&#34;&gt;
  &lt;button class=&#34;btn btn-link bookmark-button &#34;
    aria-pressed=&#34;false&#34;
    data-bookmark-id=&#34;gopalakr243,block-v1:Microsoft+DEV287x+2T2018+type@vertical+block@423e9a2a-7584-816d-6290-a2c8df171f3f&#34;
    data-bookmarks-api-url=&#34;/api/bookmarks/v1/bookmarks/&#34;&gt;
     &lt;span class=&#34;bookmark-text&#34;&gt;Bookmark this page&lt;/span&gt;
    &lt;/button&gt;
&lt;/div&gt;


&lt;div class=&#34;vert-mod&#34;&gt;
  &lt;div class=&#34;vert vert-0&#34; data-id=&#34;block-v1:Microsoft+DEV287x+2T2018+type@html+block@d3ddac86b2a04be39023597de7735789&#34;&gt;
    &lt;div class=&#34;xblock xblock-student_view xblock-student_view-html xmodule_display xmodule_HtmlModule&#34; data-runtime-class=&#34;LmsRuntime&#34; data-init=&#34;XBlockToXModuleShim&#34; data-block-type=&#34;html&#34; data-request-token=&#34;8c9b90da8d9011e89497068e1b74f120&#34; data-runtime-version=&#34;1&#34; data-usage-id=&#34;block-v1:Microsoft+DEV287x+2T2018+type@html+block@d3ddac86b2a04be39023597de7735789&#34; data-type=&#34;HTMLModule&#34; data-course-id=&#34;course-v1:Microsoft+DEV287x+2T2018&#34;&gt;
  &lt;script type=&#34;json/xblock-args&#34; class=&#34;xblock-json-init-args&#34;&gt;
    {&#34;xmodule-type&#34;: &#34;HTMLModule&#34;}
  &lt;/script&gt;
  &lt;h3 id=&#34;user-content-bayes-rule-and-the-fundamental-equation-of-speech-recognition&#34;&gt;Bayes rule and the fundamental equation of speech recognition&lt;/h3&gt;
&lt;p&gt;Speech recognition is cast as a statistical optimization problem. Specifically, for a given sequence of observations \(\mathbf{O} = \left\{ O_{1},\ldots,O_{N} \right\}\), we seek the most likely word sequence \(\mathbf{W} = \{ W_{1},\ldots,W_{M}\}\). That is, we are looking for the word sequence which maximizes the posterior probability \(P\left( \mathbf{W} \middle| \mathbf{O} \right)\text{.\ }\) Mathematically, this can be expressed as:&lt;/p&gt;
&lt;p&gt;\[\hat{W} = argmax_{W}P(W|O)\]&lt;/p&gt;
&lt;p&gt;To solve this expression, we employ Bayes rule&lt;/p&gt;
&lt;p&gt;\[P\left( W \middle| O \right) = \frac{P\left( O \middle| W \right)P\left( W \right)}{P(O)}\]&lt;/p&gt;
&lt;p&gt;Because the word sequence does not depend on the marginal probability of the observation \(P(O)\), this term can be ignored. This, we can rewrite this expression as&lt;/p&gt;
&lt;p&gt;\[\hat{W} = argmax_{W}P\left( O \middle| W \right)P(W)\]&lt;/p&gt;
&lt;p&gt;This is known as the &lt;em&gt;fundamental equation of speech recognition&lt;/em&gt;. The speech recognition problem can be cast as a search over this joint model for the best word sequence.&lt;/p&gt;
&lt;p&gt;The equation has a component P(&lt;em&gt;O&lt;/em&gt;|&lt;em&gt;W&lt;/em&gt;) known as an &lt;strong&gt;acoustic model&lt;/strong&gt;, that describes the distribution over acoustic observations &lt;em&gt;O&lt;/em&gt; given the word sequence &lt;em&gt;W&lt;/em&gt;. The acoustic model is responsible for modeling how sequences of words are converted into acoustic realizations, and then into the acoustic observations presented to the ASR system. Acoustics and acoustic modeling are covered in Modules 2 and 3 of this course.&lt;/p&gt;
&lt;p&gt;The equation has a component P(&lt;em&gt;W&lt;/em&gt;) called a &lt;strong&gt;language model&lt;/strong&gt; based solely on the word sequence &lt;em&gt;W&lt;/em&gt;. The language model assigns a probability to every possible word sequence. It is trained on sequences of words that are expected to be like those the final system will encounter in everyday use. A language model trained on English text will probably assign a high value to the word sequence &amp;ldquo;I like turtles&amp;rdquo; and a low value to &amp;ldquo;Turtles sing table.&amp;rdquo; The language model steers the search towards word sequences that follow the same patterns as in the training data. Language models can also be seen in purely text-based applications, such as the autocomplete field in modern web browsers. Module 4 of this course is dedicated to language modeling.&lt;/p&gt;
&lt;p&gt;For a variety of reasons, building a speech recognition engine is much more complicated that this simple equation implies. In this course, we will describe how these models are constructed and used together in modern speech recognition systems.&lt;/p&gt;
&lt;/div&gt;

  &lt;/div&gt;
&lt;/div&gt;

&lt;/div&gt;

  </div>
<div id="seq_content" role="tabpanel"></div>




------------


Deep speech


- Deep neural networks for acoustic modeling in speech recognition: The shared views of four research groups [[pdf]](http://cs224d.stanford.edu/papers/maas_paper.pdf)
- Speech recognition with deep recurrent neural networks [[pdf]](http://arxiv.org/pdf/1303.5778.pdf)
- Towards End-To-End Speech Recognition with Recurrent Neural Networks[[pdf]](http://www.jmlr.org/proceedings/papers/v32/graves14.pdf)
- Fast and accurate recurrent neural network acoustic models for speech recognition [[pdf]](http://arxiv.org/pdf/1507.06947)
- Deep speech 2: End-to-end speech recognition in english and mandarin [[pdf]](https://arxiv.org/pdf/1512.02595.pdf) (Baidu Speech Recognition System)
- Achieving Human Parity in Conversational Speech Recognition [[pdf]](https://arxiv.org/pdf/1610.05256v1) 
- [End-to-end Speech Recognition with Recurrent Neural Networks (D3L6 Deep Learning for Speech and Language UPC 2017)](https://www.slideshare.net/xavigiro/endtoend-speech-recognition-with-recurrent-neural-networks-d3l6-deep-learning-for-speech-and-language-upc-2017)
- [Deep Speech and Vision - Xavier Giro-i-Nieto - UPC Barcelona 2018](https://www.slideshare.net/xavigiro/deep-speech-and-vision-xavier-giroinieto-upc-barcelona-2018)
- [[PPT](https://github.com/gopala-kr/summary/blob/master/summaries/Week-1/lec26_audio.pptx)] [[PPT](https://github.com/gopala-kr/summary/blob/master/summaries/Week-1/LiDeng-BerlinOct2015-ASR-GenDisc-4by3.pptx)] [[PPT](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/07/HumansVsMachine-Afeka2017-invited.pdf)]

-----------------

- [Intelligence Quotient and Intelligence Grade of Artificial Intelligence](https://arxiv.org/abs/1709.10242)
- [What Is The Difference Between Siri And Viv?](https://www.forbes.com/sites/quora/2016/05/27/what-is-the-difference-between-siri-and-viv/#230a8fdf5b49)
- [How Siri Works – Interview with Tom Gruber, CTO of SIRI](http://www.novaspivack.com/technology/how-hisiri-works-interview-with-tom-gruber-cto-of-siri)
- [How Siri Works: Siri-A-Primer](http://www.venturewerks.com/Siri-A-Primer.pdf)
- [How Siri Works (jeffwofford.com)](https://news.ycombinator.com/item?id=3111133)
- [CHATBOT ASSISTING: SIRI](http://www.technicaljournalsonline.com/ijaers/VOL%20IV/IJAERS%20VOL%20IV%20ISSUE%20II%20JANUARY%20MARCH%202015/562.pdf)
- [Apple: Deep Learning for Siri’s Voice: On-device Deep Mixture Density Networks for Hybrid Unit Selection Synthesis](https://machinelearning.apple.com/2017/08/06/siri-voices.html)
- [Apple has designed a new Siri Architecture allowing Two Digital Assistants to Communicate with Each Other](http://www.patentlyapple.com/patently-apple/2017/05/apple-has-designed-a-new-siri-architecture-allowing-two-digital-assistants-to-communicate-with-each-other.html)

----------------
---------------

Appendix: Reference images

--------

Evolution of Search 


![cognitivesearch](https://marionoioso.com/wp-content/uploads/2018/06/cognitivesearch-768x414.jpg)

![1496154841914](https://static1.squarespace.com/static/56e9401ef8baf3149e959bb3/t/592d82cf86e6c0040d66a212/1496154841914/?format=750w)

------

Architecture of ASR:

![0*-fsj14f4eQo2EZEI](https://cdn-images-1.medium.com/max/1600/0*-fsj14f4eQo2EZEI.)

-----------

![1-s2.0-S0167639313000988-gr2](https://www.researchgate.net/profile/Alexey_Karpov2/publication/259118437/figure/fig1/AS:297010319118352@1447824186627/Architecture-of-a-state-of-the-art-automatic-speech-recognition-system-and-its-components.png)

-----------

Example App flow:

![diagram-of-speech-recognition](https://www.researchgate.net/profile/Hae-Duck_Jeong/publication/287429405/figure/fig2/AS:310678364672001@1451082902257/Data-flow-diagram-of-speech-recognition.png)

-----------

QA flow:

![1280px-DeepQA.svg.png](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/DeepQA.svg/1280px-DeepQA.svg.png?1532246161874)

-----------

<a href="https://www.researchgate.net/Architecture-to-develop-user-adapted-spoken-conversational-agents_fig3_288480562"><img src="https://www.researchgate.net/publication/288480562/figure/fig3/AS:329780403687425@1455637183466/Architecture-to-develop-user-adapted-spoken-conversational-agents.png" alt="Architecture to develop user-adapted spoken conversational agents."/></a>

--------------

IBM Watson(DeepQA) :

![DeepQA-Arch](https://researcher.watson.ibm.com/researcher/files/us-mike.barborak/DeepQA-Arch.PNG)


--------------

Alexa/Echo:


![alexa_skills_kit_architecture_diagram](https://3lhowb48prep40031529g5yj-wpengine.netdna-ssl.com/wp-content/uploads/2016/08/alexa_skills_kit_architecture_diagram.png)

![Ms9HNob9HyWcWkbk](https://cdn-images-1.medium.com/max/880/0*Ms9HNob9HyWcWkbk.png)

- [Build an Alexa Skill with Python and AWS Lambda](https://moduscreate.com/blog/build-an-alexa-skill-with-python-and-aws-lambda/)

--------

Google speech services:

![HBp13IJewSkrPZhb](https://cdn-images-1.medium.com/max/880/0*HBp13IJewSkrPZhb.png)


--------------

Google assistant(Actions workflow)

![action_sdk_workflow](https://www.grokkingandroid.com/wordpress/wp-content/uploads/2017/10/action_sdk_workflow.png)

- [Using the Actions SDK for Google Assistant Development](https://dzone.com/articles/using-the-actions-sdk-for-google-assistant-develop)

------

![google-action-request](https://www.jovo.tech/blog/wp-content/uploads/2017/08/google-action-request.png)

![[Tutorial] Build a Google Action in Node.js with Jovo](https://www.jovo.tech/blog/google-action-tutorial-nodejs/)

---------

Siri:

![a7a976303e8fa3c272824daea4706188](https://qph.ec.quoracdn.net/main-qimg-a7a976303e8fa3c272824daea4706188.webp)

-----------

![cortana](https://image.slidesharecdn.com/nlandry-developing-windows10-apps-with-speech-and-cortana-150826134754-lva1-app6891/95/building-windows-10-universal-apps-with-speech-and-cortana-28-638.jpg?cb=1440597026)


- [AI in Mobile Apps: How to Make an App like Siri](https://codetiburon.com/ai-mobile-apps-make-app-like-siri/)

---------

Sirius:

![sirius-free-voice-systems-1](https://res.infoq.com/news/2015/04/sirius-free-voice-assistant/en/resources/sirius-free-voice-systems-1.jpg)


------

![Watson-Cortana-AIs](https://marionoioso.com/wp-content/uploads/2017/04/Watson-Cortana-AIs.jpg)


---------
Mobile voice assistants architecture

![Mobile voice assistants architecture](https://www.cleveroad.com/images/article-previews/Basic-technologies-in-mobile-voice-assistants.png)


[how-to-create-virtual-assistant-apps-like-siri-and-google-assistant](https://www.cleveroad.com/blog/how-to-create-virtual-assistant-apps-like-siri-and-google-assistant)

--------------------

The complete ASR Infograph:


![oice_search-clean-hook](https://www.technology.org/texorgwp/wp-content/uploads/2018/07/voice_search-clean-hook.png)



----------

Bot ecosystem and frameworks:


![c2f9ee689ce32bef47152b8ed2046c1a](https://d3ansictanv2wj.cloudfront.net/bots-landscape-2-c2f9ee689ce32bef47152b8ed2046c1a.png)

--------

![5588dd73-2c97-4efb-9a8e-e24ff0f31806](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/5588dd73-2c97-4efb-9a8e-e24ff0f31806.png)

Source: [Conversational Bots Deep Dive – What’s new with the General Availability of Azure Bot Service and Language Understanding](https://azure.microsoft.com/en-us/blog/conversational-bots-deep-dive-what-s-new-with-the-general-availability-of-azure-bot-service-and-language-understanding/)


---------
--------------
