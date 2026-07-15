# Gibbs free energy analysis for bainitic transformations in Cu-Zn-Al

## Problem background
Cu-Zn-Al shape memory alloys exhibit a bainitic transformation whose mechanism — diffusional or shear — has been actively debated. Resolving this debate requires a thermodynamic feasibility analysis: computing the Gibbs free energy changes (driving forces) of the possible transformation paths. This task calculates the driving forces for the non‑diffusional shear β'→α', the diffusional β'→β₁'+α reaction, the disordered-to-ordered β→α transition, and the subsequent α→α' ordering transition, all for the alloy 69.33 Cu–26.67 Zn–4.00 Al (at.%), to determine which paths are thermodynamically allowed.

## Approach

### Thermodynamic parameters

All constants are given in SI units; energy values in J·mol⁻¹ unless otherwise specified. Use the gas constant R = 8.314 J·mol⁻¹·K⁻¹.

#### Chemical interchange energies (W in K, multiply by R to obtain J·mol⁻¹·K⁻¹)
- W_CuZn^(1) = 955
- W_CuZn^(2) = 535
- W_CuAl^(1) = 1345
- W_CuAl^(2) = 825
- W_ZnAl^(1) = -50
- W_ZnAl^(2) = 200
- W_CuZn^α = 582
- W_CuAl^α = 1459
- W_ZnAl^α = 0

#### Interaction energies (E in kJ·mol⁻¹)
- E_CuZn^α = -29.047
- E_CuZn^β = -43.014
- E_CuAl^α = -72.781
- E_CuAl^β = -65.306
- E_ZnAl^α = 0
- E_ZnAl^β = -3.326

#### Lattice stability functions ΔG_i^(β→α) (J·mol⁻¹)
- ΔG_Cu1^(β→α)(T) = 7232.40 + 3.14348·T
- ΔG_Cu2^(β→α)(T) = -1221.81 + 0.11418·T + 8.837×10⁻⁵·T²
- ΔG_Zn^(β→α)(T) = -325.08 - 0.79713·T - 8.1704×10⁻⁴·T²
- ΔG_Al^(β→α)(T) = 8212.38 + 2.75113·T

For the ternary, use the weighted average for Cu:
  ΔG_Cu^(β→α) = (X_Zn·ΔG_Cu1 + X_Al·ΔG_Cu2) / (X_Zn + X_Al)

#### Alloy compositions

Main alloy (for β→α, shear driving force, etc.):
  X_Cu = 0.6933, X_Zn = 0.2667, X_Al = 0.0400

For the diffusional reaction β'→β₁'+α:
  X_Zn^β' = 0.2477,   X_Al^β' = 0.0900   (→ X_Cu^β' = 0.6623)
  X_Zn^β₁' = 0.2480,  X_Al^β₁' = 0.0902 (→ X_Cu^β₁' = 0.6618)
  X_Zn^α = 0.2218,    X_Al^α = 0.0738   (→ X_Cu^α = 0.7044)

#### Ordering degree η₁
For β' ordering: (η₁/0.32)² + (T/770)⁵ = 1  →  η₁ = 0.32·√[1 – (T/770)⁵]   (T < 770 K)
For α→α' ordering: η₁ = 0.20·√[1 – (T/770)⁵]

#### Nearest-/next-nearest coordination numbers
Z₁ = 8, Z₂ = 6

### Key thermodynamic expressions

#### Regular solution free energy of a phase φ (disordered)
G^φ(T) = Σ_i X_i^φ G_i^φ(T) + R T Σ_i X_i^φ ln X_i^φ + Σ_{i<j} E_ij^φ X_i^φ X_j^φ

where G_i^φ is the free energy of pure element i in phase φ. For the calculations of this task, set the standard free energy of the pure β‑phase elements to zero:
  G_Cu^β = 0, G_Zn^β = 0, G_Al^β = 0
Then G_i^α = ΔG_i^(β→α)(T)   [using the weighted average for Cu].

#### Ordering internal energy contribution ΔU^(β→β') (J·mol⁻¹)
ΔU^(β→β') = 0.5·R·η₁² · [ (X_Zn/(X_Zn+X_Al))·(Z₂·W_CuZn^(2) – Z₁·W_CuZn^(1))
                         + (X_Al/(X_Zn+X_Al))·(Z₂·W_CuAl^(2) – Z₁·W_CuAl^(1))
                         – (X_Zn·X_Al/(X_Zn+X_Al)²)·(Z₂·W_ZnAl^(2) – Z₁·W_ZnAl^(1)) ]
where the W values are in K and are multiplied by R to convert to J·mol⁻¹. (N₀·k_B = R)

ΔU^(α→α') (J·mol⁻¹):
ΔU^(α→α') = 2·R·η₁² · ( – X_Zn/(X_Zn+X_Al)·W_CuZn^α
                         – X_Al/(X_Zn+X_Al)·W_CuAl^α
                         + (X_Zn·X_Al/(X_Zn+X_Al)²)·W_ZnAl^α )

#### Ordering free energy ΔG^(β→β') (full, including configurational entropy)
ΔG^(β→β') = ΔU^(β→β') – (R·T / (2·x)) · S_conf

where x is a short‑range order correction factor for the ternary:
  x = (X_Zn·x_CuZn + X_Al·x_CuAl) / (X_Zn + X_Al)
with x_CuZn = 0.67, x_CuAl = 0.78.

The configurational entropy term S_conf (dimensionless) is:
  S_conf = 2·X_Cu ln X_Cu + 2·(1–X_Cu) ln(1–X_Cu)
         – (η₁ + X_Cu) ln(η₁ + X_Cu)
         – (1 – X_Cu – η₁) ln(1 – X_Cu – η₁)
         – (η₁ + 1 – X_Cu) ln(η₁ + 1 – X_Cu)
         – (X_Cu – η₁) ln(X_Cu – η₁)

(If any argument is ≤ 0, set the term to 0; this only occurs when η₁ = 0).

ΔG^(β₁→β₁') uses the same expression with the composition X^β₁'.

#### Free energy of the ordered phases
G^β' = G^β + ΔG^(β→β')
G^β₁' = G^β₁ + ΔG^(β₁→β₁')

G^α is the disordered α free energy (Eq. regular solution).
ΔG^(α→α') is computed from the expression (22) that includes the same S_conf with the α composition and the internal energy part ΔU^(α→α') as above:

ΔG^(α→α') = ΔU^(α→α') – (R·T / (2·x_α)) · S_conf(α)

where x_α uses the α composition and the same x_CuZn, x_CuAl values.

#### Driving forces to compute
1. Shear: ΔG^(β'→α') = –ΔU^(β→β') + ΔG^(β→α) + ΔU^(α→α')
   Here ΔG^(β→α) is evaluated for the main alloy composition using the regular solution expression with ΔG_i^(β→α) and interaction energies E^β, E^α.

2. Disordered β→α: ΔG^(β→α) computed with the same regular solution expression, using the main alloy composition.

3. Diffusional: ΔG^(β'→β₁'+α) = G^α + (X_Zn^β' – X_Zn^α)/(X_Zn^β₁' – X_Zn^α)·(G^β₁ – G^α) – G^β'
   where G^β₁ = G^β₁'(T) – ΔG^(β₁→β₁') is the disordered free energy at composition β₁'.

4. α ordering: ΔG^(α→α') as defined above, using the α composition (X_Zn^α, X_Al^α).

All Gibbs energies are in J·mol⁻¹. Convert E values from kJ·mol⁻¹ to J·mol⁻¹. The computed driving forces are evaluated at ten evenly spaced temperatures between 300 and 750 K.

## Reproduction target
Compute the four Gibbs free energy changes ΔG^(β'→α'), ΔG^(β→α), ΔG^(β'→β₁'+α), and ΔG^(α→α') at the temperatures T = 300, 350, 400, 450, 500, 550, 600, 650, 700, 750 K. Output the values in J·mol⁻¹ to driving_forces.csv with the columns specified in the step contract. Then perform a least‑squares cubic regression on the ΔG^(β'→α') values to obtain the coefficients a₀, a₁, a₂, a₃ in ΔG^(β'→α')(T) ≈ a₀ + a₁·T + a₂·T² + a₃·T³, and write them to polynomial_coefficients.json.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Assemble thermodynamic parameters and define model equations
- Role: process
- Action: Implement the GBW ordering model and regular solution model for the β→β', α→α', β→α, and β'→β₁'+α transformations as detailed in the Approach section. Hardcode all thermodynamic parameters listed there and implement the provided equations for ΔU^(β→β'), ΔU^(α→α'), ΔG^(β→α), ΔG^(β→β') with the configurational entropy term, and the free energies of ordered/disordered phases.
- Evidence: `/app/outputs/parameters_log.txt`

### Step 2: Compute driving forces at tabulated temperatures
- Role: scored (load-bearing)
- Action: Using the implemented model, numerically evaluate the four Gibbs free energy changes (ΔG^(β'→α'), ΔG^(β→α), ΔG^(β'→β₁'+α), ΔG^(α→α')) at ten evenly spaced temperatures T = 300, 350, 400, 450, 500, 550, 600, 650, 700, 750 K. For the diffusional reaction β'→β₁'+α, adopt the composition values from the paper (X_Zn^{β'}=0.2477, X_Al^{β'}=0.0900, X_Zn^{β₁'}=0.2480, X_Al^{β₁'}=0.0902, X_Zn^{α}=0.2218, X_Al^{α}=0.0738) and compute the full ordering free energies with configurational entropy. Write the results to driving_forces.csv.
- Output file: `/app/outputs/driving_forces.csv`
- Format: csv
- Contract: T:float, DG_beta'_to_alpha':float, DG_beta_to_alpha:float, DG_beta'_to_beta1'_plus_alpha:float, DG_alpha_to_alpha':float. 10 rows, one per temperature.
- Scoring: scored by hidden verifier

### Step 3: Fit cubic polynomial for ΔG^(β'→α')
- Role: scored
- Action: Perform a least-squares cubic regression on the ΔG^(β'→α') values from driving_forces.csv to obtain coefficients a0, a1, a2, a3 such that ΔG^(β'→α')(T) ≈ a0 + a1·T + a2·T² + a3·T³. Write the coefficients to polynomial_coefficients.json.
- Output file: `/app/outputs/polynomial_coefficients.json`
- Format: json
- Contract: object with keys: constant (float), T (float), T2 (float), T3 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/driving_forces.csv`
- `/app/outputs/polynomial_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### driving_forces.csv
- path: `/app/outputs/driving_forces.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Driving forces for the four transformations at ten temperatures. Each value will be checked against the paper's published regression formulas within a small tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `DG_beta'_to_alpha'`, `DG_beta_to_alpha`, `DG_beta'_to_beta1'_plus_alpha`, `DG_alpha_to_alpha'`
  - `units`:
    - `T`: K
    - `DG_beta'_to_alpha'`: J·mol⁻¹
    - `DG_beta_to_alpha`: J·mol⁻¹
    - `DG_beta'_to_beta1'_plus_alpha`: J·mol⁻¹
    - `DG_alpha_to_alpha'`: J·mol⁻¹

### polynomial_coefficients.json
- path: `/app/outputs/polynomial_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Cubic polynomial coefficients for ΔG^(β'→α')(T). Units: constant in J·mol⁻¹, T in J·mol⁻¹·K⁻¹, T2 in J·mol⁻¹·K⁻², T3 in J·mol⁻¹·K⁻³. Compared to Eq. (11) with small component tolerances.
- schema:
  - `type`: object
  - `required`:
    - `constant`: float
    - `T`: float
    - `T2`: float
    - `T3`: float

Notes: All computations use explicit numeric parameters extracted from the paper. No gold values are provided to the agent. The hidden checker computes reference driving forces from the paper's regression formulas and compares with absolute tolerance 5 J·mol⁻¹; polynomial coefficients are compared component-wise with tolerances (constant ±0.1, T ±0.001, T² ±1e-5, T³ ±1e-7).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "driving_forces.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "DG_beta'_to_alpha'",
          "DG_beta_to_alpha",
          "DG_beta'_to_beta1'_plus_alpha",
          "DG_alpha_to_alpha'"
        ],
        "units": {
          "T": "K",
          "DG_beta'_to_alpha'": "J·mol⁻¹",
          "DG_beta_to_alpha": "J·mol⁻¹",
          "DG_beta'_to_beta1'_plus_alpha": "J·mol⁻¹",
          "DG_alpha_to_alpha'": "J·mol⁻¹"
        }
      },
      "description": "Driving forces for the four transformations at ten temperatures. Each value will be checked against the paper's published regression formulas within a small tolerance."
    },
    {
      "file": "polynomial_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "constant": "float",
          "T": "float",
          "T2": "float",
          "T3": "float"
        }
      },
      "description": "Cubic polynomial coefficients for ΔG^(β'→α')(T). Units: constant in J·mol⁻¹, T in J·mol⁻¹·K⁻¹, T2 in J·mol⁻¹·K⁻², T3 in J·mol⁻¹·K⁻³. Compared to Eq. (11) with small component tolerances."
    }
  ],
  "notes": "All computations use explicit numeric parameters extracted from the paper. No gold values are provided to the agent. The hidden checker computes reference driving forces from the paper's regression formulas and compares with absolute tolerance 5 J·mol⁻¹; polynomial coefficients are compared component-wise with tolerances (constant ±0.1, T ±0.001, T² ±1e-5, T³ ±1e-7)."
}
```

## How you are scored
A hidden verifier independently recomputes reference driving forces (from the paper‑published regression formulas) and polynomial coefficients. Each scored artifact (driving_forces.csv and polynomial_coefficients.json) is compared to its reference, and the resulting scores are combined with equal weight to form the final reward. Reporting the correct numbers from the paper is not sufficient; the artifacts must be the result of executing the full thermodynamic computation described in the workflow steps.
