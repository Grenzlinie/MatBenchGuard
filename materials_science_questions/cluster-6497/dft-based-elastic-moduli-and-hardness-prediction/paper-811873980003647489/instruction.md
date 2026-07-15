# Atomistic simulation of Ba2RE3+NbO6 double perovskites using GULP

## Problem background
Ba₂RE³⁺NbO₆ (RE = rare earth or Y) ordered double perovskites are promising microwave dielectric materials, but the systematic variation of their structural, dielectric, elastic, and mechanical properties across the lanthanide series is poorly understood. The tolerance factor, a geometric parameter that depends on the ionic radii, is expected to influence these properties, yet the character of the trends and the behaviour at the morphotropic phase boundaries between cubic, tetragonal, and monoclinic structures remain open questions. This task requires predicting these physical quantities and their dependence on the tolerance factor through atomistic simulations of the entire series.

## Approach
Use the General Utility Lattice Program (GULP) to perform static lattice‑energy minimisations of each Ba₂RENbO₆ compound in its ordered double‑perovskite structure. The interionic forces are described by a pair‑potential model: Buckingham short‑range terms plus long‑range Coulomb interactions. The Ba²⁺–O²⁻, Nb⁵⁺–O²⁻, and O²⁻–O²⁻ interactions are treated with the core‑shell model (published parameters are supplied), while the RE³⁺ ion is modelled as a rigid ion. The RE³⁺–O²⁻ interaction potentials must be derived following the paper’s procedure: start from an initial literature potential for La–O (e.g., from Lewis and Catlow), optimise it against the experimental structure and dielectric constant of Ba₂LaNbO₆, recursively generate initial potentials for all other RE ions via the relation A_i = A_j exp((R_i – R_j)/ρ) using tabulated ionic radii, and finally refine all RE–O potentials simultaneously against the available experimental structural data and dielectric constants. After relaxing each crystal at constant pressure in the experimentally reported space group, extract the equilibrium lattice parameters, static dielectric constant, and the independent elastic‑constant components. From the elastic tensor, compute the polycrystalline bulk modulus via Voigt–Reuss–Hill averaging and the P‑ and S‑wave sound velocities. Record the final lattice energy of each relaxed structure. With the full series of computed data, fit simple linear relations of the bulk modulus and lattice energy against the tolerance factor.

## Reproduction target
For each of the 16 RE ions (La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Y, Er, Tm, Yb, Lu), compute the equilibrium lattice constants, static dielectric constant, independent elastic moduli, polycrystalline bulk modulus, sound‑wave velocities, and lattice energy. Then perform two least‑squares linear regressions: bulk modulus as a function of tolerance factor, and lattice energy as a function of tolerance factor. Deliver the per‑compound properties in a CSV and the two regression equations in a plain‑text file.

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/

## Workflow steps

### Step 1: Derive RE³⁺–O²⁻ interaction potentials
- Role: process
- Action: (a) Obtain an initial set of RE³⁺–O²⁻ Buckingham parameters for La–O from the literature (e.g., Lewis and Catlow); (b) perform lattice-energy minimisation on Ba₂LaNbO₆ and optimise the La–O parameters to reproduce the experimental structural data (lattice parameters) and static dielectric constant; (c) using the optimised La–O parameters and the ionic radii of all RE ions (available from standard tables), apply the recursive relation A_i = A_La * exp((R_i - R_La)/ρ) to generate initial potentials for all other RE³⁺ ions; (d) refine all RE–O potentials simultaneously by fitting to the experimental structural data and dielectric constants of the corresponding Ba₂RENbO₆ compounds, yielding a final set of RE–O parameters. Output the derived parameters.
- Evidence: `/app/outputs/derived_potentials.csv`
- Format: csv
- Contract: RE (string), A (eV, float), ρ (Å, float). C is zero for all RE–O interactions.

### Step 2: Simulate properties for all Ba2RE3+NbO6 compounds using derived potentials
- Role: scored (load-bearing)
- Action: For each of the 16 RE ions (La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Y, Er, Tm, Yb, Lu): (a) set up the ordered double perovskite crystal structure in its appropriate space group (cubic Fm-3m, tetragonal I4/m, or monoclinic I2/m) using the experimentally reported lattice parameters and atomic positions; (b) create a GULP input file with the pair-potential model (Buckingham + core-shell) using the literature parameters for Ba–O, Nb–O, O–O (Table 1 of the source work) and the derived RE–O parameters from Step 1; (c) run a constant-pressure lattice geometry optimisation; (d) after convergence, extract the equilibrium lattice parameters, static dielectric constant, and the independent components of the elastic constant tensor (Nye notation); (e) compute the polycrystalline bulk modulus by Voigt-Reuss-Hill averaging, the P-wave and S-wave sound velocities from the elastic constants and density, and the lattice energy of the relaxed structure. Write all extracted and derived values to computed_properties.csv.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: RE (string), t (float, tolerance factor), space_group (string), a (Å, float), b (Å, float; NaN if not applicable), c (Å, float; NaN if cubic), beta (deg, float; NaN if not monoclinic), dielectric_constant (float), C11 (GPa, float), C12 (GPa, float), C44 (GPa, float), C13 (GPa, float), C33 (GPa, float), C66 (GPa, float), C15 (GPa, float), C25 (GPa, float), C35 (GPa, float), C46 (GPa, float), bulk_modulus (GPa, float), lattice_energy (eV, float), S_wave_velocity (m/s, float), P_wave_velocity (m/s, float). Elastic constants not relevant for a given symmetry are set to 0.0.
- Scoring: scored by hidden verifier

### Step 3: Fit linear relations between bulk modulus / lattice energy and tolerance factor
- Role: scored
- Action: Load computed_properties.csv. Perform a simple least-squares linear regression of bulk_modulus versus tolerance_factor t and of lattice_energy versus t. Write the two fitted lines as equations in the form 'B = a_B + b_B * t' and 'E_L = a_E + b_E * t', replacing the constants with the regressed coefficients.
- Output file: `/app/outputs/linear_fits.txt`
- Format: txt
- Contract: Two lines, each formatted as 'B = <float> + <float> * t' and 'E_L = <float> + <float> * t'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`
- `/app/outputs/linear_fits.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium properties for the 16 Ba2RE3+NbO6 compounds computed from GULP minimisations with derived RE–O potentials.
- schema:
  - `columns`: `RE`, `t`, `space_group`, `a`, `b`, `c`, `beta`, `dielectric_constant`, `C11`, `C12`, `C44`, `C13`, `C33`, `C66`, `C15`, `C25`, `C35`, `C46`, `bulk_modulus`, `lattice_energy`, `S_wave_velocity`, `P_wave_velocity`
  - `notes`: b, c, beta are NaN for cubic phases; missing elastic constants (due to symmetry) are set to 0.0.

### linear_fits.txt
- path: `/app/outputs/linear_fits.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Least-squares linear regression equations linking bulk modulus and lattice energy to the tolerance factor.
- schema:
  - `lines`: `B = <float> + <float> * t`, `E_L = <float> + <float> * t`

Notes: Only scored outputs are listed; the intermediate derived_potentials.csv is a required process artifact but not evaluated by the hidden verifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "RE",
          "t",
          "space_group",
          "a",
          "b",
          "c",
          "beta",
          "dielectric_constant",
          "C11",
          "C12",
          "C44",
          "C13",
          "C33",
          "C66",
          "C15",
          "C25",
          "C35",
          "C46",
          "bulk_modulus",
          "lattice_energy",
          "S_wave_velocity",
          "P_wave_velocity"
        ],
        "notes": "b, c, beta are NaN for cubic phases; missing elastic constants (due to symmetry) are set to 0.0."
      },
      "description": "Equilibrium properties for the 16 Ba2RE3+NbO6 compounds computed from GULP minimisations with derived RE–O potentials."
    },
    {
      "file": "/app/outputs/linear_fits.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "lines": [
          "B = <float> + <float> * t",
          "E_L = <float> + <float> * t"
        ]
      },
      "description": "Least-squares linear regression equations linking bulk modulus and lattice energy to the tolerance factor."
    }
  ],
  "notes": "Only scored outputs are listed; the intermediate derived_potentials.csv is a required process artifact but not evaluated by the hidden verifier."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact after your run. The computed properties in `computed_properties.csv` are compared against reference values using appropriate tolerances and direction‑aware scoring (meeting or exceeding a threshold earns full credit, while only larger deviations reduce the reward). The two regression equations in `linear_fits.txt` are compared to expected coefficients. The verifier also performs consistency checks, such as recomputing the bulk modulus from the elastic constants and verifying that the reported trends are reasonable for this family of compounds. The final reward is a weighted combination of the scores from the two stages, reflecting the quality of the reproduction. Simply quoting the paper's numbers is not sufficient; the hidden check is based on a genuine re‑execution of the workflow.
