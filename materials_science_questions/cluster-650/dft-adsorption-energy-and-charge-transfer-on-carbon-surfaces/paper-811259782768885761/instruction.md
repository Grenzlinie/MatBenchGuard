# DFT Computation of N2 Electro-Reduction Overpotentials and Activation Barriers on MXene Catalysts

## Problem background
Electrochemical conversion of dinitrogen (N2) to ammonia (NH3) is a promising route for sustainable ammonia production. Two-dimensional transition metal carbides (MXenes) have been proposed as potential catalysts for this reaction. This task aims to compute the limiting overpotential and activation barriers for the N2 reduction reaction on two specific MXenes, V3C2 and Nb3C2, using density functional theory (DFT) simulations. The result will help identify the catalyst with the lower overpotential and shed light on the reaction mechanism.

## Approach
We employ density functional theory (DFT) within the generalized gradient approximation (GGA) using the Perdew-Burke-Ernzerhof (PBE) functional and D3 dispersion corrections. Periodic slab models of V3C2 and Nb3C2 MXenes are constructed and relaxed. The electrochemical reduction pathway is modeled by stepwise addition of proton-electron pairs; the computational hydrogen electrode (CHE) model is used to obtain Gibbs free energy profiles at zero applied potential (U = 0 V) relative to the standard hydrogen electrode (SHE). The nudged elastic band (NEB) method is used to locate transition states and compute activation barriers. The analysis compares the two catalysts by evaluating the rate‑determining step and the limiting overpotential.

## Reproduction target
Compute the Gibbs free energy profiles for the N2 electro‑reduction pathway (minimum energy path 2) on V3C2 and Nb3C2 MXene surfaces using DFT (PBE+D3). Determine the rate‑determining step, compute the limiting overpotential (V vs. SHE), and locate the transition states TS1–TS4 for both catalysts. Output the overpotential, the rate‑determining step, and all activation barriers in the two CSV files specified below.

## Assets

- Open-source DFT package (Quantum ESPRESSO, CP2K, or equivalent): https://www.quantum-espresso.org/
- Crystal structures of M3C2 MXenes (V3C2, Nb3C2)
- Gas-phase reference molecules (N2, H2, NH3)

## Workflow steps

### Step 1: MXene slab construction and relaxation
- Role: process
- Action: Construct V3C2 and Nb3C2 slab models from bulk crystal structures. Perform geometry optimization with DFT (PBE+D3) to obtain relaxed clean surfaces.
- Evidence: none

### Step 2: N2 chemisorption calculation
- Role: process
- Action: Compute the adsorption energy of N2 on the relaxed surfaces of both MXenes. Optimize the N2-adsorbed geometry and confirm N≡N bond elongation (activation).
- Evidence: none

### Step 3: Intermediate optimization for N2 reduction pathway
- Role: process
- Action: Optimize the geometries of all intermediate species along the minimum energy path (path 2): N–NH•, N–NH2, N•, NH, NH2•, and NH3 on both V3C2 and Nb3C2. Compute their DFT total energies.
- Evidence: none

### Step 4: NEB transition state search
- Role: process
- Action: Using the nudged elastic band (NEB) method, locate transition states TS1, TS2, TS3, TS4 for both catalysts and compute their energies. Confirm that TS3 is barrier‑less.
- Evidence: none

### Step 5: Free-energy profile and overpotential calculation
- Role: scored (load-bearing)
- Action: Apply the computational hydrogen electrode (CHE) model to convert DFT energies to Gibbs free energy profiles at U=0 V vs. SHE. Determine the limiting thermodynamic step and the overall overpotential for each catalyst. Write results to overpotentials.csv.
- Output file: `/app/outputs/overpotentials.csv`
- Format: csv
- Contract: catalyst (string), overpotential_V (float), rds (string)
- Scoring: scored by hidden verifier

### Step 6: Activation barriers reporting
- Role: scored
- Action: Compile the computed activation barriers (eV) for all key transition states (TS1, TS2, TS3, TS4) on V3C2 and Nb3C2. Write to activation_barriers.csv.
- Output file: `/app/outputs/activation_barriers.csv`
- Format: csv
- Contract: catalyst (string), ts_id (string), barrier_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/overpotentials.csv`
- `/app/outputs/activation_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### overpotentials.csv
- path: `/app/outputs/overpotentials.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed limiting overpotential (V vs. SHE) and rate-determining step for V3C2 and Nb3C2.
- schema:
  - `type`: table
  - `required_columns`: `catalyst`, `overpotential_V`, `rds`
  - `units`:
    - `overpotential_V`: V vs. SHE

### activation_barriers.csv
- path: `/app/outputs/activation_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Gibbs free activation barriers (eV) for transition states TS1, TS2, TS3, TS4 on V3C2 and Nb3C2.
- schema:
  - `type`: table
  - `required_columns`: `catalyst`, `ts_id`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

Notes: The activation_barriers.csv must include a row for TS3 with barrier_eV ≤ 0.01 eV to indicate a barrier‑less process. The expected trend is that overpotential_V for V3C2 is lower than that for Nb3C2, and the highest barrier for V3C2 corresponds to TS1, while for Nb3C2 it corresponds to TS2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "overpotentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "catalyst",
          "overpotential_V",
          "rds"
        ],
        "units": {
          "overpotential_V": "V vs. SHE"
        }
      },
      "description": "Computed limiting overpotential (V vs. SHE) and rate-determining step for V3C2 and Nb3C2."
    },
    {
      "file": "activation_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "catalyst",
          "ts_id",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Gibbs free activation barriers (eV) for transition states TS1, TS2, TS3, TS4 on V3C2 and Nb3C2."
    }
  ],
  "notes": "The activation_barriers.csv must include a row for TS3 with barrier_eV ≤ 0.01 eV to indicate a barrier‑less process. The expected trend is that overpotential_V for V3C2 is lower than that for Nb3C2, and the highest barrier for V3C2 corresponds to TS1, while for Nb3C2 it corresponds to TS2."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your overpotentials.csv and activation_barriers.csv from /app/outputs. The verifier compares your reported overpotential, rate‑determining step, and activation barrier values against hidden reference data derived from the original study, using tolerance margins that account for differences in DFT implementation and numerical settings. It also validates expected trends (the catalyst with the lower overpotential and the identity of the highest barrier for each catalyst). Both output stages are scored, and the verifier combines their individual scores into a single final reward in the range [0,1]. The exact scoring thresholds and weights are not disclosed.
