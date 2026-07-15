# Momentum Density Distributions in Ni3Ga via First-Principles

## Problem background
The intermetallic compound Ni₃Ga crystallizes in the cubic L1₂ structure and shows Stoner-type magnetic behavior. Its electronic structure can be probed via momentum density distributions measured by Compton scattering and positron annihilation. First-principles calculations of the one-dimensional Compton profiles and angular correlation of positron annihilation radiation (1D‑ACAR) reveal the occupied band structure and the role of localized d‑states. This task computes these momentum distributions from a self‑consistent density‑functional calculation.

## Approach
Use a full‑potential linearized augmented‑plane‑wave (FLAPW) code such as Elk to perform a self‑consistent DFT calculation for Ni₃Ga in the L1₂ structure using the local‑density approximation (the Gunnarsson‑Lundqvist exchange‑correlation functional). The lattice constant is 6.7580 a.u., APW sphere radii are 2.2974 a.u. (Ni) and 2.4812 a.u. (Ga). From the converged ground‑state wavefunctions and Fermi energy, compute the momentum wavefunctions for electron Compton scattering and for positron annihilation within the impulse approximation. Integrate over occupied states to obtain the one‑dimensional profiles along the three principal crystallographic directions [100], [110], and [111]. Finally, derive directional anisotropy curves as differences between these profiles.

## Reproduction target
Compute the theoretical Compton profiles J⁻(p_z) on a grid of p_z from 0 to 8 a.u. along the [100], [110], and [111] directions, and the 1D‑ACAR profiles J⁺(p_z) along the same directions on a grid from 0 to 5 a.u. Each profile must contain at least 50 points. From these, derive the anisotropy curves ΔJ(p_z) = J(hkl) – J(h'k'l') for the three pairs (111)−(100), (111)−(110), and (110)−(100). Export all results as CSV files with the columns specified in the workflow steps.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.net/

## Workflow steps

### Step 1: Self-consistent DFT calculation of Ni3Ga
- Role: process
- Action: Perform a self-consistent DFT calculation for Ni3Ga in the cubic L12 structure (lattice constant 6.7580 au) using the local-density approximation (Gunnarsson-Lundqvist exchange-correlation functional). APW sphere radii: 2.2974 au (Ni), 2.4812 au (Ga). Use a suitable k-point mesh for the irreducible Brillouin zone. Converge the total energy and wavefunctions. Produce the ground-state charge density, wavefunctions, and Fermi energy.
- Evidence: `/app/outputs/dft_log.txt`

### Step 2: Compute Compton profiles
- Role: scored (load-bearing)
- Action: From the ground-state wavefunctions and Fermi energy, compute momentum wavefunctions for electron Compton scattering and evaluate the one-dimensional Compton profile J^-(p_z) along the [100], [110], and [111] directions within the impulse approximation. Include contributions from both valence (occupied) and core electrons. Output the profiles on a grid of p_z from 0 to 8 a.u. with at least 50 points.
- Output file: `/app/outputs/compton_profiles.csv`
- Format: csv
- Contract: columns: p_z (float, atomic units), J_100 (float), J_110 (float), J_111 (float). At least 50 points from 0 to 8 au.
- Scoring: scored by hidden verifier

### Step 3: Compute 1D-ACAR profiles
- Role: scored
- Action: From the ground-state wavefunctions and Fermi energy, compute the positron annihilation momentum wavefunctions and evaluate the one-dimensional angular correlation of positron annihilation radiation J^+(p_z) along the [100], [110], and [111] directions. Include both valence and core contributions. Output on a grid of p_z from 0 to 5 a.u. with at least 50 points.
- Output file: `/app/outputs/acar_profiles.csv`
- Format: csv
- Contract: columns: p_z (float), J_100 (float), J_110 (float), J_111 (float). At least 50 points from 0 to 5 au.
- Scoring: scored by hidden verifier

### Step 4: Derive Compton profile anisotropy curves
- Role: scored
- Action: From the Compton profiles in step_02, compute the directional difference curves ΔJ(p_z) = J(hkl) - J(h'k'l') for the three pairs: (111)-(100), (111)-(110), and (110)-(100). Output the three anisotropy curves on the same p_z grid.
- Output file: `/app/outputs/anisotropy_cp.csv`
- Format: csv
- Contract: columns: p_z (float), delta_110_100 (float), delta_111_100 (float), delta_111_110 (float).
- Scoring: scored by hidden verifier

### Step 5: Derive 1D-ACAR anisotropy curves
- Role: scored
- Action: From the 1D-ACAR profiles in step_03, compute the directional difference curves for the three pairs: (111)-(100), (111)-(110), and (110)-(100). Output on the same p_z grid.
- Output file: `/app/outputs/anisotropy_acar.csv`
- Format: csv
- Contract: columns: p_z (float), delta_110_100 (float), delta_111_100 (float), delta_111_110 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/compton_profiles.csv`
- `/app/outputs/acar_profiles.csv`
- `/app/outputs/anisotropy_cp.csv`
- `/app/outputs/anisotropy_acar.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### compton_profiles.csv
- path: `/app/outputs/compton_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Theoretical Compton profiles along three principal directions. The checker compares the profile values against hidden reference curves digitized from the paper's figures, computing per-curve MAD with a hidden tolerance; an integral check is also applied.
- schema:
  - `type`: table
  - `required_columns`: `p_z`, `J_100`, `J_110`, `J_111`
  - `units`:
    - `p_z`: a.u.
    - `J_100`: a.u.
    - `J_110`: a.u.
    - `J_111`: a.u.

### acar_profiles.csv
- path: `/app/outputs/acar_profiles.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Theoretical 1D-ACAR profiles along three directions. Compared against hidden reference curves digitized from the paper.
- schema:
  - `type`: table
  - `required_columns`: `p_z`, `J_100`, `J_110`, `J_111`
  - `units`:
    - `p_z`: a.u.
    - `J_100`: a.u.
    - `J_110`: a.u.
    - `J_111`: a.u.

### anisotropy_cp.csv
- path: `/app/outputs/anisotropy_cp.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Compton profile anisotropy curves. Compared against hidden reference curves derived from the paper's digitized data.
- schema:
  - `type`: table
  - `required_columns`: `p_z`, `delta_110_100`, `delta_111_100`, `delta_111_110`
  - `units`:
    - `p_z`: a.u.
    - `delta_110_100`: a.u.
    - `delta_111_100`: a.u.
    - `delta_111_110`: a.u.

### anisotropy_acar.csv
- path: `/app/outputs/anisotropy_acar.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: 1D-ACAR anisotropy curves. Compared against hidden reference curves.
- schema:
  - `type`: table
  - `required_columns`: `p_z`, `delta_110_100`, `delta_111_100`, `delta_111_110`
  - `units`:
    - `p_z`: a.u.
    - `delta_110_100`: a.u.
    - `delta_111_100`: a.u.
    - `delta_111_110`: a.u.

Notes: The hidden checker compares each profile and anisotropy curve to digitized gold standards extracted from the paper's figures and applies a mean absolute deviation (MAD) tolerance. An additional integral check is performed on the total Compton profile. The reward is proportional to the fraction of curves passing the tolerance threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "compton_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_z",
          "J_100",
          "J_110",
          "J_111"
        ],
        "units": {
          "p_z": "a.u.",
          "J_100": "a.u.",
          "J_110": "a.u.",
          "J_111": "a.u."
        }
      },
      "description": "Theoretical Compton profiles along three principal directions. The checker compares the profile values against hidden reference curves digitized from the paper's figures, computing per-curve MAD with a hidden tolerance; an integral check is also applied."
    },
    {
      "file": "acar_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_z",
          "J_100",
          "J_110",
          "J_111"
        ],
        "units": {
          "p_z": "a.u.",
          "J_100": "a.u.",
          "J_110": "a.u.",
          "J_111": "a.u."
        }
      },
      "description": "Theoretical 1D-ACAR profiles along three directions. Compared against hidden reference curves digitized from the paper."
    },
    {
      "file": "anisotropy_cp.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_z",
          "delta_110_100",
          "delta_111_100",
          "delta_111_110"
        ],
        "units": {
          "p_z": "a.u.",
          "delta_110_100": "a.u.",
          "delta_111_100": "a.u.",
          "delta_111_110": "a.u."
        }
      },
      "description": "Compton profile anisotropy curves. Compared against hidden reference curves derived from the paper's digitized data."
    },
    {
      "file": "anisotropy_acar.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_z",
          "delta_110_100",
          "delta_111_100",
          "delta_111_110"
        ],
        "units": {
          "p_z": "a.u.",
          "delta_110_100": "a.u.",
          "delta_111_100": "a.u.",
          "delta_111_110": "a.u."
        }
      },
      "description": "1D-ACAR anisotropy curves. Compared against hidden reference curves."
    }
  ],
  "notes": "The hidden checker compares each profile and anisotropy curve to digitized gold standards extracted from the paper's figures and applies a mean absolute deviation (MAD) tolerance. An additional integral check is performed on the total Compton profile. The reward is proportional to the fraction of curves passing the tolerance threshold."
}
```

## How you are scored
A hidden verifier checks the four output CSV files. For each individual profile and anisotropy curve, it compares your computed values to reference curves and calculates the mean absolute deviation (MAD). The verifier also checks that the integrated total Compton profile equals 33 (the number of valence electrons) within a tolerance. Your reward is the fraction of curves that pass all checks, linearly mapped to a score between 0 and 1. Simply reporting numbers from the literature is not sufficient; the artifact must be produced by executing the required calculations.
