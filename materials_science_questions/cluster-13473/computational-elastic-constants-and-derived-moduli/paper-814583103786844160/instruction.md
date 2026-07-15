# Lattice-Statics Macroscopic Properties of Graphene via Mie Potential

## Problem background
Accurately estimating graphene's elastic moduli from atomistic interaction potentials is challenging. Different potentials yield widely varying values for Young's modulus and Poisson's ratio, often breaking the in-plane isotropy expected for a two-dimensional hexagonal crystal. A lattice‑statics approach using a simple pair potential can compute the elastic constants and equilibrium spacing, but the potential parameters must be chosen to reproduce experimental observations. One candidate is a nonsymmetric Mie pair potential, where the repulsive part acts between all atom pairs and the attractive part acts only along the sp² bonding directions. This task implements the lattice‑statics procedure to compute the macroscopic (infinite‑size) limits of the interatomic spacing, inner displacement parameter, dimensionless Young's modulus coefficient, and Poisson's ratio for two specific exponent pairs of the Mie potential.

## Approach
The method begins by constructing ideal hexagonal graphene samples parameterized by the number of atoms on a side, N. For each sample size, the atom positions are fixed according to the perfect honeycomb lattice, yielding dimensionless interatomic vectors and distances relative to the unknown spacing a. The neighbor set for attractive interactions is defined according to sp² hybridization: only pairs connected by covalent bonds (the three nearest neighbors) contribute to the attractive term, while the repulsive part includes all pairwise interactions. 

For a given pair of Mie exponents (m, n), the equilibrium dimensionless spacing a/α is obtained from a closed‑form expression that balances the repulsive and attractive summations over the sample. Repeating this for a range of N gives a sequence that converges toward a macroscopic limit. The limit (a∞/α) is extracted by fitting the N-dependent data to an appropriate asymptotic function. 

The inner displacement parameter δ, which corrects the elastic constants for the non‑affine relaxation of the lattice under strain, is computed for each N using the same structural arrays and exponent pair. Its macroscopic limit δ∞ is extracted by an analogous fitting procedure. 

With the equilibrium spacing and inner displacement, the elastic stiffness tensor components C₁₁₁₁, C₁₁₂₂, C₁₂₁₂ are evaluated for each N using analytic second‑derivative formulas that sum over the interatomic vectors. From these components, the macroscopic (N→∞) dimensionless Young's modulus coefficient E∞·α²/β and Poisson's ratio ν∞ are derived. The entire pipeline repeats for both exponent sets (m=6,n=5) and (m=5,n=3), and all four macroscopic quantities per set are collected into a single scored JSON file.

## Reproduction target
Implement the lattice‑statics procedure described above for hexagonal graphene samples. For each of the two Mie exponent pairs (m=6, n=5) and (m=5, n=3), compute the following four macroscopic (infinite‑size) dimensionless quantities:

- a_inf_div_alpha: the limiting equilibrium interatomic spacing divided by the pair‑potential length scale α.
- delta_inf: the limiting inner displacement parameter.
- E_inf_div_beta_alpha2: the limiting Young's modulus coefficient (E∞) divided by β/α², where β is the potential well depth.
- nu_inf: the limiting Poisson's ratio.

Compile all results into a single JSON file `/app/outputs/elastic_properties.json` with the structure: an object containing an array `"sets"`, where each element is an object with keys `"m"`, `"n"`, `"a_inf_div_alpha"`, `"delta_inf"`, `"E_inf_div_beta_alpha2"`, and `"nu_inf"`. The JSON must include exactly two entries, one for each exponent pair. The numerical values are checked against reference limits by the verifier.

## Assets

- Python with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Generate hexagonal sample geometries
- Role: process
- Action: Construct ideal hexagonal graphene samples for a range of side atom counts N (e.g., N from 2 to 20). Compute the dimensionless interatomic vectors b_ij = R_ij / a and distances b_ij for the perfect lattice, and define the neighbour set S_i for attractive interactions according to sp² hybridization. This step prepares the structural arrays used by all subsequent calculations.
- Evidence: `/app/outputs/sample_geometry.pkl`

### Step 2: Compute equilibrium spacing a/α versus N
- Role: process
- Action: For each N and for each exponent pair (m=6,n=5) and (m=5,n=3), evaluate the closed‑form expression for the dimensionless equilibrium spacing a/α using the b_ij distances and the Mie exponents. Store the (N, a/α) data for subsequent fitting.
- Evidence: `/app/outputs/a_alpha_sequence.csv`

### Step 3: Fit a/α and extract macroscopic limit a_inf/α
- Role: process
- Action: Fit the (N, a/α) data for each exponent pair to the function y = c*(x - x0)^k + b with k fixed to -1, using least squares. Extract the horizontal asymptote b as the macroscopic limit a_inf/α. Write the fitted parameters including a_inf/α to a file.
- Evidence: `/app/outputs/a_inf_fit.json`

### Step 4: Compute inner displacement δ versus N
- Role: process
- Action: For each N and each (m,n) pair, compute the dimensionless inner displacement parameter δ that corrects elastic constants, using the appropriate lattice‑relaxation procedure. Store the (N, δ) data.
- Evidence: `/app/outputs/delta_sequence.csv`

### Step 5: Fit δ and extract macroscopic limit δ_inf
- Role: process
- Action: Fit the δ(N) data to an appropriate asymptotic model (e.g., same functional family as step 3) and extract the horizontal asymptote as the macroscopic limit δ_inf. Write the fitted δ_inf values.
- Evidence: `/app/outputs/delta_inf_fit.json`

### Step 6: Compute elastic stiffness tensor components
- Role: process
- Action: For each N and each (m,n) pair, compute the elastic stiffness tensor components C_1111, C_1122, C_1212 using the analytic second‑derivative formulas that involve summations over b_ij, the exponents m,n, the equilibrium spacing a/α, and the inner displacement correction δ. Store the component data for each N.
- Evidence: `/app/outputs/C_components.npz`

### Step 7: Derive macroscopic elastic moduli and compile results
- Role: scored (load-bearing)
- Action: From the C_ijkl vs N data, derive the macroscopic (infinite‑size) values: dimensionless Young’s modulus coefficient E_inf α²/β and Poisson’s ratio ν_inf. Combine with the previously obtained a_inf/α and δ_inf. Assemble all four quantities for both Mie exponent sets (m=6,n=5) and (m=5,n=3) into a single JSON file.
- Output file: `/app/outputs/elastic_properties.json`
- Format: json
- Contract: { "sets": [ { "m": integer, "n": integer, "a_inf_div_alpha": float, "delta_inf": float, "E_inf_div_beta_alpha2": float, "nu_inf": float } ] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_properties.json
- path: `/app/outputs/elastic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single JSON file containing the four macroscopic limit quantities for both Mie exponent pairs (m=6,n=5) and (m=5,n=3). The checker reads each value, compares it to the paper's reported values within a hidden tolerance, and awards full score if all values fall within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `sets`: array of objects, each with keys m, n, a_inf_div_alpha, delta_inf, E_inf_div_beta_alpha2, nu_inf
  - `items`:
    - `type`: object
    - `required_keys`: `m`, `n`, `a_inf_div_alpha`, `delta_inf`, `E_inf_div_beta_alpha2`, `nu_inf`
  - `required_columns`:
  - `units`:
    - `a_inf_div_alpha`: dimensionless (ratio of equilibrium spacing to pair-potential length scale)
    - `delta_inf`: dimensionless (inner displacement parameter)
    - `E_inf_div_beta_alpha2`: dimensionless coefficient (Young's modulus divided by β/α²)
    - `nu_inf`: dimensionless (Poisson's ratio)

Notes: The experimental values used for fitting (experimental lattice constant a^exp, experimental Young's modulus E^2D) are not required as input; the task produces dimensionless quantities that are independent of α and β. The hidden gold values are the paper's reported macroscopic limits for the two exponent sets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "sets": "array of objects, each with keys m, n, a_inf_div_alpha, delta_inf, E_inf_div_beta_alpha2, nu_inf"
        },
        "items": {
          "type": "object",
          "required_keys": [
            "m",
            "n",
            "a_inf_div_alpha",
            "delta_inf",
            "E_inf_div_beta_alpha2",
            "nu_inf"
          ]
        },
        "required_columns": [],
        "units": {
          "a_inf_div_alpha": "dimensionless (ratio of equilibrium spacing to pair-potential length scale)",
          "delta_inf": "dimensionless (inner displacement parameter)",
          "E_inf_div_beta_alpha2": "dimensionless coefficient (Young's modulus divided by β/α²)",
          "nu_inf": "dimensionless (Poisson's ratio)"
        }
      },
      "description": "Single JSON file containing the four macroscopic limit quantities for both Mie exponent pairs (m=6,n=5) and (m=5,n=3). The checker reads each value, compares it to the paper's reported values within a hidden tolerance, and awards full score if all values fall within tolerance."
    }
  ],
  "notes": "The experimental values used for fitting (experimental lattice constant a^exp, experimental Young's modulus E^2D) are not required as input; the task produces dimensionless quantities that are independent of α and β. The hidden gold values are the paper's reported macroscopic limits for the two exponent sets."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that focuses primarily on the final `elastic_properties.json`. The verifier reads the eight numerical values (four per exponent set) and compares each to a reference value using pre‑defined tolerances. A value that falls within tolerance earns full credit for that quantity; values outside tolerance receive reduced or zero credit. The total reward is a weighted sum over all quantities, with the final JSON carrying the majority of the weight.

In addition, the verifier may perform lightweight structural checks on intermediate evidence files (e.g., that expected CSV or NPZ files exist and have plausible shapes), but those checks carry only a small fraction of the total score. The primary scoring is based on how accurately your computed macroscopic limits match the hidden references. The tolerances account for differences in implementation details and finite‑size fitting quality, so a correctly implemented pipeline will achieve a high score.
