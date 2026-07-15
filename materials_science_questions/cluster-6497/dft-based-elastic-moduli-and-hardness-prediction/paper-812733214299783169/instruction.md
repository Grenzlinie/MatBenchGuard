# Computing high-pressure phase transition and elastic properties of ZnSeTe alloys using an effective interionic potential

## Problem background
II‑VI semiconductor alloys ZnSe_xTe_{1-x} exhibit a pressure‑induced structural phase transition from the zinc blende (B3) to the rock‑salt (B1) crystal structure. Reliable prediction of the transition pressure, the associated volume collapse, and the pressure‑dependent elastic constants is essential for understanding the mechanical stability of these materials under high pressure. This work models these properties using an effective interionic interaction potential (EIoIP) that includes long‑range Coulomb forces, short‑range overlap repulsion of the Hafemeister–Flygare type, and van der Waals interactions.

## Approach
The approach is to construct an effective interionic potential U(r) that sums Coulomb, overlap repulsion, and van der Waals (dipole–dipole and dipole–quadrupole) terms. For the two parent compounds ZnTe and ZnSe, the three material‑dependent parameters (modified ionic charge Z_m, hardness b, and range ρ) are determined by solving the equilibrium condition (dU/dr = 0 at the observed nearest‑neighbor separation) together with the relation linking the second derivative of the potential to the experimental bulk modulus. For the mixed compositions ZnSe_xTe_{1-x} the parameters are obtained by linear interpolation of the end‑compound values (Vegard’s law).

Once the potential is fully parameterized, the Gibbs free energies G = U + PV (evaluated at T = 0 K) of the B3 and B1 phases are computed as functions of the nearest‑neighbor separation and minimized to find the equilibrium separations at each pressure. The transition pressure P_t is identified as the pressure where ΔG = G_{B3} − G_{B1} = 0. The relative volume collapse at the transition is then obtained from the Murnaghan equation of state, which relates volume change to pressure and bulk modulus.

The second‑order elastic constants (C11, C12, C44) are calculated analytically from the first and second derivatives of the short‑range repulsive potentials using the standard expressions for both the B3 and B1 phases. From these, the bulk modulus B_T, shear modulus C44, and tetragonal modulus C_s are derived. The elastic constants are evaluated at ambient pressure for all compositions and also as a function of pressure across the phase transition, with the expected monotonic increase and a discontinuity at P_t.

## Reproduction target
Reproduce the following quantitative results for the six compositions ZnSe_xTe_{1-x} with x = 0.0, 0.2, 0.55, 0.81, 0.93, 1.0:

- Phase transition pressure P_t (GPa) and relative volume collapse ΔV/V0 (%) at the B3→B1 transition.
- Ambient‑pressure elastic moduli in the zinc blende (B3) phase: bulk modulus B_T (GPa), shear modulus C44 (GPa), and tetragonal modulus C_s (GPa).
- For at least one composition (e.g., x = 0.0), a pressure‑dependent curve of the second‑order elastic constants C11, C12, C44 covering pressures from 0 to well above the transition, showing a monotonic increase in each constant with pressure and a conspicuous discontinuity at the phase boundary.

## Assets

- numpy: numpy
- scipy: scipy
- Crystal data and vdW coefficients for ZnSe and ZnTe

## Workflow steps

### Step 1: Fit EIoIP parameters for ZnTe and ZnSe
- Role: process
- Action: Using the provided lattice constant, bulk modulus, and vdW coefficients, determine the three model parameters (Z_m, b, ρ) for ZnTe and ZnSe by solving the equilibrium condition dU/dr=0 and the bulk modulus relation.
- Evidence: `/app/outputs/fit_parameters.json`

### Step 2: Derive alloy model parameters via Vegard's law
- Role: process
- Action: Linearly interpolate the fitted end-compound parameters (Z_m, b, ρ) to obtain the parameters for ZnSe_xTe_{1-x} at the six specified compositions (x = 0.0, 0.2, 0.55, 0.81, 0.93, 1.0).
- Evidence: `/app/outputs/alloy_parameters.csv`

### Step 3: Compute phase transition pressures and volume collapses
- Role: scored (load-bearing)
- Action: For each composition, compute the Gibbs free energies of the B3 and B1 phases as a function of nearest-neighbor separation, minimize them to obtain equilibrium separations at each pressure, and find the transition pressure P_t where ΔG = G_B3 − G_B1 = 0. Compute the associated relative volume collapse ΔV/V0 at P_t using the Murnaghan equation of state.
- Output file: `/app/outputs/transition_data.csv`
- Format: csv
- Contract: Columns: composition_x (float), transition_pressure_GPa (float), volume_collapse_percent (float).
- Scoring: scored by hidden verifier

### Step 4: Compute ambient elastic constants in B3 phase
- Role: scored
- Action: Using the fitted EIoIP parameters and the formulas for C11, C12, C44 in the zinc blende phase, compute the second-order elastic constants and derived moduli (bulk modulus B_T, shear modulus C44, tetragonal modulus C_s) at ambient pressure for all six compositions.
- Output file: `/app/outputs/elastic_constants_B3.csv`
- Format: csv
- Contract: Columns: composition_x (float), B_T_GPa (float), C44_GPa (float), C_s_GPa (float).
- Scoring: scored by hidden verifier

### Step 5: Compute pressure-dependent SOEC and detect discontinuity
- Role: scored
- Action: For at least one composition (e.g., x=0.0), calculate the second-order elastic constants C11, C12, C44 in the B3 and B1 phases for a range of pressures from 0 to well above the transition. Report enough points to clearly show a monotonic increase in each constant and a conspicuous discontinuity at the phase boundary.
- Output file: `/app/outputs/soec_vs_pressure.csv`
- Format: csv
- Contract: Columns: pressure_GPa (float), C11_GPa (float), C12_GPa (float), C44_GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_data.csv`
- `/app/outputs/elastic_constants_B3.csv`
- `/app/outputs/soec_vs_pressure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_data.csv
- path: `/app/outputs/transition_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transition pressure (GPa) and relative volume collapse (%) at the B3→B1 transition for six compositions (x=0.0,0.2,0.55,0.81,0.93,1.0).
- schema:
  - `type`: table
  - `required_columns`: `composition_x`, `transition_pressure_GPa`, `volume_collapse_percent`

### elastic_constants_B3.csv
- path: `/app/outputs/elastic_constants_B3.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ambient-pressure bulk modulus B_T, shear modulus C44, and tetragonal modulus C_s for the zinc-blende (B3) phase for the same six compositions.
- schema:
  - `type`: table
  - `required_columns`: `composition_x`, `B_T_GPa`, `C44_GPa`, `C_s_GPa`

### soec_vs_pressure.csv
- path: `/app/outputs/soec_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pressure-dependent second-order elastic constants for at least one composition (e.g., ZnTe). Must show a monotonic increase in each constant with pressure and a clear discontinuity (jump) at the phase transition.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `C11_GPa`, `C12_GPa`, `C44_GPa`

Notes: The checker compares the agent's reported transition pressures and volume collapses to hidden paper values with tolerances. Ambient elastic constants are compared similarly. The pressure‑dependent SOEC are checked for the required structural features (monotonic increase, discontinuity) without exact value matching.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_x",
          "transition_pressure_GPa",
          "volume_collapse_percent"
        ]
      },
      "description": "Transition pressure (GPa) and relative volume collapse (%) at the B3→B1 transition for six compositions (x=0.0,0.2,0.55,0.81,0.93,1.0)."
    },
    {
      "file": "elastic_constants_B3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_x",
          "B_T_GPa",
          "C44_GPa",
          "C_s_GPa"
        ]
      },
      "description": "Ambient-pressure bulk modulus B_T, shear modulus C44, and tetragonal modulus C_s for the zinc-blende (B3) phase for the same six compositions."
    },
    {
      "file": "soec_vs_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "C11_GPa",
          "C12_GPa",
          "C44_GPa"
        ]
      },
      "description": "Pressure-dependent second-order elastic constants for at least one composition (e.g., ZnTe). Must show a monotonic increase in each constant with pressure and a clear discontinuity (jump) at the phase transition."
    }
  ],
  "notes": "The checker compares the agent's reported transition pressures and volume collapses to hidden paper values with tolerances. Ambient elastic constants are compared similarly. The pressure‑dependent SOEC are checked for the required structural features (monotonic increase, discontinuity) without exact value matching."
}
```

## How you are scored
A hidden verifier will independently assess each of the three scored stages: the transition data, the ambient elastic constants, and the pressure‑dependent SOEC curve. The verifier compares your computed outputs to reference values using appropriate tolerances and checks for required structural features (monotonicity and discontinuity). The reward is a weighted combination of the scores from each stage; reporting the paper’s numbers without correctly executing the computational workflow will not satisfy the scoring criteria.
