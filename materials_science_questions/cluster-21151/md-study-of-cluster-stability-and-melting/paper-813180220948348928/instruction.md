# Spectral Shifts and Linewidths of Perylene-Ar_n Clusters via MD and Semiclassical Lineshapes

## Problem background
Perylene·Ar_n heteroclusters serve as microscopic probes of solvation phenomena. The electronic absorption spectra of these clusters exhibit isomer‑specific spectral shifts and linewidths that reflect the local solvent arrangement and the dynamics of the rare‑gas adatoms. Understanding how the spectral observables depend on cluster size, isomer structure, and temperature provides insight into the interplay between static configuration and nuclear motion, including the onset of isomerization. The aim is to compute the inhomogeneous absorption lineshapes and extract the spectral shift (δν), the total inhomogeneous FWHM (Γ), and the mean homogeneous linewidth (Γ̃) for selected structural isomers of perylene·Ar_n.

## Approach
Classical molecular dynamics (MD) simulations are combined with a semiclassical spectral density method to predict the absorption lineshapes. Ground‑state constant‑energy trajectories are used to sample the phase space of perylene·Ar_n clusters built with Lennard‑Jones atom–atom potentials. Along each trajectory the time‑dependent energy gap U(t) = V_e − V_g is computed from ground‑ and excited‑state potentials. The classical energy‑gap autocorrelation function J(τ) is Fourier‑transformed, and a semiclassical correction is applied to obtain J_SC(ω). Each microcanonical subspectrum is then computed via the time‑domain double‑integral formula involving the two‑time cumulative integral of J_SC(τ). The final inhomogeneous lineshape for a given isomer is the average over 100 independent subspectra obtained from different initial phase‑space points. The spectral observables are extracted from these averaged lineshapes. The procedure is repeated for the isomers (5|0), (5|5), and (22|0) at T=30 K and over a temperature series from 5 K to 40 K.

## Reproduction target
For the perylene·Ar_n heteroclusters, compute the spectral shift δν, the total inhomogeneous linewidth Γ, and the mean homogeneous linewidth Γ̃ for the (5|0), (5|5), and (22|0) structural isomers at a temperature of 30 K. Additionally, compute these three observables for the same isomers at temperatures 5, 10, 15, 20, 30, and 40 K. Write a single JSON file results.json containing all quantities, organised as specified in the output contract.

## Assets

- Perylene 3-D structure (SDF): https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/CID/9152/record/SDF/?record_type=3d&response_type=display
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Cluster model and potential energy setup
- Role: process
- Action: Construct the planar perylene geometry from the PubChem SDF, then build the specified structural isomers (5|0), (5|5), (22|0) by placing Ar atoms according to the isomer descriptions. Define the ground- and excited-state Lennard-Jones pair potentials using the atom–atom parameters and excited-state scaling factors given in the method description.
- Evidence: none

### Step 2: MD simulation and lineshape computation
- Role: process
- Action: For each specified isomer and temperature, perform classical constant-energy ground-state MD trajectories, compute the time-dependent energy gap U(t), calculate the classical autocorrelation J(τ) and its semiclassically corrected spectral density J_SC(ω), evaluate each microcanonical homogeneous subspectrum via the time-domain formula, and average the 100 subspectra to obtain the isomer-specific inhomogeneous lineshape. Extract the spectral maximum (δν), the total FWHM (Γ), and the mean homogeneous linewidth (Γ̃).
- Evidence: `/app/outputs/trajectory_log.csv`

### Step 3: Assemble final spectral observables
- Role: scored (load-bearing)
- Action: Collect the extracted δν, Γ, and Γ̃ for the isomers (5|0), (5|5), (22|0) at T=30 K and over the temperature series (5, 10, 15, 20, 30, 40 K), and write a structured JSON file results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"isomers": ["(5|0)", "(5|5)", "(22|0)"], "T30": {"(5|0)": {"shift_cm-1": float, "Gamma_cm-1": float, "Gamma_tilde_cm-1": float}, ...}, "T_series": {"(5|0)": {"T_K": [float], "shift_cm-1": [float], "Gamma_cm-1": [float], "Gamma_tilde_cm-1": [float]}, ...}}
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
- target_policy: threshold_or_better
- description: The final spectral observables (shift, inhomogeneous FWHM, mean homogeneous linewidth) for (5|0), (5|5), (22|0) at T=30 K and across temperatures 5–40 K.
- schema:
  - `type`: object
  - `required`:
    - `isomers`: list of isomer codes
    - `T30`: object mapping isomer code to {shift_cm-1, Gamma_cm-1, Gamma_tilde_cm-1}
    - `T_series`: object mapping isomer code to {T_K: list of temperatures, shift_cm-1: list, Gamma_cm-1: list, Gamma_tilde_cm-1: list}
  - `items`: object
  - `required_columns`:
  - `units`:
    - `shift_cm-1`: cm⁻¹
    - `Gamma_cm-1`: cm⁻¹
    - `Gamma_tilde_cm-1`: cm⁻¹
    - `T_K`: K

Notes: The checker compares the reported shifts and linewidths to hidden gold values derived from the paper's figures, using tolerances that accommodate stochastic variation and implementation differences. The target_policy is threshold_or_better because a successful reproduction should yield values within an acceptable range relative to the paper.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "isomers": "list of isomer codes",
          "T30": "object mapping isomer code to {shift_cm-1, Gamma_cm-1, Gamma_tilde_cm-1}",
          "T_series": "object mapping isomer code to {T_K: list of temperatures, shift_cm-1: list, Gamma_cm-1: list, Gamma_tilde_cm-1: list}"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "shift_cm-1": "cm⁻¹",
          "Gamma_cm-1": "cm⁻¹",
          "Gamma_tilde_cm-1": "cm⁻¹",
          "T_K": "K"
        }
      },
      "description": "The final spectral observables (shift, inhomogeneous FWHM, mean homogeneous linewidth) for (5|0), (5|5), (22|0) at T=30 K and across temperatures 5–40 K."
    }
  ],
  "notes": "The checker compares the reported shifts and linewidths to hidden gold values derived from the paper's figures, using tolerances that accommodate stochastic variation and implementation differences. The target_policy is threshold_or_better because a successful reproduction should yield values within an acceptable range relative to the paper."
}
```

## How you are scored
A hidden automated verifier inspects your results.json and compares the reported values against reference data derived from a primary research publication. The verifier checks the file structure and then evaluates the T=30 K observables (δν, Γ, Γ̃) for each isomer, as well as the temperature‑dependent lines, using tolerances that account for stochastic variation and implementation differences. You receive partial credit when your numbers are close to the reference or when overall trends (e.g., temperature dependence) are consistent. Each required field contributes to the final score; missing fields or syntactically invalid entries result in zero reward for that component. Reporting a plausible value alone is insufficient — you must run the full simulation pipeline to produce the JSON file.
