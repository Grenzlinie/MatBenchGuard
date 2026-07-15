# DFT Prediction of Properties of Six Hypothetical sp³-Carbon Allotropes from Zeolite Nets

## Problem background
Carbon allotropes with diamond-like sp3 bonding are of great interest for hard, transparent materials. Hypothetical zeolite frameworks provide a vast pool of possible topologies that, when mapped to carbon, could yield novel allotropes. This task reproduces the prediction of thermodynamic, mechanical, electronic, and optical properties for a set of candidate sp3-carbon phases derived from specific zeolite nets, comparing their stability and performance against diamond.

## Approach
The method starts from a given zeolite net topology. Silicon atoms are replaced by carbon, oxygen is removed, and the lattice is scaled so that the average nearest-neighbor C–C distance matches typical sp3 bond lengths (~1.54 Å). The resulting candidate allotropes are then studied with density functional theory (DFT) using the PBE functional. A full geometry relaxation provides the equilibrium total energy and structure. The bulk modulus is derived by fitting energy versus volume data to a third‑order Birch–Murnaghan equation of state. The full elastic tensor is computed, and the Voigt–Reuss–Hill shear modulus is used with an empirical hardness model (Gao’s model) to estimate Vickers hardness. Electronic band gaps are determined at both the PBE level and with a screened hybrid functional (HSE06). Finally, the frequency‑dependent dielectric tensor is calculated to obtain the static refractive indices along the principal axes. All calculations are performed in parallel for the six target nets and for a diamond reference.

## Reproduction target
Given the six Deem hypothetical zeolite identifiers 8170628, 8129388, 8255250, 8155755, 8036927, and 8036926, produce the corresponding sp3‑carbon allotropes and a diamond reference structure. For each, compute the following quantities:
- Cohesive energy relative to diamond, ΔE (eV/atom)
- Bulk modulus (GPa)
- Vickers hardness (GPa)
- Electronic band gap at the PBE level (eV)
- Electronic band gap at the HSE level (eV)
- Refractive indices n_xx, n_yy, n_zz
Assemble the results for all seven entries into allotropes_properties.json as detailed in the output contract.

## Assets

- Deem hypothetical zeolite database: http://www.hypotheticalzeolites.net/DATABASE/DEEM/DEEM_PCOD/index.php
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/

## Workflow steps

### Step 1: Obtain zeolite net structures
- Role: process
- Action: Download the hypothetical zeolite CIF files from the Deem database for identifiers 8170628, 8129388, 8255250, 8155755, 8036927, 8036926. Also prepare a diamond reference structure (conventional cubic cell).
- Evidence: `/app/outputs/nets_downloaded.txt`

### Step 2: Generate initial carbon allotropes
- Role: process
- Action: For each zeolite net, remove oxygen atoms, replace Si with C, and scale the lattice so that the average nearest-neighbor C–C distance is approximately 1.54 Å. Create initial structure files suitable for DFT calculations.
- Evidence: `/app/outputs/initial_structures.tar.gz`

### Step 3: DFT-PBE geometry optimization
- Role: process
- Action: Perform full geometry relaxation (atomic positions and cell parameters) for each allotrope and diamond using the PBE functional with a plane-wave pseudopotential approach. Iterate until forces and stress are well converged. Save the optimized structures and total energies.
- Evidence: `/app/outputs/optimized_structures.tar.gz`

### Step 4: Energy-volume scans for bulk modulus
- Role: process
- Action: For each optimized structure, run single-point DFT calculations at a series of uniformly scaled volumes (a few percent above and below the equilibrium volume) to generate total energy vs. volume data. Fit this data to a third-order Birch-Murnaghan equation of state to extract the bulk modulus B.
- Evidence: `/app/outputs/ev_data.csv`

### Step 5: Elastic constants calculation
- Role: process
- Action: Compute the full second-order elastic constant tensor for each allotrope and diamond using density-functional perturbation theory or the stress-strain method. From the elastic constants, derive the Voigt-Reuss-Hill average bulk modulus B and shear modulus G.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 6: Electronic band gap calculations
- Role: process
- Action: Using the optimized structures, compute the electronic band structure along high-symmetry paths. Determine the fundamental band gap at the PBE level. Then perform a hybrid functional calculation (e.g., HSE06) to obtain a corrected band gap. Record both PBE and HSE values.
- Evidence: `/app/outputs/band_gaps.txt`

### Step 7: Dielectric function and refractive indices
- Role: process
- Action: Calculate the frequency-dependent dielectric tensor for each allotrope. Extract the static electronic dielectric constants ε_xx, ε_yy, ε_zz and derive the refractive indices n = √ε. Report the three principal components.
- Evidence: `/app/outputs/dielectric_data.json`

### Step 8: Assemble and report all properties
- Role: scored (load-bearing)
- Action: Compile all computed results into a single JSON file. Compute ΔE as (E_allotrope/n_atoms) - (E_diamond/n_atoms_diamond). Compute Vickers hardness H via Gao's model: H = 0.92 * (B/G)^0.5 * G, where G is the shear modulus. Include the bulk modulus from the EOS fit or elastic constants, PBE and HSE band gaps from step06, and refractive indices from step07. Write the file allotropes_properties.json containing exactly 7 entries (six allotropes + diamond).
- Output file: `/app/outputs/allotropes_properties.json`
- Format: json
- Contract: JSON array of 7 objects. Each object has keys: allotrope_id (string), space_group (string), delta_E_PBE (float, eV/atom), bulk_modulus (float, GPa), hardness (float, GPa), band_gap_PBE (float, eV), band_gap_HSE (float, eV), refractive_index_xx (float), refractive_index_yy (float), refractive_index_zz (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/allotropes_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### allotropes_properties.json
- path: `/app/outputs/allotropes_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled properties (ΔE, B, H, band gaps, refractive indices) for the six allotropes and diamond, used for scoring.
- schema:
  - `type`: array
  - `description`: Array of 7 objects (6 allotropes + diamond)
  - `items`:
    - `type`: object
    - `required`: `allotrope_id`, `space_group`, `delta_E_PBE`, `bulk_modulus`, `hardness`, `band_gap_PBE`, `band_gap_HSE`, `refractive_index_xx`, `refractive_index_yy`, `refractive_index_zz`
    - `properties`:
      - `allotrope_id`:
        - `type`: string
        - `description`: Identifier of the allotrope; use 'diamond' for the diamond reference.
      - `space_group`:
        - `type`: string
      - `delta_E_PBE`:
        - `type`: number
        - `unit`: eV/atom
        - `description`: Cohesive energy relative to diamond (PBE).
      - `bulk_modulus`:
        - `type`: number
        - `unit`: GPa
      - `hardness`:
        - `type`: number
        - `unit`: GPa
      - `band_gap_PBE`:
        - `type`: number
        - `unit`: eV
      - `band_gap_HSE`:
        - `type`: number
        - `unit`: eV
      - `refractive_index_xx`:
        - `type`: number
      - `refractive_index_yy`:
        - `type`: number
      - `refractive_index_zz`:
        - `type`: number

Notes: The checker compares each numerical field to the paper's reported values using absolute tolerances (ΔE ±0.02 eV/atom, B ±15 GPa, H ±5 GPa, band_gap_PBE ±0.3 eV, band_gap_HSE ±0.5 eV, refractive indices ±0.05). Diamond entry is required but not scored directly (penalty if missing).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "allotropes_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "description": "Array of 7 objects (6 allotropes + diamond)",
        "items": {
          "type": "object",
          "required": [
            "allotrope_id",
            "space_group",
            "delta_E_PBE",
            "bulk_modulus",
            "hardness",
            "band_gap_PBE",
            "band_gap_HSE",
            "refractive_index_xx",
            "refractive_index_yy",
            "refractive_index_zz"
          ],
          "properties": {
            "allotrope_id": {
              "type": "string",
              "description": "Identifier of the allotrope; use 'diamond' for the diamond reference."
            },
            "space_group": {
              "type": "string"
            },
            "delta_E_PBE": {
              "type": "number",
              "unit": "eV/atom",
              "description": "Cohesive energy relative to diamond (PBE)."
            },
            "bulk_modulus": {
              "type": "number",
              "unit": "GPa"
            },
            "hardness": {
              "type": "number",
              "unit": "GPa"
            },
            "band_gap_PBE": {
              "type": "number",
              "unit": "eV"
            },
            "band_gap_HSE": {
              "type": "number",
              "unit": "eV"
            },
            "refractive_index_xx": {
              "type": "number"
            },
            "refractive_index_yy": {
              "type": "number"
            },
            "refractive_index_zz": {
              "type": "number"
            }
          }
        }
      },
      "description": "Compiled properties (ΔE, B, H, band gaps, refractive indices) for the six allotropes and diamond, used for scoring."
    }
  ],
  "notes": "The checker compares each numerical field to the paper's reported values using absolute tolerances (ΔE ±0.02 eV/atom, B ±15 GPa, H ±5 GPa, band_gap_PBE ±0.3 eV, band_gap_HSE ±0.5 eV, refractive indices ±0.05). Diamond entry is required but not scored directly (penalty if missing)."
}
```

## How you are scored
A hidden verifier reads your allotropes_properties.json and compares each reported numeric value to a set of reference results (derived from the original computational study). Each property category (ΔE, bulk modulus, hardness, band_gap_PBE, band_gap_HSE, refractive indices) contributes a fixed weight to the total reward. A value is considered correct if it falls within a predefined absolute tolerance of the hidden reference; the weighted fraction of correctly reproduced properties gives your final score (0 to 1). Simply providing numbers without performing the described DFT workflow will not yield the required accuracy.
