# Anisotropic negative thermal expansion and mode Grüneisen parameters of LaC2

## Problem background
The tetragonal phase of LaC2 is a superconducting material whose anisotropic thermal expansion has been reported experimentally, but a detailed first‑principles understanding of its thermal expansion and the underlying phonon mechanisms was lacking. The paper that motivates this task used density functional theory (DFT) and the quasiharmonic approximation (QHA) to compute the temperature‑dependent lattice parameters and coefficients of thermal expansion of LaC2, and to evaluate the mode Grüneisen parameters that govern the sign of thermal expansion along different crystallographic directions.

## Approach
The reproduction is a compute‑driven workflow that performs DFT total energy calculations and phonon calculations for tetragonal LaC2 (space group I4/mmm). You will first optimize the unit cell to obtain equilibrium lattice constants. Next, you will scan a set of volumes around equilibrium, relaxing internal coordinates at each volume to obtain static energies E0(V). For each volume, you will build a supercell (e.g., 3×3×2) and compute force constants via finite displacements using PHONOPY coupled with Quantum ESPRESSO, yielding phonon frequencies and densities of states. The vibrational free energy F_vib(V,T) is obtained from the phonon DOS within the quasiharmonic approximation. The total free energy F(V,T) = E0(V) + F_vib(V,T) is then fitted to the Vinet equation of state at each temperature T to find the equilibrium volume and extract the lattice parameters a(T) and c(T). Finally, from the volume dependence of the optical phonon frequencies at the Γ point, you will compute mode Grüneisen parameters γ_i = –d(ln ω_i)/d(ln V) for the Eu, Eg, A2u, and A2g modes.

## Reproduction target
Produce two scored artifacts:
- `/app/outputs/step_04_lattice_parameters_vs_T.csv`: a CSV with columns `T(K)`, `a(Å)`, `c(Å)` for temperatures T = 0, 5, 10, …, 300 K, obtained from the QHA free‑energy minimization.
- `/app/outputs/step_05_gruneisen_parameters.json`: a JSON object with keys `"E_u"`, `"E_g"`, `"A_2u"`, `"A_2g"` and numeric (unitless) Grüneisen parameter values.
The lattice‑parameter CSV will be used to numerically derive the linear thermal expansion coefficients α_c(T) and α_a(T) and the bulk coefficient α_V = 2α_a + α_c; these derived quantities constitute the main quantitative aim of the reproduction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PHONOPY: phonopy
- PBE pseudopotentials for La and C: https://dalcorso.github.io/pslibrary/
- LaC2 crystal structure

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform DFT geometry optimization of the tetragonal LaC2 unit cell using Quantum ESPRESSO to obtain equilibrium lattice constants, internal coordinate z, and total energy.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Volume-dependent static energies
- Role: process
- Action: Generate a set of volumes around the equilibrium volume (e.g., 15 points). For each volume, perform DFT total energy calculation while relaxing internal coordinates, keeping the cell shape fixed, to obtain E0(V) and relaxed atomic positions.
- Evidence: `/app/outputs/energies.dat`

### Step 3: Phonon frequency calculations
- Role: process
- Action: For each volume, build a supercell (e.g., 3x3x2) and compute force constants via finite displacements using PHONOPY coupled with Quantum ESPRESSO. Obtain phonon frequencies and densities of states for each volume.
- Evidence: `/app/outputs/phonon_summary.txt`

### Step 4: Quasiharmonic free energy minimization and lattice constants
- Role: scored (load-bearing)
- Action: For each volume, compute the vibrational Helmholtz free energy from the phonon density of states. Assemble the total free energy F(V,T) = E0(V) + F_vib(V,T). For each temperature T from 0 to 300 K in steps of 5 K, fit F(V,T) to the Vinet equation of state to obtain the equilibrium volume and extract temperature-dependent lattice parameters a(T) and c(T). Output these as a CSV file.
- Output file: `/app/outputs/step_04_lattice_parameters_vs_T.csv`
- Format: csv
- Contract: CSV with columns: T(K), a(Å), c(Å). Rows for temperatures 0,5,10,...,300 K.
- Scoring: scored by hidden verifier

### Step 5: Mode Grüneisen parameters at Γ
- Role: scored
- Action: From the volume-dependent phonon frequencies of the optical modes at the Γ point (Eu, Eg, A2u, A2g), compute the mode Grüneisen parameters γ_i = −d(ln ω_i)/d(ln V) numerically. Output these values in a JSON file.
- Output file: `/app/outputs/step_05_gruneisen_parameters.json`
- Format: json
- Contract: JSON object with keys 'E_u', 'E_g', 'A_2u', 'A_2g' mapping to numeric Grüneisen parameter values (unitless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_lattice_parameters_vs_T.csv`
- `/app/outputs/step_05_gruneisen_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_lattice_parameters_vs_T.csv
- path: `/app/outputs/step_04_lattice_parameters_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV with columns T(K), a(Å), c(Å). Numerically differentiated to obtain linear thermal expansion coefficients αc and αa, and then bulk αV. Compared against the paper's reported values (sign, magnitude, and temperature intervals) using tolerance ranges.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `a(Å)`, `c(Å)`
  - `units`:
    - `T(K)`: K
    - `a(Å)`: Angstrom
    - `c(Å)`: Angstrom

### step_05_gruneisen_parameters.json
- path: `/app/outputs/step_05_gruneisen_parameters.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON object with Grüneisen parameters for the optical modes at Γ. The checker verifies that E_u and E_g are negative (within expected bounded ranges) and that the values are consistent with the paper's reported sign and approximate magnitude.
- schema:
  - `type`: object
  - `required`:
    - `E_u`: number
    - `E_g`: number
    - `A_2u`: number
    - `A_2g`: number

Notes: The checker will numerically differentiate the lattice constants to compute linear CTEs. Averages will be taken over defined low-temperature windows (0–42 K for c-axis, 0–10 K for a-axis) and the bulk CTE αV = 2αa + αc will be compared to the paper's value with appropriate tolerances. The Grüneisen parameters are validated for sign and order-of-magnitude consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_lattice_parameters_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "a(Å)",
          "c(Å)"
        ],
        "units": {
          "T(K)": "K",
          "a(Å)": "Angstrom",
          "c(Å)": "Angstrom"
        }
      },
      "description": "CSV with columns T(K), a(Å), c(Å). Numerically differentiated to obtain linear thermal expansion coefficients αc and αa, and then bulk αV. Compared against the paper's reported values (sign, magnitude, and temperature intervals) using tolerance ranges."
    },
    {
      "file": "step_05_gruneisen_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "E_u": "number",
          "E_g": "number",
          "A_2u": "number",
          "A_2g": "number"
        }
      },
      "description": "JSON object with Grüneisen parameters for the optical modes at Γ. The checker verifies that E_u and E_g are negative (within expected bounded ranges) and that the values are consistent with the paper's reported sign and approximate magnitude."
    }
  ],
  "notes": "The checker will numerically differentiate the lattice constants to compute linear CTEs. Averages will be taken over defined low-temperature windows (0–42 K for c-axis, 0–10 K for a-axis) and the bulk CTE αV = 2αa + αc will be compared to the paper's value with appropriate tolerances. The Grüneisen parameters are validated for sign and order-of-magnitude consistency."
}
```

## How you are scored
A hidden verifier independently scores each of the two artifacts and combines the scores with equal weight to produce a final reward between 0 and 1.

For the lattice‑parameter CSV: the verifier numerically differentiates your a(T) and c(T) to obtain α_a(T) and α_c(T), then computes average CTEs over the temperature intervals reported in the paper. These averages and the bulk CTE α_V are compared against the paper’s reference values. The reward is monotonic: if your result equals or exceeds the paper’s value in the appropriate direction (e.g., a more pronounced NTE), you receive full credit; partial credit degrades only as the agreement becomes worse. Realistic tolerances are applied to account for legitimate differences in computational details (pseudopotentials, k‑point sampling, etc.).

For the Grüneisen‑parameter JSON: the verifier checks that the submitted parameters are within physically plausible bounds and are consistent with the paper’s reported values, again using tolerances that reflect the expected computational spread. The sign and magnitude of each parameter are evaluated against the paper’s findings.

You do not need to guess exact numbers; simply perform the computation honestly following the prescribed methodology, and the verifier will assess whether your results qualify as a faithful reproduction.
