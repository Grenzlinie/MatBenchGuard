# DFT Defect Formation Energy Calculations

## Problem background
Cation exchange in PbSe-CdSe heteronanocrystals during heating leads to epitaxial PbSe growth at the expense of CdSe, driven by Cd evaporation. The proposed solid–solid–vapor (SSV) mechanism relies on vacancy-mediated transport on the cation sublattice. Density functional theory (DFT) calculations of Frenkel pair formation energies in both materials can reveal whether the Se sublattice is energetically penalized relative to the cation sublattice, providing insight into the preferential cation-vacancy transport.

## Approach
Perform first-principles DFT calculations on supercells of wurtzite CdSe and rock-salt PbSe using the generalized gradient approximation (GGA) of Perdew, Burke, and Ernzerhof (PBE) and projector augmented wave (PAW) pseudopotentials. Compute the total energy of the perfect supercell and of supercells containing one cation Frenkel pair (vacancy + interstitial of the same cation) and one anion Frenkel pair (Se vacancy + Se interstitial). The Frenkel formation energy is obtained as E(defect) − E(perfect). The four formation energies (two per material) will be compared to understand the relative stability of cation versus anion defects.

## Reproduction target
Report the four Frenkel defect formation energies in eV: Cd Frenkel in wurtzite CdSe, Se Frenkel in wurtzite CdSe, Pb Frenkel in rock-salt PbSe, and Se Frenkel in rock-salt PbSe. Save these as a JSON file with keys CdSe_Frenkel_Cd, CdSe_Frenkel_Se, PbSe_Frenkel_Pb, PbSe_Frenkel_Se.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials for Cd, Pb, Se: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structure of wurtzite CdSe
- Crystal structure of rock-salt PbSe

## Workflow steps

### Step 1: DFT Defect Energy Calculations
- Role: scored (load-bearing)
- Action: Perform DFT calculations on supercells of wurtzite CdSe and rock-salt PbSe using the PBE exchange-correlation functional and PAW pseudopotentials. Compute total energies of the perfect supercell and of cells containing a cation Frenkel pair (vacancy and interstitial of the same cation species) and an anion Frenkel pair (Se vacancy and Se interstitial). Calculate the Frenkel formation energy as E(defect) - E(perfect) for each defect type. Report the four formation energies in eV.
- Output file: `/app/outputs/step_01_defect_energies.json`
- Format: json
- Contract: JSON object with keys: CdSe_Frenkel_Cd (float, eV), CdSe_Frenkel_Se (float, eV), PbSe_Frenkel_Pb (float, eV), PbSe_Frenkel_Se (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_defect_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_defect_energies.json
- path: `/app/outputs/step_01_defect_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Frenkel defect formation energies for cation and anion vacancies in CdSe and PbSe.
- schema:
  - `type`: object
  - `required`: `CdSe_Frenkel_Cd`, `CdSe_Frenkel_Se`, `PbSe_Frenkel_Pb`, `PbSe_Frenkel_Se`
  - `properties`:
    - `CdSe_Frenkel_Cd`:
      - `type`: number
      - `units`: eV
    - `CdSe_Frenkel_Se`:
      - `type`: number
      - `units`: eV
    - `PbSe_Frenkel_Pb`:
      - `type`: number
      - `units`: eV
    - `PbSe_Frenkel_Se`:
      - `type`: number
      - `units`: eV

Notes: The hidden checker will evaluate the reported defect formation energies against undisclosed physics-based criteria.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "CdSe_Frenkel_Cd",
          "CdSe_Frenkel_Se",
          "PbSe_Frenkel_Pb",
          "PbSe_Frenkel_Se"
        ],
        "properties": {
          "CdSe_Frenkel_Cd": {
            "type": "number",
            "units": "eV"
          },
          "CdSe_Frenkel_Se": {
            "type": "number",
            "units": "eV"
          },
          "PbSe_Frenkel_Pb": {
            "type": "number",
            "units": "eV"
          },
          "PbSe_Frenkel_Se": {
            "type": "number",
            "units": "eV"
          }
        }
      },
      "description": "Frenkel defect formation energies for cation and anion vacancies in CdSe and PbSe."
    }
  ],
  "notes": "The hidden checker will evaluate the reported defect formation energies against undisclosed physics-based criteria."
}
```

## How you are scored
A hidden verifier will inspect the file step_01_defect_energies.json. It will verify that the file contains the required keys and that the values are numerical. The verifier will then evaluate the energies using hidden criteria that reflect the physics of defect formation. The final reward is a score between 0 and 1.
