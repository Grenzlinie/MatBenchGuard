# DFT Formation Enthalpy Calculation for Binary Intermetallic Stability

## Problem background
The Zr–Sn binary system contains intermetallic compounds relevant to nuclear fuel cladding. Two unresolved questions are: (1) whether the Zr5Sn4 phase is thermodynamically stable relative to Zr5Sn3 and ZrSn2, and (2) whether the off-stoichiometric Zr4Sn compound (A15-type) is stabilized by Sn vacancies or Zr anti-site defects. First-principles DFT calculations can resolve both by computing formation enthalpies and comparing the stability of competing structural models.

## Approach
Use first-principles density-functional theory (DFT) with the generalized gradient approximation (GGA-PBE) and projector augmented-wave (PAW) pseudopotentials. Compute total energies for pure Zr and Sn as reference states, for stoichiometric intermetallic compounds (Zr5Sn3, Zr5Sn4, ZrSn2, and the ideal A15 Zr3Sn), and for defect supercell models of Zr4Sn: a 2×2×2 A15 supercell with Sn vacancies (Zr48(Sn12Va4)) and three with Zr anti-site substitutions (Zr48(Sn15Zr1), Zr48(Sn13Zr3), Zr48(Sn12Zr4)). For each structure, relax cell parameters and atomic positions to obtain minimum total energies. Then extract the formation enthalpy per mole of atoms as ΔH = E_total(compound) − (1−c)·E_total(hcp Zr) − c·E_total(bct Sn). The stability of Zr5Sn4 is judged by comparing its enthalpy to neighbouring hexagonal phases; the defect type in Zr4Sn is determined by which defect model yields the most negative enthalpy. Use an open-source plane-wave pseudopotential code (e.g., Quantum ESPRESSO) and PAW-PBE pseudopotentials for Zr and Sn (obtainable from the SSSP library or the QE pseudopotential repository).

## Reproduction target
Compute the formation enthalpy (kJ/mol) for each of the following intermetallic compounds and defect models and report all values in a single JSON file: Zr5Sn3, Zr5Sn4, ZrSn2, ideal Zr3Sn, and the defect supercell models Zr48_Sn12_Va4, Zr48_Sn15_Zr1, Zr48_Sn13_Zr3, Zr48_Sn12_Zr4. The JSON output must use exactly those keys and provide a numeric enthalpy for each.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Zr PAW-PBE pseudopotential (e.g., Zr.pbe-n-kjpaw_psl.1.0.0.UPF): https://www.materialscloud.org/discover/sssp/table
- Sn PAW-PBE pseudopotential (e.g., Sn.pbe-dn-kjpaw_psl.1.0.0.UPF): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Reference total energy calculations for pure elements
- Role: process
- Action: Perform DFT total energy calculations with Quantum ESPRESSO (GGA-PBE, PAW pseudopotentials) for pure hcp Zr and bct Sn. Use adequate k-point sampling and plane-wave cutoffs. Fully relax cell volume and atomic positions to obtain minimum total energies. These reference energies are needed to compute formation enthalpies.
- Evidence: `/app/outputs/reference_energies.json`

### Step 2: Total energy calculations for stoichiometric intermetallic compounds
- Role: process
- Action: Construct crystal structures for the stoichiometric compounds Zr5Sn3 (Mn5Si3-type), Zr5Sn4 (Ti5Ga4-type), ZrSn2 (orthorhombic), and the ideal A15 Zr3Sn. Run DFT total energy calculations with full relaxation (cell volume and internal positions) using the same pseudopotential and exchange-correlation settings. Output relaxed total energies for each compound.
- Evidence: `/app/outputs/stoich_total_energies.json`

### Step 3: Total energy calculations for Zr4Sn defect supercell models
- Role: process
- Action: Construct 2×2×2 A15 supercells (64 sites) for the competing defect models: Sn‑vacancy model Zr48(Sn12Va4) (vacancies on an fcc sublattice) and three Zr anti‑site models Zr48(Sn15Zr1), Zr48(Sn13Zr3), Zr48(Sn12Zr4). Run DFT total energy calculations with full relaxation under the same settings. Output relaxed total energies for each supercell.
- Evidence: `/app/outputs/defect_total_energies.json`

### Step 4: Compute and report formation enthalpies
- Role: scored (load-bearing)
- Action: From the total energies obtained in the previous steps, compute the formation enthalpy for each compound and defect supercell as ΔH = E_total(compound) - (1-c)*E_total(hcp Zr) - c*E_total(bct Sn). Report all enthalpies in kJ/mol in the output JSON file.
- Output file: `/app/outputs/formation_enthalpies.json`
- Format: json
- Contract: A JSON object with exactly these keys: 'Zr5Sn3', 'Zr5Sn4', 'ZrSn2', 'Zr3Sn', 'Zr48_Sn12_Va4', 'Zr48_Sn15_Zr1', 'Zr48_Sn13_Zr3', 'Zr48_Sn12_Zr4'. Each value is a number representing the formation enthalpy in kJ/mol (per mole of atoms).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_enthalpies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_enthalpies.json
- path: `/app/outputs/formation_enthalpies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation enthalpies (kJ/mol) of Zr-Sn intermetallic compounds and A15 defect supercell models computed from DFT total energies.
- schema:
  - `type`: object
  - `required`: `Zr5Sn3`, `Zr5Sn4`, `ZrSn2`, `Zr3Sn`, `Zr48_Sn12_Va4`, `Zr48_Sn15_Zr1`, `Zr48_Sn13_Zr3`, `Zr48_Sn12_Zr4`
  - `properties`:
    - `Zr5Sn3`:
      - `type`: number
      - `description`: Formation enthalpy of Zr5Sn3 (kJ/mol)
    - `Zr5Sn4`:
      - `type`: number
      - `description`: Formation enthalpy of Zr5Sn4 (kJ/mol)
    - `ZrSn2`:
      - `type`: number
      - `description`: Formation enthalpy of ZrSn2 (kJ/mol)
    - `Zr3Sn`:
      - `type`: number
      - `description`: Formation enthalpy of ideal A15 Zr3Sn (kJ/mol)
    - `Zr48_Sn12_Va4`:
      - `type`: number
      - `description`: Formation enthalpy of Sn-vacancy model (kJ/mol)
    - `Zr48_Sn15_Zr1`:
      - `type`: number
      - `description`: Formation enthalpy of Zr anti-site model with 1 Zr substitution (kJ/mol)
    - `Zr48_Sn13_Zr3`:
      - `type`: number
      - `description`: Formation enthalpy of Zr anti-site model with 3 Zr substitutions (kJ/mol)
    - `Zr48_Sn12_Zr4`:
      - `type`: number
      - `description`: Formation enthalpy of Zr anti-site model with 4 Zr substitutions (kJ/mol)

Notes: Values are compared to the original paper's calculated enthalpies with a tolerance; relative ordering constraints among A15 models and hexagonal phases are also enforced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_enthalpies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Zr5Sn3",
          "Zr5Sn4",
          "ZrSn2",
          "Zr3Sn",
          "Zr48_Sn12_Va4",
          "Zr48_Sn15_Zr1",
          "Zr48_Sn13_Zr3",
          "Zr48_Sn12_Zr4"
        ],
        "properties": {
          "Zr5Sn3": {
            "type": "number",
            "description": "Formation enthalpy of Zr5Sn3 (kJ/mol)"
          },
          "Zr5Sn4": {
            "type": "number",
            "description": "Formation enthalpy of Zr5Sn4 (kJ/mol)"
          },
          "ZrSn2": {
            "type": "number",
            "description": "Formation enthalpy of ZrSn2 (kJ/mol)"
          },
          "Zr3Sn": {
            "type": "number",
            "description": "Formation enthalpy of ideal A15 Zr3Sn (kJ/mol)"
          },
          "Zr48_Sn12_Va4": {
            "type": "number",
            "description": "Formation enthalpy of Sn-vacancy model (kJ/mol)"
          },
          "Zr48_Sn15_Zr1": {
            "type": "number",
            "description": "Formation enthalpy of Zr anti-site model with 1 Zr substitution (kJ/mol)"
          },
          "Zr48_Sn13_Zr3": {
            "type": "number",
            "description": "Formation enthalpy of Zr anti-site model with 3 Zr substitutions (kJ/mol)"
          },
          "Zr48_Sn12_Zr4": {
            "type": "number",
            "description": "Formation enthalpy of Zr anti-site model with 4 Zr substitutions (kJ/mol)"
          }
        }
      },
      "description": "Formation enthalpies (kJ/mol) of Zr-Sn intermetallic compounds and A15 defect supercell models computed from DFT total energies."
    }
  ],
  "notes": "Values are compared to the original paper's calculated enthalpies with a tolerance; relative ordering constraints among A15 models and hexagonal phases are also enforced."
}
```

## How you are scored
A hidden verifier checks each workflow stage's artifact independently. Process-stage evidence files (reference_energies.json, stoich_total_energies.json, defect_total_energies.json) are inspected for completeness and consistency; the final scored artifact (formation_enthalpies.json) is compared to expected values and relative ordering constraints. The final reward is a weighted sum across all stages. Do not simply report the paper's published numbers; you must execute the calculation and produce the artifacts as described. The verifier makes its own comparison and does not require you to know the exact expected values.
