# Electron density and work-function of alkali-covered semiconductor surfaces (jellium model)

## Problem background
Understanding the electron distribution near clean and alkali-covered semiconductor surfaces is fundamental for predicting work-function changes and the electronic response of these interfaces. The valence electrons form a many-body system that screens the positive ion background, and electron-electron correlation effects are essential for a realistic description. When electropositive adsorbates such as alkali atoms are deposited, they donate charge and modify the surface dipole, altering the work-function. A uniform positive background (jellium) model, supplemented by a dielectric formalism that accounts for Coulomb correlation, provides a tractable framework for computing the electron density profile and work-function as a function of adsorbate coverage without relying on empirical parameters. The target of this task is to compute the electron density distribution and work-function for a germanium surface with and without an alkali adlayer, thereby demonstrating the predictive power of the correlated-jellium approach.

## Approach
The surface is modeled by a semi-infinite semiconductor (x<0) covered by a uniform positive adlayer of thickness d and average density n̄_a (x in [0,d]). The positive background charge density is piecewise constant: bulk semiconductor density n̄ for x<0, adlayer density n̄_a for 0<x≤d, and zero for x>d. The total electron density n(x) is represented variationally as a piecewise-exponential function that is continuous and differentiable at x=0 and satisfies overall charge neutrality. This ansatz depends on a single variational parameter y, which controls the decay of the electron density on both sides of the interface and encodes the adlayer properties through the relative density s = n̄_a / n̄. The parameter y is determined by a modified sum rule that generalizes the jellium-surface sum rule to the semiconductor-adlayer system. The sum rule involves the electrostatic potential at the surface and the derivative of the bulk energy with respect to density, and leads to a transcendental equation that must be solved numerically for each combination of adlayer thickness d and adsorbate surface density N_a = n̄_a d. The bulk electron system is characterized by the density parameter r_s (where (4π/3) r_s^3 = 1/n̄) and the static dielectric constant κ. The ground-state energy per electron E(r_s) incorporates kinetic, Hartree-Fock exchange, and correlation contributions via the Inkson dielectric function. From this energy, the chemical potential μ is obtained. Once y is known, the work-function Φ is evaluated from the electrostatic potential difference corrected by μ, and the full electron density profile n(x) can be reconstructed from the exponential ansatz. The implementation requires evaluating the bulk energy and chemical potential, solving the transcendental equation for y over a range of (d, N_a) values, and finally computing Φ and the normalized density n(x)/n̄ for selected configurations.

## Reproduction target
Compute and provide as scored artifacts:
1. **Work-function versus adsorbate density** — For adlayer thicknesses d = 5, 6, and 7 atomic units, compute the work-function Φ (in eV) at surface densities N_a ranging from 0 to 10×10^14 atoms/cm^2 in steps of 0.5×10^14 atoms/cm^2. Store the results as a CSV table with columns `d`, `Na`, `Phi`.
2. **Normalized electron density profile** — For two configurations: the clean surface (N_a = 0) and a covered surface with N_a = 6.7×10^14 atoms/cm^2 and d = 7.13 atomic units, compute n(x)/n̄ at positions x from -10 to +10 atomic units in steps of 0.5 au. Store the data as a CSV table with columns `case` (string 'clean' or 'covered'), `x`, and `n_over_nbar`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute bulk energy and chemical potential
- Role: process
- Action: Using the substrate density parameter rs=2.085 and dielectric constant κ=16, compute the bulk energy per electron E(rs) and the chemical potential μ from the energy functional formula that includes kinetic, Hartree-Fock exchange, and correlation terms. Save both values as a JSON file for later use.
- Evidence: `/app/outputs/bulk_energy.json`

### Step 2: Solve for variational parameter y
- Role: process
- Action: For each combination of adlayer thickness d (5, 6, 7 au) and adsorbate surface density Na (from 0 to 10×10^14 atoms/cm² in steps of 0.5×10^14 cm⁻²), calculate the relative density s = Na/(n̄ d) where n̄ = (4π rs³/3)⁻¹, then numerically solve the transcendental equation arising from the modified sum rule to obtain the variational parameter y. Record the results as a CSV file with columns d, Na, y.
- Evidence: `/app/outputs/variational_y.csv`

### Step 3: Compute work-function Φ vs Na
- Role: scored (load-bearing)
- Action: For each (d, Na) pair, use the solved y values and the previously computed chemical potential μ to evaluate the work-function Φ (in eV) via the formula that relates Φ to y, d, s, and μ. Write a CSV file with columns d (au), Na (atoms/cm²), Phi (eV).
- Output file: `/app/outputs/workfunction_vs_Na.csv`
- Format: csv
- Contract: Three columns: d (float, atomic units), Na (float, atoms per cm²), Phi (float, eV). Rows for d=5,6,7 au each with Na from 0 to 10×10^14 cm⁻² in steps of 0.5×10^14 cm⁻².
- Scoring: scored by hidden verifier

### Step 4: Compute electron density profile
- Role: scored
- Action: For the clean surface (Na=0) and a covered surface (Na=6.7×10^14 cm⁻², d=7.13 au), determine the appropriate y values (handling the s→0 limit for the clean case). Using the piecewise exponential ansatz for the electron density n(x), evaluate the normalized density n(x)/n̄ at x from -10 to 10 au in steps of 0.5 au. Write a CSV file with columns case, x, n_over_nbar.
- Output file: `/app/outputs/density_profile.csv`
- Format: csv
- Contract: Three columns: case (string, 'clean' or 'covered'), x (float, atomic units), n_over_nbar (float, dimensionless). x from -10 to 10 au in steps of 0.5 au.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/workfunction_vs_Na.csv`
- `/app/outputs/density_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### workfunction_vs_Na.csv
- path: `/app/outputs/workfunction_vs_Na.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Work-function as a function of adsorbate surface density for three adlayer thicknesses.
- schema:
  - `type`: table
  - `required_columns`: `d`, `Na`, `Phi`
  - `units`:
    - `d`: atomic units
    - `Na`: atoms/cm^2
    - `Phi`: eV

### density_profile.csv
- path: `/app/outputs/density_profile.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized electron density profile for clean and covered surfaces.
- schema:
  - `type`: table
  - `required_columns`: `case`, `x`, `n_over_nbar`
  - `units`:
    - `x`: atomic units
    - `n_over_nbar`: dimensionless

Notes: The experimental comparison (Fig. 3) is excluded because the experimental data are not public. The work-function and density profile are computational predictions that can be verified against hidden gold values derived from the same equations with high precision.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "workfunction_vs_Na.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "d",
          "Na",
          "Phi"
        ],
        "units": {
          "d": "atomic units",
          "Na": "atoms/cm^2",
          "Phi": "eV"
        }
      },
      "description": "Work-function as a function of adsorbate surface density for three adlayer thicknesses."
    },
    {
      "file": "density_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "x",
          "n_over_nbar"
        ],
        "units": {
          "x": "atomic units",
          "n_over_nbar": "dimensionless"
        }
      },
      "description": "Normalized electron density profile for clean and covered surfaces."
    }
  ],
  "notes": "The experimental comparison (Fig. 3) is excluded because the experimental data are not public. The work-function and density profile are computational predictions that can be verified against hidden gold values derived from the same equations with high precision."
}
```

## How you are scored
After you submit the output files, a hidden verifier will independently check each scored artifact. The verifier will compare your computed work-function values for a set of hidden (d, N_a) points and your electron density values at selected positions against reference results obtained from the same underlying equations with high numerical precision. The check uses appropriate tolerances to account for legitimate numerical differences in root-finding and floating-point operations. Each artifact's score is combined into a final reward between 0 and 1 according to a predefined weighting scheme; simply stating a number from the paper without running the actual computation will not receive credit. The verifier may also validate file format and schema. No further hints about expected values are provided.
