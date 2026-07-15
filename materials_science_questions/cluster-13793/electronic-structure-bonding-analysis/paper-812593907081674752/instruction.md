# Magnetic Moment of Co Carbides from DFT

## Problem background
In Co/C multilayers, the magnetization drops sharply when the Co thickness falls below a few nanometers. This is commonly attributed to a magnetically dead interfacial layer where Co atoms intermix with carbon, forming cobalt carbides (Co₁₋ₓCₓ). Understanding the magnetic moment per Co atom in the most stable carbide phases—Co₃C and Co₂C—is essential for controlling interface magnetism in spintronic and hard-coating applications. Ab initio density-functional theory (DFT) can predict these moments from the known crystal structures, both at ambient pressure and under hydrostatic compression.

## Approach
Use spin-polarized DFT within the generalized gradient approximation (GGA-PBE) to compute the ground-state electronic structure of orthorhombic Co₃C (space group Pnma, lattice parameters a=4.44 Å, b=4.94 Å, c=6.70 Å) and Co₂C (space group Pmnn, a=4.37 Å, b=4.38 Å, c=2.88 Å). For each phase, perform a full structural relaxation at zero pressure, obtain the total magnetic moment per formula unit, and divide by the number of Co atoms to yield the average magnetic moment per Co atom (μB/Co). Then, for Co₃C only, apply a hydrostatic pressure of 23.8 GPa by compressing the lattice using the Birch–Murnaghan equation of state, recompute the electronic structure, and extract the average magnetic moment per Co atom. Any open-source DFT code capable of spin-polarized PBE calculations (e.g., Quantum ESPRESSO, ABINIT, GPAW) may be used, together with appropriate pseudopotentials for Co and C. The workflow produces three numbers, which are written to a JSON file.

## Reproduction target
Compute the average magnetic moment per Co atom (μB/Co) for the three conditions:

1. Co₃C at ambient pressure
2. Co₂C at ambient pressure
3. Co₃C under 23.8 GPa hydrostatic pressure

Write the three numeric values to `/app/outputs/magnetic_moments.json` using the exact keys `Co3C_ambient`, `Co2C_ambient`, and `Co3C_pressurized`. The numbers should be the computed magnetic moments, rounded to a suitable number of decimal places.

## Assets

- Crystal structure of Co₃C (Pnma): ICSD 62991
- Crystal structure of Co₂C (Pmnn): ICSD 60854
- Open-source DFT code: https://www.quantum-espresso.org/
- Pseudopotentials for Co and C: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFT Magnetic Moment Calculation
- Role: scored (load-bearing)
- Action: Perform spin-polarized DFT calculations using GGA-PBE for orthorhombic Co₃C (space group Pnma) and Co₂C (space group Pmnn) with the publicly available crystal structures. For each phase, compute the total magnetic moment per formula unit and divide by the number of Co atoms to obtain the average magnetic moment per Co atom (μB/Co). For Co₃C, also apply hydrostatic pressure of 23.8 GPa using the Birch-Murnaghan equation of state and recompute the magnetic moment. Write the three results to the output file.
- Output file: `/app/outputs/magnetic_moments.json`
- Format: json
- Contract: Object with keys 'Co3C_ambient' (float, μB/Co), 'Co2C_ambient' (float, μB/Co), 'Co3C_pressurized' (float, μB/Co) corresponding to the three calculations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.json
- path: `/app/outputs/magnetic_moments.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Average magnetic moment per cobalt atom (μB/Co) for Co₃C at ambient pressure, Co₂C at ambient pressure, and Co₃C at 23.8 GPa.
- schema:
  - `type`: object
  - `required`: `Co3C_ambient`, `Co2C_ambient`, `Co3C_pressurized`
  - `properties`:
    - `Co3C_ambient`:
      - `type`: number
      - `units`: μB/Co
    - `Co2C_ambient`:
      - `type`: number
      - `units`: μB/Co
    - `Co3C_pressurized`:
      - `type`: number
      - `units`: μB/Co

Notes: The three magnetic moments are compared to the paper‑reported values with a tolerance that accounts for DFT‑code and pseudopotential variability. The scoring checks the absolute values and does not penalise a higher magnetic moment as 'worse' because the target is a fixed physical property, not a directional performance metric.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Co3C_ambient",
          "Co2C_ambient",
          "Co3C_pressurized"
        ],
        "properties": {
          "Co3C_ambient": {
            "type": "number",
            "units": "μB/Co"
          },
          "Co2C_ambient": {
            "type": "number",
            "units": "μB/Co"
          },
          "Co3C_pressurized": {
            "type": "number",
            "units": "μB/Co"
          }
        }
      },
      "description": "Average magnetic moment per cobalt atom (μB/Co) for Co₃C at ambient pressure, Co₂C at ambient pressure, and Co₃C at 23.8 GPa."
    }
  ],
  "notes": "The three magnetic moments are compared to the paper‑reported values with a tolerance that accounts for DFT‑code and pseudopotential variability. The scoring checks the absolute values and does not penalise a higher magnetic moment as 'worse' because the target is a fixed physical property, not a directional performance metric."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/magnetic_moments.json`, extracts the three reported magnetic moments, and compares each one against a hidden reference value. The scoring function rewards agreement within a tolerance that accounts for the spread between different DFT implementations and pseudopotentials. Each of the three moments contributes equally to the final reward. Simply reporting a number is not enough; the verifier checks the content of the submitted artifact.
