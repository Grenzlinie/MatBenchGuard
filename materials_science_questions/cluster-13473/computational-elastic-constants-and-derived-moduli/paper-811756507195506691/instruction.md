# Field-Induced Shear Modulus from Gaussian Column Distribution Model for Anisotropic MREs

## Problem background
Magnetorheological elastomers (MREs) are smart materials whose stiffness can be altered by an external magnetic field. Designing MREs with a desired field‑induced shear modulus requires understanding how the modulus depends on the microstructure — the arrangement and dimensions of the magnetic particles embedded in the elastomer matrix. Under a magnetic field, the particles aggregate into column‑like structures; the lengths of these columns are not all equal but follow a certain distribution in real materials. This task implements a model that predicts the field‑induced shear modulus ΔG from the column microstructure: the particles are assumed to form body‑centered tetragonal (BCT) columns whose lengths obey a Gaussian distribution. The model sums the magnetic dipole–dipole interactions within each column and aggregates over the entire column population to obtain the macroscopic shear modulus. Your job is to compute ΔG for several regimes of column length, column width, external magnetic field, and shear strain, producing a CSV file that can be compared with independent calculations.

## Approach
The magnetizable iron particles in the elastomer are treated as identical spheres of known radius and saturation magnetization. They form a large number of parallel BCT columns; the number of particles along a column (the column length ℓ) follows a Gaussian distribution with a given mean L and standard deviation σ. The width of a column is parameterized by an integer b that describes the number of particles across the column cross‑section.

When an external magnetic field H₀ is applied along the column axis and a uniform shear strain γ is imposed, each particle acquires a magnetic dipole moment. The local magnetic field at any particle is the sum of the applied external field and the fields produced by all other dipoles in the same column. Evaluating this sum for a BCT lattice with finite length and shear gives a local‑field factor f(ℓ,b,γ) and its shear derivative k(ℓ,b,γ). Because the dipole moments themselves depend on the local field, a self‑consistent equation must be solved for the dipole moment component p_z. The particle magnetization is linked to the local field via the Fröhlich–Kennelly law, which captures the nonlinearity and saturation at high fields.

After obtaining p_z, the effective magnetic susceptibility χ_eff of the whole composite and its derivative with respect to shear strain are computed by averaging over the Gaussian distribution of column lengths. Finally, the field‑induced shear modulus ΔG is obtained from the shear‑dependent susceptibility. The calculation is repeated for every combination of mean length L, standard deviation σ, column width b, external field H₀, and shear strain γ specified in the reproduction target.

## Reproduction target
Compute the field‑induced shear modulus ΔG (in MPa) for the following three parameter sets, using the fixed physical constants: particle volume fraction φ = 0.11, particle radius R = 1.25 μm, relative permeability of particles μ_p = 10³, relative permeability of matrix μ_e = 1, saturation magnetization M_s = 1.7 × 10⁶ A/m.

(a) Variation of mean column length L = 10, 20, …, 100 (step 10) for each standard deviation σ = 3, 6, 9 (corresponding to variances σ² = 9, 36, 81), with column width b = 2, external field H₀ = 1 MA/m, and shear strain γ = 0.003.

(b) Variation of column width b = 2, 3, 4, 5, 6, 7, with standard deviation σ = 9. Compute two series:
   - The experimental pairs (L, b) = (10,2), (20,3), (30,4), (40,5).
   - A continuous curve with b ranging from 2 to 7 while keeping the mean length fixed at L = 30.

(c) Variation of external magnetic field H₀ = 0.1, 0.2, …, 1.0 MA/m (step 0.1) for three shear strains γ = 0.001, 0.003, 0.005, with L = 30, σ = 3, and b = 2.

Store all ΔG values in a CSV file at /app/outputs/results.csv. The file must contain exactly seven columns: condition_id (a string that identifies the parameter set), L (integer), sigma (integer, the standard deviation), b (integer), H₀ (float, in MA/m), gamma (float), Delta_G (float, in MPa). Include one row per computed condition.

## Assets

- Python standard libraries and numpy/scipy: numpy, scipy

## Workflow steps

### Step 1: Model parameters and geometry setup
- Role: process
- Action: Define the fixed physical constants (μ0, μe, μp, Ms, particle radius, particle volume Vp, volume fraction φ) and generate the parameter grids for mean column length L, standard deviation σ, column width b, external magnetic field H0, and shear strain γ as specified in the reproduction target.
- Evidence: none

### Step 2: Self-consistent dipole moment and macroscopic shear modulus computation
- Role: process
- Action: For each (l,b,γ) combination compute the inter-particle dipole field kernel sum Σg(x,y,z) for the BCT column geometry (direct summation or polynomial fitting) to obtain the local field factor f(l,b,γ) and its shear derivative k(l,b,γ). Solve the self-consistent equation derived from the Fröhlich–Kennelly magnetization law for the particle dipole moment component p_z. Aggregate over the Gaussian column-length distribution to compute the effective susceptibility χ_eff, its shear derivative ∂χ_eff/∂γ, and the field-induced shear modulus ΔG for every (L,σ,b,H0,γ) parameter set.
- Evidence: `/app/outputs/computation_log.txt`

### Step 3: Generate results CSV
- Role: scored (load-bearing)
- Action: Write the computed field-induced shear modulus ΔG (in MPa) for all parameter combinations into a file named results.csv under /app/outputs. The file must contain columns: condition_id (string identifier), L (int), sigma (int, the standard deviation, not the variance), b (int), H0 (float, MA/m), gamma (float), Delta_G (float, MPa). Include all rows for the three parameter sets: (a) L=10,20,...,100 for σ=3,6,9, with b=2, H0=1 MA/m, γ=0.003; (b) b=2..7 with σ=9, including the experimental (L,b) pairs (10,2),(20,3),(30,4),(40,5) and a continuous curve L=30; (c) H0=0.1..1.0 MA/m (step 0.1) for γ=0.001,0.003,0.005, with L=30,σ=3,b=2.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Columns: condition_id (str), L (int), sigma (int), b (int), H0 (float, MA/m), gamma (float), Delta_G (float, MPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Field-induced shear modulus ΔG computed from the Gaussian distribution model for the specified parameter sweeps. The checker will recompute ΔG independently and compare values within predefined tolerances.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `L`, `sigma`, `b`, `H0`, `gamma`, `Delta_G`
  - `units`:
    - `H0`: MA/m
    - `Delta_G`: MPa

Notes: The agent must implement the complete model as described in the workflow steps. All input constants are public and no external data are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "L",
          "sigma",
          "b",
          "H0",
          "gamma",
          "Delta_G"
        ],
        "units": {
          "H0": "MA/m",
          "Delta_G": "MPa"
        }
      },
      "description": "Field-induced shear modulus ΔG computed from the Gaussian distribution model for the specified parameter sweeps. The checker will recompute ΔG independently and compare values within predefined tolerances."
    }
  ],
  "notes": "The agent must implement the complete model as described in the workflow steps. All input constants are public and no external data are required."
}
```

## How you are scored
Your submitted results.csv will be evaluated by a hidden verifier that runs after you finish. The verifier independently computes the field‑induced shear modulus ΔG for every condition using its own implementation of the same model (without relying on your code). It compares your reported ΔG values to its computed values, accepting small deviations that are reasonable for different numerical implementations.

In addition, the verifier checks that your results satisfy the physically expected trends: ΔG should increase with mean column length L, decrease with column width b, increase with external magnetic field H₀, and decrease with shear strain γ. The final reward combines the numerical agreement and the trend consistency; both are needed for a high score. Reporting the correct file format and including all required rows are prerequisites before value comparisons are performed.
