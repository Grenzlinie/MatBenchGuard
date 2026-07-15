# Initial Slope of Glass Transition Temperature from Stochastic Agglomeration Theory

## Problem background
Glass transition temperature (T_g) in inorganic network glasses depends on chemical composition. Understanding the initial slope of T_g with respect to modifier concentration at zero fraction is important for predicting glass properties. The Stochastic Agglomeration Theory provides a theoretical framework that accounts for local bonding arrangements and agglomeration pathways to derive a relationship between T_g and composition in binary covalent glasses.

## Approach
The Stochastic Agglomeration Theory models glass formation as a dendritic growth of clusters built from two types of atoms, A and B, with coordination numbers m_A and m_B. At each growth step, edge sites (type x for A-like and y for B-like) are saturated by incoming atoms. The process is described by a 2×2 transition matrix M whose entries are probabilities of site type conversion after one layer, depending on the modifier concentration c (fraction of B atoms) and two Boltzmann-factor ratios ξ and μ:

M_xx = m_A (1-c) ξ / [m_A (1-c) ξ + m_B c]
M_xy = m_A (1-c)      / [m_A (1-c) + m_B c μ]
(and M_yx = 1 - M_xx, M_yy = 1 - M_xy).

After many layers the distribution of site types approaches the stationary eigenvector of M (eigenvalue 1). For a homogeneous bulk glass, the stationary probability of y‑sites must equal the overall modifier concentration c, i.e. p_y = c. This condition leads to the equation

c = M_yx / (M_xy + M_yx)   (1)

where M_yx = 1 - M_xx and M_xy = 1 - M_yy, and
M_yy = m_B c μ / [m_A (1-c) + m_B c μ].

The temperature enters through ξ and μ, which can be expressed using the pure‑component glass transition temperatures T_g0 (c=0) and T_g1 (c=1) and the coordination numbers:

ξ(T) = (m_B / m_A)^(T_g0 / T)       (2)
μ(T) = (m_A / m_B)^(T_g1 / T)       (3)

Equation (1) defines the glass transition temperature T_g for a given concentration c. To obtain the initial slope dT_g/dc at c→0 you need to:

- Solve the nonlinear equation (1) for T over a small range of c (e.g. c ∈ [0.0001, 0.0002]) using a root‑finding method.
- Compute the numerical derivative ΔT/Δc and extrapolate to c=0.

The parameters for the two binary glasses you must analyze are:

- Case 1 (general case): m_A = 2, m_B = 3, T_g0 = 318 K, T_g1 = 452 K.
- Case 2 (equal‑coordination case): m_A = 2, m_B = 2, T_g0 = 318 K, T_g1 = 240 K.

## Reproduction target
Implement the Stochastic Agglomeration Model as described in the Approach. For each of the two parameter sets, solve the stationary condition (1) numerically to obtain T_g(c) and compute the initial slope dT_g/dc at c=0. Write the slope value for Case 1 to `/app/outputs/slope_case1.txt` and for Case 2 to `/app/outputs/slope_case2.txt`. Additionally, document the derivation steps and intermediate results (e.g., the equation solved, the T_g values for the small c steps, the numerical derivative) in a short evidence file `/app/outputs/model_derivation.txt`.

## Assets
No external datasets, models, or pre-built tools are required. The computation can be performed using standard mathematical functions (exponential, logarithm) available in Python's built-in math module or through NumPy. No network access is needed beyond installing any required packages.

## Workflow steps

### Step 1: Implement Stochastic Agglomeration Model (process)
- Role: process
- Action: Write code that constructs the transition matrix M, formulates the stationary eigenvector condition (Equation (1)), and expresses ξ(T) and μ(T) via (2) and (3). For each of the two parameter sets, solve the resulting nonlinear equation for T_g(c) at a few small c values, and compute the numerical slope dT_g/dc. Record the approach and intermediate values.
- Evidence: `/app/outputs/model_derivation.txt`

### Step 2: Output slope for general case (m_A ≠ m_B)
- Role: scored (load-bearing)
- Action: From the previous step, write the computed initial slope for Case 1 (m_A=2, m_B=3, T_g0=318 K, T_g1=452 K) to the output file.
- Output file: `/app/outputs/slope_case1.txt`
- Format: txt
- Contract: A single floating-point number (units: K).
- Scoring: scored by hidden verifier

### Step 3: Output slope for equal-valence case (m_A = m_B)
- Role: scored (load-bearing)
- Action: From the previous step, write the computed initial slope for Case 2 (m_A=2, m_B=2, T_g0=318 K, T_g1=240 K) to the output file.
- Output file: `/app/outputs/slope_case2.txt`
- Format: txt
- Contract: A single floating-point number (units: K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_derivation.txt`
- `/app/outputs/slope_case1.txt`
- `/app/outputs/slope_case2.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### slope_case1.txt
- path: `/app/outputs/slope_case1.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The computed initial slope of glass transition temperature with respect to modifier concentration for a binary glass where m_A != m_B, using the Stochastic Agglomeration Theory formula.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing dT_g/dc at c=0 for the general case.
  - `units`:
    - `value`: K

### slope_case2.txt
- path: `/app/outputs/slope_case2.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The computed initial slope of glass transition temperature for a binary glass where m_A = m_B, using the limit of the Stochastic Agglomeration Theory formula.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing dT_g/dc at c=0 for the equal-valence case.
  - `units`:
    - `value`: K

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "slope_case1.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing dT_g/dc at c=0 for the general case.",
        "units": {
          "value": "K"
        }
      },
      "description": "The computed initial slope of glass transition temperature with respect to modifier concentration for a binary glass where m_A != m_B, using the Stochastic Agglomeration Theory formula."
    },
    {
      "file": "slope_case2.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing dT_g/dc at c=0 for the equal-valence case.",
        "units": {
          "value": "K"
        }
      },
      "description": "The computed initial slope of glass transition temperature for a binary glass where m_A = m_B, using the limit of the Stochastic Agglomeration Theory formula."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be scored by a hidden verifier that recomputes the expected slope for each case from the given parameters using the same expressions. It will compare your output values to the reference values with a small relative tolerance. Full credit requires that both slope_case1.txt and slope_case2.txt match the reference within tolerance; a partially correct submission (only one correct file) may receive partial credit.
