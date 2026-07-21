# Monte Carlo Simulation of 3D Random-Field Ising Model: Effective Exponents and Magnetization Hysteresis

## Problem background
The three-dimensional random-field Ising model (RFIM) describes Ising spins on a simple cubic lattice with nearest-neighbor ferromagnetic exchange and quenched site-dependent random fields drawn from a binary distribution ±h_R. While the ground state is ferromagnetic for weak fields, the character of the finite-temperature phase transition—whether it is a conventional continuous transition, a continuous transition with unusual exponents, or a fluctuation-driven first-order transition—remains a subject of investigation. Monte Carlo simulations can probe this question by measuring the temperature dependence of the connected susceptibility and the correlation length, from which effective critical exponents can be extracted. Additionally, temperature hysteresis sweeps can reveal a possible magnetization jump, a hallmark of a first-order transition. This task focuses on the case h_R = 1 and requires computing the effective exponents and the hysteresis magnetization.

## Approach
The central method is a heat-bath (Glauber) Monte Carlo simulation of the RFIM on L × L × L simple cubic lattices with periodic boundary conditions. Spins are updated with the standard Glauber transition probability based on the energy change ΔE of a single-spin flip. For the critical-exponent analysis, independent runs are performed on L = 32 and L = 64 lattices at several temperatures above the apparent transition (approximately T = 4.1 to 5.0). Multiple random-field realizations are used at each temperature. The spin Fourier components are recorded, and the connected susceptibility χ(q) is computed. The correlation length ξ is extracted from the small‑q behaviour of χ⁻¹(q) by a linear regression against q². Two effective exponents are then determined: η from a log‑log fit of χ(q=0) vs ξ, and γ from a fit of χ(q=0) vs the reduced temperature (T−T_c)/T, with T_c treated as a fitting parameter. To test for a first-order transition, a single fixed random-field configuration on L = 64 is subjected to a slow cooling sweep from high temperature to low temperature and a subsequent warming sweep, measuring the absolute magnetization at each step. The magnetization on the cooling and warming branches at T = 3.75 and T = 4.0 serves as evidence for (or against) a hysteresis loop.

## Reproduction target
The final scored artifact is a JSON file, results.json, containing the effective exponent η with its standard error, the effective exponent γ with its standard error, and four magnetization values: cooling branch at T = 3.75, cooling branch at T = 4.0, warming branch at T = 3.75, and warming branch at T = 4.0. The exponents must be derived from the Monte Carlo data collected on L = 32 and L = 64 lattices, and the magnetization must come from the temperature hysteresis simulation performed on a single L = 64 sample with h_R = 1.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Monte Carlo simulations for critical exponent analysis
- Role: process
- Action: Implement a Glauber heat-bath Monte Carlo simulation for the 3D random-field Ising model on L=32 and L=64 simple cubic lattices with nearest-neighbor coupling J=1, binary random fields ±h_R (h_R=1), and periodic boundary conditions. Equilibrate and collect thermal averages of spin Fourier components S_q at several temperatures above the apparent transition (e.g., T=4.1 to 5.0). For each temperature, average over multiple field realizations to compute the connected susceptibility χ(q) and extract the correlation length ξ via linear regression of χ^{-1}(q) vs q^2 for small wavevectors. Save the resulting χ(0) and ξ per (L,T).
- Evidence: `/app/outputs/critical_raw_data.csv`

### Step 2: Temperature hysteresis simulation to detect first-order transition
- Role: process
- Action: For a single fixed random-field configuration on an L=64 lattice with h_R=1, perform a cooling sequence from high temperature (e.g., T=5.0) to low temperature (e.g., T=3.5) and a subsequent warming sequence, using Glauber updates. At each temperature, after equilibration, measure the magnetization m = (1/N)|∑_i S_i|. Record the magnetization values at T=3.75 and T=4.0 for both cooling and warming branches.
- Evidence: `/app/outputs/hysteresis_data.csv`

### Step 3: Compute and report effective exponents and hysteresis magnetization
- Role: scored
- Action: From the χ(0) and ξ data obtained in step mc_critical, determine the effective exponent η by a linear least-squares fit of log χ(0) vs log ξ, and the effective exponent γ and apparent T_c by a fit of log χ(0) vs log[(T-T_c)/T] over the temperature range. From the hysteresis data of step mc_hysteresis, extract the magnetization values at T=3.75 (low-T) and T=4.0 (high-T) for both cooling and warming branches. Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"eta": {"value": float, "error": float}, "gamma": {"value": float, "error": float}, "magnetization_cooling_low_T": float, "magnetization_cooling_high_T": float, "magnetization_warming_low_T": float, "magnetization_warming_high_T": float}
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
- target_policy: reference_match
- description: Reproduced effective critical exponents and hysteresis magnetization values; compared to the paper's reported numbers for consistency.
- schema:
  - `type`: object
  - `required`: `eta`, `gamma`, `magnetization_cooling_low_T`, `magnetization_cooling_high_T`, `magnetization_warming_low_T`, `magnetization_warming_high_T`
  - `properties`:
    - `eta`:
      - `type`: object
      - `properties`:
        - `value`:
          - `type`: number
        - `error`:
          - `type`: number
      - `required`: `value`, `error`
    - `gamma`:
      - `type`: object
      - `properties`:
        - `value`:
          - `type`: number
        - `error`:
          - `type`: number
      - `required`: `value`, `error`
    - `magnetization_cooling_low_T`:
      - `type`: number
    - `magnetization_cooling_high_T`:
      - `type`: number
    - `magnetization_warming_low_T`:
      - `type`: number
    - `magnetization_warming_high_T`:
      - `type`: number

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "eta",
          "gamma",
          "magnetization_cooling_low_T",
          "magnetization_cooling_high_T",
          "magnetization_warming_low_T",
          "magnetization_warming_high_T"
        ],
        "properties": {
          "eta": {
            "type": "object",
            "properties": {
              "value": {
                "type": "number"
              },
              "error": {
                "type": "number"
              }
            },
            "required": [
              "value",
              "error"
            ]
          },
          "gamma": {
            "type": "object",
            "properties": {
              "value": {
                "type": "number"
              },
              "error": {
                "type": "number"
              }
            },
            "required": [
              "value",
              "error"
            ]
          },
          "magnetization_cooling_low_T": {
            "type": "number"
          },
          "magnetization_cooling_high_T": {
            "type": "number"
          },
          "magnetization_warming_low_T": {
            "type": "number"
          },
          "magnetization_warming_high_T": {
            "type": "number"
          }
        }
      },
      "description": "Reproduced effective critical exponents and hysteresis magnetization values; compared to the paper's reported numbers for consistency."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your results.json and compares the reported exponents and magnetization values to reference targets. The exponent agreement is assessed using pre-defined tolerances; if your reported values fall within those tolerances, full credit is awarded. The four magnetization values are checked for the presence of a clear hysteresis: the low‑temperature magnetizations on both branches are expected to be large, the high‑temperature magnetizations small, and the cooling and warming low‑temperature values are expected to differ substantially. The total reward is a weighted combination: 60% from the exponent agreement and 40% from the hysteresis evidence. Note that simply reporting the exact numbers from any published source is not sufficient—the verifier expects values that emerge from a genuine execution of the described workflow.
