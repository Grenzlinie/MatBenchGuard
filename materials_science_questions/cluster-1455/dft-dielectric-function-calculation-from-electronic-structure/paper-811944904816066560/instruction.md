# Elastic Constants and Dielectric Function of Al3Sc from DFT

## Problem background
The Al3Sc intermetallic compound is a critical strengthening precipitate in scandium-containing aluminum alloys, contributing to high-temperature strength and microstructural stability. Understanding its elastic and optical properties is essential for alloy design and performance prediction. This task addresses the determination of the elastic stiffness constants, bulk modulus, Poisson's ratio, and the frequency-dependent dielectric function of cubic L12 Al3Sc using first-principles density functional theory calculations.

## Approach
The computational approach uses plane-wave density functional theory (DFT) within the generalized gradient approximation (GGA) using the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and ultrasoft pseudopotentials. The workflow begins with a full geometry relaxation of the L12 Al3Sc crystal to obtain the equilibrium lattice parameter and atomic positions. Using the relaxed structure, a series of small homogeneous strains is applied, and the resulting stress tensor is computed via DFT. The linear stress–strain relationship is then fitted to extract the three independent elastic constants of the cubic system, C11, C12, and C44. From these, the bulk modulus B0 = (C11+2C12)/3 and Poisson's ratio ν (via the compliance matrix) are derived. The optical response is computed by evaluating the complex frequency-dependent dielectric function ε(ω) = ε1(ω) + i ε2(ω) using the momentum matrix elements and the Ehrenreich–Cohen formalism. The real (ε1) and imaginary (ε2) parts are obtained over a photon energy range from 0 to 40 eV.

## Reproduction target
Produce two output artifacts:
1. A JSON file containing the elastic stiffness constants C11, C12, C44 (in GPa), the bulk modulus B0 (in GPa), and Poisson's ratio ν (dimensionless) for the relaxed Al3Sc crystal.
2. A comma-separated value (CSV) file containing three columns: energy (eV), epsilon1 (real part of dielectric function), and epsilon2 (imaginary part of dielectric function), covering photon energies from 0 to 40 eV.

## Assets

- Quantum ESPRESSO (or equivalent plane-wave DFT code): https://www.quantum-espresso.org
- PBE ultrasoft pseudopotentials for Al and Sc: https://www.materialscloud.org/discover/sssp/table/efficiency
- Al3Sc L12 crystal structure

## Workflow steps

### Step 1: Geometry relaxation
- Role: process
- Action: Perform full geometry optimization (cell volume and atomic positions) of cubic L12 Al3Sc using DFT with PBE GGA and ultrasoft pseudopotentials to obtain the relaxed structure.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Elastic constants and derived moduli
- Role: scored (load-bearing)
- Action: Apply small homogeneous strains to the relaxed cell, compute the stress tensor via DFT, and fit the linear stress–strain relation to extract C11, C12, C44. Compute bulk modulus B0 = (C11+2C12)/3 and Poisson's ratio ν from the compliance matrix. Write all five values as a JSON file.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"C11": float, "C12": float, "C44": float, "B0": float, "v": float}
- Scoring: scored by hidden verifier

### Step 3: Dielectric function
- Role: scored
- Action: Compute the frequency-dependent complex dielectric function from the electronic structure using momentum matrix elements and the Ehrenreich–Cohen formalism. Output ε1(ω) and ε2(ω) as CSV for photon energies from 0 to 40 eV.
- Output file: `/app/outputs/dielectric_function.csv`
- Format: csv
- Contract: columns: 'energy (eV)', 'epsilon1', 'epsilon2' (energy in eV, epsilon1 and epsilon2 dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic stiffness constants C11, C12, C44, bulk modulus B0, and Poisson's ratio v of cubic Al3Sc. All C values in GPa, v dimensionless.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (GPa)
    - `C12`: float (GPa)
    - `C44`: float (GPa)
    - `B0`: float (GPa)
    - `v`: float (dimensionless)

### dielectric_function.csv
- path: `/app/outputs/dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Frequency-dependent dielectric function: real part epsilon1 and imaginary part epsilon2 vs photon energy (eV). Energy range 0–40 eV. Structural check verifies absorption peaks in epsilon2.
- schema:
  - `type`: table
  - `required_columns`: `energy (eV)`, `epsilon1`, `epsilon2`
  - `units`:
    - `energy (eV)`: eV
    - `epsilon1`: dimensionless
    - `epsilon2`: dimensionless

Notes: The partial density of states (PDOS) analysis is omitted from the scored pipeline as it is not a headline quantitative result.

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
        "required": {
          "C11": "float (GPa)",
          "C12": "float (GPa)",
          "C44": "float (GPa)",
          "B0": "float (GPa)",
          "v": "float (dimensionless)"
        }
      },
      "description": "Elastic stiffness constants C11, C12, C44, bulk modulus B0, and Poisson's ratio v of cubic Al3Sc. All C values in GPa, v dimensionless."
    },
    {
      "file": "dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy (eV)",
          "epsilon1",
          "epsilon2"
        ],
        "units": {
          "energy (eV)": "eV",
          "epsilon1": "dimensionless",
          "epsilon2": "dimensionless"
        }
      },
      "description": "Frequency-dependent dielectric function: real part epsilon1 and imaginary part epsilon2 vs photon energy (eV). Energy range 0–40 eV. Structural check verifies absorption peaks in epsilon2."
    }
  ],
  "notes": "The partial density of states (PDOS) analysis is omitted from the scored pipeline as it is not a headline quantitative result."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores each required artifact.
- The elastic constants JSON is compared to a hidden reference value using a predefined tolerance; a high reward is given if your computed values lie within the acceptable range, and the reward decreases as deviations grow.
- The dielectric function CSV is checked for structural features (e.g., the presence and location of characteristic absorption peaks) that are physically expected for this material.
Each artifact carries a weight, and the final overall score (a float between 0 and 1) is the weighted sum of the individual scores. The verifier does not reveal the reference values or the exact tolerance; you must compute the properties accurately from the described first-principles workflow.
