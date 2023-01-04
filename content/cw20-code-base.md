---
title: How Wrong Is The Research Code Base?
author:
- Dan Hobley
year: 2020
type: hack-day
tags:
- software
- development
---


### CW20 - 2020-03-31 to 2020-04-02

Alpha - HP1-CW20


### _How Wrong Is The Research Code Base?_


### **Hackday Idea Proposer**

**Dan Hobley**





### **Context / Research Domain**

General research software development


### **Problem**

This is motivated by four observations:



1. There is a huge legacy science codebase, supporting lots of publications
2. Even professional software developers make errors at 15-50 per 1000 lines of code (McConnell, 2004)
3. Modern software best practice (reviewing, testing, etc.) has only recently begun to penetrate the research software community, broadly defined
4. Without formal testing, only code breaking bugs and those that are obviously wrong are likely to be caught.

So, _<span style="text-decoration:underline;">most legacy code is wrong</span>_. The famous cases become notorious, but the problem is probably pervasive. This proposal aims to quantify how broken, and how severe this problem might be - ideally heading towards a publishable standard of work.


### **Solution**

The github API provides a tool to have a crack at answering this. The first objective of the team will be to define exactly what method/approach will get used, but I foresee something broadly like this:



1. Assume that code that makes it to Github is broadly representative of the wider code base (this is questionable… Track with changes through time?) So, use the API to **randomly sample repos**.
2. **Separate out the “research” repos** using key terms. - “doi.org/”
3. **Separate code that uses tests** from that which doesn’t - tested code should perform better in any metrics the project makes. By ratio-ing tested against untested code, we should be able to assess the quality of the legacy code (like, or worse than, the untested Github code) against the (broadly known) quality of the tested code.
4. Try to **track bug fixing** once the code makes it to Github. We can assume any bug caught on github is the pernicious variety. Identify trends through time. This will probably also depend on number of editors active, and how “mature” the code is on github. These should be usable to back-project the bug density when the code went up on Github.
5. **Survey the nature of the bugs found. **How severe are they? What fraction are code-breaking?
6. Use what we learn by **comparison to the tested code** how broken the untested code might be. We can probably assume the average error rate in tested vs untested code should be the same (??), so what’s happening in the tested code should be a guide to the untested code… which is probably broadly representative of the legacy code.

Clearly, much detail to be added here, but that’s the spirit of it.

The visualised final output here will be ultimately, an estimate of how many bugs are found in poorly tested/legacy code under a variety of possible conditions (age, users, etc).

This hack would probably suit Python-minded people, who are also familiar with simple, widely-used Github workflows and the very basics of testing. Surveying the nature of bugs would be a non-code-y job. Specific API knowledge probably isn’t necessary, but could be useful if someone has it.

Anyone know if this has been tried before (with these kinds of tools)?

[https://stackoverflow.com/questions/26881441/can-you-get-the-number-of-lines-of-code-from-a-github-repository/29012789#29012789](https://stackoverflow.com/questions/26881441/can-you-get-the-number-of-lines-of-code-from-a-github-repository/29012789#29012789)

