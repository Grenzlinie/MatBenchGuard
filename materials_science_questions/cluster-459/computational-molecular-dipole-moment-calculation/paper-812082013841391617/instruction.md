# Reproducing MCSCF dipole moment function and vibrational matrix elements for CO

## Problem background
The electric dipole moment function (EDMF) of carbon monoxide (CO) is critical for predicting intensities of vibration-rotation transitions, which are central to astrophysical applications (e.g., interpreting stellar spectra) and to CO gas laser operation. The accuracy of these predicted intensities hinges on the quality of the EDMF and on the vibrational dipole matrix elements derived from it. This task requires computing a reliable EDMF using multi-configuration self-consistent field (MCSCF) wavefunctions and then calculating the rotationless dipole matrix elements for the fundamental and first overtone transitions.

## Approach
The approach is a computational quantum chemistry pipeline. First, a Gaussian basis set (11s6p3d) for carbon and oxygen is constructed from Huzinaga's primitive sets, augmented with diffuse and polarization functions. A 30-configuration reference space is defined; it includes all configurations needed for proper dissociation of CO into the two asymptotic ¹Σ⁺ states, additional spin couplings, and selected double excitations to 7σ/3π orbitals. State-averaged MCSCF calculations are then performed on the CO molecule at a series of internuclear distances. To prevent orbital reorganization at large distances, a very small weight is used for the second ¹Σ⁺ state in the averaging. From the optimized wavefunctions the electric dipole moment is computed at each distance, yielding the dipole moment function. In parallel, the RKR potential energy function for the electronic ground state of CO is taken from the literature (Kirschner & Watson, 1974). Solving the radial Schrödinger equation with this potential gives vibrational wavefunctions. The dipole moment function and the vibrational wavefunctions are then combined to compute the rotationless (J=0) dipole matrix elements for the desired transitions.

## Reproduction target
Produce the following two results, writing them as CSV files in /app/outputs:
1. The MCSCF dipole moment function: for the specified internuclear distances (1.5–6.0 a0, including equilibrium), compute the dipole moment (in ea0, with polarity C⁺O⁻) and collect the (distance, dipole) pairs.
2. The rotationless dipole matrix elements: using the RKR potential of Kirschner & Watson (1974) and the dipole moment function from step 1, compute and report the matrix elements (in Debye) for the fundamental (v′=1, v″=0) and first overtone (v′=2, v″=0) transitions.

## Assets

- Basis Set Exchange (Huzinaga primitive Gaussian basis sets for C and O): url: https://www.basissetexchange.org/
- PySCF quantum chemistry package: package: pyscf (pip install pyscf)
- RKR potential energy function for CO (Kirschner & Watson 1974): doi: 10.1016/0022-2852(74)90128-1

## Workflow steps

### Step 1: Basis set preparation
- Role: process
- Action: Construct the 11s6p3d Gaussian basis set for carbon and oxygen. Start from Huzinaga's 10s/5p primitive sets (available from Basis Set Exchange). Contract the innermost 4s and 2p functions. Augment with diffuse s and p functions and three d polarization functions. For oxygen: diffuse s exponents 0.3 and 0.12 (replacing the smallest s exponent), diffuse p exponents 0.25 and 0.09 (replacing the outermost p), d exponents 3.0, 1.0, 0.3. For carbon: diffuse s exponents 0.16 and 0.06, diffuse p exponents 0.14 and 0.05, d exponents 1.5, 0.5, 0.15. The resulting basis set will be used in all subsequent MCSCF calculations.
- Evidence: none

### Step 2: Configuration reference space definition
- Role: process
- Action: Define the MCSCF(30) configuration set. The reference space must include: (a) 19 configurations essential for proper dissociation and bond formation: all spin- and space-symmetry adapted configurations from distributing valence electrons among 5σ, 6σ, 1π, 2π orbitals to describe the two asymptotic ¹Σ⁺ states (M_L=0 and M_L=1). Concretely, these are the configurations listed in the paper: |5σ²,6σ²,(5σ6σ)|¹Σ⁺ × |1π⁴,1π_x²2π_y²+2π_x²1π_y²,³(1π_x2π_x)³(1π_y2π_y),2π⁴|¹Σ⁺ plus configurations coupling 1π³2π and 1π2π³ with the σ-space triplets. (b) add the remaining 5 configurations obtained by different spin couplings of the above (the 24-configuration set). (c) add 6 double excitations from the Hartree-Fock determinant into 7σ/3π orbitals: 7σ²1π⁴, 5σ² × [(1π_x²3π_x²+1π_y²3π_y²), ¹(1π_x3π_x)¹(1π_y3π_y)], |(5σ6σ)|¹Σ⁺ × |1π³3π|¹Σ⁺, |(5σ7σ)|¹Σ⁺ × |1π³2π, 1π³3π|¹Σ⁺. The total is 30 configurations. This set is used in all MCSCF calculations.
- Evidence: none

### Step 3: MCSCF dipole moment calculation
- Role: scored (load-bearing)
- Action: For the CO molecule at internuclear distances r = 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.13183, 2.3, 2.5, 2.8, 3.1, 3.4, 3.7, 4.0, 4.5, 5.0, 5.5, 6.0 a0, perform state-averaged MCSCF(30) calculations. Use the energy-averaging protocol with the two lowest ¹Σ⁺ states and a very small weight ratio W2/W1 = 0.001 to prevent orbital reorganization at large distances. At each distance, compute the dipole moment (in ea0, positive sign corresponds to C⁺O⁻). Write the (r, dipole_moment) pairs to /app/outputs/dipole_moment_function.csv.
- Output file: `/app/outputs/dipole_moment_function.csv`
- Format: csv
- Contract: r (a0), dipole_moment (ea0). One row per distance.
- Scoring: scored by hidden verifier

### Step 4: Vibrational dipole matrix elements
- Role: scored (load-bearing)
- Action: Obtain the RKR potential energy function for the ground state of CO from Kirschner & Watson (1974) [J. Mol. Spectrosc. 51, 321]. Solve the radial Schrödinger equation numerically (e.g., Cooley's method) to obtain vibrational wavefunctions. Using the dipole moment function from step_03 and the RKR potential, compute the rotationless (J=0) dipole matrix elements M_{v'}^{v''} for the fundamental (v'=1, v''=0) and first overtone (v'=2, v''=0) transitions. Convert the matrix elements to Debye (1 ea0 = 2.54158 D). Write the results to /app/outputs/dipole_matrix_elements.csv.
- Output file: `/app/outputs/dipole_matrix_elements.csv`
- Format: csv
- Contract: v_prime, v_double_prime, matrix_element_D. Two rows: (1,0) and (2,0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_moment_function.csv`
- `/app/outputs/dipole_matrix_elements.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_moment_function.csv
- path: `/app/outputs/dipole_moment_function.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: MCSCF(30) dipole moment at specified internuclear distances. The checker compares each value to the paper's hidden reference within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `r`, `dipole_moment`
  - `units`:
    - `r`: a0
    - `dipole_moment`: ea0

### dipole_matrix_elements.csv
- path: `/app/outputs/dipole_matrix_elements.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Rotationaless dipole matrix elements for fundamental (1-0) and first overtone (2-0) transitions, computed with RKR potential and MCSCF dipole function.
- schema:
  - `type`: table
  - `required_columns`: `v_prime`, `v_double_prime`, `matrix_element_D`
  - `units`:
    - `matrix_element_D`: Debye

Notes: The target policy is exact_match because the quantities are fixed physical numbers determined by the specified method and inputs. Hidden tolerances absorb expected implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_moment_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "dipole_moment"
        ],
        "units": {
          "r": "a0",
          "dipole_moment": "ea0"
        }
      },
      "description": "MCSCF(30) dipole moment at specified internuclear distances. The checker compares each value to the paper's hidden reference within a tolerance."
    },
    {
      "file": "dipole_matrix_elements.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "v_prime",
          "v_double_prime",
          "matrix_element_D"
        ],
        "units": {
          "matrix_element_D": "Debye"
        }
      },
      "description": "Rotationaless dipole matrix elements for fundamental (1-0) and first overtone (2-0) transitions, computed with RKR potential and MCSCF dipole function."
    }
  ],
  "notes": "The target policy is exact_match because the quantities are fixed physical numbers determined by the specified method and inputs. Hidden tolerances absorb expected implementation spread."
}
```

## How you are scored
A hidden verifier automatically evaluates your work after submission. It inspects the two scored output files, checks they conform to the required CSV schema, and then compares the values you reported for dipole moments and matrix elements to hidden reference values using domain-appropriate tolerances. The final score (a number between 0 and 1) is a weighted combination of the results from the two outputs. Simply copying the paper's reported numbers is not sufficient — you must execute the computational pipeline described above and submit the numbers that pipeline produces.
