# DFT electronic structure and optical properties of rutile TiO2

## Problem background
Rutile titanium dioxide (TiO₂) is a wide-band-gap semiconductor widely used as an anti-reflective layer in photovoltaic devices. The material's performance depends critically on its electronic and optical properties: the band gap, the high-frequency dielectric constants, and the optical birefringence determine how effectively it reduces light reflection and couples incident light into the solar cell. This task aims to compute these key quantities from first principles density functional theory (DFT) to assess the optical performance of rutile TiO₂ for photovoltaic anti-reflective coatings.

## Approach
The calculations are performed using the plane-wave pseudopotential method as implemented in the open-source Quantum ESPRESSO package, employing norm-conserving pseudopotentials for titanium and oxygen. Two exchange-correlation functionals are used: the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation (GGA) and the Perdew–Wang local density approximation (LDA). The workflow consists of: (1) geometry optimization of the tetragonal rutile unit cell starting from experimental lattice parameters; (2) self-consistent field (SCF) calculation to obtain the ground-state charge density and Kohn–Sham eigenvalues; (3) band structure calculation along a k-path that includes the Γ-point to identify the direct band gap; (4) computation of the frequency-dependent complex dielectric function ε(ω) via the random-phase approximation (RPA) for ordinary (xx,yy) and extraordinary (zz) polarizations; (5) extraction of the high-frequency dielectric constants from the real part of ε(ω) at high photon energy; and (6) calculation of the refractive indices using the Maxwell relation and the resulting optical birefringence at 633 nm (1.96 eV). The whole procedure is repeated for both GGA and LDA functionals, providing a direct comparison of the two approximations.

## Reproduction target
Your goal is to compute the following properties of rutile TiO₂ and output them in the specified CSV files:

- **Direct band gap at Γ** for both PBE-GGA and PW-LDA functionals (in eV), and the band gap nature (Γ–Γ direct).
- **High-frequency dielectric constants** ε₁₁(∞) = ε₂₂(∞) (ordinary) and ε₃₃(∞) (extraordinary) for both functionals (dimensionless).
- **Optical birefringence at 633 nm**, defined as Δn = n_e − n_o, for both functionals (dimensionless).

All results must be reported in the exact CSV schema described in each scored workflow step. The verifier will compare your reported values against hidden reference values for the same quantities.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Ti and O: https://www.quantum-espresso.org/pseudopotentials/
- Crystallographic data for rutile TiO2

## Workflow steps

### Step 1: Geometry optimization of rutile TiO2
- Role: process
- Action: Use Quantum ESPRESSO pw.x with vc-relax to optimize the tetragonal lattice parameters a, c, and internal coordinate u starting from experimental values (a=4.593 Å, c=2.959 Å, u=0.305) for both PBE-GGA and PW-LDA functionals.
- Evidence: `/app/outputs/relax_output.txt`

### Step 2: Self-consistent field ground-state calculation
- Role: process
- Action: For each optimized structure (PBE-GGA and PW-LDA), run a self-consistent field calculation using pw.x to obtain the ground-state charge density and Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/scf_output.txt`

### Step 3: Band structure and band gap
- Role: scored
- Action: Using the ground-state wavefunction, perform a non-self-consistent band structure calculation along a k-path covering the Γ-point to obtain the eigenvalues. Identify the valence band maximum and conduction band minimum at Γ and compute the direct band gap for each functional. Output the results.
- Output file: `/app/outputs/step_01_band_gap.csv`
- Format: csv
- Contract: Columns: functional (string), band_gap_eV (float), gap_nature (string). Two rows: pbe-GGA and pw-LDA.
- Scoring: scored by hidden verifier

### Step 4: Frequency-dependent dielectric function calculation
- Role: process
- Action: Using the ground-state wavefunction, calculate the complex dielectric function ε(ω) via the random-phase approximation as implemented in Quantum ESPRESSO's epsilon.x or equivalent post-processing tool. Compute ε1(ω) and ε2(ω) for ordinary (xx, yy) and extraordinary (zz) polarizations over a photon energy range up to 15 eV.
- Evidence: `/app/outputs/dielectric_data.txt`

### Step 5: High-frequency dielectric constant extraction
- Role: scored (load-bearing)
- Action: From the real part ε1(ω) at high photon energy (near 15 eV) determine the electronic dielectric constant ε∞ for ordinary (ε11=ε22) and extraordinary (ε33) directions for each functional. Output the values.
- Output file: `/app/outputs/step_02_dielectric_constants.csv`
- Format: csv
- Contract: Columns: functional (string), direction (string: ordinary or extraordinary), epsilon_infinity (float). Four rows: pbe-GGA ordinary, pbe-GGA extraordinary, pw-LDA ordinary, pw-LDA extraordinary.
- Scoring: scored by hidden verifier

### Step 6: Refractive index and birefringence calculation
- Role: scored
- Action: Using the dielectric function, compute the refractive index n(ω) via the Maxwell relation n = (1/√2)√(√(ε1²+ε2²)+ε1) for ordinary and extraordinary directions. Extract the refractive indices at 633 nm (1.96 eV) and compute the birefringence Δn = n_e − n_o. Output the birefringence.
- Output file: `/app/outputs/step_03_birefringence.csv`
- Format: csv
- Contract: Columns: functional (string), birefringence_633nm (float). Two rows: pbe-GGA and pw-LDA.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gap.csv`
- `/app/outputs/step_02_dielectric_constants.csv`
- `/app/outputs/step_03_birefringence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gap.csv
- path: `/app/outputs/step_01_band_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct band gap and its nature for PBE-GGA and PW-LDA functionals.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `band_gap_eV`, `gap_nature`
  - `units`:
    - `band_gap_eV`: eV
    - `gap_nature`: string (expected: Γ-Γ direct)

### step_02_dielectric_constants.csv
- path: `/app/outputs/step_02_dielectric_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: High-frequency (electronic) dielectric constants for ordinary and extraordinary directions.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `direction`, `epsilon_infinity`
  - `units`:
    - `epsilon_infinity`: dimensionless

### step_03_birefringence.csv
- path: `/app/outputs/step_03_birefringence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optical birefringence at 633 nm (1.96 eV) computed for PBE-GGA and PW-LDA.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `birefringence_633nm`
  - `units`:
    - `birefringence_633nm`: dimensionless

Notes: All scored outputs are compared to the paper's reported values with hidden tolerances. The solver must execute all process steps to produce the final scored files.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "band_gap_eV",
          "gap_nature"
        ],
        "units": {
          "band_gap_eV": "eV",
          "gap_nature": "string (expected: Γ-Γ direct)"
        }
      },
      "description": "Direct band gap and its nature for PBE-GGA and PW-LDA functionals."
    },
    {
      "file": "step_02_dielectric_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "direction",
          "epsilon_infinity"
        ],
        "units": {
          "epsilon_infinity": "dimensionless"
        }
      },
      "description": "High-frequency (electronic) dielectric constants for ordinary and extraordinary directions."
    },
    {
      "file": "step_03_birefringence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "birefringence_633nm"
        ],
        "units": {
          "birefringence_633nm": "dimensionless"
        }
      },
      "description": "Optical birefringence at 633 nm (1.96 eV) computed for PBE-GGA and PW-LDA."
    }
  ],
  "notes": "All scored outputs are compared to the paper's reported values with hidden tolerances. The solver must execute all process steps to produce the final scored files."
}
```

## How you are scored
A hidden verifier inspects the CSV artifacts you produce and independently scores each stage. For each scored output (band gap, dielectric constants, birefringence), the verifier compares your reported numbers to a hidden reference with tolerances that account for expected differences due to implementation details (e.g., pseudopotential choice, convergence settings). The reward for each stage reflects how close your result is to the reference; simply reporting the paper's published numbers is not sufficient—you must genuinely perform the DFT workflow. The final reward is a weighted combination of the stage rewards, with the dielectric constants stage (load‑bearing) receiving the highest weight. The tolerances and reference values are never revealed to you.
