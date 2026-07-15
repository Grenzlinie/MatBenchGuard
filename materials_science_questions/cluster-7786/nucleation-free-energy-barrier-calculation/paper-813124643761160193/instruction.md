# Critical Nucleus Size and Solid‑Liquid Interface Energy of Niobium from MD Simulations

## Problem background
In metal solidification, the critical nucleus size and the solid–liquid interface energy are fundamental parameters that determine how easily crystallization begins from an undercooled melt. For refractory metals such as niobium, measuring these quantities directly by experiment is extremely difficult. Molecular dynamics (MD) simulations offer a computational route: by modelling the atomic interactions explicitly and testing the stability of a crystalline nucleus inside a liquid bath, one can determine the minimum nucleus size needed for solidification at a given undercooling. That minimum size is the critical nucleus size n*, and from the dependence of n* on temperature the average solid–liquid interface energy σ can be derived using classical nucleation theory. This task asks you to compute n* for pure niobium at several undercoolings and to derive σ from the resulting data.

## Approach
The approach uses MD simulations with an embedded-atom method (EAM) potential for pure niobium. For each of the specified undercoolings ΔT (measured relative to the MD melting temperature), a crystalline nucleus with a certain number of atoms is inserted into a liquid bath containing approximately 16 000 atoms. The system is relaxed under constant temperature and pressure (NPT ensemble). The stability of the nucleus is probed by adding atoms one by one and repeating the relaxation; the smallest nucleus size for which the entire system eventually solidifies is recorded as the critical nucleus size n*(ΔT). After obtaining n* at all six undercoolings, classical nucleation theory is used to connect n* and ΔT: the quantity n*^(1/3) is expected to vary linearly with 1/ΔT. The slope of that linear fit, together with the provided physical constants (atomic volume, heat of fusion, and melting temperature), yields the average solid–liquid interface energy σ. The required formula and constants are detailed in Step 2.

## Reproduction target
Produce the following two files: 
1. `critical_nucleus_sizes.csv` – the critical nucleus size n* (number of atoms) for pure niobium at the six undercoolings ΔT = 200, 300, 400, 500, 600, 689 K. 
2. `interface_energy.txt` – the average solid–liquid interface energy σ (in J m⁻²) computed from the n* data and the constants provided in Step 2. 
The output files must follow the format and schema specified under “Output contract”.

## Assets

- EAM potential for pure Nb by Fellinger et al. (2010): https://www.ctcms.nist.gov/potentials/Entry/2010-Fellinger-M-R-Park-H-Wilkins-J-W-Nb/
- LAMMPS molecular dynamics package: https://www.lammps.org

## Workflow steps

### Step 1: MD simulation of critical nucleus size
- Role: scored (load-bearing)
- Action: Obtain the EAM potential for pure Nb from Fellinger et al. (2010) and the LAMMPS package. For each of the six undercoolings ΔT = 200, 300, 400, 500, 600, 689 K (using the MD melting point of 2689 K for Nb), construct a crystalline nucleus embedded in a liquid bath of approximately 16,000 atoms. Add atoms to the nucleus one by one, running MD under NPT conditions to test stability. Record the smallest number of atoms in the nucleus for which the system solidifies, which is the critical nucleus size n* for that undercooling. Write the resulting (ΔT, n*) pairs to the output file.
- Output file: `/app/outputs/critical_nucleus_sizes.csv`
- Format: csv
- Contract: columns: undercooling_K (float), n_star (int). Rows: six data points corresponding to the specified undercoolings.
- Scoring: scored by hidden verifier

### Step 2: Derive solid-liquid interface energy
- Role: scored
- Action: From the critical nucleus sizes n* obtained in the previous step, compute n*^(1/3) and perform a linear fit of n*^(1/3) versus 1/ΔT. Determine the slope k. Then compute the solid-liquid interface energy σ using σ = (k * ΔHm) / (Tm * (32π/(3 Va))^(1/3)), with the given constants: atomic volume Va = 19.2×10⁻³⁰ m³, heat of fusion ΔHm = 3.37×10⁹ J/m³, and MD melting point Tm = 2689 K. Write the resulting σ as a single float (in J/m²) to the output file.
- Output file: `/app/outputs/interface_energy.txt`
- Format: txt
- Contract: plain text: a single float value
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_nucleus_sizes.csv`
- `/app/outputs/interface_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_nucleus_sizes.csv
- path: `/app/outputs/critical_nucleus_sizes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical nucleus size (number of atoms) at six specified undercoolings.
- schema:
  - `type`: table
  - `required_columns`: `undercooling_K`, `n_star`
  - `units`:
    - `undercooling_K`: K
    - `n_star`: atoms

### interface_energy.txt
- path: `/app/outputs/interface_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Average solid-liquid interface energy σ of Niobium.
- schema:
  - `type`: text
  - `description`: Single float, unit J/m²

Notes: The MD verification steps (melting point and liquid density) are omitted as they only validate the potential and are not required to reproduce the main headline; the EAM potential is publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_nucleus_sizes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "undercooling_K",
          "n_star"
        ],
        "units": {
          "undercooling_K": "K",
          "n_star": "atoms"
        }
      },
      "description": "Critical nucleus size (number of atoms) at six specified undercoolings."
    },
    {
      "file": "interface_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single float, unit J/m²"
      },
      "description": "Average solid-liquid interface energy σ of Niobium."
    }
  ],
  "notes": "The MD verification steps (melting point and liquid density) are omitted as they only validate the potential and are not required to reproduce the main headline; the EAM potential is publicly available."
}
```

## How you are scored
Your submission will be evaluated by an automatic verifier. The verifier scores each scored artifact independently by comparing it against hidden reference results and by checking that the σ value is consistent with the n* data you report. The final reward is a weighted combination of the scores for the two artifacts. Therefore, simply reporting the expected numbers without actually running the described MD workflow will not yield a high score.
