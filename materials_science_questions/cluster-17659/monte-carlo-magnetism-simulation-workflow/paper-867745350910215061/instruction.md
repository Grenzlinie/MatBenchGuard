# Metastable Decay in 2D Anisotropic Heisenberg Model

## Problem background
Metastability occurs when a system is trapped near a local free-energy minimum for a long time before escaping to the global minimum. In the 2D anisotropic Heisenberg ferromagnet with exchange couplings \(J_x = J_y = 1\), \(J_z = 2\), at temperature \(T = 1\) (below the critical temperature), a reversed magnetic field \(H_z < 0\) after initial alignment along \(+z\) creates a metastable state. The decay happens via nucleation and growth of droplets of the stable phase. The average lifetime \(\langle \tau \rangle\) as a function of the inverse field magnitude \(1/|H_z|\) shows distinct single-droplet (SD), multi-droplet (MD), and strong-field (SF) regimes. The Kolmogorov-Johnson-Mehl-Avrami (KJMA) theory predicts that the slopes of the linear asymptotic regimes for SD and MD should have a ratio of 3, but actual measurements may deviate due to non-exponential prefactors in the nucleation rate. In this task, you will measure this lifetime curve and compute the actual slope ratio.

## Approach
Use Monte Carlo (MC) simulation with single-spin Glauber dynamics on an \(L \times L\) square lattice (\(L = 16\)) with periodic boundary conditions. Initialize all spins along \(+z\). At time \(t = 0\), apply a constant negative field \(H_z\). For each run, evolve the system until the total \(z\)-magnetization \(M_z\) first reaches zero; record the escape time in Monte Carlo steps per spin (MCSS). Average over at least 1000 independent escapes for each field value. Choose at least five field values spanning the SD and MD regimes (e.g., \(H_z = -1.2, -1.1, -1.0, -0.9, -0.8\)). After obtaining average lifetimes \(\langle \tau \rangle\), plot \(\langle \tau \rangle\) vs \(1/|H_z|\), identify the SD and MD linear regions, perform linear fits, and compute the ratio (MD slope) / (SD slope).

## Reproduction target
Produce a CSV file `lifetime_data.csv` with columns \(H_z\), \(1/|H_z|\) (inv_field), and average lifetime \(\langle \tau \rangle\) in MCSS for at least five field values covering the SD and MD regimes. Then compute the slope ratio from linear fits to the SD and MD regimes and write that single floating-point number to `slope_ratio.txt`.

## Assets
All necessary tools are standard Python libraries. You may use any numerical and scientific libraries (e.g., NumPy, SciPy) and a linear fitting routine. No external datasets or model files are required.

## Workflow steps

### Step 1: Run MC simulations and compute average lifetimes
- Role: scored (load-bearing)
- Action: Implement a Monte Carlo simulation of the 2D anisotropic Heisenberg model with J_x=J_y=1, J_z=2 on an L×L square lattice (L=16) with periodic boundary conditions and single-spin Glauber dynamics. Initialize all spins along +z. For each of at least five negative magnetic fields H_z (chosen to cover SD and MD regimes, e.g., -1.2, -1.1, -1.0, -0.9, -0.8), run at least 1000 independent escape simulations. In each run, at t=0 switch the field to H_z<0 and evolve until M_z first reaches 0; record the escape time τ in MCSS. Compute the average lifetime ⟨τ⟩ for each field value. Save the results as a CSV file with columns H_z, inv_field (= 1/|H_z|), and lifetime (⟨τ⟩).
- Output file: `/app/outputs/lifetime_data.csv`
- Format: csv
- Contract: CSV with columns: H_z (float, applied field), inv_field (float, 1/|H_z|), lifetime (float, average MCSS). At least 5 rows.
- Scoring: scored by hidden verifier

### Step 2: Compute SD/MD slope ratio
- Role: scored
- Action: From the lifetime data in lifetime_data.csv, identify the single-droplet (SD) and multi-droplet (MD) regimes (e.g., by visual inspection or automated detection of linear regions). Perform linear fits to the ⟨τ⟩ vs 1/|H_z| data in each regime. Compute the ratio of the MD slope to the SD slope. Write this ratio to slope_ratio.txt.
- Output file: `/app/outputs/slope_ratio.txt`
- Format: txt
- Contract: A single floating-point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lifetime_data.csv`
- `/app/outputs/slope_ratio.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lifetime_data.csv
- path: `/app/outputs/lifetime_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Metastable lifetime data: applied field, inverse field magnitude, and average escape time in MCSS for at least 5 field values covering SD and MD regimes.
- schema:
  - `type`: table
  - `required_columns`: `H_z`, `inv_field`, `lifetime`
  - `columns_units`:
    - `H_z`: dimensionless (applied field)
    - `inv_field`: dimensionless (1/|H_z|)
    - `lifetime`: MCSS

### slope_ratio.txt
- path: `/app/outputs/slope_ratio.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The ratio of the asymptotic linear slopes in the multi-droplet (MD) and single-droplet (SD) regimes, derived from the lifetime data.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the slope ratio (MD slope / SD slope).

Notes: The lifetime data is checked structurally (columns, row count, monotonicity). The slope ratio is compared to the paper-reported value within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lifetime_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "H_z",
          "inv_field",
          "lifetime"
        ],
        "columns_units": {
          "H_z": "dimensionless (applied field)",
          "inv_field": "dimensionless (1/|H_z|)",
          "lifetime": "MCSS"
        }
      },
      "description": "Metastable lifetime data: applied field, inverse field magnitude, and average escape time in MCSS for at least 5 field values covering SD and MD regimes."
    },
    {
      "file": "slope_ratio.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the slope ratio (MD slope / SD slope)."
      },
      "description": "The ratio of the asymptotic linear slopes in the multi-droplet (MD) and single-droplet (SD) regimes, derived from the lifetime data."
    }
  ],
  "notes": "The lifetime data is checked structurally (columns, row count, monotonicity). The slope ratio is compared to the paper-reported value within tolerance."
}
```

## How you are scored
Your submitted `lifetime_data.csv` and `slope_ratio.txt` will be evaluated by an automated verifier. The verifier checks `lifetime_data.csv` for the required columns, at least five field values, and a monotonically decreasing lifetime trend with increasing \(1/|H_z|\) in the SD/MD range (structural audit). The slope ratio in `slope_ratio.txt` is compared to a hidden reference value with a tolerance. The two steps are combined (with weight) into a final reward score between 0 and 1. Reporting correct-looking numbers without running the simulation is not sufficient; the structural and reference checks ensure a genuine reproduction.
