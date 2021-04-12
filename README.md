# "_In vivo_ manipulation of a genomic locus reveals the mechanical properties of interphase chromatin" Keizer et al.

Data, software and documentation to reproduce the results from Keizer et al.

## Publication status
The study Keizer et al. will be uploaded to a preprint server shortly. It has not yet been peer reviewed and is not yet published in a journal.

## Data re-use policy
As [standard practice in the field](https://www.4dnucleome.org/policies.html), researchers using this public, but as yet unpublished data must contact the specific data producer (antoine.coulon@curie.fr) to discuss possible coordinated publication. Unpublished data are those that have never been described and referenced by a peer-reviewed publication.

## Authors
Veer I. P. Keizer<sup>1,2,3,#</sup>, Simon Grosse-Holz<sup>4</sup>, Maxime Woringer<sup>1,2</sup>, Laura Zambon<sup>1,2,3</sup>, Koceila Aizel<sup>2</sup>, Maud Bongaerts<sup>2</sup>, Lorena Kolar-Znika<sup>1,2</sup>, Vittore F. Scolari<sup>1,2</sup>, Sebastian Hoffmann<sup>3</sup>, Edward J. Banigan<sup>4</sup>, Leonid A. Mirny<sup>4</sup>, Maxime Dahan<sup>2,§</sup>, Daniele Fachinetti<sup>3,*</sup>, Antoine Coulon<sup>1,2,*,¶</sup>

<span font-size:4em;">
1.	Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR3664, Laboratoire Dynamique du Noyau, 75005 Paris, France
2.	Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR168, Laboratoire Physico Chimie Curie, 75005 Paris, France
3.	Institut Curie, PSL Research University, Sorbonne Université, CNRS UMR144, Laboratoire Biologie Cellulaire et Cancer, 75005 Paris, France
4.	Department of Physics and Institute for Medical Engineering and Science, Massachusetts Institute of Technology, Cambridge, 02139 MA, USA
\# Present address: National Cancer Institute, NIH, Bethesda, MD, USA
§	Deceased
\*	Correspondence: daniele.fachinetti@curie.fr, antoine.coulon@curie.fr
¶	Lead contact.
</span>

## Content of this repository

|Description|Local folder|External link|
|---|---|---|
|Final registered and rotated TIFF files|||
|- All 8 cells analyzed for the 30’-PR experiment| | |
|- 100”-PR experiment, with time projections & kymograph (Movie S2).| | |
| --- | --- | --- |
|-	Data files with trajectories and force time profiles for all 9 analyzed cells.| | |
|-	Fiji/ImageJ/Python scripts and instructions for generating these TIFF files and trajectory data files.| | |
|---|---|---|


## Outline of this repository
We created one folder per type of data generated. We then included subfolders or links to the movies (uploaded on the [Zenodo](https://zenodo.org/) platform) corresponding to successive steps of analysis.

### List of the folders

|Folder|Name|Description|
|---|---|---|
|data|**Raw data & code to process it**|Experiments in which the magnet was added/removed, data and code to process it.|
|forceCalibration|**Force field calibration**|Experiments and simulations to estimate the force field.|
|singleMNPs|**Single MNP intensity**|Experiments and code to estimate the intensity of a single MNP, and compute the number of MNP at the locus|
