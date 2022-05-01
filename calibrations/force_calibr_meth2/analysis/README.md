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
