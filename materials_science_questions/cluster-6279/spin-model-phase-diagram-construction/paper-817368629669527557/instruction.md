# Heisenberg Antiferromagnet: Critical Temperatures, Exponents and Phase Transition Order

## Problem background
The classical Heisenberg antiferromagnet on a body-centered cubic (bcc) lattice with competing first- (J1) and second- (J2) nearest-neighbor exchange interactions exhibits a rich phase diagram. Frustration induced by a nonzero J2 can alter the nature of the magnetic ordering and the phase transition itself. This task explores how the ratio r = |J2/J1| affects the critical temperature, the universality class of the critical behavior, and the order of the phase transition from the antiferromagnetic to the paramagnetic state. The goal is to compute these properties for selected interaction ratios using large-scale Monte Carlo simulations, and then to extract the critical temperatures, static critical exponents, and transition order — providing quantitative insight into the interplay between frustration and criticality in a three-dimensional Heisenberg system.

## Approach
We study the model using the replica exchange (parallel tempering) Monte Carlo method to ensure efficient sampling near the critical region. Simulations are performed on bcc lattices of various linear sizes L with periodic boundary conditions. For each r, we collect time series of the internal energy and the sublattice magnetization over a broad range of temperatures. From these time series we compute thermodynamic observables (heat capacity, magnetic susceptibility, sublattice magnetization) and higher-order cumulants (Binder cumulant of the magnetization, energy cumulants V_n). The critical temperature T_N is located by the common intersection point of the magnetization Binder cumulant curves for different lattice sizes. At T_N, finite-size scaling relations are applied: the scaling of the cumulants yields the correlation-length exponent ν, while the scaling of the magnetization and susceptibility gives the ratios β/ν and γ/ν. The heat-capacity peak scaling provides α/ν, and Fisher's exponent η follows from η = 2 − γ/ν. For the regime where a first-order transition may occur, we construct histograms of the internal energy distribution and examine the temporal dynamics of the energy to detect coexistence between distinct energy levels.

## Reproduction target
Implement the above Monte Carlo workflow for three interaction ratios: r = 0.0, 0.6, and 0.7. For r = 0.0 and 0.6, use lattice sizes L = 12, 16, 20, 24 to determine the critical temperature from Binder cumulants and then extract the full set of static critical exponents ν, α, β, γ, η via finite-size scaling. For r = 0.7, use a large lattice (L ≥ 80) to resolve the order of the phase transition from the energy distribution and internal energy dynamics. Produce the critical temperatures as a JSON file, the critical exponents as a CSV file, and the transition order (first‑order or second‑order) as a text file.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Monte Carlo Simulation
- Role: process
- Action: Implement a replica exchange Monte Carlo simulation of the classical Heisenberg antiferromagnet on a bcc lattice with first and second nearest neighbor interactions. For each interaction ratio r = 0.0, 0.6, and 0.7, run simulations on several linear system sizes L spanning a range suitable for finite‑size scaling (for r=0.0 and 0.6, use L up to at least 90, e.g., L = 24, 48, 72, 90; for r=0.7, use L ≥ 80). Collect time series of internal energy U and sublattice magnetization M at a dense set of temperatures near the expected critical region.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute Thermodynamic Observables
- Role: process
- Action: From the simulation time series, compute heat capacity C, magnetic susceptibility χ, sublattice magnetization M, and energy cumulants V_n (n=1,2,3) as functions of temperature for each (r, L). Use the standard statistical formulas based on fluctuations of energy and sublattice magnetization.
- Evidence: none

### Step 3: Determine Critical Temperatures
- Role: scored
- Action: For each r, plot the Binder magnetization cumulant U_L versus temperature for different L. Locate the common intersection point to obtain the critical temperature T_N. Output the best estimate for each r in a JSON file.
- Output file: `/app/outputs/critical_temperatures.json`
- Format: json
- Contract: JSON object with keys 'r=0.0', 'r=0.6', 'r=0.7', each mapping to a float (the critical temperature).
- Scoring: scored by hidden verifier

### Step 4: Compute Critical Exponents
- Role: scored (load-bearing)
- Action: For r=0.0 and 0.6, at T=T_N, apply finite-size scaling: fit log(V_n) vs log(L) to obtain ν; log(M) vs log(L) to obtain β/ν; log(χ) vs log(L) to obtain γ/ν; peak heat capacity scaling to obtain α/ν; and η = 2 - γ/ν. Output the resulting exponents as a CSV file.
- Output file: `/app/outputs/critical_exponents.csv`
- Format: csv
- Contract: CSV with columns: r (string), nu (float), alpha (float), beta (float), gamma (float), eta (float). One row per r.
- Scoring: scored by hidden verifier

### Step 5: Phase Transition Order for r=0.7
- Role: scored (load-bearing)
- Action: For r=0.7, using the largest available lattice size (L ≥ 80), construct the energy distribution histogram near T_N and monitor the temporal dynamics of internal energy. Determine whether the transition is first-order (bimodal distribution, coexistence of energy levels) or second-order. Output the result as a single string.
- Output file: `/app/outputs/transition_order.txt`
- Format: txt
- Contract: A single line containing either 'first-order' or 'second-order'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_temperatures.json`
- `/app/outputs/critical_exponents.csv`
- `/app/outputs/transition_order.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_temperatures.json
- path: `/app/outputs/critical_temperatures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The critical temperature for each r obtained from Binder cumulant intersection.
- schema:
  - `type`: object
  - `required`:
    - `r=0.0`:
      - `type`: number
    - `r=0.6`:
      - `type`: number
    - `r=0.7`:
      - `type`: number
  - `description`: Critical temperatures for the three interaction ratios.

### critical_exponents.csv
- path: `/app/outputs/critical_exponents.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static critical exponents derived from finite‑size scaling analysis.
- schema:
  - `type`: table
  - `required_columns`: `r`, `nu`, `alpha`, `beta`, `gamma`, `eta`
  - `items`:
    - `r`:
      - `type`: string
    - `nu`:
      - `type`: float
    - `alpha`:
      - `type`: float
    - `beta`:
      - `type`: float
    - `gamma`:
      - `type`: float
    - `eta`:
      - `type`: float
  - `description`: Critical exponents for r=0.0 and r=0.6.

### transition_order.txt
- path: `/app/outputs/transition_order.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The order of the phase transition for r=0.7 determined from energy histogram and temporal dynamics.
- schema:
  - `type`: text
  - `description`: A single line containing either 'first-order' or 'second-order'.

Notes: Scoring compares the reported values to hidden reference values from the paper with suitable tolerances. Transition order is checked by exact string match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "r=0.0": {
            "type": "number"
          },
          "r=0.6": {
            "type": "number"
          },
          "r=0.7": {
            "type": "number"
          }
        },
        "description": "Critical temperatures for the three interaction ratios."
      },
      "description": "The critical temperature for each r obtained from Binder cumulant intersection."
    },
    {
      "file": "critical_exponents.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "nu",
          "alpha",
          "beta",
          "gamma",
          "eta"
        ],
        "items": {
          "r": {
            "type": "string"
          },
          "nu": {
            "type": "float"
          },
          "alpha": {
            "type": "float"
          },
          "beta": {
            "type": "float"
          },
          "gamma": {
            "type": "float"
          },
          "eta": {
            "type": "float"
          }
        },
        "description": "Critical exponents for r=0.0 and r=0.6."
      },
      "description": "Static critical exponents derived from finite‑size scaling analysis."
    },
    {
      "file": "transition_order.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line containing either 'first-order' or 'second-order'."
      },
      "description": "The order of the phase transition for r=0.7 determined from energy histogram and temporal dynamics."
    }
  ],
  "notes": "Scoring compares the reported values to hidden reference values from the paper with suitable tolerances. Transition order is checked by exact string match."
}
```

## How you are scored
Each of the three scored artifacts (critical temperatures, critical exponents, transition order) is evaluated by an automated hidden verifier. The verifier compares your submitted numerical values and string answer against the reference results obtained from the original study. The scores for each artifact are combined by weight to produce a final reward between 0 and 1. Meeting or exceeding the expected precision yields full credit; the reward decreases as the reported values deviate further from the reference. You must run the entire simulation and analysis pipeline—merely reporting the reference numbers is not sufficient.
