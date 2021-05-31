# DataSet

In order to evaluation **SSPT**, a repository of test scenarios is needed. Below, we describe the content of the [DataSet](https://github.com/ssbse2021/SSPT/blob/main/scenarios/DataSet.csv) and the process of obtaining it. 

## Test scenarios. 

 As shown in the following figure, a test scenario for ADSs, in our experiment, is defined with **19** [properties](https://github.com/ssbse2021/SSPT/blob/main/scenarios/properties%20used%20to%20specify%20a%20scenario.png). **Five** of them are about the ego vehicle (e.g., acceleration and speed) and the other **fourteen** properties describe the environment (e.g., pedestrians, weather). 

<div align=center><img src="https://github.com/ssbse2021/SSPT/blob/main/scenarios/properties%20used%20to%20specify%20a%20scenario.png" width = "500" /></div>

To produce the dataset, we employed the Baidu Apollo Open Platform 5.0 as the ADS under test and integrated it with the LGSVL simulator. We chose the San Francisco map as for scenarios collecting because it has a large number of different types of roads such as one-way roads, two-way roads and cross walks.

## Collecting  Data. 

The test scenarios in the dataset were automatically produced and collected when we were testing Apollo 5.0 with a machine learning based environment configuration generation strategy. We let the framework execute for nearly 1000 times on four different roads of the San Francisco map loaded in LGSVL; meanwhile we let the ADS drive from a start point to the destination. In the end, we managed to collect the dataset of 90K test scenarios, each of which is characterized with the 19 properties. 

## Processing Data.

First, we removed duplicated test scenarios from the original dataset. Without doing so would cause unnecessary effort for prioritization, though one of our optimization objective is to maximize the diversity of a test suite (i.e., **TSDIV**). In the end, we obtained a dataset containing 60K scenarios. To save time on calculating diversity during the execution of the MOSAs, we further calculated all the pair-wise comparison diversity values of the test scenarios in advance, i.e., **SDIV**.

## Labelling test scenarios with their attributes. 

After data collecting and pre-processing, for each test scenario, we calculated four values for each of the four attributes. The labeled dataset was then fed to **SSPT** for selecting and prioritizing scenarios in our experiment.
