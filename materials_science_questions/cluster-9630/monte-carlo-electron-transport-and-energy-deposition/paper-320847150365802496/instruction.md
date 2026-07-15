# Spontaneous charge distribution in metal nanoparticle monolayers on conducting substrates

## Problem background
The task investigates the spontaneous charge state of disordered monolayers of metallic nanoparticles on a conducting substrate. In such structures, thermally activated electron tunneling between particles and the substrate (driven by work-function differences) and between neighboring particles can produce a distribution of excess charges. The electrostatic energy of these transitions depends strongly on the random particle placement, which introduces disorder, and the mutual polarization of particles and image charges in the substrate. The goal is to compute the average charge per particle and the resulting macroscopic surface charge density, and to understand how these quantities vary with surface coverage, dielectric environment, and material properties.

## Approach
The system is modeled as identical spherical metal nanoparticles (core radius r, oxide shell thickness d_p) randomly placed on a planar conducting substrate. The sole source of disorder is the random positions; all particles have the same size. The model is implemented in four stages:

1. **Random particle placement**: Generate a configuration of N = 1600 particles by a random sequential adsorption (billiard) method that enforces a minimum center-to-center distance of 2r + 2d_p. This produces one configuration per surface coverage η.

2. **Capacitance matrix**: Compute the full inverse capacitance matrix C^{-1}_{ij}, which encodes self- and mutual electrostatic energies including image charges and polarization. For each particle, a hemispherical domain containing the 24 nearest neighbors is defined. Laplace’s equation is solved (zero potential on the substrate and the outer boundary) using an open-source FEM solver. An optimization routine finds a set of particle potentials such that the central particle carries a unit test charge while all others remain neutral; this yields C_{ii}^{-1} and C_{ij}^{-1}. For particles outside the domain, the mutual term is approximated by C_{ij} ≈ const/r_{ij}.

3. **Transition rates and Monte Carlo**: Using the capacitance matrix, compute the rates for electron tunneling between a particle and the substrate (via the work-function difference Δw) and between neighboring particles. The tunneling probability for each process is proportional to a thermally activated factor. Start from all particles neutral and run a single‑electron Monte Carlo simulation: at each step, choose a transition according to the rate distribution, update the charges, and recalculate the rates. Evolve until the total system charge becomes approximately constant (quasi‑stationary state).

4. **Aggregation**: From the final charge configuration, extract the average charge per particle (in units of elementary charge e) and the surface charge density (in C/m²) using the elementary charge and the particle number density derived from η and the particle radius.

## Reproduction target
Implement the model for two materials on a carbon substrate:
- Nickel nanoparticles: core radius r = 1.25 nm, oxide shell thickness d_p = 0.2 nm, work-function difference Δw = -0.25 eV (Ni relative to substrate).
- Platinum nanoparticles: core radius r = 0.9 nm, oxide shell thickness d_p = 0.2 nm, work-function difference Δw = +0.60 eV (Pt relative to substrate).

For each material, perform simulations at dielectric constants ε = 1 and ε = 2, and for surface coverages η = 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7. Use a temperature of T = 300 K. Compute the average charge per particle (in elementary charge e) and the surface charge density (in C/m²). Collect all results in a single CSV file `average_charge_results.csv` with columns: material (Ni or Pt), epsilon (float), eta (float), avg_charge (float), surface_charge_density (float). Every combination of material, ε, and η must be present.

## Assets

- Open-source finite element solver (e.g., FEniCS, deal.II, or scikit-fem): https://fenicsproject.org/download/
- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Random nanoparticle placement
- Role: process
- Action: Generate random positions for N=1600 identical spherical nanoparticles on the substrate surface using a billiard method (random sequential adsorption or equivalent) that enforces the minimum center-to-center distance 2r+2d_p. Produce one configuration per surface coverage η listed in the target.
- Evidence: `/app/outputs/positions.csv`

### Step 2: Capacitance matrix calculation
- Role: process
- Action: For each configuration, compute the inverse capacitance matrix C^{-1}_{ij} by solving Laplace's equation on a hemispherical domain around each particle using an open-source FEM solver. Include the 24 nearest neighbors and impose zero potential on the substrate and the outer boundary. Use an optimization routine (e.g., SciPy) to find potentials yielding unit charge on the central particle and zero on others. For particles outside the domain, approximate C_{ij} ∝ r_{ij}.
- Evidence: `/app/outputs/capacitance_matrix.npy`

### Step 3: Single-electron Monte Carlo simulation
- Role: process
- Action: Initialize all particles with zero excess charge. Using the capacitance matrix and the transition rate formulas with material-specific work function differences, temperature 300 K, and assumed tunneling parameters α and χ, run a single-electron Monte Carlo simulation until a quasi-stationary state is reached (total charge approximately constant over many transitions). Repeat for all combinations of material, ε, and η.
- Evidence: `/app/outputs/charge_states.csv`

### Step 4: Compute average charge and surface charge density
- Role: scored (load-bearing)
- Action: From the simulated charge configurations, calculate the average charge per particle (in units of elementary charge) and the surface charge density (in C/m², using elementary charge 1.602e-19 C and the particle number density derived from η and particle radius). Collect results for all η, ε, and materials and write them to average_charge_results.csv.
- Output file: `/app/outputs/average_charge_results.csv`
- Format: csv
- Contract: Columns: material (string, 'Ni' or 'Pt'), epsilon (float), eta (float), avg_charge (float, units of elementary charge), surface_charge_density (float, units C/m²). Each row is one (material, epsilon, eta) combination; values for eta = 0.1,0.2,0.3,0.4,0.5,0.6,0.7 and epsilon = 1,2 must be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/average_charge_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### average_charge_results.csv
- path: `/app/outputs/average_charge_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Average charge per nanoparticle and surface charge density as functions of material, dielectric constant, and surface coverage.
- schema:
  - `type`: table
  - `required_columns`: `material`, `epsilon`, `eta`, `avg_charge`, `surface_charge_density`
  - `units`:
    - `epsilon`: dimensionless
    - `eta`: dimensionless (fraction of surface coverage)
    - `avg_charge`: elementary charge e
    - `surface_charge_density`: C/m^2

Notes: The agent must re-implement the full computation from scratch using an open-source FEM solver and SciPy optimization, replacing the proprietary COMSOL/SNOPT used in the paper. Only the main quantitative results (average charge, surface charge density) are scored; other paper figures (energy histograms, electric field distribution) are omitted as they are either qualitative or not central to the principal claim. The Monte Carlo simulation is stochastic; the provided tolerances absorb run-to-run variation. Tunneling rate pre-factors (α, χ) are not explicitly stated in the paper; the solver must choose physically plausible values (e.g., α=1e12 s⁻¹, χ=10 nm⁻¹) – the overall trends are robust and tolerance accounts for any resulting shift.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "average_charge_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "epsilon",
          "eta",
          "avg_charge",
          "surface_charge_density"
        ],
        "units": {
          "epsilon": "dimensionless",
          "eta": "dimensionless (fraction of surface coverage)",
          "avg_charge": "elementary charge e",
          "surface_charge_density": "C/m^2"
        }
      },
      "description": "Average charge per nanoparticle and surface charge density as functions of material, dielectric constant, and surface coverage."
    }
  ],
  "notes": "The agent must re-implement the full computation from scratch using an open-source FEM solver and SciPy optimization, replacing the proprietary COMSOL/SNOPT used in the paper. Only the main quantitative results (average charge, surface charge density) are scored; other paper figures (energy histograms, electric field distribution) are omitted as they are either qualitative or not central to the principal claim. The Monte Carlo simulation is stochastic; the provided tolerances absorb run-to-run variation. Tunneling rate pre-factors (α, χ) are not explicitly stated in the paper; the solver must choose physically plausible values (e.g., α=1e12 s⁻¹, χ=10 nm⁻¹) – the overall trends are robust and tolerance accounts for any resulting shift."
}
```

## How you are scored
A hidden verifier will read your CSV and compare each row’s `avg_charge` and `surface_charge_density` to reference values that represent the expected physical behavior for those conditions. The comparison tolerates realistic spread from stochastic simulation, finite-element discretization, and solver choices. For each row, full credit is awarded if the values fall within generous tolerances; partial credit is given for larger deviations, proportionally. The final reward is the average credit over all rows. Do not attempt to guess or fabricate numbers – only a correct implementation of the model yields physically grounded results.
