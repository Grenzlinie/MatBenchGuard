# Thermodynamic Functions of Gaseous YF3 and Y2F6 from Molecular Constants

## Problem background
Reliable thermodynamic data for yttrium trifluoride (YF3) and its dimer (Y2F6) in the gas phase are required for thermodynamic modeling of high-temperature processes involving rare-earth halides. Experimental structural data for YF3 are ambiguous, and no thermodynamic functions were previously available for Y2F6. This task aims to compute the standard thermodynamic functions — constant-pressure heat capacity (Cp), entropy (S), reduced Gibbs energy (Phi), and enthalpy increment (H(T)-H(0)) — for both molecules using the rigid rotator-harmonic oscillator approximation in statistical thermodynamics.

## Approach
The thermodynamic functions are evaluated in the rigid rotator-harmonic oscillator approximation. The necessary molecular constants are provided below. Using these constants, compute the translational, rotational, and vibrational contributions to the molecular partition functions, then derive Cp, S, Phi = S − (H−H(0))/T, and H−H(0) at the specified temperatures.

The molecular constants are:

**YF3**
- Product of moments of inertia: IA·IB·IC = 15.3×10³ × 10⁻¹¹⁷ g³ cm⁶
- Harmonic vibrational frequencies (cm⁻¹) with degeneracies in parentheses:
  ν₁ = 575, ν₂ = 95, ν₃ = 595 (2), ν₄ = 140 (2)
- Symmetry number σ = 6
- Ground-state statistical weight pₓ = 1

**Y₂F₆**
- Product of moments of inertia: IA·IB·IC = 245.1×10⁴ × 10⁻¹¹⁷ g³ cm⁶
- Harmonic vibrational frequencies (cm⁻¹) — all non‑degenerate:
  ν₁ = 611, ν₂ = 579.8, ν₃ = 593, ν₄ = 554.7, ν₅ = 425, ν₆ = 414, ν₇ = 361,
  ν₈ = 360, ν₉ = 201, ν₁₀ = 196, ν₁₁ = 133, ν₁₂ = 125, ν₁₃ = 110, ν₁₄ = 105,
  ν₁₅ = 94, ν₁₆ = 69, ν₁₇ = 55, ν₁₈ = 38
- Symmetry number σ = 4
- Ground-state statistical weight pₓ = 1

Implement the standard rigid rotator and harmonic oscillator partition function formulas. The translational contribution uses the pressure 1 bar (10⁵ Pa). Compute the functions at four temperatures: 298.15 K, 1000 K, 2000 K, and 3000 K. All results must be reported on a per‑mole basis with the units specified in the output contract.

## Reproduction target
Write a script that computes the thermodynamic functions Cp (J/(mol·K)), S (J/(mol·K)), Phi (J/(mol·K)), and H_minus_H0 (kJ/mol) for YF3 and Y₂F₆ at T = 298.15, 1000, 2000, and 3000 K using the provided molecular constants and the rigid rotator‑harmonic oscillator approximation. Output the results to `/app/outputs/thermodynamic_functions.csv` with columns: molecule ("YF3" or "Y2F6"), T, Cp, S, Phi, H_minus_H0.

## Assets

- numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute thermodynamic functions
- Role: scored (load-bearing)
- Action: Implement the rigid rotator-harmonic oscillator statistical thermodynamic formulas to compute the standard thermodynamic functions (heat capacity Cp, entropy S, reduced Gibbs energy Phi, enthalpy increment H_minus_H0) for YF3 and Y2F6 using the provided molecular constants (product of moments of inertia, harmonic vibrational frequencies with degeneracies, symmetry numbers). Compute at temperatures 298.15 K, 1000 K, 2000 K, and 3000 K. Write the results to the output CSV file.
- Output file: `/app/outputs/thermodynamic_functions.csv`
- Format: csv
- Contract: CSV with columns: molecule (YF3 or Y2F6), T (K), Cp (J/(mol·K)), S (J/(mol·K)), Phi (J/(mol·K)), H_minus_H0 (kJ/mol). Row order: all YF3 rows then all Y2F6 rows, or any ordering as long as molecule and T are specified.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_functions.csv
- path: `/app/outputs/thermodynamic_functions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed thermodynamic functions for YF3 and Y2F6 in the rigid rotator-harmonic oscillator approximation. The checker will independently recompute these quantities from the same hidden molecular constants and compare fields using absolute tolerances.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `T`, `Cp`, `S`, `Phi`, `H_minus_H0`
  - `units`:
    - `T`: K
    - `Cp`: J/(mol·K)
    - `S`: J/(mol·K)
    - `Phi`: J/(mol·K)
    - `H_minus_H0`: kJ/mol
  - `rows`: 8 rows: 4 temperatures × 2 molecules. molecule exactly 'YF3' or 'Y2F6'.

Notes: All required molecular constants (product of moments of inertia, vibrational frequencies, symmetry numbers, ground-state weights) are provided in the instruction. The agent must implement the standard rigid rotator-harmonic oscillator partition function formulas. No polynomial fitting is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "T",
          "Cp",
          "S",
          "Phi",
          "H_minus_H0"
        ],
        "units": {
          "T": "K",
          "Cp": "J/(mol·K)",
          "S": "J/(mol·K)",
          "Phi": "J/(mol·K)",
          "H_minus_H0": "kJ/mol"
        },
        "rows": "8 rows: 4 temperatures × 2 molecules. molecule exactly 'YF3' or 'Y2F6'."
      },
      "description": "Computed thermodynamic functions for YF3 and Y2F6 in the rigid rotator-harmonic oscillator approximation. The checker will independently recompute these quantities from the same hidden molecular constants and compare fields using absolute tolerances."
    }
  ],
  "notes": "All required molecular constants (product of moments of inertia, vibrational frequencies, symmetry numbers, ground-state weights) are provided in the instruction. The agent must implement the standard rigid rotator-harmonic oscillator partition function formulas. No polynomial fitting is required."
}
```

## How you are scored
Your submitted `thermodynamic_functions.csv` will be checked by an automatic verifier. The verifier independently recomputes the same thermodynamic functions from the identical molecular constants (which are hidden from you) and compares each field in your file against its own computed reference. The comparison is performed per field (Cp, S, Phi, H_minus_H0) at each temperature for each molecule. Each field is either accepted or rejected based on an absolute tolerance set to absorb small numerical differences from different implementations. Your final reward is the fraction of those fields that pass the comparison. You do not need to match any particular published numbers exactly; the verifier checks consistency with a correct implementation of the rigid rotator‑harmonic oscillator model.
