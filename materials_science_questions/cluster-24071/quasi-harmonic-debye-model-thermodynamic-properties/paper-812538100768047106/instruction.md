# Compute elastic constants, derived moduli and phonon frequencies for V3Co from first-principles DFT

## Problem background
Vanadium-based A15 intermetallic compounds V₃X (X = Fe, Co, Ni) are candidates for high‑temperature structural applications. Their suitability depends on mechanical properties (elastic constants, stiffness, hardness) and vibrational stability. First‑principles density‑functional theory (DFT) can predict these properties from the crystal structure alone. This task focuses on V₃Co and requires you to compute the elastic constants, derive key polycrystalline moduli and stability/ductility indicators, and determine the phonon frequencies at the Γ point. These quantities together characterise the mechanical and vibrational stability of the material.

## Approach
Use plane‑wave DFT with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and an open‑source plane‑wave code (e.g., Quantum ESPRESSO).

1. **Geometry optimisation** – Fully relax the atomic positions and the cell volume of V₃Co in the cubic A15 (Pm‑3n) structure, starting from the standard atomic coordinates and an initial lattice constant near 4.675 Å.
2. **Elastic constants via stress–strain** – Apply small, symmetry‑preserving strain deformations to the optimised cell. From the resulting stress tensors, extract the three independent cubic elastic constants C₁₁, C₁₂, C₄₄.
3. **Derived moduli and stability** – Compute the bulk modulus B = (C₁₁ + 2 C₁₂)/3, the Voigt and Reuss shear moduli G_V, G_R, their Hill average G, the B/G ratio, and the Cauchy pressure C_P = C₁₂ − C₄₄. Use Pugh’s ratio (B/G > 1.75) and positive C_P to assess ductility, and Born’s criteria to confirm mechanical stability.
4. **Phonon calculation** – Build a supercell (e.g., 2×2×2) and obtain the phonon dispersion either by the finite‑displacement (frozen‑phonon) method or by density‑functional perturbation theory (DFPT).
5. **Γ‑point phonon frequencies** – Extract the eight phonon frequencies at the Γ point; all must be positive (no imaginary modes) for vibrational stability.

All steps use the same PBE functional and public pseudopotentials for V and Co (the SSSP library is recommended).

## Reproduction target
Your task is to produce three machine‑readable artifacts that together capture the key mechanical and vibrational properties of V₃Co.

- **Elastic constants** – Report the three cubic constants C₁₁, C₁₂, C₄₄ (in GPa).
- **Derived moduli and stability verdicts** – From those constants, compute B, G, B/G, C_P, and the boolean flags `mechanical_stable` (all Born criteria satisfied) and `ductile` (B/G > 1.75 and C_P > 0).
- **Γ‑point phonon frequencies** – Provide the list of eight frequencies (in THz) and a flag `all_real` indicating that no imaginary modes appear (allowing a small numerical tolerance for noise).

All three artifacts must be written in the exact JSON format specified in the workflow steps, under `/app/outputs`.

## Assets

- V3Co crystal structure description (A15, Pm-3n)
- PBE pseudopotentials for V and Co: https://www.materialscloud.org/discover/sssp/table
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Geometry optimization of V3Co
- Role: process
- Action: Using an open-source plane-wave DFT code and PBE pseudopotentials, perform a full geometry optimization of V3Co in the A15 Pm-3n crystal structure. Start from the standard atomic positions and an initial lattice constant of approximately 4.675 Å. Relax both atomic positions and cell volume until forces and stress are below reasonable convergence thresholds.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Compute elastic constants
- Role: scored (load-bearing)
- Action: From the optimized structure, compute the three independent cubic elastic constants C11, C12, C44 (in GPa) for V3Co using a stress-strain approach. Apply small strain deformations and extract the stress tensor from DFT total-energy derivatives. Write the constants as a JSON object to the output file.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"type": "object", "properties": {"C11": {"type": "number", "description": "GPa"}, "C12": {"type": "number", "description": "GPa"}, "C44": {"type": "number", "description": "GPa"}}, "required": ["C11", "C12", "C44"]}
- Scoring: scored by hidden verifier

### Step 3: Derive polycrystalline moduli and check stability/ductility
- Role: scored
- Action: From the elastic constants C11, C12, C44, compute the bulk modulus B = (C11+2C12)/3, Voigt shear modulus G_V = (C11-C12+3C44)/5, Reuss shear modulus G_R = 5(C11-C12)C44/(C44+3(C11-C12)), averaged shear modulus G = (G_V+G_R)/2, B/G ratio, and Cauchy pressure C_P = C12−C44. Verify the Born mechanical stability criteria (C11−C12>0, C11+2C12>0, C44>0) and the Pugh ductility criterion (B/G>1.75 and C_P>0). Write the derived quantities and the boolean verdicts as a JSON object.
- Output file: `/app/outputs/derived_moduli.json`
- Format: json
- Contract: {"type": "object", "properties": {"B": {"type": "number", "description": "GPa"}, "G": {"type": "number", "description": "GPa"}, "B/G": {"type": "number"}, "C_P": {"type": "number", "description": "GPa"}, "mechanical_stable": {"type": "boolean"}, "ductile": {"type": "boolean"}}, "required": ["B", "G", "B/G", "C_P", "mechanical_stable", "ductile"]}
- Scoring: scored by hidden verifier

### Step 4: Phonon calculation for V3Co
- Role: process
- Action: Using the optimized structure, build a supercell (e.g., 2×2×2) and compute the phonon dispersion via a finite-displacement (frozen-phonon) approach or density-functional perturbation theory (DFPT). Obtain the phonon dispersion curves along high-symmetry lines and the phonon density of states. This step is computationally intensive and produces the raw data for gamma-point frequency extraction.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 5: Extract Gamma-point phonon frequencies
- Role: scored
- Action: From the phonon calculation results, extract the eight phonon frequencies (in THz) at the Gamma (Γ) point. Verify that all frequencies are positive (allowing a small tolerance of -0.1 THz for numerical noise) and set a boolean flag all_real accordingly. Write the frequency list and the flag as a JSON object.
- Output file: `/app/outputs/phonon_gamma_frequencies.json`
- Format: json
- Contract: {"type": "object", "properties": {"frequencies_THz": {"type": "array", "items": {"type": "number"}, "minItems": 8, "maxItems": 8, "description": "phonon frequencies in THz"}, "all_real": {"type": "boolean"}}, "required": ["frequencies_THz", "all_real"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/derived_moduli.json`
- `/app/outputs/phonon_gamma_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The three independent cubic elastic constants for V3Co in units of GPa.
- schema:
  - `type`: object
  - `properties`:
    - `C11`:
      - `type`: number
      - `description`: GPa
    - `C12`:
      - `type`: number
      - `description`: GPa
    - `C44`:
      - `type`: number
      - `description`: GPa
  - `required`: `C11`, `C12`, `C44`

### derived_moduli.json
- path: `/app/outputs/derived_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Voigt-Reuss-Hill averaged bulk and shear moduli, B/G ratio, Cauchy pressure, and mechanical stability/ductility verdicts.
- schema:
  - `type`: object
  - `properties`:
    - `B`:
      - `type`: number
      - `description`: GPa
    - `G`:
      - `type`: number
      - `description`: GPa
    - `B/G`:
      - `type`: number
    - `C_P`:
      - `type`: number
      - `description`: GPa
    - `mechanical_stable`:
      - `type`: boolean
    - `ductile`:
      - `type`: boolean
  - `required`: `B`, `G`, `B/G`, `C_P`, `mechanical_stable`, `ductile`

### phonon_gamma_frequencies.json
- path: `/app/outputs/phonon_gamma_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Eight Gamma-point phonon frequencies for V3Co and a flag indicating vibrational stability (no imaginary modes).
- schema:
  - `type`: object
  - `properties`:
    - `frequencies_THz`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 8
      - `maxItems`: 8
      - `description`: phonon frequencies at the Gamma point in THz
    - `all_real`:
      - `type`: boolean
  - `required`: `frequencies_THz`, `all_real`

Notes: All output artifacts are scored against paper-reported values for V3Co (hidden gold) using appropriate tolerances. The derived_moduli are expected to be consistent with the submitted elastic constants; the checker will recompute them and compare.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "C11": {
            "type": "number",
            "description": "GPa"
          },
          "C12": {
            "type": "number",
            "description": "GPa"
          },
          "C44": {
            "type": "number",
            "description": "GPa"
          }
        },
        "required": [
          "C11",
          "C12",
          "C44"
        ]
      },
      "description": "The three independent cubic elastic constants for V3Co in units of GPa."
    },
    {
      "file": "derived_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "B": {
            "type": "number",
            "description": "GPa"
          },
          "G": {
            "type": "number",
            "description": "GPa"
          },
          "B/G": {
            "type": "number"
          },
          "C_P": {
            "type": "number",
            "description": "GPa"
          },
          "mechanical_stable": {
            "type": "boolean"
          },
          "ductile": {
            "type": "boolean"
          }
        },
        "required": [
          "B",
          "G",
          "B/G",
          "C_P",
          "mechanical_stable",
          "ductile"
        ]
      },
      "description": "Voigt-Reuss-Hill averaged bulk and shear moduli, B/G ratio, Cauchy pressure, and mechanical stability/ductility verdicts."
    },
    {
      "file": "phonon_gamma_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "frequencies_THz": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 8,
            "maxItems": 8,
            "description": "phonon frequencies at the Gamma point in THz"
          },
          "all_real": {
            "type": "boolean"
          }
        },
        "required": [
          "frequencies_THz",
          "all_real"
        ]
      },
      "description": "Eight Gamma-point phonon frequencies for V3Co and a flag indicating vibrational stability (no imaginary modes)."
    }
  ],
  "notes": "All output artifacts are scored against paper-reported values for V3Co (hidden gold) using appropriate tolerances. The derived_moduli are expected to be consistent with the submitted elastic constants; the checker will recompute them and compare."
}
```

## How you are scored
A hidden verifier independently scores each of the three output files. It compares your reported values against a reference set (derived from the same computational protocol), verifies the internal consistency between your elastic constants and derived moduli, and checks the phonon frequencies for positivity and agreement with the reference. Each artifact carries a share of the total reward; the final score is the weighted sum. Partial credit is awarded for results that are close but not exact. Simply reporting the correct numbers without the required computation pipeline will not satisfy the process steps.
