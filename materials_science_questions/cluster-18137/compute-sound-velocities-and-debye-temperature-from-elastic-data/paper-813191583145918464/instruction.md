# Corrected Acoustic-Phonon and Phason Velocities and Specific Heat for Al-Mn-Pd Quasicrystal

## Problem background
At low temperatures the specific heat of the icosahedral quasicrystal Al₆₈.₂Mn₉Pd₂₂.₈ deviates strongly from the standard Debye model. A theoretical framework was proposed that augments the continuum elasticity description with phason degrees of freedom to explain the excess heat capacity. However, a later analysis identified a critical coordinate‑system inconsistency in the original numerical evaluation: the 6D‑to‑3D projection matrix and the elastic constants were taken from different coordinate systems without the required transformation. This task corrects that error and recalculates the acoustic‑phonon and phason mode velocities, the density‑of‑vibrational‑states (DOVS) coefficients, and the low‑temperature specific‑heat parameters for the same quasicrystal. The corrected numbers allow a direct comparison of the theory's predictions with experimental data.

## Approach
The correction proceeds in two stages. First, the correct 6D‑to‑3D projection matrix for the coordinate system of Ding et al. is used to obtain the three‑dimensional direction cosines (l,m,n) of the fivefold, twofold and threefold symmetry axes from the corresponding 6D hyperspace lattice vectors. Second, the literature values of the phason elastic constants K₁, K₂ and R are transformed from the Widom notation to Ding's notation using the relations K₁ᴰ = K₁ᴷ − K₂ᴷ/3, K₂ᴰ = −K₂ᴷ, Rᴰ = Rᴷ. With the direction cosines, the transformed elastic constants, and an appropriate mass density for Al₆₈.₂Mn₉Pd₂₂.₈, the generalized wave equations of the Li–Liu phonon–phason theory are used to construct a 6×6 dynamical matrix for each propagation direction. Solving the eigenvalue problem yields the six mode velocities. The DOVS coefficients a and b and the low‑temperature specific‑heat coefficients β, δ, ω₀, and Θᴅ are then computed by polycrystalline orientation averaging, and the results are compared with experimental data from the literature.

## Reproduction target
Produce two comma‑separated value (CSV) files under `/app/outputs`. The first file (`table_i_velocities.csv`) must contain the six mode velocities v₁–v₆ (in m/s) for each of the three high‑symmetry propagation directions (fivefold A5, twofold A2, threefold A3). The second file (`table_ii_coefficients.csv`) must contain the DOVS coefficients a (s³/rad³ mol) and b (s⁵/rad⁵ mol), and the specific‑heat coefficients β (J/mol K⁴), δ (J/mol K⁶), ω₀ (rad/s), and Θᴅ (K) for each of the three calculated directions, together with a row of experimental reference values taken from the public Wälti et al. data. All quantities must be derived from the corrected projection matrix and transformed elastic constants described in the workflow, and from a publicly available mass density for this quasicrystal.

## Assets

- Li & Liu wave propagation theory paper: 10.1103/PhysRevB.63.064203
- Mass density of Al68.2Mn9Pd22.8 icosahedral quasicrystal
- Experimental specific heat data (Walti et al.): 10.1103/PhysRevB.57.10504
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute corrected projection matrix and direction cosines
- Role: process
- Action: Using icosahedral geometry parameters (θ=2π/5, S=2/√5, C=1/√5) and the 6D hyperspace lattice vectors for the fivefold (1,0,0,0,0,0), twofold (1,-1,0,0,0,0), and threefold (1,1,-1,1,1,-1) axes, construct the corrected projection matrix (6×3) and derive the 3D direction cosines (l,m,n) for each propagation direction.
- Evidence: `/app/outputs/direction_cosines.json`

### Step 2: Transform elastic constants to Ding's notation
- Role: process
- Action: Apply the coordinate transformation formulas K1^D = K1^W - K2^W/3, K2^D = -K2^W, R^D = R^W to the literature elastic constants (K1^W=0.81, K2^W=-0.50, R^W=0.0066, λ=0.75, μ=0.65, all in 10^12 dyn/cm^2) to obtain the transformed constants (K1^D, K2^D, R^D).
- Evidence: `/app/outputs/transformed_constants.json`

### Step 3: Calculate mode velocities
- Role: scored (load-bearing)
- Action: Using the direction cosines from step_direction_cosines, the transformed elastic constants from step_elastic_constants, and an appropriate mass density ρ for Al68.2Mn9Pd22.8 (to be obtained from public literature), construct the 6×6 dynamical matrix for each of the three propagation directions following the wave equations of Li and Liu. Solve the eigenvalue problem and extract the six mode velocities v1–v6 (in m/s). Write results to table_i_velocities.csv.
- Output file: `/app/outputs/table_i_velocities.csv`
- Format: csv
- Contract: CSV with 3 rows (A5, A2, A3), columns: axis, direction_6d, v1, v2, v3, v4, v5, v6 (all numeric velocities in m/s).
- Scoring: scored by hidden verifier

### Step 4: Calculate DOVS and specific-heat coefficients
- Role: scored
- Action: From the mode velocities computed in step_velocities, compute the density-of-vibrational-states (DOVS) coefficients a and b, then the specific-heat parameters β (J/mol·K^4), δ (J/mol·K^6), cutoff frequency ω0 (rad/s), and Debye temperature ΘD (K) using the polycrystalline averaging and formulas of Li and Liu. Include a row labeled 'Expt' containing the experimental values from Walti et al. (Ref. 1) obtained from the published literature. Write the full data to table_ii_coefficients.csv.
- Output file: `/app/outputs/table_ii_coefficients.csv`
- Format: csv
- Contract: CSV with 4 rows (Expt, Calc_A5, Calc_A2, Calc_A3), columns: source (string), a (float), b (float), beta (float), delta (float), omega0 (float), Theta_D (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_i_velocities.csv`
- `/app/outputs/table_ii_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_i_velocities.csv
- path: `/app/outputs/table_i_velocities.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mode velocities along fivefold, twofold, and threefold axes.
- schema:
  - `type`: table
  - `required_columns`: `axis`, `direction_6d`, `v1`, `v2`, `v3`, `v4`, `v5`, `v6`
  - `units`:
    - `v1`: m/s
    - `v2`: m/s
    - `v3`: m/s
    - `v4`: m/s
    - `v5`: m/s
    - `v6`: m/s

### table_ii_coefficients.csv
- path: `/app/outputs/table_ii_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: DOVS and specific heat coefficients from experiment and three calculated directions.
- schema:
  - `type`: table
  - `required_columns`: `source`, `a`, `b`, `beta`, `delta`, `omega0`, `Theta_D`
  - `units`:
    - `a`: s^3/rad^3 mol
    - `b`: s^5/rad^5 mol
    - `beta`: J/mol K^4
    - `delta`: J/mol K^6
    - `omega0`: rad/s
    - `Theta_D`: K

Notes: The mass density ρ must be obtained from public literature; it is not provided here. The wave equations are from Li and Liu (Phys. Rev. B 63, 064203); the agent must implement the dynamical matrix.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_i_velocities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "axis",
          "direction_6d",
          "v1",
          "v2",
          "v3",
          "v4",
          "v5",
          "v6"
        ],
        "units": {
          "v1": "m/s",
          "v2": "m/s",
          "v3": "m/s",
          "v4": "m/s",
          "v5": "m/s",
          "v6": "m/s"
        }
      },
      "description": "Mode velocities along fivefold, twofold, and threefold axes."
    },
    {
      "file": "table_ii_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "source",
          "a",
          "b",
          "beta",
          "delta",
          "omega0",
          "Theta_D"
        ],
        "units": {
          "a": "s^3/rad^3 mol",
          "b": "s^5/rad^5 mol",
          "beta": "J/mol K^4",
          "delta": "J/mol K^6",
          "omega0": "rad/s",
          "Theta_D": "K"
        }
      },
      "description": "DOVS and specific heat coefficients from experiment and three calculated directions."
    }
  ],
  "notes": "The mass density ρ must be obtained from public literature; it is not provided here. The wave equations are from Li and Liu (Phys. Rev. B 63, 064203); the agent must implement the dynamical matrix."
}
```

## How you are scored
An automated hidden verifier reads the two CSV files you output. It first validates the required column and row structure, then compares every numerical value against hidden reference numbers (the corrected values reported in the original analysis). Comparison uses per‑column tolerances chosen to accept legitimate differences due to implementation choices (e.g., floating‑point arithmetic, eigenvalue solver) while rejecting trivial guesses or memorized numbers. The final score is a weighted combination of the per‑cell scores for the velocity table and the coefficient table; reporting the paper’s numbers without performing the actual computation will not pass. The verifier runs off‑line and accesses no external resources — do not attempt to fetch anything during scoring.
