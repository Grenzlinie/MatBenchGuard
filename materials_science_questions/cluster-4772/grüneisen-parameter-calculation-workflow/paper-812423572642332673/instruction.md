# Phonon and thermodynamic properties of cubic III-nitrides from rigid-ion models

## Problem background
Wide-bandgap cubic III-nitrides (especially GaN and AlN) are important for optoelectronic and high‑power devices that often operate under elevated temperatures and pressures. Their thermal expansion, specific heat, and phonon properties as a function of pressure are critical for device reliability but challenging to characterise experimentally. This task computes these pressure‑dependent properties from a physics‑based rigid‑ion model (RIM), using public experimental constants as inputs, thereby enabling accurate prediction of lattice dynamics without requiring ab initio calculations.

## Approach
We adopt a quasi‑harmonic approach anchored on a rigid‑ion model (RIM). Starting from ambient‑pressure lattice constants, elastic constants, and critical‑point phonon frequencies (provided in the input CSV), the high‑pressure lattice constant is obtained via Murnaghan's equation of state (bulk modulus B0 and its pressure derivative B0′). Two independent RIM force‑constant sets are then fitted: one at ambient pressure, the other at the high pressure (22.9 GPa for AlN, 52.2 GPa for GaN), using constrained non‑linear least‑squares optimisation to reproduce the target data (elastic constants and phonon frequencies). From these parametrisations, the dynamical matrix is solved on a fine wave‑vector mesh to compute the full phonon dispersion, the one‑phonon density of states g(ω), and the mode Grüneisen parameters γ_j(q) = (B0/ω)(∂ω/∂P). Finally, the quasi‑harmonic specific heat C_v(T) and the linear thermal expansion coefficient α(T) are evaluated via integrals over g(ω) and γ_j(q). The two scored artifacts—zone‑centre optical phonon frequencies and mode γ, plus C_v and α at selected temperatures—are derived from these intermediate quantities, enforcing that the full fitting and phonon calculation pipeline is genuinely executed.

## Reproduction target
Produce two comma‑separated files under `/app/outputs`:

- `phonon_results.csv`: For cubic GaN and AlN at both ambient and high pressure, list the Γ‑point LO and TO phonon frequencies (in cm⁻¹) and their mode Grüneisen parameters (dimensionless). Required columns: `compound`, `pressure` ("ambient" or "high"), `q_point` ("Γ"), `mode` ("LO" or "TO"), `frequency_cm1`, `mode_gamma`.

- `thermodynamic_results.csv`: For cubic GaN and AlN, list the quasi‑harmonic specific heat C_v (J/(mol·K)) and linear thermal expansion coefficient α (10⁻⁶ K⁻¹) at temperatures 100, 300, and 500 K. Required columns: `compound`, `temperature_K`, `Cv_J_mol_K`, `alpha_1e6_K`.

## Assets

- Compiled input data for cubic GaN and AlN
- NumPy: numpy
- SciPy: scipy
- Phonopy (optional): phonopy

## Workflow steps

### Step 1: Murnaghan EOS and high‑pressure lattice constant
- Role: process
- Action: Using the ambient lattice constant and Murnaghan parameters (B0, B0') from the input CSV, compute the volume ratio V/V0 vs. pressure curve via Murnaghan's equation of state. Determine the lattice constant corresponding to the high‑pressure points (22.9 GPa for AlN, 52.2 GPa for GaN). Write the resulting lattice constants to a file for later use.
- Evidence: `/app/outputs/murnaghan_output.txt`

### Step 2: Fit ambient‑pressure RIM force constants
- Role: process
- Action: Build the rigid‑ion model (RIM) with a parameterized set of interatomic force constants. Using the ambient lattice constant and the provided ambient‑pressure target data (elastic constants and critical‑point phonon frequencies at Γ, X, L), perform a constrained non‑linear least‑squares optimization to determine the ambient‑pressure force‑constant set. Weight the data appropriately. Store the optimized force constants in a JSON file.
- Evidence: `/app/outputs/ambient_force_constants.json`

### Step 3: Fit high‑pressure RIM force constants
- Role: process
- Action: Repeat the RIM construction and constrained non‑linear least‑squares fitting using the high‑pressure lattice constant (from step_01) and the provided high‑pressure target data (high‑pressure Γ experimental frequencies and estimated X,L frequencies). Store the high‑pressure force‑constant set in a JSON file.
- Evidence: `/app/outputs/high_force_constants.json`

### Step 4: Compute full phonon dispersion and density of states
- Role: process
- Action: Using the fitted force‑constant sets for ambient and high pressure, solve the RIM dynamical matrix on a fine wave‑vector mesh to obtain phonon frequencies ω_j(q) and the one‑phonon density of states g(ω) for both pressures. Also compute the mode Grüneisen parameters γ_j(q) from the pressure derivative of the frequencies using the bulk modulus. Save the results (frequencies, DOS, Grüneisen parameters) to a .npy file for later use.
- Evidence: `/app/outputs/phonon_dispersion.npy`

### Step 5: Report zone‑center phonon frequencies and mode Grüneisen parameters
- Role: scored (load-bearing)
- Action: From the computed phonon data, extract the LO and TO frequencies at the Γ point for both ambient and high pressure. Report the corresponding mode Grüneisen parameter for each mode (derived as γ = (B0/ω) (Δω/ΔP) from the pressure difference between the two sets). Write the results to phonon_results.csv.
- Output file: `/app/outputs/phonon_results.csv`
- Format: csv
- Contract: Columns: compound (str), pressure (str: 'ambient' or 'high'), q_point (str, e.g. 'Γ'), mode (str: 'LO' or 'TO'), frequency_cm1 (float), mode_gamma (float). Rows for GaN and AlN at ambient and high pressure.
- Scoring: scored by hidden verifier

### Step 6: Calculate specific heat and thermal expansion
- Role: scored (load-bearing)
- Action: Using the one‑phonon density of states and the mode Grüneisen parameters computed in step_04, evaluate the quasi‑harmonic specific heat C_v(T) (standard harmonic formula from g(ω)) and the linear thermal expansion coefficient α(T) (via integration over g(ω) and γ_j(q) as described by the quasi‑harmonic theory). Compute values at temperatures T = 100, 300, 500 K. Write the results to thermodynamic_results.csv.
- Output file: `/app/outputs/thermodynamic_results.csv`
- Format: csv
- Contract: Columns: compound (str), temperature_K (float), Cv_J_mol_K (float), alpha_1e6_K (float). Rows for GaN and AlN at T=100, 300, 500 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_results.csv`
- `/app/outputs/thermodynamic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_results.csv
- path: `/app/outputs/phonon_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Zone‑center optical phonon frequencies and mode Grüneisen parameters for cubic GaN and AlN at ambient and high pressure. The hidden checker compares these values to the paper‑reported data with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `pressure`, `q_point`, `mode`, `frequency_cm1`, `mode_gamma`
  - `units`:
    - `frequency_cm1`: cm⁻¹
    - `mode_gamma`: dimensionless

### thermodynamic_results.csv
- path: `/app/outputs/thermodynamic_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Quasi‑harmonic specific heat Cv and linear thermal expansion coefficient α at 100, 300, 500 K for cubic GaN and AlN. Checked against paper‑reported values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `temperature_K`, `Cv_J_mol_K`, `alpha_1e6_K`
  - `units`:
    - `Cv_J_mol_K`: J/(mol K)
    - `alpha_1e6_K`: 10⁻⁶ K⁻¹

Notes: The two scored artifacts are re‑derivable from the raw phonon data (step_04) using the RIM fitted parameters. The hidden checker performs result‑level comparison (exact_match with tolerance) against the paper's reported values, plus structural checks (frequencies should increase or remain consistent under pressure, mode γ positive, Cv increases with T, plausible α temperature trend). The bundled input CSV contains all required target data, including the estimated high‑pressure X,L frequencies, so the agent does not need to reproduce the Ref. [10] estimation, only the fitting and computation steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "pressure",
          "q_point",
          "mode",
          "frequency_cm1",
          "mode_gamma"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹",
          "mode_gamma": "dimensionless"
        }
      },
      "description": "Zone‑center optical phonon frequencies and mode Grüneisen parameters for cubic GaN and AlN at ambient and high pressure. The hidden checker compares these values to the paper‑reported data with tolerances."
    },
    {
      "file": "thermodynamic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "temperature_K",
          "Cv_J_mol_K",
          "alpha_1e6_K"
        ],
        "units": {
          "Cv_J_mol_K": "J/(mol K)",
          "alpha_1e6_K": "10⁻⁶ K⁻¹"
        }
      },
      "description": "Quasi‑harmonic specific heat Cv and linear thermal expansion coefficient α at 100, 300, 500 K for cubic GaN and AlN. Checked against paper‑reported values within tolerances."
    }
  ],
  "notes": "The two scored artifacts are re‑derivable from the raw phonon data (step_04) using the RIM fitted parameters. The hidden checker performs result‑level comparison (exact_match with tolerance) against the paper's reported values, plus structural checks (frequencies should increase or remain consistent under pressure, mode γ positive, Cv increases with T, plausible α temperature trend). The bundled input CSV contains all required target data, including the estimated high‑pressure X,L frequencies, so the agent does not need to reproduce the Ref. [10] estimation, only the fitting and computation steps."
}
```

## How you are scored
A hidden verifier reads `phonon_results.csv` and `thermodynamic_results.csv`. It compares the reported phonon frequencies, mode Grüneisen parameters, specific heats, and thermal expansion coefficients against reference values. Each output is scored independently (structural checks may also apply) and the scores are combined into a final reward between 0.0 and 1.0. Providing the exact paper‑reported numbers is not required; the verifier applies appropriate tolerances that reward a faithful implementation of the RIM pipeline. No gold values or tolerances are revealed in the instructions.
