# Critical Exponents of an Elastic Ising Antiferromagnet from Constant-Pressure Monte Carlo

## Problem background
Binary alloys that form antiferromagnetic superstructures can be described by an elastic Ising model where Ising spins couple to lattice distortions. When the lattice is allowed to relax (the compressible case), theory predicts that the phase transition at constant pressure may become weakly first order, deviating from the standard three‑dimensional Ising universality class. However, the nature of the transition in a realistic atomic model remains an open quantitative question. This task reproduces the finite‑size scaling analysis that yields the critical exponents and the universal Binder cumulant crossing value, providing definitive evidence for or against a deviation from pure Ising behavior.

## Approach
The model is an elastic antiferromagnet on a diamond lattice, with atomic interactions given by the Stillinger–Weber potential adapted for a binary system. Unlike‑species pairs are favoured antiferromagnetically by lowering the pair energy ε(+1,−1) to –2.3427 eV, while like‑species energies remain ε(+1,+1) = –2.17 eV and ε(−1,−1) = –1.93 eV. Constant‑pressure semigrand‑canonical Monte Carlo simulations are performed at zero pressure for multiple system sizes. The resulting energy and staggered‑magnetization histograms are reweighted to obtain thermodynamic quantities (staggered susceptibility, Binder cumulant, logarithmic derivatives). Finite‑size scaling of these observables then yields estimates for the critical exponents ν, β, γ and the Binder cumulant crossing value.

## Reproduction target
Perform the constant‑pressure Monte Carlo simulations at a temperature near kBT ≈ 0.31 eV for lattice sizes L = 6, 8, 10, 12, 14, 16, 18, 20, 24. From the accumulated joint histograms of potential energy and staggered magnetization, apply histogram reweighting to compute the Binder cumulant U₄, staggered magnetization m⁺, staggered susceptibility χ⁺, and their temperature derivatives. Through a finite‑size scaling analysis, extract the inverse correlation‑length exponent 1/ν, the ratio β/ν, the ratio γ/ν, and the universal Binder cumulant crossing value. Convert the ratios to the exponents ν, β, γ and report all four quantities together with their uncertainties in the file critical_exponents.json.

## Assets

- Stillinger–Weber potential parameters for binary Si-Ge (Laradji et al., Phys. Rev. B 51, 4894 (1995)): 10.1103/PhysRevB.51.4894
- NumPy: numpy
- SciPy: scipy
- Numba (optional): numba

## Workflow steps

### Step 1: Define the elastic antiferromagnetic Hamiltonian and simulation ensemble
- Role: process
- Action: Construct the Hamiltonian for an elastic Ising antiferromagnet on a diamond lattice using the Stillinger-Weber potential with the antiferromagnetic modification: set the unlike-species pair energy ε(+1,−1) = –2.3427 eV, while like-species energies remain ε(+1,+1) = –2.17 eV and ε(-1,−1) = –1.93 eV. All other potential parameters (radial cutoff, three‑body terms, etc.) are taken from Laradji et al., Phys. Rev. B 51, 4894 (1995). Set up the constant‑pressure semigrand‑canonical ensemble at zero pressure with volume rescaling moves. The system sizes to simulate are linear dimensions L = 6, 8, 10, 12, 14, 16, 18, 20, 24.
- Evidence: `/app/outputs/model_description.txt`

### Step 2: Run constant‑pressure Monte Carlo simulations
- Role: process
- Action: For each system size L, execute a constant‑pressure Monte Carlo simulation at a temperature near the expected critical point (k_B T₀ ≈ 0.31 eV). Use the Metropolis algorithm with spin flips, position displacements, and volume rescaling attempts. Accumulate a joint histogram of the Stillinger‑Weber potential energy W and the absolute staggered magnetization |m⁺| over 10⁷ Monte Carlo sweeps (MCS). Save the histogram for each size for subsequent reweighting.
- Evidence: `/app/outputs/histogram_L*.json`

### Step 3: Histogram reweighting and calculation of thermodynamic observables
- Role: process
- Action: For each system size, apply the Ferrenberg‑Swendsen single‑histogram technique to reweight the (W, |m⁺|) histograms from step 2 over a fine temperature grid. Compute the staggered susceptibility χ⁺, the Binder cumulant U₄, the logarithmic derivatives d ln|m⁺|/dK and d ln|m⁺|²/dK, and their temperature dependence. Locate the maximum of each derivative and the maxima of χ⁺ for the finite‑size scaling analysis.
- Evidence: `/app/outputs/reweighted_observables.json`

### Step 4: Finite‑size scaling analysis and report critical exponents
- Role: scored (load-bearing)
- Action: Using the maxima from step 3, perform nonlinear least‑squares fits to the scaling forms. Extract 1/ν from the size dependence of the maximum slopes of U₄ and the logarithmic derivatives of |m⁺| and |m⁺|². Determine β/ν from the finite‑size scaling of the staggered magnetization evaluated at the infinite‑lattice critical coupling K_c (estimated from the fits). Obtain γ/ν from the maxima of the staggered susceptibility. Compute ν, β, and γ from the ratios. Also determine the Binder cumulant crossing value U₄* by averaging the crossing points for L ≥ 10. From the estimated infinite‑lattice critical coupling K_c, compute the critical temperature T_c = 1/K_c (in energy units with k_B = 1) and its uncertainty. Write the final results to critical_exponents.json as an object with keys 'nu', 'beta', 'gamma', 'U4_crossing', and 'Tc', each having subfields 'value' (float) and 'error' (float).
- Output file: `/app/outputs/critical_exponents.json`
- Format: json
- Contract: {"nu": {"value": <float>, "error": <float>}, "beta": {"value": <float>, "error": <float>}, "gamma": {"value": <float>, "error": <float>}, "U4_crossing": {"value": <float>, "error": <float>}, "Tc": {"value": <float>, "error": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_exponents.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_exponents.json
- path: `/app/outputs/critical_exponents.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The critical exponents (ν, β, γ), critical temperature T_c, and the Binder cumulant crossing value U₄*, together with their uncertainties, obtained from the finite‑size scaling analysis of the simulated data.
- schema:
  - `type`: object
  - `required`:
    - `nu`: object with fields value (number) and error (number)
    - `beta`: object with fields value (number) and error (number)
    - `gamma`: object with fields value (number) and error (number)
    - `U4_crossing`: object with fields value (number) and error (number)
    - `Tc`: object with fields value (number) and error (number)

Notes: The checker compares the reported exponents, crossing value, and critical temperature to the paper’s published numbers with a tolerance of a few standard deviations. No other outputs are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "nu": "object with fields value (number) and error (number)",
          "beta": "object with fields value (number) and error (number)",
          "gamma": "object with fields value (number) and error (number)",
          "U4_crossing": "object with fields value (number) and error (number)",
          "Tc": "object with fields value (number) and error (number)"
        }
      },
      "description": "The critical exponents (ν, β, γ), critical temperature T_c, and the Binder cumulant crossing value U₄*, together with their uncertainties, obtained from the finite‑size scaling analysis of the simulated data."
    }
  ],
  "notes": "The checker compares the reported exponents, crossing value, and critical temperature to the paper’s published numbers with a tolerance of a few standard deviations. No other outputs are scored."
}
```

## How you are scored
A hidden verifier will read your critical_exponents.json and compare the reported exponents ν, β, γ and the Binder cumulant crossing value to a reference obtained from the primary literature. Each quantity is scored individually: if your value falls within a prescribed tolerance of the reference you earn full credit for that quantity; larger deviations yield reduced credit. The final reward is a weighted sum over the four quantities. Reporting the correct trend or a plausible guess is not sufficient – the verifier requires a genuine finite‑size scaling analysis derived from the Monte Carlo simulations you performed.
