# DFT analysis of N-doped graphene active sites for ORR

## Problem background
Nitrogen-doped graphene has emerged as a highly promising metal-free catalyst for the oxygen reduction reaction (ORR), which is critical for fuel cells and metal–air batteries. However, the role of different nitrogen configurations — pyridinic, graphitic, pyrrolic — and whether they are located inside or at the edge of the graphene sheet is actively debated. Understanding which nitrogen environment creates the most active sites and the lowest electronic band gap is essential for designing better catalysts. This task focuses on the computational investigation of these structure–property relationships using density functional theory (DFT).

## Approach
We use spin‑polarized DFT calculations to model five stable N‑doped graphene configurations: Graphitic N‑inside, Graphitic N‑edge, Pyridinic N‑inside, Pyridinic N‑edge, and Pyrrolic N‑edge. For each configuration, we construct a periodic supercell of graphene with the nitrogen substitution at the designated position, terminating edge carbon atoms with hydrogen. We then perform a self‑consistent electronic structure calculation using the GGA‑PBE exchange‑correlation functional and ultrasoft pseudopotentials. From the resulting Kohn–Sham eigenvalues, we extract the highest occupied and lowest unoccupied molecular orbital energies and their gap (HOMO–LUMO gap). We also compute Löwdin atomic charges and spins to identify atoms with large charge or spin density, which are candidate active sites for ORR. By comparing the gaps and active‑site counts across configurations, we determine which doping environment leads to the most favorable catalytic properties.

## Reproduction target
You will build the five N‑doped graphene models, run the DFT calculations, and produce two scored artifacts: (1) a CSV file containing the HOMO, LUMO, and HOMO–LUMO gap (in eV) for each configuration; (2) a JSON file listing, for each configuration, every atom whose absolute Löwdin charge exceeds 0.1 or whose absolute spin exceeds 0.1, together with its element, charge, and spin. The verifier will evaluate whether your reported gaps and the assignment of active sites are in agreement with the expected results derived from the DFT calculations, allowing for small numerical differences due to implementation choices.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org/download
- SSSP pseudopotential library (GGA-PBE ultrasoft): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build N-doped graphene models
- Role: process
- Action: Construct atomic models for five N-doped graphene configurations: Graphitic N-inside, Graphitic N-edge, Pyridinic N-inside, Pyridinic N-edge, Pyrrolic N-edge. Create periodic graphene supercells with >10 Å vacuum and edge C atoms terminated by H. Write coordinate files (e.g., QE input format) to a directory.
- Evidence: none

### Step 2: Run spin-polarized DFT calculations
- Role: process
- Action: For each model, run Quantum ESPRESSO PWscf with spin polarization, GGA-PBE, ultrasoft pseudopotentials, gamma-point k-sampling. Save standard output and charge density files.
- Evidence: none

### Step 3: Compute HOMO-LUMO gaps
- Role: scored
- Action: Extract HOMO and LUMO eigenvalues from DFT outputs. Compute gap (LUMO - HOMO) in eV. Write a CSV file.
- Output file: `/app/outputs/homolumo_gaps.csv`
- Format: csv
- Contract: config_name (string), homo (float, eV), lumo (float, eV), gap (float, eV). One row per configuration.
- Scoring: scored by hidden verifier

### Step 4: Identify active sites
- Role: scored (load-bearing)
- Action: Compute Löwdin atomic charges and spins from DFT charge density. For each configuration, list atoms with |charge| > 0.1 or |spin| > 0.1 as active sites. Write a JSON file.
- Output file: `/app/outputs/active_sites.json`
- Format: json
- Contract: A JSON object: keys are configuration names (e.g., 'Pyridinic N-edge'), values are arrays of objects with fields atom_label (string), element (string), charge (float), spin (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homolumo_gaps.csv`
- `/app/outputs/active_sites.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homolumo_gaps.csv
- path: `/app/outputs/homolumo_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: HOMO-LUMO energy gaps for each configuration. Compared to paper-reported values within ±0.05 eV tolerance.
- schema:
  - `type`: table
  - `required_columns`: `config_name`, `homo`, `lumo`, `gap`
  - `units`:
    - `homo`: eV
    - `lumo`: eV
    - `gap`: eV
  - `description`: One row per N-doped graphene configuration; config_name is one of Graphitic N-inside, Graphitic N-edge, Pyridinic N-inside, Pyridinic N-edge, Pyrrolic N-edge.

### active_sites.json
- path: `/app/outputs/active_sites.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Active site lists for each N-doping configuration. Compared to paper-reported active site assignments within tolerance for charge and spin values.
- schema:
  - `type`: object
  - `keys`: configuration names (strings)
  - `values`: array of objects: { atom_label: string, element: string, charge: float, spin: float }
  - `description`: Each object contains the atom label (e.g., 'N11'), element symbol, Löwdin atomic charge, and atomic spin. Atoms with |charge|>0.1 or |spin|>0.1 are identified as active sites.

Notes: All values are derived from the spin-polarized DFT calculations. The checker compares the reported gaps and active site lists to the paper's results using appropriate tolerances (gaps: ±0.05 eV; charges/spins: ±0.02).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homolumo_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "config_name",
          "homo",
          "lumo",
          "gap"
        ],
        "units": {
          "homo": "eV",
          "lumo": "eV",
          "gap": "eV"
        },
        "description": "One row per N-doped graphene configuration; config_name is one of Graphitic N-inside, Graphitic N-edge, Pyridinic N-inside, Pyridinic N-edge, Pyrrolic N-edge."
      },
      "description": "HOMO-LUMO energy gaps for each configuration. Compared to paper-reported values within ±0.05 eV tolerance."
    },
    {
      "file": "active_sites.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "keys": "configuration names (strings)",
        "values": "array of objects: { atom_label: string, element: string, charge: float, spin: float }",
        "description": "Each object contains the atom label (e.g., 'N11'), element symbol, Löwdin atomic charge, and atomic spin. Atoms with |charge|>0.1 or |spin|>0.1 are identified as active sites."
      },
      "description": "Active site lists for each N-doping configuration. Compared to paper-reported active site assignments within tolerance for charge and spin values."
    }
  ],
  "notes": "All values are derived from the spin-polarized DFT calculations. The checker compares the reported gaps and active site lists to the paper's results using appropriate tolerances (gaps: ±0.05 eV; charges/spins: ±0.02)."
}
```

## How you are scored
The hidden verifier independently checks your two output files against reference data generated by the same computational protocol. Each file is scored according to its declared target policy: exact_match for gaps (with a tolerance that accounts for pseudopotential and numerical differences) and reference_match for active sites (matching atom labels and charge/spin values within a tolerance). The two scores are weighted — the active_sites.json file carries the larger weight because it is the principal load‑bearing result — and combined into a final reward between 0 and 1. Merely guessing the paper’s reported numbers without actually performing the DFT workflow will not yield a satisfactory score.
