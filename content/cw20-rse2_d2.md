---
title: "RSE2_D2"
author:
- Yo Yehudi
- David Perez-Suarez
- Blair Archibald
- Marion Weinzierl
- Vahid Garousi
year: 2020
type: collaborative-ideas
tags:
- twitter
- training
- rse
---

### CW20 - 2020-03-31 to 2020-04-02

RSE2_D2 - CI10-CW20


### **Participants**

* Yo Yehudi - Software dev and EngD student (Cambridge and Manchester) 
* David Perez-Suarez - RSE at UCL
* Blair Archibald - 2017 fellow, Postdoc Glasgow (soft spot for Haskell) 
* Marion Weinzierl - RSE at Durham University, Not a fellow... yet!
* Vahid Garousi - Belfast 

---

### **Context / Research Domain**

A long time ago, in an office far, far away, RSEs and researchers were developing software and may not be aware of all the good practices and are in need of a bit of motivation.

### **Problem**

The researchers of the universe need help with their software, but where can they turn? Where else but to set their communicators to Twitter to ask for help and advice from the one and only RSE2-D2.

### **Solution**

RSE2-D2 is a twitter bot providing advice about creating/maintaining research software. It provides, amongst other things (see images below):

*   Automated analysis of github links
    *   “Help @RSE2_D2 analyse! github.com/OpenResearcher/somecoolproject. You’re my only hope”
    *   Adding a readme/license
    *   Revisit some old issues that haven't been labeled
    *   To praise to new contributors
    *   To praise long term contributors
    *   To praise maintainers
    *   Add a CoC
    *   No CI detected!
    *   No style followed? Try this tool for this language! GH: @pep8speak ...
*   Share moral lessons and horror stories
    *   [https://www5.in.tum.de/~huckle/bugse.html](https://www5.in.tum.de/~huckle/bugse.html) 
    *   #horrorstories slack room links
*   Share motivational tweets and useful reminders - commit your code! Use a colleague as a rubber duckie. Check your contributing guidelines are up to date! Don’t forget to write a docstring for that method. It’s a feature, not a bug.
*   Today is a good day for writing a new test! #MondayMotivation #Testing
*   Updates about new open science tooling
*   Daily/weekly updates on test coverage
*   Reminders to write documentation / tests
*   Something along the lines of @CodeWisdom on Twitter https://twitter.com/CodeWisdom
*   Check how many/which Github issues are open and flag one up every so often
    
    *   Triage Tweets: “Project y” needs some help (based on issues)
*   A competition with other users, you get points for documentation, test coverage, … You can win a 1-2-1 chat with a real-life RSE to talk about your code!
*   Check if tools are unmaintained: @scipy we haven’t seen a commit recently, you alright?
*   Language month/week. Tweet about podcasts, resources, link to other tweet accounts of that particular language
*   Tip of the day
*   A help! Command to summon a real RSE


### **Diagrams / Illustrations**

![The rse_d2 bot in action.](../images/cw20-rse_d2.jpg)


![RSE2_D2 helpful tweets.](../images/cw20-rse2_d22.jpg)


_R2-D2 image via [https://www.shopdisney.co.uk/disney-store-r2-d2-interactive-action-figure-star-wars-461010647492.html](https://www.shopdisney.co.uk/disney-store-r2-d2-interactive-action-figure-star-wars-461010647492.html) _


_Original brainstorm notes_

Discussion:

Brainstorming session: 

Blair: Try to automate make files. Strace can wrap the commands they will use and "basically" get all that into a make file. Then you can edit it. Stop recording or whatever it is.... You can get reproducibility from it. One issue is that you can't use strace in windows.

Q: Are makefiles contemporary and still popular? A: good for workflow if not for software. 

Q: Other tools like snakemake?

Yo: During discussion group yesterday they talked about covid. What was found that they need project leadership. Project leadership training programme to be deployed quickly and used by others.

Q: Delivery length?

Marion: Legacy software that hasn't been touch for a long time, for example a fortran and c++ code that are tied and they involved a set of scripts/languages that glue them together. It's there a way that helps to understand how they work, debug them, ...

How to bootstrap messy code? 

It's up to the maintainers to modernise, a chicken-egg situation because all it's entangled.

When should we put it under git? It should go from the beginning, then you can track the changes better.

Horror stories blog, piece of art, messy code of piece of poetry

David: Maybe we could analyse messy code with metrics and recommendations. E.g. shellcheck for shell scripts, give hints to tools (high level code checkers etc) - interaction tools etc. Tips for integrating certain technologies (front end/back end), what might be better in other languages/APIs/Structure. Success stories to drive the guidance. A wizard RSE

Q: What about RSEBot, the twitter bot/ RoboRSE

*   Detect github links: and recommend  (maybe not all at once, but if they are many they can be delivered one per week....)
    *   adding a readme/license
    *   Revisit some old issues that haven't been labeled
    *   To praise to new contributors
    *   To praise long term contributors
    *   To praise maintainers
    *   Add a CoC
    *   No CI detected!
    *   No style followed? Try this tool for this language! GH: @pep8speak ...
*   `@rse_bot analyse!` 

        -  Maybe some metric, e.g. “looking great”, “how about some more licencing” (needs to fit in the 280 Character limit (wow that’s a lot more than I thought!)

*   Share moral lessons and horror stories
    *   [https://www5.in.tum.de/~huckle/bugse.html](https://www5.in.tum.de/~huckle/bugse.html) 
    *   #horrorstories slack room links
*   Share motivational tweets and useful reminders - commit your code! Use a colleague as a rubber duckie. Check your contributing guidelines are up to date! Don’t forget to write a docstring for that method. It’s a feature, not a bug.
*   Today is a good day for writing a new test! #MondayMotivation #Testing
*    Updates about new open science tooling
*    Daily/weekly updates on test coverage
*    Reminders to write documentation / tests
*    Something along the lines of @CodeWisdom on Twitter https://twitter.com/CodeWisdom
*   Check how many/which Github issues are open and flag one up every so often
    
    *   Triage Tweets: Project y needs some help (based on issues)
*   A competition with other users, you get points for documentation, test coverage, … You can win a 1-2-1 chat with a real-life RSE to talk about your code!
*   Check if tools are unmaintained: @scipy we haven’t seen a commit recently, you alright?
*   Language month/week. Tweet about podcasts, resources, link to other tweet accounts of that particular language
*   Tip of the day
*   A help! Command to summon a real RSE (maybe it is a wizard…)
