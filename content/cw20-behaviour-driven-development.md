---
title: "Adding Behaviour Driven Development to Exploratory Research Notebooks"
author:
- Jon Massey
- Ben Krikler
- Anastasis Georgoulas
- Matthew Bluteau
- Steve Crouch
year: 2020
type: collaborative-ideas
tags:
- notebooks
- testing
---
### CW20 - 2020-03-31 to 2020-04-02

Idea 7 - CI7-CW20

Adding Behaviour Driven Development to Exploratory Research Notebooks


### **Participants**

* _Jon Massey_

* _Ben Krikler_

* _Anastasis Georgoulas_

* _Matthew Bluteau_

* _Steve Crouch_



---


_Discussion_



*   _Jon: Trying to do SE after the fact - behaviour specs. Way to apply this instead of documentation after the fact? Pitch from SSI fellowship - taking industrial practices to academia_
    *   _Anastasis: Intended behaviour of software not always known beforehand. Unsure what will work, analyses that will be done, etc. Possible to adapt it to this?_
    *   _At some point you transition from exploratory base to doing things properly. Understanding that transition, test from an earlier stage? How to test notebook_
    *   _Also get situations where code developed for ourselves gets used and adopted by others unexpectedly. Perhaps always assume this will happen - e.g. just always do TDD, or something similar. Ways to write test specs at this transitionary time?_
    *   _Steve: capturing requirements during exploratory phase critical for transition to more mature phase of project; “Just in Time Specification”; there is value in “faking” development/design good practices_
*   _Ben: bringing Agile/Lean principles into the process of exploratory research_
    *   _Jon: Cucumber integration with Jupyter notebooks; specify what the behaviour of that notebook should be, and then actually be able to use this to test the behaviour later on_
    *   _Perhaps also have a linter for checking validity of Cucumber/Notebook descriptions_
    *   _MoSCoW - MH - 60%, SH - 20%, CH - 20%. Perhaps something here to fit behaviour back to requirements?_
    *   _Use BDD markups after the fact (e.g. JIT) to describe behaviour (at the point where you wish to go beyond exploratory development)_
    *   _Behave (Python) package: BDD descriptions in code/notebooks - explore this repository and add to it? [https://pypi.org/project/behave/](https://pypi.org/project/behave/)_
*   _Add template to a notebook with a pre-populated structure, e.g. start notebook, starts with that templated structure_


### **Context / Research Domain**

_General Research Software Development, and how to capture the behaviour of software_


### **Problem**

_As sometimes happens in academia, that software you wrote just for yourself or to explore an idea is suddenly useful for others. Often, this means the original software form has to be reimplemented, sometimes quite drastically (e.g. refactoring a Jupyter Notebook, or reimplementing one to standalone Python scripts). What can we do to capture a software's behaviour so it can be tested against if/when it transitions to production, and needs to be refactored/reimplemented?_


### **Solution**

_Develop a way to apply Behaviour-Driven Development in the context of exploratory research software development:_



1. _How has it been applied elsewhere? When and for what reasons has it been successful?_
2. _Given that Jupyter Notebooks are a common tool used for such exploratory software development, determine how we can make best use of existing BDD tools in this environment. For example, integration of Gherkin BDD descriptions throughout a notebook to describe its behaviour_
3. _Develop tool support for BDD within notebooks, e.g. automatic generation of tests based on docstrings that encapsulate BDD in a notebook (using doctest), generation of a skeleton BDD structure within a notebook for filling in behavioural details as the notebook develops_


### **Diagrams / Illustrations**

_You can include one or two diagrams in this section. Please ensure you have the right to use the image(s), and include an attribution if applicable._


###


![Flow of the notebook processing.](../images/cw20-notebook-flow.jpg)




Room 7 FTW!

