# DFT-based AIMD of Zn-Doped Hematite/Water Interface: Hole Defect State Energy and Level Alignment

## Problem background
Hematite (α-Fe2O3) is a promising photoanode material for solar water oxidation, but its practical performance is limited by fast electron–hole recombination and poor charge transport. Introducing hole carriers at the surface, for example by substituting Fe with Zn (p-type doping), has been shown experimentally to lower the overpotential for the oxygen evolution reaction (OER). However, the atomistic nature of the hole states created by Zn doping at the hematite/water interface, and how their energy and localization fluctuate under operating conditions, is not well understood. This task addresses that question by using first-principles density functional theory (DFT) and ab initio molecular dynamics (AIMD) to characterize the electronic structure of a subsurface Zn-doped hematite (0001) slab in contact with liquid water, specifically focusing on the energy of the defect state (DS) within the band gap and its alignment to the electrochemical scale.

## Approach
The computational approach combines AI-based dynamics with hybrid DFT electronic structure analysis. A six-layer hematite slab is doped with a single Zn atom in a subsurface Fe site and placed in contact with an explicit layer of water molecules. Two different DFT exchange–correlation protocols are used to propagate the AIMD at room temperature: (i) the PBE functional with Grimme's D3 dispersion correction, and (ii) the same functional augmented with a Hubbard U correction on Fe 3d states. Along the trajectories, snapshots are taken at regular intervals, and the electronic structure of each snapshot is recomputed with the hybrid PBE0 functional (with 12% exact exchange) to obtain accurate Kohn–Sham eigenvalues. From these single-point calculations, the energy of the unoccupied defect state (the lowest unoccupied eigenvalue in the α-spin channel) is extracted relative to the instantaneous valence band maximum (VBM). The mean and standard deviation of the defect state energy is then computed separately over the two trajectory segments. Finally, the electrochemical level alignment is performed: the electrostatic potential of the slab is averaged in the surface-normal direction and used to align the VBM to the reversible hydrogen electrode (RHE) scale, after which the defect state level is referenced accordingly. This provides a statistical picture of the hole state's energy distribution under dynamic aqueous conditions and its relation to the thermodynamic potential for water oxidation.

## Reproduction target
Your goal is to produce a JSON file, ds_energies.json, that contains the following data derived from the AIMD simulations and subsequent hybrid DFT analysis: (1) For each trajectory segment (first ~35.7 ps with PBE+D3, then ~14.3 ps with PBE+U+D3), a time_series list of records with time, the defect state energy relative to the VBM, and the VBM–CBM gap; (2) the duration_ps, the mean and standard deviation of the defect state energy (ds_energy_mean_eV and ds_energy_std_eV) for each segment; (3) an alignment object that reports the VBM level on the RHE scale (vbm_vs_rhe_V) and the resulting defect state level (ds_level_vs_rhe_V). The defect state is identified as the lowest unoccupied eigenvalue in the α-spin channel of the PBE0(0.12) single-point calculation on the rehydrogenated slab. The alignment must be performed using the plane-averaged electrostatic potential and a literature value for the point of zero charge pH of hematite (~8.5). The completed JSON file must be placed at /app/outputs/ds_energies.json.

## Assets

- CP2K: https://www.cp2k.org

## Workflow steps

### Step 1: Construct Zn-doped hematite (0001) slab with water interface
- Role: process
- Action: Build a six-layer hematite (0001) slab with stoichiometry Fe48O84H24, substitute one Fe in the β-spin subsurface layer with Zn, fully hydroxylate both surfaces, then remove two H atoms from the surface proximal to Zn to approximate catalytic surface composition. Add 56 water molecules to form the interface, and pre-equilibrate with a short AIMD run (PBE0(0.12) level, ~2.5 ps) as described in the paper's Methods.
- Evidence: `/app/outputs/interface.xyz`

### Step 2: Run AIMD production simulation
- Role: process
- Action: Propagate AIMD of the Zn-doped hematite/water interface using CP2K in the NVT ensemble at 300 K with a Nosé–Hoover thermostat and a 0.5 fs time step. Run the first ~35.7 ps using the PBE+D3 functional, then switch to PBE+U+D3 (U=4.3 eV on Fe 3d) for an additional ~14.3 ps. Save atomic coordinates and velocities every 200 fs for later analysis.
- Evidence: `/app/outputs/aimd_trajectory.xyz`

### Step 3: Extract defect state energies and perform level alignment
- Role: scored (load-bearing)
- Action: For each saved snapshot along the trajectory, rehydrogenate the slab and run a PBE0(0.12) single-point calculation. Identify the unoccupied defect state (DS) in the α-channel as the lowest unoccupied eigenvalue; record its energy relative to the instantaneous VBM and the VBM–CBM gap. Compute the average and standard deviation of the DS energy for the PBE+D3 and PBE+U+D3 trajectory segments. Align the VBM of the interface to the RHE scale using the plane-averaged potential and literature pH_PZC, and compute the average DS level on the RHE scale. Write the compiled results to ds_energies.json.
- Output file: `/app/outputs/ds_energies.json`
- Format: json
- Contract: Defect state energy statistics from AIMD snapshot analysis and electrochemical level alignment.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ds_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ds_energies.json
- path: `/app/outputs/ds_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: AIMD-derived defect state energy statistics and aligned level on the RHE scale.
- schema:
  - `type`: object
  - `required`:
    - `trajectory_segments`: object
    - `alignment`: object
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The checker will recompute the mean and standard deviation of ds_vs_vbm_eV from the time_series for each trajectory segment and compare them to a hidden reference within tolerances. The alignment values vbm_vs_rhe_V and ds_level_vs_rhe_V will also be compared. The DS level relative to the O2/H2O redox potential will be audited for consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ds_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "trajectory_segments": "object",
          "alignment": "object"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "AIMD-derived defect state energy statistics and aligned level on the RHE scale."
    }
  ],
  "notes": "The checker will recompute the mean and standard deviation of ds_vs_vbm_eV from the time_series for each trajectory segment and compare them to a hidden reference within tolerances. The alignment values vbm_vs_rhe_V and ds_level_vs_rhe_V will also be compared. The DS level relative to the O2/H2O redox potential will be audited for consistency."
}
```

## How you are scored
A hidden verifier will read your ds_energies.json and score the submission. The verifier will independently recompute the mean and standard deviation of the defect-state energies from your reported time-series arrays and compare these statistics against reference benchmarks that represent the expected results from the protocol (taken from the published literature, with appropriate tolerances). It will also compare your aligned VBM and defect-state levels on the RHE scale to reference values. The final score is a weighted combination of these checks, with greater emphasis on the accuracy of the mean defect-state energies than on the alignment, while also checking overall self-consistency. The tolerances are designed to reward accurate reproduction of the key quantities and penalize significant deviations.
