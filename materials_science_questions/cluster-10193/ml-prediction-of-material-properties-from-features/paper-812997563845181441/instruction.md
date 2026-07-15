# DFT-based Surface d-Band Center Distributions in Nanoparticles

## Problem background
High-entropy-alloy nanoparticles (HEA NPs) open a vast compositional space with potentially rich electronic properties that deviate from simple additive behaviors of their constituent elements. Understanding the local electronic structure at the surface is critical, as catalytic reactions occur at surface sites. The d-band center (ε_d), the energy-weighted center of the d-projected density of states, is a widely used descriptor for reactivity. While monometallic nanoparticles exhibit a narrow distribution of surface ε_d values governed by atomic coordination, it is an open question how the local ε_d values of surface atoms in HEA NPs distribute across elements and configurations. This task aims to compute the local ε_d for every surface atom in monometallic and HEA nanoparticle models to investigate these distributions.

## Approach
The computational approach constructs atomistic models of 201-atom truncated octahedral fcc nanoparticles for each of the eight noble metals (Ru, Rh, Pd, Ag, Os, Ir, Pt, Au) and for several random configurations of an equimolar noble-metal HEA. Spin-unpolarized density functional theory (DFT) calculations are performed on each model using the PBE exchange-correlation functional and standard pseudopotentials to obtain the electronic ground state. From converged charge densities, the d-projected local density of states (LDOS) is computed for every atom. For each surface atom (identified by coordination number less than 12), the local d-band center ε_d = ∫ E·D_d(E) dE / ∫ D_d(E) dE is evaluated. The per-element distributions of ε_d in the HEA are then compared with those in the monometallic nanoparticles, focusing on the ranges of ε_d values each element exhibits.

## Reproduction target
Produce two artifacts: (1) a CSV file (`surface_dband_centers.csv`) listing every identified surface atom across all models, with columns for model type (monometallic or HEA), element symbol, atom index, and its computed ε_d (in eV). (2) a JSON summary (`ranges_summary.json`) aggregating per-element minimum, maximum, and range of ε_d for the monometallic and HEA subsets, as well as the overall minimum and maximum ε_d among all HEA surface atoms. The reproduction objective is to provide the raw data and summaries that allow a structural comparison of ε_d distributions between monometallic and HEA nanoparticles.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- ASE (Atomic Simulation Environment): ase
- PBE pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python with pymatgen and scipy: pymatgen, scipy

## Workflow steps

### Step 1: Build nanoparticle atomic models
- Role: process
- Action: Construct 201-atom truncated octahedral fcc nanoparticle models for each of the eight noble metals (Ru, Rh, Pd, Ag, Os, Ir, Pt, Au) and for ten random configurations of the equimolar NM-HEA. Use standard fcc lattice constants; for the alloy, set the average lattice constant. Save coordinates in a format compatible with Quantum ESPRESSO (e.g., .xyz).
- Evidence: `/app/outputs/model_build_log.txt`

### Step 2: Run DFT electronic structure calculations
- Role: process
- Action: For each nanoparticle model, perform spin-unpolarized DFT calculations using Quantum ESPRESSO with PBE pseudopotentials. After SCF convergence, perform a non-self-consistent calculation to obtain the d-projected local density of states (PDOS) for every atom. Save the PDOS data for downstream processing.
- Evidence: `/app/outputs/dft_convergence_log.txt`

### Step 3: Compute surface d-band centers and save CSV
- Role: scored (load-bearing)
- Action: From the PDOS output, extract the d-projected LDOS for every surface atom (coordination number < 12). Compute the local d-band center epsilon_d = ∫ E·D_d(E) dE / ∫ D_d(E) dE for each such atom. Write a CSV file listing every surface atom with model_type, element, atom_index, and epsilon_d.
- Output file: `/app/outputs/surface_dband_centers.csv`
- Format: csv
- Contract: CSV columns: model_type (string, 'monometallic' or 'HEA'), element (string, atomic symbol), atom_index (integer), epsilon_d (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Aggregate ranges and save JSON summary
- Role: scored
- Action: Compute per-element min, max, and range for monometallic and NM-HEA subsets, and the overall NM-HEA surface epsilon_d min and max. Write a JSON summary file containing these aggregated values.
- Output file: `/app/outputs/ranges_summary.json`
- Format: json
- Contract: JSON object: { 'monometallic': { 'element': { 'min': float, 'max': float, 'range': float } }, 'NMHEA': { 'element': { 'min': float, 'max': float, 'range': float } }, 'overall_NMHEA': { 'min': float, 'max': float } }. All values in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_dband_centers.csv`
- `/app/outputs/ranges_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_dband_centers.csv
- path: `/app/outputs/surface_dband_centers.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of every surface atom's local d-band center. The checker recomputes per-element ranges from this CSV and verifies required structural relationships (range broadening, overall span).
- schema:
  - `type`: table
  - `required_columns`: `model_type`, `element`, `atom_index`, `epsilon_d`
  - `units`:
    - `epsilon_d`: eV

### ranges_summary.json
- path: `/app/outputs/ranges_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Aggregated summary of epsilon_d ranges. The checker may validate structure and consistency with the CSV, but primary scoring is based on recomputation from the CSV.
- schema:
  - `type`: object
  - `required`: `monometallic`, `NMHEA`, `overall_NMHEA`
  - `items`:
    - `monometallic`:
      - `element`:
        - `min`: float
        - `max`: float
        - `range`: float
    - `NMHEA`:
      - `element`:
        - `min`: float
        - `max`: float
        - `range`: float
    - `overall_NMHEA`:
      - `min`: float
      - `max`: float

Notes: The workflow covers only the DFT-based d-band center analysis. Experimental spectra, HER activity, LDOS profile shape comparisons, and supervised learning regression are excluded per the defined scope. The agent must produce both artifacts; scoring is weighted primarily on the CSV via recomputed structural inequalities.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_dband_centers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_type",
          "element",
          "atom_index",
          "epsilon_d"
        ],
        "units": {
          "epsilon_d": "eV"
        }
      },
      "description": "Table of every surface atom's local d-band center. The checker recomputes per-element ranges from this CSV and verifies required structural relationships (range broadening, overall span)."
    },
    {
      "file": "ranges_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "monometallic",
          "NMHEA",
          "overall_NMHEA"
        ],
        "items": {
          "monometallic": {
            "element": {
              "min": "float",
              "max": "float",
              "range": "float"
            }
          },
          "NMHEA": {
            "element": {
              "min": "float",
              "max": "float",
              "range": "float"
            }
          },
          "overall_NMHEA": {
            "min": "float",
            "max": "float"
          }
        }
      },
      "description": "Aggregated summary of epsilon_d ranges. The checker may validate structure and consistency with the CSV, but primary scoring is based on recomputation from the CSV."
    }
  ],
  "notes": "The workflow covers only the DFT-based d-band center analysis. Experimental spectra, HER activity, LDOS profile shape comparisons, and supervised learning regression are excluded per the defined scope. The agent must produce both artifacts; scoring is weighted primarily on the CSV via recomputed structural inequalities."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores each workflow stage's artifact. The verifier reads `surface_dband_centers.csv`, groups surface atoms by model type and element, recomputes per-element ε_d ranges, and checks that certain structural relationships hold between the monometallic and HEA datasets. A second check validates the structure and consistency of `ranges_summary.json` against the CSV. The final reward is a weighted combination of scores from these checks. Accuracy and completeness of the computed ε_d values, as reflected in the correctness of the derived structural trends, determine the score. Simply reporting a number without executing the workflow will not receive credit.
