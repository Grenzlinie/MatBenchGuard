# First-principles electronic structure of oxygen-deficient amorphous ITO

## Problem background
Amorphous Sn-doped In2O3 (a-ITO) is a widely used transparent conducting oxide whose electronic properties are sensitive to oxygen vacancies, a common defect type. Understanding how oxygen deficiency alters the band gap and the spatial localization of electronic states is central to optimising its optoelectronic performance. This task investigates the electronic structure of stoichiometric and oxygen-deficient a-ITO using first-principles density-functional theory (DFT).

## Approach
The workflow constructs the amorphous network through melt-and-quench ab initio molecular dynamics (AIMD) starting from a crystalline 81-atom supercell of composition (SnO2)2(In2O3)15. After equilibration, a single oxygen vacancy is introduced to create the defective structure. Static DFT calculations with the PBE exchange-correlation functional and PAW pseudopotentials are performed on both the stoichiometric and oxygen-deficient configurations. From the resulting Kohn-Sham wavefunctions, the band gap at the Γ point and the normalized inverse participation ratio (IPR) of states near the valence and conduction band edges are computed. The two conditions (stoichiometric vs. oxygen-deficient) are compared to reveal the impact of the vacancy on the electronic structure.

## Reproduction target
Produce two JSON artifacts:

- `band_gap_report.json` containing the Γ-point band gaps (eV) for the stoichiometric and oxygen-deficient structures.
- `ipr_report.json` containing the average IPR values for states within 0.2 eV of the valence band edge (VBE) and conduction band edge (CBE) for both structures.

The hidden verifier will assess whether the reported band gaps and IPR averages exhibit the structural trends expected from oxygen deficiency, i.e., whether the defect induces a change in the gap and alters the localization near the band edges.

## Assets

- Quantum ESPRESSO (or equivalent DFT code with PAW support): https://www.quantum-espresso.org/download
- PAW pseudopotentials for In, Sn, O (PBE): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate stoichiometric a-ITO structure via melt-and-quench AIMD
- Role: process
- Action: Perform melt-and-quench ab initio molecular dynamics (AIMD) simulation to generate a stoichiometric amorphous Sn-doped In2O3 structure. Start from a crystalline 81-atom supercell of composition (SnO2)2(In2O3)15. Use a DFT code with PAW pseudopotentials. Melt at high temperature, quench, and anneal until the total energy and atomic structure converge. Output the final stoichiometric a-ITO atomic coordinates.
- Evidence: `/app/outputs/stoichiometric_aITO.cif`

### Step 2: Create oxygen‑deficient a-ITO structure
- Role: process
- Action: Remove one oxygen atom from the equilibrated stoichiometric a-ITO supercell generated in Step 1 to obtain the one‑oxygen‑missing defective structure.
- Evidence: `/app/outputs/odeficient_aITO.cif`

### Step 3: Static DFT calculation on stoichiometric a-ITO
- Role: process
- Action: Run a static DFT calculation on the stoichiometric a-ITO structure using the same DFT code and PAW pseudopotentials as in Step 1. Use an appropriately converged plane-wave cutoff and k‑point sampling. Retain the Kohn‑Sham wavefunctions and band structure data.
- Evidence: `/app/outputs/stoichiometric_dft.log`

### Step 4: Static DFT calculation on oxygen‑deficient a-ITO
- Role: process
- Action: Run a static DFT calculation on the oxygen‑deficient a-ITO structure with the same computational parameters as in Step 3. Retain the Kohn‑Sham wavefunctions and band structure data.
- Evidence: `/app/outputs/odeficient_dft.log`

### Step 5: Extract band gaps and write band_gap_report.json
- Role: scored (load-bearing)
- Action: From the band structure data of the stoichiometric and oxygen‑deficient calculations, determine the electronic band gap at the Γ point for each structure. Write the gaps (in eV) to band_gap_report.json with keys 'stoichiometric_gap_ev' and 'oxygen_deficient_gap_ev'.
- Output file: `/app/outputs/band_gap_report.json`
- Format: json
- Contract: {"stoichiometric_gap_ev": <float>, "oxygen_deficient_gap_ev": <float>}
- Scoring: scored by hidden verifier

### Step 6: Compute IPRs and write ipr_report.json
- Role: scored (load-bearing)
- Action: For each structure, compute the normalized inverse participation ratio (IPR) of the Kohn‑Sham wavefunctions. Use the formula IPR = (N Σ c_i⁴) / (Σ c_i²)², where c_i² is the partial weight on atom i and N is the number of atoms. Average the IPR over states within 0.2 eV of the valence band edge (VBE) and within 0.2 eV of the conduction band edge (CBE). Write the averages to ipr_report.json with keys 'stoichiometric_avg_ipr_vbe', 'stoichiometric_avg_ipr_cbe', 'oxygen_deficient_avg_ipr_vbe', 'oxygen_deficient_avg_ipr_cbe'.
- Output file: `/app/outputs/ipr_report.json`
- Format: json
- Contract: {"stoichiometric_avg_ipr_vbe": <float>, "stoichiometric_avg_ipr_cbe": <float>, "oxygen_deficient_avg_ipr_vbe": <float>, "oxygen_deficient_avg_ipr_cbe": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_report.json`
- `/app/outputs/ipr_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_report.json
- path: `/app/outputs/band_gap_report.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed band gaps (eV) at Γ for stoichiometric and oxygen-deficient a-ITO. A hidden verifier will assess the structural impact of oxygen deficiency.
- schema:
  - `type`: object
  - `properties`:
    - `stoichiometric_gap_ev`:
      - `type`: number
      - `unit`: eV
    - `oxygen_deficient_gap_ev`:
      - `type`: number
      - `unit`: eV
  - `required`: `stoichiometric_gap_ev`, `oxygen_deficient_gap_ev`

### ipr_report.json
- path: `/app/outputs/ipr_report.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Average inverse participation ratio near the valence and conduction band edges for stoichiometric and oxygen-deficient a-ITO. A hidden verifier will assess the structural impact of oxygen deficiency.
- schema:
  - `type`: object
  - `properties`:
    - `stoichiometric_avg_ipr_vbe`:
      - `type`: number
      - `unit`: dimensionless
    - `stoichiometric_avg_ipr_cbe`:
      - `type`: number
      - `unit`: dimensionless
    - `oxygen_deficient_avg_ipr_vbe`:
      - `type`: number
      - `unit`: dimensionless
    - `oxygen_deficient_avg_ipr_cbe`:
      - `type`: number
      - `unit`: dimensionless
  - `required`: `stoichiometric_avg_ipr_vbe`, `stoichiometric_avg_ipr_cbe`, `oxygen_deficient_avg_ipr_vbe`, `oxygen_deficient_avg_ipr_cbe`

Notes: The structural impact of oxygen deficiency on the electronic structure is assessed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "stoichiometric_gap_ev": {
            "type": "number",
            "unit": "eV"
          },
          "oxygen_deficient_gap_ev": {
            "type": "number",
            "unit": "eV"
          }
        },
        "required": [
          "stoichiometric_gap_ev",
          "oxygen_deficient_gap_ev"
        ]
      },
      "description": "Computed band gaps (eV) at Γ for stoichiometric and oxygen-deficient a-ITO. A hidden verifier will assess the structural impact of oxygen deficiency."
    },
    {
      "file": "ipr_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "stoichiometric_avg_ipr_vbe": {
            "type": "number",
            "unit": "dimensionless"
          },
          "stoichiometric_avg_ipr_cbe": {
            "type": "number",
            "unit": "dimensionless"
          },
          "oxygen_deficient_avg_ipr_vbe": {
            "type": "number",
            "unit": "dimensionless"
          },
          "oxygen_deficient_avg_ipr_cbe": {
            "type": "number",
            "unit": "dimensionless"
          }
        },
        "required": [
          "stoichiometric_avg_ipr_vbe",
          "stoichiometric_avg_ipr_cbe",
          "oxygen_deficient_avg_ipr_vbe",
          "oxygen_deficient_avg_ipr_cbe"
        ]
      },
      "description": "Average inverse participation ratio near the valence and conduction band edges for stoichiometric and oxygen-deficient a-ITO. A hidden verifier will assess the structural impact of oxygen deficiency."
    }
  ],
  "notes": "The structural impact of oxygen deficiency on the electronic structure is assessed."
}
```

## How you are scored
A hidden checker reads the two output files and validates their structure and key presence. It then assesses the structural impact of oxygen deficiency on the electronic structure. Each artifact carries a weight; missing or malformed JSON files receive zero credit for that artifact. The final reward is the weighted sum of the stage scores. Simply reporting a plausible number is not sufficient — the workflow steps must be executed, and the generated structures and DFT calculations must produce internally consistent results.
