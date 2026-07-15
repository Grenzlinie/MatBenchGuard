# Compute OVGF/TZVP vertical ionization energies for bicyclo[2.2.2]octa-2,5-dione

## Problem background
Bicyclo[2.2.2]octa-2,5-dione (BCOD) is a strained bridged cyclic diketone. Understanding its valence electronic structure is important for characterizing through-bond and through-space interactions that influence the ordering and character of molecular orbitals. Quantum chemical calculations, such as the outer-valence Green's function (OVGF) method, provide vertical ionization energies that serve as benchmarks for interpreting experimental spectra and assigning orbital symmetries. This task focuses on computing those energies to evaluate the electronic structure of BCOD.

## Approach
The workflow first optimizes the molecular geometry of BCOD using density functional theory at the B3LYP/TZVP level. Using this optimized structure, vertical ionization energies are then computed with a propagator method: either the outer-valence Green's function method with the TZVP basis set (OVGF/TZVP) or, if OVGF is unavailable, the third-order algebraic diagrammatic construction method with the cc-pVDZ basis set (ADC(3)/cc-pVDZ). The energies are extracted for the 18 outer-valence molecular orbitals labelled by their symmetry (a/b). A JSON file records each orbital's label, ionization energy, and the method used.

## Reproduction target
Compute the vertical ionization energies (in eV) for the 18 outer-valence molecular orbitals of BCOD using the OVGF/TZVP method (or ADC(3)/cc-pVDZ as a fallback). The required orbital labels are: 14a, 13b, 12b, 13a, 12a, 11a, 10a, 11b, 10b, 9b, 8b, 9a, 8a, 7b, 6b, 7a, 6a, 5b. Save the results in a JSON file that lists each orbital, its computed energy, and the calculation method. The quality of the computed energies will be assessed by a hidden verifier against established reference values.

## Assets

- Quantum chemistry package with OVGF or ADC(3) capability
- BCOD molecular structure

## Workflow steps

### Step 1: Optimize BCOD geometry at B3LYP/TZVP
- Role: process
- Action: Perform a geometry optimization of bicyclo[2.2.2]octa-2,5-dione (BCOD, C8H10O2) using density functional theory with the B3LYP functional and the TZVP basis set. Start from an initial geometry built from SMILES or a public database. Save the optimized structure (e.g., in XYZ format) for use in the next step.
- Evidence: `/app/outputs/b3lyp_optimized.xyz`

### Step 2: Compute OVGF/TZVP ionization energies
- Role: scored (load-bearing)
- Action: Using the B3LYP/TZVP optimized geometry, compute vertical ionization energies with the outer-valence Green's function method and the TZVP basis set (OVGF/TZVP). If OVGF is not available, use ADC(3)/cc-pVDZ as a fallback. Extract the ionization energies for the 18 outer-valence molecular orbitals: 14a, 13b, 12b, 13a, 12a, 11a, 10a, 11b, 10b, 9b, 8b, 9a, 8a, 7b, 6b, 7a, 6a, 5b. Write the results to ionization_energies.json.
- Output file: `/app/outputs/ionization_energies.json`
- Format: json
- Contract: A JSON array of objects. Each object must have keys: "orbital" (string, e.g., "14a"), "energy_eV" (float), "method" (string, one of "OVGF/TZVP" or "ADC(3)/cc-pVDZ"). The array must contain 18 entries, one for each of the listed orbitals.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ionization_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ionization_energies.json
- path: `/app/outputs/ionization_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed vertical ionization energies for the outer-valence orbitals of BCOD. The hidden checker reads this file, matches each entry by orbital label to the paper's reference OVGF/TZVP (or ADC(3)) energies, and accepts a match if the energy difference is within a hidden tolerance. The final score is the fraction of correctly matched orbitals.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `orbital`, `energy_eV`, `method`
    - `properties`:
      - `orbital`:
        - `type`: string
      - `energy_eV`:
        - `type`: number
      - `method`:
        - `type`: string
        - `enum`: `OVGF/TZVP`, `ADC(3)/cc-pVDZ`
  - `minItems`: 18
  - `maxItems`: 18
  - `unique_orbital_labels`: True

Notes: Only the BCOD ionization energies are scored; momentum profile simulations and cross-molecule comparisons are excluded from reproducible scope per task design.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ionization_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "orbital",
            "energy_eV",
            "method"
          ],
          "properties": {
            "orbital": {
              "type": "string"
            },
            "energy_eV": {
              "type": "number"
            },
            "method": {
              "type": "string",
              "enum": [
                "OVGF/TZVP",
                "ADC(3)/cc-pVDZ"
              ]
            }
          }
        },
        "minItems": 18,
        "maxItems": 18,
        "unique_orbital_labels": true
      },
      "description": "Computed vertical ionization energies for the outer-valence orbitals of BCOD. The hidden checker reads this file, matches each entry by orbital label to the paper's reference OVGF/TZVP (or ADC(3)) energies, and accepts a match if the energy difference is within a hidden tolerance. The final score is the fraction of correctly matched orbitals."
    }
  ],
  "notes": "Only the BCOD ionization energies are scored; momentum profile simulations and cross-molecule comparisons are excluded from reproducible scope per task design."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads `ionization_energies.json`. The verifier matches each orbital by its label and compares your computed energy to a reference value. A correct match (energy within an undisclosed tolerance) counts toward your score; the final reward is the fraction of orbitals that are correctly reproduced. The geometry optimization step itself is not directly scored, but a proper optimization is necessary to obtain accurate ionization energies.
