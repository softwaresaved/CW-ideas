---
title: "Open Source Covid Analysis of References (OSCAR)"
author:
- Michelle Barker
- Shoaib Suf
- Daniel S Katz
- Carina Haupt
- Callum Rollo
year: 2021
type: collaborative-ideas
tags:
- Covid
---

### CW21 - 2021-03-30

Oscar - CI15-CW21


### **Participants**

* **Michelle Barker**

* **Shoaib Suf**

* **Daniel S Katz**

* **Carina Haupt**

* **Callum Rollo**


---

### Title: Open Source Covid Analysis of References (OSCAR)


### **Context / Research Domain**


Software’s use in the Covid19 pandemic is somewhat hidden but ubiquitous. Understanding the impact of software in the pandemic would give it the credit that software deserves, raise its profile and potentially highlight the software readiness that would help in any future public health emergency.

CZI initially made [77,000 articles on Covid19 available (called CORD-19)](https://www.semanticscholar.org/cord19) for analysis.  In an effort to automate the process of identifying and analyzing the use of software in biomedical research, Alex Wade and Ivana Williams developed a SciBERT-based machine learning model to extract mentions of software. They trained the model on [a dataset collected by James Howison  and colleagues (called SoftCite)](https://github.com/howisonlab/softcite-dataset/), and then ran it on the CORD-19 dataset of articles, resulting in this [dataset of the papers and the software mentioned in each](https://datadryad.org/stash/dataset/doi:10.5061/dryad.vmcvdncs0).


### **Problem**

How to analyse the dataset of the papers that mentioned software, and thus evidence and highlight the importance of research software to funders and policy makers?

A [study was undertaken by Nangia and Katz](https://arxiv.org/abs/1706.06527) on software mentions in a sample of 40 Nature papers could provide ideas, as it found that 80% of papers mentioned software, with an average of 6 distinct pieces of software mentioned per paper. Could similar analysis be undertaken on this much larger database, or are there other fantastic statistics that could be unearthed?


### **Solution**

It would be useful to consider different ways to analyse the dataset, to identify statistics or trends that could illustrate issues such as - the key role software has played in responding to COVID-19 (and lack of recognition of its importance), the issues in citation of research software (and possibly findability and accessibility of the software), methods to identify key software infrastructure.

Some of the questions OSCAR hope to answer are:

*   Is information provided about the software authors to give them credit?
*   How many/which pieces of software are repeatedly mentioned (and could possibly be defined as critical research infrastructure)?
*   How was the software mentioned? (e.g. proper references to the software, in-line in the text, footnote, etc.)
*   How was the software itself referenced (e.g. A GitHub page to a project, a GitHub page to a release, a Zenodo DOI to an archive, a Software Heritage link to a release, etc.)
*   What percentage of all articles mention software? How many pieces of software are mentioned per paper?
*   What was the software used for (e.g. platform, analysis)
*   Subdiscipline analysis - is there some smaller set of the dataset (eg a subdiscipline) where the answers to any of these questions differ to that of the whole dataset, that might illuminate where a community is doing things differently/better?


### **Diagrams / Illustrations**


![alt_text](../images/cw21-cat.jpg)


[Nathan Riley](https://unsplash.com/@nrly?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on[ Unsplash](https://unsplash.com/s/photos/cat-paper?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

END IDEA

---


NOTES BEGIN

Notes from session:

This document should be used to capture the information for a Collaborative Session / Hack Day Idea. (The total amount of text should ideally be between 100-300 words and you can include a diagram or two). The document should be no larger than two pages of A4. Don’t delete the details at the top of the document but you should delete all of this hint text (Arial, italic, grey, size 11) once you no longer need it.

The ideas:

Mentoring toolkit

Standards/systems on formulating knowledge bases or toolkits for capturing and sharing knowledge in a domain (e.g. data management or computational techniques)

CZI machine model [pulling out software mentions in 77,000 covid19 articles](https://chanzuckerberg.com/newsroom/new-dataset-makes-coronavirus-research-open-and-machine-readable/) (dataset [here](https://pages.semanticscholar.org/coronavirus-research)) - similar to other work finding [different software mentions in a set of 40 Nature papers](https://arxiv.org/abs/1706.06527). 4

Small library to extract software datasets out of a GitLab  - filtering (activity, language, etc); help with software analytics - how does it change over time, developers churn, activity levels. Are they FAIR, license, could compare local performance vs Gitlab in the wild or a business. 3

Disability related - tools/experience/awareness raising - accessible check (screen reader, colour checking, etc) - is it possible in a generic way - many proprietary tools, take away some ability and then see if the experience was still useful (differently enabled) 3

Amplifying this morning’s panel discussion message - brainstorm ways to share challenges faced eg blog on this morning’s panel, ask RSE podcasts to interview one of the panelists 1

Disability monitoring system - for new members of staff and link disability offices with schools 1


### Licence

These materials (unless otherwise specified) are available under the Creative Commons Attribution 4.0 Licence. Please see the [human-readable summary](https://creativecommons.org/licenses/by/4.0/) of the CC BY 4.0 and the full [legal text](https://creativecommons.org/licenses/by/4.0/legalcode) for further information. 

