# First-Principles Calculation of Half-Metallicity and Intermediate Band in Cr-Doped ZnTe

## Problem background
Cr-doped ZnTe is a dilute magnetic semiconductor that has attracted attention for spintronics and intermediate-band solar cells. When Cr substitutes Zn at low concentrations, a partially filled impurity band can appear inside the host band gap, potentially leading to half-metallic behavior or an isolated intermediate band. The electronic structure is sensitive to strong electron correlations on the Cr 3d orbitals, which are often treated with an on-site Hubbard U term. Understanding how the band structure—especially the gap between valence band and intermediate band, the intermediate band width, and the minority-spin gap—changes with Cr concentration and U is essential for predicting material functionality. This task asks you to compute these properties from first principles and report the quantitative results.

## Approach
The task employs spin-polarized density functional theory within the local spin density approximation (LSDA) and its extension LSDA+U. Starting from 64-atom zinc-blende ZnTe supercells with an experimental lattice constant of 6.10 Å, you will construct two Cr concentrations by substituting Zn atoms: x = 1/32 (one Cr) and x = 2/32 (two Cr). For each concentration, you will perform ferromagnetic DFT calculations at three Hubbard U values: 0 eV (pure LSDA), 3 eV, and 6 eV. To confirm that the ferromagnetic state is the ground state for the higher concentration, you will also compute the total energy of the antiferromagnetic alignment for x = 2/32. From the self-consistent electronic structure, you will extract the energy positions of the valence band, conduction band, and intermediate band for both spin channels, integrate the projected density of states within the intermediate band, and compute Mulliken orbital populations on the Cr atom. The workflow uses a publicly available DFT code (SIESTA or Quantum ESPRESSO) with Troullier‑Martins pseudopotentials. The final output is a structured JSON file containing all the extracted numerical quantities.

## Reproduction target
Produce a JSON file, results.json, with top-level keys for each condition: 'x1_32_U0', 'x1_32_U3', 'x1_32_U6', 'x2_32_U0', 'x2_32_U3', 'x2_32_U6'. Each key holds an object with the following numeric fields: the majority-spin VB-IB gap (Delta_E_VI, eV), the IB bandwidth (Delta_E_I, eV), the majority-spin IB-CB gap (Delta_E_IC, eV), the minority-spin VB-CB gap (Delta_E_VC, eV), the integrated majority-spin DOS from IB bottom to Fermi energy (int_DOS_below_Fermi, electrons per cell) and from Fermi energy to IB top (int_DOS_above_Fermi, electrons per cell), and the Mulliken charges per spin: total charge (q_plus, q_minus), t-orbital populations (t_plus, t_minus), e-orbital populations (e_plus, e_minus), and p-orbital populations (p_plus, p_minus). All values must be obtained directly from your DFT output.

## Assets

- SIESTA code (or equivalent DFT+U package): https://gitlab.com/siesta-project/siesta
- Troullier-Martins pseudopotentials for Zn, Te, Cr: https://www.quantum-espresso.org/pseudopotentials
- Python 3 standard library: python3

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Generate 64-atom zinc-blende ZnTe supercells (lattice constant 6.10 Å) and create Cr-doped configurations for x=1/32 and x=2/32 by replacing Zn atoms with Cr. Write atomic coordinates to a file (e.g., supercells.xyz).
- Evidence: `/app/outputs/supercells.xyz`

### Step 2: LSDA and LSDA+U calculations
- Role: process
- Action: For each Cr concentration (x=1/32, x=2/32) run spin-polarized DFT with ferromagnetic alignment using LSDA and LSDA+U with Hubbard U = 0, 3, 6 eV. Use double-zeta polarized basis, Troullier-Martins pseudopotentials, and 18 special k-points. For x=2/32 also compute the total energy of the antiferromagnetic configuration to confirm FM ground state. Save all output files (band structure, total and projected DOS, Mulliken charges) in a directory for later parsing.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 3: Extract numerical results
- Role: scored (load-bearing)
- Action: From the DFT output, extract: VB-IB gap (Delta_E_VI, eV), IB bandwidth (Delta_E_I, eV), IB-CB gap (Delta_E_IC, eV), minority-spin VB-CB gap (Delta_E_VC, eV); the integrated number of electrons in the IB from IB bottom to Fermi energy (int_DOS_below_Fermi) and from Fermi energy to IB top (int_DOS_above_Fermi); and Mulliken orbital populations per spin (q_plus, q_minus, t_plus, t_minus, e_plus, e_minus, p_plus, p_minus) for the Cr atom. Do this for both concentrations and all U values. Write results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys: 'x1_32_U0', 'x1_32_U3', 'x1_32_U6', 'x2_32_U0', 'x2_32_U3', 'x2_32_U6'. Each value is an object with numeric fields: 'Delta_E_VI', 'Delta_E_I', 'Delta_E_IC', 'Delta_E_VC', 'int_DOS_below_Fermi', 'int_DOS_above_Fermi', 'q_plus', 'q_minus', 't_plus', 't_minus', 'e_plus', 'e_minus', 'p_plus', 'p_minus'. Energies in eV, integrated DOS in electrons per cell, Mulliken charges in electrons.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Compiled electronic structure results for all Cr concentrations and U values, including band gaps, IB bandwidths, integrated DOS occupancies, and Mulliken orbital populations.
- schema:
  - `type`: object
  - `required`: `x1_32_U0`, `x1_32_U3`, `x1_32_U6`, `x2_32_U0`, `x2_32_U3`, `x2_32_U6`
  - `additionalProperties`: False
  - `properties`:
    - `x1_32_U0`:
      - `type`: object
      - `required`: `Delta_E_VI`, `Delta_E_I`, `Delta_E_IC`, `Delta_E_VC`, `int_DOS_below_Fermi`, `int_DOS_above_Fermi`, `q_plus`, `q_minus`, `t_plus`, `t_minus`, `e_plus`, `e_minus`, `p_plus`, `p_minus`
      - `properties`:
        - `Delta_E_VI`:
          - `type`: number
          - `description`: VB-IB gap for majority spin (eV)
        - `Delta_E_I`:
          - `type`: number
          - `description`: IB bandwidth (eV)
        - `Delta_E_IC`:
          - `type`: number
          - `description`: IB-CB gap for majority spin (eV)
        - `Delta_E_VC`:
          - `type`: number
          - `description`: VB-CB gap for minority spin (eV)
        - `int_DOS_below_Fermi`:
          - `type`: number
          - `description`: Integrated DOS from IB bottom to Fermi energy (electrons per cell)
        - `int_DOS_above_Fermi`:
          - `type`: number
          - `description`: Integrated DOS from Fermi energy to IB top (electrons per cell)
        - `q_plus`:
          - `type`: number
          - `description`: Total Mulliken charge majority spin (electrons)
        - `q_minus`:
          - `type`: number
          - `description`: Total Mulliken charge minority spin (electrons)
        - `t_plus`:
          - `type`: number
          - `description`: t-orbital population majority spin (electrons)
        - `t_minus`:
          - `type`: number
          - `description`: t-orbital population minority spin (electrons)
        - `e_plus`:
          - `type`: number
          - `description`: e-orbital population majority spin (electrons)
        - `e_minus`:
          - `type`: number
          - `description`: e-orbital population minority spin (electrons)
        - `p_plus`:
          - `type`: number
          - `description`: p-orbital population majority spin (electrons)
        - `p_minus`:
          - `type`: number
          - `description`: p-orbital population minority spin (electrons)
    - `x1_32_U3`:
      - `$ref`: #/properties/x1_32_U0
    - `x1_32_U6`:
      - `$ref`: #/properties/x1_32_U0
    - `x2_32_U0`:
      - `$ref`: #/properties/x1_32_U0
    - `x2_32_U3`:
      - `$ref`: #/properties/x1_32_U0
    - `x2_32_U6`:
      - `$ref`: #/properties/x1_32_U0

Notes: All energies are in eV, integrated DOS are in electrons per cell, Mulliken charges are in electrons. The checker will compare each numeric field against hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "x1_32_U0",
          "x1_32_U3",
          "x1_32_U6",
          "x2_32_U0",
          "x2_32_U3",
          "x2_32_U6"
        ],
        "additionalProperties": false,
        "properties": {
          "x1_32_U0": {
            "type": "object",
            "required": [
              "Delta_E_VI",
              "Delta_E_I",
              "Delta_E_IC",
              "Delta_E_VC",
              "int_DOS_below_Fermi",
              "int_DOS_above_Fermi",
              "q_plus",
              "q_minus",
              "t_plus",
              "t_minus",
              "e_plus",
              "e_minus",
              "p_plus",
              "p_minus"
            ],
            "properties": {
              "Delta_E_VI": {
                "type": "number",
                "description": "VB-IB gap for majority spin (eV)"
              },
              "Delta_E_I": {
                "type": "number",
                "description": "IB bandwidth (eV)"
              },
              "Delta_E_IC": {
                "type": "number",
                "description": "IB-CB gap for majority spin (eV)"
              },
              "Delta_E_VC": {
                "type": "number",
                "description": "VB-CB gap for minority spin (eV)"
              },
              "int_DOS_below_Fermi": {
                "type": "number",
                "description": "Integrated DOS from IB bottom to Fermi energy (electrons per cell)"
              },
              "int_DOS_above_Fermi": {
                "type": "number",
                "description": "Integrated DOS from Fermi energy to IB top (electrons per cell)"
              },
              "q_plus": {
                "type": "number",
                "description": "Total Mulliken charge majority spin (electrons)"
              },
              "q_minus": {
                "type": "number",
                "description": "Total Mulliken charge minority spin (electrons)"
              },
              "t_plus": {
                "type": "number",
                "description": "t-orbital population majority spin (electrons)"
              },
              "t_minus": {
                "type": "number",
                "description": "t-orbital population minority spin (electrons)"
              },
              "e_plus": {
                "type": "number",
                "description": "e-orbital population majority spin (electrons)"
              },
              "e_minus": {
                "type": "number",
                "description": "e-orbital population minority spin (electrons)"
              },
              "p_plus": {
                "type": "number",
                "description": "p-orbital population majority spin (electrons)"
              },
              "p_minus": {
                "type": "number",
                "description": "p-orbital population minority spin (electrons)"
              }
            }
          },
          "x1_32_U3": {
            "$ref": "#/properties/x1_32_U0"
          },
          "x1_32_U6": {
            "$ref": "#/properties/x1_32_U0"
          },
          "x2_32_U0": {
            "$ref": "#/properties/x1_32_U0"
          },
          "x2_32_U3": {
            "$ref": "#/properties/x1_32_U0"
          },
          "x2_32_U6": {
            "$ref": "#/properties/x1_32_U0"
          }
        }
      },
      "description": "Compiled electronic structure results for all Cr concentrations and U values, including band gaps, IB bandwidths, integrated DOS occupancies, and Mulliken orbital populations."
    }
  ],
  "notes": "All energies are in eV, integrated DOS are in electrons per cell, Mulliken charges are in electrons. The checker will compare each numeric field against hidden reference values with appropriate tolerances."
}
```

## How you are scored
After you submit, a hidden verifier will read your results.json and compare each required numeric field against a set of reference values that correspond to the correct electronic structure for the given conditions. The comparison uses tolerances that account for reasonable numerical differences between DFT implementations. The verifier computes a reward between 0 and 1, giving full credit for fields within tolerance and partial credit for others. Only the extracted numerical values matter; the verifier does not examine the intermediate DFT logs or plots. Therefore, the accuracy of your DFT simulation and the correctness of your extraction code determine your score.
