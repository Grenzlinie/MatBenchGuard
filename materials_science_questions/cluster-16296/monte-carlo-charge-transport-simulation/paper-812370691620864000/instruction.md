# Monte Carlo Simulation of Electron Transport and Superlattice Formation in InN Diode

## Problem background
Electron transport in InN n⁺nn⁺ diodes at low lattice temperature (80 K) under applied bias is studied using the Monte Carlo particle technique. At bias voltages high enough to force strong optical‑phonon emission but below the threshold for intervalley transfer, electrons are repeatedly accelerated and then lose energy by emitting an optical phonon, leading to a spatial periodic modulation of transport quantities in the lightly doped n‑region. This periodic motion forms a superlattice‑like structure that can enable microwave power generation in the THz range. The goal is to compute the steady‑state spatial profiles and the small‑signal impedance spectrum to determine under what conditions negative differential resistance emerges.

## Approach
The simulation uses the Monte Carlo particle (MCP) technique to solve the coupled Boltzmann, Poisson, and, for the impedance analysis, external circuit equations. A spherically symmetric nonparabolic conduction band is used with material parameters for wurtzite InN taken from published literature (e.g., Foutz et al., J. Appl. Phys. 85, 7727 (1999) for band parameters; Bernardini et al., Phys. Rev. B63, 193201 (2001) for piezoelectric constants). Scattering mechanisms include polar optical phonons (ħω₀ = 89 meV), acoustic deformation and piezoelectric phonons (treated as elastic at low energies), and ionized impurities. Electron‑electron scattering is neglected.

The device is a 0.02–3.0–0.02 μm n⁺nn⁺ diode with doping concentrations n = 2.2×10¹⁶ cm⁻³ in the n‑region and n⁺ = 10¹⁸ cm⁻³ in the contacts, at lattice temperature 80 K and applied DC bias 1.2 V.

First, a steady‑state MCP simulation is performed to extract spatial profiles across the n‑region. From these profiles, the spatial period of the superlattice (the average distance between successive optical‑phonon‑emission “stop” regions) is computed. Then, a small‑signal analysis is carried out by applying a sinusoidal voltage perturbation U(t) = 1.2 + 0.1·cos(2πft) V over a range of frequencies f, and the complex impedance Z(f) is derived from the current response.

## Reproduction target
You must reproduce the steady‑state transport properties and the high‑frequency response of the InN diode. Specifically:

1. Obtain the spatial profiles of electron concentration n(x), average velocity v(x), mean energy ε(x), electric field E(x), and effective optical‑phonon emission rate v_o(x) across the n‑region. The profiles should reveal the periodic structure.

2. From these profiles, determine the superlattice period l₀, i.e., the average distance between consecutive optical‑phonon emission stop regions.

3. Compute the small‑signal impedance Z(f) (real and imaginary parts) for frequencies in the THz range, covering at least 0.5 to 1.5 THz with fine frequency resolution. The impedance spectrum should be analyzed to identify whether negative real impedance occurs and, if so, the frequency range and the frequency of the minimum.

All outputs must be written to the files specified in the workflow steps under `/app/outputs`. The raw data you provide will allow the hidden verifier to recompute the period and check the impedance characteristics without relying on any pre‑computed summary.

## Assets

- InN wurtzite material parameters (band structure, scattering rates): 10.1063/1.369839

## Workflow steps

### Step 1: Model and simulation setup
- Role: process
- Action: Define device geometry (0.02–3.0–0.02 μm n+nn+ diode), doping concentrations (n=2.2×10^16 cm^-3, n+=1×10^18 cm^-3), lattice temperature T=80 K, applied bias U=1.2 V, and set up InN material parameters and scattering models (polar optical phonons, acoustic deformation, piezoelectric, ionized impurity). Prepare input configuration for the subsequent MCP simulation.
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Steady-state MCP simulation and output profiles
- Role: scored (load-bearing)
- Action: Run a Monte Carlo particle simulation solving the coupled Boltzmann and Poisson equations for the diode to reach a steady state. Extract spatial profiles along the n-region: electron concentration n(x), velocity v(x), energy ε(x), electric field E(x), and effective optical-phonon emission rate v_o(x). Write the profiles to a CSV file.
- Output file: `/app/outputs/step_01_profiles.csv`
- Format: csv
- Contract: CSV with columns: x (µm, float), n (cm^-3, float), v (cm/s, float), energy (eV, float), field (kV/cm, float), v_o (s^-1, float). At least 100 data points uniformly covering x=0 to 3.0 µm.
- Scoring: scored by hidden verifier

### Step 3: Extract superlattice period
- Role: scored
- Action: From the steady-state profiles (e.g., by peak detection on v_o(x)), compute the average distance between successive stop regions and write the spatial period l0 in microns to a plain text file.
- Output file: `/app/outputs/step_02_period.txt`
- Format: txt
- Contract: A single floating-point number (l0 in µm) with no extra text.
- Scoring: scored by hidden verifier

### Step 4: Small-signal impedance simulation
- Role: scored (load-bearing)
- Action: Perform MCP simulation of the diode with a small periodic voltage perturbation U(t)=1.2+0.1·cos(2πft) V for a range of frequencies f. Compute the complex small-signal impedance Z(f) from the current response and write the frequency-dependent real and imaginary parts to a CSV file.
- Output file: `/app/outputs/step_03_impedance.csv`
- Format: csv
- Contract: CSV with columns: frequency_THz (float), ReZ_cm2 (float), ImZ_cm2 (float). Frequency points covering 0.5 to 1.5 THz with at least 0.01 THz resolution.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_profiles.csv`
- `/app/outputs/step_02_period.txt`
- `/app/outputs/step_03_impedance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_profiles.csv
- path: `/app/outputs/step_01_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Steady-state spatial profiles of electron concentration, velocity, energy, electric field, and optical-phonon emission rate in the n-region of the InN diode. The checker recomputes the superlattice period and verifies peak count.
- schema:
  - `type`: table
  - `required_columns`: `x`, `n`, `v`, `energy`, `field`, `v_o`
  - `units`:
    - `x`: µm
    - `n`: cm^-3
    - `v`: cm/s
    - `energy`: eV
    - `field`: kV/cm
    - `v_o`: s^-1

### step_02_period.txt
- path: `/app/outputs/step_02_period.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The superlattice period l0 extracted from the stop regions in the profiles.
- schema:
  - `type`: text
  - `schema`: single floating-point number representing the superlattice period in microns, no extra text

### step_03_impedance.csv
- path: `/app/outputs/step_03_impedance.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Frequency-dependent small-signal impedance spectrum. The checker recomputes the frequency range of negative ReZ and the frequency of minimum ReZ.
- schema:
  - `type`: table
  - `required_columns`: `frequency_THz`, `ReZ_cm2`, `ImZ_cm2`
  - `units`:
    - `frequency_THz`: THz
    - `ReZ_cm2`: cm^2
    - `ImZ_cm2`: cm^2

Notes: The nonlocal v(E) and v_o(ε) curves, comparison with bulk-mobility impedance, and microwave power generation in a resonant circuit are not scored targets; they are either derived from the same profiles or require additional circuit parameters beyond the main scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "n",
          "v",
          "energy",
          "field",
          "v_o"
        ],
        "units": {
          "x": "µm",
          "n": "cm^-3",
          "v": "cm/s",
          "energy": "eV",
          "field": "kV/cm",
          "v_o": "s^-1"
        }
      },
      "description": "Steady-state spatial profiles of electron concentration, velocity, energy, electric field, and optical-phonon emission rate in the n-region of the InN diode. The checker recomputes the superlattice period and verifies peak count."
    },
    {
      "file": "step_02_period.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "schema": "single floating-point number representing the superlattice period in microns, no extra text"
      },
      "description": "The superlattice period l0 extracted from the stop regions in the profiles."
    },
    {
      "file": "step_03_impedance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_THz",
          "ReZ_cm2",
          "ImZ_cm2"
        ],
        "units": {
          "frequency_THz": "THz",
          "ReZ_cm2": "cm^2",
          "ImZ_cm2": "cm^2"
        }
      },
      "description": "Frequency-dependent small-signal impedance spectrum. The checker recomputes the frequency range of negative ReZ and the frequency of minimum ReZ."
    }
  ],
  "notes": "The nonlocal v(E) and v_o(ε) curves, comparison with bulk-mobility impedance, and microwave power generation in a resonant circuit are not scored targets; they are either derived from the same profiles or require additional circuit parameters beyond the main scope."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that inspects each output artifact. The verifier extracts the spatial period from the profile CSV (step_01_profiles.csv) and compares it against a hidden reference. It also processes the impedance CSV (step_03_impedance.csv) to determine the frequency range where the real part is negative (if any) and the frequency of its minimum, comparing those characteristics to hidden expected values. Each scored step carries a weight, and the final reward is a weighted sum between 0 and 1. Reporting a number that happens to match a published value is not sufficient; the verifier recomputes from your raw data and checks that the physical behaviour (period, negative‑resistance window, minimum location) is consistent with the simulation. The exact tolerances and weights are not disclosed.
