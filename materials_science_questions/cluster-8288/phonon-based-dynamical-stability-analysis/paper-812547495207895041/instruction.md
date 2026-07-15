# Ferroelectric Polarization and Soft-Mode Projection in Monolayer As2S3

## Problem background
Two-dimensional materials that break inversion symmetry can display ferroelectricity and piezoelectricity, making them promising for atomically thin functional devices. Monolayer orpiment (As2S3) has recently been isolated and is a candidate intrinsic ferroelectric. Its polar phase (space group Pmn2₁) is believed to originate from a high-symmetry reference structure (space group Pmmn) via a single soft phonon mode. This task reproduces the first-principles evidence: you will compute the spontaneous electric polarization of monolayer As2S3 in the Pmn2₁ phase and quantify how much the structural distortion from Pmmn to Pmn2₁ is governed by the soft B2u zone-center phonon mode.

## Approach
Use plane-wave density functional theory (DFT) as implemented in Quantum ESPRESSO with the Perdew–Burke–Ernzerhof (PBE) functional and norm-conserving pseudopotentials from the SSSP library. Build the monolayer Pmn2₁ crystal structure from the bulk orpiment lattice parameters, and construct the higher-symmetry Pmmn reference by symmetrization. Relax both structures to obtain their ground-state geometries. For the relaxed Pmmn structure, perform density-functional perturbation theory (DFPT) at the Γ point to obtain phonon eigenvectors; identify the soft B2u mode. For the relaxed Pmn2₁ structure, compute the spontaneous polarization along the x-axis using the Berry-phase method. Finally, calculate the atomic displacement vector ΔR between the relaxed Pmmn and Pmn2₁ positions and project it onto the normalized B2u eigenvector to obtain the overlap fraction η, which measures the dominance of that mode in the ferroelectric distortion.

## Reproduction target
For monolayer As2S3, determine the spontaneous electric polarization P (in pC/m, along the x-axis) of the relaxed Pmn2₁ ferroelectric phase, and compute the projection fraction η of the atomic displacement from the high-symmetry Pmmn phase onto the soft B2u phonon mode. Report both quantities in the scored output file `/app/outputs/results.json`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials library: https://www.materialscloud.org/discover/sssp/table/precision
- Bulk orpiment crystal structure (As2S3)

## Workflow steps

### Step 1: DFT relaxation of Pmn2₁ and Pmmn structures
- Role: process
- Action: Build initial monolayer As2S3 structures in the polar Pmn2₁ and high-symmetry Pmmn phases from the bulk orpiment crystal structure. Perform DFT structural relaxation of both phases using the PBE functional in Quantum ESPRESSO, yielding optimized atomic coordinates and cell parameters.
- Evidence: `/app/outputs/relaxed_structures.xyz`

### Step 2: Phonon calculation on Pmmn structure
- Role: process
- Action: Perform a density-functional perturbation theory (DFPT) phonon calculation on the relaxed Pmmn structure at the Γ point using Quantum ESPRESSO. Extract the normalized eigenvectors of all zone‑center soft phonon modes, in particular the B2u mode.
- Evidence: `/app/outputs/phonon_eigenvectors.npy`

### Step 3: Spontaneous polarization calculation
- Role: process
- Action: Using the relaxed Pmn2₁ structure, compute the spontaneous electric polarization along the x‑axis via the Berry‑phase method in Quantum ESPRESSO.
- Evidence: `/app/outputs/polarization.txt`

### Step 4: Soft-mode projection and final results
- Role: scored (load-bearing)
- Action: Compute the atomic displacement vector ΔR between the relaxed Pmmn and Pmn2₁ structures. Project ΔR onto the normalized B2u eigenvector to obtain the overlap fraction η(B2u). Compile η(B2u) and the spontaneous polarization from step s3 into a single JSON artifact results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: eta_B2u (float, unitless), polarization (float, in pC/m). Example: {"eta_B2u": 0.86, "polarization": 71.0}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the soft-mode projection η onto B2u mode, the spontaneous electric polarization, and the piezoelectric strain coefficients d11 and d12.
- schema:
  - `type`: object
  - `required`:
    - `eta_B2u`: float
    - `polarization`: float
    - `d11`: float
    - `d12`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `eta_B2u`: unitless
    - `polarization`: pC/m
    - `d11`: pm/V
    - `d12`: pm/V

Notes: The exact_match policy compares the reported values to hidden paper-derived reference numbers within hidden tolerances. All quantities are fixed deterministic results of the specified DFT workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "eta_B2u": "float",
          "polarization": "float",
          "d11": "float",
          "d12": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "eta_B2u": "unitless",
          "polarization": "pC/m",
          "d11": "pm/V",
          "d12": "pm/V"
        }
      },
      "description": "Scored artifact containing the soft-mode projection η onto B2u mode, the spontaneous electric polarization, and the piezoelectric strain coefficients d11 and d12."
    }
  ],
  "notes": "The exact_match policy compares the reported values to hidden paper-derived reference numbers within hidden tolerances. All quantities are fixed deterministic results of the specified DFT workflow."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/results.json` and compares the reported `eta_B2u` and `polarization` to reference values with appropriate tolerances. The tolerances absorb typical DFT code/functional variations while excluding random or guessed values. Each quantity is scored independently; the final score is a weighted sum. Providing correct numbers without executing the required relaxation, DFPT, and Berry-phase calculations will not satisfy the tolerances. The verifier does not re-run DFT itself; it solely checks your submitted artifacts.
