# Compute adsorbed finite-difference derivative of H₂ parallel polarizability using semi-harmonic perturbation theory

## Problem background
The adsorption of diatomic molecules on surfaces or in porous materials perturbs their intramolecular potential, altering bond lengths and property functions such as polarizability. Reliable modeling of interaction energies and vibrational spectra requires knowing whether the property dependence on intramolecular distance is significantly changed upon adsorption. This task reproduces a key numerical check for molecular hydrogen (H₂) in NaA zeolite: using stationary perturbation theory with a linear interaction potential, one can compute a semi-harmonic correction to the gas-phase finite-difference derivative of the parallel polarizability α∥. The computed adsorbed derivative tests the claim that the slope parameter b of the linear approximation X(R)=a+b ΔR remains essentially unchanged.

## Approach
The calculation begins with gas-phase expectation values of parallel polarizability α∥ and bond length R for vibrational levels v=0,1,2 (obtained from literature). Molecular constants (harmonic frequency ωe, anharmonicity ωexe, equilibrium distance Re) and the perturbation coefficient K1 for the linear adsorption potential are provided. The semi-harmonic approximation uses first-order perturbed vibrational wavefunctions with the perturbation U(R)=K0+K1(R−Re). The gas-phase finite-difference derivative for the v=0→1 transition is computed. Then a correction S to the numerator (and similarly S_R to the denominator) is evaluated using harmonic-oscillator matrix elements of the reduced coordinate ξ and anharmonic energy denominators. The adsorbed finite-difference derivative is obtained as (gas_numerator + S) / (gas_denominator + S_R). All numerical inputs are listed in the Assets section; the computation requires only elementary arithmetic and harmonic-oscillator matrix elements.

## Reproduction target
Compute the adsorbed finite-difference derivative of the parallel polarizability α∥ for H₂ (v=0→1 transition) and write the result as a single floating-point number to `/app/outputs/adsorbed_derivative.txt`, in units of e²a₀²E_h⁻¹. This is the central quantity: it represents the slope of α∥ versus bond length in the adsorbed state under the semi-harmonic approximation. Intermediate values (gas-phase derivative, S, S_R) may be logged locally but are not required for scoring.

## Numerical inputs

All values are in atomic units unless otherwise noted. Use the following constants:

### Gas-phase expectation values (from Kolos & Wolniewicz, Poll & Wolniewicz, Wolniewicz)
| v | α∥ (e²a₀²E_h⁻¹) | R (a₀) |
|---|---|---|
| 0 | 6.7631 | 1.4487 |
| 1 | 7.5420 | 1.5454 |
| 2 | 8.3674 | 1.6461 |

### Molecular constants (from Huber & Herzberg)
- Harmonic frequency ωe = 4401.21 cm⁻¹
- Anharmonicity ωexe = 121.336 cm⁻¹
- Equilibrium bond length Re = 1.400 a₀

### Perturbation coefficient
- K1 = −6.1 × 10⁻³ E_h a₀⁻¹

### Physical constants
- Speed of light c = 2.99792458 × 10¹⁰ cm s⁻¹
- Planck constant h = 6.62607015 × 10⁻²⁷ erg·s   (required for energy scaling; the product hc converts cm⁻¹ into energy)
- π = 3.141592653589793

## Workflow steps

### Step 1: Compute semi-harmonic correction S
- Role: process
- Action: Implement the semi-harmonic correction S for the v=0→1 transition using the explicit formula:
  S = (b * K1 * Re²) / (4 * π² * h * c² * ωe) × [ 2/(ωe − 2*ωexe) − 2/(ωe − 4*ωexe) ]
  where b is the gas-phase finite-difference slope of α∥, computed as (〈α∥(v=1)〉 − 〈α∥(v=0)〉) / (〈R(v=1)〉 − 〈R(v=0)〉). Use this b to compute the numerator correction S. For the denominator correction S_R, use the same formula with b = 1. All constants are from the 'Numerical inputs' section. You may keep intermediate values for your own reference; no specific output file is required for this step.

### Step 2: Compute adsorbed finite-difference derivative of α∥
- Role: scored
- Action: Compute the adsorbed-state finite-difference derivative of the parallel polarizability as (gas_numerator + S) / (gas_denominator + S_R) and write the resulting scalar to the output file. The calculation uses the intermediate values computed in the previous step.
- Output file: `/app/outputs/adsorbed_derivative.txt`
- Format: txt
- Contract: plain-text float, units e²a₀²E_h⁻¹
- Scoring: scored by hidden verifier

## Output files
Write all scored artifacts under `/app/outputs`:
- `/app/outputs/adsorbed_derivative.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorbed_derivative.txt
- path: `/app/outputs/adsorbed_derivative.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The key result demonstrating that the adsorption-induced change in the slope parameter b is negligible; it represents the adsorbed finite-difference derivative of α∥ for H₂ (v=0→1). The checker compares this scalar to the hidden paper-gold value within a tolerance.
- schema:
  - `type`: text
  - `description`: A single floating-point number on a single line, representing the computed adsorbed finite-difference derivative of the parallel polarizability α∥ for H₂ (v=0→1) in units e²a₀²E_h⁻¹.

Note: Only the final derivative scalar is verified against the paper's result.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorbed_derivative.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number on a single line, representing the computed adsorbed finite-difference derivative of the parallel polarizability α∥ for H₂ (v=0→1) in units e²a₀²E_h⁻¹."
      },
      "description": "The key result demonstrating that the adsorption-induced change in the slope parameter b is negligible; it represents the adsorbed finite-difference derivative of α∥ for H₂ (v=0→1). The checker compares this scalar to the hidden paper-gold value within a tolerance."
    }
  ],
  "notes": "Only the final derivative scalar is verified against the paper's result."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `/app/outputs/adsorbed_derivative.txt` and compares the numerical value to a reference gold value. The reward is based on the agreement, within a tolerance that accounts for numerical rounding. Correct implementation of the described semi-harmonic correction is required to obtain the correct value. No other output files are scored.