---
title: "Dealing with Legacy Code"
author:
- Patricia Herterich 
- Cat Smith 
- Christopher Fullerton
- Raniere Silva
- Philipp Boersch-Supan
year: 2020
type: collaborative-ideas
tags:
- legacy-code
- training
- reproducibility
---
### CW20 - 2020-03-31 to 2020-04-02

Idea 4 - CI4-CW20

Dealing with Legacy Code


### **Participants**

Patricia Herterich_ _

Cat Smith_ _

Christopher Fullerton

Raniere Silva

Philipp Boersch-Supan



---



### **Context / Research Domain**

All research domains which have to contend with/rely on legacy code which does not conform to best practices.


### **Problem**

Researchers are instructed to use some legacy code written by their team, a third party or even themselves a while ago. The code isn't documented or unit tested. Researchers face the problem of using the code in the dark. How can researchers save the legacy code and lower the learning curve for future users?


### **Solution**

The outcome of this hack idea session is a checklist (preferably ordered by importance) which outlines things that can/should be done to help improve the code. This might need to differ for different programming languages or contexts but much will probably be similar. Sub-checklists could be useful covering topics like introducing tests into a large legacy code base, which things should be documented first, etc. 

Some ideas we already came up in our discussion and which could inform the development of such a checklist as as follows:



*   Try to (1) install/setup and (2) use legacy code and document successful steps. You can start writing things in the README file and later, when the documentation starts to be too long, you can migrate to another platform and break it into sections.
    *   Depending of the language and dependencies used by your project, is useful to future users to have a Makefile (for examples, projects in C or Fortran) or a Dockerfile (for example, projects in Django or Node.js) as those files reduce repetitive typing from users
*   Ask or pay someone new to the project to review the steps that you documented (particularly with regards to download/installation/setup). Undergraduate students and earlier stage RSE are great for this task as they might be also new to technologies that you are using. For example, students might be new to Git submodules and report to you that additional instructions are needed. This will also help you identify hardware configurations that need to be documented, for example Docker requires virtualisation enabled.
*   Restructuring/Refactoring/Rewriting code in the original language can be useful:
    *   documentation still to be worked on, but code is now clearer. 
    *   Restructuring the code (e.g. main project and sub-module) can make sharing easier; 
    *   Can make translating to other languages easier as you can progress with smaller sections/modules and reduce the risk of breaking with untested original code
*   Introducing testing is really difficult if you have one large complicated workflow it might be best, if applicable to the code, to start with overall tests that ensure the final result is correct before introducing unit tests for smaller sections
*   Contact your university library and ask if they have a procedure to archive/register software. If they do, they might be able to provide you with additional check (for example, to have a citation file or DOI) and staff time to check your code. The Data Curation Network has created primers to review a range of data and code types that can facilitate that process: [https://datacurationnetwork.org/resources/data-curation-primers/](https://datacurationnetwork.org/resources/data-curation-primers/) The hackday could create an index of institutions listing the support services available.


### **Diagrams / Illustrations**

You can include one or two diagrams in this section. Please ensure you have the right to use the image(s), and include an attribution if applicable.

