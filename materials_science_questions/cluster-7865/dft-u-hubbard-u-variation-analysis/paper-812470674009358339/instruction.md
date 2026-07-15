# Hubbard U Parameter Determination for Ni and Co Hydroxides

## Problem background
Transition metal hydroxides such as β-Ni(OH)₂ and β-Co(OH)₂ are important electrocatalysts. Density functional theory (DFT) calculations using standard functionals suffer from self-interaction error in localized d orbitals, leading to inaccurate bandgaps and magnetic moments. The Hubbard U correction is a common remedy, but the appropriate U value is material- and functional-dependent. This task determines the optimal Hubbard U parameters for Ni(II) and Co(II) in the β-M(OH)₂ lattice by systematically varying U and comparing computed optical bandgap and local magnetic moment to established experimental benchmarks.

## Approach
Use DFT with the GGA+U method and the BEEF-vdW exchange-correlation functional. Model the bulk β-Ni(OH)₂ and β-Co(OH)₂ unit cells with spin‑polarized antiferromagnetic ordering. For each material, perform a series of self‑consistent calculations while scanning the Hubbard U parameter applied to the transition‑metal d states. From each calculation, extract the optical bandgap from the total density of states; for Ni also extract the local magnetic moment. The optimal U for each element is the value that brings the computed properties into best agreement with known experimental references (optical bandgap and magnetic moment).

## Reproduction target
Perform GGA+U calculations on the relaxed bulk unit cells of β-Ni(OH)₂ and β-Co(OH)₂ for a series of Hubbard U values (∼0–8 eV, step ∼0.5 eV). For each U, record the optical bandgap extracted from the TDOS. For β-Ni(OH)₂, also record the local Ni magnetic moment. The goal is to produce the scan data from which the U value that best matches the following experimental targets can be determined:
- β-Ni(OH)₂: optical bandgap ~3.0–3.5 eV and local Ni magnetic moment 2.0±0.2 μB
- β-Co(OH)₂: optical bandgap ~2.85 eV.
The results must be saved as JSON arrays in the designated output files.

## Assets

- β-Ni(OH)₂ bulk structure (Materials Project mp-27912): https://next-gen.materialsproject.org/materials/mp-27912
- β-Co(OH)₂ bulk structure (ICSD 26763): ICSD-26763
- GPAW (DFT code): https://wiki.fysik.dtu.dk/gpaw/
- ASE (Atomic Simulation Environment): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Relax bulk β-Ni(OH)₂ unit cell
- Role: process
- Action: Load β‑Ni(OH)₂ primitive cell from Materials Project (mp‑27912). Set up spin‑polarized antiferromagnetic initialisation and relax the cell using GPAW with the BEEF‑vdW functional until atomic forces are converged.
- Evidence: `/app/outputs/ni_relaxed.traj`

### Step 2: Relax bulk β-Co(OH)₂ unit cell
- Role: process
- Action: Load β‑Co(OH)₂ structure from ICSD‑26763. Set up spin‑polarized antiferromagnetic initialisation and relax the cell using GPAW with the BEEF‑vdW functional until atomic forces are converged.
- Evidence: `/app/outputs/co_relaxed.traj`

### Step 3: Ni Hubbard U scan
- Role: scored (load-bearing)
- Action: Using the relaxed β‑Ni(OH)₂ cell, perform self‑consistent GGA+U calculations for Hubbard U values of the Ni d‑states in the range 0–8 eV (step ~0.5 eV) with the BEEF‑vdW functional and antiferromagnetic spin ordering. For each U, extract the optical bandgap from the total density of states (TDOS) and the local Ni magnetic moment. Save the results as a JSON array.
- Output file: `/app/outputs/ni_u_scan.json`
- Format: json
- Contract: [{"U": <float>, "bandgap": <float>, "magnetic_moment": <float>}, ...]
- Scoring: scored by hidden verifier

### Step 4: Co Hubbard U scan
- Role: scored
- Action: Using the relaxed β‑Co(OH)₂ cell, perform self‑consistent GGA+U calculations for Hubbard U values of the Co d‑states in the range 0–8 eV (step ~0.5 eV) with the BEEF‑vdW functional. For each U, extract the optical bandgap from the TDOS. Save the results as a JSON array.
- Output file: `/app/outputs/co_u_scan.json`
- Format: json
- Contract: [{"U": <float>, "bandgap": <float>}, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ni_u_scan.json`
- `/app/outputs/co_u_scan.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ni_u_scan.json
- path: `/app/outputs/ni_u_scan.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Ni Hubbard U scan: for each trial U, the computed optical bandgap and local Ni magnetic moment. The checker uses these data to derive the optimal U_Ni that best matches experimental targets (hidden) and compares to the paper's U_Ni within tolerance.
- schema:
  - `type`: array
  - `required`:
    - `U`: float (eV)
    - `bandgap`: float (eV)
    - `magnetic_moment`: float (μB)
  - `items`:
    - `U`: float
    - `bandgap`: float
    - `magnetic_moment`: float

### co_u_scan.json
- path: `/app/outputs/co_u_scan.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Co Hubbard U scan: for each trial U, the computed optical bandgap. The checker uses these data to derive the optimal U_Co that best matches the experimental target (hidden) and compares to the paper's U_Co within tolerance.
- schema:
  - `type`: array
  - `required`:
    - `U`: float (eV)
    - `bandgap`: float (eV)
  - `items`:
    - `U`: float
    - `bandgap`: float

Notes: The checker recomputes the optimal Hubbard U values from the raw scan data (ni_u_scan.json, co_u_scan.json) according to the published fitting protocol (comparison to experimental optical bandgap and magnetic moment benchmarks). The agent does not need to report a final U value; the scan data is sufficient. The hidden gold values and tolerances are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ni_u_scan.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "required": {
          "U": "float (eV)",
          "bandgap": "float (eV)",
          "magnetic_moment": "float (μB)"
        },
        "items": {
          "U": "float",
          "bandgap": "float",
          "magnetic_moment": "float"
        }
      },
      "description": "Ni Hubbard U scan: for each trial U, the computed optical bandgap and local Ni magnetic moment. The checker uses these data to derive the optimal U_Ni that best matches experimental targets (hidden) and compares to the paper's U_Ni within tolerance."
    },
    {
      "file": "co_u_scan.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "required": {
          "U": "float (eV)",
          "bandgap": "float (eV)"
        },
        "items": {
          "U": "float",
          "bandgap": "float"
        }
      },
      "description": "Co Hubbard U scan: for each trial U, the computed optical bandgap. The checker uses these data to derive the optimal U_Co that best matches the experimental target (hidden) and compares to the paper's U_Co within tolerance."
    }
  ],
  "notes": "The checker recomputes the optimal Hubbard U values from the raw scan data (ni_u_scan.json, co_u_scan.json) according to the published fitting protocol (comparison to experimental optical bandgap and magnetic moment benchmarks). The agent does not need to report a final U value; the scan data is sufficient. The hidden gold values and tolerances are not disclosed."
}
```

## How you are scored
A hidden verifier reads your submitted raw scan data files (ni_u_scan.json and co_u_scan.json). It independently determines the optimal Hubbard U values for Ni and Co according to the published fitting protocol (comparison against the experimental benchmarks). The verifier then compares its determined U values to the paper’s reference values using pre‑set tolerances. The final reward is a weighted combination of the agreements for Ni and Co; full credit is awarded when both determined U values lie within the hidden tolerance. Reporting the paper’s numbers without producing genuine scan data will not pass this verification.
