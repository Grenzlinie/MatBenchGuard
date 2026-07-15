# Thermodynamic prediction of stacking fault energy in Fe-Cr-Ni-Mo alloys

## Problem background
Stacking fault energy (SFE) in austenitic steels governs dislocation motion, work hardening, and dynamic recrystallization (DRX). The addition of interstitial elements like nitrogen and carbon can significantly alter SFE, yet the explicit relationship between interstitial content, SFE, and hot‑working behaviour is not always straightforward. This task focuses on predicting SFE for Fe‑Cr‑Ni‑Mo austenitic alloys with varying total interstitial (N + C) content. An upgraded thermodynamic model was developed to compute SFE from chemical composition and temperature, incorporating Mo as a substitutional element, treating C and N as independent interstitial species, and extending to high working temperatures. The predicted SFE values help explain rate‑dependent DRX characteristics.

## Approach
Implement a thermodynamic model for SFE based on the free energy change associated with the formation of a stacking fault, i.e., the transition from the FCC (γ) to the HCP (ζ) phase within the faulted layer. The SFE is expressed as the sum of the interfacial energy and the bulk, magnetic, and segregation free‑energy contributions, each scaled by the molar surface density. The bulk free energy comprises: (i) a sum over substitutional elements (Fe, Cr, Ni, Mo) of their individual free‑energy differences and excess interaction terms, and (ii) independent contributions from the interstitial solutes C and N. All free‑energy parameters are obtained from the SGTE CALPHAD pure‑elements database. The molar surface density is computed from a literature lattice parameter for austenitic stainless steel (e.g., ~3.60 Å). The compositions of the three alloy variants (7N, 11N, 22N) are taken from the original study and will be provided directly in this instruction; they must be converted from weight percent to mole fractions before use. The model is implemented to compute SFE at room temperature (298 K) and at the hot‑working temperature of 1323 K.

## Reproduction target
Calculate the stacking fault energy (in mJ/m²) for the three Fe‑Cr‑Ni‑Mo alloy variants 7N, 11N, and 22N at two temperatures: 298 K (room temperature) and 1323 K. Write the results to the file sfe_results.csv with exactly three rows and three columns: variant, SFE_RT, SFE_1323K. The computed SFE values should exhibit a consistent monotonic relationship with respect to the total interstitial (N + C) content: as the interstitial content increases from 7N to 22N, the SFE at each temperature must change monotonically (either always increasing or always decreasing). The hidden verifier will test this trend together with the absolute SFE values.

## Assets

- SGTE Pure Elements Thermodynamic Database (Dinsdale 1991): pycalphad
- pycalphad (Python CALPHAD library): https://pycalphad.org/
- Lattice parameter for austenitic stainless steel
- Chemical compositions of 7N, 11N, 22N variants

## Workflow steps

### Step 1: Prepare thermodynamic input data
- Role: process
- Action: Obtain the thermodynamic parameters (free energy changes ΔG, excess free energies Ω, interfacial energy σ_I, molar surface density ψ) for the Fe-Cr-Ni-Mo-C-N system from the SGTE CALPHAD database (via pycalphad or similar) and a lattice parameter (e.g., 3.60 Å). Convert the supplied variant compositions (weight percent) to mole fractions for each element.
- Evidence: `/app/outputs/thermo_log.txt`

### Step 2: Compute SFE for all variants at room temperature and 1323 K
- Role: scored (load-bearing)
- Action: Implement the modified thermodynamic model (based on the upgrade to the Curtze et al. formalism, incorporating Mo as a BCC-stabilizing substitutional element, treating C and N as independent interstitial species, and extending to high temperatures) using the parameters from Step 1. For each variant (7N, 11N, 22N), compute the stacking fault energy (γ_SFE) at 298 K and 1323 K. Write the results to sfe_results.csv, one row per variant.
- Output file: `/app/outputs/sfe_results.csv`
- Format: csv
- Contract: Columns: variant (string), SFE_RT (float, mJ/m²), SFE_1323K (float, mJ/m²). One row per variant.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sfe_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sfe_results.csv
- path: `/app/outputs/sfe_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted stacking fault energy for the three alloy variants at room temperature (298 K) and at 1323 K.
- schema:
  - `type`: table
  - `required_columns`: `variant`, `SFE_RT`, `SFE_1323K`
  - `units`:
    - `SFE_RT`: mJ/m^2
    - `SFE_1323K`: mJ/m^2

Notes: The hidden checker compares the reported SFE_RT values to a reference set (paper's predicted values) with a predetermined tolerance. Additionally, it verifies that both SFE_RT and SFE_1323K values strictly decrease (or are non-increasing) as the total interstitial content increases, i.e., 7N > 11N > 22N. Both absolute value checks and trend enforcement contribute to the overall reward.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sfe_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "variant",
          "SFE_RT",
          "SFE_1323K"
        ],
        "units": {
          "SFE_RT": "mJ/m^2",
          "SFE_1323K": "mJ/m^2"
        }
      },
      "description": "Predicted stacking fault energy for the three alloy variants at room temperature (298 K) and at 1323 K."
    }
  ],
  "notes": "The hidden checker compares the reported SFE_RT values to a reference set (paper's predicted values) with a predetermined tolerance. Additionally, it verifies that both SFE_RT and SFE_1323K values strictly decrease (or are non-increasing) as the total interstitial content increases, i.e., 7N > 11N > 22N. Both absolute value checks and trend enforcement contribute to the overall reward."
}
```

## How you are scored
A hidden verifier reads your submitted sfe_results.csv and independently evaluates both the absolute SFE values and the monotonic trend. The verifier compares your reported SFE_RT and SFE_1323K values to reference values derived from the original study, using a predefined tolerance for each temperature. It also checks that the SFE values across the three variants (7N, 11N, 22N) follow a monotonic trend with increasing interstitial content, i.e., the sequence is either strictly non‑increasing or non‑decreasing. The total reward is a weighted combination of these two checks, with greater weight placed on the accuracy of the absolute values. Full credit is awarded when the reported values fall within the tolerance and the monotonicity condition is satisfied; otherwise, partial credit is given based on the degree of deviation.
