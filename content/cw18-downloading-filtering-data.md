---
title: Downloading and filtering datasets
author:
- Vincent Knight
- Thibault Clérice
- Henry Wilde
- Anastasis Georgoulas
- Adrian-Tudor Panescu
- Aleksandra Nenadic
- Tobias Schlauch
- Louise Brown
- Martin O'Reilly
- Robert Maftei
year: 2018
type: collacorative-ideas
tags:
- data
- download
- filter
---


### Collaborations Workshop 2018 - 2018-03-26

Smarter data sources - Group L - CI8-CW18


### **Reporter**

Aleksandra Nenadic - anenadic@gmail.com


### **Participants**

Vincent Knight

Thibault Clérice

Henry Wilde

Anastasis Georgoulas

Adrian-Tudor Panescu

Aleksandra Nenadic

Tobias Schlauch

Louise Brown

Martin O'Reilly

Robert Maftei


---


### **Context / Research Domain**

_Any project that needs to download and filter datasets._


### **Problem**

_Many current datasets, especially very large ones provide limited ability to query / filter the data on all properties / dimensions it contains and metadata about what the data means (data definitions, units etc) are often held separately from the data itself and not findable from the data source. For example, a dataset of historical weather observations may be a series of files, with one file holding all observation for a given time period. Analysing this data for a single site or region across time requires downloading the entire dataset and processing it locally. The data may also not come with information on the units for various measures or the information required to interpret various categories / codes._


### **Solution**

_Things that would be nice to be able to do with datasets:_

* _Ability to subselect / filter datasets on a full set of properties without having to download the full dataset_
* _Ability to combine / compose / join datasets. For example, if three different studies have classified website articles by language, sentiment and subject matter, it should be possible for a fourth study to select angry articles about Trump from the original datasets based on the classifications of the three other datasets. This should be possible without having to duplicate the data into a separate composite dataset or download it all to do the combination locally._
* _Ability to import datasets in a programming environment in a similar manner to code packages (e.g. see rOpenSci - https://ropensci.org/). Ideally, the structure of the data and some content could be used to easily navigate via auto completion (e.g. see TheGamma - https://thegamma.net/), with context help / tooltips providing metadata / data definition “inline” with the data._
* _Ability to cache data locally and work with specific versions of data._
* _Ability to work programmatically / in an automated fashion with non-open datasets once access has been approved for a user (e.g. ConnectomeDB has user agreements that must be accepted and also allows you to link your account with an Amazon user key. Once you have done both you can access the data programmatically with your key - https://db.humanconnectome.org)._


### 
