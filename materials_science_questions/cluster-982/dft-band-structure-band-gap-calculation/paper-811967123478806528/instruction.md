# Band Gap and Oxygen Vacancy Formation Energy Trends in A-site Substituted Lead Zirconate Titanate

## Problem background
Lead zirconate titanate (PZT) is a ferroelectric perovskite widely used in actuators, sensors, and nonvolatile memory. Oxygen vacancies are known to degrade device performance through a fatigue effect. Doping the A‑site with trivalent ions from group IIIA (Sc, Y, La) is one strategy to mitigate fatigue and tune the electronic structure, but the systematic variation of electronic and optical properties with dopant species is not fully characterized. This task reproduces first‑principles density functional theory (DFT) calculations to quantify the energy band gap, optical band gap, Ti‑O‑Ti bond angle, and oxygen vacancy formation energy for La‑, Y‑, and Sc‑substituted PZT (Zr/Ti=25/75) supercells. By computing these properties, you will reveal the systematic trend that results from doping the PZT A‑site with different Group IIIA cations.

## Approach
The workflow uses periodic DFT calculations with a plane‑wave basis set and pseudopotentials, implemented with the open‑source Quantum ESPRESSO code and the SSSP pseudopotential library. 

First, 2×2×4 supercells of Pb(Zr₀.₂₅Ti₀.₇₅)O₃ are built with lattice constants a=b=7.892 Å, c/a=2.094. For each dopant (La, Y, Sc), the charge‑neutral substitution is modelled by replacing the central Pb atom with a vacancy and two other Pb atoms with the trivalent substituent. Geometry optimisation of each supercell is performed at the GGA‑PBE level, relaxing all atomic positions without symmetry constraints. 

The relaxed structures are then used to compute the electronic structure and optical properties at the meta‑GGA level: the band structure, density of states, and the imaginary part of the dielectric function are obtained. From these, the Kohn‑Sham band gap (VBM–CBM) and the optical absorption spectrum are extracted; the optical band gap is determined via Tauc analysis. Separately, the Ti–O–Ti bond angle is measured from the optimised geometry.

Finally, the total energy of an isolated O₂ molecule is calculated with GGA‑PBE to define the oxygen chemical potential under oxygen‑rich conditions. Defect supercells with one neutral oxygen vacancy are created for each doped system, and their total energies are computed. The formation energy of the oxygen vacancy is then evaluated as E_f = E_defect − E_perfect + μ_O for each dopant.

## Reproduction target
For the three doped systems (La‑, Y‑, and Sc‑substituted PZT, with Zr/Ti = 25/75), compute and report the following quantities:

- The Kohn‑Sham energy band gap (VBM–CBM) and the optical band gap obtained from Tauc analysis of the calculated absorption spectrum.
- The average Ti–O–Ti bond angle in the relaxed supercell.
- The neutral oxygen vacancy formation energy under oxygen‑rich conditions, using the chemical potential determined from the isolated O₂ molecule.

Write your results to the three output CSV files specified below. The target is to produce these quantities faithfully from first‑principles DFT calculations, not merely to guess a set of numbers.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Build supercell structures for doped PZT
- Role: process
- Action: Construct 2×2×4 supercells of Pb(Zr0.25Ti0.75)O3 with lattice parameters a=b=7.892 Å, c/a=2.094. For each dopant (La, Y, Sc), replace the central Pb with a vacancy and two other Pb atoms with the trivalent substituent to maintain charge neutrality.
- Evidence: `/app/outputs/supercell_construction.log`

### Step 2: Geometry optimization of doped supercells
- Role: process
- Action: Perform DFT geometry optimization using GGA-PBE functional, relaxing all atomic positions without symmetry constraints.
- Evidence: `/app/outputs/relaxation_output.txt`

### Step 3: Compute Ti‑O‑Ti bond angles
- Role: scored
- Action: From the optimized structures, compute and record the Ti‑O‑Ti bond angle for each doped system.
- Output file: `/app/outputs/step_02_bond_angles.csv`
- Format: csv
- Contract: columns: system (string), Ti_O_Ti_angle_deg (float)
- Scoring: scored by hidden verifier

### Step 4: Electronic structure and optical calculation
- Role: process
- Action: Perform meta‑GGA DFT calculations for each doped system: compute density of states, band structure, and the frequency‑dependent dielectric function to obtain the absorption spectrum.
- Evidence: `/app/outputs/dos_bands_optics.log`

### Step 5: Compute energy and optical band gaps
- Role: scored (load-bearing)
- Action: From the band structure, determine the Kohn‑Sham band gap (energy difference VBM–CBM). From the absorption spectrum, apply Tauc analysis (extrapolation of (αhν)² vs hν) to obtain the optical band gap. Record both gaps for each system.
- Output file: `/app/outputs/step_01_band_gaps.csv`
- Format: csv
- Contract: columns: system (string), energy_band_gap_eV (float), optical_band_gap_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Reference O2 molecule calculation
- Role: process
- Action: Compute the total energy of an isolated O2 molecule (bond length 1.21 Å) using GGA‑PBE to obtain the oxygen chemical potential under oxygen‑rich conditions.
- Evidence: `/app/outputs/o2_energy.txt`

### Step 7: Calculate total energies of supercells with oxygen vacancies
- Role: process
- Action: Create defect supercells by removing one oxygen atom from each relaxed doped supercell, then perform single‑point energy calculations to obtain their total energies.
- Evidence: `/app/outputs/vacancy_energies.log`

### Step 8: Compute oxygen vacancy formation energies
- Role: scored
- Action: Using the total energies of the perfect and defect supercells and the oxygen chemical potential, compute the formation energy via E_f = E_defect − E_perfect + μ_O.
- Output file: `/app/outputs/step_03_formation_energies.csv`
- Format: csv
- Contract: columns: system (string), O_vacancy_formation_energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gaps.csv`
- `/app/outputs/step_02_bond_angles.csv`
- `/app/outputs/step_03_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gaps.csv
- path: `/app/outputs/step_01_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy band gap (Kohn-Sham gap) and optical band gap (Tauc analysis) for each doped system.
- schema:
  - `required_columns`: `system`, `energy_band_gap_eV`, `optical_band_gap_eV`
  - `units`:
    - `energy_band_gap_eV`: eV
    - `optical_band_gap_eV`: eV

### step_02_bond_angles.csv
- path: `/app/outputs/step_02_bond_angles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ti-O-Ti bond angle for each doped system.
- schema:
  - `required_columns`: `system`, `Ti_O_Ti_angle_deg`
  - `units`:
    - `Ti_O_Ti_angle_deg`: deg

### step_03_formation_energies.csv
- path: `/app/outputs/step_03_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Neutral oxygen vacancy formation energy under oxygen-rich conditions for each doped system.
- schema:
  - `required_columns`: `system`, `O_vacancy_formation_energy_eV`
  - `units`:
    - `O_vacancy_formation_energy_eV`: eV

Notes: Quantities are computed from first-principles DFT using open-source tools. The checker compares the reported values against hidden reference data and verifies the expected monotonic trends (band gaps decreasing with increasing atomic number; bond angles increasing with ionic radius). No gold values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "system",
          "energy_band_gap_eV",
          "optical_band_gap_eV"
        ],
        "units": {
          "energy_band_gap_eV": "eV",
          "optical_band_gap_eV": "eV"
        }
      },
      "description": "Energy band gap (Kohn-Sham gap) and optical band gap (Tauc analysis) for each doped system."
    },
    {
      "file": "step_02_bond_angles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "system",
          "Ti_O_Ti_angle_deg"
        ],
        "units": {
          "Ti_O_Ti_angle_deg": "deg"
        }
      },
      "description": "Ti-O-Ti bond angle for each doped system."
    },
    {
      "file": "step_03_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "system",
          "O_vacancy_formation_energy_eV"
        ],
        "units": {
          "O_vacancy_formation_energy_eV": "eV"
        }
      },
      "description": "Neutral oxygen vacancy formation energy under oxygen-rich conditions for each doped system."
    }
  ],
  "notes": "Quantities are computed from first-principles DFT using open-source tools. The checker compares the reported values against hidden reference data and verifies the expected monotonic trends (band gaps decreasing with increasing atomic number; bond angles increasing with ionic radius). No gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier reads your submitted output files and scores each stage independently, then combines the stage scores into a final reward between 0 and 1.

For the band gaps and bond angles, the verifier checks both the absolute values and the relative ordering of the computed quantities across the three dopant systems: the trend must follow the expected physical pattern for Group IIIA substitution. For the formation energies, the verifier compares your reported values to reference data.

Reporting numbers that agree with the hidden reference values and that exhibit the correct trend across dopants yields a high score; deviations or missing artifacts reduce the score. You are not required to know the paper's published numbers — the verifier holds them — and the tolerances used are not disclosed. The task is solved by performing the DFT workflow as specified and writing the results to the output files, not by manually matching any particular pre‑known value.
