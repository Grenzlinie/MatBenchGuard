# Monolayer hBN in-plane optical phonon polynomial model and nonlinear susceptibilities from DFT

## Problem background
Nonlinear optical response in the mid-infrared region is essential for harmonic generation, optical modulation, and quantum optics. Two-dimensional materials provide a promising platform due to strong light–matter interaction. Hexagonal boron nitride (hBN) supports long-lived optical phonon polaritons, and its in-plane atomic vibrations can become anharmonic under strong driving, potentially yielding high-order harmonic generation and Kerr nonlinearity. This task investigates the nonlinear vibrational response of monolayer hBN by computing the anharmonic potential and dipole from first principles and deriving the resulting optical susceptibilities.

## Approach
The central ingredient is the displacement‑dependent potential energy landscape and unit‑cell dipole for in‑plane relative B–N motion. These are obtained via density‑functional theory (DFT) calculations at the Γ point, spanning a grid of relative displacement vectors up to 0.03 Å. The computed energy and dipole are fitted to symmetry‑adapted polynomial expansions that honour the hexagonal crystal symmetry. From the fitted coefficients and the reduced mass, the linear phonon resonance frequency follows. The classical equation of motion for the relative coordinate under a monochromatic external field is then solved perturbatively, giving closed‑form expressions for the linear susceptibility, second‑harmonic generation (SHG), third‑harmonic generation (THG), and the third‑order Kerr self‑modulation at resonance, assuming a phenomenological lifetime. An additional static (DC) field shifts the equilibrium point and thus the resonance frequency; the linearized change is evaluated for a representative DC field strength.

## Reproduction target
Produce two output files:
1. `fitted_coefficients.csv` – the seven polynomial coefficients that parametrize the in‑plane energy and dipole landscape (e0, e1, e2, p0, Q0, Q1, Q2), reported in atomic units.
2. `susceptibilities.csv` – the on‑resonance (ω = ω₀) perturbative susceptibilities χ⁽¹⁾ (linear, dimensionless), χ⁽²⁾ (SHG, in m/V), χ⁽³⁾ (THG, in m²/V²), and χ⁽³⁾ (Kerr, in m²/V²) for a phonon lifetime of 2 ps, as well as the DC‑field‑induced resonance frequency shift Δω₀ (in meV) for an applied DC field of 10⁹ V/m along the bond direction. All susceptibilities must be converted to SI units using the unit‑cell volume V = A·h with A = 5.43 Å² and h = 3.3 Å.

## Assets

- Monolayer hBN crystal structure
- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- PAW pseudopotentials for B and N (PBE functional): https://www.quantum-espresso.org/pseudopotentials/
- Python with NumPy, SciPy, Matplotlib

## Workflow steps

### Step 1: DFT calculation of in-plane energy and dipole landscape
- Role: process
- Action: Perform DFT calculations for monolayer hBN at the Gamma point for a grid of in-plane relative B-N displacement vectors u = (u_x, u_y) with magnitude up to 0.03 Å. For each displacement, compute the total energy per unit cell and the unit-cell dipole moment. Save the raw data as a CSV file.
- Evidence: `/app/outputs/dft_raw_data.csv`

### Step 2: Polynomial fit of energy and dipole
- Role: scored
- Action: Fit the DFT energy and dipole data to the symmetry-allowed polynomial expansions: E = e0*(ux^2+uy^2) + e1*ux*(ux^2-3*uy^2) + e2*(ux^2+uy^2)^2; p = p0*x_hat + Q0*u + Q1*[(ux^2-uy^2)*x_hat - 2*ux*uy*y_hat] + Q2*(ux^2+uy^2)*u. Use least-squares fitting. Report the fitted coefficients in atomic units.
- Output file: `/app/outputs/fitted_coefficients.csv`
- Format: csv
- Contract: Header: coefficient,value,unit. Rows: e0, e1, e2, p0, Q0, Q1, Q2. Values are floating-point numbers.
- Scoring: scored by hidden verifier

### Step 3: Perturbative nonlinear susceptibilities and DC shift
- Role: scored (load-bearing)
- Action: Using the fitted coefficients and the reduced mass M = 6.102 Da, compute the resonance frequency ω0 = sqrt(2*e0/M). Then compute the perturbative nonlinear susceptibilities at resonance (ω=ω0) for a lifetime τ=2 ps. The analytical expressions from perturbation theory are:

  χ¹¹ ≈ (Q₀²)/(ε₀ V M) · D⁻¹
  χ²² ≈ (Q₀³)/(ε₀ V M²) · (e₁/(M ω₀²) + Q₁/Q₀) · D⁻²
  χ³³ ≈ (i Q₀⁴)/(4 ε₀ V M⁴ ω₀²) · (2 e₂ + 8 e₁ Q₁/Q₀ + 3 e₁²/(M ω₀²) + 4 M Q₂ ω₀²/Q₀) · D⁻³
  χ³¹ ≈ (6 Q₀⁴)/(ε₀ V M⁴) · (5 e₁²/(M ω₀²) − 2 e₂) · 1/(D² |D|²)

  where D = ω₀² − ω(ω + i τ⁻¹) (evaluated at ω=ω₀, giving D = −i ω₀/τ), ε₀ is the vacuum permittivity, and V is the unit‑cell volume V = A·h with A = 5.43 Å² and h = 3.3 Å. Convert all susceptibilities to SI units.

  Compute the DC‑field‑induced resonance frequency shift Δω₀ for E_DC = 10⁹ V/m applied along x using:

  Δω₀ ≈ (3 Q₀ e₁/(M ω₀²) − 2 Q₁) E_DC / (M ω₀)

  Report the results as a CSV.
- Output file: `/app/outputs/susceptibilities.csv`
- Format: csv
- Contract: Header: label,value,unit. Rows: chi_11 (m^0), chi_22 (m/V), chi_33 (m^2/V^2), chi_31 (m^2/V^2), DC_shift (meV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_coefficients.csv`
- `/app/outputs/susceptibilities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_coefficients.csv
- path: `/app/outputs/fitted_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fitted coefficients e0, e1, e2, p̄0, Q0, Q1, Q2 in atomic units from DFT data.
- schema:
  - `type`: table
  - `required_columns`: `coefficient`, `value`, `unit`
  - `units`:
    - `coefficient`: atomic units
  - `description`: Fitted polynomial coefficients for in-plane potential and dipole of monolayer hBN.

### susceptibilities.csv
- path: `/app/outputs/susceptibilities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nonlinear susceptibilities χ^(1), χ^(2), χ^(3) at resonance and DC shift for E_DC=10^9 V/m.
- schema:
  - `type`: table
  - `required_columns`: `label`, `value`, `unit`
  - `units`:
    - `chi_11`: m^0
    - `chi_22`: m/V
    - `chi_33`: m^2/V^2
    - `chi_31`: m^2/V^2
    - `DC_shift`: meV
  - `description`: Perturbative nonlinear susceptibilities and DC-field-induced resonance shift.

Notes: The checker compares each reported value against the paper's reference values using relative tolerances and absolute tolerance for the DC shift. The reward is based on the fraction of values within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coefficient",
          "value",
          "unit"
        ],
        "units": {
          "coefficient": "atomic units"
        },
        "description": "Fitted polynomial coefficients for in-plane potential and dipole of monolayer hBN."
      },
      "description": "Fitted coefficients e0, e1, e2, p̄0, Q0, Q1, Q2 in atomic units from DFT data."
    },
    {
      "file": "susceptibilities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "label",
          "value",
          "unit"
        ],
        "units": {
          "chi_11": "m^0",
          "chi_22": "m/V",
          "chi_33": "m^2/V^2",
          "chi_31": "m^2/V^2",
          "DC_shift": "meV"
        },
        "description": "Perturbative nonlinear susceptibilities and DC-field-induced resonance shift."
      },
      "description": "Nonlinear susceptibilities χ^(1), χ^(2), χ^(3) at resonance and DC shift for E_DC=10^9 V/m."
    }
  ],
  "notes": "The checker compares each reported value against the paper's reference values using relative tolerances and absolute tolerance for the DC shift. The reward is based on the fraction of values within tolerance."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files, validates their schema, and extracts the reported values. It compares each value to a hidden reference and applies a tolerance. The reward is computed as the weighted fraction of values that meet the tolerance, monotonically decreasing as deviations increase. The two output files jointly determine the final score, with the susceptibilities carrying the majority weight. You must faithfully execute the workflow and compute the numbers; simply guessing or copying known values is not guaranteed to succeed because the reference values are hidden.
