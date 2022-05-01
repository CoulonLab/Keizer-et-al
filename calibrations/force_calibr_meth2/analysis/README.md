# Analysis of bead diffusion and attracrtion

### Analysis of bead diffusion

Outputs of this analysis is in [`./1-bead_diffusion/`](./1-bead_diffusion/).

The free diffusion of 5 µm polystyrene beads was estimated from 3 movies:
- `20211208_micr2_5um-beads-noAb_gbdishCoverglass_forDiffusion_translight_3`
- `20211208_micr2_5um-beads-noAb_gbdishCoverglass_forDiffusion_diluted_translight_2`
- `20211208_micr2_5um-beads-noAb_gbdishCoverglass_forDiffusion_diluted_translight_3`

Using Fiji,
- each movie was scaled down by a factor 0.2x (see files ending with `_scale0.2.tif`)
- a Gaussian blur was applied (radius of 1 px) and a value of `1000` was subtracted to pixel values, making all features but the sedimenting particles become `0` (see files ending with `_scale0.2_blur1px_subtr1000.tif`). This is to ensure that the tracked beads are not in contact with the coverglass, which could impair their diffusion.

The sedimenting beads were tracked using our [`trackUsingMouse`](../../../data/3-code_and_protocol/trackUsingMouse) software (repectively 9,11 and 10 beads in the 3 analyzed movies).

Using Jupyter notebook [`MSD_beads.ipynb`](./1-bead_diffusion/MSD_beads.ipynb),
- the ballistic motion of all beads due to small convection effects in each movie was subtracted,
- mean square displacement (MSD) curves were calculated for each bead, averaged together and fit to a Brownian diffusion model.


### Analysis of bead attraction

Outputs of this analysis is in [`./2-bead_attraction/`](./2-bead_attraction/).

The attraction of ferritin-coated 5 µm polystyrene beads was measured from all 13 movies in [`../data/`](../data/). These movies (ending with `_sel.tif`) only contain the frames between the moment the magnet is placed and the moment the beads have reached the micropillar.

Using the Fiji script [`locate_maxima.ijm`](./2-bead_attraction/locate_maxima.ijm), for each movie, GFP images of the beads are blurred and local maxima are located. A file ending with `_maxima.tif` is created and used to generated trajectory files using our [`trackUsingMouse`](../../../data/3-code_and_protocol/trackUsingMouse) software.

Using Jupyter notebook [`bead_attraction_vs_force.ipynb`](./2-bead_attraction/bead_attraction_vs_force.ipynb),
- trajectories of all 20 beads are aligned with respect to the location of the micropillars,
- the instant speed of each bead is calculated and converted into a force using the diffusion coefficient calculated above
- the calculated force is compared to the predicted force (using the [simulated force map](https://github.com/CoulonLab/MagSim) that was calibrated using the data in [`calibrations/force_calibr_meth1/`](../../force_calibr_meth1/)).



