# Thermoelectric Transport in Endohedral Fullerene Junctions

## Problem background
The thermoelectric properties of single-molecule junctions formed by endohedral fullerenes (M@C60, M=Co and Ni) between gold electrodes are studied using density functional theory (DFT) combined with the non-equilibrium Green's function (NEGF) formalism. The central question is how the incorporation of a transition metal atom inside the fullerene cage modifies the electronic transmission, the Seebeck coefficient, and the thermoelectric figure of merit ZT. In this task you will compute these quantities for three systems: bare C60, Ni@C60, and Co@C60, and report the energy-dependent curves that reveal the characteristic transport features.

## Approach
The approach is a two-stage DFT+NEGF workflow. First, perform geometry optimization for each molecular junction (bare C60, Ni@C60, Co@C60) between gold electrodes using the open-source DFT code SIESTA with a double-zeta polarized (DZP) basis set and the GGA-PBE exchange-correlation functional. This step produces the ground-state Kohn-Sham Hamiltonians. Second, feed these Hamiltonians into a quantum transport code implementing the NEGF formalism (the open-source code GOLLUM, or an equivalent) to compute the transmission coefficient T(E), the Seebeck coefficient S(E), and the figure of merit ZT(E) as functions of energy. The energy range should cover the HOMO-LUMO gap region. The comparison across the three systems—bare versus doped—reveals how transition metal doping influences the number and positions of transmission resonances and, consequently, the thermoelectric performance.

## Reproduction target
Produce the curves of T(E), S(E), and ZT(E) for all three systems (C60, Ni@C60, Co@C60) over an energy window that spans the HOMO-LUMO gap (e.g., -2 to 2 eV). Save each set of curves as a single CSV file as specified in the Workflow steps below. The hidden verifier will read your CSV files and check: (1) the number and approximate energy positions of transmission resonances in the HOMO-LUMO gap for each system; (2) the range of the Seebeck coefficient for Co@C60 at energies near the Fermi level; (3) the maximum ZT value for Co@C60. The target is to demonstrate that your simulation captures the transport features that distinguish the doped from the undoped junctions without needing to reproduce exact published numbers.

## Assets

- SIESTA: https://gitlab.com/siesta-project/siesta
- GOLLUM: https://gollum.quiet-flower.org/

## Workflow steps

### Step 1: DFT Geometry Optimization
- Role: process
- Action: Perform DFT geometry optimization for bare C60, Ni@C60, and Co@C60 molecular junctions between gold electrodes using SIESTA with DZP basis set and GGA-PBE exchange-correlation functional. Obtain ground-state Kohn-Sham Hamiltonians.
- Evidence: `/app/outputs/siesta.log`

### Step 2: NEGF Transport Calculation
- Role: process
- Action: Using the ground-state Hamiltonians from step_0, compute the transmission coefficient T(E), Seebeck coefficient S(E), and figure of merit ZT(E) for each system with the NEGF formalism as implemented in GOLLUM (or an equivalent open-source transport code).
- Evidence: `/app/outputs/transport_log.txt`

### Step 3: Output Transmission Coefficients
- Role: scored (load-bearing)
- Action: Write the computed transmission coefficient T(E) for all three systems (C60, Ni@C60, Co@C60) into a single CSV file over the energy range of interest (e.g., -2 to 2 eV).
- Output file: `/app/outputs/step_01_transmission.csv`
- Format: csv
- Contract: CSV with columns: energy(eV) (float), system (string: 'C60', 'Ni@C60', 'Co@C60'), transmission (float, dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Output Seebeck Coefficients
- Role: scored
- Action: Write the computed Seebeck coefficient S(E) for all three systems into a single CSV file over the same energy grid.
- Output file: `/app/outputs/step_02_seebeck.csv`
- Format: csv
- Contract: CSV with columns: energy(eV) (float), system (string: 'C60', 'Ni@C60', 'Co@C60'), seebeck_coefficient (float, μV/K)
- Scoring: scored by hidden verifier

### Step 5: Output Figure of Merit ZT
- Role: scored
- Action: Write the computed figure of merit ZT(E) for all three systems into a single CSV file over the same energy grid.
- Output file: `/app/outputs/step_03_zt.csv`
- Format: csv
- Contract: CSV with columns: energy(eV) (float), system (string: 'C60', 'Ni@C60', 'Co@C60'), zt (float, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_transmission.csv`
- `/app/outputs/step_02_seebeck.csv`
- `/app/outputs/step_03_zt.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_transmission.csv
- path: `/app/outputs/step_01_transmission.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transmission coefficient as a function of energy for bare C60, Ni@C60, and Co@C60. Checker compares resonance peak positions to a hidden reference.
- schema:
  - `required_columns`: `energy(eV)`, `system`, `transmission`
  - `units`:
    - `energy`: eV
    - `transmission`: dimensionless

### step_02_seebeck.csv
- path: `/app/outputs/step_02_seebeck.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Seebeck coefficient as a function of energy for all three systems. Checker compares range/values near the Fermi level to a hidden reference.
- schema:
  - `required_columns`: `energy(eV)`, `system`, `seebeck_coefficient`
  - `units`:
    - `energy`: eV
    - `seebeck_coefficient`: μV/K

### step_03_zt.csv
- path: `/app/outputs/step_03_zt.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Figure of merit ZT as a function of energy for all three systems. Checker compares maximum ZT value to a hidden reference.
- schema:
  - `required_columns`: `energy(eV)`, `system`, `zt`
  - `units`:
    - `energy`: eV
    - `zt`: dimensionless

Notes: Each CSV should contain enough energy points to resolve resonance features in the HOMO-LUMO gap. The energy grid should be fine enough to capture the reported resonance peaks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_transmission.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "energy(eV)",
          "system",
          "transmission"
        ],
        "units": {
          "energy": "eV",
          "transmission": "dimensionless"
        }
      },
      "description": "Transmission coefficient as a function of energy for bare C60, Ni@C60, and Co@C60. Checker compares resonance peak positions to a hidden reference."
    },
    {
      "file": "step_02_seebeck.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "energy(eV)",
          "system",
          "seebeck_coefficient"
        ],
        "units": {
          "energy": "eV",
          "seebeck_coefficient": "μV/K"
        }
      },
      "description": "Seebeck coefficient as a function of energy for all three systems. Checker compares range/values near the Fermi level to a hidden reference."
    },
    {
      "file": "step_03_zt.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "energy(eV)",
          "system",
          "zt"
        ],
        "units": {
          "energy": "eV",
          "zt": "dimensionless"
        }
      },
      "description": "Figure of merit ZT as a function of energy for all three systems. Checker compares maximum ZT value to a hidden reference."
    }
  ],
  "notes": "Each CSV should contain enough energy points to resolve resonance features in the HOMO-LUMO gap. The energy grid should be fine enough to capture the reported resonance peaks."
}
```

## How you are scored
A hidden verifier independently evaluates each scored stage's CSV artifact. For transmission, it locates resonance peaks in the HOMO-LUMO gap and compares their approximate energy positions to a hidden reference. For Seebeck, it extracts the range of the Seebeck coefficient near the Fermi level and checks it against a reference. For ZT, it finds the maximum ZT value for Co@C60 and compares it to a threshold. Each stage contributes a weight to the final reward (0 – 1). Reporting memorised numbers from the literature is not sufficient; the verifier expects the curves to originate from your own simulation and will evaluate the numerical values accordingly.
