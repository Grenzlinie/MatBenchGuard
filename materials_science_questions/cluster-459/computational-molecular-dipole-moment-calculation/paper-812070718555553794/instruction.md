# Molecular Dipole Moment Expansion Coefficient Determination via Weighted Least-Squares Fit

## Problem background
The dipole moment of a diatomic molecule depends solely on the internuclear distance. Away from the equilibrium geometry it is customary to expand the dipole moment as a power series in the displacement coordinate. The expansion coefficients encode the molecule's charge distribution and directly determine the intensities of infrared vibrational transitions and the magnitudes of state-specific dipole moments. This task concerns the determination of the cubic expansion coefficients for carbon monoxide (CO) and hydrogen chloride (HCl) from a set of experimental spectroscopic observables. The observables include transition moments, dipole moments of vibrational states, and Herman–Wallis factors that account for rotation–vibration interaction. By combining these measurements with harmonic-oscillator matrix elements obtained from numerically diagonalized wave functions, one can form a weighted linear least-squares problem whose solution yields the expansion coefficients.

## Approach
The approach consists of three stages.

1. **Rotationless matrix elements.** Using a harmonic‑oscillator basis and the molecular force constants supplied below, the vibrational Hamiltonian matrix is constructed and diagonalised to obtain the perturbed vibrational wavefunctions as linear combinations of harmonic‑oscillator basis functions. From the resulting eigenvectors, the required rotationless matrix elements ⟨v|q^k|v′⟩ are computed for the low‑lying vibrational levels (v, v′ ≤ 3). This follows the standard numerical diagonalisation method: H_{nn'} = (n+1/2) δ_{nn'} + Σ_{k≥3} k_k ⟨n|q^k|n′⟩, with a sufficiently large basis (e.g., 20 functions).

2. **Vibration‑rotation wavefunctions.** For each isotopologue (CO, HCl, DCl) the vibration‑rotation Hamiltonian is diagonalised for a range of rotational quantum numbers J (e.g., 0–5) to obtain the coefficients b_{vn}^{J} that express the perturbed vibration‑rotation states |v,J⟩ in the harmonic‑oscillator basis. The procedure is analogous to stage 1 but includes the rotational term B_e J(J+1) q^2 in the Hamiltonian. From the b coefficients the matrix elements ⟨v′J′|q^k|vJ⟩ are evaluated and stored for the (v,J) levels needed to model the experimental observables (see step 2 description).

3. **Weighted least‑squares fit.** The coefficients p_0…p_3 are determined by a weighted least‑squares fit that simultaneously matches all experimental data: rotationless transition moments R_v^{v′}, state dipole moments μ_v, and Herman–Wallis factors C_v^{v′} and D_v^{v′}. For any trial set of p_k the model predictions are computed as follows:
   - rotationless observables: R_v^{v′} = Σ_k p_k ⟨v|q^k|v′⟩, μ_v = Σ_k p_k ⟨v|q^k|v⟩.
   - vibration‑rotation transition moments: R_{vJ}^{v′J′} = Σ_k p_k ⟨v′J′|q^k|vJ⟩.
   For each vibrational transition, the theoretical Herman–Wallis factors C and D are obtained by evaluating R_{vJ}^{v′J′} for several appropriate rotational branches (or m values) and fitting the squared ratio to the form 1 + C m + D m² (see Eq. 13 of the standard formulation). The same branch conventions (m = –J for P‑branch, m = J+1 for R‑branch) and a small range of |m| (e.g., 1–3) are sufficient.

The fit then minimizes the weighted sum of squared residuals over all data types, using the weights tabulated below. Because the Herman–Wallis contribution depends non‑linearly on p_k, the minimisation may be carried out with a non‑linear least‑squares routine (e.g., scipy.optimize.least_squares) where the residuals are the differences between computed and experimental values, each multiplied by the square root of the weight. Separate fits are performed for CO and for the HCl isotopologue set (combining HCl and DCl data) to obtain one set of coefficients for each molecule.

## Reproduction target
Produce a JSON file containing the fitted dipole moment expansion coefficients p0, p1, p2, p3 (in Debye) for CO and for HCl. The output file must be written to `/app/outputs/fitted_coefficients.json` and have the structure:

```
{
  "CO": {
    "p0": <float>,
    "p1": <float>,
    "p2": <float>,
    "p3": <float>
  },
  "HCl": {
    "p0": <float>,
    "p1": <float>,
    "p2": <float>,
    "p3": <float>
  }
}
```

The fit for HCl must be performed on the combined HCl and DCl data to obtain the coefficients for the HCl dipole moment function.

## Assets

- NumPy: numpy
- SciPy: scipy

## Input Data

### CO experimental data and weights (rotationless observables only)

| Label | Observable type | Value | Weight |
|-------|----------------|-------|--------|
| $R_0^1$ | transition moment | -0.104 | 0.025 |
| $R_0^2$ | transition moment | 0.00653 | 1.0 |
| $R_0^3$ | transition moment | -0.000424 | 290.0 |
| $\mu_0$ | dipole moment | 0.112 | 1.0 |

### CO force constants for the vibrational Hamiltonian

The following constants (in cm$^{-1}$) define the potential energy function used to build the vibrational Hamiltonian. The rotationless matrix elements $\langle v|q^k|v'\rangle$ must be computed by diagonalising the Hamiltonian (see the workflow steps for details).

- $\omega_e = 2169.9191$
- $k_3 = -123.5529$
- $k_4 = 8.7314$
- $k_5 = -0.46782$
- $k_6 = 0.01579$
- $B_e = 1.931241$ (not needed for the rotationless fit, but provided for completeness)

### CO Herman–Wallis factors

| Label     | Type                | Value  | Weight |
|-----------|---------------------|--------|--------|
| C_0¹      | Herman–Wallis C     | 0.0    | 1.0    |
| C_0²      | Herman–Wallis C     | 0.0054 | 0.0625 |
| C_0³      | Herman–Wallis C     | 0.0118 | 0.02   |
| D_0¹      | Herman–Wallis D     | 0.0    | 1.0    |
| D_0²      | Herman–Wallis D     | 0.00004| 0.02   |
| D_0³      | Herman–Wallis D     | 0.00018| 1.0    |

### HCl and DCl experimental data and weights (rotationless observables only)

#### HCl

| Label | Observable type | Value | Weight |
|-------|----------------|-------|--------|
| $R_0^1$ | transition moment | 0.068 | 0.6 |
| $R_0^2$ | transition moment | -0.0080 | 39.0 |
| $R_0^3$ | transition moment | 0.00051 | 0.0 |
| $R_1^2$ | transition moment | 0.0971 | 0.01 |
| $R_2^3$ | transition moment | 0.1187 | 0.01 |
| $\mu_0$ | dipole moment | 1.1085 | 4.0 |
| $\mu_1$ | dipole moment | 1.1390 | 1.0 |
| $\mu_2$ | dipole moment | 1.1685 | 1.0 |

#### DCl

| Label | Observable type | Value | Weight |
|-------|----------------|-------|--------|
| $R_0^1$ | transition moment | 0.0563 | 0.01 |
| $R_0^2$ | transition moment | -0.0050 | 0.01 |
| $R_0^3$ | transition moment | 0.00031 | 0.01 |
| $\mu_0$ | dipole moment | 1.1033 | 4.0 |
| $\mu_1$ | dipole moment | 1.1256 | 1.0 |

### HCl Herman–Wallis factors

| Label     | Type                | Value  | Weight |
|-----------|---------------------|--------|--------|
| C_0¹      | Herman–Wallis C     | −0.026 | 0.25   |
| C_0²      | Herman–Wallis C     | −0.0086| 0.44   |
| C_0³      | Herman–Wallis C     |  0.017 | 0.0    |
| D_0¹      | Herman–Wallis D     | 0.00045| 25.0   |
| D_0²      | Herman–Wallis D     | 0.00041| 25.0   |
| D_0³      | Herman–Wallis D     |  —     | 0      |

### HCI/DCl force constants for the vibrational Hamiltonian

The following constants (in cm$^{-1}$) define the common HCl potential. The same potential applies to both HCl and DCl; the respective matrix elements $\langle v|q^k|v'\rangle$ for each isotopologue must be computed by diagonalising its own vibrational Hamiltonian using these constants, together with the appropriate reduced-mass scaling implicit in the harmonic‑oscillator basis.

- $\omega_c = 2991.8183$
- $k_3 = -299.0935$
- $k_4 = 39.0356$
- $k_5 = -3.88475$
- $k_6 = 0.27635$
- $k_7 = -0.01859$
- $k_8 = 0.00125$
- $B_e = 10.593553$ (not needed for the rotationless fit, but provided for completeness)

## Workflow steps

### Step 1: Compute rotationless matrix elements
- Role: process
- Action: Using the force constants provided for CO, HCl, and DCl, construct the vibrational Hamiltonian matrix in a truncated harmonic‑oscillator basis (e.g., 20 basis functions). Diagonalise it to obtain the eigenvectors a_{vn}. Evaluate the required rotationless matrix elements ⟨v|q^k|v′⟩ for k=0,1,2,3 and the (v,v′) pairs listed below. The Hamiltonian matrix elements are H_{nn'} = (n+1/2)δ_{nn'} + Σ_{k≥3} k_k ⟨n|q^k|n′⟩, where ⟨n|q^k|n′⟩ are the analytic harmonic‑oscillator matrix elements. Use the eigenvector expansion ⟨v|q^k|v′⟩ = Σ_{n,m} a_{vn} a_{v′m} ⟨n|q^k|m⟩. Required pairs: CO – (0,0), (0,1), (0,2), (0,3); HCl – (0,0), (1,1), (2,2), (0,1), (0,2), (0,3), (1,2), (2,3); DCl – (0,0), (1,1), (0,1), (0,2), (0,3).
- Evidence: none

### Step 2: Compute vibration‑rotation wavefunction coefficients b_{vn}^J
- Role: process
- Action: For each isotopologue (CO, HCl, DCl), diagonalise the vibration‑rotation Hamiltonian including the rotational term B_e J(J+1) q^2 for a set of rotational quantum numbers J (e.g., 0–5). This yields coefficients b_{vn}^J that describe the state |v,J⟩ in the harmonic‑oscillator basis. From these coefficients, construct the matrix elements ⟨v′J′|q^k|vJ⟩ (k=0–3) that are needed to evaluate the transition moments entering the Herman–Wallis factors. Save these matrix elements in memory (or an optional evidence file) to be used in step 3.
- Evidence: none (optional: save b‑coefficient tables as an intermediate file if desired)

### Step 3: Non‑linear least‑squares fit of dipole expansion coefficients
- Role: scored (load-bearing)
- Action: Determine p0–p3 by a single weighted non‑linear least‑squares fit that simultaneously matches all experimental data (rotationless transition moments, dipole moments, and Herman–Wallis C and D factors) for the molecule. For a given trial vector p, compute:
   (i) predicted rotationless moments R_v^{v′} = Σ_k p_k ⟨v|q^k|v′⟩,
   (ii) predicted dipole moments μ_v = Σ_k p_k ⟨v|q^k|v⟩,
   (iii) predicted vibration‑rotation transition moments R_{vJ}^{v′J′} = Σ_k p_k ⟨v′J′|q^k|vJ⟩ for the necessary (v,J) pairs,
   (iv) for each vibrational transition, derive the theoretical C and D by computing R_{vJ}^{v′J′} for a few rotational lines (e.g., |m|=1,2,3 for the appropriate P‑ and R‑branches) and fitting the squared ratio to 1 + C m + D m².
   The weighted residuals are obtained by comparing the computed predictions with the experimental values (from the Input Data sections), each multiplied by the square root of the tabulated weight. Minimise the sum of squared residuals over p using a non‑linear least‑squares routine (e.g., scipy.optimize.least_squares). Perform two separate fits: (a) for CO using its rotationless and Herman–Wallis data; (b) for the HCl isotopologue set, using the combined HCl and DCl rotationless data and the HCl Herman–Wallis data (DCl has no Herman–Wallis data). Output the fitted coefficients as described below.
- Output file: `/app/outputs/fitted_coefficients.json`
- Format: json
- Contract: JSON object with top-level keys 'CO' and 'HCl'. Each key holds an object with numeric keys 'p0', 'p1', 'p2', 'p3' (floats in Debye). Example shape: {"CO": {"p0": <float>, "p1": <float>, "p2": <float>, "p3": <float>}, "HCl": {"p0": <float>, "p1": <float>, "p2": <float>, "p3": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_coefficients.json
- path: `/app/outputs/fitted_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted dipole moment expansion coefficients p_k (k=0..3) from weighted least-squares fit to experimental spectroscopic data for CO and HCl. The values are deterministic given the provided input data.
- schema:
  - `type`: object
  - `required_keys`: `CO`, `HCl`
  - `properties`:
    - `CO`:
      - `type`: object
      - `required`: `p0`, `p1`, `p2`, `p3`
      - `item_types`:
        - `p0`: number
        - `p1`: number
        - `p2`: number
        - `p3`: number
      - `units`: Debye
    - `HCl`:
      - `type`: object
      - `required`: `p0`, `p1`, `p2`, `p3`
      - `item_types`:
        - `p0`: number
        - `p1`: number
        - `p2`: number
        - `p3`: number
      - `units`: Debye

Notes: The checker recomputes the p_k coefficients by solving the identical weighted least-squares problem using the same input data embedded in the instruction (hardcoded in checker). It compares the agent's submitted coefficients to its recomputed reference within a numeric tolerance (relative error < 1e-4 or absolute error < 1e-5 for near-zero values).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "CO",
          "HCl"
        ],
        "properties": {
          "CO": {
            "type": "object",
            "required": [
              "p0",
              "p1",
              "p2",
              "p3"
            ],
            "item_types": {
              "p0": "number",
              "p1": "number",
              "p2": "number",
              "p3": "number"
            },
            "units": "Debye"
          },
          "HCl": {
            "type": "object",
            "required": [
              "p0",
              "p1",
              "p2",
              "p3"
            ],
            "item_types": {
              "p0": "number",
              "p1": "number",
              "p2": "number",
              "p3": "number"
            },
            "units": "Debye"
          }
        }
      },
      "description": "Fitted dipole moment expansion coefficients p_k (k=0..3) from weighted least-squares fit to experimental spectroscopic data for CO and HCl. The values are deterministic given the provided input data."
    }
  ],
  "notes": "The checker recomputes the p_k coefficients by solving the identical weighted least-squares problem using the same input data embedded in the instruction (hardcoded in checker). It compares the agent's submitted coefficients to its recomputed reference within a numeric tolerance (relative error < 1e-4 or absolute error < 1e-5 for near-zero values)."
}
```

## How you are scored
A hidden verifier will independently reconstruct the same weighted linear least-squares problems from the identical input data embedded in this instruction. It will compute reference values for p0–p3 for CO and for HCl and compare your submitted coefficients against those references. The comparison uses a threshold-or-better tolerance policy: if your fitted coefficients are within an acceptable numeric tolerance of the reference, you receive full credit; if they deviate, the credit decreases monotonically with the deviation. The tolerance is chosen to accommodate legitimate numerical spread from different linear algebra implementations while demanding that the underlying physical fit has been performed correctly. Reporting the paper's numbers without actually carrying out the fit will not satisfy the verifier.
