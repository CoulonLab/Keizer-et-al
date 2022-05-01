# Keizer _et al._ – Data, software and documentation

Main repository to access all the data, software and documentation to reproduce the results presented in **[Keizer _et al._['Live-cell micromanipulation of a genomic locus reveals interphase chromatin mechanics'](https://www.biorxiv.org/content/10.1101/2021.04.20.439763v1)]**.

### PROCESSED DATA and ANALYSIS NOTEBOOKS
|||  
| ----------- | :---: |
| <ul><li>**Final cropped, rotated and registered TIFF files**:<br>- **30’-PR** experiments: n = 35 cells<br>- **100”-PR** experiment, including time projections & kymograph<br>- **dt = 0.5”** experiments: n = 3 cells<br>- **no force**: n = 11 cells before manipulation, n = 8 cells after manipulation</li><li>**Trajectory and force time profile** data files for all cells</li><li>Instructions and Fiji/Python scripts to reproduce these files.</li></ul> | <sup>[./**data**/](./data/)</sup> <br><sup><sub>[Zenodo 13](https://zenodo.org/record/)* for large files.</sup></sub> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| **Analysis notebooks** to generate all graphs shown in [Keizer _et al._] | <sup>[./**notebooks**/](./notebooks/)</sup> |
| **Python library for force inference** using different polymer models | <sup>[**rouselib** repository](https://github.com/SGrosse-Holz/rouselib)</sup> |

### RAW DATA and IMAGE ANALYSIS
|||  
| ----------- | :---: |
| **Raw microscopy data**:<ul><li>Experiments performed with the 30’-PR scheme</li><li>Experiment performed with the 100”-PR scheme</li><li>Experiment performed with high frame rate (dt = 0.5”)</li></ul>| <sub> <sup>[Zenodo 1](https://zenodo.org/record/)* (30’-PR),	[Zenodo 2](https://zenodo.org/record/)* (30’-PR),<br> [Zenodo 3](https://zenodo.org/record/)* (30’-PR),	[Zenodo 4](https://zenodo.org/record/)* (30’-PR),<br> [Zenodo 5](https://zenodo.org/record/)* (30’-PR),	[Zenodo 6](https://zenodo.org/record/)* (100”-PR),<br> [Zenodo 7](https://zenodo.org/record/)* (30’-PR),	[Zenodo 8](https://zenodo.org/record/)* (30’-PR),<br> [Zenodo 9](https://zenodo.org/record/)* (dt = 0.5"),	[Zenodo 10](https://zenodo.org/record/)* (30’-PR)</sup></sub>  |
| Concatenated TIFF files and timestamp files for all of the 30’-PR data. | <sub><sup>[Zenodo 11](https://zenodo.org/record/)* (1/2),	[Zenodo 12](https://zenodo.org/record/)* (2/2)</sup></sub>  |
| Python pipeline to generate <ol type="i"><li>concatenated movies for each field of view</li><li>cropped and rotated movies for each cell</li><li>force time profiles for each cell.</li><ol> | <sub>[**ChroMag-pipeline** repository](https://github.com/CoulonLab/chromag-pipeline)</sub> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |

### FORCE CALIBRATIONS and MAGNETIC SIMULATIONS
|||  
| ----------- | :---: |
| **Single-MNPs fluorescence**: raw data, Python/Fiji scripts and instructions | <sup>[./calibrations/**single_MNPs**/](./calibrations/single_MNPs/)</sup> <br><sup><sub>[Zenodo 14](https://zenodo.org/record/)* for large files.</sup></sub> |
| **Force calibration - Method 1**: Gradient of free GFP-ferritin in solution<ul><li>Raw microscopy data (6 pillars)</li><li>Calculated force maps, Fiji scripts and instructions</li></ul> | <sup>[./calibrations/**force_calibr_meth1**/](./calibrations/force_calibr_meth1/)</sup> <br><sup><sub>[Zenodo 15](https://zenodo.org/record/4627062)* for large files.</sup></sub> |
| **Force calibration - Method 2**: Attraction of ferritin-coated beads<ul><li>-	Raw microscopy data (free diffusion and attraction)</li><li>-	Python/Fiji scripts to calculate forces</li></ul> | <sup>[./calibrations/**force_calibr_meth2**/](./calibrations/force_calibr_meth2/)</sup> <br><sup><sub>[Zenodo 16](https://zenodo.org/record/)* for large files.</sup></sub> |
| <ul><li>MagSim, **Python library for magnetic simulations**</li><li>Jupyter notebook for calibrating and generating maps</li></ul> |	<sub>[**MagSim** repository](https://github.com/CoulonLab/MagSim)</sub> |

<sup>* Will be made public upon publication of the study [Keizer _et al._].</sup>


## Authors
Veer I. P. Keizer<sup>1,2,3,\#</sup>, Simon Grosse-Holz<sup>4</sup>, Maxime Woringer<sup>1,2</sup>, Laura Zambon<sup>1,2,3</sup>, Koceila Aizel<sup>2</sup>, Maud Bongaerts<sup>2</sup>, Fanny Delille<sup>5</sup>, Lorena Kolar-Znika<sup>1,2</sup>, Vittore F. Scolari<sup>1,2</sup>, Sebastian Hoffmann<sup>3</sup>, Edward J. Banigan<sup>4</sup>, Leonid A. Mirny<sup>4</sup>, Maxime Dahan<sup>2,§</sup>, Daniele Fachinetti<sup>3,\*</sup>, Antoine Coulon<sup>1,2,\*,¶</sup>

<sup>**1\.** Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR3664, Laboratoire Dynamique du Noyau, 75005 Paris, France. **2.** Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR168, Laboratoire Physico Chimie Curie, 75005 Paris, France. **3.** Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR144, Laboratoire Biologie Cellulaire et Cancer, 75005 Paris, France. **4.** Department of Physics and Institute for Medical Engineering and Science, Massachusetts Institute of Technology, Cambridge, 02139 MA, USA. **5** ESPCI Paris, PSL Research University, Sorbonne Université, CNRS UMR8213, Laboratoire de Physique et d’Étude des Matériaux, 75005 Paris, France. **\#** Present address: National Cancer Institute, NIH, Bethesda, MD, USA. **§** Deceased, **\*** Correspondence: daniele.fachinetti@curie.fr, antoine.coulon@curie.fr (**¶** Lead contact).</sup>

## Publication status
The study [Keizer _et al._](https://www.biorxiv.org/content/10.1101/2021.04.20.439763v1) is currently available as a preprint. It has not yet been published in a journal.

## Reuse policy
As [standard practice in the field](https://www.4dnucleome.org/policies.html), researchers using this public, but as yet unpublished data must contact the specific data producer (antoine.coulon@curie.fr) to discuss possible coordinated publication. Unpublished data are those that have never been described and referenced by a peer-reviewed publication.

In addition to this restriction, all the code, data and documentation in this repository is under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license. The study [Keizer _et al._](https://www.biorxiv.org/content/10.1101/2021.04.20.439763v1) is under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

