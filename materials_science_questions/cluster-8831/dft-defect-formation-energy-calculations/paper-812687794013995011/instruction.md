# DFT Calculation of Vacancy Formation Energies in Si-Doped Amorphous ZnON

## Problem background
Zinc oxynitride (ZnON) thin-film transistors offer high field-effect mobility for next-generation displays, but their bias stability under negative gate stress remains a challenge. One proposed strategy to improve stability is silicon (Si) doping. It is thought that Si may suppress the formation of nitrogen vacancies ($V_N$), which act as carrier donors and trap sites. Density functional theory (DFT) calculations of vacancy formation energies can test this hypothesis. This task aims to compute the nitrogen vacancy formation energies in pure amorphous ZnON and in Si-doped amorphous ZnON to determine how Si doping affects $V_N$ stability.

## Approach
Ab initio molecular dynamics (MD) and hybrid-DFT calculations are used to model amorphous ZnON. Melt-quench MD simulations generate amorphous supercells with atomic compositions matching experimentally reported ratios: pure ZnON (N ~4.5 at%, O ~44.4 at%, Zn ~51.1 at%) and Si-doped ZnON (N ~2.3 at%, O ~47.8 at%, Si ~1.1 at%, Zn ~48.8 at%). The structures are relaxed using DFT, and the electronic band gap is computed. Nitrogen and oxygen vacancy defects are then created at multiple inequivalent sites in each relaxed cell, and total energies are calculated. Formation energies are derived using elemental chemical potentials from standard reference states (N₂ dimer, O₂ dimer, bulk Zn, bulk Si). The average $V_N$ formation energy in each system is compared to assess the effect of Si doping.

## Reproduction target
Produce the per-site formation energies for nitrogen and oxygen vacancies in both pure ZnON and Si-doped ZnON, output as a CSV file (`formation_energies.csv`) with columns: structure, vacancy_type, site_label, formation_energy (eV). Compute the average $V_N$ formation energy and the band gap for each material, and report them in a JSON summary (`summary.json`). The goal is to quantify whether Si doping substantially increases the $V_N$ formation energy, and to report the band gap values for both compositions.

## Assets

- Ab initio DFT and molecular dynamics code: cp2k

## Workflow steps

### Step 1: Generate amorphous ZnON supercells via melt-quench MD
- Role: process
- Action: Using ab initio molecular dynamics, generate amorphous ZnON and Si-doped ZnON supercells with compositions matching the experimentally reported atomic ratios: ZnON (N ~4.5 at%, O ~44.4 at%, Zn ~51.1 at%) and Si-doped (N ~2.3 at%, O ~47.8 at%, Si ~1.1 at%, Zn ~48.8 at%). Perform melt-and-quench to obtain disordered structures.
- Evidence: none

### Step 2: DFT geometry relaxation and electronic structure calculation
- Role: process
- Action: Relax the atomic positions of the generated supercells using DFT and compute the band gap for each structure (ZnON and Si-doped ZnON). Use a hybrid functional to obtain band gaps consistent with the experimental reference.
- Evidence: none

### Step 3: Calculate vacancy formation energies
- Role: scored (load-bearing)
- Action: For each relaxed structure, create nitrogen and oxygen vacancy defects at multiple inequivalent sites, compute total energies, and derive formation energies using chemical potentials of the elements (from standard reference states). Output the results to formation_energies.csv with columns: structure, vacancy_type, site_label, formation_energy.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: structure: string, vacancy_type: string, site_label: int, formation_energy: float
- Scoring: scored by hidden verifier

### Step 4: Compute summary metrics
- Role: scored
- Action: From the formation energies and the computed band gaps, compute the average V_N formation energy for ZnON and Si-doped, and report these together with the band gaps in summary.json with keys: ZnON.E_form_V_N_avg, ZnON.band_gap, Si_doped.E_form_V_N_avg, Si_doped.band_gap.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: { "ZnON": { "E_form_V_N_avg": float, "band_gap": float }, "Si_doped": { "E_form_V_N_avg": float, "band_gap": float } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-site vacancy formation energies for nitrogen and oxygen vacancies in pure ZnON and Si-doped ZnON structures.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `vacancy_type`, `site_label`, `formation_energy`
  - `units`:
    - `formation_energy`: eV

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Summary containing the average nitrogen vacancy formation energy and band gap for each material system.
- schema:
  - `type`: object
  - `required`:
    - `ZnON`:
      - `E_form_V_N_avg`: float
      - `band_gap`: float
    - `Si_doped`:
      - `E_form_V_N_avg`: float
      - `band_gap`: float

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "vacancy_type",
          "site_label",
          "formation_energy"
        ],
        "units": {
          "formation_energy": "eV"
        }
      },
      "description": "Per-site vacancy formation energies for nitrogen and oxygen vacancies in pure ZnON and Si-doped ZnON structures."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "ZnON": {
            "E_form_V_N_avg": "float",
            "band_gap": "float"
          },
          "Si_doped": {
            "E_form_V_N_avg": "float",
            "band_gap": "float"
          }
        }
      },
      "description": "Summary containing the average nitrogen vacancy formation energy and band gap for each material system."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently inspects each output file. For `formation_energies.csv`, it checks that the data structure is valid and compares the computed formation energies (especially the average $V_N$ energy per system) against reference values with appropriate tolerances. For `summary.json`, it extracts the average $V_N$ energies and band gaps and verifies that they are consistent with the CSV data and that the relative trend between the pure and Si-doped systems matches physical expectations derived from the published study. Reporting the paper’s numbers alone is insufficient; the verifier scores the outputs based on accuracy and trend agreement.
