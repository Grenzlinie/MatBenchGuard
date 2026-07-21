# Sequential Monte Carlo Simulation of Contact Formation Topography

## Problem background
In advanced semiconductor manufacturing, tungsten (W) plugs that connect transistor electrodes to the first metal layer are formed through a chain of vacuum processes: reactive ion etching (RIE) of the SiO₂ insulator creates a high‑aspect‑ratio contact hole, a TiN barrier/liner is deposited by sputtering, and finally the hole is filled with tungsten by chemical vapor deposition (CVD). As design rules shrink, the aspect ratio of the contact hole increases dramatically, and predicting the end‑to‑end topography becomes critical. In particular, if the sidewall coverage is insufficient, the deposited tungsten may disconnect, creating an electrical open and a sharp increase in contact resistance. Simulating the sequential topography evolution — etching, barrier deposition, and filling — is essential to identify the film thicknesses at which disconnection becomes likely.

## Approach
The approach uses three sequential Monte Carlo particle‑based simulations, one for each process, that feed their output into the next.

- **RIE simulation:** A plasma/sheath model computes the fluxes and energies of the dominant etchants (CF₂, O, C₄F₆⁺) from the baseline process conditions (capacitively coupled discharge at 13.56 MHz, 1500 W, C₅F₈/O₂/CO/Ar mixture). An ion‑enhanced surface reaction model then evolves the etched hole profile through a cycle of polymer deposition, polymer removal by O radicals, and ion‑induced etching of SiO₂. The same model also accounts for photoresist erosion.
- **TiN sputtering simulation:** Using the etched profile as input, TiN particles are emitted from a target with a Maxwellian energy distribution (average 10 eV) and cosine angular distribution, transported through Ar background gas with hard‑sphere collisions, and deposited with a sticking coefficient of 0.93. The deposition rate is calibrated so that the TiN thickness on the wafer surface matches 10 nm, consistent with the long‑throw sputtering geometry.
- **W‑CVD simulation:** With the resulting TiN coverage map, a simple sticking‑coefficient Monte Carlo model fills the contact hole. Sticking coefficients differ radically between surfaces: that for W on TiN/W is of order 10⁻³, while that for W on SiO₂ is ~10⁻⁸. The simulation proceeds until the hole top closes, producing a final W‑filled profile.

After the three simulations, the tungsten connection ratio Rc is computed from the filling profile as the percentage of vertical meshes filled with W from the top of the hole to the bottom. The procedure is repeated for three SiO₂ film thicknesses (2.0, 2.5, and 3.0 µm) with a fixed mask pattern (0.13 µm hole diameter, 89° taper, 300 nm photoresist).

## Reproduction target
Run the full sequential Monte Carlo pipeline for SiO₂ film thicknesses of 2.0 µm, 2.5 µm, and 3.0 µm under the baseline process conditions described above. For each thickness, compute the connection ratio Rc (percentage of vertical meshes filled with W from top to bottom) and determine whether disconnection has occurred (disconnection = true when Rc < 100%). Write the results to /app/outputs/connection_ratios.csv with columns thickness_um, rc_percent, disconnection.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: RIE Plasma Simulation
- Role: process
- Action: Save the following precomputed plasma fluxes to /app/outputs/rie_plasma_fluxes.json: CF₂ flux = 2.0×10¹⁵ cm⁻² s⁻¹, O flux = 5.0×10¹⁴ cm⁻² s⁻¹, C₄F₆⁺ flux = 1.5×10¹⁵ cm⁻² s⁻¹, ion energy = 300 eV.
- Evidence: `/app/outputs/rie_plasma_fluxes.json`

### Step 2: RIE Surface Monte Carlo Simulation
- Role: process
- Action: Using the plasma fluxes and the ion‑enhanced etching model with the following calibrated parameters: α₁ = 0.04 nm·s per 10¹⁵ cm⁻² s⁻¹, α₂ = 0.02 nm·s per 10¹⁵ cm⁻² s⁻¹, etching yield = 0.3, A = 0.025 nm⁻¹, simulate the SiO₂ etching profile evolution for the predefined mask pattern (0.13 µm hole, 89° taper, 300 nm photoresist on SiO₂ films of thickness 2.0, 2.5, 3.0 µm).
- Evidence: `/app/outputs/etched_profiles.npy`

### Step 3: TiN Sputtering Simulation
- Role: process
- Action: With the etched profiles as input, simulate long‑throw TiN sputtering deposition using a Monte Carlo particle model: emit TiN from the target with a Maxwellian energy distribution (E₀=10 eV) and cosine angular distribution, transport through Ar gas with collisions, and deposit with a sticking coefficient of 0.93. Calibrate the deposition rate to match the baseline 10 nm thickness on the wafer surface.
- Evidence: `/app/outputs/tin_coverage.npy`

### Step 4: W‑CVD Monte Carlo Simulation
- Role: process
- Action: Using the TiN coverage, simulate tungsten CVD filling with the simple sticking‑coefficient Monte Carlo model: sticking coefficients α_W_TiN/W = 2.5×10⁻³, α_W_SiO₂ = 10⁻⁸, Knudsen number 28.5, deposition rate calibrated to the baseline process. Simulate for each SiO₂ thickness until the hole top closes.
- Evidence: `/app/outputs/w_filling_profile.npy`

### Step 5: Connection Ratio Analysis
- Role: scored (load-bearing)
- Action: From the W filling profiles, compute the connection ratio Rc (percentage of vertical meshes filled with W from top to bottom) for each SiO₂ thickness. Save the results to connection_ratios.csv.
- Output file: `/app/outputs/connection_ratios.csv`
- Format: csv
- Contract: Header: thickness_um, rc_percent, disconnection. Three rows for 2.0, 2.5, 3.0 µm. thickness_um: float; rc_percent: float; disconnection: boolean (true if rc_percent < 100.0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/connection_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### connection_ratios.csv
- path: `/app/outputs/connection_ratios.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed connection ratio and disconnection status for SiO₂ film thicknesses 2.0, 2.5, 3.0 µm. The disconnection flag is true when rc_percent < 100%.
- schema:
  - `type`: table
  - `required_columns`: `thickness_um`, `rc_percent`, `disconnection`
  - `units`:
    - `thickness_um`: um
    - `rc_percent`: %

Notes: The checker will evaluate whether the connection ratio exceeds 95% for 2.0 µm, falls below 95% for 2.5 and 3.0 µm, decreases monotonically, and that disconnection is true only for thickness ≥2.5 µm. These are structural constraints that verify the paper's disconnection claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "connection_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_um",
          "rc_percent",
          "disconnection"
        ],
        "units": {
          "thickness_um": "um",
          "rc_percent": "%"
        }
      },
      "description": "Computed connection ratio and disconnection status for SiO₂ film thicknesses 2.0, 2.5, 3.0 µm. The disconnection flag is true when rc_percent < 100%."
    }
  ],
  "notes": "The checker will evaluate whether the connection ratio exceeds 95% for 2.0 µm, falls below 95% for 2.5 and 3.0 µm, decreases monotonically, and that disconnection is true only for thickness ≥2.5 µm. These are structural constraints that verify the paper's disconnection claim."
}
```

## How you are scored
A hidden verifier reads your connection_ratios.csv and compares each row’s rc_percent and disconnection flag against reference criteria derived from the structural behavior of the simulated system. The evaluation checks that the connection ratio and disconnection status follow the expected trend with increasing SiO₂ thickness, including monotonicity and threshold crossing, without requiring an exact match to any specific number. The final reward is a weighted combination of these per‑thickness checks; producing results that are structurally consistent with the physics of the process yields high reward.
