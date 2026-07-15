# Comparison of Metastable and Equilibrium Drop Properties via Lattice-Gas Quasichemical Approximation

## Problem background
This work computationally compares the properties of metastable and equilibrium drops in the vapor phase. A spherical drop is described by a lattice-gas model in the quasichemical approximation. The comparison investigates how the total free energy and total mass of the drop depend on the drop radius (size) and on the choice of the dividing surface (equimolecular, moments-of-forces, or tension surface) over a range of reduced temperatures. The key quantities to compute are the ratios of total free energy and total mass between metastable and equilibrium drops of the same size, as well as ratios of localized internal properties (liquid density, internal pressure, chemical potential difference, surface tension).

## Approach
The system is modeled as a spherical drop of a lattice gas, with a liquid core of radius R (in lattice units) surrounded by a vapor phase and an interfacial transition layer. The state is determined by solving the quasichemical approximation equations self-consistently for the layer-resolved densities, internal pressures, chemical potentials, and surface tension. Equilibrium drops satisfy equal chemical potentials between liquid and vapor; metastable drops have a chemical potential difference. Three definitions of the dividing surface are used: (a) equimolecular surface, (b) surface derived from the equality of moments of forces, and (c) the tension surface (which only exists above a certain temperature). For each combination of reduced temperature, drop radius, and dividing surface, the layer profiles are computed, and the total free energy and total mass are aggregated by summing contributions from the liquid volume and the transition layers. Ratios of these total quantities between metastable and equilibrium drops, as well as ratios of the liquid-phase internal properties, are then extracted.

## Reproduction target
Implement the lattice-gas quasichemical solver for spherical drops and generate two CSV files:

- `energies_and_masses.csv`: columns `temperature` (float), `dividing_surface` (string, one of `equimolecular`, `moments_of_forces`, `tension`), `R` (int), `E_ratio` (float), `m_ratio` (float).
- `local_properties.csv`: columns `temperature` (float), `dividing_surface` (string), `R` (int), `theta_ratio` (float), `pi_ratio` (float), `delta_mu` (float), `sigma_ratio` (float).

Compute results for reduced temperatures τ = 0.55 and 0.89, and for drop radii R from 1 to 20 inclusive (lattice units). The Lennard-Jones related lattice structure parameter is λ = 1.12. For τ = 0.55, use only the equimolecular and moments-of-forces dividing surfaces; for τ = 0.89, include all three dividing surfaces. Produce the files in `/app/outputs`.

## Assets

- Lattice-gas model and quasichemical approximation
- Python: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define model parameters and conditions
- Role: process
- Action: Define the thermodynamic conditions: reduced temperatures τ = 0.55 and 0.89, drop radii R as integers from 1 to 20 (in lattice units), Lennard-Jones lattice parameter λ = 1.12, and the three dividing surface conventions (equimolecular, moments-of-forces, tension). Specify the condition for equilibrium drops (chemical potentials equal) and metastable drops (chemical potentials differ).
- Evidence: none

### Step 2: Solve drop profiles via lattice-gas quasichemical approximation
- Role: process
- Action: Implement the lattice-gas quasichemical approximation for a spherical drop. For each combination of (τ, R, dividing surface, drop type), compute the layer-resolved density θ_q, internal liquid pressure π_1, chemical potentials μ_ℓ and μ_κ, surface tension σ, and dividing surface radius ρ. The model equations are derived from the lattice-gas model; use self-consistent iterative solution.
- Evidence: none

### Step 3: Compute total free energy and total mass
- Role: process
- Action: From the layer-resolved profiles, compute the total free energy E and total mass m for each drop using the formulas E = V_l E_l + Σ_q 4π(R+ρ)² E_q and m = V_l θ_l + Σ_q 4π(R+ρ)² θ_q, where the sums run over the transition layers.
- Evidence: none

### Step 4: Compute energy and mass ratios
- Role: scored (load-bearing)
- Action: For each combination of temperature, dividing surface, and R, compute the ratios E_meta/E_eq and m_meta/m_eq. Write the results to energies_and_masses.csv.
- Output file: `/app/outputs/energies_and_masses.csv`
- Format: csv
- Contract: Columns: temperature (float), dividing_surface (string, one of equimolecular, moments_of_forces, tension), R (int), E_ratio (float), m_ratio (float).
- Scoring: scored by hidden verifier

### Step 5: Compute local property ratios
- Role: scored
- Action: For each combination of temperature, dividing surface, and R, compute the ratios θ*_1/θ_1, π*_1/π_1, Δμ = μ_ℓ − μ_κ, and σ/σ_b (relative to planar surface tension σ_b). Write the results to local_properties.csv.
- Output file: `/app/outputs/local_properties.csv`
- Format: csv
- Contract: Columns: temperature (float), dividing_surface (string), R (int), theta_ratio (float), pi_ratio (float), delta_mu (float), sigma_ratio (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies_and_masses.csv`
- `/app/outputs/local_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies_and_masses.csv
- path: `/app/outputs/energies_and_masses.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ratios of total free energy and total mass between metastable and equilibrium drops for each (temperature, dividing_surface, R) condition.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `dividing_surface`, `R`, `E_ratio`, `m_ratio`

### local_properties.csv
- path: `/app/outputs/local_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Local property ratios and chemical potential difference for each (temperature, dividing_surface, R) condition.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `dividing_surface`, `R`, `theta_ratio`, `pi_ratio`, `delta_mu`, `sigma_ratio`

Notes: The hidden checker compares selected rows (R=2,5,10,15 at τ=0.55 and 0.89 for equimolecular and moments-of-forces surfaces) to pre-extracted reference values with a 5% relative tolerance, and also validates qualitative trends (presence of a maximum, decrease to zero, coincidence at very small R).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies_and_masses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "dividing_surface",
          "R",
          "E_ratio",
          "m_ratio"
        ]
      },
      "description": "Ratios of total free energy and total mass between metastable and equilibrium drops for each (temperature, dividing_surface, R) condition."
    },
    {
      "file": "local_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "dividing_surface",
          "R",
          "theta_ratio",
          "pi_ratio",
          "delta_mu",
          "sigma_ratio"
        ]
      },
      "description": "Local property ratios and chemical potential difference for each (temperature, dividing_surface, R) condition."
    }
  ],
  "notes": "The hidden checker compares selected rows (R=2,5,10,15 at τ=0.55 and 0.89 for equimolecular and moments-of-forces surfaces) to pre-extracted reference values with a 5% relative tolerance, and also validates qualitative trends (presence of a maximum, decrease to zero, coincidence at very small R)."
}
```

## How you are scored
A hidden verifier inspects your CSV output files after submission. It compares the reported ratios (E_ratio, m_ratio, theta_ratio, pi_ratio, delta_mu, sigma_ratio) against pre-extracted reference values using appropriate tolerances. It also checks qualitative trends: for example, the ratios should exhibit a maximum at intermediate radii and approach 1.0 at very small R. Each scored step is assigned a weight, and your final reward is the weighted sum of the stage scores. The verifier does not re-run your simulation; it only validates the contents of the output files you provide.
