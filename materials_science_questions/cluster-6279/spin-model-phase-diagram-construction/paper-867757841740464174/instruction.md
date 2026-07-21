# Extrapolated Critical Temperatures and Exponents from Finite-Size Scaling of 3D Classical XY Model with Bilinear-Biquadratic Exchange

## Problem background
Three-dimensional classical spin models with XY symmetry exhibit rich critical behaviour. When both bilinear and biquadratic nearest-neighbor exchange interactions are present, the system can support two distinct types of long-range order: dipole ferromagnetic order (DLRO) and axial quadrupole order (QLRO). The competition between these interactions is predicted to produce a phase diagram containing first-order and second-order phase boundaries, separate dipole and quadrupole ordering transitions, and multicritical points. The precise location of the phase boundaries and the values of the critical exponents for the different transitions, especially in the region where the biquadratic exchange is comparable to or larger than the bilinear one, are open questions that can be investigated by large-scale Monte Carlo simulations.

## Approach
The approach is a finite‑size scaling analysis of extensive Monte Carlo simulations. The bilinear–biquadratic XY Hamiltonian is implemented on a simple cubic lattice with periodic boundary conditions. Standard Metropolis Monte Carlo (SMC) is used to record the temperature dependence of the internal energy, the dipole and quadrupole order parameters, specific heat, susceptibilities, and fourth‑order cumulants. These are complemented by histogram Monte Carlo (HMC) simulations near the estimated transition points to obtain high‑resolution energy and order‑parameter histograms and logarithmic derivatives. For parameter values where the transition is first‑order, the size‑dependent transition temperature is extracted by the equal‑height method applied to bimodal energy histograms and extrapolated to infinite size assuming a volume scaling. For second‑order transitions, critical temperatures are located from the peaks of susceptibilities and logarithmic derivatives, finite‑size scaling relations are used to extract the correlation‑length exponent ν and the susceptibility exponent γ, and the infinite‑size transition temperature is obtained by extrapolating Tc(L) against L^{-1/ν}. The entire procedure is repeated over a set of exchange‑ratio values that span the phase diagram.

## Reproduction target
Compute the infinite‑system transition temperatures and, for second‑order transitions, the critical exponents. Specifically, determine:

- For first‑order transitions at exchange ratios J/J' = 0.35, 0.4, 0.5, the infinite‑size transition temperature Tc extracted from finite‑size scaling of the Lee–Kosterlitz equal‑height temperatures.
- For DLRO (dipole‑quadrupole) transitions at J/J' = 0.8, 1.0, 2.5, and the bilinear‑only limit J/J' → ∞, the extrapolated transition temperature Tc, the correlation‑length exponent ν, and the susceptibility exponent γ.
- For QLRO (pure quadrupole) transitions at J/J' = 0, 0.1, 0.2, 0.3, the extrapolated transition temperature Tc, the correlation‑length exponent ν, and the susceptibility exponent γ.

All values must be collected into a single JSON file `/app/outputs/results.json` with three top‑level arrays: `first_order_transitions`, `DLRO_transitions`, and `QLRO_transitions`, each entry containing the appropriate fields (`J_over_Jprime`, `Tc`, `nu`, `gamma`) and numeric values with at least three decimal places.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Standard Monte Carlo (SMC) simulations
- Role: process
- Action: Implement the bilinear-biquadratic XY model Hamiltonian on a simple cubic lattice with periodic boundary conditions. For each required exchange ratio (J/J' = 0.35, 0.4, 0.5, 0.8, 1.0, 2.5, infinity, 0, 0.1, 0.2, 0.3) and suitable range of linear lattice sizes (e.g., L = 6, 12, 18, 24, 30), run standard Metropolis Monte Carlo simulations with equilibration and averaging steps. Record temperature-dependent series of the internal energy E, the dipole and quadrupole long-range order parameters M and Q, the specific heat c, the susceptibilities χ_M and χ_Q, and the fourth-order Binder cumulants g_M and g_Q.
- Evidence: none

### Step 2: Histogram Monte Carlo (HMC) simulations
- Role: process
- Action: For each J/J' value and lattice size, run histogram Monte Carlo (Ferrenberg–Swendsen) simulations at temperatures near the transition points identified from the SMC results. Use long equilibration and averaging to produce high-quality energy histograms P(E), order parameter histograms P(M) and P(Q), and temperature series of the logarithmic derivatives D1M, D2M, D1Q, D2Q.
- Evidence: none

### Step 3: Extract size-dependent transition temperatures and scaling maxima
- Role: process
- Action: Using the SMC and HMC output, determine the size-dependent transition temperatures Tc(L) for each (J/J', L) combination. For second-order transitions, locate Tc(L) from peaks of susceptibilities and logarithmic derivatives. For first-order transitions (J/J' = 0.35, 0.4, 0.5), apply the Lee–Kosterlitz equal-height method to bimodal energy histograms to find precise Tc(L). Collect the maximum values of susceptibilities and logarithmic derivatives that enter the finite-size scaling relations.
- Evidence: none

### Step 4: Finite-size scaling extrapolation to infinite size
- Role: scored (load-bearing)
- Action: Perform finite-size scaling extrapolations to obtain the infinite‑system transition temperatures and critical exponents. For first-order transitions, extrapolate Tc(L) using Tc(L) vs L^{-3}. For second-order DLRO transitions, extract the correlation-length exponent ν_M from log‑log slopes of the logarithmic derivative maxima, then extrapolate Tc(L) vs L^{-1/ν_M}; similarly extract the susceptibility exponent γ_M. For QLRO transitions, repeat the procedure to obtain ν_Q and γ_Q. Compile the extrapolated values into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with three top‑level keys: first_order_transitions (array of objects with keys 'J_over_Jprime' (number) and 'Tc' (number)), DLRO_transitions (array of objects with keys 'J_over_Jprime' (number or the string 'inf'), 'Tc' (number), 'nu' (number), 'gamma' (number)), and QLRO_transitions (array of objects with keys 'J_over_Jprime' (number), 'Tc' (number), 'nu' (number), 'gamma' (number)). All numeric values must have at least three decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final extrapolated infinite‑size transition temperatures and critical exponents. The verifier compares the contents against reference values from the reported Monte Carlo study.
- schema:
  - `type`: object
  - `required`:
    - `first_order_transitions`: array of objects with numeric field J_over_Jprime and numeric field Tc
    - `DLRO_transitions`: array of objects with fields J_over_Jprime (number or string 'inf'), Tc (number), nu (number), gamma (number)
    - `QLRO_transitions`: array of objects with fields J_over_Jprime (number), Tc (number), nu (number), gamma (number)
  - `notes`: Numeric values are expected with at least three decimal places. The J_over_Jprime field in DLRO_transitions must be the string 'inf' when representing the bilinear-only limit.

Notes: The output file must contain all three arrays; missing or malformed entries receive zero credit for that part. The verifier uses hidden reference values and will apply appropriate tolerances to each numeric field.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "first_order_transitions": "array of objects with numeric field J_over_Jprime and numeric field Tc",
          "DLRO_transitions": "array of objects with fields J_over_Jprime (number or string 'inf'), Tc (number), nu (number), gamma (number)",
          "QLRO_transitions": "array of objects with fields J_over_Jprime (number), Tc (number), nu (number), gamma (number)"
        },
        "notes": "Numeric values are expected with at least three decimal places. The J_over_Jprime field in DLRO_transitions must be the string 'inf' when representing the bilinear-only limit."
      },
      "description": "Final extrapolated infinite‑size transition temperatures and critical exponents. The verifier compares the contents against reference values from the reported Monte Carlo study."
    }
  ],
  "notes": "The output file must contain all three arrays; missing or malformed entries receive zero credit for that part. The verifier uses hidden reference values and will apply appropriate tolerances to each numeric field."
}
```

## How you are scored
A hidden verifier independently checks the contents of your `/app/outputs/results.json` file. It compares the transition temperatures and critical exponents you report against reference values obtained from a direct implementation of the same protocol, with tolerances that account for the stochastic nature of Monte Carlo simulations. The verifier does not re‑run your simulation; it reads your final reported numbers and verifies that they fall within the expected range of a correct reproduction. Each of the three transition categories contributes a fraction of the total reward, summed to produce a final score between 0 and 1. Simply quoting numbers from the literature without running the required simulations will not pass the verification tolerances.
