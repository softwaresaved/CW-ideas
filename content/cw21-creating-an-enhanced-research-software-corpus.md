---
title: "Enabling analysis of research software: Creating an enhanced research software corpus"
author:
- Neil Chue Hong
- Stephan Druskat
year: 2021
type: hack day
tags:
- data-analysis
- research
---

### CW21 Hack Day - 2021-03-31 to 2021-04-01

Batey-1941 - HP2-CW21

### **Hack Day idea proposers**

Neil Chue Hong and Stephan Druskat


---


### **Idea name (provisional)**


Enabling analysis of research software: Creating an enhanced research software corpus


### **Context and/or research domain**

Research on research software (cross-domain)


### **Problem**

Until very recently, a key challenge in trying to understand the research software landscape was that we didn’t know how to find research software - there was no single, comprehensive “research software directory” or curated lists of commonly used research software, though there are discipline-specific catalogues and lists (e.g. on Wikipedia), an increasing number of entries on Wikidata (e.g. for [SQLite](https://www.wikidata.org/wiki/Q319417)), and recent initiatives such as the [NLeSC Research Software Directory](https://www.research-software.nl/) and the [Research Software Encyclopedia](https://rseng.github.io/software/). 

Many approaches took publications as a starting point, often manually identifying software that was mentioned in the publication. Domain registries such as swMath for mathematical software and ASCL.net for astrophysics software which accept author-led suggestions also use these techniques to identify possible candidates for inclusion. Other approaches relied on automatically mining code repositories looking for key markers, such as citation files or DOIs.

This year, two datasets have been released which have gone further to produce a “gold standard” corpus that can be used for other research. The SoftCite project is a human curated list of 4,093 software mentions in life sciences and social sciences, as a TEI/XML file: [https://github.com/howisonlab/softcite-dataset](https://github.com/howisonlab/softcite-dataset). This, in turn, was used by a team at CZI to train a machine learning model that has been used to identify software references in COVID-19 research papers, collectively CORD-19, which has been published as a raw dataset: [https://doi.org/10.5061/dryad.vmcvdncs0](https://doi.org/10.5061/dryad.vmcvdncs0) 

We would like to make this data more useful for those wanting to undertake research in this area.


### **Solution**


Potential ways of improving this include:

*   Analysing and cleaning the CORD-19 software mentions to create a canonical list of software along with common aliases (e.g. MS Excel, Excel, Microsoft Excel should all be related)
*   Annotating the datasets to provide additional useful metadata such as DOIs, URLs to code repositories where they exist, release dates
*   Creating processes and tools that assist with the above

This could then be used to provide some basic metrics around the research software landscape e.g.

*   What is the most popular license for research software? Has this changed through time? 
*   Is the most popular software updated more often?
*   How many people contribute code to research software on average?
*   Distribution of usage, contributions, updates → guidance for funding, sustainability of RS
*   Does the set of contributors to research software shift, which could be a marker for reuse?
*   How many software projects provide citation information?
    *   possible look into citation network, contributor network, dependency network (and/or overlap between these)

It could also be used to demonstrate things that we could do with such a corpus

*   Demonstrate the state of FAIRness of software, and track the development of FAIRness
*   Use it for testing and benchmarking software engineering methods, e.g., automated program repair, test generation, etc.

And, of course, the big one:

*   What software is most important to COVID-19 research?

As suggested by the [OSCAR collaborative ideas group](https://docs.google.com/document/d/1o2ax52Lxk0DLCkGiocqvMai0ZLfbQP0Rs0fmUd381ks/edit), there are many things that could be done to analyse the dataset, to identify statistics or trends that could illustrate issues. These include the key role software has played in responding to COVID-19 (and lack of recognition of its importance), the issues in citation of research software (and possibly findability and accessibility of the software), methods to identify key software infrastructure.

Some of the questions we could hope to answer are:

*   Is information provided about the software authors to give them credit?
*   How many/which pieces of software are repeatedly mentioned (and could possibly be defined as critical research infrastructure)?
*   How was the software mentioned? (e.g. proper references to the software, in-line in the text, footnote, etc.)
*   How was the software itself referenced (e.g. A GitHub page to a project, a GitHub page to a release, a Zenodo DOI to an archive, a Software Heritage link to a release, etc.)
*   What percentage of all articles mention software? How many pieces of software are mentioned per paper?
*   What was the software used for (e.g. platform, analysis)
*   Subdiscipline analysis - is there some smaller set of the dataset (eg a subdiscipline) where the answers to any of these questions differ to that of the whole dataset, that might illuminate where a community is doing things differently/better?


### **Diagrams / illustrations**


**_What do we want to see in a data set from different perspectives?_**

**_What do we want to answer regarding the prevalence of software and what metadata would capture it? _**
