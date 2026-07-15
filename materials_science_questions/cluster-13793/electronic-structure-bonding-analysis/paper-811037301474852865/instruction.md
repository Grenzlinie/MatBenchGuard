# DFT Electronic Structure and Bonding Analysis of AlH3 Polymorphs

## Problem background
Aluminum hydride (AlH3) polymorphs are promising materials for hydrogen storage and hydride electronics, with high gravimetric hydrogen capacity and interesting electronic properties. Understanding the stability and electronic structure of the different polymorphs (α, β, γ, and α′) is essential for optimizing their performance. Density functional theory (DFT) calculations provide a way to predict formation enthalpies, band gaps, and bonding character. This task involves performing first‑principles electronic structure calculations to determine these quantities for the α‑, β‑, γ‑, and α′‑AlH3 phases.

## Approach
The reproduction uses an all‑electron full‑potential DFT method (e.g., Elk or Quantum ESPRESSO with PAW) similar to the linearized augmented plane‑wave approach. Initial crystal structures for the polymorphs are obtained from public crystallographic data. The workflow involves: structural relaxation using the GGA‑PBE exchange‑correlation functional to obtain relaxed lattice parameters and total energies; separate calculations of reference energies for fcc Al metal and an isolated H2 molecule; computation of formation enthalpies from these energies; band structure calculations with GGA‑PBE and the Tran‑Blaha modified Becke‑Johnson (TBmBJ) exchange potential to estimate band gaps; and Bader charge analysis on the self‑consistent electron density to assess atomic charges and bonding character. All calculations are performed with standard convergence criteria, and results are collected into the specified output files.

## Reproduction target
Produce computed values of the following quantities for the α, β, γ, and α′ polymorphs of AlH3:
* Optimized lattice parameters (a, b, c in Å) and volume per formula unit (Å³) from GGA‑PBE relaxation.
* Formation enthalpy (kJ per mol of H₂) calculated from the DFT total energies of each polymorph, fcc Al, and H₂.
* Fundamental band gap (eV) using both GGA‑PBE and TBmBJ functionals.
* Bader atomic charges (in e) for Al and H atoms from GGA‑PBE (optionally also from TBmBJ) for α‑, β‑, and γ‑AlH3.
The results should be written to the specified output files with the exact formats described in the workflow steps.

## Assets

- All-electron full-potential DFT code (e.g., Elk or Quantum ESPRESSO with PAW): https://elk.sourceforge.io/
- Bader charge analysis program: http://theory.cm.utexas.edu/henkelman/code/bader/
- Initial crystal structures of AlH3 polymorphs

## Workflow steps

### Step 1: Compute total energy of fcc Al reference
- Role: process
- Action: Perform a DFT self-consistent field calculation for fcc aluminum (space group Fm-3m, experimental lattice constant ~4.04 Å) using GGA-PBE to obtain its total electronic energy.
- Evidence: `/app/outputs/al_energy.json`

### Step 2: Compute total energy of H2 molecule
- Role: process
- Action: Perform a DFT calculation for an isolated H2 molecule using the same GGA-PBE functional to obtain its total electronic energy (the paper used a value from a previous study; here we recompute for consistency).
- Evidence: `/app/outputs/h2_energy.json`

### Step 3: Structural relaxation of AlH3 polymorphs
- Role: process
- Action: Starting from the initial crystal structures (α-, β-, γ-, α'-AlH3), perform full structural relaxation (lattice parameters and atomic positions) with GGA-PBE until forces on atoms are converged. Record the final total energies and relaxed geometries.
- Evidence: `/app/outputs/relaxation_data.json`

### Step 4: Report optimized lattice parameters
- Role: scored
- Action: Extract the optimized lattice parameters (a, b, c) and formula-unit volume for each polymorph from the relaxation output and save to a CSV file.
- Output file: `/app/outputs/lattice_parameters.csv`
- Format: csv
- Contract: Columns: polymorph (string, e.g., 'alpha'), a (float, Å), b (float, Å), c (float, Å), volume_per_fu (float, Å³). Optional notes column.
- Scoring: scored by hidden verifier

### Step 5: Calculate formation enthalpies
- Role: scored (load-bearing)
- Action: Calculate the formation enthalpy ΔH = E_AlH3 - E_Al - 1.5*E_H2 (kJ/mol H2) for each polymorph using the total energies from the relaxation step and the reference energies from steps s0 and s1.
- Output file: `/app/outputs/formation_enthalpies.json`
- Format: json
- Contract: JSON object with keys 'alpha', 'beta', 'gamma', 'alpha_prime'. Each key maps to an object with 'total_energy_Ry' (float) and 'formation_enthalpy_kJ_per_mol_H2' (float).
- Scoring: scored by hidden verifier

### Step 6: Compute band gaps
- Role: scored
- Action: Using the relaxed structures, perform band structure calculations with GGA-PBE and TBmBJ functionals. Determine the band gap (eV) for each polymorph from the resulting band structures.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON object with keys 'alpha', 'beta', 'gamma', 'alpha_prime'. Each maps to an object with 'GGA_PBE' (float, eV) and 'TBmBJ' (float, eV).
- Scoring: scored by hidden verifier

### Step 7: Bader charge analysis
- Role: scored
- Action: Perform Bader charge analysis on the self-consistent electron density from GGA-PBE runs (and optionally TBmBJ) for each polymorph. Report the atomic charges (in e) for Al and H atoms.
- Output file: `/app/outputs/bader_charges.json`
- Format: json
- Contract: JSON object with keys 'alpha', 'beta', 'gamma'. Each maps to an object with 'Al' (float, e) and 'H' (either a single float or an array of floats per site, e). For γ, list values for each distinct H site as an array.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.csv`
- `/app/outputs/formation_enthalpies.json`
- `/app/outputs/band_gaps.json`
- `/app/outputs/bader_charges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.csv
- path: `/app/outputs/lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice constants and formula-unit volume for each AlH3 polymorph.
- schema:
  - `type`: table
  - `required_columns`: `polymorph`, `a`, `b`, `c`, `volume_per_fu`
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å
    - `volume_per_fu`: Å³

### formation_enthalpies.json
- path: `/app/outputs/formation_enthalpies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Formation enthalpies of AlH3 polymorphs computed from DFT total energies.
- schema:
  - `type`: object
  - `required`:
    - `alpha`:
      - `type`: object
      - `required`: `total_energy_Ry`, `formation_enthalpy_kJ_per_mol_H2`
    - `beta`:
      - `type`: object
      - `required`: `total_energy_Ry`, `formation_enthalpy_kJ_per_mol_H2`
    - `gamma`:
      - `type`: object
      - `required`: `total_energy_Ry`, `formation_enthalpy_kJ_per_mol_H2`
    - `alpha_prime`:
      - `type`: object
      - `required`: `total_energy_Ry`, `formation_enthalpy_kJ_per_mol_H2`
  - `units`:
    - `total_energy_Ry`: Rydberg
    - `formation_enthalpy_kJ_per_mol_H2`: kJ/mol H2

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Band gaps of AlH3 polymorphs computed with GGA-PBE and TBmBJ functionals.
- schema:
  - `type`: object
  - `required`:
    - `alpha`:
      - `type`: object
      - `required`: `GGA_PBE`, `TBmBJ`
    - `beta`:
      - `type`: object
      - `required`: `GGA_PBE`, `TBmBJ`
    - `gamma`:
      - `type`: object
      - `required`: `GGA_PBE`, `TBmBJ`
    - `alpha_prime`:
      - `type`: object
      - `required`: `GGA_PBE`, `TBmBJ`
  - `units`:
    - `GGA_PBE`: eV
    - `TBmBJ`: eV

### bader_charges.json
- path: `/app/outputs/bader_charges.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bader charges for Al and H atoms in α-, β-, and γ-AlH3. H value may be a single float or an array of floats for distinct hydrogen sites.
- schema:
  - `type`: object
  - `required`:
    - `alpha`:
      - `type`: object
      - `required`: `Al`, `H`
    - `beta`:
      - `type`: object
      - `required`: `Al`, `H`
    - `gamma`:
      - `type`: object
      - `required`: `Al`, `H`
  - `units`:
    - `Al`: e
    - `H`: e (single float or array of floats per site)

Notes: All outputs are compared against hidden reference values with appropriate tolerances. The Bader charge step is optional; if missing, its weight is redistributed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "polymorph",
          "a",
          "b",
          "c",
          "volume_per_fu"
        ],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å",
          "volume_per_fu": "Å³"
        }
      },
      "description": "Optimized lattice constants and formula-unit volume for each AlH3 polymorph."
    },
    {
      "file": "formation_enthalpies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha": {
            "type": "object",
            "required": [
              "total_energy_Ry",
              "formation_enthalpy_kJ_per_mol_H2"
            ]
          },
          "beta": {
            "type": "object",
            "required": [
              "total_energy_Ry",
              "formation_enthalpy_kJ_per_mol_H2"
            ]
          },
          "gamma": {
            "type": "object",
            "required": [
              "total_energy_Ry",
              "formation_enthalpy_kJ_per_mol_H2"
            ]
          },
          "alpha_prime": {
            "type": "object",
            "required": [
              "total_energy_Ry",
              "formation_enthalpy_kJ_per_mol_H2"
            ]
          }
        },
        "units": {
          "total_energy_Ry": "Rydberg",
          "formation_enthalpy_kJ_per_mol_H2": "kJ/mol H2"
        }
      },
      "description": "Formation enthalpies of AlH3 polymorphs computed from DFT total energies."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha": {
            "type": "object",
            "required": [
              "GGA_PBE",
              "TBmBJ"
            ]
          },
          "beta": {
            "type": "object",
            "required": [
              "GGA_PBE",
              "TBmBJ"
            ]
          },
          "gamma": {
            "type": "object",
            "required": [
              "GGA_PBE",
              "TBmBJ"
            ]
          },
          "alpha_prime": {
            "type": "object",
            "required": [
              "GGA_PBE",
              "TBmBJ"
            ]
          }
        },
        "units": {
          "GGA_PBE": "eV",
          "TBmBJ": "eV"
        }
      },
      "description": "Band gaps of AlH3 polymorphs computed with GGA-PBE and TBmBJ functionals."
    },
    {
      "file": "bader_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha": {
            "type": "object",
            "required": [
              "Al",
              "H"
            ]
          },
          "beta": {
            "type": "object",
            "required": [
              "Al",
              "H"
            ]
          },
          "gamma": {
            "type": "object",
            "required": [
              "Al",
              "H"
            ]
          }
        },
        "units": {
          "Al": "e",
          "H": "e (single float or array of floats per site)"
        }
      },
      "description": "Bader charges for Al and H atoms in α-, β-, and γ-AlH3. H value may be a single float or an array of floats for distinct hydrogen sites."
    }
  ],
  "notes": "All outputs are compared against hidden reference values with appropriate tolerances. The Bader charge step is optional; if missing, its weight is redistributed."
}
```

## How you are scored
A hidden verifier independently compares each of your output files against pre‑established reference values (the expected results for this reproduction). For the lattice parameters, formation enthalpies, band gaps, and Bader charges, the verifier checks that the reported numbers match the references within tolerances appropriate for differences between DFT implementations. Each stage carries a weight that contributes to the final reward score: lattice parameters (10%), formation enthalpies (30%), band gaps (40%), and Bader charges (20%). If the Bader charge analysis is not feasible with your chosen DFT code, that stage may be omitted and its weight redistributed. Your final score is a weighted sum of the per‑stage scores; simply reporting the correct values from the literature is not sufficient—the verifier checks that the numbers are the result of a genuine DFT computation as described in the workflow.
