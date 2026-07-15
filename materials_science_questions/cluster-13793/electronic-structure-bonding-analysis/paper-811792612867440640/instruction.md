# DFT bonding analysis of ZrCuSiAs and ZrCuSiP

## Problem background
Quaternary pnictides with the ZrCuSiAs structure type crystallise in a tetragonal layer-like arrangement (space group P4/nmm) composed of [ZrSi] and [CuPn] slabs (Pn = P, As). Within this framework, the silicon atoms form square nets that are substantially contracted relative to the interlayer spacing, raising the question of whether strong Si–Si homoatomic bonding builds a polyanionic network. At the same time, the close approach of Zr atoms in one slab to pnicogen atoms in the adjacent slab suggests that covalent interactions may bridge the layers, potentially transforming the electronic structure from two‑dimensional to three‑dimensional character. Resolving the relative strength of these competing intra- and interlayer bonds is central to understanding the electronic behaviour of these compounds, and a first‑principles bonding analysis provides a quantitative route to test these structural hypotheses.

## Approach
First‑principles density functional theory (DFT) calculations are performed for the two title compounds using their experimentally determined crystal structures. After obtaining a converged electronic ground state, the resulting wave‑functions are post‑processed with the crystal orbital Hamilton population (COHP) technique, which decomposes the band‑structure energy into pairwise orbital‑interaction contributions. By integrating the COHP curves up to the Fermi level, integrated –ICOHP values are extracted for the major nearest‑neighbour bonds: Zr–Si, Si–Si, Cu–Pn, Zr–Pn, and Cu–Cu. These bond‑energy descriptors quantify the covalent bond strength for each contact in eV per bond, allowing an ordering of bond strengths within and between the [ZrSi] and [CuPn] slabs. In parallel, the total electronic density of states is computed and the value at the Fermi level is examined to determine whether a pseudogap—a deep minimum in the DOS near the Fermi energy—is present, which would indicate semimetallic behaviour.

## Reproduction target
Compute integrated –ICOHP values (eV/bond) for the bonds Zr–Si, Si–Si, Cu–As (in ZrCuSiAs) or Cu–P (in ZrCuSiP), Zr–As (or Zr–P), and Cu–Cu in both compounds. Determine the relative ordering of bond strengths. Additionally, compute the total electronic density of states at the Fermi level and report whether a pseudogap (DOS at Ef below 0.5 states/eV per formula unit) is observed in each compound. The results must be written to two JSON files: `icohp_values.json` and `pseudogap_report.json`, following the exact schemas defined in the workflow steps below.

## Assets

- Crystal structures of ZrCuSiAs and ZrCuSiP: https://icsd.products.fiz-karlsruhe.de
- Quantum ESPRESSO: https://www.quantum-espresso.org
- LOBSTER: http://www.cohp.de
- Pseudopotential library: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT calculations
- Role: process
- Action: For ZrCuSiAs and ZrCuSiP, set up input files with the experimental crystal structures, run Quantum ESPRESSO self-consistent field (SCF) and non-self-consistent (NSCF) calculations to obtain a converged charge density and wavefunctions needed for COHP analysis.
- Evidence: `/app/outputs/scf_summary.txt`

### Step 2: COHP analysis and Integrated -ICOHP extraction
- Role: scored (load-bearing)
- Action: Run LOBSTER using the DFT wavefunctions to compute crystal orbital Hamilton populations. For each compound, identify the nearest-neighbor bonds within a cutoff of approximately 3.5 Å and extract the integrated -ICOHP values (eV/bond) for the bonds Zr-Si, Si-Si, Cu-Pn (As or P), Zr-Pn, and Cu-Cu. Write the results to icohp_values.json.
- Output file: `/app/outputs/icohp_values.json`
- Format: json
- Contract: Top-level keys 'ZrCuSiAs' and 'ZrCuSiP'. Each value is an object with keys: 'Zr-Si', 'Si-Si', 'Cu-As' (for ZrCuSiAs), 'Cu-P' (for ZrCuSiP), 'Zr-As', 'Zr-P', 'Cu-Cu'. Values are floats in eV/bond.
- Scoring: scored by hidden verifier

### Step 3: DOS and pseudogap check
- Role: scored
- Action: From the DFT calculations, compute the total electronic density of states (DOS). Extract the DOS value at the Fermi level (E_f) in states/eV per formula unit. Determine whether a pseudogap is present by checking if DOS(E_f) is below 0.5 states/eV/f.u. Write the boolean flag and the DOS(E_f) value to pseudogap_report.json.
- Output file: `/app/outputs/pseudogap_report.json`
- Format: json
- Contract: Top-level keys 'ZrCuSiAs' and 'ZrCuSiP'. Each value is an object with keys: 'pseudogap' (boolean) and 'dos_ef' (float in states/eV/f.u.).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/icohp_values.json`
- `/app/outputs/pseudogap_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### icohp_values.json
- path: `/app/outputs/icohp_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Integrated -ICOHP values for the major bonds in ZrCuSiAs and ZrCuSiP.
- schema:
  - `type`: object
  - `required`: `ZrCuSiAs`, `ZrCuSiP`
  - `properties`:
    - `ZrCuSiAs`:
      - `type`: object
      - `properties`:
        - `Zr-Si`:
          - `type`: number
          - `units`: eV/bond
        - `Si-Si`:
          - `type`: number
          - `units`: eV/bond
        - `Cu-As`:
          - `type`: number
          - `units`: eV/bond
        - `Zr-As`:
          - `type`: number
          - `units`: eV/bond
        - `Cu-Cu`:
          - `type`: number
          - `units`: eV/bond
    - `ZrCuSiP`:
      - `type`: object
      - `properties`:
        - `Zr-Si`:
          - `type`: number
          - `units`: eV/bond
        - `Si-Si`:
          - `type`: number
          - `units`: eV/bond
        - `Cu-P`:
          - `type`: number
          - `units`: eV/bond
        - `Zr-P`:
          - `type`: number
          - `units`: eV/bond
        - `Cu-Cu`:
          - `type`: number
          - `units`: eV/bond

### pseudogap_report.json
- path: `/app/outputs/pseudogap_report.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Pseudogap flag and DOS at the Fermi level for both compounds.
- schema:
  - `type`: object
  - `required`: `ZrCuSiAs`, `ZrCuSiP`
  - `properties`:
    - `ZrCuSiAs`:
      - `type`: object
      - `properties`:
        - `pseudogap`:
          - `type`: boolean
        - `dos_ef`:
          - `type`: number
          - `units`: states/eV/f.u.
    - `ZrCuSiP`:
      - `type`: object
      - `properties`:
        - `pseudogap`:
          - `type`: boolean
        - `dos_ef`:
          - `type`: number
          - `units`: states/eV/f.u.

Notes: The hidden checker compares the submitted -ICOHP values and pseudogap results against the paper's reported values with appropriate tolerances. The icohp_values are checked for correct bond ordering and magnitude consistency; the pseudogap is validated by threshold. All gold values are derived from the paper's computational results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "icohp_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "ZrCuSiAs",
          "ZrCuSiP"
        ],
        "properties": {
          "ZrCuSiAs": {
            "type": "object",
            "properties": {
              "Zr-Si": {
                "type": "number",
                "units": "eV/bond"
              },
              "Si-Si": {
                "type": "number",
                "units": "eV/bond"
              },
              "Cu-As": {
                "type": "number",
                "units": "eV/bond"
              },
              "Zr-As": {
                "type": "number",
                "units": "eV/bond"
              },
              "Cu-Cu": {
                "type": "number",
                "units": "eV/bond"
              }
            }
          },
          "ZrCuSiP": {
            "type": "object",
            "properties": {
              "Zr-Si": {
                "type": "number",
                "units": "eV/bond"
              },
              "Si-Si": {
                "type": "number",
                "units": "eV/bond"
              },
              "Cu-P": {
                "type": "number",
                "units": "eV/bond"
              },
              "Zr-P": {
                "type": "number",
                "units": "eV/bond"
              },
              "Cu-Cu": {
                "type": "number",
                "units": "eV/bond"
              }
            }
          }
        }
      },
      "description": "Integrated -ICOHP values for the major bonds in ZrCuSiAs and ZrCuSiP."
    },
    {
      "file": "pseudogap_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "ZrCuSiAs",
          "ZrCuSiP"
        ],
        "properties": {
          "ZrCuSiAs": {
            "type": "object",
            "properties": {
              "pseudogap": {
                "type": "boolean"
              },
              "dos_ef": {
                "type": "number",
                "units": "states/eV/f.u."
              }
            }
          },
          "ZrCuSiP": {
            "type": "object",
            "properties": {
              "pseudogap": {
                "type": "boolean"
              },
              "dos_ef": {
                "type": "number",
                "units": "states/eV/f.u."
              }
            }
          }
        }
      },
      "description": "Pseudogap flag and DOS at the Fermi level for both compounds."
    }
  ],
  "notes": "The hidden checker compares the submitted -ICOHP values and pseudogap results against the paper's reported values with appropriate tolerances. The icohp_values are checked for correct bond ordering and magnitude consistency; the pseudogap is validated by threshold. All gold values are derived from the paper's computational results."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact against a reference derived from the original study. For step 2 (COHP analysis), the verifier checks both the magnitude of the submitted –ICOHP values and the bond‑strength ordering; correctness of the ordering and agreement within an appropriate numerical tolerance are the primary scoring criteria. For step 3 (DOS and pseudogap), the verifier checks the reported pseudogap flag and the DOS‑at‑Ef value against the expected threshold‑based result. The two scored stages are combined by weight into the final reward (the –ICOHP analysis carries the larger share, the pseudogap check the smaller share). Reporting numbers without genuinely executing the DFT+COHP pipeline is not sufficient—the verifier expects results that are consistent with a correct computational workflow.
