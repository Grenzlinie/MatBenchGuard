# DFT Property Reproduction for Planar Hexacoordinate SiSb3Ca3+ Cluster

## Problem background
Planar hypercoordination is exceptionally rare for main-group elements, and achieving a planar hexacoordinate silicon (phSi) is an outstanding challenge. Recently, a family of clusters with global minimum D3h-symmetric structures, SiE3M3+ (E = N, P, As, Sb; M = Ca, Sr, Ba), was proposed. For the composition SiSb3Ca3+, the bonding is described as three Si–Sb multiple bonds complemented by three Si–Ca ionic bonds, which would constitute a true planar hexacoordinate silicon motif. The stability is attributed to π-localized Si–Sb covalent bonding and electrostatic interactions with the Ca ligands. This task aims to reproduce the key structural, bonding, charge, and energetic properties of that D3h SiSb3Ca3+ cluster at the density functional theory level, providing a quantitative verification of the bonding picture.

## Approach
The investigation employs Kohn–Sham density functional theory (DFT) with the hybrid PBE0 functional and the all-electron def2-TZVP basis set. Starting from a D3h-symmetric initial guess with Si at the origin, Sb atoms at roughly 2.6 Å, and Ca atoms at roughly 3.2 Å, a full geometry optimization is performed, followed by a harmonic vibrational frequency calculation to confirm that the optimized structure is a local minimum. The wavefunction obtained from the DFT calculation is then analyzed to extract chemical bonding information: Natural Population Analysis (NPA) charges, Wiberg bond indices, Adaptive Natural Density Partitioning (AdNDP) bonding patterns, and Interacting Quantum Atoms (IQA) energy decomposition. All calculations use the open-source ORCA package for DFT and the Multiwfn program for post-processing analyses. The workflow targets the single D3h isomer; no potential energy surface exploration is required.

## Reproduction target
Compute the following properties of the optimized D3h-symmetric SiSb3Ca3+ cluster at the PBE0/def2-TZVP level:
- Si–Sb and Si–Ca bond distances (Å)
- Wiberg bond index (WBI) for the Si–Sb bond
- NPA charges (|e|) on Si, Sb, and Ca
- From AdNDP analysis: occupation numbers of the three 2c-2e σ bonds and of the three 4c-2e π bonds
- IQA interaction energy components (kcal/mol) for the Si–Ca pair: V_Total, V_Ionic, and V_Coval
All values must be written to a JSON file following the specified schema.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- Multiwfn: http://sobereva.com/multiwfn/

## Workflow steps

### Step 1: Geometry optimization and frequency calculation
- Role: process
- Action: Build a D3h symmetric initial guess for SiSb3Ca3+ with Si at origin, Sb atoms at roughly 2.6 Å and Ca atoms at roughly 3.2 Å along the threefold axes. Run full geometry optimization and harmonic vibrational frequency calculation at the PBE0/def2-TZVP level using ORCA. Verify the structure is a local minimum (no imaginary frequencies). Save the optimized geometry (XYZ) and the wavefunction (Molden or WFN) for later analysis.
- Evidence: `/app/outputs/SiSb3Ca3_opt.xyz`

### Step 2: Compute key properties and write scored output
- Role: scored (load-bearing)
- Action: Using Multiwfn, load the wavefunction file from Step 1. Determine Si-Sb and Si-Ca bond distances from the geometry. Compute Wiberg bond indices for Si-Sb bonds, Natural Population Analysis (NPA) charges on Si, Sb, Ca, perform AdNDP analysis to identify three 2c-2e σ bonds and three 4c-2e π bonds and record their occupation numbers. Compute IQA decomposition for the Si-Ca interaction to get V_Total, V_Ionic and V_Coval. Write all results to outputs.json following the schema.
- Output file: `/app/outputs/outputs.json`
- Format: json
- Contract: {"type":"object","properties":{"B_Si_Sb":{"type":"number","unit":"angstrom"},"B_Si_Ca":{"type":"number","unit":"angstrom"},"WBI_Si_Sb":{"type":"number"},"Q_Si":{"type":"number","unit":"|e|"},"Q_Sb":{"type":"number","unit":"|e|"},"Q_Ca":{"type":"number","unit":"|e|"},"AdNDP_3c2e_sigma_ON":{"type":"number"},"AdNDP_4c2e_pi_ON":{"type":"number"},"IQA_V_Total_Si_Ca":{"type":"number","unit":"kcal/mol"},"IQA_V_Ionic_Si_Ca":{"type":"number","unit":"kcal/mol"},"IQA_V_Coval_Si_Ca":{"type":"number","unit":"kcal/mol"}},"required":["B_Si_Sb","B_Si_Ca","WBI_Si_Sb","Q_Si","Q_Sb","Q_Ca","AdNDP_3c2e_sigma_ON","AdNDP_4c2e_pi_ON"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/outputs.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### outputs.json
- path: `/app/outputs/outputs.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed structural, bonding, charge, and energetic properties of the D3h SiSb3Ca3+ cluster. Checked against hidden reference values derived from the paper, with tolerances appropriate for DFT re-runs.
- schema:
  - `type`: object
  - `properties`:
    - `B_Si_Sb`:
      - `type`: number
      - `unit`: angstrom
    - `B_Si_Ca`:
      - `type`: number
      - `unit`: angstrom
    - `WBI_Si_Sb`:
      - `type`: number
    - `Q_Si`:
      - `type`: number
      - `unit`: |e|
    - `Q_Sb`:
      - `type`: number
      - `unit`: |e|
    - `Q_Ca`:
      - `type`: number
      - `unit`: |e|
    - `AdNDP_3c2e_sigma_ON`:
      - `type`: number
    - `AdNDP_4c2e_pi_ON`:
      - `type`: number
    - `IQA_V_Total_Si_Ca`:
      - `type`: number
      - `unit`: kcal/mol
    - `IQA_V_Ionic_Si_Ca`:
      - `type`: number
      - `unit`: kcal/mol
    - `IQA_V_Coval_Si_Ca`:
      - `type`: number
      - `unit`: kcal/mol
  - `required`: `B_Si_Sb`, `B_Si_Ca`, `WBI_Si_Sb`, `Q_Si`, `Q_Sb`, `Q_Ca`, `AdNDP_3c2e_sigma_ON`, `AdNDP_4c2e_pi_ON`

Notes: IQA fields (V_Total, V_Ionic, V_Coval) are encouraged but not required; if missing they score 0 for the IQA portion. The required fields must be present. All values are numeric; units are indicated. The hidden checker compares each field to reference values with predefined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "outputs.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "B_Si_Sb": {
            "type": "number",
            "unit": "angstrom"
          },
          "B_Si_Ca": {
            "type": "number",
            "unit": "angstrom"
          },
          "WBI_Si_Sb": {
            "type": "number"
          },
          "Q_Si": {
            "type": "number",
            "unit": "|e|"
          },
          "Q_Sb": {
            "type": "number",
            "unit": "|e|"
          },
          "Q_Ca": {
            "type": "number",
            "unit": "|e|"
          },
          "AdNDP_3c2e_sigma_ON": {
            "type": "number"
          },
          "AdNDP_4c2e_pi_ON": {
            "type": "number"
          },
          "IQA_V_Total_Si_Ca": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "IQA_V_Ionic_Si_Ca": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "IQA_V_Coval_Si_Ca": {
            "type": "number",
            "unit": "kcal/mol"
          }
        },
        "required": [
          "B_Si_Sb",
          "B_Si_Ca",
          "WBI_Si_Sb",
          "Q_Si",
          "Q_Sb",
          "Q_Ca",
          "AdNDP_3c2e_sigma_ON",
          "AdNDP_4c2e_pi_ON"
        ]
      },
      "description": "Computed structural, bonding, charge, and energetic properties of the D3h SiSb3Ca3+ cluster. Checked against hidden reference values derived from the paper, with tolerances appropriate for DFT re-runs."
    }
  ],
  "notes": "IQA fields (V_Total, V_Ionic, V_Coval) are encouraged but not required; if missing they score 0 for the IQA portion. The required fields must be present. All values are numeric; units are indicated. The hidden checker compares each field to reference values with predefined tolerances."
}
```

## How you are scored
A hidden verifier reads the submitted output JSON and compares each reported quantity to a reference set derived from the same computational protocol. The comparison uses tolerances that reflect the expected spread when re-running the calculation with a different code/settings. The final reward is a weighted sum: structural parameters and WBI contribute 30%, NPA charges 20%, AdNDP occupation numbers 20%, and IQA interaction energies 30%. Meeting or exceeding the expected value (i.e., staying within tolerance) earns full credit for that component; the reward decreases monotonically with larger deviations. If any required field is missing, its component scores zero. The verifier does not use exact equality; it rewards physical agreement, not bitwise reproduction.
