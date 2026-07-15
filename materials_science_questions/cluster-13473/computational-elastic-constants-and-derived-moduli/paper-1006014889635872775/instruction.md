# Local Elastic Moduli in Nanocrystalline Metals via Molecular Dynamics

## Problem background
Nanocrystalline metals exhibit non-uniform local elastic properties because a significant fraction of atoms reside at or near grain boundaries, where the atomic arrangement differs markedly from the crystalline interior. Understanding how these local elastic moduli are distributed spatially and how their averages depend on grain size is essential for predicting macroscopic mechanical behaviour and for developing mean‑field models of polycrystalline materials. This task addresses that open question by using molecular dynamics to compute per‑atom elastic moduli in nanocrystalline copper and tantalum across a range of grain sizes, providing data to test the relationship between microstructure and local elasticity.

## Approach
The approach combines classical molecular dynamics with a local elasticity evaluator. Starting from polycrystalline initial configurations of Cu and Ta generated via Voronoi tessellation, each system is equilibrated under zero pressure and then simulated in the NVT ensemble. During the NVT run, a custom LAMMPS compute evaluates the per‑atom Born elasticity tensor for embedded‑atom‑method (EAM) potentials, from which local bulk, shear, Young’s moduli and Poisson’s ratio are derived via Voigt averages. Atoms are classified as grain or grain‑boundary using the centrosymmetry parameter. The resulting per‑atom data allow constructing probability density histograms of the local shear modulus, computing population‑averaged elastic moduli at each grain size, determining the grain‑boundary atomic fraction, and fitting a mean‑field model that relates total moduli to grain and grain‑boundary contributions.

## Reproduction target
For nanocrystalline Cu and Ta with grain sizes 5, 8, 10, 12, 15, 18, 20 nm, perform the simulations and compute the following scored artifacts: (1) probability density histograms of per‑atom shear modulus for grain and grain‑boundary atoms; (2) average elastic moduli (shear modulus G, Young’s modulus E, bulk modulus B, Poisson’s ratio ν) for total, grain, and grain‑boundary populations; (3) grain‑boundary atomic fraction as a function of grain size; (4) mean‑field model parameters (characteristic length d₀ from inverse‑grain‑size scaling, and grain‑size‑averaged moduli of grain and grain‑boundary atoms). The target is to produce these results from the described protocol; the hidden verifier will compare the submitted outputs against independently derived reference values.

## Assets

- LAMMPS molecular dynamics code: https://www.lammps.org/
- Cu EAM interatomic potential – Mishin et al. (2001): https://www.ctcms.nist.gov/potentials/download/Cu/1/Cu_mishin01.eam.alloy
- Ta EAM interatomic potential – Ravelo et al. (2013): https://www.ctcms.nist.gov/potentials/download/Ta/1/Ta_ravelo13.eam.alloy

## Workflow steps

### Step 1: Generate polycrystalline initial configurations
- Role: process
- Action: Create initial atomic configurations of nanocrystalline Cu (fcc, a=3.615 Å) and Ta (bcc, a=3.304 Å) with grain sizes d = 5, 8, 10, 12, 15, 18, 20 nm using Voronoi tessellation. Keep the number of grains constant across sizes.
- Evidence: `/app/outputs/generation.log`

### Step 2: Equilibrate via NPT relaxation
- Role: process
- Action: For each initial configuration, run an NPT molecular dynamics simulation in LAMMPS using the corresponding EAM potential. Relax the box size until the total pressure averages to zero (target pressure zero, 200 ps with 2 fs timestep). Monitor instantaneous and cumulative average pressure.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: NVT MD with on‑the‑fly local elasticity calculation
- Role: process
- Action: Run an NVT molecular dynamics simulation on each relaxed configuration using a custom LAMMPS compute that implements the per‑atom Born elasticity tensor for EAM potentials. The per‑atom tensor is computed using the EAM‑specific formula:

V_i C_{i,αβγδ}^B = 1/2 ∑_{j≠i} X_{ij} (r_{ij,α} r_{ij,β} r_{ij,γ} r_{ij,δ}) / r_{ij}^2 + F''(ρ_i) g_{i,αβ} g_{i,γδ}

with

X_{ij} = v''(r_{ij}) - (1/r_{ij}) v'(r_{ij}) + (F'(ρ_i) + F'(ρ_j)) (ρ''(r_{ij}) - (1/r_{ij}) ρ'(r_{ij})),

g_{i,αβ} = ∑_{j≠i} ρ'(r_{ij}) (r_{ij,α} r_{ij,β} / r_{ij}),

where v, F, ρ are the EAM potential functions (pair potential, embedding function, density). Then derive local moduli using Voigt averages:

9 B = C_{11}+C_{22}+C_{33}+2(C_{12}+C_{23}+C_{31}),

15 G = C_{11}+C_{22}+C_{33}−(C_{12}+C_{23}+C_{31})+3(C_{44}+C_{55}+C_{66}),

1/E = 1/(3G) + 1/(9B),

ν = 1/2 (1 − 3G/(3B+G)).

Output per‑atom elastic tensor components and the derived local moduli (bulk B, shear G, Young’s E, Poisson’s ratio ν). Also calculate the per‑atom centrosymmetry parameter.
- Evidence: `/app/outputs/per_atom_elasticity.tar.gz`

### Step 4: Compute shear‑modulus probability density histograms
- Role: scored (load-bearing)
- Action: Read the per‑atom data, classify each atom as grain or grain‑boundary using the centrosymmetry parameter, and for each metal and grain size build normalized probability density histograms of the per‑atom shear modulus for grain and grain‑boundary populations. Write the results.
- Output file: `/app/outputs/shear_modulus_distributions.csv`
- Format: csv
- Contract: metal, grain_size_nm, atom_type, bin_center_GPa, density
- Scoring: scored by hidden verifier

### Step 5: Compute average elastic moduli per population
- Role: scored
- Action: Using the same per‑atom data and classification, compute the arithmetic average of shear modulus G, Young’s modulus E, bulk modulus B, and Poisson’s ratio ν for the total system, grain atoms, and grain‑boundary atoms at each grain size. Write the results.
- Output file: `/app/outputs/average_moduli.csv`
- Format: csv
- Contract: metal, grain_size_nm, population, G_GPa, E_GPa, B_GPa, Poisson_ratio
- Scoring: scored by hidden verifier

### Step 6: Compute grain‑boundary atomic fraction
- Role: scored
- Action: From the per‑atom classification, calculate the grain‑boundary atomic fraction x_gb as a function of grain size. Write the fractions.
- Output file: `/app/outputs/gb_fraction.csv`
- Format: csv
- Contract: metal, grain_size_nm, gb_fraction
- Scoring: scored by hidden verifier

### Step 7: Derive mean‑field model parameters
- Role: scored
- Action: Using the average moduli and the grain‑boundary fraction, fit the scaling relation x_gb = d0 / d to obtain d0. Compute the grain‑size‑averaged moduli of grain and grain‑boundary atoms. Write the mean‑field model parameters.
- Output file: `/app/outputs/mean_field_params.csv`
- Format: csv
- Contract: metal, d0_nm, avg_G_grain_GPa, avg_G_gb_GPa, avg_E_grain_GPa, avg_E_gb_GPa, avg_B_grain_GPa, avg_B_gb_GPa, avg_poisson_grain, avg_poisson_gb
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/shear_modulus_distributions.csv`
- `/app/outputs/average_moduli.csv`
- `/app/outputs/gb_fraction.csv`
- `/app/outputs/mean_field_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shear_modulus_distributions.csv
- path: `/app/outputs/shear_modulus_distributions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized probability density histograms of the per‑atom shear modulus, separately for grain and grain‑boundary atoms, for every (metal, grain_size) combination. The histogram bins and density values must be such that the L1 distance to the hidden gold (from the paper's Fig. 4) is below the required tolerance.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `grain_size_nm`, `atom_type`, `bin_center_GPa`, `density`
  - `units`:
    - `bin_center_GPa`: GPa
    - `density`: dimensionless probability density (integral ≈ 1)

### average_moduli.csv
- path: `/app/outputs/average_moduli.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Average elastic moduli for total, grain, and grain‑boundary populations for each metal and grain size. Values are compared against hidden gold from the paper (Fig. 8) within relative tolerances (5% for G, E, B; 10% for Poisson's ratio).
- schema:
  - `type`: table
  - `required_columns`: `metal`, `grain_size_nm`, `population`, `G_GPa`, `E_GPa`, `B_GPa`, `Poisson_ratio`
  - `units`:
    - `G_GPa`: GPa
    - `E_GPa`: GPa
    - `B_GPa`: GPa
    - `Poisson_ratio`: dimensionless

### gb_fraction.csv
- path: `/app/outputs/gb_fraction.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Grain‑boundary atomic fraction x_gb as a function of grain size for Cu and Ta. The hidden checker verifies that the fractions follow x_gb = d0/d with d0 within 0.3 nm of the paper's values (Cu ≈ 1.5 nm, Ta ≈ 1.7 nm).
- schema:
  - `type`: table
  - `required_columns`: `metal`, `grain_size_nm`, `gb_fraction`
  - `units`:
    - `gb_fraction`: dimensionless fraction between 0 and 1

### mean_field_params.csv
- path: `/app/outputs/mean_field_params.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Mean‑field model parameters: d0 from the 1/d fit and grain‑size‑averaged moduli of grain and grain‑boundary atoms. The values must be self‑consistent with steps 5 and 6, and d0 must match the paper's values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `d0_nm`, `avg_G_grain_GPa`, `avg_G_gb_GPa`, `avg_E_grain_GPa`, `avg_E_gb_GPa`, `avg_B_grain_GPa`, `avg_B_gb_GPa`, `avg_poisson_grain`, `avg_poisson_gb`
  - `units`:
    - `d0_nm`: nm
    - `avg_G_grain_GPa`: GPa
    - `avg_G_gb_GPa`: GPa
    - `avg_E_grain_GPa`: GPa
    - `avg_E_gb_GPa`: GPa
    - `avg_B_grain_GPa`: GPa
    - `avg_B_gb_GPa`: GPa
    - `avg_poisson_grain`: dimensionless
    - `avg_poisson_gb`: dimensionless

Notes: All outputs are CSV files with headers. The hidden checker will digitise reference histograms and compare them using L1 distance, apply relative tolerances to average moduli, and check scaling consistency. No network fetch is required for the checker; all gold values are bundled.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shear_modulus_distributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "grain_size_nm",
          "atom_type",
          "bin_center_GPa",
          "density"
        ],
        "units": {
          "bin_center_GPa": "GPa",
          "density": "dimensionless probability density (integral ≈ 1)"
        }
      },
      "description": "Normalized probability density histograms of the per‑atom shear modulus, separately for grain and grain‑boundary atoms, for every (metal, grain_size) combination. The histogram bins and density values must be such that the L1 distance to the hidden gold (from the paper's Fig. 4) is below the required tolerance."
    },
    {
      "file": "average_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "grain_size_nm",
          "population",
          "G_GPa",
          "E_GPa",
          "B_GPa",
          "Poisson_ratio"
        ],
        "units": {
          "G_GPa": "GPa",
          "E_GPa": "GPa",
          "B_GPa": "GPa",
          "Poisson_ratio": "dimensionless"
        }
      },
      "description": "Average elastic moduli for total, grain, and grain‑boundary populations for each metal and grain size. Values are compared against hidden gold from the paper (Fig. 8) within relative tolerances (5% for G, E, B; 10% for Poisson's ratio)."
    },
    {
      "file": "gb_fraction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "grain_size_nm",
          "gb_fraction"
        ],
        "units": {
          "gb_fraction": "dimensionless fraction between 0 and 1"
        }
      },
      "description": "Grain‑boundary atomic fraction x_gb as a function of grain size for Cu and Ta. The hidden checker verifies that the fractions follow x_gb = d0/d with d0 within 0.3 nm of the paper's values (Cu ≈ 1.5 nm, Ta ≈ 1.7 nm)."
    },
    {
      "file": "mean_field_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "d0_nm",
          "avg_G_grain_GPa",
          "avg_G_gb_GPa",
          "avg_E_grain_GPa",
          "avg_E_gb_GPa",
          "avg_B_grain_GPa",
          "avg_B_gb_GPa",
          "avg_poisson_grain",
          "avg_poisson_gb"
        ],
        "units": {
          "d0_nm": "nm",
          "avg_G_grain_GPa": "GPa",
          "avg_G_gb_GPa": "GPa",
          "avg_E_grain_GPa": "GPa",
          "avg_E_gb_GPa": "GPa",
          "avg_B_grain_GPa": "GPa",
          "avg_B_gb_GPa": "GPa",
          "avg_poisson_grain": "dimensionless",
          "avg_poisson_gb": "dimensionless"
        }
      },
      "description": "Mean‑field model parameters: d0 from the 1/d fit and grain‑size‑averaged moduli of grain and grain‑boundary atoms. The values must be self‑consistent with steps 5 and 6, and d0 must match the paper's values within tolerance."
    }
  ],
  "notes": "All outputs are CSV files with headers. The hidden checker will digitise reference histograms and compare them using L1 distance, apply relative tolerances to average moduli, and check scaling consistency. No network fetch is required for the checker; all gold values are bundled."
}
```

## How you are scored
A hidden verifier checks each of the four scored output files independently against reference data. Each file contributes a share of the total reward, with the main emphasis on the shear‑modulus distributions and the average elastic moduli. The verifier does not simply check for presence; it compares the quantitative contents using appropriate statistical measures and self‑consistency checks. Reporting the paper’s numbers alone is not sufficient — your outputs must be computed from the molecular dynamics workflow. The final reward is a weighted sum of the per‑artifact scores, with the largest weight on the distributions and average moduli.
