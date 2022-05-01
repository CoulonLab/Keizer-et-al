# Generation of TIFF and trajectory files for each analyzed cell

Description of how the files in [`../1-TIFF_files/`](../1-TIFF_files/) and [`../2-trajectory_files/`](../2-trajectory_files/) were generated.

### 30'-PR scheme

  - **Manual analysis**:<br>The following files (ending with `_`) were generated and analyzed as described in `ChroMag_manual_analysis_protocol_v1.2.xlsx`

<sup>`20190410_Pos20_cell0_.tif`, `20190415_Pos1_cell0_.tif`, `20191217_Pos15_cell0_.tif`, `20191217_Pos22_cell3_.tif`, `20191223_Pos0_cell0_.tif`, `20191223_Pos11_cell0_.tif`, `20191223_Pos2_cell0_.tif`, `20200221_Pos4_cell0_.tif`</sup>

- **Pipeline-based analysis**:<br> The other files (listed below) were generated as follows:
  - The **[ChroMag pipeline](https://github.com/CoulonLab/chromag-pipeline)** was used to produce, for each cell (equiv. of manual protocol up to step 6)
    - a cropped and rotated TIFF file (`fine-correction` output folder)
    - a force time profile CSV file (`exports` output folder).
  - Steps 7 to 8 of the manual protocol were performed (refinement of cell motion correction and locus tracking).
  - Force time profiles were rescaled by a manual estimation of the force at t=0, since the number of MNPs at the locus is better estimated manually than by the pipeline (see number used in `calc_MNPs_and_inital_force.xlsx`).
  - Trajectory and force time profile files were merged into a single `.txt` file.

<sub>`20191217_Pos22_cell0.tif`, `20191217_Pos25_cell0.tif`, `20191223_Pos10_cell0.tif`, `20191223_Pos11_cell1.tif`, `20200221_Pos5_cell0.tif`, `20210719_Pos2_cell0.tif`, `20210719_Pos3_cell1.tif`, `20210719_Pos6_cell0.tif`, `20210721_Pos4_cell0.tif`, `20210721_Pos5_cell1.tif`, `20210721_Pos6_cell1.tif`, `20210721_Pos6_cell2.tif`, `20210721_Pos7_cell0.tif`, `20210721_Pos7_cell2.tif`, `20210721_Pos9_cell0.tif`, `20210723_Pos0_cell0.tif`, `20210723_Pos0_cell2.tif`, `20210723_Pos0_cell3.tif`, `20210723_Pos0_cell4.tif`, `20210723_Pos1_cell0.tif`, `20210723_Pos1_cell2.tif`, `20210723_Pos3_cell0.tif`, `20210723_Pos3_cell1.tif`, `20210723_Pos3_cell2.tif`, `20210723_Pos4_cell0.tif`, `20210723_Pos4_cell1.tif`, `20210723_Pos8_cell0.tif`</sup>

### 100"-PR scheme

- The 100"-PR movie was analyzed in described in `ChroMag_manual_analysis_protocol_v1.2.xlsx`, except that
  1. all the steps were performed in 2D, since the source data is a single z-plane timelapse,
  2. `sd1=2.5` was used in `1_add-bpass-channels.ijm` to reduce further imaging noise,
  3. an extra channel with a Gaussian at the center of mass of the locus was added to locate it precisely even when out of focus.

### dt=0.5s scheme

- Movies were analyzed as for the 100"-PR scheme, except that
  1. force time profiles were not calcuated (use of a different filter set impaired proper estimation of MNP number),
  2. cell motion was not corrected (minor over the probed timescale),
  3. mechanical drifts upon magned placement/removal were corrected post-tracking, by taking the loci that were > 30 µm away from the micropillar as a reference.

### noForce scheme (locus mobility before/after manipulation)

- Movies were analyzed as for the 100"-PR scheme, skipping steps that involve forces (rotation and force time profile calculation).

