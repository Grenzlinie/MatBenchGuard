# Thermodynamic clustering of defects in highly lattice-mismatched ZnBVI-rich alloys

## Problem background
Highly lattice-mismatched semiconductor alloys suffer from large internal strains and a diversity of non-identical clusters. Zinc blende ZnBVI-rich CdxZn1−xOyBVI1−y (with BVI = S, Se, Te) are promising hosts where identical 4O10Cd clusters — oxygen tetrahedrons surrounded by Cd atoms — may form and significantly reduce these strains. A thermodynamic model has been proposed to determine the equilibrium cluster order parameters and to quantify the resulting strain energy reduction. The central question is whether such clusters are thermodynamically stable under dilute Cd and O conditions in ZnS-, ZnSe-, and ZnTe-rich matrices, and by what factor the internal strain energy can be decreased when all mismatched atoms occupy 4O10Cd clusters.

## Approach
The approach is a free-energy minimization over two cluster order parameters: α (fraction of oxygen atoms in 4O10Cd clusters) and β (fraction in 1O4Cd clusters). The free energy per unit cell area is written as f = uB + uIS − T s. The bond energy term uB contains a single host-dependent bond-energy parameter ΔuB that captures the chemical preference between Cd−O / Zn−BVI and Cd−BVI / Zn−O bonds. The internal strain energy uIS is a linear combination of deformation energies of isolated Cd atoms, isolated O atoms, 1O4Cd clusters, and 4O10Cd clusters; these deformation energies are known constants for each host matrix. The configurational entropy s is derived from the combinatorial arrangements of isolated atoms and clusters on the alloy sublattices. At each temperature T, the free energy is numerically minimized with respect to α and β, yielding the equilibrium cluster order parameters. The internal strain energy reduction factor is then obtained by evaluating uIS in the fully clustered state (α = 1, β = 0) and in the fully isolated state (α = 0, β = 0), and taking their ratio. The needed constants are:

- **Bond‑energy parameters** (kJ mol⁻¹): Δu_S^B = −16, Δu_Se^B = −25, Δu_Te^B = +37.
- **Deformation energies** (kJ mol⁻¹) for each host matrix:
  - *ZnS*: u_Cd(ZnS)=24.983, u_O(ZnS)=58.911, u_1O4Cd(ZnS)=58.6102, u_4O10Cd(ZnS)=57.243.
  - *ZnSe*: u_Cd(ZnSe)=6.225, u_O(ZnSe)=77.721, u_1O4Cd(ZnSe)=97.604, u_4O10Cd(ZnSe)=101.656.
  - *ZnTe*: u_Cd(ZnTe)=6.063, u_O(ZnTe)=162.03, u_1O4Cd(ZnTe)=137.02, u_4O10Cd(ZnTe)=389.95.

- **Configurational entropy** (J mol⁻¹ K⁻¹, R = 8.314 J mol⁻¹ K⁻¹):

$$-T s = R T (1-\alpha) y \ln \frac{(1-\alpha) y}{1-\alpha y} + R T (1-y) \ln \frac{1-y}{1-\alpha y}
+ R T \left(x - \frac{10}{4} \alpha y - 4 \beta y\right) \ln \frac{x - \frac{10}{4} \alpha y - 4 \beta y}{1 - \frac{10}{4} \alpha y - 4 \beta y}
+ R T (1-x) \ln \frac{1-x}{1 - \frac{10}{4} \alpha y - 4 \beta y}
+ R T (1-\alpha-\beta) y \ln \frac{1-\alpha-\beta}{1-\alpha}
+ R T \beta y \ln \frac{\beta}{1-\alpha}
+ \frac{1}{10} R T \alpha y \ln \frac{27 \alpha y}{20}
+ \frac{2}{27} R T \ln \frac{20 - 27 \alpha y}{20}$$

The free energy to be minimized is $f = u^B + u^{IS} - T s$. The bond energy term $u^B$ depends on the cluster order parameters only through $\Delta u_{B^{VI}}^B (\alpha+\beta)(1-x)y$; additional composition‑dependent constants do not affect the minimization and can be omitted. The internal strain energy $u^{IS}$ is given by Eq. (3) of the paper using the deformation energies above. At each temperature, minimize $f$ with respect to $\alpha$ and $\beta$ using a numerical optimization routine (e.g., `scipy.optimize.minimize`) with bounds $0 \le \alpha,\beta \le 1$ and the constraints that all atomic fractions remain non‑negative. The compositions are $x = 2.5y$, with $y$ values as specified in the workflow steps.

## Reproduction target
Produce the following four CSV artifacts under `/app/outputs`:

1. `cop_ZnS.csv` — Cluster order parameters α and β for the ZnS-rich alloy at composition x = 2.5 y, y = 5 × 10⁻⁴. Columns: `T (K)` (float), `alpha` (float), `beta` (float). One row per temperature from 273 K to 1073 K in steps of 10 K.
2. `cop_ZnSe.csv` — Same for the ZnSe-rich alloy with y = 3 × 10⁻⁴, x = 2.5 y.
3. `cop_ZnTe.csv` — Same for the ZnTe-rich alloy with y = 2 × 10⁻³, x = 2.5 y.
4. `strain_reduction_factors.csv` — Internal strain energy reduction factor (isolated energy divided by clustered energy) for each matrix. Columns: `matrix` (string, one of ZnS, ZnSe, ZnTe) and `reduction_factor` (float). Exactly three rows.

Use the bond-energy differences and deformation energies given in the workflow steps. The minimization must be performed over the full temperature range with the indicated step size.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute 4O10Cd and 1O4Cd cluster order parameters for ZnS-rich alloy
- Role: scored (load-bearing)
- Action: Implement the thermodynamic free-energy model using the published bond-energy parameter and deformation energies for ZnS matrix. Set composition x=2.5y with y=5e-4. Numerically minimize the free energy with respect to alpha and beta at each temperature from 273 K to 1073 K in steps of 10 K. Output the resulting temperature, alpha, beta values.
- Output file: `/app/outputs/cop_ZnS.csv`
- Format: csv
- Contract: Columns: T (K) (float), alpha (float), beta (float). One row per temperature from 273 K to 1073 K in steps of 10 K.
- Scoring: scored by hidden verifier

### Step 2: Compute 4O10Cd and 1O4Cd cluster order parameters for ZnSe-rich alloy
- Role: scored (load-bearing)
- Action: Using the published bond-energy parameter and deformation energies for ZnSe matrix, set composition x=2.5y with y=3e-4. Minimize the free energy over 273–1073 K (step 10 K) and write T, alpha, beta.
- Output file: `/app/outputs/cop_ZnSe.csv`
- Format: csv
- Contract: Columns: T (K) (float), alpha (float), beta (float). One row per temperature from 273 K to 1073 K in steps of 10 K.
- Scoring: scored by hidden verifier

### Step 3: Compute 4O10Cd and 1O4Cd cluster order parameters for ZnTe-rich alloy
- Role: scored (load-bearing)
- Action: Using the published bond-energy parameter and deformation energies for ZnTe matrix, set composition x=2.5y with y=2e-3. Minimize the free energy over 273–1073 K (step 10 K) and write T, alpha, beta.
- Output file: `/app/outputs/cop_ZnTe.csv`
- Format: csv
- Contract: Columns: T (K) (float), alpha (float), beta (float). One row per temperature from 273 K to 1073 K in steps of 10 K.
- Scoring: scored by hidden verifier

### Step 4: Compute internal strain energy reduction factors for all three matrices
- Role: scored
- Action: For each host matrix (ZnS, ZnSe, ZnTe), use the same deformation energies to compute internal strain energy for the fully clustered state (alpha=1, beta=0) and the fully isolated state (alpha=beta=0) according to the model's strain energy expression. Compute the reduction factor as isolated_energy / clustered_energy. Output a CSV with matrix name and reduction factor.
- Output file: `/app/outputs/strain_reduction_factors.csv`
- Format: csv
- Contract: Columns: matrix (string), reduction_factor (float). Three rows: ZnS, ZnSe, ZnTe.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cop_ZnS.csv`
- `/app/outputs/cop_ZnSe.csv`
- `/app/outputs/cop_ZnTe.csv`
- `/app/outputs/strain_reduction_factors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cop_ZnS.csv
- path: `/app/outputs/cop_ZnS.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: 4O10Cd and 1O4Cd cluster order parameters vs temperature for ZnS-rich alloy. Temperature range 273–1073 K in 10 K steps.
- schema:
  - `type`: table
  - `required_columns`: `T (K)`, `alpha`, `beta`
  - `units`:
    - `T (K)`: K
    - `alpha`: dimensionless
    - `beta`: dimensionless

### cop_ZnSe.csv
- path: `/app/outputs/cop_ZnSe.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: COP vs T for ZnSe-rich alloy. Same temperature range and step.
- schema:
  - `type`: table
  - `required_columns`: `T (K)`, `alpha`, `beta`
  - `units`:
    - `T (K)`: K
    - `alpha`: dimensionless
    - `beta`: dimensionless

### cop_ZnTe.csv
- path: `/app/outputs/cop_ZnTe.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: COP vs T for ZnTe-rich alloy. Same temperature range and step.
- schema:
  - `type`: table
  - `required_columns`: `T (K)`, `alpha`, `beta`
  - `units`:
    - `T (K)`: K
    - `alpha`: dimensionless
    - `beta`: dimensionless

### strain_reduction_factors.csv
- path: `/app/outputs/strain_reduction_factors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Internal strain energy reduction factor (isolated/clustered) for each of the three host matrices.
- schema:
  - `type`: table
  - `required_columns`: `matrix`, `reduction_factor`
  - `units`:
    - `matrix`: string
    - `reduction_factor`: dimensionless

Notes: All scored artifacts are recomputed by the hidden checker using the same thermodynamic model and published input constants. Reference values are obtained by high-precision minimization. Agent outputs must be within tolerance, not perfectly match any specific paper figure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cop_ZnS.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T (K)",
          "alpha",
          "beta"
        ],
        "units": {
          "T (K)": "K",
          "alpha": "dimensionless",
          "beta": "dimensionless"
        }
      },
      "description": "4O10Cd and 1O4Cd cluster order parameters vs temperature for ZnS-rich alloy. Temperature range 273–1073 K in 10 K steps."
    },
    {
      "file": "cop_ZnSe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T (K)",
          "alpha",
          "beta"
        ],
        "units": {
          "T (K)": "K",
          "alpha": "dimensionless",
          "beta": "dimensionless"
        }
      },
      "description": "COP vs T for ZnSe-rich alloy. Same temperature range and step."
    },
    {
      "file": "cop_ZnTe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T (K)",
          "alpha",
          "beta"
        ],
        "units": {
          "T (K)": "K",
          "alpha": "dimensionless",
          "beta": "dimensionless"
        }
      },
      "description": "COP vs T for ZnTe-rich alloy. Same temperature range and step."
    },
    {
      "file": "strain_reduction_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "matrix",
          "reduction_factor"
        ],
        "units": {
          "matrix": "string",
          "reduction_factor": "dimensionless"
        }
      },
      "description": "Internal strain energy reduction factor (isolated/clustered) for each of the three host matrices."
    }
  ],
  "notes": "All scored artifacts are recomputed by the hidden checker using the same thermodynamic model and published input constants. Reference values are obtained by high-precision minimization. Agent outputs must be within tolerance, not perfectly match any specific paper figure."
}
```

## How you are scored
A hidden verifier independently recomputes the reference 4O10Cd cluster order parameter curves and the strain energy reduction factors from the same thermodynamic model and the same input constants, using a high‑precision numerical minimization. It then compares your submitted artifacts to these reference values. For each matrix, the verifier checks that the temperature range and step size are correct and that the values of α, β, and the reduction factor fall within an appropriate tolerance. The tolerance is chosen to absorb legitimate numerical differences between independent implementations while still requiring a valid re‑computation. Each scored artifact contributes to the final reward (a single number between 0 and 1), and submitting the paper‑reported numbers alone is not sufficient — the outputs must pass the tolerance checks against the independently recomputed references.
