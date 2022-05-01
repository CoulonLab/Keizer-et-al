# Keizer _et al._ – Data, software and documentation

Main repository to access all the data, software and documentation to reproduce the results presented in **[Keizer _et al._['Live-cell micromanipulation of a genomic locus reveals interphase chromatin mechanics'](https://www.biorxiv.org/content/10.1101/2021.04.20.439763v1)]**.


| Description | Location |
| ----------- | :---: |
| **Raw microscopy data**:<ul><li>Experiments performed with the 30’-PR scheme</li><li>Experiment performed with the 100”-PR scheme</li><li>Experiment performed with high frame rate (dt = 0.5”)</li></ul>| <sub> <sup>[Zenodo 1](https://zenodo.org/record/)* (30’-PR),	[Zenodo 2](https://zenodo.org/record/)* (30’-PR),<br> [Zenodo 3](https://zenodo.org/record/)* (30’-PR),	[Zenodo 4](https://zenodo.org/record/)* (30’-PR),<br> [Zenodo 5](https://zenodo.org/record/)* (30’-PR),	[Zenodo 6](https://zenodo.org/record/)* (100”-PR),<br> [Zenodo 7](https://zenodo.org/record/)* (30’-PR),	[Zenodo 8](https://zenodo.org/record/)* (30’-PR),<br> [Zenodo 9](https://zenodo.org/record/)* (dt = 0.5"),	[Zenodo 10](https://zenodo.org/record/)* (30’-PR)</sup></sub>  |
| Concatenated TIFFs and timestamp files for all of the 30’-PR data | <sub><sup>[Zenodo 11](https://zenodo.org/record/)* (1/2),	[Zenodo 12](https://zenodo.org/record/)* (2/2)</sup></sub>  |
| Python pipeline to generate (i) concatenated movies, (ii) cropped and<br> rotated movies for each cell, and (iii) force time profiles for each cell. | <sub>[**ChroMag** github repository](https://github.com/CoulonLab/chromag-pipeline)</sub> |
| <ul><li>**Final registered and rotated TIFF files**:<br>- **30’-PR** experiments: n = 35 cells<br>- **100”-PR** experiment, including time projections & kymograph<br>- **dt = 0.5”** experiments: n = 3 cells<br>- **no force**: n = 11 and 8 cells before and after manipulation</li><li>**Data files with trajectories and force time profiles** for all cells</li><li>Instructions and Fiji/Python scripts to reproduce these files.</li></ul> | <sup><sub>[Zenodo 13](https://zenodo.org/record/)* for large files.</sup></sub> |


<sup>* Will be made public upon publication of the study [Keizer et al.].</sup>


## Content of this repository

|Description|Location on GitHub|External link|
|---|:---:|:---:|
|**Final registered and rotated TIFF files**:<ul><li>All 8 cells analyzed for the 30’-PR experiment</li><li>100”-PR experiment, with time projections & kymograph</li></ul>|  | [Zenodo](https://zenodo.org/record/4674438) |
|Data files with **trajectories and forces** for all analyzed cells| [`./data/2-trajectory_files/`](./data/2-trajectory_files/) | \" |
|**Fiji/Python scripts** for generating these files| [`./data/3-code_and_protocol/`](./data/3-code_and_protocol/) | \" |
| ––––––––––––––––––––––––––––––––––––––––––––––––––––––––– | ––––––––––––––––––––––––––––– | ––––––– |
|Raw spinning-disk microscopy **data for force calibration**|  | [Zenodo](https://zenodo.org/record/4627062) |
|Force maps calculated on this data|  | \" |
|**Fiji scripts** for generating these force maps| [`./forcecalibration/scripts/`](./forcecalibration/scripts/) | \" |
| ––––––––––––––––––––––––––––––––––––––––––––––––––––––––– | ––––––––––––––––––––––––––––– | ––––––– |
|Raw microscopy **data for single-MNP intensity calibration**|  | [Zenodo](https://zenodo.org/record/4674531) |
|**Fiji scripts** for generating average single-MNP image| [`./singleMNPs/analysis/`](./singleMNPs/analysis/) | \" |
| ––––––––––––––––––––––––––––––––––––––––––––––––––––––––– | ––––––––––––––––––––––––––––– | ––––––– |
|**Python pipeline for concatenating** raw microscopy images| [`CoulonLab/chromag-pipeline`](https://github.com/CoulonLab/chromag-pipeline) | [Zenodo](https://zenodo.org/record/4674417) |
|**Magnetic simulations**:<ul><li>MagSim Python library</li><li>Jupyter notebook for calibrating and generating maps</li></ul>| [`CoulonLab/MagSim`](https://github.com/CoulonLab/MagSim) | [Zenodo](https://zenodo.org/record/4672595) |
|**Python library for force inference** using polymer models| [`SGrosse-Holz/rouselib`](https://github.com/SGrosse-Holz/rouselib) | [Zenodo](https://zenodo.org/record/4674399) |

## Authors
Veer I. P. Keizer<sup>1,2,3,\#</sup>, Simon Grosse-Holz<sup>4</sup>, Maxime Woringer<sup>1,2</sup>, Laura Zambon<sup>1,2,3</sup>, Koceila Aizel<sup>2</sup>, Maud Bongaerts<sup>2</sup>, Fanny Delille<sup>5</sup>, Lorena Kolar-Znika<sup>1,2</sup>, Vittore F. Scolari<sup>1,2</sup>, Sebastian Hoffmann<sup>3</sup>, Edward J. Banigan<sup>4</sup>, Leonid A. Mirny<sup>4</sup>, Maxime Dahan<sup>2,§</sup>, Daniele Fachinetti<sup>3,\*</sup>, Antoine Coulon<sup>1,2,\*,¶</sup>

<sup>**1\.** Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR3664, Laboratoire Dynamique du Noyau, 75005 Paris, France. **2.** Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR168, Laboratoire Physico Chimie Curie, 75005 Paris, France. **3.** Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR144, Laboratoire Biologie Cellulaire et Cancer, 75005 Paris, France. **4.** Department of Physics and Institute for Medical Engineering and Science, Massachusetts Institute of Technology, Cambridge, 02139 MA, USA. **5** ESPCI Paris, PSL Research University, Sorbonne Université, CNRS UMR8213, Laboratoire de Physique et d’Étude des Matériaux, 75005 Paris, France. **\#** Present address: National Cancer Institute, NIH, Bethesda, MD, USA. **§** Deceased, **\*** Correspondence: daniele.fachinetti@curie.fr, antoine.coulon@curie.fr (**¶** Lead contact).</sup>

## Publication status
The study [Keizer _et al._](https://www.biorxiv.org/content/10.1101/2021.04.20.439763v1) is currently available as a preprint. It has not yet been published in a journal.

## Reuse policy
As [standard practice in the field](https://www.4dnucleome.org/policies.html), researchers using this public, but as yet unpublished data must contact the specific data producer (antoine.coulon@curie.fr) to discuss possible coordinated publication. Unpublished data are those that have never been described and referenced by a peer-reviewed publication.

In addion to this restriction, all the code, data and documentation in this repository is under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license. The study [Keizer _et al._](https://www.biorxiv.org/content/10.1101/2021.04.20.439763v1) is under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

