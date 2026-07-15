# BCS Transition Temperature and Isotope Exponent from Anisotropic Tight-Binding Model

## Problem background
Within BCS theory, the transition temperature and the isotope effect exponent depend on the electronic density of states (DOS) near the Fermi energy. When the DOS varies rapidly, these quantities can deviate from the standard 3D BCS values. This task computes the transition temperature Tc and the isotope exponent α for an anisotropic tight-binding model, examining how they depend on the interlayer coupling strength (γ) and the Fermi-level position relative to the band center (δ).

## Approach
The electronic structure is modelled by a tight-binding band on a simple cubic lattice:  
E(k) = ε0 − 2t(cos k_x a + cos k_y a) − 2γt cos k_z a,  
where t is the intralayer hopping, γ is the ratio of interlayer to intralayer hopping, and ε0 is the on-site energy.  
The density of states N(E) is obtained from this band (e.g., via the imaginary part of the Green function).  
The BCS transition temperature Tc is determined by solving the integral equation  

\[ \frac{2}{V} = \int_{E_F-\hbar\omega_c}^{E_F+\hbar\omega_c} \tanh\!\left(\frac{E-E_F}{2k_B T_c}\right) \frac{N(E)}{E-E_F}\,dE \]

numerically for each choice of δ = E_F − ε0 and γ. The isotope exponent α is then evaluated by numerical differentiation:  

\[ \alpha = \frac{1}{2}\frac{d\ln T_c}{d\ln(\hbar\omega_c)}. \]

The computation uses the parameters V/2t = 0.75, ħω_c/2t = 0.12, and t = 0.2 eV.  
The task computes Tc and α for γ = 0, 0.05, 0.25, 0.5, 0.75, 1.0 at δ = 0, and for γ = 0 and γ = 1 over a range of δ ∈ [−0.2, 0.2] eV, observing how the results evolve with anisotropy and Fermi-level position.

## Reproduction target
Numerically compute the BCS transition temperature Tc and the isotope effect exponent α for the anisotropic tight-binding model described above, at the specified values of γ and δ. Produce a CSV file (`results.csv`) with columns `gamma`, `delta`, `Tc`, `alpha` containing the results for all required (γ, δ) combinations.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute electronic density of states from tight-binding model
- Role: process
- Action: Compute the electronic density of states N(E) for the anisotropic tight-binding band E(k) = ε0 - 2t(cos k_x a + cos k_y a) - 2γt cos k_z a for the required γ values (0, 0.05, 0.25, 0.5, 0.75, 1.0). Use the standard approach of integrating over the Brillouin zone (e.g., via the imaginary part of the Green function). The resulting N(E) data must be available for the subsequent Tc calculation.
- Evidence: none

### Step 2: Solve BCS gap equation and compute isotope exponent
- Role: scored (load-bearing)
- Action: Using the computed density of states N(E), numerically solve the BCS gap equation (the integral equation for the transition temperature Tc) as a function of the Fermi-level deviation δ = E_F - ε_0 for each γ value. For each solution, compute the isotope effect exponent α via numerical differentiation of ln(Tc) with respect to ln(ħω_c). Record all (γ, δ, Tc, α) combinations in results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: gamma (float, dimensionless), delta (float, in eV), Tc (float, in K), alpha (float, dimensionless). The file must include rows for gamma in {0, 0.05, 0.25, 0.5, 0.75, 1.0} at delta=0, and for gamma=0 and gamma=1 a set of delta values covering the range [-0.2, 0.2] eV with a step size no larger than 0.01 eV.
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
- description: The agent's computed BCS transition temperature Tc and isotope effect exponent alpha for various anisotropy ratios gamma and Fermi-level deviations delta. The hidden checker compares these values to the paper-reported reference values and verifies structural trends (peak location, monotonicity).
- schema:
  - `type`: table
  - `required_columns`: `gamma`, `delta`, `Tc`, `alpha`
  - `units`:
    - `gamma`: dimensionless
    - `delta`: eV
    - `Tc`: K
    - `alpha`: dimensionless

Notes: The agent must implement the tight-binding DOS calculation and the numerical solution of the BCS integral equation independently. The output must contain the required (gamma, delta) grid. No gold values or tolerances are disclosed.

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
          "gamma",
          "delta",
          "Tc",
          "alpha"
        ],
        "units": {
          "gamma": "dimensionless",
          "delta": "eV",
          "Tc": "K",
          "alpha": "dimensionless"
        }
      },
      "description": "The agent's computed BCS transition temperature Tc and isotope effect exponent alpha for various anisotropy ratios gamma and Fermi-level deviations delta. The hidden checker compares these values to the paper-reported reference values and verifies structural trends (peak location, monotonicity)."
    }
  ],
  "notes": "The agent must implement the tight-binding DOS calculation and the numerical solution of the BCS integral equation independently. The output must contain the required (gamma, delta) grid. No gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier reads your `results.csv` and compares the Tc and alpha values against hidden reference values as well as expected structural trends (e.g., how Tc and α change with γ and δ). Points are awarded for each required data point and for the consistency of the overall trends; empty or missing rows earn no credit. The verifier does not disclose the reference values, so you must compute them faithfully from the model.
