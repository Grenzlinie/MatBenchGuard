# Reproduce Kosterlitz-Thouless transition temperatures and Ising critical exponent from Monte Carlo simulations of an XY model with nematic coupling on a triangular lattice

## Problem background
The two-dimensional XY model with an additional nematic (biquadratic) coupling on a triangular lattice supports a rich phase diagram that includes algebraic-magnetic, algebraic-nematic, and paramagnetic phases. Determining the temperatures of the Kosterlitz-Thouless transitions and the Ising-type transition, as well as the critical exponent of the latter, is important for understanding statistical-mechanical models and magnetic materials such as triangular-lattice compounds. This task asks you to compute the Kosterlitz-Thouless transition temperatures for two representative nematic coupling strengths and, for the larger coupling, to locate the low-temperature Ising transition and extract its critical exponent from the specific heat.

## Approach
Use the standard Metropolis Monte Carlo algorithm to simulate a ferromagnetic XY model with nematic coupling on triangular lattices of several linear sizes. The Hamiltonian contains standard nearest-neighbour cosine interactions with strengths J1 = 1−x (ferromagnetic) and J2 = x (nematic). For each lattice size and coupling strength, compute the helicity modulus (spin-wave stiffness) from the appropriate configurational averages. The Kosterlitz-Thouless transition temperature for a finite lattice is obtained by the temperature where the helicity modulus crosses the universal critical line; extrapolation to infinite system size yields the thermodynamic transition temperature. For the large-nematic-coupling regime, also compute the specific heat as a function of temperature. The low-temperature peak marks the Ising-type transition; a scaling analysis of the peak shape against the reduced temperature provides an estimate of the critical exponent α.

## Reproduction target
Simulate the model on triangular lattices of sizes L = 18, 27, 36, 45, 54, 72 for nematic coupling strengths x = 0.4 and x = 0.9. For every (x, L) combination, compute the helicity modulus and locate the crossing temperature with the critical line to obtain the finite-size Kosterlitz-Thouless temperature. Fit a polynomial in 1/L to these crossing temperatures and extrapolate to L → ∞, giving a Kosterlitz-Thouless temperature for each x. For x = 0.9 and the lattice size L = 36, compute the specific heat over a temperature range that includes the low-temperature peak. Identify the peak temperature and, from the specific heat data near the peak, perform a scaling fit to extract the critical exponent α of the Ising transition.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Monte Carlo simulation
- Role: process
- Action: Run standard Metropolis Monte Carlo simulations for the Hamiltonian H = -J1 Σ cos(θ_ij) - J2 Σ cos(2θ_ij) on triangular lattices with periodic boundary conditions, using J1 = 1-x and J2 = x. Perform simulations for nematic coupling strengths x = 0.4 and 0.9, each with lattice sizes L = 18, 27, 36, 45, 54, 72. For each (x, L), simulate over a temperature grid spanning the transition region, using 3×10^5 equilibration steps and 2×10^5 production steps per temperature. Record, for each temperature and L, the following averages: ⟨Σ cos(θ_ij)⟩, ⟨Σ cos(2θ_ij)⟩, the average of the squared fluctuation term F = (J1 Σ x_ij sin(θ_ij) + 2J2 Σ x_ij sin(2θ_ij))^2, the average energy ⟨E⟩, and ⟨E^2⟩.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Helicity modulus and crossing temperatures
- Role: scored (load-bearing)
- Action: Compute the helicity modulus Y(T) for each (x, L) pair using the formula Y = (J1/(2L^2))⟨Σ cos θ_ij⟩ + (2J2/L^2)⟨Σ cos 2θ_ij⟩ − (1/(T L^2))⟨(J1 Σ x_ij sin θ_ij + 2J2 Σ x_ij sin 2θ_ij)^2⟩, where J1=1-x, J2=x, and the angle brackets denote the averages recorded in step 1. For each L, determine the temperature where Y(T) crosses the line (2/π)(√3/2)(1+3x)T using linear interpolation. Output a CSV with columns x (float), L (int), and T_cross (float) giving the crossing temperature for every (x, L) combination.
- Output file: `/app/outputs/helicity_crossings.csv`
- Format: csv
- Contract: CSV with columns: x (float), L (int), T_cross (float). x values: 0.4, 0.9; L values: 18,27,36,45,54,72.
- Scoring: scored by hidden verifier

### Step 3: KT temperature extrapolation
- Role: scored
- Action: Read helicity_crossings.csv. For each x, fit a polynomial in 1/L (e.g., quadratic) to the crossing temperatures T_cross vs 1/L, and extrapolate to 1/L=0 to obtain T_KT. Estimate the error from the fit uncertainty. Output a JSON object with two keys: 'x0_4' and 'x0_9', each containing T_KT (float) and error (float).
- Output file: `/app/outputs/KT_temperatures.json`
- Format: json
- Contract: JSON object with keys 'x0_4' and 'x0_9', each an object with fields 'T_KT' (float) and 'error' (float).
- Scoring: scored by hidden verifier

### Step 4: Specific heat for x=0.9
- Role: scored (load-bearing)
- Action: From the simulation data for L=36, x=0.9, compute the specific heat C(T) = (⟨E^2⟩ − ⟨E⟩^2) / (N k_B T^2) where N = L^2 and k_B = 1, over a temperature grid that includes the low-temperature peak (roughly T ∈ [0.2, 0.5]). Output a CSV with columns T (float) and C (float).
- Output file: `/app/outputs/specific_heat_L36_x0.9.csv`
- Format: csv
- Contract: CSV with columns T (float, temperature) and C (float, specific heat).
- Scoring: scored by hidden verifier

### Step 5: Ising transition analysis
- Role: scored
- Action: Read specific_heat_L36_x0.9.csv. Identify the temperature T_l of the low-temperature maximum. Perform a scaling analysis: for temperatures near T_l (e.g., within 0.05), fit C vs |T−T_l| to a power law C ~ A |T−T_l|^{-α} to extract the critical exponent α. Output a JSON with keys T_l (float), alpha (float), and method (string describing the fitting procedure).
- Output file: `/app/outputs/Ising_analysis.json`
- Format: json
- Contract: JSON object with keys 'T_l' (float), 'alpha' (float), 'method' (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/helicity_crossings.csv`
- `/app/outputs/KT_temperatures.json`
- `/app/outputs/specific_heat_L36_x0.9.csv`
- `/app/outputs/Ising_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### helicity_crossings.csv
- path: `/app/outputs/helicity_crossings.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Crossing temperatures of the helicity modulus with the critical line, for every (x, L) combination. The checker recomputes T_KT by fitting a polynomial in L^{-1} and extrapolating to L=infty.
- schema:
  - `type`: table
  - `required_columns`: `x`, `L`, `T_cross`

### KT_temperatures.json
- path: `/app/outputs/KT_temperatures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-extrapolated KT transition temperatures. The checker compares these against its own recomputed T_KT from the raw crossings for consistency.
- schema:
  - `type`: object
  - `required`: `x0_4`, `x0_9`
  - `properties`:
    - `x0_4`:
      - `type`: object
      - `required`: `T_KT`, `error`
    - `x0_9`:
      - `type`: object
      - `required`: `T_KT`, `error`

### specific_heat_L36_x0.9.csv
- path: `/app/outputs/specific_heat_L36_x0.9.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Specific heat as a function of temperature for L=36 at x=0.9. The checker locates the peak and performs a scaling analysis to obtain T_l and alpha.
- schema:
  - `type`: table
  - `required_columns`: `T`, `C`

### Ising_analysis.json
- path: `/app/outputs/Ising_analysis.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-extracted Ising transition temperature and critical exponent. The checker compares these against its own recomputed values from the specific heat data for consistency.
- schema:
  - `type`: object
  - `required`: `T_l`, `alpha`, `method`

Notes: The Monte Carlo simulation is a required process step that must be executed by the agent; no precomputed simulation averages are provided. All scored outputs derive from the agent's own simulation data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "helicity_crossings.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "L",
          "T_cross"
        ]
      },
      "description": "Crossing temperatures of the helicity modulus with the critical line, for every (x, L) combination. The checker recomputes T_KT by fitting a polynomial in L^{-1} and extrapolating to L=infty."
    },
    {
      "file": "KT_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "x0_4",
          "x0_9"
        ],
        "properties": {
          "x0_4": {
            "type": "object",
            "required": [
              "T_KT",
              "error"
            ]
          },
          "x0_9": {
            "type": "object",
            "required": [
              "T_KT",
              "error"
            ]
          }
        }
      },
      "description": "Agent-extrapolated KT transition temperatures. The checker compares these against its own recomputed T_KT from the raw crossings for consistency."
    },
    {
      "file": "specific_heat_L36_x0.9.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "C"
        ]
      },
      "description": "Specific heat as a function of temperature for L=36 at x=0.9. The checker locates the peak and performs a scaling analysis to obtain T_l and alpha."
    },
    {
      "file": "Ising_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "T_l",
          "alpha",
          "method"
        ]
      },
      "description": "Agent-extracted Ising transition temperature and critical exponent. The checker compares these against its own recomputed values from the specific heat data for consistency."
    }
  ],
  "notes": "The Monte Carlo simulation is a required process step that must be executed by the agent; no precomputed simulation averages are provided. All scored outputs derive from the agent's own simulation data."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that operates independently. For helicity_crossings.csv, the verifier will refit the 1/L extrapolation and compare the resulting Kosterlitz-Thouless temperatures to expected values. KT_temperatures.json is checked for consistency with the verifier's own extrapolation. For specific_heat_L36_x0.9.csv, the verifier will locate the low-temperature maximum and perform a scaling analysis to obtain the peak temperature and exponent α. Ising_analysis.json is cross-checked against those recomputed quantities. The final reward is a weighted combination of the scores from all four artifacts; reporting a number without genuine computation does not yield a high score.
