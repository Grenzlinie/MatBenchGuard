# Upper bounds for the critical temperature of the Blume-Capel model

## Problem background
The Blume-Capel model is a spin-1 ferromagnetic system with nearest-neighbor exchange J > 0 and single-ion anisotropy D. Its critical temperature Tc demarcates the transition between ordered and disordered phases. Rigorous upper bounds for Tc can be derived by combining exact two-spin correlation identities with correlation inequalities (Griffiths I and II, Newman's). This yields lattice-specific inequalities for the two-point function; the condition where a sum of nearest-neighbor coefficients equals 1 provides an upper bound on Tc. This task reproduces those upper bounds for the honeycomb, square, and cubic lattices at two anisotropy limits.

## Approach
The approach implements the analytical derivation numerically. Starting from an exact identity for the spin-1 correlation function, one obtains an inequality of the form ⟨S0 Sl⟩ ≤ Σ a_j⟨Sj Sl⟩, where the coefficients a_j depend on the temperature T (through β = 1/kT with k=1, J=1) and the anisotropy D via the function f(x)=2 exp(βD) sinh(x) / (2 exp(βD) cosh(x)+1). The a_j are built from lattice-specific A_n coefficients (closed-form expressions involving f evaluated at multiples of βJ) and the one-dimensional correlation function. For each lattice (honeycomb: z=3, square: z=4, cubic: z=6) and each D (0, ∞), the critical temperature upper bound is the root of the equation Σ_{nearest neighbors} a_j = 1. The task is to code these formulas and solve the root-finding problem numerically, using standard Python libraries.

## Reproduction target
For each of the three lattices (honeycomb, square, cubic) and each anisotropy value D=0 and D=∞, numerically find the temperature T (i.e., the dimensionless kTc/J) such that the sum over nearest neighbours of a_j equals 1. For honeycomb: 3 a_j = 1; square: 4 a_j = 1; cubic: 6 a_j = 1. Set J=1 throughout. Write the six resulting upper-bound values to the file critical_temperatures.csv with columns lattice, D, kTc_over_J.

## Assets

- NumPy: numpy
- SciPy: scipy

## Mathematical formulas

The core function is: f(x) = 2 exp(βD) sinh(x) / (2 exp(βD) cosh(x) + 1), with k = βJ and J = 1.

For each lattice the A_n coefficients are:
**Honeycomb (z=3):**
A1 = 3 f(k)
A2 = 3 f(2k) - 6 f(k)
A3 = (1/4)[f(3k) - 3 f(k)]
A4 = (3/4)[5 f(k) + f(3k) - 4 f(2k)]

**Square (z=4):**
A1 = 4 f(k)
A2 = 6 f(2k) - 12 f(k)
A3 = f(3k) - 3 f(k)
A4 = 15 f(k) - 12 f(2k) + 3 f(3k)
A5 = (1/2)f(4k) - f(3k) - f(2k) + 3 f(k)
A6 = (1/2)f(4k) - 3 f(3k) + 7 f(2k) - 7 f(k)

**Cubic (z=6):**
A1 = 6 f(k)
A2 = -30 f(k) + 15 f(2k)
A3 = 5 f(3k) - 15 f(k)
A4 = 75 f(k) + 15 f(3k) - 60 f(2k)
A5 = -15 f(3k) + 45 f(k) + (15/2)f(4k) - 15 f(2k)
A6 = -45 f(3k) - 105[f(k) - f(2k)] + (15/2)f(4k)
A7 = (3/8)f(5k) - (15/8)f(3k) + (15/4)f(k)
A8 = (45/4)f(3k) - (105/2)f(k) + (15/4)f(5k) - 15 f(4k) + 30 f(2k)
A9 = -(3/8)f(5k) + (15/8)f(3k) - (15/4)f(k) + (3/16)f(6k) - (3/4)f(4k) + (15/16)f(2k)
A10 = (405/8)f(3k) + (315/4)f(k) + (15/8)f(5k) - 15 f(4k) - 90 f(2k)
A11 = -(5/4)f(3k) + (45/2)f(k) + (15/2)f(4k) - (135/8)f(2k) - (15/4)f(5k) + (5/8)f(6k)

The one-dimensional two-spin correlation (separated by two lattice sites) is:
⟨S₁S₂⟩_{1D} = (1 + √(1 - 2 f(2k))) / f(2k)

The per-neighbor coefficient a_j for each lattice is:
- Honeycomb: a_j = A1 - |A2| - |A3|·⟨S₁S₂⟩_{1D} + A4
- Square:    a_j = A1 - |A2| - |A3|·⟨S₁S₂⟩_{1D} + A4 + A5·⟨S₁S₂⟩_{1D} + A6
- Cubic:     a_j = A1 - |A2| - |A3|·⟨S₁S₂⟩_{1D} + A4 + A5·⟨S₁S₂⟩_{1D} + A6 + A7 + A8 + A9 + A10 + A11

For D=∞ the limit βD→∞ gives f(x) = tanh(x); for D=0 use the expression above.

## Workflow steps

### Step 1: Implement coefficient functions and 1D correlations
- Role: process
- Action: Using the explicit formulas in the Mathematical formulas section above, implement f(x), the A_n coefficients (given in closed form), and the one-dimensional correlation formula. Then compute the per-neighbor coefficient a_j and the total nearest-neighbour sum for each case, as needed for the next step.
- Evidence: none

### Step 2: Solve for critical temperature bounds
- Role: scored (load-bearing)
- Action: For each of the three lattices (honeycomb, square, cubic) and each anisotropy D=0 and D=∞, numerically solve for temperature T such that the sum over nearest neighbours of a_j equals 1 (honeycomb: 3*a_j=1; square: 4*a_j=1; cubic: 6*a_j=1). Use J=1 throughout. Write the six resulting kTc/J values to critical_temperatures.csv.
- Output file: `/app/outputs/critical_temperatures.csv`
- Format: csv
- Contract: Columns: lattice (string: honeycomb/square/cubic), D (string: 0 or Inf), kTc_over_J (float). One row per lattice/D combination, total 6 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_temperatures.csv
- path: `/app/outputs/critical_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Six upper bound critical temperature values (kTc/J) for honeycomb, square, cubic lattices at D=0 and D=∞.
- schema:
  - `type`: table
  - `required_columns`: `lattice`, `D`, `kTc_over_J`
  - `units`:
    - `kTc_over_J`: dimensionless (k_B T_c / J)

Notes: The agent must compute the values; the hidden gold reference values are the paper's reported numbers. The checker will compare each reported kTc_over_J to the hidden gold with an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice",
          "D",
          "kTc_over_J"
        ],
        "units": {
          "kTc_over_J": "dimensionless (k_B T_c / J)"
        }
      },
      "description": "Six upper bound critical temperature values (kTc/J) for honeycomb, square, cubic lattices at D=0 and D=∞."
    }
  ],
  "notes": "The agent must compute the values; the hidden gold reference values are the paper's reported numbers. The checker will compare each reported kTc_over_J to the hidden gold with an appropriate tolerance."
}
```

## How you are scored
A hidden verifier reads your critical_temperatures.csv and compares each kTc_over_J value to independently known reference values. The comparison uses an appropriate tolerance expected for a correct numerical implementation. The reward is proportional to the number of values that fall within the tolerance; full credit is awarded when all six values are consistent with the paper's rigorous bounds. Reporting numbers without performing the required computation (e.g., by hardcoding or guessing) will not match the hidden reference values.
