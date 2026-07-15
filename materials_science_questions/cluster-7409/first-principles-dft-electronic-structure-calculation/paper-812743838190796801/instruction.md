# DFT structural and electronic properties of doped ZrN systems

## Problem background
Metallic nitrides such as ZrN are hard, wear-resistant ceramics used in protective coatings and high-temperature applications. Substitutionally doping ZrN with Ti or C modifies crystal structure and electronic properties, offering a route to tailor material performance. First-principles density functional theory (DFT) provides a direct way to compute relaxed lattice parameters, symmetries, and electronic structure for a family of doped compounds, enabling a systematic comparison of how different dopant concentrations affect geometric and electronic properties. This task reproduces those calculations for a series of Ti- and C-doped ZrN compositions.

## Approach
Use plane-wave DFT within the generalized gradient approximation (GGA-PBE). Build initial structures by substituting atoms in the cubic ZrN unit cell to create the target compositions. Perform variable-cell geometry optimization to relax all atomic positions and lattice parameters. From the relaxed structures, compute the electronic density of states with a denser k-point grid and extract the total DOS at the Fermi level. Finally, run total-energy calculations at several volumes around equilibrium and fit an equation of state to obtain the bulk modulus for each composition. The method does not require any external pre-trained model or dataset; all inputs are derived from the defined crystal structures and the specified pseudopotentials.

## Reproduction target
Compute the following properties for the nine compositions: ZrN, TiZr3N4, TiZrN2, Ti3ZrN4, TiN, Zr4CN3, Zr2CN, Zr4C3N, and ZrC. For each composition, report the fully relaxed lattice constants (a, b, c in Å) and the space group symbol in `relaxed_structures.json`. Extract the total density of states at the Fermi level (electrons/eV) into `dos_fermi.json`. Determine the bulk modulus (GPa) by fitting an equation of state to energy-volume data and write the results to `bulk_moduli.json`. The precise workflow is detailed in the steps below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build initial crystal structures
- Role: process
- Action: Construct initial crystal structures for all nine compositions: ZrN, TiZr3N4, TiZrN2, Ti3ZrN4, TiN, Zr4CN3, Zr2CN, Zr4C3N, and ZrC, starting from the cubic ZrN (Fm-3m, a≈4.6176 Å) unit cell with appropriate atom substitutions. Save the structures in a standard DFT input format (e.g., Quantum ESPRESSO input files).
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: For each composition, perform DFT geometry optimization using Quantum ESPRESSO: relax atomic positions and cell parameters with the GGA-PBE functional, ultrasoft pseudopotentials, and appropriate k-point sampling. Save the fully relaxed structures.
- Evidence: none

### Step 3: Export relaxed lattice parameters and space groups
- Role: scored
- Action: From the relaxed structures, extract the lattice parameters (a, b, c in Å) and space group for each composition and write them to a JSON file.
- Output file: `/app/outputs/relaxed_structures.json`
- Format: json
- Contract: Object mapping each composition name (ZrN, TiZr3N4, TiZrN2, Ti3ZrN4, TiN, Zr4CN3, Zr2CN, Zr4C3N, ZrC) to an object with keys a, b, c (float, lattice parameters in Å) and space_group (string).
- Scoring: scored by hidden verifier

### Step 4: Electronic structure calculation (DOS)
- Role: process
- Action: For each relaxed composition, run a DFT single-point calculation with a denser k-point mesh to obtain the electronic density of states (DOS). Save the raw DOS data.
- Evidence: none

### Step 5: Extract DOS at Fermi level
- Role: scored
- Action: From the computed DOS data, extract the total density of states at the Fermi level (in electrons/eV) for each composition and write to a JSON file.
- Output file: `/app/outputs/dos_fermi.json`
- Format: json
- Contract: Object mapping each composition name to a float (electrons/eV).
- Scoring: scored by hidden verifier

### Step 6: Bulk modulus via equation of state
- Role: process
- Action: For each relaxed composition, perform a set of DFT total-energy calculations at several cell volumes (around equilibrium) and fit the energy-volume data to an equation of state to obtain the bulk modulus. Save the fitting results.
- Evidence: none

### Step 7: Export bulk moduli
- Role: scored (load-bearing)
- Action: For each composition, write the computed bulk modulus (in GPa) to a JSON file.
- Output file: `/app/outputs/bulk_moduli.json`
- Format: json
- Contract: Object mapping each composition name to a float (GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_structures.json`
- `/app/outputs/dos_fermi.json`
- `/app/outputs/bulk_moduli.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_structures.json
- path: `/app/outputs/relaxed_structures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice parameters (a,b,c in Å) and space group for all nine compositions.
- schema:
  - `type`: object
  - `required`:
    - `ZrN`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `TiZr3N4`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `TiZrN2`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `Ti3ZrN4`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `TiN`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `Zr4CN3`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `Zr2CN`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `Zr4C3N`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string
    - `ZrC`:
      - `a`: number
      - `b`: number
      - `c`: number
      - `space_group`: string

### dos_fermi.json
- path: `/app/outputs/dos_fermi.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total density of states at the Fermi level (electrons/eV) for each composition.
- schema:
  - `type`: object
  - `required`:
    - `ZrN`: number
    - `TiZr3N4`: number
    - `TiZrN2`: number
    - `Ti3ZrN4`: number
    - `TiN`: number
    - `Zr4CN3`: number
    - `Zr2CN`: number
    - `Zr4C3N`: number
    - `ZrC`: number

### bulk_moduli.json
- path: `/app/outputs/bulk_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bulk modulus (GPa) for each composition.
- schema:
  - `type`: object
  - `required`:
    - `ZrN`: number
    - `TiZr3N4`: number
    - `TiZrN2`: number
    - `Ti3ZrN4`: number
    - `TiN`: number
    - `Zr4CN3`: number
    - `Zr2CN`: number
    - `Zr4C3N`: number
    - `ZrC`: number

Notes: Hardness calculation is omitted because the paper's microscopic hardness model is not sufficiently specified for reproduction. The three scored outputs cover the paper's main structural and electronic claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_structures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ZrN": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "TiZr3N4": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "TiZrN2": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "Ti3ZrN4": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "TiN": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "Zr4CN3": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "Zr2CN": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "Zr4C3N": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          },
          "ZrC": {
            "a": "number",
            "b": "number",
            "c": "number",
            "space_group": "string"
          }
        }
      },
      "description": "Relaxed lattice parameters (a,b,c in Å) and space group for all nine compositions."
    },
    {
      "file": "dos_fermi.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ZrN": "number",
          "TiZr3N4": "number",
          "TiZrN2": "number",
          "Ti3ZrN4": "number",
          "TiN": "number",
          "Zr4CN3": "number",
          "Zr2CN": "number",
          "Zr4C3N": "number",
          "ZrC": "number"
        }
      },
      "description": "Total density of states at the Fermi level (electrons/eV) for each composition."
    },
    {
      "file": "bulk_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ZrN": "number",
          "TiZr3N4": "number",
          "TiZrN2": "number",
          "Ti3ZrN4": "number",
          "TiN": "number",
          "Zr4CN3": "number",
          "Zr2CN": "number",
          "Zr4C3N": "number",
          "ZrC": "number"
        }
      },
      "description": "Bulk modulus (GPa) for each composition."
    }
  ],
  "notes": "Hardness calculation is omitted because the paper's microscopic hardness model is not sufficiently specified for reproduction. The three scored outputs cover the paper's main structural and electronic claims."
}
```

## How you are scored
A hidden verifier will read your three JSON output files and compare your reported values for each composition against expected reference values. Correct lattice parameters, space group, DOS at the Fermi level, and bulk modulus each contribute to the score. The final reward is proportional to the number of compositions that meet all comparison criteria, weighted across the three output files. Simply printing the values from the paper is insufficient; you must actually perform the DFT calculations to produce genuine results.
