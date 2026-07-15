# Superconductivity in electron-doped alkali-metal hydride Rb1-xSrxH

## Problem background
Alkali-metal hydrides such as RbH are insulators with large band gaps at ambient conditions. Electron doping, achieved by substituting Rb with an alkaline-earth element like Sr, can metallize the hydride without applying external pressure, opening a route to phonon-mediated superconductivity. The solid solution Rb1‑xSrxH (rock‑salt structure) is investigated here using first‑principles density functional theory. The aim is to compute the electronic band gap of pristine RbH, the density of states at the Fermi level N(0) as a function of Sr content, the electron–phonon coupling constant λ, and the superconducting critical temperature Tc, thereby quantifying the doping‑driven superconducting behavior.

## Approach
The workflow uses the plane‑wave pseudopotential method as implemented in Quantum ESPRESSO, with the PBE exchange‑correlation functional and scalar‑relativistic ultrasoft pseudopotentials for Rb, Sr, and H. The virtual crystal approximation (VCA) replaces Rb atoms with a virtual atom of Rb and Sr to model the solid solutions at several Sr concentrations. Structural optimisation incorporates zero‑point energy corrections via the quasi‑harmonic approximation (QHA) to obtain equilibrium lattice parameters for each composition. From these structures, the electronic band structure and density of states are computed, from which the direct band gap at the L‑point (for pristine RbH) and N(0) (for doped compositions) are extracted. Density functional perturbation theory (DFPT) yields phonon dispersions and phonon linewidths (γqj) on a coarse q‑mesh that is subsequently Fourier‑interpolated to a dense mesh. The linewidths and N(0) are used to construct the Eliashberg spectral function α²F(ω) and the average electron–phonon coupling λ. Finally, the isotropic Migdal–Eliashberg gap equations are solved on the imaginary axis, using two values of the Coulomb pseudopotential μ*, to obtain Tc for the highest Sr concentration.

## Reproduction target
You must implement the above protocol and write the following four output files under `/app/outputs`:
- `band_gap_pristine_RbH.txt`: a single floating‑point number giving the direct band gap (eV) of pristine RbH at the L‑point.
- `N0_vs_x.csv`: a CSV with columns `x` and `N0`, containing N(0) (states/eV/atom/spin) for Sr contents x = 0.05, 0.20, 0.45.
- `lambda_vs_x.csv`: a CSV with columns `x` and `lambda`, containing the average electron–phonon coupling constant λ for the same three x values.
- `Tc_at_x045.txt`: two space‑separated floating‑point numbers (units K), the critical temperature at x = 0.45 for μ* = 0.1 and μ* = 0, respectively.
The hidden verifier will evaluate each artifact independently and combine the scores into a final reward.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Rb, Sr, H ultrasoft pseudopotentials (USPP from PSLibrary): https://www.quantum-espresso.org/pseudopotentials/pslibrary
- Isotropic Migdal-Eliashberg solver

## Workflow steps

### Step 1: Structural optimization with ZPE (VCA)
- Role: process
- Action: Perform variable-cell relaxation for Rb1-xSrxH at Sr contents x = 0, 0.05, 0.20, 0.45 using DFT-PBE within Quantum ESPRESSO under the virtual crystal approximation (VCA). Incorporate zero-point energy corrections via the quasi-harmonic approximation to obtain equilibrium lattice parameters for each composition.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Band gap of pristine RbH
- Role: scored
- Action: From the optimized pristine RbH (x=0) structure, compute the electronic band structure and extract the direct band gap at the L-point. Write the value in eV as a single float to band_gap_pristine_RbH.txt.
- Output file: `/app/outputs/band_gap_pristine_RbH.txt`
- Format: txt
- Contract: A single floating-point number.
- Scoring: scored by hidden verifier

### Step 3: Density of states at Fermi level N(0)
- Role: scored
- Action: For each Sr content x = 0.05, 0.20, 0.45, compute the electronic density of states. Determine the Fermi energy and extract N(0) (electronic DOS per atom and per spin at the Fermi level, units: states/eV/atom/spin). Write a CSV file with columns 'x,N0' and one row per composition.
- Output file: `/app/outputs/N0_vs_x.csv`
- Format: csv
- Contract: Two columns: x (float), N0 (float, states/eV/atom/spin). Three data rows.
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion and electron-phonon linewidths
- Role: process
- Action: Using density functional perturbation theory (DFPT) in Quantum ESPRESSO, compute phonon frequencies and phonon linewidths γ_qj for each composition x = 0.05, 0.20, 0.45 on a coarse q-mesh, then Fourier-interpolate to a dense q-mesh. The calculated linewidths and frequencies are needed to build the Eliashberg function.
- Evidence: `/app/outputs/phonon_linewidths.json`

### Step 5: Electron-phonon coupling constant λ
- Role: scored (load-bearing)
- Action: From the phonon linewidths and N(0), compute the Eliashberg spectral function α²F(ω) and the average electron-phonon coupling constant λ for each x using the standard formulas. Write a CSV file with columns 'x,lambda' and one row per composition.
- Output file: `/app/outputs/lambda_vs_x.csv`
- Format: csv
- Contract: Two columns: x (float), lambda (float). Three data rows.
- Scoring: scored by hidden verifier

### Step 6: Superconducting critical temperature Tc
- Role: scored (load-bearing)
- Action: Using the Eliashberg spectral function α²F(ω) for x=0.45, solve the isotropic Migdal-Eliashberg gap equations on the imaginary axis for Coulomb pseudopotentials μ*=0.1 and μ*=0 to obtain the critical temperature Tc. Write two space-separated floats to Tc_at_x045.txt: first Tc with μ*=0.1, then Tc with μ*=0.
- Output file: `/app/outputs/Tc_at_x045.txt`
- Format: txt
- Contract: Two floating-point numbers (units K) separated by a space: Tc(μ*=0.1) Tc(μ*=0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_pristine_RbH.txt`
- `/app/outputs/N0_vs_x.csv`
- `/app/outputs/lambda_vs_x.csv`
- `/app/outputs/Tc_at_x045.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_pristine_RbH.txt
- path: `/app/outputs/band_gap_pristine_RbH.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Direct band gap of pristine RbH at L-point.
- schema:
  - `type`: text
  - `items`:
    - `value`: float (eV)

### N0_vs_x.csv
- path: `/app/outputs/N0_vs_x.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: N(0) values for three Sr contents; threshold_or_better checks monotonic increase and per-point tolerances.
- schema:
  - `type`: table
  - `required_columns`: `x`, `N0`
  - `items`:
    - `x`: float
    - `N0`: float (states/eV/atom/spin)

### lambda_vs_x.csv
- path: `/app/outputs/lambda_vs_x.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Electron-phonon coupling λ for three Sr contents; threshold_or_better checks monotonic increase and per-point tolerances.
- schema:
  - `type`: table
  - `required_columns`: `x`, `lambda`
  - `items`:
    - `x`: float
    - `lambda`: float

### Tc_at_x045.txt
- path: `/app/outputs/Tc_at_x045.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Superconducting critical temperature at x=0.45 for two Coulomb pseudopotentials.
- schema:
  - `type`: text
  - `items`:
    - `value1`: float (K, μ*=0.1)
    - `value2`: float (K, μ*=0)

Notes: All artifacts are compared to hidden paper gold values within appropriate tolerances: band gap and Tc against fixed reference numbers; N(0) and λ using threshold_or_better that enforces monotonic increase across x and per-point tolerances. The process steps (structural optimization, phonon/linewidth calculation) are required because the load-bearing scored steps (λ and Tc) depend on them.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_pristine_RbH.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "items": {
          "value": "float (eV)"
        }
      },
      "description": "Direct band gap of pristine RbH at L-point."
    },
    {
      "file": "N0_vs_x.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "N0"
        ],
        "items": {
          "x": "float",
          "N0": "float (states/eV/atom/spin)"
        }
      },
      "description": "N(0) values for three Sr contents; threshold_or_better checks monotonic increase and per-point tolerances."
    },
    {
      "file": "lambda_vs_x.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "lambda"
        ],
        "items": {
          "x": "float",
          "lambda": "float"
        }
      },
      "description": "Electron-phonon coupling λ for three Sr contents; threshold_or_better checks monotonic increase and per-point tolerances."
    },
    {
      "file": "Tc_at_x045.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "items": {
          "value1": "float (K, μ*=0.1)",
          "value2": "float (K, μ*=0)"
        }
      },
      "description": "Superconducting critical temperature at x=0.45 for two Coulomb pseudopotentials."
    }
  ],
  "notes": "All artifacts are compared to hidden paper gold values within appropriate tolerances: band gap and Tc against fixed reference numbers; N(0) and λ using threshold_or_better that enforces monotonic increase across x and per-point tolerances. The process steps (structural optimization, phonon/linewidth calculation) are required because the load-bearing scored steps (λ and Tc) depend on them."
}
```

## How you are scored
Your submission is scored by a hidden verifier that compares your computed results to reference criteria. Each scored artifact (band gap, N(0), λ, Tc) is evaluated separately using tolerances appropriate for first‑principles recomputations. Some checks also assess the internal consistency and the expected physical relationships among the quantities. The final reward is a weighted combination of the per‑artifact scores. Simply reporting a value without genuine execution of the computational workflow will not receive full credit, because the verifier examines multiple independent results whose mutual agreement cannot be guessed.
