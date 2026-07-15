# Molecular Dynamics Simulation of Superionic Ag2S and Neutron Scattering Analysis

## Problem background
Superionic conductors are a class of materials in which one ionic species forms a rigid crystalline framework while a second species diffuses through the lattice. In Ag2S, silver ions (Ag⁺) move within a body-centered cubic (BCC) framework of sulfur ions (S²⁻). Neutron scattering experiments have revealed unusual quasi-elastic scattering intensity near the reciprocal lattice point Q = (1.6, 1, 0) and, below the superionic transition temperature (≈ 450 K), a low-energy excitation appears in the dynamic structure factor S(Q, ω). Understanding the physical origin of these features—which ion-pair correlations dominate, the spatial anisotropy of the scattering intensity, and how the low-energy excitation evolves with temperature—is the subject of the present reproduction task.

## Approach
The method reconstructs the dynamics of Ag₂S using classical molecular dynamics (MD) with three effective pair potentials (Ag–Ag, Ag–S, S–S) that include Coulomb, short-range repulsion (∝ r⁻⁷) and a van der Waals‑like term (∝ r⁻⁴). Coulomb forces are handled by Ewald summation. A simulation cell of 384 particles (256 Ag⁺, 128 S²⁻) is built by placing sulfur on a BCC lattice at the experimental number density and distributing silver randomly over 2/3 of the tetrahedral interstitial sites. After thermalization, production runs at three temperatures—one well below, one near, and one above the superionic transition—generate ion trajectories. From these trajectories the species‑resolved intermediate scattering functions Fαβ(Q,t) are computed for a set of Q vectors around (1.6,1,0). A coherent neutron scattering function S(Q,ω) is assembled by weighting the four partial dynamical structure factors with the known neutron scattering lengths of Ag and S, and is convolved with a Gaussian function to mimic the experimental energy resolution. The zero‑energy intensity S(Q,0) and the energy‑resolved S(Q,ω) at a key wavevector are then extracted to characterise the spatial and temperature variations of the scattering.

## Reproduction target
Run MD simulations of Ag₂S at 268 K, 339 K, and 470 K using the specified pair potentials. From the trajectories, compute the species‑resolved intermediate scattering functions Fαβ(Q, t) at t = 0 for five Q vectors: (1.8,1,0), (1.6,1,0), (1.4,1,0), (1.6,0.8,0), and (1.6,1.2,0) (in BCC reciprocal lattice units). Then compute the total coherent zero‑energy neutron intensity S(Q,0) for the same Q vectors and temperatures by constructing the species‑weighted coherent scattering function, applying a 0.7 meV Gaussian resolution broadening, and taking the ω = 0 value. Finally, extract the full energy‑resolved S(Q,ω) curve at Q = (1.8,1,0) on an energy grid 0–10 meV (step ≤ 0.2 meV) for all three temperatures and identify whether any low‑energy peak exists in the 0–5 meV range. The objective is to determine: (i) which species‑pair correlations dominate the intermediate scattering; (ii) the Q‑dependence and anisotropy of the zero‑energy intensity; (iii) the existence and temperature evolution of a low‑energy excitation in the energy‑resolved S(Q,ω).

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/downloads.html
- Python scientific packages (numpy, scipy): pip install numpy scipy

## Workflow steps

### Step 1: MD simulation of Ag2S
- Role: process
- Action: Set up and run molecular dynamics simulations of Ag2S using effective pair potentials (Coulomb, short-range repulsion, van der Waals) and Ewald summation. Place sulphur ions on a BCC lattice and distribute silver ions randomly over tetrahedral sites; system size 384 particles at fixed number density 5.233×10²² cm⁻³. Perform production runs of at least 18000 steps at 268 K, 339 K, and 470 K, saving trajectories and velocities with sufficient temporal resolution to compute intermediate scattering functions up to ~40 ps.
- Evidence: `/app/outputs/md_trajectories.log`

### Step 2: Intermediate scattering functions F_αβ(Q,t) static values
- Role: scored (load-bearing)
- Action: From the MD trajectories at 470 K, compute the species-resolved intermediate scattering functions F_αβ(Q,t) = ⟨ρ_α(Q,t)ρ_β*(Q,0)⟩ for α,β ∈ {Ag,S} at the five Q vectors (in BCC reciprocal lattice units): (1.8,1,0), (1.6,1,0), (1.4,1,0), (1.6,0.8,0), (1.6,1.2,0). Extract the t=0 values (static structure factors) and write them to a CSV file.
- Output file: `/app/outputs/intermediate_scattering_functions_470K.csv`
- Format: csv
- Contract: Header: Q_h, Q_k, Q_l, F_AgAg, F_AgS, F_SAg, F_SS. Five rows, one per Q vector. All values floating-point.
- Scoring: scored by hidden verifier

### Step 3: Coherent zero-energy neutron intensity S(Q,0)
- Role: scored
- Action: For all three temperatures, compute the species-weighted coherent neutron scattering function S(Q,ω) = Σ_αβ b_α b_β √(c_α c_β) S_αβ(Q,ω) using neutron scattering lengths b_Ag = 5.922 fm, b_S = 2.847 fm and concentrations c_Ag = 2/3, c_S = 1/3, by Fourier transforming F_αβ(Q,t). Apply a Gaussian energy resolution with FWHM = 0.7 meV and extract the zero-energy intensity S(Q,0) for each of the five Q vectors. Write the values to a CSV file.
- Output file: `/app/outputs/zero_energy_intensity.csv`
- Format: csv
- Contract: Header: temperature, Q_h, Q_k, Q_l, S_zero. 15 rows (three temperatures × five Q vectors). All values floating-point.
- Scoring: scored by hidden verifier

### Step 4: Energy-resolved S(Q,ω) at Q=(1.8,1,0)
- Role: scored
- Action: For each temperature, extract the energy-resolved coherent scattering function S(Q,ω) for Q=(1.8,1,0) on an energy grid from 0 to 10 meV with steps no larger than 0.2 meV, after applying the 0.7 meV Gaussian resolution broadening. Write the curves to a CSV file.
- Output file: `/app/outputs/S_Q_w_Q1.8_1_0.csv`
- Format: csv
- Contract: Header: temperature, energy_meV, S. Multiple rows per temperature. Energy in meV, S unitless (arbitrary relative scale).
- Scoring: scored by hidden verifier

### Step 5: Low-energy excitation peak location
- Role: scored
- Action: From the S(Q,ω) curves for Q=(1.8,1,0), locate the energy at which S(Q,ω) attains its maximum in the range 0–5 meV after resolution broadening, separately for the 268 K and 339 K runs. For the 470 K run, if no distinct peak exists above the baseline, record null. Write the peak energies as a JSON object.
- Output file: `/app/outputs/low_energy_peak_summary.json`
- Format: json
- Contract: JSON object with keys: peak_energy_meV_268K (float), peak_energy_meV_339K (float or null), peak_energy_meV_470K (float or null).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/intermediate_scattering_functions_470K.csv`
- `/app/outputs/zero_energy_intensity.csv`
- `/app/outputs/S_Q_w_Q1.8_1_0.csv`
- `/app/outputs/low_energy_peak_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### intermediate_scattering_functions_470K.csv
- path: `/app/outputs/intermediate_scattering_functions_470K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Static structure factors F_αβ(Q,t=0) for 470 K at five Q vectors; used to verify that Ag–Ag correlations dominate (at least 10× larger than any other pair).
- schema:
  - `type`: table
  - `required_columns`: `Q_h`, `Q_k`, `Q_l`, `F_AgAg`, `F_AgS`, `F_SAg`, `F_SS`

### zero_energy_intensity.csv
- path: `/app/outputs/zero_energy_intensity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Zero-energy neutron intensity S(Q,0) for three temperatures and five Q vectors, plus the quasi-elastic peak FWHM at Q=(1.6,1,0) for each temperature. Used to verify the spatial pattern, temperature trend, and the monotonic increase of the linewidth with temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `Q_h`, `Q_k`, `Q_l`, `S_zero`, `FWHM_meV`

### S_Q_w_Q1.8_1_0.csv
- path: `/app/outputs/S_Q_w_Q1.8_1_0.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: S(Q,ω) curves for Q=(1.8,1,0) spanning 0–10 meV; checked for a distinct low-energy peak around 3 meV at 268 K and its broadening or disappearance at 470 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `energy_meV`, `S`

### low_energy_peak_summary.json
- path: `/app/outputs/low_energy_peak_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Detected low-energy excitation peak positions; the 268 K peak must lie in the 2–4 meV range, and the 470 K entry must be null.
- schema:
  - `type`: object
  - `required`:
    - `peak_energy_meV_268K`: float
    - `peak_energy_meV_339K`: float or null
    - `peak_energy_meV_470K`: float or null

Notes: All checks are structural and comparison-based: the verifier reads the submitted CSVs/JSON and confirms (i) Ag–Ag dominance, (ii) S_zero spatial pattern, (iii) FWHM of the quasi-elastic peak increases monotonically with temperature, (iv) low-energy peak existence and energy range, without requiring exact numeric agreement with the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "intermediate_scattering_functions_470K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Q_h",
          "Q_k",
          "Q_l",
          "F_AgAg",
          "F_AgS",
          "F_SAg",
          "F_SS"
        ]
      },
      "description": "Static structure factors F_αβ(Q,t=0) for 470 K at five Q vectors; used to verify that Ag–Ag correlations dominate (at least 10× larger than any other pair)."
    },
    {
      "file": "zero_energy_intensity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "Q_h",
          "Q_k",
          "Q_l",
          "S_zero",
          "FWHM_meV"
        ]
      },
      "description": "Zero-energy neutron intensity S(Q,0) for three temperatures and five Q vectors, plus the quasi-elastic peak FWHM at Q=(1.6,1,0) for each temperature. Used to verify the spatial pattern, temperature trend, and the monotonic increase of the linewidth with temperature."
    },
    {
      "file": "S_Q_w_Q1.8_1_0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "energy_meV",
          "S"
        ]
      },
      "description": "S(Q,ω) curves for Q=(1.8,1,0) spanning 0–10 meV; checked for a distinct low-energy peak around 3 meV at 268 K and its broadening or disappearance at 470 K."
    },
    {
      "file": "low_energy_peak_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "peak_energy_meV_268K": "float",
          "peak_energy_meV_339K": "float or null",
          "peak_energy_meV_470K": "float or null"
        }
      },
      "description": "Detected low-energy excitation peak positions; the 268 K peak must lie in the 2–4 meV range, and the 470 K entry must be null."
    }
  ],
  "notes": "All checks are structural and comparison-based: the verifier reads the submitted CSVs/JSON and confirms (i) Ag–Ag dominance, (ii) S_zero spatial pattern, (iii) FWHM of the quasi-elastic peak increases monotonically with temperature, (iv) low-energy peak existence and energy range, without requiring exact numeric agreement with the paper."
}
```

## How you are scored
A hidden verifier examines each of the four output files independently. It checks that in the static Fαβ data one species pair dominates over all others for every Q vector. It verifies that the zero‑energy intensity S(Q,0) is highest at a specific Q point and that the intensity decreases more rapidly when moving away along one crystallographic direction than along another. The energy‑resolved S(Q,ω) curve at Q = (1.8,1,0) is inspected for the presence of a low‑energy excitation (0–5 meV) at temperatures below the superionic transition, and it is confirmed that the feature weakens or disappears above the transition. Scoring is based on structural trends and relative comparisons, not on exact numerical absolute values; reproducing the correct physical signatures is sufficient.
