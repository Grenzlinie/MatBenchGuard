# Barrier Heights and CVT/SCT Rate Constants for H + Si2H6 Reaction at G3MP2//UMP2 Level

## Problem background
The reaction of atomic hydrogen with disilane (Si₂H₆) is a model system for hydrogen‑silicon etching during plasma‑assisted chemical vapor deposition and semiconductor fabrication. The reaction can proceed via several competing channels: hydrogen abstraction, frontside substitution, and backside substitution. Quantitative knowledge of the energy barriers and rate constants for each channel is essential to understand etching rates, branching ratios, and the relative reactivity of Si–H bonds. In this task you will compute these quantities from first principles using a hierarchy of quantum chemical methods and variational transition state theory.

## Approach
You will investigate the potential energy surface of H + Si₂H₆ with ab initio molecular orbital theory and kinetic rate theory. First, perform geometry optimizations, vibrational frequency analyses, and intrinsic reaction coordinate (IRC) calculations for all stationary points at the UMP2(full)/6‑31G(d,p) level. This provides the minimum energy paths (MEPs), Hessian matrices, and zero‑point energies needed for kinetics. Next, refine the energies using the G3MP2 composite method, which combines QCISD(T) and UMP2 single‑point calculations with a high‑level empirical correction and the scaled zero‑point energy. From the refined G3MP2 energies you extract the forward and reverse barriers and the heat of reaction for each channel. Finally, you perform canonical variational transition state theory (CVT) with small‑curvature tunneling (SCT) correction along each MEP to obtain rate constants. The entire pipeline is implemented with open‑source quantum chemistry software and Python scientific libraries.

## Reproduction target
Your goal is to compute the G3MP2//UMP2(full)/6‑31G(d,p) forward and reverse energy barriers and heats of reaction for the three reaction channels (hydrogen abstraction, frontside substitution, and backside substitution), and to compute the canonical variational transition state theory (CVT/SCT) rate constants at 298 K for each individual channel (denoted k₁, k₂ₐ, k₂ᵦ) and for the total overall rate constant (k_total = k₁ + k₂ₐ + k₂ᵦ). Report the barriers and heats in `barriers_and_heats.csv` and the rate constants in `rate_constants_298K.csv` using the exact schemas and units specified in the workflow steps.

## Assets

- Open-source quantum chemistry package (e.g., PySCF, ORCA, Psi4): https://pyscf.org/ (alternative: https://orcaforum.kofo.mpg.de/, https://psicode.org/)
- Basis set definitions (6-31G(d,p) and G3MP2large): https://www.basissetexchange.org/
- Python 3 with numpy and scipy: numpy, scipy

## Workflow steps

### Step 1: Reference QM calculations (geometry, TS, frequencies, MEP)
- Role: process
- Action: Perform UMP2(full)/6-31G(d,p) geometry optimizations for all reactants (Si₂H₆ staggered, H), products (Si₂H₅, H₂, SiH₄, SiH₃), and transition states for the three channels (abstraction TS₁, frontside substitution TS₂ₐ, backside substitution TS₂ᵦ). Verify transition states by checking for a single imaginary frequency and by intrinsic reaction coordinate (IRC) calculations. Compute harmonic vibrational frequencies and zero-point energies (scaled by 0.95). For each channel, generate the minimum energy path (MEP) in mass-weighted Cartesian coordinates with a step size of 0.05 amu^{1/2}·bohr, and compute the Hessian matrices at stationary points and at selected non-stationary points along the MEP.
- Evidence: `/app/outputs/qm_calc_summary.json`

### Step 2: G3MP2 energy refinement
- Role: process
- Action: Using the geometries from step_01, perform single-point energy calculations at the QCISD(T)/6-31G(d), UMP2/6-31G(d), and UMP2/G3MP2large levels for all stationary points and selected non-stationary points along each MEP. Combine the energies using the G3MP2 formula: E(G3MP2) = E(QCISD(T)/6-31G(d)) + E(UMP2/G3MP2large) − E(UMP2/6-31G(d)) + HLC + ZPE, where HLC = −0.004471·n_α − 0.004808·n_β and ZPE is the scaled zero-point energy from step_01.
- Evidence: `/app/outputs/g3mp2_energies.json`

### Step 3: Energy barriers and reaction heats
- Role: scored
- Action: From the G3MP2 energies of the stationary points, calculate the forward and reverse energy barriers and the heat of reaction for each of the three channels: abstraction, frontside substitution, and backside substitution. Write the results to barriers_and_heats.csv.
- Output file: `/app/outputs/barriers_and_heats.csv`
- Format: csv
- Contract: CSV with columns: channel (string: abstraction, frontside, backside), forward_barrier (float, kJ/mol), reverse_barrier (float, kJ/mol), heat_of_reaction (float, kJ/mol). One row per channel.
- Scoring: scored by hidden verifier

### Step 4: CVT/SCT rate constants at 298 K
- Role: scored (load-bearing)
- Action: Using the refined G3MP2 MEP energies from step_02 and the Hessian matrices from step_01, perform a canonical variational transition state theory (CVT) calculation with small-curvature tunneling (SCT) correction for each reaction channel. Evaluate the rate constants at 298 K for the abstraction (k₁), frontside substitution (k₂ₐ), backside substitution (k₂ᵦ), and total overall rate constant (k_total = k₁ + k₂ₐ + k₂ᵦ). Write the results to rate_constants_298K.csv.
- Output file: `/app/outputs/rate_constants_298K.csv`
- Format: csv
- Contract: CSV with columns: channel (string: k1, k2a, k2b, k_total), rate_constant (float, L·molecule⁻¹·s⁻¹). One row per channel.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers_and_heats.csv`
- `/app/outputs/rate_constants_298K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers_and_heats.csv
- path: `/app/outputs/barriers_and_heats.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Energy barriers and heats of reaction for the three reaction channels (abstraction, frontside, backside) at the G3MP2//UMP2(full)/6-31G(d,p) level.
- schema:
  - `type`: table
  - `required_columns`: `channel`, `forward_barrier`, `reverse_barrier`, `heat_of_reaction`
  - `units`:
    - `forward_barrier`: kJ/mol
    - `reverse_barrier`: kJ/mol
    - `heat_of_reaction`: kJ/mol

### rate_constants_298K.csv
- path: `/app/outputs/rate_constants_298K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CVT/SCT rate constants at 298 K for the three individual channels (k1, k2a, k2b) and the total overall rate constant (k_total).
- schema:
  - `type`: table
  - `required_columns`: `channel`, `rate_constant`
  - `units`:
    - `rate_constant`: L·molecule⁻¹·s⁻¹

Notes: The hidden gold values are the paper-reported barriers, heats, and rate constants. The checker compares submitted values to these with appropriate tolerances (tight for energies, relative for rate constants). No further public details are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers_and_heats.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "channel",
          "forward_barrier",
          "reverse_barrier",
          "heat_of_reaction"
        ],
        "units": {
          "forward_barrier": "kJ/mol",
          "reverse_barrier": "kJ/mol",
          "heat_of_reaction": "kJ/mol"
        }
      },
      "description": "Energy barriers and heats of reaction for the three reaction channels (abstraction, frontside, backside) at the G3MP2//UMP2(full)/6-31G(d,p) level."
    },
    {
      "file": "rate_constants_298K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "channel",
          "rate_constant"
        ],
        "units": {
          "rate_constant": "L·molecule⁻¹·s⁻¹"
        }
      },
      "description": "CVT/SCT rate constants at 298 K for the three individual channels (k1, k2a, k2b) and the total overall rate constant (k_total)."
    }
  ],
  "notes": "The hidden gold values are the paper-reported barriers, heats, and rate constants. The checker compares submitted values to these with appropriate tolerances (tight for energies, relative for rate constants). No further public details are disclosed."
}
```

## How you are scored
A hidden verifier will independently score each workflow artifact. For the scored CSV files, the verifier compares your computed values to reference results, allowing for the small numerical differences that arise from using a different quantum chemistry implementation. Meeting or exceeding the required accuracy on both scored artifacts earns full credit; the final reward is a weighted combination of the scores from `barriers_and_heats.csv` and `rate_constants_298K.csv`. The process evidence files (`qm_calc_summary.json` and `g3mp2_energies.json`) are not scored but must be produced to confirm that the full computational pipeline was executed. No further details about the reference values or tolerances are disclosed – carry out the computation as faithfully as possible.
