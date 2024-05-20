---
accordion:
- funder: NIHR
  links: https://wsca-measurement.co.uk/
  pi: Becca Rendall, NIHR
  tech: PHP, Laravel
  title: Whole School & College Approach Online Tool
- tech: Unity, C#, Oculus Rift
  title: 'Colourmind: VR Colour Shifting'
- tech: Oracle Apex, Python
  title: Language Health Centre
- tech: PHP, Laravel
  title: Trial Pigeon
- tech: Node.js, React
  title: CALMS
- tech: TBC
  title: Landecker Digital Memory
- tech: Unity, C#
  title: Dog-go-nogo
- tech: PHP, Laravel
  title: SPRAR
accordion2:
- funder: Unboxed (Uk Government)
  links: https://perceptioncensus.dreamachine.world/
  pi: Anil Seth, University of Sussex & Fiona Macpherson, University of Glasgow
  tech: Jspsych, PHP, Laravel
  title: Perception Census
- tech: Unity, C#, C++, iOS
  title: Colourspot
- tech: Moodle, PHP
  title: Parenting with Anxiety
- tech: React, AWS
  title: 'Octopath: Digital Histopathology'
- tech: TBC
  title: Valuable Lives
- tech: Objective C, iOS
  title: Soundsight
- tech: PHP, Drupal, Javascript
  title: Syntoolkit
- tech: Python
  title: Mass Observation Visualisation
- tech: Javascript
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
    