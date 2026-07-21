# Lattice-gas model of CO adlayers on a square lattice: phase diagram, heat of adsorption, and adsorption isobars

## Problem background
CO adsorbs on Pd(100) surfaces on bridge sites and forms various ordered structures depending on coverage. A lattice-gas model with pairwise interactions—strong nearest-neighbour (NN) and second-nearest-neighbour (2NN) exclusion, and a finite third-nearest-neighbour (3NN) repulsion—can describe the statistical mechanics of the adlayer. The model predicts phase boundaries between disordered, semiordered, and fully ordered phases, a coverage-dependent isosteric heat of adsorption, and adsorption isobars. Here we implement this lattice-gas model and compute these quantities numerically. The computed phase diagram, heat curve, and isobars can then be compared against experimental measurements to assess the model.

## Approach
We model the CO adlayer on a square lattice of bridge sites (obtained by rotating the Pd(100) substrate lattice by 45°). The Hamiltonian includes infinite NN and 2NN exclusion and a finite positive 3NN repulsion ω₃. Phase boundaries are located by transfer-matrix (TM) calculations on strips of size M=10 and by Monte Carlo (MC) simulations on L×L lattices (L=40–128) with periodic boundary conditions; transitions are identified via maxima in dθ/dμ or heat capacity. The isosteric heat of adsorption E_st is obtained from TM data in the grand canonical ensemble by computing the coverage dependence of the chemical potential at fixed temperature, using the interaction parameters ω₂=0.17 eV, ω₃=0.03 eV. Adsorption isobars are computed by coupling the lattice-gas model to a gas-phase reservoir via the relation μ = ε_b + k_B T ln(P/(ν₀√(2π m k_B T))) with ε_b=1.60 eV and ν₀=10¹³ s⁻¹. All calculations use the Python scientific stack (numpy, scipy, matplotlib).

## Reproduction target
Compute and output the following three CSV artifacts:
1) Phase boundary points (both the μ-ω₃ and coverage-temperature diagrams) for the lattice-gas model with NN/2NN exclusion and finite 3NN repulsion.
2) The coverage-dependent isosteric heat of adsorption at T=300 K using ω₂=0.17 eV, ω₃=0.03 eV.
3) The adsorption isobar for p_CO = 1×10⁻⁷ Torr over a temperature range that captures the 0.5 ML plateau and the dense regime.
The correctness of the submitted CSV files is evaluated by comparing the computed phase boundaries, heat values, and isobar coverage-vs.-temperature curves against hidden reference data. The task is self-contained; no external datasets need to be downloaded.

## Assets

- Python scientific computing stack (numpy, scipy, matplotlib): numpy, scipy, matplotlib

## Workflow steps

### Step 1: Compute phase diagram (μ-ω3 and coverage-T)
- Role: scored (load-bearing)
- Action: Implement the lattice-gas model with NN and 2NN exclusion (infinite repulsion) and finite 3NN repulsion on the rotated square lattice. Use transfer matrix (TM) calculations on strips of size M=10 and Monte Carlo (MC) simulations on L×L systems (L=40 to 128) with periodic boundary conditions to locate phase boundaries by detecting maxima in dθ/dμ or heat capacity. Compute both the μ-ω3 phase diagram at fixed temperature and the coverage-temperature phase diagram. Output all boundary points with phase type labels.
- Output file: `/app/outputs/phase_boundaries.csv`
- Format: csv
- Contract: Columns: beta_mu (dimensionless chemical potential, float), beta_omega3 (dimensionless 3NN repulsion, float), coverage (monolayer coverage, float; optional, present for coverage-T points), phase_type (string indicating transition, e.g., 'D-SO', 'SO-c4x2', 'D-c4x2', 'D-sqrt5', 'sqrt5-c4x2', 'tricritical'), method (string, 'TM' or 'MC').
- Scoring: scored by hidden verifier

### Step 2: Compute coverage-dependent heat of adsorption
- Role: scored
- Action: Using the lattice-gas model with parameters ω1=∞, ω2=0.17 eV, ω3=0.03 eV, calculate the isosteric heat of adsorption E_st as a function of CO coverage at T=300 K via transfer matrix calculations in the grand canonical ensemble. Output coverage (θ) and E_st (eV).
- Output file: `/app/outputs/heat_adsorption.csv`
- Format: csv
- Contract: Columns: coverage (float, 0 to 1), Est_eV (float, eV).
- Scoring: scored by hidden verifier

### Step 3: Compute adsorption isobars
- Role: scored
- Action: Using the lattice-gas model with parameters ω1=∞, ω2=0.17 eV, ω3=0.03 eV, and binding energy ε_b=1.60 eV, calculate adsorption isobars (coverage vs temperature) for at least p_CO = 1×10⁻⁷ Torr via transfer matrix or MC. Use the relation μ = ε_b + k_B T ln(P/(ν₀√(2π m k_B T))) with ν₀ = 10¹³ s⁻¹. Output temperature (K), coverage, and pressure (Torr).
- Output file: `/app/outputs/adsorption_isobars.csv`
- Format: csv
- Contract: Columns: temperature_K (float, K), coverage (float, monolayer), pressure_Torr (float, Torr).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_boundaries.csv`
- `/app/outputs/heat_adsorption.csv`
- `/app/outputs/adsorption_isobars.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_boundaries.csv
- path: `/app/outputs/phase_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase boundary points for the μ-ω3 and coverage-temperature phase diagrams of the lattice-gas model with NN/2NN exclusion and finite 3NN repulsion. Each row corresponds to a point on a phase boundary, labelled by the nature of the transition and the method used.
- schema:
  - `type`: table
  - `required_columns`: `beta_mu`, `beta_omega3`, `phase_type`, `method`
  - `columns`:
    - `beta_mu`: dimensionless chemical potential, float
    - `beta_omega3`: dimensionless 3NN repulsion, float
    - `coverage`: monolayer coverage, float (optional for μ-ω3 points)
    - `phase_type`: string identifying the transition
    - `method`: string, either 'TM' or 'MC'

### heat_adsorption.csv
- path: `/app/outputs/heat_adsorption.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Coverage-dependent isosteric heat of adsorption computed for ω2=0.17 eV, ω3=0.03 eV at T=300 K using transfer matrix in the grand canonical ensemble.
- schema:
  - `type`: table
  - `required_columns`: `coverage`, `Est_eV`
  - `columns`:
    - `coverage`: CO coverage in monolayers, float between 0 and 1
    - `Est_eV`: isosteric heat of adsorption in eV, float

### adsorption_isobars.csv
- path: `/app/outputs/adsorption_isobars.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption isobars (coverage vs temperature at fixed pressures) for the final set of interaction parameters, using the relation between pressure and chemical potential with ε_b=1.60 eV and ν₀=10¹³ s⁻¹.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `coverage`, `pressure_Torr`
  - `columns`:
    - `temperature_K`: temperature in Kelvin, float
    - `coverage`: CO coverage in monolayers, float
    - `pressure_Torr`: CO gas pressure in Torr, float

Notes: The phase_boundaries.csv file may contain points from both the μ-ω3 and coverage-T diagrams; rows corresponding to the μ-ω3 diagram will have a coverage column left blank or set to NaN. The heat_adsorption.csv covers the full coverage range up to 1 ML. The adsorption_isobars.csv should include at least the p_CO = 1×10⁻⁷ Torr curve and may include additional pressures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta_mu",
          "beta_omega3",
          "phase_type",
          "method"
        ],
        "columns": {
          "beta_mu": "dimensionless chemical potential, float",
          "beta_omega3": "dimensionless 3NN repulsion, float",
          "coverage": "monolayer coverage, float (optional for μ-ω3 points)",
          "phase_type": "string identifying the transition",
          "method": "string, either 'TM' or 'MC'"
        }
      },
      "description": "Phase boundary points for the μ-ω3 and coverage-temperature phase diagrams of the lattice-gas model with NN/2NN exclusion and finite 3NN repulsion. Each row corresponds to a point on a phase boundary, labelled by the nature of the transition and the method used."
    },
    {
      "file": "heat_adsorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coverage",
          "Est_eV"
        ],
        "columns": {
          "coverage": "CO coverage in monolayers, float between 0 and 1",
          "Est_eV": "isosteric heat of adsorption in eV, float"
        }
      },
      "description": "Coverage-dependent isosteric heat of adsorption computed for ω2=0.17 eV, ω3=0.03 eV at T=300 K using transfer matrix in the grand canonical ensemble."
    },
    {
      "file": "adsorption_isobars.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "coverage",
          "pressure_Torr"
        ],
        "columns": {
          "temperature_K": "temperature in Kelvin, float",
          "coverage": "CO coverage in monolayers, float",
          "pressure_Torr": "CO gas pressure in Torr, float"
        }
      },
      "description": "Adsorption isobars (coverage vs temperature at fixed pressures) for the final set of interaction parameters, using the relation between pressure and chemical potential with ε_b=1.60 eV and ν₀=10¹³ s⁻¹."
    }
  ],
  "notes": "The phase_boundaries.csv file may contain points from both the μ-ω3 and coverage-T diagrams; rows corresponding to the μ-ω3 diagram will have a coverage column left blank or set to NaN. The heat_adsorption.csv covers the full coverage range up to 1 ML. The adsorption_isobars.csv should include at least the p_CO = 1×10⁻⁷ Torr curve and may include additional pressures."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. For each workflow stage the checker reads the corresponding CSV file and compares the computed data (phase boundary points, heat of adsorption values, isobar coverage vs. temperature) against hidden reference data derived from the paper. The comparison uses predefined absolute tolerances for key features and checks for required qualitative trends (e.g., monotonic decrease in E_st after 0.5 ML, presence of a coverage plateau near 0.5 ML at the specified pressure). Meeting or exceeding the reference threshold earns full credit for that step; credit decreases as the result deviates further. The per-step scores are weighted (the phase diagram step carries the largest weight) and combined into a final reward between 0 and 1. Reporting plausible numbers is not sufficient—the data must match the expected phase boundaries, heat of adsorption curve shape, and isobar characteristics.
