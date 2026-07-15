# Ag-Ru Prototype Elastic and Vibrational Stability Reproduction

## Problem background
In an equilibrium immiscible Ag-Ru binary metal system, nonequilibrium crystalline phases can be formed under far-from-equilibrium processing conditions. The structural stability of these hypothetical phases is crucial for understanding the role of chemical bonding in overcoming the positive heat of formation. In this task, you will investigate the mechanical and vibrational stability of six hypothetical Ag-Ru crystalline structures: Ag₃Ru and AgRu₃ in D0₃ (bcc), L1₂ (fcc), and D0₁₉ (hcp) prototypes. You will compute elastic constants and phonon spectra using first-principles density-functional theory (DFT) to determine which of these phases can be metastable.

## Approach
You will perform first-principles DFT calculations using the open-source Quantum ESPRESSO package with standard GGA-PBE pseudopotentials for Ag and Ru. For each of the six crystal structures, first carry out a full geometry optimization to relax the atomic positions and lattice parameters. From the optimized structures, compute the second-order elastic stiffness constants (C11, C12, C44, and for the hexagonal D0₁₉ prototype also C13 and C33). For cubic prototypes, the mechanical stability criterion is the shear constant C′ = (C11 − C12)/2; a positive C′ indicates stability against pure shear deformation. Separately, calculate the phonon dispersion relations for each structure along high-symmetry directions in the Brillouin zone and check for the presence of any imaginary (negative) phonon frequencies, which signal vibrational instability. The combination of elastic and vibrational criteria yields a classification of metastability for each phase.

## Reproduction target
Your task is to produce two scored artifacts:

1. A CSV file, `elastic_constants.csv`, containing the computed elastic stiffness constants (in GPa) and the derived C′ for all six structures. Columns: `stoichiometry`, `prototype`, `C11`, `C12`, `C13`, `C33`, `C44`, `C_prime`. For cubic prototypes, set `C13` and `C33` to `NA`. The shear constant `C_prime` must be (C11−C12)/2 for cubic structures; for D0₁₉, provide it only if your calculation directly yields it, but you must report the full set of elastic constants needed to assess mechanical stability.

2. A JSON file, `phonon_stability.json`, with an array of objects: `{"stoichiometry": "Ag3Ru", "prototype": "D03", "has_imaginary_frequencies": true}` for all six structures. For each, indicate whether the calculated phonon dispersion contains any imaginary frequency anywhere in the Brillouin zone.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- Ag pseudopotential (4d¹⁰ 5s¹): https://www.materialscloud.org/discover/sssp/table
- Ru pseudopotential (4s² 4p⁶ 4d⁷ 5s¹): https://www.materialscloud.org/discover/sssp/table
- TB-SMA potential parameters (Li et al., J. Phys. Chem. B 108, 16071, 2004): 10.1021/jp048048x

## Workflow steps

### Step 1: Generate initial crystal structures
- Role: process
- Action: Create the initial atomic geometries for Ag3Ru and AgRu3 in D03, L12, and D019 prototypes (six structures) with approximate lattice parameters. This produces the structural input files for DFT.
- Evidence: none

### Step 2: DFT geometry optimization and elastic constants calculation
- Role: process
- Action: For each structure, perform DFT geometry optimization using Quantum ESPRESSO with GGA-PBE pseudopotentials, plane‑wave cutoff ~330 eV, and a suitable k‑point mesh. Then compute the elastic stiffness constants (C11, C12, C44, C13, C33) using the stress‑strain or energy‑strain method.
- Evidence: `/app/outputs/elastic_calc.log`

### Step 3: DFT phonon spectrum calculation
- Role: process
- Action: For each structure, compute the phonon dispersion using density-functional perturbation theory (ph.x) or the finite-displacement method, checking for any negative/imaginary phonon frequencies.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 4: Compile elastic constants and shear stability metric
- Role: scored
- Action: Assemble the computed elastic constants for all six structures. For cubic prototypes compute the shear stability metric C' = (C11 - C12)/2. Write the results to elastic_constants.csv.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: Columns: stoichiometry (string, e.g., 'Ag3Ru'), prototype (string, one of 'D03','L12','D019'), C11 (float, GPa), C12 (float), C13 (float or 'NA'), C33 (float or 'NA'), C44 (float), C_prime (float). One row per structure.
- Scoring: scored by hidden verifier

### Step 5: Classify vibrational stability
- Role: scored
- Action: From the phonon calculation, determine for each structure whether any imaginary phonon frequency exists. Record the boolean verdict in phonon_stability.json.
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: Array of objects: {'stoichiometry': 'Ag3Ru', 'prototype': 'D03', 'has_imaginary_frequencies': true|false}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/phonon_stability.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed elastic stiffness constants and the derived shear stability parameter C' for six Ag-Ru prototypes. The checker verifies sign and magnitude of C' against the paper's reference values.
- schema:
  - `type`: table
  - `required_columns`: `stoichiometry`, `prototype`, `C11`, `C12`, `C13`, `C33`, `C44`, `C_prime`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C_prime`: GPa

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Per‑structure boolean indicating the presence of imaginary phonon frequencies. The checker expects exact agreement with the paper's reported classification.
- schema:
  - `type`: array
  - `items`:
    - `stoichiometry`: string
    - `prototype`: string
    - `has_imaginary_frequencies`: boolean

Notes: The workflow uses open-source DFT (Quantum ESPRESSO, GGA-PBE pseudopotentials) and does not depend on any proprietary code or private data. The output elastic constants are expected to differ slightly from the paper's CASTEP values; the scorer tolerates reasonable method-dependent spread while requiring correct mechanical stability trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stoichiometry",
          "prototype",
          "C11",
          "C12",
          "C13",
          "C33",
          "C44",
          "C_prime"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C_prime": "GPa"
        }
      },
      "description": "Computed elastic stiffness constants and the derived shear stability parameter C' for six Ag-Ru prototypes. The checker verifies sign and magnitude of C' against the paper's reference values."
    },
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "stoichiometry": "string",
          "prototype": "string",
          "has_imaginary_frequencies": "boolean"
        }
      },
      "description": "Per‑structure boolean indicating the presence of imaginary phonon frequencies. The checker expects exact agreement with the paper's reported classification."
    }
  ],
  "notes": "The workflow uses open-source DFT (Quantum ESPRESSO, GGA-PBE pseudopotentials) and does not depend on any proprietary code or private data. The output elastic constants are expected to differ slightly from the paper's CASTEP values; the scorer tolerates reasonable method-dependent spread while requiring correct mechanical stability trends."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier against hidden reference criteria. The verifier will:
- Parse `elastic_constants.csv` and check that the reported elastic constants are internally consistent and that the sign and relative magnitude of C′ across prototypes follow the expected mechanical stability trends derived from a correct DFT calculation at the specified level of theory. It does not compare to a single fixed number but judges whether your results reproduce the correct pattern of stability or instability.
- Parse `phonon_stability.json` and compare your boolean flags for each structure against the correct classification. A well-converged DFT phonon calculation at this level of theory yields a deterministic result for the presence of imaginary frequencies, so an exact match to the reference is expected.
Each scored file contributes a share to the total reward. Merely copying numbers from an external source without performing the required DFT calculations will not pass because the verifier checks consistency with the physics of the chosen computational setup.
