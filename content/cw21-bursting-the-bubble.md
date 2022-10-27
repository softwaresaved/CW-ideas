---
title: "Bursting the Bubble: Teaching PIs the value of good code"
author:
- Marion Weinzierl
- Sam Harrison
- Arielle Bennett
- Steve Crouch
- Mark Turner
year: 2021
type: collaborative-ideas
tags:
- guidance
- good-practice
---
### CW21 - 2021-03-30

Noodle - CI14-CW21


### **Participants**

* Marion Weinzierl (Durham University)
* Sam Harrison (UK Centre for Ecology & Hydrology)
* Arielle Bennett (Alan Turing Institute, London)
* Steve Crouch (SSI, Southampton)
* Mark Turner (Durham University)

---

### Notes

*   Marion: How to work with and take forward legacy code? Is there a checklist to make use of for this? Or develop an automatic script to parse the repo and tell me how to improve it?
    *   [https://software.ac.uk/sites/default/files/SSI-SoftwareEvaluationCriteria.pdf](https://software.ac.uk/sites/default/files/SSI-SoftwareEvaluationCriteria.pdf) - SSI's software evaluation criteria
    *   [https://github.com/RSE2-D2/RSE2-D2](https://github.com/RSE2-D2/RSE2-D2)
    *   [https://github.com/RSE2-D2/RSE2-D2/issues/33](https://github.com/RSE2-D2/RSE2-D2/issues/33) 
    *   [https://fair-software.eu/](https://fair-software.eu/)
    *   [https://bestpractices.coreinfrastructure.org/en](https://bestpractices.coreinfrastructure.org/en) - [https://bestpractices.coreinfrastructure.org/en/criteria/0](https://bestpractices.coreinfrastructure.org/en/criteria/0)
    *   From last years Hack Day [SiccarPoint/how_wrong_is_the_code: Repo for CollabW20 hack day - how wrong is the research code base? (github.com)](https://github.com/SiccarPoint/how_wrong_is_the_code) 
*   Sam: training - how to on-board traditional academics who know nothing about software sustainability?
    *   Marion: last year - how to sell the values of software practices to PIs - link to it
    *   [https://software.ac.uk/blog/2020-06-10-how-do-we-persuade-funders-support-software-maintenance](https://software.ac.uk/blog/2020-06-10-how-do-we-persuade-funders-support-software-maintenance)
    *   [https://software.ac.uk/blog/2020-05-27-how-engage-research-group-leaders-sustainable-software-practices](https://software.ac.uk/blog/2020-05-27-how-engage-research-group-leaders-sustainable-software-practices)
    *   [https://software.ac.uk/blog/2020-05-25-maintaining-your-legacy-tips-making-legacy-code-sustainable](https://software.ac.uk/blog/2020-05-25-maintaining-your-legacy-tips-making-legacy-code-sustainable)
    *   [https://software.ac.uk/blog/2020-05-22-carrot-and-stick-approaches-promoting-research-software-community](https://software.ac.uk/blog/2020-05-22-carrot-and-stick-approaches-promoting-research-software-community)
    *   [https://software.ac.uk/blog/2020-05-19-incentives-good-research-software-practices](https://software.ac.uk/blog/2020-05-19-incentives-good-research-software-practices)
    *   Etc… This problem seems to come up again and again!
*   Mark: a tool that indicates you are building up technical debt - a plugin/analysis of repo. Technical debt - builds up over time when you work on code, focusing on features not maintenance. Easy metrics to pick up
*   A lot of communities looking into these issues, but why don't we do it? FAIR, Turing, etc. HPC/RSE communities, Carpentries, but it's not really happening. Is this a communication issue - a bubble? Level of communication needs to be improved, somehow incentivise and lower the barrier to entry for doing these things. Do we need to collect these things? Same idea coming up again and again
*   Resource list somewhere? Another kind of event?
*   Key difficulty with training e.g. PIs - availability. How to convince them? With PIs, it comes down to making them understand the importance of this, adjust expectations. Journals are increasingly requiring researchers to conform to better code practices.


### Bursting the bubble: Teaching PIs the value of good code


### **Context / Research Domain**

Issues with poor coding practices are typically tackled via community interest groups or training sessions (for example Carpentries training), which introduces the skills and collaboration needed to write code well. Training is also often aimed at early career researchers such as PhD students or postdocs and has been adapted to suit the needs of different scientific domains from astrophysics to zoology. 

However, developing an understanding of good and bad coding practices, and the benefits and risks of each, also needs to be promoted in more established researchers, such as PIs. At this career stage, their influence on the research culture and therefore coding practices of their groups and labs is significant. PIs need to be onboard with promoting good coding if the training aimed at ECRs is to stick and translate into long term culture change, right across the research domains. 

Of course, underpinning the problem is the continued use of incentives in the academic system in particular that do not reward good coding practices directly and instead focus on outputs such as papers, where code quality is of secondary importance. 

**Problem**

In our discussion there were a number of issues around engaging PIs and researchers in good software practices and applying guidelines that came up, as well as the problem of legacy code and how to improve it in an automated or at least structured way. Diving deeper into this discussions, and doing a quick online research, it turns out that these issues have been discussed (and blogged about) repeatedly in previous Collaboration Workshops, and elsewhere. Why does it still seem that no progress has been made? Why does having resources like the Turing Way Handbook, and initiatives like FAIR for software seem not to have a groundbreaking impact in research? It seems that there is an issue in both communication between communities and initiatives, and an issue in incentives and time commitment from PIs and researchers. How can we burst these bubbles and improve the communication? How can we make it easy for everyone to find the resources on good software practices that they need, and to apply them? 


### **Solution**

The key to overcoming many of these problems is gaining an appreciation of the promises and the pitfalls of software development at the level of the PI. Whilst a lot of research, tools, practices and guidance exists, we advocate that **what is also needed is concrete evidence of projects that have succeeded and failed that speaks strongly to PIs understanding and interests**.

By reviewing the existing resources and research software projects and highlighting the practical causes and criteria behind their success or failure in terms of practices, PIs may then relate these to activities within their own projects, and project potential future outcomes for those projects. From this understanding, the idea is that PIs are then incentivised to increase time and effort for practices and activities that promote better practice.


### **Diagrams / Illustrations**


![Cumulative functionality against time](../images/cx21-cumulative-functionality.jpg)


_Low internal quality might seem to ‘do the job’ for short-term projects where time is of the essence. Sustainable development efforts benefit from slower development cycles that encapsulate more refactoring and greater attention to design decisions._


![A bursting soap bubble](../images/cw21-bursting-bubble.jpg)

### Licence

These materials (unless otherwise specified) are available under the Creative Commons Attribution 4.0 Licence. Please see the [human-readable summary](https://creativecommons.org/licenses/by/4.0/) of the CC BY 4.0 and the full [legal text](https://creativecommons.org/licenses/by/4.0/legalcode) for further information. 

