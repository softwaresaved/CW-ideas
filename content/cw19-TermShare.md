---
title: "Terminal History Sharing"
author:
- Jason Gates
year: 2019
type: hack-ideas
tags:
---
### Collaborations Workshop 2019 (CW19) #CollabW19          2019-04-01 to 2019-04-03

Terminal History Sharing - HP3-CW2CC


### **Hackday Idea Proposer**

Jason Gates - jmgate@sandia.gov



---


_This document should be used to capture the information for a Hack Day Idea._


### **Context / Research Domain**

_Training_


### **Problem**

_When running in-person training classes that involve live coding, requiring participants to follow along with what the instructor is doing in a terminal on the screen and replicating that on their own machine, a common complaint is that the terminal input and output winds up scrolling off the top of the screen too soon.  Participants can stop the class and ask the instructor to scroll back up so they can see what they missed, but they are often reluctant to do so for a variety of reasons.  It would be ideal if all participants had the ability to scroll back through the instructor’s terminal input/output independently.  In that way they would always have access to what they need to follow along and catch up, and the pace of the class is unhindered.  Unfortunately there are no out-of-the-box solutions for this._

_Design Specifications:_



*   _Participants will not have login access to the instructor’s machine._
*   _Participants may not even be on the same network as the instructor’s machine._
*   _Participants should be able to scroll back up to the beginning of class at any time and see everything as it was displayed on the instructor’s screen._
*   _Bonus:_
    *   _If we could implement the solution in such a way that a participant could toggle between viewing just the command line input vs input and output (i.e., “I just want to know what command to type”), that would be great._




### **Solution**

_Here’s one solution, though there may be others out there.  We should be able to do something along the lines of the following:_



*   _At the beginning of a training session:_
    *   _Redirect the terminals’ stdout and stderr both to the screen and to a file._
    *   _Start a cron job running every second that:_
        *   _Checks for an update to that file._
        *   _If an update exists, commit it to a repository and push._
    *   _Have participants pull up this history file in a browser (GitHub, GitLab)._
    *   _Tell them anytime they want to look back in history they can refresh that page._
*   _Continue the class as you normally would._
*   _Be sure to switch off that cron job when the class is over._


### **Diagrams / Illustrations**

_Not applicable._

