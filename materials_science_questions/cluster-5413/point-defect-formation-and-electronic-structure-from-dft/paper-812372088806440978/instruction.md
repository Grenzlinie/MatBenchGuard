# Reproduce formation energy and geometry of FS+(OH-) defect on MgO(100) using periodic DFT

## Problem background
Point defects at oxide surfaces, particularly oxygen vacancies (F centers), strongly influence the chemical and physical properties of MgO, a widely used catalyst and support. Understanding the nature and formation of paramagnetic color centers at the MgO(100) surface is important for interpreting electron paramagnetic resonance (EPR) spectra and surface reactivity. This work examines the interaction of atomic hydrogen with MgO(100) and introduces a defect center consisting of an oxygen vacancy with a trapped electron adjacent to an adsorbed hydroxyl group, denoted FS+(OH−). Periodic density functional theory (DFT) calculations are used to characterize the geometry and formation energy of this defect. Reproducing these calculated properties tests our ability to model surface defects on MgO with periodic plane-wave DFT.

## Approach
The approach uses periodic plane-wave DFT with the PW91 exchange-correlation functional and ultrasoft pseudopotentials. The MgO(100) surface is represented by slabs of three and four atomic layers within a supercell to minimize defect-defect interactions. An oxygen vacancy is created by removing a surface oxygen atom, and an OH group is placed on a neighboring Mg ion. Two configurations are studied: one where the vacancy and OH are adjacent on the same surface (three-layer slab), and another where they are on opposite sides of the slab (four-layer slab). For each configuration, DFT relaxations are performed to obtain total energies and optimized atomic positions. To compute the formation energy, the total energies of the defective slab, the clean slab, and an isolated hydrogen atom are obtained. The formation energy is then calculated as the difference E(defect) – E(clean) – E(H). From the relaxed three-layer adjacent structure, the Mg–OH bond distance and Mg–O–H angle are extracted. The workflow builds these models and performs the required relaxations and energy extractions.

## Reproduction target
Compute and report the following for the FS+(OH−) defect using periodic DFT with the PW91 functional: (1) For a three-layer MgO(100) slab with the oxygen vacancy and OH group adjacent, provide the total energies of the clean slab, defective slab, isolated H atom, and the resulting formation energy (eV). Also report the relaxed Mg–OH bond distance (Å) and Mg–O–H angle (degrees). (2) For a four-layer slab with the vacancy and OH on opposite surfaces, provide the analogous total energies and formation energy. The required outputs are three JSON files: one each for the three-layer formation energy, three-layer geometry, and four-layer formation energy, as specified in the output contract.

## Assets

- Quantum ESPRESSO (or equivalent open-source plane-wave DFT code supporting PW91 functional): https://www.quantum-espresso.org
- PW91 ultrasoft pseudopotentials for Mg, O, and H (e.g., from SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build periodic slab supercells and defect configurations
- Role: process
- Action: Construct three-layer and four-layer MgO(100) slab supercells (2√2×2√2 surface unit cell, 8 Å vacuum). For the three-layer slab, create an oxygen vacancy by removing a surface O atom and add an OH group on a neighbouring Mg ion (FS+(OH−) with adjacent OH). For the four-layer slab, create the vacancy on one surface and an OH group on the opposite surface (separated configuration). Prepare DFT input files for relaxation using PW91 functional and ultrasoft pseudopotentials.
- Evidence: `/app/outputs/slab_structures.log`

### Step 2: Run DFT relaxations for clean slabs and isolated H atom
- Role: process
- Action: Perform DFT relaxation of the clean three-layer and four-layer slabs to obtain total energies. Compute the total energy of an isolated H atom in a spin-polarized asymmetric box. Record the energies for later use.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Run DFT relaxation for three-layer FS+(OH-) defect
- Role: process
- Action: Perform DFT relaxation of the three-layer slab containing the FS+(OH-) defect (vacancy and OH adjacent). Obtain the total energy and the final atomic positions.
- Evidence: `/app/outputs/defect_3layer_results.json`

### Step 4: Report formation energy for three-layer defect
- Role: scored (load-bearing)
- Action: Compute the formation energy E_f = E(defect_slab_3layer) – E(clean_slab_3layer) – E(H_atom) and export the three total energies plus the computed E_f to /app/outputs/three_layer_formation_energy.json.
- Output file: `/app/outputs/three_layer_formation_energy.json`
- Format: json
- Contract: {"E_clean_slab_3layer": number (eV), "E_defect_slab_3layer": number (eV), "E_H_atom": number (eV), "formation_energy": number (eV)}
- Scoring: scored by hidden verifier

### Step 5: Report geometry of three-layer defect
- Role: scored
- Action: Extract the Mg–OH bond distance (Å) and Mg–O–H angle (degrees) from the relaxed three-layer defect structure and export to /app/outputs/three_layer_geometry.json.
- Output file: `/app/outputs/three_layer_geometry.json`
- Format: json
- Contract: {"Mg_OH_distance": number (Angstrom), "Mg_O_H_angle": number (degrees)}
- Scoring: scored by hidden verifier

### Step 6: Run DFT relaxation for four-layer separated defect
- Role: process
- Action: Perform DFT relaxation of the four-layer slab with the FS+(OH-) defect where the vacancy and OH are on opposite sides of the slab. Obtain the total energy.
- Evidence: `/app/outputs/defect_4layer_energy.json`

### Step 7: Report formation energy for four-layer separated defect
- Role: scored (load-bearing)
- Action: Compute E_f = E(defect_slab_4layer) – E(clean_slab_4layer) – E(H_atom) and export to /app/outputs/four_layer_separated_formation_energy.json.
- Output file: `/app/outputs/four_layer_separated_formation_energy.json`
- Format: json
- Contract: {"E_clean_slab_4layer": number (eV), "E_defect_slab_4layer": number (eV), "E_H_atom": number (eV), "formation_energy": number (eV)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/three_layer_formation_energy.json`
- `/app/outputs/three_layer_geometry.json`
- `/app/outputs/four_layer_separated_formation_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### three_layer_formation_energy.json
- path: `/app/outputs/three_layer_formation_energy.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Total energies of 3-layer clean slab, 3-layer defect slab, isolated H atom, and the derived formation energy.
- schema:
  - `type`: object
  - `required`: `E_clean_slab_3layer`, `E_defect_slab_3layer`, `E_H_atom`, `formation_energy`
  - `properties`:
    - `E_clean_slab_3layer`:
      - `type`: number
      - `unit`: eV
    - `E_defect_slab_3layer`:
      - `type`: number
      - `unit`: eV
    - `E_H_atom`:
      - `type`: number
      - `unit`: eV
    - `formation_energy`:
      - `type`: number
      - `unit`: eV

### three_layer_geometry.json
- path: `/app/outputs/three_layer_geometry.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mg–OH bond distance and Mg–O–H angle from the relaxed 3-layer defect structure.
- schema:
  - `type`: object
  - `required`: `Mg_OH_distance`, `Mg_O_H_angle`
  - `properties`:
    - `Mg_OH_distance`:
      - `type`: number
      - `unit`: Angstrom
    - `Mg_O_H_angle`:
      - `type`: number
      - `unit`: degrees

### four_layer_separated_formation_energy.json
- path: `/app/outputs/four_layer_separated_formation_energy.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Total energies of 4-layer clean slab, 4-layer defect slab with separated vacancy and OH, isolated H atom, and the derived formation energy.
- schema:
  - `type`: object
  - `required`: `E_clean_slab_4layer`, `E_defect_slab_4layer`, `E_H_atom`, `formation_energy`
  - `properties`:
    - `E_clean_slab_4layer`:
      - `type`: number
      - `unit`: eV
    - `E_defect_slab_4layer`:
      - `type`: number
      - `unit`: eV
    - `E_H_atom`:
      - `type`: number
      - `unit`: eV
    - `formation_energy`:
      - `type`: number
      - `unit`: eV

Notes: The checker will recompute the formation energy from the provided total energies and compare it to the reference value. The geometry values will be compared directly to reference values. All comparisons use appropriate tolerances to account for DFT implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "three_layer_formation_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "E_clean_slab_3layer",
          "E_defect_slab_3layer",
          "E_H_atom",
          "formation_energy"
        ],
        "properties": {
          "E_clean_slab_3layer": {
            "type": "number",
            "unit": "eV"
          },
          "E_defect_slab_3layer": {
            "type": "number",
            "unit": "eV"
          },
          "E_H_atom": {
            "type": "number",
            "unit": "eV"
          },
          "formation_energy": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Total energies of 3-layer clean slab, 3-layer defect slab, isolated H atom, and the derived formation energy."
    },
    {
      "file": "three_layer_geometry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Mg_OH_distance",
          "Mg_O_H_angle"
        ],
        "properties": {
          "Mg_OH_distance": {
            "type": "number",
            "unit": "Angstrom"
          },
          "Mg_O_H_angle": {
            "type": "number",
            "unit": "degrees"
          }
        }
      },
      "description": "Mg–OH bond distance and Mg–O–H angle from the relaxed 3-layer defect structure."
    },
    {
      "file": "four_layer_separated_formation_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "E_clean_slab_4layer",
          "E_defect_slab_4layer",
          "E_H_atom",
          "formation_energy"
        ],
        "properties": {
          "E_clean_slab_4layer": {
            "type": "number",
            "unit": "eV"
          },
          "E_defect_slab_4layer": {
            "type": "number",
            "unit": "eV"
          },
          "E_H_atom": {
            "type": "number",
            "unit": "eV"
          },
          "formation_energy": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Total energies of 4-layer clean slab, 4-layer defect slab with separated vacancy and OH, isolated H atom, and the derived formation energy."
    }
  ],
  "notes": "The checker will recompute the formation energy from the provided total energies and compare it to the reference value. The geometry values will be compared directly to reference values. All comparisons use appropriate tolerances to account for DFT implementation differences."
}
```

## How you are scored
A hidden automated verifier checks your submitted files. For the formation energy files, the verifier recomputes the formation energy from the total energies you provide and compares it to a hidden reference value; the check passes if the value falls within a specified tolerance that accounts for differences in DFT implementations. For the geometry file, the verifier compares your reported distance and angle directly to hidden reference values, again with a tolerance. The overall score is a weighted combination of these individual checks. Simply reporting numbers without performing the required DFT workflow is not sufficient to pass the verifier.
