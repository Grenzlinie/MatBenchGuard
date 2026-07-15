# Corrected Adsorption Energies of Xylene Isomers on H-MOR Zeolite

## Problem background
Zeolite catalysts such as H-MOR (mordenite) are used for shape-selective hydrocarbon reactions. Density functional theory (DFT) is widely applied to model adsorption, but standard functionals neglect van der Waals dispersion, leading to a large underestimation of adsorption energies. This work addresses that gap by combining periodic DFT with a classical force-field correction for dispersion to compute physically realistic adsorption energies of xylene isomers within the zeolite pores.

## Approach
The method uses periodic DFT with the PW91 exchange-correlation functional to describe the zeolite framework and the adsorbed xylene molecules. A model of H-MOR with one Al substitution (Si/Al=23) and a Brønsted acidic proton is built and its atomic positions optimized. Adsorption energies of para-, meta-, and ortho-xylene are then computed from total energies of the zeolite+xylene complex, the bare zeolite, and the isolated xylene molecule. These DFT adsorption energies are corrected by adding a van der Waals contribution obtained from the classical force field of Deka et al. (1999), which describes the dispersion interaction between the aromatic guest and the zeolite host. The final corrected adsorption energies are the sum of the DFT adsorption energy and the van der Waals correction for each isomer.

## Reproduction target
Compute the corrected adsorption energies of para-xylene, meta-xylene, and ortho-xylene on H-MOR zeolite. Perform periodic DFT calculations to obtain the uncorrected DFT adsorption energies, compute the van der Waals correction using the Deka et al. force field, and then combine them to produce the corrected adsorption energies. Output the results as three JSON files: dft_adsorption_energies.json (the DFT adsorption energies), van_der_waals_correction.json (the van der Waals correction energy), and corrected_adsorption_energies.json (the final corrected adsorption energies).

## Assets

- H-MOR zeolite structure: http://www.iza-structure.org/databases/
- Quantum ESPRESSO: https://www.quantum-espresso.org
- Deka et al. force field parameters

## Workflow steps

### Step 1: Build H-MOR zeolite model
- Role: process
- Action: Construct the periodic H-MOR zeolite unit cell with one Al substitution (Si/Al=23) and a Brønsted acidic proton attached to a bridging oxygen near the Al atom. Use the lattice parameters a=13.648 Å, b=13.672 Å, c=15.105 Å, α=96.792°, β=90.003°, γ=90.022°. Optimize the atomic positions of the bare zeolite framework using DFT with the PW91 functional.
- Evidence: `/app/outputs/h_mor_structure.out`

### Step 2: DFT adsorption energies of xylene isomers
- Role: scored (load-bearing)
- Action: Perform periodic DFT geometry optimization of para-xylene, meta-xylene, and ortho-xylene physisorbed to the Brønsted proton in the H-MOR cell using the PW91 functional (open-source DFT code). Compute total energies of the zeolite+xylene complex, the bare zeolite (from step 0), and each isolated xylene molecule in vacuum. Calculate E_ads = E(complex) - E(zeolite) - E(xylene_gas) for each isomer. Output a JSON file with the three energies in kJ/mol.
- Output file: `/app/outputs/dft_adsorption_energies.json`
- Format: json
- Contract: {"para": number, "meta": number, "ortho": number}
- Scoring: scored by hidden verifier

### Step 3: Van der Waals correction
- Role: scored
- Action: Using the DFT-optimized geometries of the xylene isomers inside H-MOR (from step 1), compute the van der Waals interaction energy between the xylene molecule and the zeolite framework using the classical force field parameters from Deka et al. (1999). Report the value in kJ/mol. Output as JSON with key 'E_VdW'.
- Output file: `/app/outputs/van_der_waals_correction.json`
- Format: json
- Contract: {"E_VdW": number}
- Scoring: scored by hidden verifier

### Step 4: Corrected adsorption energies
- Role: scored (load-bearing)
- Action: Read the DFT adsorption energies from step 1 and the van der Waals correction from step 2. For each isomer, compute E_ads_corrected = E_ads + E_VdW. Output a JSON file with the three corrected energies in kJ/mol.
- Output file: `/app/outputs/corrected_adsorption_energies.json`
- Format: json
- Contract: {"para": number, "meta": number, "ortho": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_adsorption_energies.json`
- `/app/outputs/van_der_waals_correction.json`
- `/app/outputs/corrected_adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_adsorption_energies.json
- path: `/app/outputs/dft_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT adsorption energies of para-xylene, meta-xylene, and ortho-xylene on H-MOR.
- schema:
  - `type`: object
  - `required`:
    - `para`: float (kJ/mol)
    - `meta`: float (kJ/mol)
    - `ortho`: float (kJ/mol)
  - `items`: object
  - `required_columns`:
  - `units`: object

### van_der_waals_correction.json
- path: `/app/outputs/van_der_waals_correction.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Van der Waals dispersion correction for xylene adsorption on H-MOR.
- schema:
  - `type`: object
  - `required`:
    - `E_VdW`: float (kJ/mol)
  - `items`: object
  - `required_columns`:
  - `units`: object

### corrected_adsorption_energies.json
- path: `/app/outputs/corrected_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Force-field corrected adsorption energies of xylene isomers.
- schema:
  - `type`: object
  - `required`:
    - `para`: float (kJ/mol)
    - `meta`: float (kJ/mol)
    - `ortho`: float (kJ/mol)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The scorer compares each value to the paper-reported reference with per-file tolerances (hidden).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "para": "float (kJ/mol)",
          "meta": "float (kJ/mol)",
          "ortho": "float (kJ/mol)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "DFT adsorption energies of para-xylene, meta-xylene, and ortho-xylene on H-MOR."
    },
    {
      "file": "van_der_waals_correction.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_VdW": "float (kJ/mol)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Van der Waals dispersion correction for xylene adsorption on H-MOR."
    },
    {
      "file": "corrected_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "para": "float (kJ/mol)",
          "meta": "float (kJ/mol)",
          "ortho": "float (kJ/mol)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Force-field corrected adsorption energies of xylene isomers."
    }
  ],
  "notes": "The scorer compares each value to the paper-reported reference with per-file tolerances (hidden)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently reads each of the three output JSON artifacts. For each artifact, the verifier compares your computed values to reference values within an appropriate tolerance. The total reward is a weighted combination of the scores from the individual artifacts. Simply reporting numbers that match the paper is not sufficient; your workflow must produce the artifacts through the described computational steps.
