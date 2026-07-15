# Thermodynamic Stability of H2–Noble Gas Mixtures

## Problem background
The mutual solubility and thermodynamic stability of hydrogen–noble gas mixtures are important across a wide range of temperatures and pressures. This task investigates the mixing properties of H₂ with He, Ne, and Ar by computing the concentration dependence of the excess Gibbs free energy of mixing, the excess entropy of mixing, and the concentration fluctuations. These quantities together characterise whether a mixture tends to remain homogeneously mixed or to segregate under given thermodynamic conditions.

## Approach
The model employs a statistical mechanical perturbation scheme. Pair interactions are separated into a repulsive hard-sphere reference and a long-range attractive tail described by a Double Yukawa (DY) potential. Unlike-pair interactions are not assumed additive; the deviation from the Lorentz-Berthelot rule is parameterised by a temperature-dependent non-additivity parameter α(T), which is obtained from experimental excess second virial coefficients. The Helmholtz free energy F is decomposed into four contributions: the ideal gas term, a hard-convex-body term (which accounts for dimerisation of the H₂ molecule), a first-order perturbation term from the DY tail (evaluated analytically via Laplace transforms of the hard-sphere radial distribution function), and the leading quantum correction. The Gibbs free energy G is obtained from F and the pressure p, where p is computed from density derivatives of each free energy contribution. The excess Gibbs free energy of mixing G_xs is defined as the difference between the mixture G and the composition-weighted sum of the pure-fluid standard-state Gibbs energies, minus the ideal mixing term. The excess entropy S_xs is obtained by numerical temperature differentiation of G, taking into account the temperature dependence of the hard-sphere diameters and of α(T). The normalised concentration fluctuations S_cc* are derived from the second derivative of G with respect to composition.

## Reproduction target
Produce three CSV files containing the computed thermodynamic quantities for the binary mixtures H₂–He, H₂–Ne, and H₂–Ar. (1) `excess_gibbs.csv`: G_xs (kJ mol⁻¹) as a function of H₂ mole fraction (0.0 to 1.0, at least 11 equally spaced points) at T = 150 K and p = 1.0 GPa. (2) `excess_entropy.csv`: S_xs (in units of R) on the same composition grid and under the same (T,p) condition. (3) `S_cc_star.csv`: normalised concentration fluctuations S_cc*(0) (dimensionless) at equiatomic composition (c_H₂ = 0.5) for a grid of temperatures from 150 K to 350 K (at least 5 values) and pressures from 0.01 GPa to 10 GPa (at least 4 values). Each CSV must contain the columns defined in the output contract.

## Assets

- Empirical pair potentials for pure H2 (Ree exp-6 potential, Ref. [2]), He (Ree exp-6 potential, Ref. [2]), Ne (Leonhard–Dieters ab initio potential, Ref. [3]), and Ar (Aziz potential, Ref. [4,5]), whose forms and parameters are given in the paper's Section 2.2 and illustrated in Figure 1. These are public literature potentials and must be retrieved by the agent.
- Experimental excess second virial coefficients E_xs* for the mixtures H2–He, H2–Ne, and H2–Ar (Brewer and Vaughun, Ref. [6] / J. Chem. Phys. 50, 2960 (1969)). These are public and are used to solve for the temperature-dependent non-additivity parameter α(T).

## Workflow steps

### Step 1: Fit DY potential parameters for pure elements
- Role: process
- Action: Retrieve the empirical pair potentials for H2, He, Ne, and Ar from the literature (see Assets). Numerically fit a Double Yukawa potential (Equation 5) to each empirical potential to obtain the parameters λ, v, A, ε (K), and σ0 (Å) for each pure element. The fitted parameters will be used as inputs for modelling the mixture. No scored artifact is produced at this stage; store the parameters for use in later steps.
- Evidence: none

### Step 2: Determine the non-additivity parameter α(T) from experimental virial coefficients
- Role: process
- Action: Using the empirical pair potentials and the experimental excess second virial coefficients E_xs* for H2–He, H2–Ne, and H2–Ar (see Assets), numerically solve Equation 22 to obtain α(T) at several temperatures between 150 K and 350 K. Fit a linear relation α(T) = g1·T + g2 for each mixture. The resulting coefficients g1 and g2 become inputs for the perturbation model. No scored artifact is produced; store the coefficients.
- Evidence: none

### Step 3: Implement perturbation theory free energy model
- Role: process
- Action: Using the DY potential parameters from Step 1 and the α(T) coefficients from Step 2, write code that implements the full Gibbs free energy G(c,T,p) for a binary mixture. This includes the ideal term F_id, the hard-convex-body term F_HCB (accounting for H2 dimerisation), the first-order perturbation term F^t via analytic Laplace transforms of rg_HS(r) for the DY tail, and the leading quantum correction F^Q. Also compute pressure p from density derivatives of each F term to obtain G. Numerical derivatives with respect to T and c will be needed later for entropy and concentration fluctuations.
- Evidence: none

### Step 4: Compute excess Gibbs free energy of mixing G_xs
- Role: scored (load-bearing)
- Action: Using the implemented model, evaluate G_xs(c,T,p) as defined in Eq. 30 for the mixtures H2–He, H2–Ne, H2–Ar at T=150 K, p=1.0 GPa. For each mixture, compute G_xs at exactly 11 equally spaced H2 mole fractions c_H2 = 0.0, 0.1, 0.2, ..., 1.0. The required standard-state Gibbs energies G_i^0 are obtained in the limit c_j→0. Write the results to the output CSV.
- Output file: `/app/outputs/excess_gibbs.csv`
- Format: csv
- Contract: columns: mixture (string, one of 'H2-He', 'H2-Ne', 'H2-Ar'), mole_fraction_H2 (float, in [0,1]), G_xs (float, kJ mol⁻¹).
- Scoring: scored by hidden verifier

### Step 5: Compute excess entropy of mixing S_xs
- Role: scored
- Action: Compute S_xs(c,T,p) via numerical temperature differentiation of the Gibbs free energy (Eq. 32) using the same 11-point composition grid, T=150 K, and p=1.0 GPa as Step 4. Take proper account of the temperature dependence of hard-sphere diameters and α(T). Write the results to the output CSV.
- Output file: `/app/outputs/excess_entropy.csv`
- Format: csv
- Contract: columns: mixture (string), mole_fraction_H2 (float), S_xs (float, in units of R).
- Scoring: scored by hidden verifier

### Step 6: Compute concentration fluctuations S_cc*
- Role: scored
- Action: Calculate the normalised concentration fluctuations S_cc*(0) = S_cc(0)/S_cc^id(0) from Eq. 1 (second derivative of G with respect to c) at equiatomic composition (c_H2=0.5) for each mixture. Evaluate S_cc_star at the **exact** following temperatures and pressures:
  - Temperatures: T = 150, 200, 250, 300, 350 K
  - Pressures: p = 0.01, 0.1, 1.0, 10.0 GPa
  (20 points per mixture). Write the results to the output CSV.
- Output file: `/app/outputs/S_cc_star.csv`
- Format: csv
- Contract: columns: mixture (string), temperature_K (float), pressure_GPa (float), S_cc_star (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/excess_gibbs.csv`
- `/app/outputs/excess_entropy.csv`
- `/app/outputs/S_cc_star.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### excess_gibbs.csv
- path: `/app/outputs/excess_gibbs.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Excess Gibbs free energy of mixing for H2–He, H2–Ne, H2–Ar at T=150 K, p=1.0 GPa, over a composition grid of at least 11 points per mixture.
- schema:
  - `type`: table
  - `required_columns`: `mixture`, `mole_fraction_H2`, `G_xs`

### excess_entropy.csv
- path: `/app/outputs/excess_entropy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Excess entropy of mixing for H2–He, H2–Ne, H2–Ar at T=150 K, p=1.0 GPa, over the same composition grid.
- schema:
  - `type`: table
  - `required_columns`: `mixture`, `mole_fraction_H2`, `S_xs`

### S_cc_star.csv
- path: `/app/outputs/S_cc_star.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalised concentration fluctuations S_cc*(0) at equiatomic composition for the three mixtures, covering T∈[150,350] K and p∈[0.01,10] GPa with at least 5 T and 4 p values each.
- schema:
  - `type`: table
  - `required_columns`: `mixture`, `temperature_K`, `pressure_GPa`, `S_cc_star`

Notes: The hidden checker compares the agent's CSV values against paper-derived gold references using tolerances appropriate for a perturbation-theory reimplementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "excess_gibbs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mixture",
          "mole_fraction_H2",
          "G_xs"
        ]
      },
      "description": "Excess Gibbs free energy of mixing for H2–He, H2–Ne, H2–Ar at T=150 K, p=1.0 GPa, over a composition grid of at least 11 points per mixture."
    },
    {
      "file": "excess_entropy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mixture",
          "mole_fraction_H2",
          "S_xs"
        ]
      },
      "description": "Excess entropy of mixing for H2–He, H2–Ne, H2–Ar at T=150 K, p=1.0 GPa, over the same composition grid."
    },
    {
      "file": "S_cc_star.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mixture",
          "temperature_K",
          "pressure_GPa",
          "S_cc_star"
        ]
      },
      "description": "Normalised concentration fluctuations S_cc*(0) at equiatomic composition for the three mixtures, covering T∈[150,350] K and p∈[0.01,10] GPa with at least 5 T and 4 p values each."
    }
  ],
  "notes": "The hidden checker compares the agent's CSV values against paper-derived gold references using tolerances appropriate for a perturbation-theory reimplementation."
}
```

## How you are scored
A hidden verifier will read your three CSV files and compare the computed values against reference results. Scoring combines accuracy across the three artifacts with independent checks: numerical accuracy of G_xs and S_xs (with tolerances appropriate for a reimplementation of the perturbation theory), accuracy of S_cc*, and structural consistency checks (e.g., relative ordering of S_cc* among the three mixtures at specified conditions, sign of G_xs, and expected temperature/pressure trends). Reporting the paper's numbers without running the computation is not sufficient; the verifier rewards faithful execution of the model.
