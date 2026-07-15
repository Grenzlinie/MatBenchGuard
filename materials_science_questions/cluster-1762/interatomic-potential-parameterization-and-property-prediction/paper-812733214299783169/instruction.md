# Structural phase transition and elastic properties of ZnSe_xTe_{1-x} via effective interionic potential

## Problem background
The II-VI semiconductors ZnSe and ZnTe, and their alloys ZnSe_xTe_{1-x}, undergo pressure-induced first-order structural phase transitions from the zinc blende (B3) crystal structure to the rock-salt (B1) structure. Predicting the transition pressures, the associated volume collapses, and the elastic constants of these phases is important for understanding the high-pressure behavior of these materials. In this task an effective interionic interaction potential (EIoIP) is used to compute these properties across six alloy compositions (x = 0.0, 0.2, 0.55, 0.81, 0.93, 1.0).

## Approach
The interionic potential consists of a long-range Coulomb term with a modified ionic charge, a short-range overlap repulsion of the Hafemeister–Flygare type (exponential form with hardness and range parameters), and attractive van der Waals terms (dipole–dipole and dipole–quadrupole interactions). The van der Waals coefficients are computed from atomic polarizabilities using the Slater–Kirkwood variational method. The three material-dependent parameters (modified ionic charge, hardness, range) are fitted separately for the two end members ZnTe and ZnSe by solving the equilibrium condition and the bulk modulus relation at the experimental lattice constants. For the intermediate alloy compositions the parameters are obtained by linear interpolation (Vegard's law). Once the potential is determined for each composition, the Gibbs free energy at T = 0 K (i.e., enthalpy H = U + PV) is evaluated for the B3 and B1 phases. The nearest-neighbour distances are optimised at each pressure, and the structural phase transition pressure is identified as the point where the free energy difference ΔG = G_B3 – G_B1 crosses zero. The volume collapse at the transition is computed using the Murnaghan equation of state. Additionally, the second-order elastic constants C11, C12, and C44 are derived from analytical expressions that involve first and second derivatives of the short-range potentials evaluated at the equilibrium nearest-neighbour distances for the B3 phase at zero pressure; from these the bulk modulus, shear modulus C44, and tetragonal modulus Cs = (C11 – C12)/2 are obtained.

## Reproduction target
Using the effective interionic potential model described above, compute for each of the six compositions (ZnTe, ZnSe0.2Te0.8, ZnSe0.55Te0.45, ZnSe0.81Te0.19, ZnSe0.93Te0.07, ZnSe) the B3→B1 transition pressure (in GPa) and the associated volume collapse (in percent) at the transition. Write the results to `/app/outputs/transition_properties.csv` with columns: composition, transition_pressure_GPa, volume_collapse_percent. Also compute for the B3 phase at zero pressure the bulk modulus, the shear modulus C44, and the tetragonal modulus Cs (all in GPa). Write these to `/app/outputs/elastic_constants_b3.csv` with columns: composition, bulk_modulus_BT_GPa, shear_modulus_C44_GPa, tetragonal_modulus_Cs_GPa.

## Assets

- Ionic radii: Zn²⁺, Te²⁻, Se²⁻
- Lattice constants and bulk moduli for ZnTe and ZnSe
- Atomic polarizabilities for Zn, Se, Te

## Workflow steps

### Step 1: Compute van der Waals coefficients
- Role: process
- Action: Using standard atomic polarizabilities for Zn, Se, and Te, apply the Slater-Kirkwood variational method to compute the dipole-dipole (c_ij) and dipole-quadrupole (d_ij) van der Waals coefficients for each of the six compositions (pure ZnTe, ZnSe, and the four alloys). The alloy coefficients are obtained by mixing rules.
- Evidence: `/app/outputs/vdw_coefficients.csv`

### Step 2: Determine model parameters (Zm, b, rho)
- Role: process
- Action: For the pure end-members ZnTe and ZnSe, determine the three free parameters of the effective interionic potential (modified ionic charge Z_m, hardness parameter b, and range parameter rho) by solving the equilibrium condition dU/dr=0 at the experimental lattice constant and the bulk modulus condition d²U/dr² = (9kr₀)⁻¹ B_T. Use the vdW coefficients from step 1. Then, for each of the four alloy compositions ZnSe_xTe_{1-x} (x=0.2,0.55,0.81,0.93), compute the parameters via Vegard's law linear interpolation.
- Evidence: `/app/outputs/model_parameters.csv`

### Step 3: Compute phase transition pressures and volume collapses
- Role: scored (load-bearing)
- Action: For each composition, use the fitted interionic potential to compute the Gibbs free energy (at T=0 K) for the B3 (zinc blende) and B1 (rock-salt) phases as functions of pressure. Minimize the free energies with respect to nearest-neighbor distances. Find the transition pressure where the Gibbs free energy difference ΔG = G_B3 - G_B1 changes sign (crosses zero). Compute the associated volume collapse (ΔV/V(0) in percent) at that pressure using the Murnaghan equation of state. Write the results to a CSV file with columns: composition, transition_pressure_GPa, volume_collapse_percent.
- Output file: `/app/outputs/transition_properties.csv`
- Format: csv
- Contract: composition (string), transition_pressure_GPa (float), volume_collapse_percent (float)
- Scoring: scored by hidden verifier

### Step 4: Calculate second-order elastic constants at zero pressure
- Role: scored
- Action: For each composition, using the B3 phase potential parameters, compute the second-order elastic constants C11, C12, and C44 at ambient pressure (P=0) from analytical expressions that involve derivatives of the short-range potentials. From these, derive the bulk modulus B_T = (C11+2C12)/3, the shear modulus C44, and the tetragonal modulus C_s = (C11-C12)/2. Write the results to a CSV file with columns: composition, bulk_modulus_BT_GPa, shear_modulus_C44_GPa, tetragonal_modulus_Cs_GPa.
- Output file: `/app/outputs/elastic_constants_b3.csv`
- Format: csv
- Contract: composition (string), bulk_modulus_BT_GPa (float), shear_modulus_C44_GPa (float), tetragonal_modulus_Cs_GPa (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_properties.csv`
- `/app/outputs/elastic_constants_b3.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_properties.csv
- path: `/app/outputs/transition_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed B3 to B1 transition pressure and volume collapse for six compositions.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `transition_pressure_GPa`, `volume_collapse_percent`
  - `units`:
    - `transition_pressure_GPa`: GPa
    - `volume_collapse_percent`: %

### elastic_constants_b3.csv
- path: `/app/outputs/elastic_constants_b3.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Second-order elastic constants (bulk, shear, tetragonal moduli) for the B3 phase at zero pressure for six compositions.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `bulk_modulus_BT_GPa`, `shear_modulus_C44_GPa`, `tetragonal_modulus_Cs_GPa`
  - `units`:
    - `bulk_modulus_BT_GPa`: GPa
    - `shear_modulus_C44_GPa`: GPa
    - `tetragonal_modulus_Cs_GPa`: GPa

Notes: The checker compares the agent's reported transition pressures, volume collapses, and elastic constants against hidden reference values from the paper's Tables 3 and 4 using tolerances appropriate for a re-implemented potential.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "transition_pressure_GPa",
          "volume_collapse_percent"
        ],
        "units": {
          "transition_pressure_GPa": "GPa",
          "volume_collapse_percent": "%"
        }
      },
      "description": "Computed B3 to B1 transition pressure and volume collapse for six compositions."
    },
    {
      "file": "elastic_constants_b3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "bulk_modulus_BT_GPa",
          "shear_modulus_C44_GPa",
          "tetragonal_modulus_Cs_GPa"
        ],
        "units": {
          "bulk_modulus_BT_GPa": "GPa",
          "shear_modulus_C44_GPa": "GPa",
          "tetragonal_modulus_Cs_GPa": "GPa"
        }
      },
      "description": "Second-order elastic constants (bulk, shear, tetragonal moduli) for the B3 phase at zero pressure for six compositions."
    }
  ],
  "notes": "The checker compares the agent's reported transition pressures, volume collapses, and elastic constants against hidden reference values from the paper's Tables 3 and 4 using tolerances appropriate for a re-implemented potential."
}
```

## How you are scored
A hidden verifier reads the two output CSV files. It compares your computed transition pressures, volume collapses, and elastic constants against reference values derived from the original study. Comparisons use per‑property tolerances that are wide enough to absorb legitimate differences arising from re‑implementing the potential, numerical solvers, and equation-of-state handling, but tight enough that a plausible but incorrect guess would not pass. The verifier assigns partial credit for each numerical value that falls within the tolerance range, and combines the scores from both files into a single overall reward (0 to 1). The transition pressures and elastic constants carry the largest weight; the volume collapses contribute a smaller share.
