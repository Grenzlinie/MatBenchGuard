# Ensemble Monte Carlo Simulation of Hole Mobility in Wurtzite InN

## Problem background
Hole transport in wurtzite InN is critical for developing p-type InN-based devices, but direct measurement of mobility is hindered by a surface electron accumulation layer that masks bulk hole properties. As a result, the low-field hole mobility can only be estimated through theoretical simulation. This task addresses the open question of what the hole mobility in wurtzite InN is at room temperature when transport is limited by lattice scattering alone, and how that mobility is suppressed when realistic defect densities—residual donors and threading dislocations—are present.

## Approach
The mobility is computed using an ensemble Monte Carlo (EMC) simulation. Hole dynamics are simulated under low electric fields, with sampling over a large number of carriers to obtain the average drift velocity. From the linear low-field region of the velocity–field curve, the mobility is extracted as the slope. The simulation includes all relevant scattering mechanisms: polar optical phonons (LO), nonpolar optical phonons (TO), acoustic phonons (both deformation potential and piezoelectric coupling), ionized and neutral impurities, and threading dislocations (modeled via the approach of Look and Sizelove). Carrier screening is treated with the Brooks‑Herring method. The hole concentration used in the simulation is not a free parameter but is determined self‑consistently from a neutrality condition that combines acceptor activation, residual donor density, and the thermal occupation of the valence band. Two distinct scenarios are studied: a nearly ideal, phonon‑limited case, and a realistic case that includes the high dislocation and donor densities typical of present‑day InN material.

## Reproduction target
Implement the EMC simulator described in the approach and apply it to two conditions:

1. **Phonon‑limited condition** — acceptor concentration Na = 2 × 10¹⁷ cm⁻³, residual donor concentration Nd = 5 × 10¹⁶ cm⁻³, threading dislocation density Ndisl = 0.
2. **Realistic condition** — Nd = 5 × 10¹⁷ cm⁻³, Ndisl = 1 × 10¹⁰ cm⁻². Choose the acceptor concentration Na iteratively so that the resulting hole concentration p is approximately 1 × 10¹⁶ cm⁻³.

For each condition, extract the low‑field hole mobility (cm² V⁻¹ s⁻¹) from the linear slope of the velocity‑field data. Report the phonon‑limited mobility, the realistic mobility, and the ratio of the two (realistic / phonon‑limited) in a single JSON file (`mobility_results.json`).

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Compute hole concentration via neutrality condition
- Role: process
- Action: Using the provided wurtzite InN material parameters and the neutrality equation at T=300 K, compute the hole concentration p for two target scenarios: (A) phonon-limited: acceptor concentration Na = 2e17 cm^-3, residual donor concentration Nd = 5e16 cm^-3; (B) realistic: Nd = 5e17 cm^-3, and choose Na iteratively to achieve hole concentration p ≈ 1e16 cm^-3. Record the resulting hole concentration p and the Na used for the realistic case.
- Evidence: `/app/outputs/hole_concentrations.json`

### Step 2: Run ensemble Monte Carlo simulations
- Role: process
- Action: Implement an ensemble Monte Carlo simulator for hole transport in wurtzite InN. Include all scattering mechanisms: LO polar optical phonons, TO nonpolar optical phonons, acoustic phonons (deformation potential and piezoelectric), ionized impurities with Brooks-Herring screening (Debye length), neutral impurities, and threading dislocations (Look-Sizelove model). Use the material parameters provided. For each scenario (phonon-limited and realistic), using the hole concentration from step 1, simulate an ensemble of 50,000 holes for 20 ps at a series of low electric fields. Record the average drift velocity at each electric field.
- Evidence: `/app/outputs/velocity_field_phonon_limited.csv, velocity_field_realistic.csv`

### Step 3: Extract low-field hole mobility
- Role: scored (load-bearing)
- Action: From the velocity-field data produced in step 2, identify the linear low-field region and perform linear regression to extract the slope as the low-field hole mobility μ (cm²/V·s) for each scenario. Compute the ratio of realistic mobility to phonon-limited mobility. Write these three numbers to a JSON file.
- Output file: `/app/outputs/mobility_results.json`
- Format: json
- Contract: {"phonon_limited_mobility": "float", "realistic_mobility": "float", "mobility_ratio": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mobility_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mobility_results.json
- path: `/app/outputs/mobility_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Low-field hole mobility for the two conditions: (a) phonon-limited, (b) with realistic dislocation density and residual donor concentration. The ratio is realistic_mobility / phonon_limited_mobility.
- schema:
  - `type`: object
  - `required`:
    - `phonon_limited_mobility`: float (cm²/V·s)
    - `realistic_mobility`: float (cm²/V·s)
    - `mobility_ratio`: float (dimensionless)

Notes: The checker compares each mobility and the ratio to hidden reference values (derived from the paper) with appropriate tolerances. Agent must implement the EMC simulation from scratch; no pre-existing code is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mobility_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "phonon_limited_mobility": "float (cm²/V·s)",
          "realistic_mobility": "float (cm²/V·s)",
          "mobility_ratio": "float (dimensionless)"
        }
      },
      "description": "Low-field hole mobility for the two conditions: (a) phonon-limited, (b) with realistic dislocation density and residual donor concentration. The ratio is realistic_mobility / phonon_limited_mobility."
    }
  ],
  "notes": "The checker compares each mobility and the ratio to hidden reference values (derived from the paper) with appropriate tolerances. Agent must implement the EMC simulation from scratch; no pre-existing code is provided."
}
```

## How you are scored
A hidden verifier reads your `mobility_results.json`. It independently compares your reported phonon‑limited mobility, realistic mobility, and their ratio to reference values obtained from the original study, using tolerances appropriate for the stochastic nature of Monte Carlo simulation and implementation differences. In addition, the verifier checks a basic structural requirement: that the mobility in the realistic scenario is lower than the phonon‑limited mobility, reflecting the suppression caused by defects. The final reward is a weighted combination of these quantitative and structural checks. You are not required to match any particular digit; a correct implementation that faithfully carries out the prescribed procedure will naturally fall within the expected range.
