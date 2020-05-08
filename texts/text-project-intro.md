---
title: "Investigating feedbacks between behavioural strategies and landscape charactersistics: An Introduction"
author: Pratik Gupte and Christoph Netz
date: 8^th^ May, 2020
documentclass: article
fontfamily: tgtermes
geometry: margin=1.2in
table-of-contents: true
toc-depth: 2
bibliography: "../course-2020-comm-ecol.bib"
csl: "../oikos.csl"
header-includes:
   - \usepackage{lineno}
   - \setcounter{secnumdepth}{2}
---

\linenumbers

This document is a brief introduction to the Community Ecology project _Investigating feedbacks between behavioural strategies and landscape charactersistics_.

# Contact

## Who

There are two supervisors, Pratik and Christoph, but this project was born of Pratik's old and failing mind. Contact Pratik for immediate issues with R, Python, git/Github, and/or Peregrine, but get in touch with either/both of us for conceptual issues.

## How

You can contact us by email for now, until we set up a Slack or similar. If you have a preference let us know.

Name|Email
---|---
Pratik|p.r.gupte@rug.nl
Christoph|c.f.g.netz@rug.nl

NB: We also have `@student.rug.nl` addresses in the system which we don't use. If you email these addresses, we're never going to know.

## When and why

In general, feel free to contact us when you think it's necessary. We'll get a system set up for contact hours etc. in discussion with you. Below, you can see when we're busy with other meetings.

**NB:** These are difficult times, and we get that. Feel free to contact us if you have an external issue that may impact your participation in the course. You needn't give details, but let us know.

Name|Usually unavailable
---|---
Pratik|Mondays 11:00 -- 12:00
---|Wednesdays 10:30 -- 12:00
---|Fridays 10:00 -- 12:00
---|All days 18:00 -- 20:00
Christoph|Wednesdays 10:30 -- 12:00

# Project Description

> Just in case you'd forgotten what you signed up for.

The availability of resources determines the movement and behaviour of individuals on resource landscapes. Simultaneously, individuals deplete resources and thus change the resource landscape they inhabit. The feedback between individuals and resources can have important eco-evolutionary implications, as individuals adapt their behavioural strategies to the resource landscape. This change can itself modify the resource landscape such that it favours a very different behavioural strategy.

Such eco-evolutionary dynamics are difficult to investigate, particularly if there are qualitatively different types of behaviour among individuals. 
In the Kleptomove simulation model, we have considered two such behaviours: searching for food, or stealing food from other individuals who have already found a food item (‘kleptoparasitism’). The model implements the evolution of the two strategies and the implications for the resource landscape. Though kleptoparasitism always evolves and establishes itself as a common strategy, visual inspection of the simulation results suggests that this only occurs at specifc locations in the resource landscape.

This project will study the correlation between each strategy and the spatial characteristics of the resource landscape, and examine the consequences of the evolution of kleptoparasitism on the resource landscape. The student will use Kleptomove output to identify global ‘tipping points’ in the behavioural strategy, quantify local indicators of spatial association in the landscape at distinct time-points before, during, and following the establishment of kleptoparasitism in the population, and quantify the global change in LISA classes.

# Workflow

## Reading literature

It's important to know what you're dealing with, and reading previous findings is a good place to begin. Take a week to read the literature.

A literature collection is being assembled in a Zotero group library: **[https://www.zotero.org/groups/2499059/course-2020-comm-ecol](https://www.zotero.org/groups/2499059/course-2020-comm-ecol)**. You'll need to register on Zotero and request access. Contact us if this gets confusing.

Zotero **[link: https://www.zotero.org/](https://www.zotero.org/)** is a reference management program for the storage and citation of academic papers. Download Zotero, the connector for your browser, and optionally the plugin for your word processor. Create an account and sync the group library for access to the references and pdfs.

### How to approach the literature list

1. Begin by reading papers that give a broad overview of the fields of spatial ecology [@levin1992], animal movement [@nathan2008] and the links between movement and large-scale processes such as community assembly [@jeltsch2013; @schlagel2020]. 

    Consider a specific example from a simulation study of how individual movement behaviour can lead to large scale patterns in the spread of rabies [@jeltsch1997].

2. Move on to reading about the evolution of individual behavioural strategies [@wolf2010; @wolf2012], and the consequences of variation in strategies for ecology and evolution [@wolf2012a]. 

    Read about the North American bluebird system  in @duckworth2007 as an illustration of these concepts.

3. The data you'll analyse comes from _Kleptomove_, a spatially explicit individual based simulation model (IBM); read what IBMs are and why they were developed [@huston1988; @deangelis2005].

    Return to this document to read more about _Kleptomove_ in the section below.

    Continue to explore how IBMs are used to study processes at both the landscape scale [such as spatial patterning; @grimm2005] and the individual level [such as animal movement; @deangelis2019].

4. In _Kleptomove_ the strategy of stealing food from other individuals, or kleptoparasitism, abruptly takes over the population until a large proportion of individuals attempt to steal from others. 

    Such abrupt shifts in a system are called _critical transitions_ [@scheffer2001], and the state of a system at which these shifts occur is called a _tipping point_[@vannes2016].

    Critical transitions occur in many different systems: from landscapes [@hirota2011] to animal groups [@tunstrom2013]. Read these papers about critical transitions to understand more.

5. Critical transitions are often referred to as 'catastrophic', and there is wide ranging interest in detecting them before they happen. The spatial characteristics of landscapes can hold clues to impending critical transitions. 

    Read @guttal2009 and @dakos2010 to see how spatial correlation (how similar are two points on the landscape) can indicate a critical transition.

5. You'll be doing spatial autocorrelation analysis at two scales: global, i.e., referring to the full extent of the Kleptomove landscape, and local, i.e., relating to smaller areas within the landscape. 

    Read about global spatial autocorrelation [@sokal1978; @sokal1978a], and then local spatial autocorrelation [@sokal1998; @sokal1998a]. Read [@anselin1995] to look at a specific measure of local spatial autocorrelation called _Moran I local_.

## Learning tools

### Organisation

1. Slack for communication
2. Zotero for reference management

### R and R projects

### Python scripts

### git and Github

## Getting data

### Accessing data from iRods



## Writing code

## Mid-project presentation

## Final presentation 

# Tools

## Critical

## Useful

# References