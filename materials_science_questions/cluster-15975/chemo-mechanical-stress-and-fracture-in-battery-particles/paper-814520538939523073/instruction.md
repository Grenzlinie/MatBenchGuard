# Chemo-Mechanical Stress and Fracture in Battery Particles

## Problem background
Silicon (Si) is a promising anode material for lithium-ion batteries, but the large volume expansion (~300%) during lithiation causes mechanical stress and brittle fracture, limiting its practical application. Understanding the coupled diffusion-deformation-fracture behavior is essential for designing durable electrodes. This task reproduces a variational framework that integrates large elasto-plastic deformation with phase-field brittle fracture to model the two-phase lithiation of Si. The framework captures anisotropic deformation arising from different crystallographic directions and predicts crack initiation under chemo-mechanical loading.

## Approach
The coupled chemo-mechanical problem is formulated as a three-field variational problem with primary unknowns: the deformation field, the chemical potential, and the damage phase-field. A staggered finite element solution scheme is used, decoupling the damage update from the deformation-diffusion problem. The constitutive model combines large-deformation elasto-plasticity with perfect von Mises plasticity, a tension-compression split so that only tensile driving forces promote damage, and a regular-solution chemical free energy. The two-phase lithiation is described by a reaction-controlled diffusion model: the sharp phase boundary between unlithiated Si and lithiated Li_xSi is advanced by a reaction rate that depends on local hydrostatic pressure, lithium concentration, and anisotropic bond-breaking energy barriers (distinct for ⟨100⟩ and ⟨110⟩ crystallographic directions). A history-field algorithm enforces crack irreversibility. The agent must implement this framework from scratch (e.g., using an open-source finite element library), calibrate the concentration-dependent diffusion coefficient, and execute the required simulations.

## Reproduction target
Simulate two-phase lithiation of a quarter-symmetric ⟨100⟩ crystalline silicon nanopillar (radius 300 nm) under plane strain. Use the anisotropic reaction-controlled diffusion model and the calibrated concentration-dependent diffusion coefficient. Perform two simulations:
- **Without damage (d = 0):** Extract the hoop stress at outer-surface points A (θ = 0°) and B (θ = 45°) at times t = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 seconds and save the results to `hoop_stress_evolution.csv` with columns: `time` (s), `hoop_stress_A` (GPa), `hoop_stress_B` (GPa).
- **With phase-field fracture (fracture energy release rate 12.5 J/m², length scale 8 nm):** At states of charge SOC = 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, compute the crack surface functional Γ = ∫ γ(d,∇d) dV and save the results to `crack_length_vs_soc.csv` with columns: `soc` (dimensionless), `crack_length` (dimensionless).

## Assets

- Python scientific computing stack: numpy scipy matplotlib
- Finite element library: https://fenicsproject.org/

## Workflow steps

### Step 1: Implement the variational chemo-mechanical FE framework
- Role: process
- Action: Implement the three-field (deformation φ, chemical potential μ, damage phase-field d) variational finite element solver as described: staggered solution scheme, multiplicative decomposition of the deformation gradient, large-deformation elasto-plasticity with perfect von Mises plasticity, tension‑compression split for phase‑field fracture, regular‑solution chemical free energy, reaction‑controlled two‑phase diffusion model with anisotropic bond‑breaking barriers (E0<110>=0.60 eV, E0<100>=0.66 eV), history‑field‑driven damage update, and geometric reaction front tracking algorithm.
- Evidence: `/app/outputs/solver_code_and_log.txt`

### Step 2: Prepare simulation inputs
- Role: process
- Action: Generate a quarter‑symmetric mesh (plane strain, ~11638 Q1 elements) for an ⟨100⟩ c-Si nanopillar with radius 300 nm. Collect all material parameters from the paper (Young's modulus, Poisson's ratio, yield stress, fracture energy release rate, expansion coefficient, gas constant, etc.). Set initial chemical potential μ₀ = –11.5 J/mol, outer boundary potential ramp to 11.5 J/mol within the first second, and define the linearly concentration‑dependent diffusion coefficient D(c) profile to be determined in the calibration step.
- Evidence: none

### Step 3: Calibrate the concentration-dependent diffusion coefficient
- Role: process
- Action: Run trial two‑phase lithiation simulations without damage for several concentration‑dependent diffusion coefficient profiles (constant and linearly increasing with concentration). Select the profile (e.g., D(c) = 1 × 10⁻¹² → 15 × 10⁻¹² cm²/s, linearly increasing with c from 0 to 1) that yields a sharp concentration gradient at the reaction front consistent with experimental observations. Document the chosen profile and the resulting concentration curves along the radius.
- Evidence: `/app/outputs/calibration_report.txt`

### Step 4: Lithiation without damage — hoop stress evolution
- Role: scored
- Action: Using the calibrated D(c) and the anisotropic two‑phase model, run the coupled diffusion–deformation simulation with damage disabled (d = 0). Extract the hoop stress at the outer‑surface points A (θ = 0°) and B (θ = 45°) at times t = 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 s and write the results to hoop_stress_evolution.csv.
- Output file: `/app/outputs/hoop_stress_evolution.csv`
- Format: csv
- Contract: time (s), hoop_stress_A (GPa), hoop_stress_B (GPa). Rows for t=2,4,6,8,10,12,14,16,18,20 s.
- Scoring: scored by hidden verifier

### Step 5: Lithiation with phase‑field fracture — crack length vs SOC
- Role: scored (load-bearing)
- Action: Run the full coupled simulation including phase‑field fracture (g_c = 12.5 J/m², length scale l = 8 nm) for the anisotropic two‑phase ⟨100⟩ c-Si nanopillar. At states of charge (SOC) = 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, compute the crack surface functional Γ = ∫ γ(d,∇d) dV and write the results to crack_length_vs_soc.csv.
- Output file: `/app/outputs/crack_length_vs_soc.csv`
- Format: csv
- Contract: soc (dimensionless), crack_length (dimensionless). Rows for soc=0.05,0.10,0.15,0.20,0.25,0.30,0.35.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hoop_stress_evolution.csv`
- `/app/outputs/crack_length_vs_soc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hoop_stress_evolution.csv
- path: `/app/outputs/hoop_stress_evolution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time series of hoop stresses at outer-surface points A (θ=0°) and B (θ=45°) of a ⟨100⟩ c-Si nanopillar during two-phase lithiation without damage.
- schema:
  - `type`: table
  - `required_columns`: `time`, `hoop_stress_A`, `hoop_stress_B`
  - `units`:
    - `time`: s
    - `hoop_stress_A`: GPa
    - `hoop_stress_B`: GPa

### crack_length_vs_soc.csv
- path: `/app/outputs/crack_length_vs_soc.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Crack length (Γ) as a function of state of charge for the same nanopillar with phase-field fracture (g_c=12.5 J/m²).
- schema:
  - `type`: table
  - `required_columns`: `soc`, `crack_length`
  - `units`:
    - `soc`: dimensionless
    - `crack_length`: dimensionless

Notes: The checker will compare the reported hoop stress values at the listed times against reference data, with tolerances, and compute the mean absolute percentage error (MAPE) for the crack length curve. The check also verifies that hoop stress transitions from compressive to tensile before 8 s and that crack length increases monotonically with SOC and first becomes non-zero between SOC 0.12 and 0.28.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hoop_stress_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "hoop_stress_A",
          "hoop_stress_B"
        ],
        "units": {
          "time": "s",
          "hoop_stress_A": "GPa",
          "hoop_stress_B": "GPa"
        }
      },
      "description": "Time series of hoop stresses at outer-surface points A (θ=0°) and B (θ=45°) of a ⟨100⟩ c-Si nanopillar during two-phase lithiation without damage."
    },
    {
      "file": "crack_length_vs_soc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "soc",
          "crack_length"
        ],
        "units": {
          "soc": "dimensionless",
          "crack_length": "dimensionless"
        }
      },
      "description": "Crack length (Γ) as a function of state of charge for the same nanopillar with phase-field fracture (g_c=12.5 J/m²)."
    }
  ],
  "notes": "The checker will compare the reported hoop stress values at the listed times against reference data, with tolerances, and compute the mean absolute percentage error (MAPE) for the crack length curve. The check also verifies that hoop stress transitions from compressive to tensile before 8 s and that crack length increases monotonically with SOC and first becomes non-zero between SOC 0.12 and 0.28."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. The checker compares your submitted CSVs against reference data using appropriate error metrics (e.g., pointwise deviation for hoop stress, monotonicity and crack initiation SOC range for the crack length curve) and combines the stage scores into a weighted overall reward. Simply reporting plausible numbers is not sufficient; the checker expects correctly formatted artifacts that reflect a faithful re-implementation of the described framework.
