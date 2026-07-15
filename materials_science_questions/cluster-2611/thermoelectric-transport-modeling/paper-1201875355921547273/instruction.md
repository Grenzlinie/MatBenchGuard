# Thermoelectric Transport Modeling of SnSe‑based Hybrids and Layered CsPbI3

## Problem background
Thermoelectric materials convert temperature differences directly to electricity, and their efficiency is measured by the dimensionless figure of merit ZT = S²σT/κ, where S is the Seebeck coefficient, σ is the electrical conductivity, T is the absolute temperature, and κ is the thermal conductivity. This task focuses on the electronic contribution to ZT, denoted ZT_elec = S²σ T / κ₀, where κ₀ is the electronic thermal conductivity (ignoring lattice contributions). The systems under study are two hybrid supercells, SnSe-hBN and SnSe-CsPbI₃, and layered CsPbI₃ with different numbers of layers. Your goal is to compute ZT_elec for these systems using first-principles electronic structure calculations and semi-classical Boltzmann transport theory in the constant relaxation time approximation.

## Approach
The computational approach follows three stages. First, density functional theory (DFT) geometry relaxation is performed with the PBE exchange‑correlation functional and a van der Waals correction (vdW‑DFT3). Second, self‑consistent and non‑self‑consistent band structure calculations are carried out on the relaxed structures to obtain the band energies on a dense k‑mesh suitable for transport. Third, the Boltzmann transport code (BoltzTraP) is used in the constant relaxation time approximation to compute the transport distribution and the resulting transport coefficients (σ/τ, S, κ₀/τ) as functions of chemical potential. Finally, ZT_elec = S²σ T / κ₀ is evaluated at each temperature, and its maximum value over the scanned chemical potential range is recorded.

## Reproduction target
Compute the maximum electronic figure of merit ZT_elec for the SnSe‑hBN and SnSe‑CsPbI₃ hybrid supercells at temperatures 100 K, 200 K, …, 1000 K (step 100 K). Additionally, compute ZT_elec for three‑layer and four‑layer CsPbI₃ at 150 K. Record these values in the output JSON file (`zt_elec_results.json`) following the specified schema.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP: http://www.boltzp.org/
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/
- Initial structures for SnSe‑hBN and SnSe‑CsPbI3 hybrid supercells: 10.17632/py638t2nmg.1

## Workflow steps

### Step 1: Geometry relaxation
- Role: process
- Action: Perform full DFT geometry relaxation using Quantum ESPRESSO with PBE+vdW‑DFT3 for the SnSe‑hBN hybrid, SnSe‑CsPbI3 hybrid, and layered CsPbI3 (monolayer, bilayer, trilayer, tetralayer). Use initial atomic coordinates from the Mendeley repository (doi:10.17632/py638t2nmg.1) and SSSP pseudopotentials. The solver chooses all numerical convergence parameters (k‑mesh, cutoffs, force thresholds).
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Electronic structure calculation
- Role: process
- Action: Run self‑consistent and non‑self‑consistent band structure calculations on the relaxed structures from the previous step. Use a dense k‑mesh suitable for transport and write the band energies in a format readable by BoltzTraP.
- Evidence: `/app/outputs/bands_energy.dat`

### Step 3: Boltzmann transport calculation
- Role: process
- Action: Run BoltzTraP on the band energies to obtain transport coefficients (electrical conductivity divided by relaxation time, Seebeck coefficient, electronic thermal conductivity divided by relaxation time) as functions of chemical potential. Compute these for the hybrid systems at temperatures 100,200,…,1000 K, and for the layered CsPbI3 structures (all layers) at 150 K.
- Evidence: `/app/outputs/boltzp_output.tar.gz`

### Step 4: Extract maximum ZT_elec
- Role: scored (load-bearing)
- Action: From the BoltzTraP output, compute ZT_elec = S² σ T / κ₀ at each temperature. For each system and temperature, find the maximum value over the scanned chemical potential range and record it in the output JSON file.
- Output file: `/app/outputs/zt_elec_results.json`
- Format: json
- Contract: { "SnSe_hBN": { "100": number, "200": number, "...", "1000": number }, "SnSe_CsPbI3": { "100": number, ..., "1000": number }, "layered_CsPbI3": { "3-layer": { "150": number }, "4-layer": { "150": number } } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zt_elec_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zt_elec_results.json
- path: `/app/outputs/zt_elec_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored artifact: maximum ZT_elec values for the two hybrid systems from 100 K to 1000 K, and for 3‑layer and 4‑layer CsPbI3 at 150 K. Checked against hidden paper‑reported thresholds and monotonic temperature trend.
- schema:
  - `type`: object
  - `required`: `SnSe_hBN`, `SnSe_CsPbI3`, `layered_CsPbI3`
  - `properties`:
    - `SnSe_hBN`:
      - `type`: object
      - `additionalProperties`:
        - `type`: number
      - `description`: Maximum ZT_elec for SnSe‑hBN at temperatures 100 K to 1000 K (step 100 K). Keys are the temperature in Kelvin as strings.
    - `SnSe_CsPbI3`:
      - `type`: object
      - `additionalProperties`:
        - `type`: number
      - `description`: Maximum ZT_elec for SnSe‑CsPbI3 at temperatures 100 K to 1000 K (step 100 K).
    - `layered_CsPbI3`:
      - `type`: object
      - `required`: `3-layer`, `4-layer`
      - `properties`:
        - `3-layer`:
          - `type`: object
          - `additionalProperties`: False
          - `properties`:
            - `150`:
              - `type`: number
          - `required`: `150`
        - `4-layer`:
          - `type`: object
          - `additionalProperties`: False
          - `properties`:
            - `150`:
              - `type`: number
          - `required`: `150`

Notes: The checker verifies (1) the ZT_elec at 100 K for SnSe‑hBN and SnSe‑CsPbI3 meets or exceeds the paper’s hidden threshold, (2) the ZT_elec for 3‑layer and 4‑layer CsPbI3 at 150 K is ≥ 2.0, and (3) the ZT_elec values for each hybrid decrease monotonically with increasing temperature (structural audit).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zt_elec_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "SnSe_hBN",
          "SnSe_CsPbI3",
          "layered_CsPbI3"
        ],
        "properties": {
          "SnSe_hBN": {
            "type": "object",
            "additionalProperties": {
              "type": "number"
            },
            "description": "Maximum ZT_elec for SnSe‑hBN at temperatures 100 K to 1000 K (step 100 K). Keys are the temperature in Kelvin as strings."
          },
          "SnSe_CsPbI3": {
            "type": "object",
            "additionalProperties": {
              "type": "number"
            },
            "description": "Maximum ZT_elec for SnSe‑CsPbI3 at temperatures 100 K to 1000 K (step 100 K)."
          },
          "layered_CsPbI3": {
            "type": "object",
            "required": [
              "3-layer",
              "4-layer"
            ],
            "properties": {
              "3-layer": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "150": {
                    "type": "number"
                  }
                },
                "required": [
                  "150"
                ]
              },
              "4-layer": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "150": {
                    "type": "number"
                  }
                },
                "required": [
                  "150"
                ]
              }
            }
          }
        }
      },
      "description": "Scored artifact: maximum ZT_elec values for the two hybrid systems from 100 K to 1000 K, and for 3‑layer and 4‑layer CsPbI3 at 150 K. Checked against hidden paper‑reported thresholds and monotonic temperature trend."
    }
  ],
  "notes": "The checker verifies (1) the ZT_elec at 100 K for SnSe‑hBN and SnSe‑CsPbI3 meets or exceeds the paper’s hidden threshold, (2) the ZT_elec for 3‑layer and 4‑layer CsPbI3 at 150 K is ≥ 2.0, and (3) the ZT_elec values for each hybrid decrease monotonically with increasing temperature (structural audit)."
}
```

## How you are scored
A hidden verifier independently scores each stage's output artifact and combines them into a final reward (a float between 0 and 1). The process‑step evidence files (relaxation log, band energies, transport output) are checked for presence and basic integrity; the primary scoring weight rests on the final `zt_elec_results.json`. The verifier compares your reported ZT_elec values against hidden reference values, using tolerances appropriate for an independent re‑run of the same workflow. It also checks that the ZT_elec values for each hybrid system follow the expected monotonic behaviour with temperature. Reporting the paper's numbers without genuine computation is not sufficient to pass the checks. The overall reward is a weighted sum of these components, with the magnitude at key temperatures and the trend across the full temperature range each contributing a meaningful fraction.
