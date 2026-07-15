# Determining Spinodal and Binodal Loci and Collective Contribution to Self-Diffusion in Lennard-Jones Argon via MD Simulations

## Problem background
Liquid-state dynamics near the spinodal (limit of thermodynamic stability) and binodal (liquid–vapor coexistence boundary) are not fully understood. The collective contribution to molecular self-diffusion, originating from vortex-like hydrodynamic flow patterns, and its behavior as temperature changes are of fundamental interest. This work investigates whether the fraction of collective self-diffusion D_c/D_s and the spinodal and binodal temperatures can be quantitatively determined for a Lennard-Jones fluid from molecular dynamics simulations.

## Approach
We simulate liquid argon modeled by the Lennard-Jones potential on a fixed isochore (ρ=1.37 g/cm³) at several temperatures ranging from 30 K to 140 K. For each temperature, the system is equilibrated in the NPT ensemble to correct the density, then a long NVE trajectory is produced. The velocity autocorrelation function (VACF) and mean-square displacement (MSD) are computed from the unperturbed trajectories. The self-diffusion coefficient D_s is determined via the Green–Kubo integral of the VACF and via the Einstein relation from the MSD long-time slope. A dimensionless characteristic function built from the MSD and D_s is used to extract the collective fraction D_c/D_s (the method does not require the Maxwell relaxation time). To locate the binodal, we perform perturbation runs: the equilibrated system is briefly exposed to a slightly perturbed twin configuration and then evolved in NVE; the highest temperature at which the unperturbed and perturbed VACFs diverge significantly is identified as the binodal. The spinodal temperature is obtained by plotting D_s(T) and detecting the temperature where the slope changes abruptly.

## Reproduction target
For Lennard-Jones argon on the isochore ρ=1.37 g/cm³, carry out MD simulations at multiple temperatures (30–140 K). Compute D_s from both the VACF and the MSD, and determine the collective fraction D_c/D_s via the characteristic function at 85 K and 100 K. Identify the spinodal temperature T_s from the slope change in D_s(T) and the binodal temperature T_b from the perturbation VACF divergence. Write the required outputs as specified in the workflow steps.

## Assets

- GROMACS (Molecular Dynamics Package): https://www.gromacs.org/
- Lennard-Jones parameters for argon

## Workflow steps

### Step 1: MD simulations for argon on fixed isochore
- Role: process
- Action: Set up equilibrium MD simulations of Lennard-Jones argon on the isochore ρ=1.37 g/cm³ at temperatures T = 30, 60, 80, 100, 120, 130, 140 K. For each temperature, equilibrate via NPT to correct the density, then run a long NVE production trajectory (≥10 ps). Additionally, for each temperature perform a perturbation run: briefly expose the equilibrated system to a slightly perturbed twin configuration and continue the NVE run to detect the binodal. Save atomic velocities and positions.
- Evidence: `/app/outputs/trajectory_counts.json`

### Step 2: Compute VACF, MSD, and self-diffusion coefficient D_s
- Role: process
- Action: For each temperature, post-process the unperturbed trajectories to compute the velocity autocorrelation function (VACF) and the mean-square displacement (MSD). From these derive D_s via integration of the VACF (Green–Kubo) and from the long-time slope of the MSD (Einstein). Store the per-temperature results.
- Evidence: `/app/outputs/ds_intermediate.csv`

### Step 3: Characteristic function and D_c/D_s ratio
- Role: scored (load-bearing)
- Action: From the unperturbed MSD and D_s, construct the dimensionless characteristic function F_MD(x) = (3√π/10) x^{1/2} (1 − Γ̃(x)/x) (using any τ_M that ensures x^{1/2}≫1) and average its plateau over x₁<x<x_u to obtain the ratio D_c/D_s. Report the ratios at temperatures 85 K and 100 K, together with the corresponding D_s values obtained from VACF and MSD, in a CSV file.
- Output file: `/app/outputs/step_01_Ds_values.csv`
- Format: csv
- Contract: temperature (K), D_s_VACF (10^-5 cm^2/s), D_s_MSD (10^-5 cm^2/s), D_c_Ds_char_func (dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Spinodal and binodal temperatures
- Role: scored (load-bearing)
- Action: Plot the self‑diffusion coefficient D_s(T) obtained from the unperturbed runs (prefer the VACF‑based D_s) as a function of temperature for the isochore ρ=1.37 g/cm³. Identify the temperature where the slope changes abruptly (spinodal). Using the perturbation runs, determine the highest temperature at which the unperturbed and perturbed VACFs diverge significantly (binodal). Write the two temperatures to a text file.
- Output file: `/app/outputs/step_02_spinodal_binodal.txt`
- Format: txt
- Contract: Two lines: first line T_s (K), second line T_b (K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_Ds_values.csv`
- `/app/outputs/step_02_spinodal_binodal.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_Ds_values.csv
- path: `/app/outputs/step_01_Ds_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Self-diffusion coefficient D_s (from VACF and MSD) and the collective fraction D_c/D_s obtained from the characteristic function, at 85 K and 100 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `D_s_VACF`, `D_s_MSD`, `D_c_Ds_char_func`
  - `units`:
    - `temperature`: K
    - `D_s_VACF`: 10^-5 cm^2/s
    - `D_s_MSD`: 10^-5 cm^2/s
    - `D_c_Ds_char_func`: dimensionless

### step_02_spinodal_binodal.txt
- path: `/app/outputs/step_02_spinodal_binodal.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Spinodal and binodal temperatures for argon on the isochore ρ=1.37 g/cm³.
- schema:
  - `type`: text
  - `description`: Two lines: first line is spinodal temperature T_s in K, second line is binodal temperature T_b in K.

Notes: The hidden checker will compare the reported scalar values to paper‑reported reference numbers with appropriate relative or absolute tolerances. No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_Ds_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "D_s_VACF",
          "D_s_MSD",
          "D_c_Ds_char_func"
        ],
        "units": {
          "temperature": "K",
          "D_s_VACF": "10^-5 cm^2/s",
          "D_s_MSD": "10^-5 cm^2/s",
          "D_c_Ds_char_func": "dimensionless"
        }
      },
      "description": "Self-diffusion coefficient D_s (from VACF and MSD) and the collective fraction D_c/D_s obtained from the characteristic function, at 85 K and 100 K."
    },
    {
      "file": "step_02_spinodal_binodal.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Two lines: first line is spinodal temperature T_s in K, second line is binodal temperature T_b in K."
      },
      "description": "Spinodal and binodal temperatures for argon on the isochore ρ=1.37 g/cm³."
    }
  ],
  "notes": "The hidden checker will compare the reported scalar values to paper‑reported reference numbers with appropriate relative or absolute tolerances. No gold values are disclosed here."
}
```

## How you are scored
A hidden verifier independently scores each output artifact produced by the workflow. For the numeric outputs (D_c/D_s at 85 K and 100 K, and T_s, T_b) the verifier compares your reported scalars to hidden reference values with appropriate tolerances. The overall reward is a weighted combination of the scores from the individual artifacts. Executing only a data lookup or reporting memorized values is not sufficient; the verifier expects the results to originate from a faithfully executed simulation and analysis pipeline as described in the workflow steps.
