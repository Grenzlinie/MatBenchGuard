# Self-consistent two-phase model for metal-insulator transition in CMR manganites

## Problem background
Doped colossal magnetoresistive (CMR) manganites exhibit a sharp metal-insulator transition near the Curie temperature, accompanied by dramatic changes in magnetization and conductivity. The transition is believed to arise from competition between itinerant carriers in a double‑exchange (Zener) metallic state and small polarons in a localized insulating state. A two‑phase percolation model with equal hole density describes the coexistence of these phases: below the transition, a metallic ferromagnetic Zener phase dominates with polaronic enclaves, and the ferromagnetic volume fraction collapses abruptly at the transition. Reproducing the self‑consistent thermodynamic behavior of this model — the magnetization versus temperature, the critical temperature as a function of doping, and the temperature evolution of the Zener phase fraction — provides a quantitative test of the proposed mechanism for the CMR effect.

## Approach
Implement the two‑phase model with equal hole density. First, construct the bare tight‑binding band dispersion for the cubic lattice using the two‑band formula that includes anisotropic hopping between manganese sites. The hopping amplitude is set to t = 0.3 eV. Then, introduce renormalization of the Zener band: the effective hopping is reduced by a Kubo–Ohata factor that depends on the ordering field λ and accounts for magnetic disorder, and by a percolative feedback factor p^(f) which is the instantaneous fraction of the sample in the ferromagnetic Zener phase. The localized polaronic phase is represented by a single energy level whose position depends on doping and on the two model parameters E1 = –0.125 eV and E2 = –0.25 eV. The thermodynamics of this mixed phase are governed by the total free energy, which includes grand‑canonical potentials for both carrier species and a mean‑field ion‑spin entropy. The free energy depends on the ordering field λ, the chemical potential μ, and the ferromagnetic fraction p^(f). A self‑consistency constraint enforces equal hole density in both phases. At each temperature and doping, minimize the free energy with respect to λ and p^(f) while satisfying the density constraint to obtain the equilibrium values. From the solution compute the normalized magnetization M/M0 and the Zener phase fraction p^(f). Perform this minimization over a suitable temperature range for each doping level x ∈ {0.175, 0.2, 0.25, 0.3, 0.35, 0.4}. Finally, for each doping, identify the transition temperature Tc as the temperature of steepest descent of the magnetization curve.

## Reproduction target
Produce three primary artifacts by running the self‑consistent two‑phase model:

1. **Magnetization curves:** For doping levels x = 0.175, 0.2, 0.25, 0.3, 0.35, 0.4, compute the normalized magnetization M(T)/M0 and save a CSV (see output schema).
2. **Phase diagram Tc(x):** Extract the critical temperature Tc for each doping from the steepest descent of M(T) and write a CSV with one row per doping.
3. **Zener phase fraction for x = 0.3:** For the specific doping x = 0.3, compute the ferromagnetic volume fraction p^(f) as a function of temperature and write a CSV.

All computations must use the model parameters E1 = –0.125 eV, E2 = –0.25 eV, and t = 0.3 eV. The outputs must strictly follow the column schemas and units defined in the workflow steps and output contract.

## Assets

- Python numerical stack (numpy, scipy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Compute bare tight-binding band dispersion
- Role: process
- Action: Generate a uniform 3D k-point grid for the cubic Brillouin zone (first octant) and compute the two-band dispersion epsilon_k_zeta^(0) using the tight-binding formula with t=0.3 eV. Save the grid and energies.
- Evidence: `/app/outputs/band_dispersion.npy`

### Step 2: Run self-consistent two-phase thermodynamics
- Role: process
- Action: Using the bare band dispersion and model parameters E1=-0.125 eV, E2=-0.25 eV, implement the self-consistent minimization under the equal-density constraint for doping levels x in [0.175,0.2,0.25,0.3,0.35,0.4] and a temperature sweep. For each (x,T), solve for the ordering field λ, ferromagnetic fraction p^(f), and chemical potential μ; compute magnetization M and Zener fraction p^(f). Save all raw arrays (x, T, M, p^(f), Tc estimates) into raw_results.npz.
- Evidence: `/app/outputs/raw_results.npz`

### Step 3: Write magnetization curves CSV
- Role: scored (load-bearing)
- Action: Read raw_results.npz and write magnetization_curves.csv with columns x, T, M (normalized magnetization M/M0).
- Output file: `/app/outputs/magnetization_curves.csv`
- Format: csv
- Contract: Columns: x (float, doping), T (float, temperature in eV/k_B), M (float, normalized magnetization M/M0). Rows for each (x, T) combination.
- Scoring: scored by hidden verifier

### Step 4: Write phase diagram CSV
- Role: scored
- Action: From raw_results.npz, extract the critical temperature Tc for each doping as the temperature of steepest descent of M(T). Write phase_diagram.csv with columns x, Tc.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: x (float), Tc (float, critical temperature in eV/k_B). One row per doping level.
- Scoring: scored by hidden verifier

### Step 5: Write Zener fraction CSV for x=0.3
- Role: scored
- Action: From raw_results.npz, for doping x=0.3 write zener_fraction.csv with columns T, p_f.
- Output file: `/app/outputs/zener_fraction.csv`
- Format: csv
- Contract: Columns: T (float, temperature in eV/k_B), p_f (float). Rows covering the transition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_curves.csv`
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/zener_fraction.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_curves.csv
- path: `/app/outputs/magnetization_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized magnetization M/M0 vs temperature for each doping level.
- schema:
  - `type`: table
  - `required_columns`: `x`, `T`, `M`
  - `units`:
    - `T`: eV/k_B
    - `M`: normalized dimensionless

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical temperature Tc vs doping x.
- schema:
  - `type`: table
  - `required_columns`: `x`, `Tc`
  - `units`:
    - `Tc`: eV/k_B

### zener_fraction.csv
- path: `/app/outputs/zener_fraction.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zener phase fraction p_f vs temperature at x=0.3.
- schema:
  - `type`: table
  - `required_columns`: `T`, `p_f`
  - `units`:
    - `T`: eV/k_B
    - `p_f`: dimensionless fraction

Notes: The hidden checker compares the agent's reported magnetization curves, Tc values, and Zener fraction to paper-reported reference values with appropriate tolerances. The magnetization curve step is load-bearing; it requires genuine execution of the self-consistent solver.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "T",
          "M"
        ],
        "units": {
          "T": "eV/k_B",
          "M": "normalized dimensionless"
        }
      },
      "description": "Normalized magnetization M/M0 vs temperature for each doping level."
    },
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "Tc"
        ],
        "units": {
          "Tc": "eV/k_B"
        }
      },
      "description": "Critical temperature Tc vs doping x."
    },
    {
      "file": "zener_fraction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "p_f"
        ],
        "units": {
          "T": "eV/k_B",
          "p_f": "dimensionless fraction"
        }
      },
      "description": "Zener phase fraction p_f vs temperature at x=0.3."
    }
  ],
  "notes": "The hidden checker compares the agent's reported magnetization curves, Tc values, and Zener fraction to paper-reported reference values with appropriate tolerances. The magnetization curve step is load-bearing; it requires genuine execution of the self-consistent solver."
}
```

## How you are scored
A hidden verifier independently evaluates each of your output files. It reads your submitted magnetization curves, phase diagram, and Zener fraction, and compares the reported quantities against reference values obtained from the same model with a calibrated implementation. The reward is a weighted combination of scores from the three artifacts. For the magnetization curves, the verifier measures the deviation of your M(T) points from the reference at sampled temperatures; larger deviations reduce the score. For Tc, the verifier checks how closely your extracted critical temperatures agree with the reference Tc values for each doping. For the Zener fraction, the verifier verifies that p^(f)(T) shows a sharp drop near the transition and is consistent with the expected shape. In all cases, reward starts at full credit and decreases monotonically as your results move further from the reference — there is no penalty for being slightly off within an acceptable margin, but substantial errors lower the score. The verifier does not rely on any self‑reported summary; it checks the raw CSV contents you write. Therefore, genuine execution of the model and correct data output are required.
