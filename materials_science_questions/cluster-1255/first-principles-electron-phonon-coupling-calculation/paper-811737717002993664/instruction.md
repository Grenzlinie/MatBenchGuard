# RPA calculation of spin-fluctuation spectral weight and quasiparticle spectral weight in a d-wave superconductor

## Problem background
Angle-resolved photoemission spectroscopy (ARPES) measurements on high-temperature superconductors, such as Bi-2212, typically show a sharp quasiparticle peak, a broad inelastic background, and—when the sample is cooled below the superconducting transition temperature Tc—a dip feature next to the main peak. The origin of this dip has been debated. This task implements a model in which the dip arises from the opening of a spin gap in the magnetic susceptibility. The model computes the momentum-integrated spin-fluctuation spectral weight D(E) and the total quasiparticle spectral weight A(k,E) that includes both an elastic coherent part and an incoherent background from spin-fluctuation emission and absorption. By evaluating D(E) and A(k,E) at temperatures above and below Tc, one can investigate whether a spin gap and a corresponding dip feature appear as a natural consequence of the superconducting state.

## Approach
The theoretical framework combines a tight-binding electronic band structure, a d-wave superconducting order parameter, and a random-phase approximation (RPA) treatment of the spin susceptibility. The key steps are: (i) define the normal-state band and the d-wave gap; (ii) compute the bare electronic spin susceptibility χ⁰(q,E) using the electronic Green’s function, superconducting coherence factors, and Fermi-Dirac statistics; (iii) obtain the RPA interacting susceptibility Im χ(q,E) from χ⁰ via a Stoner-like enhancement factor; (iv) integrate (g/t)² Im χ(q,E) over the full two-dimensional Brillouin zone to obtain the spin-fluctuation spectral weight D(E); (v) compute the elastic quasiparticle peak A⁰(k,E) from the retarded Green’s function at a chosen k-point on the Fermi surface; (vi) compute the inelastic background A_inel(k,E) by convolving the imaginary part of the Green’s function with D(E) and the thermal Bose-Einstein and Fermi-Dirac distribution functions; finally, (vii) obtain the total spectral weight A(k,E) as a linear combination of the elastic and inelastic contributions. All calculations are carried out for two temperatures: T/Tc=1.0 (normal state) and T/Tc=0.3 (superconducting state). The comparison between the two temperatures reveals how the opening of the superconducting gap modifies the spin-fluctuation spectrum and, in turn, the photoemission spectrum.

## Reproduction target
Produce the following scored artifacts as CSV files:

- D_E.csv: Momentum-integrated spin-fluctuation spectral weight D(E)·t on a grid of energies from 0 to 0.5t with a step no larger than 0.01t. The file must contain three columns: energy (in units of t), D_E_T1 (value at T/Tc=1.0), and D_E_T2 (value at T/Tc=0.3).
- A_k_E.csv: Total quasiparticle spectral weight A(k,E)·t at the Fermi surface point k=(π,0.1624), on an energy grid from -0.2t to 0.4t with a step no larger than 0.01t. The file must contain three columns: energy (in units of t), A_T1 (value at T/Tc=1.0), and A_T2 (value at T/Tc=0.3).

All input model parameters are fixed: tight‑binding with t' = -0.45t, chemical potential μ = -1.75t; d-wave gap amplitude Δ₀ = 0.1t; electronic damping Γ = Γ₀ + Γ₁(T/Tc)³ with Γ₀ = 0.04t and Γ₁ = 0.05t; spin-fluctuation coupling constant g = U = 1.0t; inelastic/elastic mixing factor α = 4.0. The calculations must be done for the two temperatures mentioned above. The resulting curves serve as the basis for examining whether the model produces a spin gap in D(E) and a dip feature in A(k,E) below Tc, which would support the proposed mechanism.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute bare and RPA spin susceptibility
- Role: process
- Action: Compute the bare electronic spin susceptibility χ⁰(q,E) by summing over momentum p and integrating over energy E' using the tight-binding band ξ_k, d-wave gap Δ_k, damping Γ, and superconducting coherence factors. Then obtain the RPA interacting susceptibility Im χ(q,E) using coupling constant U=1.0t.
- Evidence: none

### Step 2: Spin-fluctuation spectral weight D(E)
- Role: scored (load-bearing)
- Action: Compute D(E) by integrating (U/t)^2 Im χ(q,E) over the full Brillouin zone. Compute for temperatures T/Tc=1.0 and 0.3. Output the curves as a CSV file with columns: energy, D_E_T1, D_E_T2. Energy range 0 to 0.5t with step ≤0.01t.
- Output file: `/app/outputs/D_E.csv`
- Format: csv
- Contract: CSV with columns: energy (float, energy in units of t), D_E_T1 (float, D(E) at T/Tc=1.0), D_E_T2 (float, D(E) at T/Tc=0.3). Energy range [0, 0.5t], step ≤0.01t.
- Scoring: scored by hidden verifier

### Step 3: Elastic spectral weight A⁰(k,E)
- Role: process
- Action: Compute the elastic main peak contribution A⁰(k,E) from the retarded Green's function using the tight-binding band, d-wave gap, and damping, at the Fermi surface point k=(π,0.1624). Compute for both temperatures.
- Evidence: none

### Step 4: Inelastic spectral weight A_inel(k,E)
- Role: process
- Action: Compute the inelastic background contribution A_inel(k,E) using the convolution integral that couples Im G(k,E) with the spin-fluctuation spectral weight D(E), weighted by the Bose-Einstein and Fermi-Dirac occupation factors and energy-conservation step functions. Use α=4.0.
- Evidence: none

### Step 5: Quasiparticle spectral weight A(k,E)
- Role: scored (load-bearing)
- Action: Combine elastic and inelastic contributions as A(k,E)=A⁰(k,E)+α A_inel(k,E). Output the curves as a CSV file with columns: energy, A_T1, A_T2. Energy range -0.2t to 0.4t with step ≤0.01t.
- Output file: `/app/outputs/A_k_E.csv`
- Format: csv
- Contract: CSV with columns: energy (float, energy in units of t), A_T1 (float, A(k,E) at T/Tc=1.0), A_T2 (float, A(k,E) at T/Tc=0.3). Energy range [-0.2t, 0.4t], step ≤0.01t.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/D_E.csv`
- `/app/outputs/A_k_E.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### D_E.csv
- path: `/app/outputs/D_E.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Momentum-integrated spin-fluctuation spectral weight D(E) multiplied by t, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `D_E_T1`, `D_E_T2`
  - `units`:
    - `energy`: t (nearest-neighbor hopping energy unit)
    - `D_E_T1`: dimensionless (D(E)*t)
    - `D_E_T2`: dimensionless (D(E)*t)

### A_k_E.csv
- path: `/app/outputs/A_k_E.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total quasiparticle spectral weight A(k,E) multiplied by t, at k=(π,0.1624) on the Fermi surface, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `A_T1`, `A_T2`
  - `units`:
    - `energy`: t (nearest-neighbor hopping energy unit)
    - `A_T1`: dimensionless (A(k,E)*t)
    - `A_T2`: dimensionless (A(k,E)*t)

Notes: The model parameters are fixed: tight-binding with t'=-0.45t, μ=-1.75t, d-wave gap Δ0=0.1t, damping Γ0=0.04t, Γ1=0.05t, coupling U=1.0t, α=4.0, and the k-point is (π,0.1624). All equations are as given in the paper's methods; energies are in units of t. The structural audit does not require exact numerical agreement, only the qualitative physical characteristics described in the model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "D_E.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "D_E_T1",
          "D_E_T2"
        ],
        "units": {
          "energy": "t (nearest-neighbor hopping energy unit)",
          "D_E_T1": "dimensionless (D(E)*t)",
          "D_E_T2": "dimensionless (D(E)*t)"
        }
      },
      "description": "Momentum-integrated spin-fluctuation spectral weight D(E) multiplied by t, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references."
    },
    {
      "file": "A_k_E.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "A_T1",
          "A_T2"
        ],
        "units": {
          "energy": "t (nearest-neighbor hopping energy unit)",
          "A_T1": "dimensionless (A(k,E)*t)",
          "A_T2": "dimensionless (A(k,E)*t)"
        }
      },
      "description": "Total quasiparticle spectral weight A(k,E) multiplied by t, at k=(π,0.1624) on the Fermi surface, for two temperatures. The structural audit evaluates whether the curve shapes are physically plausible according to the model, without requiring exact numerical references."
    }
  ],
  "notes": "The model parameters are fixed: tight-binding with t'=-0.45t, μ=-1.75t, d-wave gap Δ0=0.1t, damping Γ0=0.04t, Γ1=0.05t, coupling U=1.0t, α=4.0, and the k-point is (π,0.1624). All equations are as given in the paper's methods; energies are in units of t. The structural audit does not require exact numerical agreement, only the qualitative physical characteristics described in the model."
}
```

## How you are scored
A hidden automatic verifier will read your submitted D_E.csv and A_k_E.csv. It will first validate that both files follow the declared format (correct columns, energy ranges, no missing values). It will then analyze the physical content of the curves through a series of structural checks that do not require matching specific numerical reference values from the literature. The verifier will evaluate whether the computed curves exhibit the qualitative physical characteristics predicted by the model (e.g., signatures of superconductivity, changes between normal and superconducting states). The analysis uses techniques such as local extrema detection, monotonicity testing, and comparison of the two temperature curves. The final reward is a weighted combination of the scores from the two artifacts, with D_E.csv and A_k_E.csv each carrying substantial weight. To obtain a high score, your implementation must faithfully execute the physical model described in the approach and produce numerically well‑resolved output files.
