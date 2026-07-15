# DFT Simulation of O2 Confinement in Ultramicropores

## Problem background
Heterogeneous activation of dioxygen (O2) into the superoxide radical (O2•−) is a critical step in many catalytic oxidation processes applied in environmental remediation and chemical synthesis. A central open question is why room‑temperature O2 activation occurs readily in sp²‑carbon materials with ultramicropores but not in non‑carbon analogues such as MgO or graphitic carbon nitride (C3N4). Elucidating this phenomenon requires quantifying the electron transfer, bond distortion, and adsorption thermodynamics when an O2 molecule is confined in slit‑shaped pores at the sub‑nanometre scale. This computational task reproduces the first‑principles study that probes those quantities as a function of pore diameter for graphene, MgO and C3N4.

## Approach
Density functional theory (DFT) calculations are used to model O2 molecules placed inside slit‑shaped pores formed by two parallel slabs of the host material. Three material classes are examined: graphene (representing sp²‑carbon), MgO (rock‑salt structure) and C3N4 (graphitic carbon nitride). For the carbon case, pore diameters are swept from 0.36 nm to 0.45 nm in 0.01 nm steps; for MgO and C3N4 a single pore diameter of 0.4 nm is computed. The electronic structure is treated with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and a van‑der‑Waals dispersion correction. Geometry relaxations are followed by Bader charge analysis to obtain the charge transferred from the host to the O2 molecule. In addition, the O–O bond length, the adsorption energy (Etotal – Epore_slab – EO2), and the Gibbs free energy of adsorption are extracted. The combined dataset enables a systematic comparison across pore sizes and materials, revealing the structural and electronic prerequisites for O2 activation in ultramicropores.

## Reproduction target
For carbon (graphene), compute the Bader charge transfer, O–O bond length, adsorption energy, and Gibbs free energy of O2 confined in slit pores with diameters from 0.36 nm to 0.45 nm (0.01 nm increment). For MgO and C3N4, compute the charge transfer at a pore diameter of 0.4 nm. Report all results in two CSV files (carbon_fine_scan.csv and material_comparison_D0.4.csv) with the columns and units specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader Charge Analysis: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build slit‑pore models
- Role: process
- Action: Construct atomic models of slit‑shaped pores for pristine graphene, MgO (rock‑salt), and C3N4 (graphitic carbon nitride) with pore diameters from 0.36 nm to 0.45 nm in 0.01 nm steps (for carbon) and at D=0.4 nm (for MgO and C3N4). Place an O2 molecule inside each pore.
- Evidence: `/app/outputs/slit_pore_models_created.log`

### Step 2: Run DFT relaxations
- Role: process
- Action: Perform DFT geometry optimization and total energy calculation for every model using Quantum ESPRESSO (PBE functional, van‑der‑Waals correction). Obtain relaxed geometries and charge densities.
- Evidence: `/app/outputs/dft_outputs.log`

### Step 3: Compute post‑processing quantities
- Role: process
- Action: From the DFT outputs, calculate Bader charge transfer (difference between O2 in the pore and free O2), O–O bond length, adsorption energy (E(total) – E(pore_slab) – E(O2)), and Gibbs free energy of adsorption for all pore diameters and materials.
- Evidence: `/app/outputs/computed_raw_data.json`

### Step 4: Write carbon fine‑scan CSV
- Role: scored
- Action: Write the computed values for carbon (graphene) at each pore diameter to /app/outputs/carbon_fine_scan.csv, with columns pore_diameter (nm), charge_transfer (|e|), oo_bond_length (Angstrom), adsorption_energy (eV), gibbs_free_energy (eV).
- Output file: `/app/outputs/carbon_fine_scan.csv`
- Format: csv
- Contract: pore_diameter (nm), charge_transfer (|e|), oo_bond_length (Angstrom), adsorption_energy (eV), gibbs_free_energy (eV)
- Scoring: scored by hidden verifier

### Step 5: Write material comparison CSV
- Role: scored
- Action: Write the computed charge transfer for MgO, C3N4, and carbon at D=0.4 nm to /app/outputs/material_comparison_D0.4.csv, with columns material (string), pore_diameter (nm), charge_transfer (|e|).
- Output file: `/app/outputs/material_comparison_D0.4.csv`
- Format: csv
- Contract: material (string), pore_diameter (nm), charge_transfer (|e|)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/carbon_fine_scan.csv`
- `/app/outputs/material_comparison_D0.4.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### carbon_fine_scan.csv
- path: `/app/outputs/carbon_fine_scan.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: DFT‑computed quantities for O2 inside carbon ultramicropores over the pore‑diameter range 0.36–0.45 nm.
- schema:
  - `type`: table
  - `required_columns`: `pore_diameter`, `charge_transfer`, `oo_bond_length`, `adsorption_energy`, `gibbs_free_energy`
  - `units`:
    - `pore_diameter`: nm
    - `charge_transfer`: |e|
    - `oo_bond_length`: Angstrom
    - `adsorption_energy`: eV
    - `gibbs_free_energy`: eV

### material_comparison_D0.4.csv
- path: `/app/outputs/material_comparison_D0.4.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bader charge transfer for O2 confined in slit‑pores of MgO, C3N4, and carbon at a pore diameter of 0.4 nm.
- schema:
  - `type`: table
  - `required_columns`: `material`, `pore_diameter`, `charge_transfer`
  - `units`:
    - `pore_diameter`: nm
    - `charge_transfer`: |e|

Notes: The checker compares the values in these CSV files to the paper's reported DFT reference values (hidden) with appropriate tolerances. The scored artifacts are result‑level comparisons; recomputation from a lighter artifact is not feasible for DFT outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "carbon_fine_scan.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pore_diameter",
          "charge_transfer",
          "oo_bond_length",
          "adsorption_energy",
          "gibbs_free_energy"
        ],
        "units": {
          "pore_diameter": "nm",
          "charge_transfer": "|e|",
          "oo_bond_length": "Angstrom",
          "adsorption_energy": "eV",
          "gibbs_free_energy": "eV"
        }
      },
      "description": "DFT‑computed quantities for O2 inside carbon ultramicropores over the pore‑diameter range 0.36–0.45 nm."
    },
    {
      "file": "material_comparison_D0.4.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "pore_diameter",
          "charge_transfer"
        ],
        "units": {
          "pore_diameter": "nm",
          "charge_transfer": "|e|"
        }
      },
      "description": "Bader charge transfer for O2 confined in slit‑pores of MgO, C3N4, and carbon at a pore diameter of 0.4 nm."
    }
  ],
  "notes": "The checker compares the values in these CSV files to the paper's reported DFT reference values (hidden) with appropriate tolerances. The scored artifacts are result‑level comparisons; recomputation from a lighter artifact is not feasible for DFT outputs."
}
```

## How you are scored
A hidden verifier will inspect your two CSV output files. It compares your computed quantities to reference targets that reflect the expected physical behaviour (charge transfer magnitude, bond‑length trends, sign changes of adsorption energies, and relative ordering across materials) using appropriate numerical tolerances. Each file receives a score, and the final reward (a float between 0 and 1) is a weighted combination of those scores. Ticking every box of the workflow is necessary but not sufficient; the values themselves must be physically consistent and fall within the expected ranges derived from the independent reference study. No single “correct” number is provided, but consistent, well‑executed DFT calculations will naturally satisfy the verifier’s criteria.
