# Phonon-based Dynamical Stability Analysis

## Problem background
The existence and stability of metallic hydrogen at zero pressure is a long-standing problem motivated by potential high-temperature superconductivity and the search for a metastable metallic phase. Theoretical predictions suggest that at electron densities around r_s ≈ 1.7 the metallic phase may have a positive compressibility and that certain low-symmetry crystal structures could be energetically competitive. However, the identity of the ground-state crystal structure and its dynamical stability remain to be determined computationally. This task addresses that open question by asking you to compute the total energies of several candidate structure families and to assess the phonon spectrum of the most favourable candidate.

## Approach
We use plane-wave density-functional theory (DFT) with a standard hydrogen pseudopotential to evaluate the total energy per atom of metallic hydrogen at a fixed electron density. Four candidate structure families are considered: simple hexagonal, simple tetragonal, the triangular family (derived from simple hexagonal by a shear along the c-axis that preserves the hexagonal projection, with c/a < 1), and the square family (derived from simple tetragonal by an analogous shear that preserves the tetragonal projection). From the resulting energies we identify the lowest-energy family. Then, for that family, we compute the phonon dispersion and density of states using density-functional perturbation theory to check for imaginary (negative) frequency modes, which would signal dynamical instability. The overall comparison yields a verdict on which family provides the absolute energy minimum and whether it is dynamically stable at zero pressure.

## Reproduction target
Your task is to identify the lowest-energy crystal structure family among simple hexagonal, simple tetragonal, the triangular family, and the square family of metallic hydrogen at an electron density corresponding to r_s ≈ 1.7, and to assess the dynamical stability of that lowest-energy structure. To accomplish this, you must:

- Run DFT total-energy calculations for all four families and write the total energy per atom (in Ry or eV) to `/app/outputs/energy_table.json`.
- Compute the phonon dispersion for the family that shows the lowest total energy and write the number of imaginary modes and the minimum phonon frequency (in cm⁻¹) to `/app/outputs/phonon_dispersion.json`.
- Compile a summary that states which family is the lowest in energy and whether it is dynamically stable (no significant imaginary modes) in `/app/outputs/stability_summary.json`.

The exact JSON schemas for these files are given in the workflow steps and output contract below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Hydrogen pseudopotential: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Total energy calculations
- Role: scored
- Action: Set up the unit cells for simple hexagonal, simple tetragonal, triangular family (sheared hexagonal with c/a < 1) and square family (sheared tetragonal) structures at an electron density corresponding to r_s ≈ 1.7. Run DFT calculations using Quantum ESPRESSO to obtain total energy per atom. Collect the results into a JSON file.
- Output file: `/app/outputs/energy_table.json`
- Format: json
- Contract: {"hexagonal": <float>, "tetragonal": <float>, "triangular": <float>, "square": <float>}
- Scoring: scored by hidden verifier

### Step 2: Phonon dispersion calculation
- Role: scored (load-bearing)
- Action: Using the lowest-energy structure from step 1, compute its phonon dispersion (frequencies at a set of q-points) and density of states with Quantum ESPRESSO's ph.x module. Record the number of imaginary (negative) frequency modes and the minimum phonon frequency.
- Output file: `/app/outputs/phonon_dispersion.json`
- Format: json
- Contract: {"n_imaginary_modes": <int>, "min_imaginary_freq": <float>}
- Scoring: scored by hidden verifier

### Step 3: Stability summary
- Role: scored
- Action: From the energy table and phonon dispersion result, compile a summary JSON file indicating the family with the lowest energy and whether the structure is dynamically stable (no imaginary modes, min_imaginary_freq ≈ 0 or non-negative).
- Output file: `/app/outputs/stability_summary.json`
- Format: json
- Contract: {"lowest_energy_family": <string>, "dynamically_stable": <bool>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_table.json`
- `/app/outputs/phonon_dispersion.json`
- `/app/outputs/stability_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_table.json
- path: `/app/outputs/energy_table.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON object with total energy per atom for the four structure families. The checker verifies that the relative energy ordering among the families matches the paper's expected result.
- schema:
  - `type`: object
  - `required`:
    - `hexagonal`: float (energy per atom)
    - `tetragonal`: float (energy per atom)
    - `triangular`: float (energy per atom)
    - `square`: float (energy per atom)
  - `units`:
    - `energy`: Ry or eV

### phonon_dispersion.json
- path: `/app/outputs/phonon_dispersion.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON object summarizing the phonon stability check. The checker verifies that n_imaginary_modes is 0 and min_imaginary_freq is non-negative (within a small tolerance).
- schema:
  - `type`: object
  - `required`:
    - `n_imaginary_modes`: int
    - `min_imaginary_freq`: float (cm⁻¹, negative if imaginary)
  - `units`:
    - `frequency`: cm⁻¹

### stability_summary.json
- path: `/app/outputs/stability_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON object with the final conclusion: the name of the lowest-energy family and a boolean for dynamical stability. The checker verifies that the lowest_energy_family is consistent with the energy table and that dynamically_stable reflects the phonon stability result.
- schema:
  - `type`: object
  - `required`:
    - `lowest_energy_family`: string
    - `dynamically_stable`: bool

Notes: The main reproducibility claim is that a specific crystal structure family yields the absolute energy minimum and is dynamically stable. The checker performs a structural audit: energy ordering (the claimed family must have the lowest energy) and phonon stability (no imaginary modes). The stability summary provides a human-readable verdict consistent with the computed data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_table.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "hexagonal": "float (energy per atom)",
          "tetragonal": "float (energy per atom)",
          "triangular": "float (energy per atom)",
          "square": "float (energy per atom)"
        },
        "units": {
          "energy": "Ry or eV"
        }
      },
      "description": "JSON object with total energy per atom for the four structure families. The checker verifies that the relative energy ordering among the families matches the paper's expected result."
    },
    {
      "file": "phonon_dispersion.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "n_imaginary_modes": "int",
          "min_imaginary_freq": "float (cm⁻¹, negative if imaginary)"
        },
        "units": {
          "frequency": "cm⁻¹"
        }
      },
      "description": "JSON object summarizing the phonon stability check. The checker verifies that n_imaginary_modes is 0 and min_imaginary_freq is non-negative (within a small tolerance)."
    },
    {
      "file": "stability_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "lowest_energy_family": "string",
          "dynamically_stable": "bool"
        }
      },
      "description": "JSON object with the final conclusion: the name of the lowest-energy family and a boolean for dynamical stability. The checker verifies that the lowest_energy_family is consistent with the energy table and that dynamically_stable reflects the phonon stability result."
    }
  ],
  "notes": "The main reproducibility claim is that a specific crystal structure family yields the absolute energy minimum and is dynamically stable. The checker performs a structural audit: energy ordering (the claimed family must have the lowest energy) and phonon stability (no imaginary modes). The stability summary provides a human-readable verdict consistent with the computed data."
}
```

## How you are scored
A hidden verifier independently evaluates each of your three output files. For `energy_table.json`, it checks the relative energy ordering among the four families. For `phonon_dispersion.json`, it verifies that the reported imaginary-mode count and the minimum frequency are consistent with dynamical stability (no physically significant imaginary modes). For `stability_summary.json`, it confirms that the declared lowest-energy family and the stability boolean agree with the energy and phonon data. The final reward is a weighted combination of these checks; reporting numbers alone is not sufficient—the submitted artifacts must be internally consistent and derived from the prescribed computational workflow.
