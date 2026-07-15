# Monte Carlo Hot-Electron Transport Simulation and Second-Derivative Analysis

## Problem background
Hot-electron transport across a metal/semiconductor interface is central to several device concepts, including ballistic electron spectroscopy and heterostructure-integrated thermionic (HIT) energy converters. This task investigates the degree to which transverse electron momentum is conserved when hot electrons cross an epitaxial ErAs/GaAs(100) interface. The system under study is an Al/Al<sub>2</sub>O<sub>3</sub>/Al/ErAs/GaAs metal-base transistor operated in common-base configuration at 80 K. Electrons tunnel from an Al emitter through a thin oxide barrier into an Al/ErAs base, then traverse the base and may enter the GaAs collector provided their energy exceeds the Schottky barrier. By measuring the collector current I<sub>cb</sub> and emitter current I<sub>eb</sub> as the emitter bias V<sub>eb</sub> is swept, one obtains a transfer ratio α = I<sub>cb</sub>/I<sub>eb</sub>. Spectroscopic analysis of this ratio — in particular its second derivative with respect to the emitter energy — can reveal the relative contributions of the Γ and L conduction valleys in GaAs. Because the Γ valley lies at the zone centre (low transverse momentum) and the L valleys lie at finite transverse momentum, the shape of d²α/d(eV)² indicates how strongly the interfacial scattering randomizes the electron momentum. The goal of this reproduction is to compute that second-derivative spectrum for the case of complete interfacial scattering, allowing one to infer the degree of transverse momentum conservation at the interface.

## Approach
The experiment is modelled with a Monte Carlo simulation of hot-electron transport. The emitter and base are described by a free-electron model, while the GaAs collector is treated in an effective-mass picture that includes both the Γ and L conduction valleys. The tunnel barrier is assumed to be planar with a fixed thickness and barrier height; the tunnelling process preferentially transmits electrons with small transverse wave vector. After traversing the base, electrons encounter the ErAs/GaAs interface where they can be admitted into the collector if their energy and transverse momentum match an available conduction-band state. The interfacial scattering mechanism is taken as isotropic S‑wave events that randomise the electron's total momentum, characterised by a scattering probability p. For this task the simulation must be run with p = 1 (100 % scattering), meaning every electron reaching the interface loses all memory of its incident direction. Multiple reflections inside the base and elastic scattering within the base are ignored, consistent with the simplified transport model used in the literature. By sweeping the emitter voltage V<sub>eb</sub> from 0.85 V to 1.3 V with fine enough steps to yield a smooth derivative, the Monte Carlo code generates the emitter current I<sub>eb</sub> and collector current I<sub>cb</sub> at each bias. The transfer ratio α(V<sub>eb</sub>) = I<sub>cb</sub>/I<sub>eb</sub> is then computed, smoothed if necessary, and numerically differentiated twice to obtain d²α/d(eV)². The resulting spectral curve is the primary output of the reproduction.

## Reproduction target
Implement the Monte Carlo simulation described above for the 100% interfacial scattering case (p = 1). Use a tunnel barrier thickness of 15 Å and a barrier height of 2.2 eV. Sweep the emitter bias from 0.85 to 1.3 V with sufficient resolution to support a clean numerical second derivative. Record the emitter and collector currents and then compute the transfer ratio and its second derivative d²α/d(eV)². Write the final second-derivative curve to a CSV file with columns energy_eV (the emitter bias in eV) and d2_alpha (the dimensionless second derivative). The curve must capture the shape of the experimental second-derivative spectrum for this scattering scenario.

## Assets
This task does not require any external datasets, pre-trained models, or proprietary software. All necessary material parameters (GaAs effective masses for the Γ and L valleys, Al free-electron density, Schottky barrier height, etc.) are standard values available in semiconductor physics textbooks or the public literature. The agent should implement the simulation from scratch using widely available scientific computing libraries (e.g., NumPy, SciPy). No downloadable asset manifest exists; the task is self-contained once the required physical constants are looked up.

## Workflow steps

### Step 1: Monte Carlo simulation of hot-electron transport
- Role: process
- Action: Implement and run a Monte Carlo simulation of electron transport through an Al/ErAs/GaAs metal-base transistor. Use a free-electron model for the Al emitter and base, and an effective-mass description for the GaAs conduction valleys (Γ and L). Model interfacial scattering as isotropic S-wave events that randomize total momentum, with probability 100%. Use a tunnel barrier thickness of 15 Å and barrier height 2.2 eV. Ignore multiple reflections and elastic scattering within the base. Sweep emitter voltage V_eb from 0.85 to 1.3 V with sufficient resolution to later compute a smooth second derivative, and for each voltage, compute the emitter current I_eb and collector current I_cb. Record the results in a CSV file with columns: V_eb (V), I_eb (arbitrary units), I_cb (arbitrary units).
- Evidence: `/app/outputs/simulated_currents.csv`

### Step 2: Compute second derivative of transfer ratio
- Role: scored (load-bearing)
- Action: From the simulated currents, compute the transfer ratio α = I_cb / I_eb. Smooth the curve and numerically compute its second derivative with respect to emitter energy d²α/d(eV)². Output the result as a CSV file with columns: energy_eV (the emitter bias in eV) and d2_alpha (dimensionless).
- Output file: `/app/outputs/second_derivative_curve.csv`
- Format: csv
- Contract: Two columns: energy_eV (float), d2_alpha (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/second_derivative_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### second_derivative_curve.csv
- path: `/app/outputs/second_derivative_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The second derivative of the normalized collector-to-emitter current ratio as a function of emitter energy, for the 100% interfacial scattering case. This curve is the primary result compared to experimental data.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `d2_alpha`
  - `units`:
    - `energy_eV`: eV
    - `d2_alpha`: dimensionless

Notes: The checker will compare the submitted curve against a hidden reference curve using Pearson correlation and mean absolute error; the agent must not hardcode the answer.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "second_derivative_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "d2_alpha"
        ],
        "units": {
          "energy_eV": "eV",
          "d2_alpha": "dimensionless"
        }
      },
      "description": "The second derivative of the normalized collector-to-emitter current ratio as a function of emitter energy, for the 100% interfacial scattering case. This curve is the primary result compared to experimental data."
    }
  ],
  "notes": "The checker will compare the submitted curve against a hidden reference curve using Pearson correlation and mean absolute error; the agent must not hardcode the answer."
}
```

## How you are scored
A hidden verifier independently examines each workflow stage's output and combines the scores into a final reward in [0,1]. The primary scoring is on the second-derivative curve (`second_derivative_curve.csv`). The verifier reads your submitted energy–d2_alpha pairs, interpolates them onto a common energy grid, applies min‑max normalisation to both your curve and a hidden reference curve, and then computes the Pearson correlation coefficient and the mean absolute error (MAE). A high correlation and a low MAE are required to pass; the precise thresholds are hidden. Reporting the paper's numbers without running the simulation is not sufficient: the verifier checks the shape of the entire curve, not a single aggregated scalar. Intermediate evidence (e.g., `simulated_currents.csv`) may be audited but carries little direct weight.
