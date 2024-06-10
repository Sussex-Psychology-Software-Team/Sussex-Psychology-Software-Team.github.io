---
accordion:
- description: An online toolkit to allow educational settings to self-assess their
    whole school and college approach to mental health.    The app was developed over
    the course of 2 weeks and has had over 300 schools sign up in the first 4 months
    of release.
  funder: NIHR
  links: https://wsca-measurement.co.uk/
  pi: Becca Rendall, NIHR
  tech: PHP, Laravel
  title: Whole School & College Approach Online Tool
- description: We adapted the latest Oculus rift headset to use 'shaders' which accurately
    map realistic colours to a transformed colour space, in order to allow experimentation
    with the human visual system under different visual colour environments.
  funder: ESRC
  pi: Anna Franklin
  tech: Unity, C#, Oculus Rift
  title: 'Colourmind: VR Colour Shifting'
- description: We created a frontend, and contributed to the MLOPs behind a new service
    designed to allow researchers to access machine learning models for categorising
    hatespeech online.
  funder: Oracle
  pi: Paul Keene
  tech: Oracle Apex, Python
  title: Language Health Centre
- description: A new service to manage trial related communications (email, SMS, in-app).  Reserarchers
    can write up emails, and use a flow chart to manage sending reminders and integrate
    with data gathering platforms such as Qualtrics.
  funder: University of Sussex
  pi: James Alvarez
  tech: PHP, Laravel
  title: Trial Pigeon
- description: "We were tasked with updating a mobile application to be used by parents\
    \ receiving mental health services for children\u2019s disruptive behavioural\
    \ problems and by academic researchers in this field.  The app required software\
    \ updates and extensive editing to allow it to be used in a clinical setting to\
    \ monitor progress of the intervention."
  funder: UCL
  pi: Emily Midouhas
  tech: Node.js, React
  title: CALMS
- description: We are about to embark on creating web software to help preserve the
    testimony and memories of Holocaust survivors.  Design workshop stage will begin
    June 2024, with the project framework aiming to be online within the year.
  funder: Landecker
  pi: Victoria Walden
  tech: TBC
  title: Landecker Digital Memory
- description: An implementation of classic attentional control paradigms in the form
    of tablet games.  We created a series of tasks to allow experimental study of
    variants of this paradigm in Unity with C#.
  funder: Univertsity of Sussex
  pi: Dominique Makowski
  tech: Unity, C#
  title: Dog-go-nogo
- description: An internal tool for the psychology department which streamlines the
    yearly data gathering for various metrics.  A customisable form creation package,
    with a UI design to help send reminders and encourage users to fill out necessary
    data before deadlines.
  funder: University of Sussex
  pi: John Drury
  tech: PHP, Laravel
  title: SPRAR
- description: We inherited a website and an important tool using natural language
    processing to extract and present themes from first-hand testominies on events
    given by the public.  The site required a careful upgrade, and provisioning on
    a new service and several tricky bugs to be fixed!
  funder: University of Sussex
  pi: Justyna Robinson
  tech: Python
  title: Mass Observation Visualisation
- description: We are currently working on this real-time video chat project with
    a unique method of allowing students (and staff) to meet and discuss matters within
    a course.
  funder: University of Sussex
  pi: Matthias Goebel
  tech: AWS, Javascript, PHP
  title: Circles
accordion2:
- description: An award winning ('Creative effectiveness' category in the CR Annual
    Awards 2024) online test platform , a collaboration between Sussex and Glasgow
    Universities and Collective Act. In total, 33,780 people from 133 countries took
    part, completing 102,689 sections of The Perception Census, making it the largest
    study of its kind. The findings and insights will impact numerous academic fields
    from neuroscience, to philosophy, to anthropology. The tests included questionnaires,
    optical illusions and many different kinds of interactive multimedia based evaluations
    of perceptual skills and differences.
  funder: Unboxed (Uk Government)
  links: https://perceptioncensus.dreamachine.world/
  pi: Anil Seth, University of Sussex & Fiona Macpherson, University of Glasgow
  tech: Jspsych, PHP, Laravel
  title: Perception Census
- description: Colourspot is an iPad game that provides an indicative diagnostic assessment
    of childrens' colour vision. Children tap coloured dots, and it runs statistical
    models to detect common colour vision deficiencies. It is currently undergoing
    a certification process for UKCA marking. The app was built in Unity, with animations
    and illustrations provided by a designer. The game's display required custom shaders
    to render a controlled presentation of colours.
  funder: ESRC
  pi: Anna Franklin
  tech: Unity, C#, C++, iOS
  title: Colourspot
- description: The Parenting with Anxiety app is an online version of a successful
    intervention for parents who have anxiety. The aim of the intervention was to
    teach parents how to manage their anxiety in a way that makes it less likely to
    pass on to their children. It was built in Moodle with a RCT framework custom
    programmed. The results of the RCT were positive and the app is currently in the
    stages of being implemented bu tje Kent Surrey Sussex Academic Health Science
    Network!
  funder: Kavli
  pi: Sam Cartwright-Hatton
  tech: Moodle, PHP
  title: Parenting with Anxiety
- description: We built the React frontend dashboard for this AI-powered software
    to assist pathologists in performing their daily tasks.
  funder: UCL
  pi: Charles-Antoine Collins-Fekete
  tech: React, AWS
  title: 'Octopath: Digital Histopathology'
- description: We collaborated on a series of design workshops with the Valuable Lives
    team at UCL in order to produce requirements specifications and design briefs
    for a new website providing public access to records of enslaved individuals from
    the 19th century.
  funder: UCL
  pi: Matthew Smith
  tech: TBC
  title: Valuable Lives
- description: Soundsight is an iOS app which uses depth information from the iPhone
    camera to generate sounds, which visually impaired people can use to help with
    navigation. Depth information from the native iPhone cameras, and from third party
    hardware is transformed into a realtime stream of parameters which are hooked
    up to a variety of sound loops. The user has the experience of sound changing
    as they navigate towards and away from obstacles, as well as the quality of sound
    changing with colour shifts.
  funder: University of Sussex
  pi: Jamie Ward
  tech: Objective C, iOS
  title: Soundsight
- description: Syntoolkit started as a series of customisable tests for different
    types of synaesthesia. It grew into a general purpose platform for creating and
    hosting psychology experiments, with a form builder, experiment flow, and results
    sharing interface. It is now used within the department by many researchers to
    help spin up psychology experiments quickly and for free, and to share and collaborate
    with students and other researchers.
  funder: ESRC
  pi: Julia Simner
  tech: PHP, Drupal, Javascript
  title: Syntoolkit
- description: In order to conduct experiments on the effects of street environments
    on a variety of psychological instruments, we created an immersive platform to
    allow the use of Google Images within VR headsets.
  funder: University of Sussex
  pi: Matthias Goebel
  tech: Javascript
  title: VR Streeview
layout: home
title: Projects
---

The team have worked on a number of projects in the past, and are always looking for new opportunities to collaborate.
Here are some of the projects we have worked on:

### Current projects:
<ul class="jekyllcodex_accordion">
    {% for item in page.accordion %}
    <li>
        <input id="accordion{{ forloop.index }}" type="checkbox" />
        <label for="accordion{{ forloop.index }}">
            {{ item.title }}
        </label>
        <div>
            <p>{{ item.description }}</p>
            <ul>
                {% if item.pi %}<li><strong>PI:</strong> {{ item.pi }}</li>{% endif %}
                {% if item.funder %}<li><strong>Funder:</strong> {{ item.funder }}</li>{% endif %}
                {% if item.tech %}<li><strong>Technologies:</strong> {{ item.tech }}</li>{% endif %}
                {% if item.links %}<li><strong>Links:</strong> {{ item.links }}</li>{% endif %}
            </ul>
        </div>
    </li>
    {% endfor %}
</ul>

### Past projects:
<ul class="jekyllcodex_accordion">
    {% for item in page.accordion2 %}
    <li>
        <input id="accordion2{{ forloop.index }}" type="checkbox" />
        <label for="accordion2{{ forloop.index }}">
            {{ item.title }}
        </label>
        <div>
            <p>{{ item.description }}</p>
            <ul>
                {% if item.pi %}<li><strong>PI:</strong> {{ item.pi }}</li>{% endif %}
                {% if item.funder %}<li><strong>Funder:</strong> {{ item.funder }}</li>{% endif %}
                {% if item.tech %}<li><strong>Technologies:</strong> {{ item.tech }}</li>{% endif %}
                {% if item.links %}<li><strong>Links:</strong> {{ item.links }}</li>{% endif %}
            </ul>
        </div>
    </li>
    {% endfor %}
</ul>

<style>
    ul.jekyllcodex_accordion {position: relative; margin: 1.4rem 0!important; border-bottom: 1px solid rgba(0,0,0,0.25); padding-bottom: 0;}
    ul.jekyllcodex_accordion > li {border-top: 1px solid rgba(0,0,0,0.25); list-style: none; margin-left: 0;}
    ul.jekyllcodex_accordion > li input {display: none;}
    ul.jekyllcodex_accordion > li label {display: block; cursor: pointer; padding: 0.75rem 2.4rem 0.75rem 0; margin: 0;}
    ul.jekyllcodex_accordion > li div {display: none; padding-bottom: 1.2rem;}
    ul.jekyllcodex_accordion > li input:checked + label {font-weight: bold;}
    ul.jekyllcodex_accordion > li input:checked + label + div {display: block;}
    ul.jekyllcodex_accordion > li label::before {content: "+"; font-weight: normal; font-size: 130%; line-height: 1.1rem; padding: 0; position: absolute; right: 0.5rem; transition: all 0.15s ease-in-out;}
    ul.jekyllcodex_accordion > li input:checked + label::before {transform: rotate(-45deg);}
</style>
    