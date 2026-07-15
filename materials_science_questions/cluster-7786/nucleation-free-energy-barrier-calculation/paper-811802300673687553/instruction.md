# Nucleation Free-Energy Barrier Calculation

## Problem background
The three-dimensional ferromagnetic plaquette Ising model (FPIM) on a simple cubic lattice consists of Ising spins interacting via four-spin products on each elementary plaquette. With periodic boundary conditions, the model exhibits a first-order melting transition at a temperature near 3.60 (in natural units with coupling J=1 and Boltzmann constant k_B=1). When the liquid phase is slowly cooled below this melting point, a second, sharper anomaly appears at a lower temperature around 3.40, marked by a drop in internal energy and a jump in specific heat. Understanding the physical nature of this low-temperature feature—whether it represents a genuine thermodynamic glass transition or a kinetic (spinodal) instability—is the central problem addressed here. The investigation requires computing the configurational entropy of the supercooled liquid, locating the Kauzmann temperature where the extrapolated liquid entropy would equal that of the crystal, and comparing the equilibration time of the supercooled liquid with the nucleation time of stable crystal droplets. The task is to reproduce this thermodynamic and kinetic analysis from Monte Carlo simulations and subsequent calculations, without presupposing the outcome.

## Approach
The analysis proceeds in several conceptual stages. First, Metropolis Monte Carlo simulations are performed on simple cubic lattices with periodic boundary conditions, using a linear cooling protocol, to obtain the internal energy per spin as a function of temperature for the liquid, supercooled liquid, and crystal phases. The crystal energy is fitted to a low-temperature power law, and the quasiequilibrium supercooled liquid energy is extrapolated to lower temperatures with a suitable functional form. Next, thermodynamic integration is used to obtain the Helmholtz free energies of the liquid and crystal from their energy functions. From the free energies, the entropies are derived and the configurational entropy S_c(T) = S_liquid(T) - S_crystal(T) is constructed. The Kauzmann temperature T_K is estimated as the temperature at which the extrapolated configurational entropy vanishes, corresponding to the point where the supercooled liquid entropy would equal the crystal entropy. Separately, the melting temperature T_c is determined from the condition F_liquid(T_c) = F_crystal(T_c). The free-energy difference δF(T) near melting is approximated linearly as δF(T) ≃ 0.5 (T_c - T). The crystal nucleation time at the target temperature T=3.40 is computed using classical nucleation theory, requiring both this free-energy difference and a temperature-dependent surface tension. In a supercooled liquid, the surface tension is renormalized by the presence of many nearly degenerate glassy states and is expected to scale as σ(T) ∝ (T - T_K)^{1/2} in three dimensions. With a known reference nucleation time τ_nuc(3.50) ∼ 10^25 Monte Carlo steps (MCS) provided as an input, the scaling to T=3.40 can be obtained. The quasiequilibration time τ_eq at T=3.40 is estimated from the relaxation time formula τ(T) = 2.23/(T - 3.39) (also provided), using the relation τ_eq ≈ 20 τ. The final task is to compare τ_eq and τ_nuc at T=3.40 and to check whether they are of comparable magnitude, which would identify T≈3.40 as a kinetic spinodal temperature where the supercooled liquid loses metastability.

## Reproduction target
The concrete deliverables are three scored JSON files placed under `/app/outputs`:

1. **Kauzmann temperature** (`step_03_kauzmann_temperature.json`): report the estimated Kauzmann temperature `TK` (a floating-point number in the natural units J=1, k_B=1) together with the string `"units": "temperature"`.

2. **Nucleation time at T=3.40** (`step_05_nucleation_time.json`): report the computed crystal nucleation time at T=3.40 as `tau_nuc` (a floating-point number) with `"T": 3.40` and `"units": "MCS"` (Monte Carlo steps).

3. **Time-scale crossing demonstration** (`step_06_crossing_demonstration.json`): provide the computed values of `tau_eq` (equilibration time) and `tau_nuc` (nucleation time) at T=3.40, together with `"T": 3.40` and the inferred effective spinodal temperature `T_sp` (a number). The goal is to demonstrate that the two time scales are comparable at this temperature, indicating a kinetic spinodal.

Supporting intermediate files (`step_01_energy_data.csv` and `step_02_free_energy.csv`) must also be produced as evidence that the full pipeline was executed, but they are not directly scored.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: 3D Monte Carlo simulation and energy fitting
- Role: process
- Action: Run Metropolis Monte Carlo simulations of the 3D ferromagnetic plaquette Ising model on simple cubic lattices with periodic boundary conditions to obtain internal energy per spin for the supercooled liquid and crystal phases as functions of temperature. Fit the crystal energy and extrapolate the liquid energy using appropriate functional forms. Store the fitted/extrapolated liquid and crystal energies at a dense set of temperatures.
- Evidence: `/app/outputs/step_01_energy_data.csv`

### Step 2: Thermodynamic integration and configurational entropy
- Role: process
- Action: From the fitted energy functions for liquid and crystal, compute the free energies via thermodynamic integration with appropriate integration limits and numerical integration, derive entropies and the configurational entropy S_c(T)=S_liquid−S_crystal. Write a table of T, F_liquid, F_crystal, S_config.
- Evidence: `/app/outputs/step_02_free_energy.csv`

### Step 3: Kauzmann temperature
- Role: scored (load-bearing)
- Action: Using the configurational entropy from the free energy table, extrapolate S_config to zero to estimate the Kauzmann temperature T_K where the supercooled liquid entropy equals the crystal entropy. Write the result to a JSON file with keys TK and units.
- Output file: `/app/outputs/step_03_kauzmann_temperature.json`
- Format: json
- Contract: {"TK": float, "units": "temperature"}
- Scoring: scored by hidden verifier

### Step 4: Nucleation time at T=3.40
- Role: scored (load-bearing)
- Action: Compute the crystal nucleation time at T=3.40 using classical nucleation theory formula with temperature-dependent bulk free-energy difference (linear approximation near melting point) and a renormalized surface-tension scaling relation. Use the melting temperature determined from the free-energy equality and the Kauzmann temperature from the previous step. Use a reference nucleation time at T=3.50 of 1e25 MCS (provided). Write the result to a JSON file with T, tau_nuc, and units.
- Output file: `/app/outputs/step_05_nucleation_time.json`
- Format: json
- Contract: {"T": 3.40, "tau_nuc": float, "units": "MCS"}
- Scoring: scored by hidden verifier

### Step 5: Time-scale crossing demonstration
- Role: scored
- Action: Calculate the quasiequilibration time tau_eq at T=3.40 using the relationship tau_eq ≈ 20 * tau, where tau(T)=2.23/(T−3.39) (provided). Compare with the nucleation time from the previous step and confirm that the two time scales are comparable. Write a JSON file containing T, tau_eq, tau_nuc, and the effective spinodal temperature T_sp=3.40.
- Output file: `/app/outputs/step_06_crossing_demonstration.json`
- Format: json
- Contract: {"T": 3.40, "tau_eq": float, "tau_nuc": float, "T_sp": 3.40}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_kauzmann_temperature.json`
- `/app/outputs/step_05_nucleation_time.json`
- `/app/outputs/step_06_crossing_demonstration.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_kauzmann_temperature.json
- path: `/app/outputs/step_03_kauzmann_temperature.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The estimated Kauzmann temperature T_K.
- schema:
  - `type`: object
  - `required`: `TK`, `units`
  - `properties`:
    - `TK`:
      - `type`: number
    - `units`:
      - `type`: string

### step_05_nucleation_time.json
- path: `/app/outputs/step_05_nucleation_time.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed crystal nucleation time at T=3.40.
- schema:
  - `type`: object
  - `required`: `T`, `tau_nuc`, `units`
  - `properties`:
    - `T`:
      - `type`: number
    - `tau_nuc`:
      - `type`: number
    - `units`:
      - `type`: string

### step_06_crossing_demonstration.json
- path: `/app/outputs/step_06_crossing_demonstration.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Demonstration that tau_eq and tau_nuc are comparable and that T_sp ≈ 3.40.
- schema:
  - `type`: object
  - `required`: `T`, `tau_eq`, `tau_nuc`, `T_sp`
  - `properties`:
    - `T`:
      - `type`: number
    - `tau_eq`:
      - `type`: number
    - `tau_nuc`:
      - `type`: number
    - `T_sp`:
      - `type`: number

Notes: The 2D FPIM analysis is excluded per taskability scope. The equilibration time is computed from the provided relaxation-time formula, not from cooling-rate experiments. The reference nucleation time at T=3.50 is taken as given.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_kauzmann_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "TK",
          "units"
        ],
        "properties": {
          "TK": {
            "type": "number"
          },
          "units": {
            "type": "string"
          }
        }
      },
      "description": "The estimated Kauzmann temperature T_K."
    },
    {
      "file": "step_05_nucleation_time.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "T",
          "tau_nuc",
          "units"
        ],
        "properties": {
          "T": {
            "type": "number"
          },
          "tau_nuc": {
            "type": "number"
          },
          "units": {
            "type": "string"
          }
        }
      },
      "description": "The computed crystal nucleation time at T=3.40."
    },
    {
      "file": "step_06_crossing_demonstration.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "T",
          "tau_eq",
          "tau_nuc",
          "T_sp"
        ],
        "properties": {
          "T": {
            "type": "number"
          },
          "tau_eq": {
            "type": "number"
          },
          "tau_nuc": {
            "type": "number"
          },
          "T_sp": {
            "type": "number"
          }
        }
      },
      "description": "Demonstration that tau_eq and tau_nuc are comparable and that T_sp ≈ 3.40."
    }
  ],
  "notes": "The 2D FPIM analysis is excluded per taskability scope. The equilibration time is computed from the provided relaxation-time formula, not from cooling-rate experiments. The reference nucleation time at T=3.50 is taken as given."
}
```

## How you are scored
A hidden verifier (not visible to you) examines each scored output file independently and compares your reported results against reference values that capture the findings of the original study. For the Kauzmann temperature and the nucleation time, the verifier checks whether your computed numbers lie within acceptable bounds. For the crossing demonstration, it assesses whether τ_eq and τ_nuc are of the same order of magnitude and whether the inferred spinodal temperature is consistent with the analysis. The verifier may also cross-validate your intermediate free-energy and configurational entropy tables to ensure they are physically consistent and that no artifact was fabricated without running the required simulations. The final reward is a weighted combination of the scores for the three JSON artifacts; simply writing a known number is not sufficient—you must execute the full Monte Carlo and thermodynamic integration workflow described in the steps above.
