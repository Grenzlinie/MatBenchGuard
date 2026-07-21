# NJL Model Phase Diagrams under Chromomagnetic Field

## Problem background
The two-flavor, three-color Nambu–Jona-Lasinio (NJL) model with scalar quark-antiquark and scalar diquark interactions is studied in the presence of a homogeneous chromomagnetic background field that mimics the QCD gluon condensate, along with finite baryon chemical potential and temperature. The objective is to determine how the external chromomagnetic field influences the competition between chiral symmetry breaking (characterised by a non-zero quark condensate σ) and colour superconductivity (CSC, characterised by a non-zero diquark condensate Δ). The key quantities to compute are the phase boundaries in the (μ, gH, T) parameter space where the ground state transitions from a phase with only chiral symmetry breaking to the CSC phase, and the behaviour of the diquark condensate Δ as a function of the field strength gH at given chemical potentials and temperatures.

## Approach
The system is described by a regularized thermodynamic potential V_r(σ, Δ) that incorporates the effects of the chromomagnetic field through Landau-level sums and includes smooth momentum-dependent form factors to regulate UV divergences. The coupling constants G₁ (chiral channel) and G₂ (diquark channel) are taken to satisfy G₂ = 3/8 G₁. A three-momentum cutoff Λ is introduced via the form factors; three values Λ = 0.6, 0.8, 1.0 GeV are considered separately. For each Λ the coupling G₁ is calibrated by requiring that at zero temperature, chemical potential, and chromomagnetic field the global minimum of the potential occurs at σ = 0.4 GeV and Δ = 0, which fixes the absolute scale of the interactions. Once calibrated, the global minimum of V_r is found on a grid of (μ, gH, T) by scanning the order parameters σ ≥ 0 and Δ ≥ 0. From these minima the phase of the system (symmetric, chirally broken, or colour-superconducting) is identified at each grid point, allowing the extraction of the critical chemical potential μ_crit(gH) that separates the chirally broken and CSC phases, as well as the value of the diquark condensate Δ(gH) at fixed μ, T, Λ.

## Reproduction target
From the numerical minimization of the thermodynamic potential, produce the following data files:

1. **Phase boundary at T = 0** (`phase_boundary_T0.csv`): For each cutoff Λ = 0.6, 0.8, 1.0 GeV, report the critical chemical potential μ_crit as a function of the chromomagnetic field strength gH where the transition from the chirally broken phase (σ ≠ 0, Δ = 0) to the colour-superconducting phase (σ = 0, Δ ≠ 0) occurs. Columns: Lambda (GeV), gH (GeV²), mu_crit (GeV).
2. **Phase boundary at T = 0.15 GeV** (`phase_boundary_T0.15.csv`): Same as above, but for a fixed temperature T = 0.15 GeV.
3. **Diquark condensate curves at μ = 0.4 GeV** (`diquark_condensate_mu0.4_Lambda0.8.csv`): For cutoff Λ = 0.8 GeV and chemical potential μ = 0.4 GeV, give the diquark condensate Δ as a function of gH at three temperatures: T = 0, 0.1, 0.15 GeV. Columns: gH (GeV²), Delta_T0 (GeV), Delta_T0.1 (GeV), Delta_T0.15 (GeV).
4. **Diquark condensate curves at μ = 0.8 GeV** (`diquark_condensate_mu0.8.csv`): For chemical potential μ = 0.8 GeV, give Δ versus gH for two cutoffs (0.8 and 1.0 GeV) and two temperatures (0 and 0.15 GeV). Columns: gH (GeV²), Delta_T0_Lambda0.8 (GeV), Delta_T0_Lambda1.0 (GeV), Delta_T0.15_Lambda0.8 (GeV), Delta_T0.15_Lambda1.0 (GeV).

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Calibrate coupling constants
- Role: process
- Action: Implement the regularized thermodynamic potential V_r(σ,Δ) with form factors (20) for N_f=2, N_c=3. For each cutoff Λ = 0.6, 0.8, 1.0 GeV, determine G1 such that the global minimum of V_r at T=μ=H=0 gives σ=0.4 GeV and Δ=0, using G2 = 3/8 G1. Save the calibrated constants.
- Evidence: `/app/outputs/calibration_results.json`

### Step 2: Run parameter grid minimization
- Role: process
- Action: For each cutoff Λ and for all required (μ, gH, T) combinations spanning the phase transition regions, globally minimize V_r with respect to σ and Δ. Record the optimal (σ, Δ) and the potential value at each grid point. Save the raw grid data for downstream extraction.
- Evidence: `/app/outputs/raw_grid_data.npz`

### Step 3: Extract phase boundary at T=0
- Role: scored (load-bearing)
- Action: From the raw grid data for T=0, identify the critical chemical potential μ_crit as a function of gH where the global minimum transitions from the chiral‑broken phase (σ≠0, Δ=0) to the CSC phase (σ=0, Δ≠0). For each cutoff Λ, output the boundary as a CSV.
- Output file: `/app/outputs/phase_boundary_T0.csv`
- Format: csv
- Contract: Lambda (GeV), gH (GeV^2), mu_crit (GeV)
- Scoring: scored by hidden verifier

### Step 4: Extract phase boundary at T=0.15 GeV
- Role: scored (load-bearing)
- Action: From the raw grid data for T=0.15 GeV, determine μ_crit vs gH for each cutoff Λ and output the boundary as a CSV.
- Output file: `/app/outputs/phase_boundary_T0.15.csv`
- Format: csv
- Contract: Lambda (GeV), gH (GeV^2), mu_crit (GeV)
- Scoring: scored by hidden verifier

### Step 5: Extract diquark condensate curves for μ=0.4 GeV, Λ=0.8 GeV
- Role: scored (load-bearing)
- Action: From the raw grid data at μ=0.4 GeV, Λ=0.8 GeV, extract the diquark condensate Δ as a function of gH for T = 0, 0.1, and 0.15 GeV. Output a CSV with one column per temperature.
- Output file: `/app/outputs/diquark_condensate_mu0.4_Lambda0.8.csv`
- Format: csv
- Contract: gH (GeV^2), Delta_T0 (GeV), Delta_T0.1 (GeV), Delta_T0.15 (GeV)
- Scoring: scored by hidden verifier

### Step 6: Extract diquark condensate curves for μ=0.8 GeV
- Role: scored (load-bearing)
- Action: From the raw grid data at μ=0.8 GeV, extract Δ vs gH for (Λ=0.8, T=0), (Λ=1.0, T=0), (Λ=0.8, T=0.15) and (Λ=1.0, T=0.15). Output a single CSV with all four curves.
- Output file: `/app/outputs/diquark_condensate_mu0.8.csv`
- Format: csv
- Contract: gH (GeV^2), Delta_T0_Lambda0.8 (GeV), Delta_T0_Lambda1.0 (GeV), Delta_T0.15_Lambda0.8 (GeV), Delta_T0.15_Lambda1.0 (GeV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundary_T0.csv`
- `/app/outputs/phase_boundary_T0.15.csv`
- `/app/outputs/diquark_condensate_mu0.4_Lambda0.8.csv`
- `/app/outputs/diquark_condensate_mu0.8.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundary_T0.csv
- path: `/app/outputs/phase_boundary_T0.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase boundary between chiral‑broken (II) and CSC (III) phases at T=0. Each row is a point on the μ_crit(gH) curve for a given cutoff Λ.
- schema:
  - `type`: table
  - `required_columns`: `Lambda`, `gH`, `mu_crit`
  - `units`:
    - `Lambda`: GeV
    - `gH`: GeV^2
    - `mu_crit`: GeV

### phase_boundary_T0.15.csv
- path: `/app/outputs/phase_boundary_T0.15.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase boundary between chiral‑broken (II) and CSC (III) phases at T=0.15 GeV.
- schema:
  - `type`: table
  - `required_columns`: `Lambda`, `gH`, `mu_crit`
  - `units`:
    - `Lambda`: GeV
    - `gH`: GeV^2
    - `mu_crit`: GeV

### diquark_condensate_mu0.4_Lambda0.8.csv
- path: `/app/outputs/diquark_condensate_mu0.4_Lambda0.8.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Diquark condensate Δ vs chromomagnetic field strength gH for μ=0.4 GeV, Λ=0.8 GeV, at three temperatures.
- schema:
  - `type`: table
  - `required_columns`: `gH`, `Delta_T0`, `Delta_T0.1`, `Delta_T0.15`
  - `units`:
    - `gH`: GeV^2
    - `Delta_T0`: GeV
    - `Delta_T0.1`: GeV
    - `Delta_T0.15`: GeV

### diquark_condensate_mu0.8.csv
- path: `/app/outputs/diquark_condensate_mu0.8.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Diquark condensate Δ vs gH for μ=0.8 GeV, at two cutoffs (0.8 and 1.0 GeV) and two temperatures (0 and 0.15 GeV).
- schema:
  - `type`: table
  - `required_columns`: `gH`, `Delta_T0_Lambda0.8`, `Delta_T0_Lambda1.0`, `Delta_T0.15_Lambda0.8`, `Delta_T0.15_Lambda1.0`
  - `units`:
    - `gH`: GeV^2
    - `Delta_T0_Lambda0.8`: GeV
    - `Delta_T0_Lambda1.0`: GeV
    - `Delta_T0.15_Lambda0.8`: GeV
    - `Delta_T0.15_Lambda1.0`: GeV

Notes: The checker compares each CSV row to hidden reference values digitised from the paper's phase diagrams and diquark‑condensate figures, using tolerances of 5 % for μ_crit and 10 % for Δ. It also verifies the monotonically increasing trend of μ_crit with gH and the vanishing of Δ at large gH when T>0. The agent must provide at least 5 points per boundary/curve to allow meaningful comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundary_T0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Lambda",
          "gH",
          "mu_crit"
        ],
        "units": {
          "Lambda": "GeV",
          "gH": "GeV^2",
          "mu_crit": "GeV"
        }
      },
      "description": "Phase boundary between chiral‑broken (II) and CSC (III) phases at T=0. Each row is a point on the μ_crit(gH) curve for a given cutoff Λ."
    },
    {
      "file": "phase_boundary_T0.15.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Lambda",
          "gH",
          "mu_crit"
        ],
        "units": {
          "Lambda": "GeV",
          "gH": "GeV^2",
          "mu_crit": "GeV"
        }
      },
      "description": "Phase boundary between chiral‑broken (II) and CSC (III) phases at T=0.15 GeV."
    },
    {
      "file": "diquark_condensate_mu0.4_Lambda0.8.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gH",
          "Delta_T0",
          "Delta_T0.1",
          "Delta_T0.15"
        ],
        "units": {
          "gH": "GeV^2",
          "Delta_T0": "GeV",
          "Delta_T0.1": "GeV",
          "Delta_T0.15": "GeV"
        }
      },
      "description": "Diquark condensate Δ vs chromomagnetic field strength gH for μ=0.4 GeV, Λ=0.8 GeV, at three temperatures."
    },
    {
      "file": "diquark_condensate_mu0.8.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gH",
          "Delta_T0_Lambda0.8",
          "Delta_T0_Lambda1.0",
          "Delta_T0.15_Lambda0.8",
          "Delta_T0.15_Lambda1.0"
        ],
        "units": {
          "gH": "GeV^2",
          "Delta_T0_Lambda0.8": "GeV",
          "Delta_T0_Lambda1.0": "GeV",
          "Delta_T0.15_Lambda0.8": "GeV",
          "Delta_T0.15_Lambda1.0": "GeV"
        }
      },
      "description": "Diquark condensate Δ vs gH for μ=0.8 GeV, at two cutoffs (0.8 and 1.0 GeV) and two temperatures (0 and 0.15 GeV)."
    }
  ],
  "notes": "The checker compares each CSV row to hidden reference values digitised from the paper's phase diagrams and diquark‑condensate figures, using tolerances of 5 % for μ_crit and 10 % for Δ. It also verifies the monotonically increasing trend of μ_crit with gH and the vanishing of Δ at large gH when T>0. The agent must provide at least 5 points per boundary/curve to allow meaningful comparison."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. For each of the four required CSV files, the verifier compares your output to reference data (digitized from the published curves) and checks that the numerical values fall within an acceptable tolerance range. In addition, the verifier tests expected physical trends: for the phase boundaries, the critical chemical potential μ_crit should increase monotonically with the field strength gH; for the diquark condensate curves at finite temperature, Δ must vanish at sufficiently large gH. The four scored artifacts contribute weight to the overall reward; simply reporting the expected qualitative behaviour without correctly computed data will not earn full credit. No hidden parameter values or tolerances are disclosed.
