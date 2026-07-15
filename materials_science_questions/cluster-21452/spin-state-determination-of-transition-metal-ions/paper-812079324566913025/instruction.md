# DFT and ab initio calculation of magnetic exchange and anisotropy in [(VIVO)2M5II] Anderson wheels

## Problem background
Heterometallic Anderson wheels of the type [(VIVO)2M5II] (M = Ni, Co) contain seven paramagnetic metal ions arranged as a centred hexagon. The presence of multiple VIV (S=1/2) and MII centres (NiII S=1 or CoII S=3/2) gives rise to a complex network of pairwise magnetic exchange interactions, some ferromagnetic and some antiferromagnetic. Understanding the sign, strength, and origin of these interactions, as well as the single-ion magnetic anisotropy of the CoII ions, is essential for interpreting the observed magnetic behaviour and for designing related molecule-based magnets. Theoretical calculations based on density functional theory (DFT) and ab initio quantum chemistry can provide quantitative values for the exchange coupling constants J and zero-field splitting parameter D directly from the crystal structure, without relying on experimental magnetic data.

## Approach
The strategy uses broken-symmetry density functional theory (BS-DFT) to compute the energies of different spin configurations on the full heptanuclear cluster of the Ni analogue. From the energies of the high-spin state and several broken-symmetry determinants, the four distinct pairwise exchange coupling constants (J1–J4) are extracted using a suitable spin-projection method (e.g., the Yamaguchi formula). For the Co analogue, the large single-ion anisotropy precludes reliable DFT exchange values; instead, the task focuses on computing the local zero-field splitting parameters |D| for the chemically distinct Co sites (one ring Co and the central Co). This is done by constructing diamagnetic-substituted models (replacing other paramagnetic Co and V ions with ZnII) and performing multireference CASSCF/NEVPT2 calculations including spin-orbit coupling via quasi-degenerate perturbation theory. The calculated |D| values reflect the magnetic anisotropy that dominates the low-temperature properties. All calculations are based solely on the atomic coordinates from the published crystal structures.

## Reproduction target
Using the deposited crystal structures (CCDC 1847956 for the Ni wheel, 1847957 for the Co wheel), perform the theoretical calculations described above and report the computed magnetic parameters. For the Ni complex, produce the four isotropic exchange constants J1, J2, J3, J4 (in cm⁻¹). For the Co complex, produce the absolute axial zero-field splitting parameters |D_Co_ring| and |D_Co_central| (in cm⁻¹). Save the results in ni_j_values.json and co_d_values.json with the exact JSON schemas specified in the workflow steps. The computation must be based exclusively on the provided crystal structures; experimental magnetic susceptibility data are not needed.

## Assets

- Crystal structure of complex 1 (CCDC 1847956): https://www.ccdc.cam.ac.uk/structures/search?Ccdc=1847956
- Crystal structure of complex 2 (CCDC 1847957): https://www.ccdc.cam.ac.uk/structures/search?Ccdc=1847957
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Prepare input models
- Role: process
- Action: From the downloaded CIF files (CCDC 1847956, 1847957), extract atomic coordinates. For Ni complex 1, keep all metal and ligand atoms; set appropriate charge and spin for the high-spin state. For Co complex 2, generate Zn-substituted models for each unique Co site (ring and central) by replacing other paramagnetic Co and V with Zn(II) while preserving geometry, for local D calculations.
- Evidence: `/app/outputs/model_preparation.log`

### Step 2: Compute exchange couplings for Ni wheel
- Role: scored
- Action: Perform broken-symmetry DFT calculations (using an appropriate functional and basis set) on the Ni7 cluster to obtain energies of the high-spin state and several broken-symmetry states covering the four exchange pathways (J1-J4). Compute J values using a suitable projection method and write results to ni_j_values.json.
- Output file: `/app/outputs/ni_j_values.json`
- Format: json
- Contract: {"J1": float, "J2": float, "J3": float, "J4": float}
- Scoring: scored by hidden verifier

### Step 3: Compute Co single-ion anisotropy
- Role: scored
- Action: Perform ab initio CASSCF/NEVPT2 calculations including spin-orbit coupling (e.g., QDPT) on the Zn-substituted models for the unique Co sites in complex 2. For each distinct Co (ring and central), compute the axial zero-field splitting parameter D and extract its magnitude. Report the absolute values in co_d_values.json.
- Output file: `/app/outputs/co_d_values.json`
- Format: json
- Contract: {"|D_Co_ring|": float, "|D_Co_central|": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ni_j_values.json`
- `/app/outputs/co_d_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ni_j_values.json
- path: `/app/outputs/ni_j_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Exchange coupling constants (cm⁻¹). Must have correct signs (J2 negative) and order-of-magnitude agreement with the paper's DFT values.
- schema:
  - `type`: object
  - `required`:
    - `J1`: number
    - `J2`: number
    - `J3`: number
    - `J4`: number
  - `units`:
    - `J1`: cm-1
    - `J2`: cm-1
    - `J3`: cm-1
    - `J4`: cm-1

### co_d_values.json
- path: `/app/outputs/co_d_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnitudes of single-ion axial anisotropy (cm⁻¹). Order of magnitude should match the paper's ab initio results.
- schema:
  - `type`: object
  - `required`:
    - `|D_Co_ring|`: number
    - `|D_Co_central|`: number
  - `units`:
    - `|D_Co_ring|`: cm-1
    - `|D_Co_central|`: cm-1

Notes: This task reproduces the theoretical calculations only (DFT exchange couplings and ab initio anisotropy) as reported in the paper. Experimental magnetic data fitting is not required. The agent must install a suitable quantum chemistry package (e.g., ORCA) and may require substantial computational resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ni_j_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "J1": "number",
          "J2": "number",
          "J3": "number",
          "J4": "number"
        },
        "units": {
          "J1": "cm-1",
          "J2": "cm-1",
          "J3": "cm-1",
          "J4": "cm-1"
        }
      },
      "description": "Exchange coupling constants (cm⁻¹). Must have correct signs (J2 negative) and order-of-magnitude agreement with the paper's DFT values."
    },
    {
      "file": "co_d_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "|D_Co_ring|": "number",
          "|D_Co_central|": "number"
        },
        "units": {
          "|D_Co_ring|": "cm-1",
          "|D_Co_central|": "cm-1"
        }
      },
      "description": "Magnitudes of single-ion axial anisotropy (cm⁻¹). Order of magnitude should match the paper's ab initio results."
    }
  ],
  "notes": "This task reproduces the theoretical calculations only (DFT exchange couplings and ab initio anisotropy) as reported in the paper. Experimental magnetic data fitting is not required. The agent must install a suitable quantum chemistry package (e.g., ORCA) and may require substantial computational resources."
}
```

## How you are scored
Each scored output file (ni_j_values.json and co_d_values.json) is independently evaluated by a hidden verifier. The verifier compares your submitted J and |D| values against reference values using generous relative tolerances that account for differences in software, functional, basis set, or active space choices. Credit is awarded based on correctness of sign, relative ordering of exchange pathways, and order-of-magnitude agreement. No single exact number needs to be matched. The two artifacts carry roughly equal weight, and the final reward is the weighted sum, normalised to the range [0,1]. Your code must genuinely compute these quantities; simply reporting numbers without running the calculations will not pass the verifier's checks.
