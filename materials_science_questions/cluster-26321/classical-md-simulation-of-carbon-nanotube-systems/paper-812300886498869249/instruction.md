# Reproduce Elastic Coefficients of Carbon Nanotubes from Quantum Molecular Dynamics

## Problem background
Single-walled carbon nanotubes (SWNTs) exhibit exceptional mechanical properties under strain, but finite-temperature quantum-mechanical effects on their uniaxial elastic response are challenging to simulate. This reproduction task investigates the structural stability and elasticity of armchair and zigzag SWNTs under uniaxial pressure using an order‑N tight‑binding molecular dynamics (TBMD) method. The goal is to quantify the elastic regime through the quadratic coefficients of the potential energy versus strain and to determine the strain at the potential energy minimum as a function of temperature and tube geometry.

## Approach
Build an O(N) TBMD code using the Fermi matrix expansion method and per-atom localization regions to achieve linear scaling with system size. Use transferable tight-binding parameters for carbon from Xu et al. (1992). Construct models of several SWNT chiralities ((10,10), (8,8), (12,12), (17,0)) with periodic boundary conditions along the tube axis and vacuum padding in the perpendicular directions. Implement the extended Andersen pressure control to vary the uniaxial pressure along the tube axis stepwise while tracking the internal pressure via the virial expression. Run MD simulations at temperatures of 50 K, 300 K, 600 K, and 900 K, recording potential energy per atom and strain time series. From the small-strain region where pressure is well controlled, extract strain-energy data and fit a quadratic form E(ε) = 0.5 a ε² + b ε + c. For the (10,10) tube, report the fitted coefficients a, b, c; for all tubes, compute the strain at the energy minimum ε0 = –b/a and report it.

## Reproduction target
For the (10,10) SWNT, compute the quadratic coefficients a, b, c (in eV/atom) describing the potential energy per atom as a function of axial strain at temperatures of 50 K, 300 K, 600 K, and 900 K. For the (8,8), (12,12), and (17,0) SWNTs, compute the strain at the potential energy minimum ε0 (dimensionless) at those same four temperatures. Report all results in a single JSON file (table_data.json) as specified in the output contract.

## Assets

- Transferable tight-binding parameters for carbon (Xu et al., 1992): https://doi.org/10.1088/0953-8984/4/28/010

## Workflow steps

### Step 1: System construction
- Role: process
- Action: Construct atomic models of (10,10), (8,8), (12,12), and (17,0) single-walled carbon nanotubes with sufficient unit cells to achieve an axial length of approximately 20 Å. Assign the transferable tight-binding parameters for carbon from Xu et al. (1992). Set up the MD supercell with 50 Å vacuum padding in the x and z directions and periodic boundary conditions along the tube axis (y-direction).
- Evidence: none

### Step 2: Pressure-controlled O(N) TBMD simulation
- Role: process
- Action: Implement an order‑N tight‑binding molecular dynamics (TBMD) code using the Fermi matrix expansion method and per-atom localization regions to achieve linear scaling. Incorporate an extended Andersen pressure control with parameters b=0.5, c=0.1 GPa⁻¹, increasing the external prescribed pressure stepwise by 0.2 GPa every 1000 time steps and regulating internal pressure every 100 steps via the virial expression. For each constructed nanotube, run simulations at temperatures of 50 K, 300 K, 600 K, and 900 K using the Verlet integrator with a time step and thermostat as described in the published protocol. Record time series of strain, potential energy per atom, and internal pressure.
- Evidence: none

### Step 3: Quadratic coefficients and ε0 report
- Role: scored (load-bearing)
- Action: For each tube and temperature, identify the small‑strain region where pressure is well controlled. Perform a least‑squares fit of the quadratic form E = 0.5 a ε² + b ε + c to the potential energy per atom vs. strain data. Compute the strain at the potential energy minimum ε0 = −b/a. Output the fitted coefficients a, b, c for the (10,10) tube and the ε0 values for all tubes, organized by temperature, into a single JSON file.
- Output file: `/app/outputs/table_data.json`
- Format: json
- Contract: JSON object with top-level keys: '(10,10)', '(8,8)', '(12,12)', '(17,0)'. For (10,10), the value is an object with keys '50K', '300K', '600K', '900K', each containing numeric fields 'a', 'b', 'c'. For other tubes, the value is an object with the same temperature keys, each containing the numeric field 'epsilon0'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_data.json
- path: `/app/outputs/table_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Table of quadratic coefficients for (10,10) SWNT and strain at potential energy minimum ε0 for all studied nanotubes, used to verify the elastic properties under uniaxial pressure.
- schema:
  - `type`: object
  - `required`:
    - `(10,10)`:
      - `50K`:
        - `a`: number
        - `b`: number
        - `c`: number
      - `300K`:
        - `a`: number
        - `b`: number
        - `c`: number
      - `600K`:
        - `a`: number
        - `b`: number
        - `c`: number
      - `900K`:
        - `a`: number
        - `b`: number
        - `c`: number
    - `(8,8)`:
      - `50K`:
        - `epsilon0`: number
      - `300K`:
        - `epsilon0`: number
      - `600K`:
        - `epsilon0`: number
      - `900K`:
        - `epsilon0`: number
    - `(12,12)`:
      - `50K`:
        - `epsilon0`: number
      - `300K`:
        - `epsilon0`: number
      - `600K`:
        - `epsilon0`: number
      - `900K`:
        - `epsilon0`: number
    - `(17,0)`:
      - `50K`:
        - `epsilon0`: number
      - `300K`:
        - `epsilon0`: number
      - `600K`:
        - `epsilon0`: number
      - `900K`:
        - `epsilon0`: number

Notes: The checker compares each numeric value to hidden reference values with a defined tolerance and verifies that ε0 for each tube is negative and becomes more negative with increasing temperature. No gold values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "(10,10)": {
            "50K": {
              "a": "number",
              "b": "number",
              "c": "number"
            },
            "300K": {
              "a": "number",
              "b": "number",
              "c": "number"
            },
            "600K": {
              "a": "number",
              "b": "number",
              "c": "number"
            },
            "900K": {
              "a": "number",
              "b": "number",
              "c": "number"
            }
          },
          "(8,8)": {
            "50K": {
              "epsilon0": "number"
            },
            "300K": {
              "epsilon0": "number"
            },
            "600K": {
              "epsilon0": "number"
            },
            "900K": {
              "epsilon0": "number"
            }
          },
          "(12,12)": {
            "50K": {
              "epsilon0": "number"
            },
            "300K": {
              "epsilon0": "number"
            },
            "600K": {
              "epsilon0": "number"
            },
            "900K": {
              "epsilon0": "number"
            }
          },
          "(17,0)": {
            "50K": {
              "epsilon0": "number"
            },
            "300K": {
              "epsilon0": "number"
            },
            "600K": {
              "epsilon0": "number"
            },
            "900K": {
              "epsilon0": "number"
            }
          }
        }
      },
      "description": "Table of quadratic coefficients for (10,10) SWNT and strain at potential energy minimum ε0 for all studied nanotubes, used to verify the elastic properties under uniaxial pressure."
    }
  ],
  "notes": "The checker compares each numeric value to hidden reference values with a defined tolerance and verifies that ε0 for each tube is negative and becomes more negative with increasing temperature. No gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier will independently check each scored artifact. It will read your submitted `table_data.json` and compare the reported quadratic coefficients (a, b, c for (10,10)) and the strain-at-minimum ε0 (for all tubes) against hidden reference values with appropriate tolerances. The verifier also validates the structural consistency of your data. The final score is a weighted sum across the scored artifacts: the (10,10) coefficients carry the majority weight, and the ε0 values for the other tubes carry the remainder. The verifier does NOT compare against any paper text or document; it uses pre-recorded reference values and math. Do NOT copy any gold values from external sources — your output will be judged solely on its numerical correctness.
