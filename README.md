# Public Data for Peer Review of SPECTRE

> To facilitate reviewing our proposed approach, reviewers please refer to the corresponding data in this repository:
> 
> **[experiment](https://github.com/ssbse2021/SPECTRE/tree/main/experiment)**: all raw data and analysis results for the experiment;<br/> 
> **[scenarios](https://github.com/ssbse2021/SPECTRE/tree/main/scenarios)**: dataset and scenario properties description in our experiment.
# SPECTRE Overview
As shown in the figure, SPECTRE relies on test scenario execution results from a previous version of an ADS to prioritize test scenarios that are executed on the newer version of the ADS.
<div align=center><img src="https://github.com/ssbse2021/SPECTRE/blob/main/figures/SPECTRE.png" width = "500" /></div>

In SPECTRE, each scenario is characterized with a set of properties of the ego vehicle with the ADS under test deployed (e.g., acceleration, speed) and its environment (e.g., weather, number of obstacles).

The simulation of each test scenario leads to output four key values (**Execution Results** in Overview Figure): (1) whether a collision occurred with the scenario; (2) collision probability associated with the scenario, (3) the extent of demand on the ADS put by the scenario, and (4) diversity of the scenario as compared to the others. Based on these attributes, we define four optimization objectives.

More details can be seen in other parts of this repository.
