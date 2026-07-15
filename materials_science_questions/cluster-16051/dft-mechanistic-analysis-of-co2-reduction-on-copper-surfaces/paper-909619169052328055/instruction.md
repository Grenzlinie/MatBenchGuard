# DFT Free Energy Calculations for CO2 Reduction Intermediates on Sulfur-Modified Copper Surfaces

## Problem background
Electrochemical CO2 reduction (CO2RR) on copper-based catalysts is known to produce a range of products including CO, formate, and multicarbon species. Introducing sulfur into copper catalysts has been observed to strongly shift the product distribution toward formate, but the mechanistic origin of this selectivity change remains an open question. One way to investigate the reaction mechanism is through first‑principles thermodynamics: mapping the free‑energy landscape of reaction intermediates on chemically different catalyst surfaces. Here we focus on the computational modelling of CO2RR intermediates on metallic Cu(111) and on a model surface where sulfur is adsorbed on Cu(111).

## Approach
Density functional theory (DFT) calculations will be used to compute the total energies of key CO2RR intermediates adsorbed on two surfaces: a clean Cu(111) slab and an S-adsorbed Cu(111) slab at a S coverage of 1/2 monolayer. The intermediates considered include *CO2, *OCHO (the intermediate frequently linked to formate production), *COOH (the intermediate associated with CO production), and *H (a descriptor of the competing hydrogen evolution reaction). After determining the total energies, standard zero‑point energy and entropy corrections from published thermochemical tables will be applied to obtain Gibbs free energies at the reference conditions of 298 K, pH = 0, and an applied potential of 0 V vs. RHE. The resulting free energies on the two surfaces will be compared to understand how surface sulfur influences the relative stability of the different reaction intermediates.

## Reproduction target
Compute the Gibbs free energies (in eV) of the intermediates *OCHO, *COOH, and *H adsorbed on Cu(111) and on S-adsorbed Cu(111), under the conditions 298 K, pH 0, and 0 V vs. RHE. Report these values in the JSON file `/app/outputs/free_energies.json` according to the schema specified in the output contract. All required inputs are publicly available: the crystal structure of copper, standard DFT protocols, and the thermochemical correction data commonly used in the electrocatalysis literature.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Standard thermochemical correction tables (Norskov et al.)

## Workflow steps

### Step 1: Build Surface Models
- Role: process
- Action: Construct a 3x3 Cu(111) slab (4 layers, 15 Å vacuum) and an S-adsorbed Cu(111) model with 1/2 monolayer S coverage. Prepare input geometries for DFT.
- Evidence: none

### Step 2: DFT Total Energy Calculations
- Role: process
- Action: Perform DFT geometry optimizations for *CO2, *OCHO, *COOH, *H (and optionally *CO) on both surfaces using an open-source plane-wave DFT code with appropriate pseudopotentials and dispersion correction, and extract total energies.
- Evidence: none

### Step 3: Compute Gibbs Free Energies and Report
- Role: scored (load-bearing)
- Action: Apply zero-point energy and entropy corrections from standard thermochemical tables to the DFT total energies to obtain Gibbs free energies at 298 K, pH=0, U=0 V vs RHE. Compile free energies for *OCHO, *COOH, *H (and optionally *CO2, *CO) on both surfaces into a JSON file.
- Output file: `/app/outputs/free_energies.json`
- Format: json
- Contract: Array of objects: {"surface": string ("Cu(111)" or "S-adsorbed Cu(111)"), "intermediate": string (e.g., "*OCHO", "*COOH", "*H"), "free_energy_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energies.json
- path: `/app/outputs/free_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed Gibbs free energies (eV) for key intermediates on both surfaces. The checker compares each value to a hidden paper-reported gold within tolerance and verifies three relative trends: free_energy(*OCHO) on S-adsorbed Cu < free_energy(*OCHO) on Cu; free_energy(*COOH) on S-adsorbed Cu > free_energy(*COOH) on Cu; free_energy(*H) on S-adsorbed Cu > free_energy(*H) on Cu.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `surface`, `intermediate`, `free_energy_eV`
    - `properties`:
      - `surface`:
        - `type`: string
        - `enum`: `Cu(111)`, `S-adsorbed Cu(111)`
      - `intermediate`:
        - `type`: string
      - `free_energy_eV`:
        - `type`: number

Notes: The trends are derived from the paper's conclusion that S adsorption favors *OCHO and disfavors *COOH and *H. Scoring uses absolute-value tolerance for individual energies and boolean trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "surface",
            "intermediate",
            "free_energy_eV"
          ],
          "properties": {
            "surface": {
              "type": "string",
              "enum": [
                "Cu(111)",
                "S-adsorbed Cu(111)"
              ]
            },
            "intermediate": {
              "type": "string"
            },
            "free_energy_eV": {
              "type": "number"
            }
          }
        }
      },
      "description": "Computed Gibbs free energies (eV) for key intermediates on both surfaces. The checker compares each value to a hidden paper-reported gold within tolerance and verifies three relative trends: free_energy(*OCHO) on S-adsorbed Cu < free_energy(*OCHO) on Cu; free_energy(*COOH) on S-adsorbed Cu > free_energy(*COOH) on Cu; free_energy(*H) on S-adsorbed Cu > free_energy(*H) on Cu."
    }
  ],
  "notes": "The trends are derived from the paper's conclusion that S adsorption favors *OCHO and disfavors *COOH and *H. Scoring uses absolute-value tolerance for individual energies and boolean trend checks."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/free_energies.json` file and evaluate it against a set of reference values. The evaluation checks both the absolute free-energy values for each intermediate and surface, and the direction of three relative trends: the difference in free energy of *OCHO between the two surfaces, the difference in free energy of *COOH, and the difference in free energy of *H. Your overall score is a weighted combination of these checks. Successfully running the full computational workflow and producing physically meaningful numbers is required; simply guessing values is unlikely to satisfy the tolerance criteria used by the verifier.
