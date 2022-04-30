2022/01/02 AC

Analysis for estimating single MNP fluorescence intensity
=========================================================

Source data: `data/Fanny/20211201`

---------
"Standard" imaging conditions of our usual experiments are
- gain=30
- exposure=100ms
- SpectraX-Cyan=5%

From previous measurements, we confirmed that fluo intensity scales linearly with exposure time and with gain. For the SpectraX illumination intensity, we determined with a powermeter that 
- SpectraX-Cyan=4%   => power=15.87mW => ratio=0.875
- SpectraX-Cyan=5%   => power=18.14mW => ratio=1 (reference)
- SpectraX-Cyan=100% => power=133.3mW => ratio=7.35

To convert a measured fluo intensity into the "standard" imaging conditions:
`fluo_std = fluo_nonStd / SpectraX-Cyan-ratio * 100/exposure * 30/gain`

--------------
In data/Fanny/20211201, the data data considered here, taken with the SpectraX are
gain=30
exposure=100ms
SpectraX-Cyan=100%

==> `fluo_std = fluo_20211201 * 0.13605` <==

--------------
Analyzed datasets:
- Position 'Pos9' => immobile MNPs adhered onto the coverglass (i.e. outside of the cell).
- Position 'Pos10' => Cell with a large portion of the cytoplasm making a thing layer, where MNPs can be well visualized

--------------
Strategy for analysis of 'Pos9':
- only the first 10 images taken at high illumination were used (i.e. acquisition `20211201_single-MNP_needle3_Pos9_2_exp100ms_spectraCyan100_MNPonGlass_1`)
- Imagej script `Pos9/offset_normalize_avg.ijm` was used to correct for minor bleaching and to average all 10 images
- A mask was drawn by hand to select the area of interest
- Python notebook `Pos9/analyse_spot_intensities_Pos9.ipynb` was used to identify well-isolated spots within the mask, and calculate their mean and median intensities.

--------------
Strategy for analysis of 'Pos10':
- only the first 50 images taken at high illumination were used (first 50 frames of `20211201_single-MNP_needle3_Pos10_2_exp100ms_spectraCyan100_1`)
- Imagej script `Pos10/offset_normalize.ijm` was used to correct for minor bleaching
- A mask was drawn by hand to select the area of interest
- Python notebook `Pos10/analyse_spot_intensities_Pos10.ipynb` was used to identify well-isolated spots within the mask, and calculate their mean and median intensities.
