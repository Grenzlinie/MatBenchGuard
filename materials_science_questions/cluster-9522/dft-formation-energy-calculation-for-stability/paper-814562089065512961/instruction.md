# DFT Formation Energy and Bader Charge Analysis of Mixed Na/Sr Lithium Titanate

## Problem background
Metal lithium titanates (MLTO) with formula MLi₂Ti₆O₁₄ (M = 2Na, Sr, Ca, Ba, Pb) are promising anode materials for lithium-ion batteries. The operating potential of these titanates is linked to the Ti³⁺/Ti⁴⁺ redox energy, which depends on the electron density on Ti atoms and can be influenced by the identity of the M cation. This work explores the possibility of tuning electrochemical properties by mixing two different M cations — sodium and strontium — to form solid solutions Na₂−₂ₓSrₓLi₂Ti₆O₁₄. To understand the thermodynamic stability and the mechanism of potential tuning, one must determine the formation energies of the mixed phases relative to the endmembers and quantify how the average electron density on Ti atoms changes across compositions.

## Approach
The approach uses first-principles density functional theory (DFT) to compute total energies and electron densities for a series of Na₂−₂ₓSrₓLi₂Ti₆O₁₄ compositions (x = 0, 0.25, 0.5, 0.75, 1). Crystal structures are constructed based on the known monoclinic MLTO structure (space group C₂/c). For each composition, geometry relaxation and a static calculation are performed with the PBE functional using a plane-wave pseudopotential code. From the relaxed total energies, formation energies (ΔG) of the mixed phases are evaluated relative to the pure endmembers Na₂Li₂Ti₆O₁₄ and SrLi₂Ti₆O₁₄. Separately, a grid-based Bader charge analysis of the charge density files from the DFT step yields the average Bader charge on the Ti atoms for each composition.

## Reproduction target
Produce two scored CSV files under `/app/outputs`:

- `formation_energies.csv` containing the composition label, the calculated total energy (eV), and the formation energy (kJ mol⁻¹) for each of the five compositions.
- `bader_charges.csv` containing the composition label and the average Bader charge on Ti atoms (in elementary charge e) for each composition.

The csv files must conform to the schemas listed in the Output Contract below, and the reported values must derive from the DFT workflow described in the steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Bader charge analysis code (Henkelman group): http://theory.cm.utexas.edu/henkelman/code/bader/
- Crystal structure of Na2Li2Ti6O14 and SrLi2Ti6O14: 10.1021/ic902262z

## Workflow steps

### Step 1: DFT total energy and structure relaxation
- Role: process
- Action: Construct crystal structure models for Na2-2xSrxLi2Ti6O14 with x = 0, 0.25, 0.5, 0.75, 1 based on the known MLTO structure (space group C2/c). Perform DFT total energy calculations (geometry relaxation and static calculation) using a plane-wave pseudopotential code (e.g., Quantum ESPRESSO) with the PBE functional. Output relaxed total energies, structural parameters, and charge density files required for the downstream analysis.
- Evidence: `/app/outputs/dft_results.json`

### Step 2: Compute formation energies
- Role: scored
- Action: From the total energies obtained in the DFT step, compute the formation energies (ΔG in kJ mol⁻¹) of Na2-2xSrxLi2Ti6O14 mixed phases relative to the endmembers Na2Li2Ti6O14 and SrLi2Ti6O14. Report the total energy and formation energy for all five compositions.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: CSV with columns: composition (string), total_energy_eV (float), formation_energy_kJ_mol (float). Five rows for x=0, 0.25, 0.5, 0.75, 1.
- Scoring: scored by hidden verifier

### Step 3: Compute Bader charges on Ti atoms
- Role: scored
- Action: Using the charge density files from the DFT step, perform a grid-based Bader charge analysis to calculate the average Bader charge on Ti atoms for each composition.
- Output file: `/app/outputs/bader_charges.csv`
- Format: csv
- Contract: CSV with columns: composition (string), avg_ti_bader_charge_e (float). Five rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/bader_charges.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Formation energies of Na2-2xSrxLi2Ti6O14 compositions. The checker verifies structural trends and internal consistency.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `total_energy_eV`, `formation_energy_kJ_mol`
  - `units`:
    - `total_energy_eV`: eV
    - `formation_energy_kJ_mol`: kJ mol⁻¹

### bader_charges.csv
- path: `/app/outputs/bader_charges.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average Bader charge on Ti atoms for each composition. The checker audits structural properties.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `avg_ti_bader_charge_e`
  - `units`:
    - `avg_ti_bader_charge_e`: e

Notes: The agent may use any open-source DFT code as an alternative to the commercial VASP. The formation energy step must report total energies from which formation energies can be recomputed. The Bader charge scoring relies on structural properties without stating the expected trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "total_energy_eV",
          "formation_energy_kJ_mol"
        ],
        "units": {
          "total_energy_eV": "eV",
          "formation_energy_kJ_mol": "kJ mol⁻¹"
        }
      },
      "description": "Formation energies of Na2-2xSrxLi2Ti6O14 compositions. The checker verifies structural trends and internal consistency."
    },
    {
      "file": "bader_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "avg_ti_bader_charge_e"
        ],
        "units": {
          "avg_ti_bader_charge_e": "e"
        }
      },
      "description": "Average Bader charge on Ti atoms for each composition. The checker audits structural properties."
    }
  ],
  "notes": "The agent may use any open-source DFT code as an alternative to the commercial VASP. The formation energy step must report total energies from which formation energies can be recomputed. The Bader charge scoring relies on structural properties without stating the expected trend."
}
```

## How you are scored
A hidden verifier independently scores each output file and combines the scores into a final reward between 0 and 1. The verifier checks that the formation energies satisfy the structural requirements stated in the output contract (e.g., physically meaningful sign for mixed compositions and a plausible relative ordering) and that the average Ti Bader charges follow the required trend across compositions. It may also recompute derived quantities from your submitted raw data to ensure internal consistency. A higher score reflects a more faithful reproduction of the expected physical trends and compliance with the output schema.
