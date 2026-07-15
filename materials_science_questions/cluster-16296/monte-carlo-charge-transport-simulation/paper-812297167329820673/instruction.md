# Joint spectral density and Monte Carlo simulation of hot-electron quantum transport

## Problem background
Quantum transport theory in semiconductors must account for collisional broadening and intra‑collisional field effects to go beyond the semiclassical Boltzmann equation. The joint spectral density K(k,k') is the central quantity that encodes these quantum corrections in the scattering rates. This workflow evaluates analytical models for the joint spectral density under ICFE and collisional broadening, and uses ensemble Monte Carlo simulations to compute the resulting electron energy distributions and drift velocities for a model semiconductor, thereby providing quantitative insight into the role of collisional broadening in hot‑electron transport.

## Approach
The approach consists of two stages. First, we numerically evaluate the joint spectral density models. For free electrons with ICFE, the joint spectral density is computed from an integral involving Fresnel integrals; its positive‑definite Lorentzian approximation is also evaluated. For collisional broadening, the joint spectral density is computed using a dimensionless integral formula that accounts for an energy‑dependent broadening. All evaluations use the fixed parameters of a model semiconductor: effective mass m=0.3 m₀, optical phonon energy ω₀=0.04 eV, and broadening parameter γ²=1.1 meV. The ICFE computations are performed at electric fields E=2.5 and 10 kV/cm; the CB computations are performed for several initial kinetic energies.

Second, we construct an ensemble Monte Carlo simulation of electron transport for a single isotropic parabolic band with non‑polar optical phonon scattering at zero temperature (spontaneous emission only). Two scattering models are implemented: (a) a delta‑function preserving kinetic energy (golden‑rule, no collisional broadening) and (b) the collisional broadening joint spectral density. The simulation is run for 10⁴ electrons at a steady electric field of 500 kV/cm until a steady state is reached. The final kinetic energies of all electrons are recorded and the average drift velocity is computed. From the recorded energies, normalized energy distribution histograms are produced for the two conditions, allowing the influence of collisional broadening to be assessed.

## Reproduction target
The goal is to produce three scored artifacts:

1. `joint_spectral_density.csv` – values of K for the ICFE models (exact and Lorentzian) as functions of the energy mismatch P at the two electric fields, and for the CB model as a function of final energy at the three initial energies.
2. `monte_carlo_distribution.csv` – normalized histograms of kinetic energy for the Monte Carlo simulations without and with collisional broadening.
3. `drift_velocity.csv` – the steady‑state drift velocities (in cm/s) for the two conditions.

All outputs must conform to the column schemas given in the workflow steps. The quality of these outputs will be evaluated by a hidden verifier.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute joint spectral density (ICFE and CB)
- Role: scored
- Action: Compute the exact ICFE joint spectral density (using Fresnel integrals) and its positive‑definite Lorentzian approximation as functions of the energy mismatch P for electric fields E=2.5 kV/cm and E=10 kV/cm. Compute the collisional broadening (CB) joint spectral density using the dimensionless integral formula as a function of final kinetic energy for initial kinetic energies 0.05, 0.1, and 1.0 eV. Use m=0.3 m₀, ω₀=0.04 eV, γ²=1.1 meV. For ICFE calculations, use the maximum‑effect alignment: q parallel to E, with q = k_i + k_f, where k_i = √(2m ε)/ħ and k_f = √(2m (ε − ω₀))/ħ, in atomic units (ħ = 1, m₀ = 1). Convert E from kV/cm to atomic units (1 V/m = 5.14220652×10¹¹ a.u.; 1 kV/cm = 1e5 V/m) and energies from eV to atomic units (1 eV = 0.0367493 Hartree). Use η = −1 for emission. Output all values in a single CSV file with columns type, field_kVcm, initial_energy_eV, P_eV, final_energy_eV, K, model.
- Output file: `/app/outputs/joint_spectral_density.csv`
- Format: csv
- Contract: type(string), field_kVcm(float, blank for CB), initial_energy_eV(float, blank for ICFE), P_eV(float, for ICFE rows), final_energy_eV(float, for CB rows), K(float), model(string: exact, lorentzian, or CB)
- Scoring: scored by hidden verifier

### Step 2: Run ensemble Monte Carlo simulation
- Role: process
- Action: Implement an ensemble Monte Carlo simulation of electron transport for a single isotropic parabolic band (effective mass m=0.3 m₀) with non‑polar optical phonon scattering at zero temperature (spontaneous emission only, phonon energy ω₀=0.04 eV). Use two scattering models: (a) golden‑rule delta (no collisional broadening) and (b) collisional broadening described by the CB joint spectral density (γ²=1.1 meV). Simulate 10⁴ electrons at a steady electric field of 500 kV/cm until a steady state is reached. Record the final kinetic energies and the average drift velocity for each condition. Store the raw simulation results in an intermediate file for the downstream steps.
- Evidence: `/app/outputs/simulation_data.pkl`

### Step 3: Generate energy distribution functions
- Role: scored (load-bearing)
- Action: From the Monte Carlo simulation data, produce a normalized histogram of electron kinetic energies for the ‘without_CB’ and ‘with_CB’ conditions. Output a CSV with columns condition, energy_eV, probability_density.
- Output file: `/app/outputs/monte_carlo_distribution.csv`
- Format: csv
- Contract: condition(string), energy_eV(float), probability_density(float)
- Scoring: scored by hidden verifier

### Step 4: Calculate drift velocity
- Role: scored (load-bearing)
- Action: From the Monte Carlo simulation data, compute the steady‑state drift velocity (in cm/s) for the ‘without_CB’ and ‘with_CB’ conditions. Output a CSV with columns condition, drift_velocity_cm_s.
- Output file: `/app/outputs/drift_velocity.csv`
- Format: csv
- Contract: condition(string), drift_velocity_cm_s(float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/joint_spectral_density.csv`
- `/app/outputs/monte_carlo_distribution.csv`
- `/app/outputs/drift_velocity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### joint_spectral_density.csv
- path: `/app/outputs/joint_spectral_density.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Joint spectral density values for ICFE (exact and Lorentzian) and collisional broadening. Checker recomputes K from the same formulas and parameters and compares with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `type`, `field_kVcm`, `initial_energy_eV`, `P_eV`, `final_energy_eV`, `K`, `model`
  - `units`:
    - `field_kVcm`: kV/cm
    - `initial_energy_eV`: eV
    - `P_eV`: eV
    - `final_energy_eV`: eV
    - `K`: dimensionless

### monte_carlo_distribution.csv
- path: `/app/outputs/monte_carlo_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electron energy distribution histograms with and without collisional broadening. Checker verifies structural properties: the ‘without_CB’ distribution approximates a Maxwellian shape, and the ‘with_CB’ distribution shows a noticeably enhanced high‑energy tail compared to the ‘without_CB’ case.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `energy_eV`, `probability_density`
  - `units`:
    - `energy_eV`: eV
    - `probability_density`: dimensionless

### drift_velocity.csv
- path: `/app/outputs/drift_velocity.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Steady‑state drift velocity for the two conditions. Checker verifies that drift velocity with CB exceeds that without CB by a meaningful margin, consistent with the physical effect of collisional broadening.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `drift_velocity_cm_s`
  - `units`:
    - `drift_velocity_cm_s`: cm/s

Notes: The reproducibility of the Monte Carlo distribution and drift velocity relies on the agent running the full simulation with the specified parameters. The joint spectral density is recomputed from first principles by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "joint_spectral_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "type",
          "field_kVcm",
          "initial_energy_eV",
          "P_eV",
          "final_energy_eV",
          "K",
          "model"
        ],
        "units": {
          "field_kVcm": "kV/cm",
          "initial_energy_eV": "eV",
          "P_eV": "eV",
          "final_energy_eV": "eV",
          "K": "dimensionless"
        }
      },
      "description": "Joint spectral density values for ICFE (exact and Lorentzian) and collisional broadening. Checker recomputes K from the same formulas and parameters and compares with a relative tolerance."
    },
    {
      "file": "monte_carlo_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "energy_eV",
          "probability_density"
        ],
        "units": {
          "energy_eV": "eV",
          "probability_density": "dimensionless"
        }
      },
      "description": "Electron energy distribution histograms with and without collisional broadening. Checker verifies structural properties: the ‘without_CB’ distribution approximates a Maxwellian shape, and the ‘with_CB’ distribution shows a noticeably enhanced high‑energy tail compared to the ‘without_CB’ case."
    },
    {
      "file": "drift_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "drift_velocity_cm_s"
        ],
        "units": {
          "drift_velocity_cm_s": "cm/s"
        }
      },
      "description": "Steady‑state drift velocity for the two conditions. Checker verifies that drift velocity with CB exceeds that without CB by a meaningful margin, consistent with the physical effect of collisional broadening."
    }
  ],
  "notes": "The reproducibility of the Monte Carlo distribution and drift velocity relies on the agent running the full simulation with the specified parameters. The joint spectral density is recomputed from first principles by the checker."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently checks each required output file and combines the scores by weight. It does not simply compare a reported number; it evaluates the actual artifacts you produce.

- `joint_spectral_density.csv` is checked by recomputing the expected joint spectral density values from the same formulas and parameters, then comparing them to your submitted values with an appropriate tolerance.
- `monte_carlo_distribution.csv` is audited for structural properties: the `without_CB` distribution should be approximately Maxwellian, and the `with_CB` distribution should show a different high‑energy tail population relative to the `without_CB` case.
- `drift_velocity.csv` is compared against hidden reference values; the drift velocity with collisional broadening is expected to exceed the without‑broadening value by a significant amount.

The verifier will run the full workflow you are asked to perform; simply reporting a number without generating the intermediate and final artifacts will not suffice.
