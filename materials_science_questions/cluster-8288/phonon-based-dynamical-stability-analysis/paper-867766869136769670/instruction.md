# Electron-phonon limited transport in a 2D sodium monolayer

## Problem background
Two-dimensional (2D) materials often exhibit electronic and thermal properties that differ markedly from their bulk forms. A free-standing hexagonal monolayer of sodium (2D Na) has been proposed as a mechanically stable system that behaves like a two-dimensional electron gas (2DEG). Understanding its intrinsic electron-phonon (e-ph) limited electrical resistivity and thermal transport is essential for potential electronic and thermopower applications. Key open questions include the temperature dependence of the resistivity, the power-law regimes, the Bloch-Grüneisen temperature, and the validity of the Wiedemann-Franz law in this 2D metallic sheet. This task investigates those transport properties for the undoped case by computing the relevant quantities from first principles.

## Approach
The workflow uses density-functional theory (DFT) and density-functional perturbation theory (DFPT) to obtain the electronic structure and vibrational properties of 2D Na. Electron-phonon coupling matrix elements are computed on a coarse grid in reciprocal space and then Wannier-interpolated to a fine grid using the EPW code to achieve convergence. The linearized Boltzmann transport equation (BTE) is solved (Allen's model or an exact iterative solution) to yield the temperature-dependent electrical resistivity and electronic thermal conductivity for undoped 2D Na (no Fermi energy shift). From the resistivity curve, low- and high-temperature power-law fits are performed to extract the Bloch-Grüneisen temperature and the associated coefficients. The Lorenz number is then calculated from the electronic transport coefficients at 300 K.

## Reproduction target
Compute the temperature-dependent electrical resistivity for undoped 2D Na (no Fermi energy shift). From the output, extract the coefficients A and B that describe the power-law dependence in the low- and high-temperature regimes (ρ/ρ_{300K} ≈ A·T⁴ and ≈ B·T), determine the Bloch-Grüneisen temperature Θ_BG as the intersection of the two regimes, and report the Lorenz number L = κ_e/(σ·T) at 300 K. The results must be written to three distinct scored artifacts: a CSV file containing temperature and resistivity data, a JSON file with the fitted parameters, and a text file with the Lorenz number.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- EPW (electron-phonon Wannier): https://epw-code.org/
- Norm-conserving pseudopotential for Na: https://www.pseudo-dojo.org/

## Workflow steps

### Step 1: Geometry optimization of 2D Na
- Role: process
- Action: Optimize the hexagonal unit cell of free-standing 2D Na (one Na atom, lattice constant ~3.66 Å, ~10 Å vacuum) using DFT with a norm-conserving pseudopotential in Quantum ESPRESSO.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Self-consistent DFT calculation
- Role: process
- Action: Perform a self-consistent DFT calculation on the optimized structure to obtain ground-state electron density, Kohn-Sham wavefunctions, and band structure, using an appropriate k-point grid (e.g., 8×8×1).
- Evidence: `/app/outputs/scf.log`

### Step 3: DFPT phonons and e-ph matrix elements
- Role: process
- Action: Run density-functional perturbation theory (DFPT) to compute phonon frequencies and electron-phonon coupling matrix elements on a coarse 8×8×1 q‑point grid using Quantum ESPRESSO.
- Evidence: `/app/outputs/dfpt_eph.log`

### Step 4: Wannier interpolation to fine grid
- Role: process
- Action: Use EPW to Wannier-interpolate the coarse electron-phonon matrix elements to a fine 200×200×1 grid, producing converged e-ph coupling data.
- Evidence: `/app/outputs/epw_interp.log`

### Step 5: Boltzmann transport solution
- Role: process
- Action: Solve the Boltzmann transport equation (Allen's model or exact iterative solution) using the interpolated e-ph matrix elements to compute temperature-dependent electrical resistivity and electronic thermal conductivity for undoped 2D Na (no Fermi energy shift). Write the raw numerical arrays (temperatures, resistivity, thermal conductivity) to an intermediate file for later extraction.
- Evidence: `/app/outputs/bte_output.npz`

### Step 6: Resistivity data (structural sanity check)
- Role: scored
- Action: Extract the temperature-dependent resistivity from the BTE results and write a CSV file with columns T_K (temperature in K), rho_abs_microOhm_cm (absolute resistivity in µΩ·cm), and rho_normalized (resistivity divided by its value at 300 K). At least 10 temperature points are expected.
- Output file: `/app/outputs/resistivity_temperature.csv`
- Format: csv
- Contract: T_K (float), rho_abs_microOhm_cm (float), rho_normalized (float)
- Scoring: scored by hidden verifier

### Step 7: Fitted Bloch–Grüneisen parameters
- Role: scored (load-bearing)
- Action: Fit the normalized resistivity versus temperature data (low-T regime) to A·T⁴ and the high-T regime to B·T. Determine the Bloch–Grüneisen temperature Θ_BG as the intersection of the fitted lines. Output a JSON object with keys A_K_minus4 (in K⁻⁴), B_K_minus1 (in K⁻¹), and Theta_BG_K (in K).
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: A_K_minus4 (float), B_K_minus1 (float), Theta_BG_K (float)
- Scoring: scored by hidden verifier

### Step 8: Lorenz number at 300 K
- Role: scored (load-bearing)
- Action: From the electronic thermal conductivity κ_e and electrical conductivity σ obtained from the BTE solution, compute the Lorenz number L = κ_e / (σ·T) at T = 300 K. Write the result in V²/K² to a text file.
- Output file: `/app/outputs/lorenz_number_300K.txt`
- Format: txt
- Contract: a single float number
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/resistivity_temperature.csv`
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/lorenz_number_300K.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### resistivity_temperature.csv
- path: `/app/outputs/resistivity_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature-dependent resistivity data for structural sanity check. The primary scoring is on the fitted parameters and Lorenz number.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `rho_abs_microOhm_cm`, `rho_normalized`
  - `units`:
    - `T_K`: K
    - `rho_abs_microOhm_cm`: µΩ·cm
    - `rho_normalized`: dimensionless

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted low‑T (T⁴) and high‑T (T) power-law coefficients and the Bloch–Grüneisen temperature Θ_BG. These quantities can only be obtained by genuinely running the DFT/DFPT/EPW/BTE pipeline, making this step load‑bearing.
- schema:
  - `type`: object
  - `required`: `A_K_minus4`, `B_K_minus1`, `Theta_BG_K`
  - `properties`:
    - `A_K_minus4`:
      - `type`: number
      - `units`: K⁻⁴
    - `B_K_minus1`:
      - `type`: number
      - `units`: K⁻¹
    - `Theta_BG_K`:
      - `type`: number
      - `units`: K

### lorenz_number_300K.txt
- path: `/app/outputs/lorenz_number_300K.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Lorenz number at 300 K, computed from the BTE electronic thermal and electrical conductivities. Also load‑bearing because the required conductivities are outputs of the full pipeline.
- schema:
  - `type`: text
  - `content_type`: single float
  - `units`: V²/K²

Notes: The resistivity CSV is a low‑weight structural check. The primary scored artifacts are fitted_parameters.json and lorenz_number_300K.txt, which are scored by result‑level comparison (T0) against hidden paper‑reported gold with appropriate tolerances. The pipeline is forced by the load‑bearing scored steps, as these quantities cannot be guessed without genuinely executing the DFT–DFPT–EPW–BTE workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "resistivity_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "rho_abs_microOhm_cm",
          "rho_normalized"
        ],
        "units": {
          "T_K": "K",
          "rho_abs_microOhm_cm": "µΩ·cm",
          "rho_normalized": "dimensionless"
        }
      },
      "description": "Temperature-dependent resistivity data for structural sanity check. The primary scoring is on the fitted parameters and Lorenz number."
    },
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "A_K_minus4",
          "B_K_minus1",
          "Theta_BG_K"
        ],
        "properties": {
          "A_K_minus4": {
            "type": "number",
            "units": "K⁻⁴"
          },
          "B_K_minus1": {
            "type": "number",
            "units": "K⁻¹"
          },
          "Theta_BG_K": {
            "type": "number",
            "units": "K"
          }
        }
      },
      "description": "Fitted low‑T (T⁴) and high‑T (T) power-law coefficients and the Bloch–Grüneisen temperature Θ_BG. These quantities can only be obtained by genuinely running the DFT/DFPT/EPW/BTE pipeline, making this step load‑bearing."
    },
    {
      "file": "lorenz_number_300K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content_type": "single float",
        "units": "V²/K²"
      },
      "description": "Lorenz number at 300 K, computed from the BTE electronic thermal and electrical conductivities. Also load‑bearing because the required conductivities are outputs of the full pipeline."
    }
  ],
  "notes": "The resistivity CSV is a low‑weight structural check. The primary scored artifacts are fitted_parameters.json and lorenz_number_300K.txt, which are scored by result‑level comparison (T0) against hidden paper‑reported gold with appropriate tolerances. The pipeline is forced by the load‑bearing scored steps, as these quantities cannot be guessed without genuinely executing the DFT–DFPT–EPW–BTE workflow."
}
```

## How you are scored
A hidden verifier inspects each scored artifact. The resistivity CSV is checked for structural sanity (monotonic temperature trend, sufficient number of points). The fitted parameters in `fitted_parameters.json` and the Lorenz number in `lorenz_number_300K.txt` are compared against hidden reference values using appropriate tolerances. These two artifacts are load-bearing: their correct values cannot be guessed or derived without genuinely executing the full DFT–DFPT–EPW–BTE pipeline. The overall reward is a weighted combination of the artifact scores, with the highest weight placed on the fitted parameters and the Lorenz number. Simply reporting a number without completing the computational steps will yield a low or zero score.
