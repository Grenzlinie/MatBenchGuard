# Hydrogen vibrational frequency shift and broadening from lattice-gas Monte Carlo

## Problem background
In niobium hydride (NbH_c), hydrogen atoms occupy interstitial tetrahedral sites and form a lattice gas or lattice liquid. The hydrogen optic-mode vibrational frequencies shift and broaden with temperature (T) and concentration (c) because local lattice deformations statically alter the effective spring constants. This task calculates these shifts and broadenings from a model that couples a lattice‑gas Hamiltonian with a linear anharmonicity relation linking local dilations to frequency changes. All required inputs are specified within the workflow; no external datasets are needed.

## Approach
We implement a grand‑canonical Monte Carlo simulation of H on tetrahedral sites of a bcc Nb lattice using an elastic‑interaction model. Pair‑interaction energies are given for nine shells (in K) with hard‑core exclusion up to the third‑neighbor shell. A mean‑field term accounts for surface and long‑range effects via the host isothermal compressibility. For two temperatures (500 K, 600 K) the chemical potential is tuned to achieve several H concentrations near 0.2, 0.3, 0.4. After equilibration, the average energy per hydrogen E/N (excluding self‑energy) and the rms deviation σ_E of the individual particle energies are computed; we set ΔE/N = σ_E / 2. Energies are converted from kelvin to eV (1 eV = 11604.5 K). The fractional frequency shift is (ω−ω₀)/ω₀ = γ × (−2 E/N) / TrQ and the half‑width broadening Δω/ω₀ = (2γ/TrQ) × ΔE/N, with γ = −5 and TrQ = 10 eV. The simulation yields the c‑ and T‑dependence of the shift and broadening.

## Reproduction target
Produce a CSV file with columns T (K), c (dimensionless), E_N (K), ΔE_N (K), shift (dimensionless), and broadening (dimensionless). The file must contain at least six rows: for each of the two temperatures T = 500 K and 600 K, at least three concentration values close to c ≈ 0.2, 0.3, 0.4. The CSV will be checked against reference results derived from the original study.

## Assets
No external datasets, models, or tools are required. All Hamiltonian parameters, interaction energies, and physical constants are provided in the workflow steps. The simulation can be implemented with standard Python libraries (e.g., NumPy) and optionally performance‑oriented packages (Cython, Numba).

## Workflow steps

### Step 1: Monte Carlo simulation and vibrational frequency analysis
- Role: scored (load-bearing)
- Action: Implement a grand-canonical Monte Carlo simulation of hydrogen on tetrahedral interstitial sites in bcc Nb using the Horner-Wagner lattice-gas model. The system is a 6a0×6a0×6a0 supercell (2592 sites) with periodic boundaries. Use the nine-shell pair interaction energies ε̄_jk (in K): -4174, -2907, -1967, -1218, -589, -426, -212, 86, 190, 500 (shells 0–9, exclude self-energy). Exclude hard-core overlaps up to the third-neighbor shell. Include a mean-field surface/long-range term with host-lattice isothermal compressibility K_T = 1.73×10^12 dyn/cm^2 and volume U appropriate for Nb. For T = 500 K and 600 K, adjust the chemical potential to achieve several H concentrations c ≈ 0.2, 0.3, 0.4. For each run, after equilibration, compute the average energy per hydrogen E_N (K, excluding self-energy) and the rms deviation σ_E of the individual particle energies; then set ΔE_N = σ_E / 2. Convert E_N and ΔE_N to eV using 1 eV = 11604.5 K. Compute the fractional frequency shift (ω−ω₀)/ω₀ = γ × (−2E_N in eV) / TrQ with γ=−5, TrQ=10 eV. Compute the fractional half-width broadening as the positive magnitude: Δω/ω₀ = |(2γ/TrQ) × (ΔE_N in eV)|. Write a CSV file with columns T, c, E_N, ΔE_N, shift, broadening. The CSV must contain at least six rows (two temperatures, three concentrations each).
- Output file: `/app/outputs/step_01_results.csv`
- Format: csv
- Contract: Columns: T (float, K), c (float, H/Nb ratio), E_N (float, K), ΔE_N (float, K), shift (float, dimensionless), broadening (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.csv
- path: `/app/outputs/step_01_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the simulation results for each temperature and concentration condition.
- schema:
  - `type`: table
  - `required_columns`: `T`, `c`, `E_N`, `ΔE_N`, `shift`, `broadening`
  - `units`:
    - `T`: K
    - `c`: dimensionless
    - `E_N`: K
    - `ΔE_N`: K
    - `shift`: dimensionless
    - `broadening`: dimensionless

Notes: The CSV must contain at least six rows (two temperatures, three concentrations each).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "c",
          "E_N",
          "ΔE_N",
          "shift",
          "broadening"
        ],
        "units": {
          "T": "K",
          "c": "dimensionless",
          "E_N": "K",
          "ΔE_N": "K",
          "shift": "dimensionless",
          "broadening": "dimensionless"
        }
      },
      "description": "CSV containing the simulation results for each temperature and concentration condition."
    }
  ],
  "notes": "The CSV must contain at least six rows (two temperatures, three concentrations each)."
}
```

## How you are scored
A hidden verifier reads your CSV and compares each row’s E_N, ΔE_N, shift, and broadening to expected values with appropriate tolerances. It also checks that the shift values exhibit an approximately linear concentration dependence consistent with the physical model. The verifier does not simply reward reporting numbers; it evaluates the accuracy of the computed quantities and the overall physical behavior. The final score is a weighted combination of these checks.
