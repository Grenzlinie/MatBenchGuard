# Reproduce relativistic effective electron numbers for hcp lutetium

## Problem background
Lutetium is the lightest of the 5d transition metals. Because relativistic effects are expected to modify its electronic structure, a detailed analysis of the valence electron distribution under different relativistic treatments provides insight into the role of mass‑velocity, Darwin, and spin‑orbit corrections. The goal is to compute the effective valence electron numbers per atom for hcp lutetium from all‑electron density‑functional theory, comparing three levels of relativistic treatment: non‑relativistic, scalar‑relativistic, and fully relativistic including spin‑orbit coupling.

## Approach
Three independent all‑electron DFT calculations are performed for the same hcp lutetium crystal potential. The first is a non‑relativistic augmented‑plane‑wave (or equivalent all‑electron) calculation that serves as a baseline. The second adds scalar‑relativistic corrections (mass‑velocity and Darwin terms) but omits spin‑orbit coupling. The third is a fully relativistic calculation that includes spin‑orbit coupling. For each case the total and partial densities of states are computed on a dense k‑point mesh, after which the occupied valence bands are integrated to obtain effective electron numbers per atom for the angular momentum channels (s, p, d, f, g) and for the interstitial region. By keeping the crystal potential and lattice parameters identical across the three runs, any differences in the electron numbers are attributable solely to the relativistic treatment.

## Reproduction target
Perform the three all‑electron DFT calculations for hcp lutetium using an open‑source all‑electron code such as Elk or FLEUR. From each calculation, integrate the filled valence bands to extract the effective electron numbers per atom: n_s, n_p, n_d, n_f, n_g, and the interstitial charge n_out. Write the non‑relativistic and scalar‑relativistic results to `table1.csv` and the spin‑orbit‑resolved results from the fully relativistic calculation to `table2.csv`. The output schemas are specified in the workflow steps and output contract.

## Assets

- Elk all-electron DFT code (or FLEUR): http://elk.sourceforge.io
- hcp lutetium crystal structure parameters
- Lutetium atomic electronic configuration (5d¹ 6s²)

## Workflow steps

### Step 1: Crystal potential construction
- Role: process
- Action: Construct the crystal potential for hcp lutetium using the Mattheiss scheme with Dirac-Hartree-Fock-Slater atomic densities for the Lu 5d^1 6s^2 configuration and the Slater exchange (α=1).
- Evidence: `/app/outputs/potential_construction.log`

### Step 2: Non-relativistic APW calculation
- Role: process
- Action: Perform a non-relativistic all-electron DFT calculation for hcp Lu using the augmented-plane-wave (APW) method (or an equivalent all-electron method) to obtain the total and partial densities of states (s, p, d, f) with a dense k-point mesh.
- Evidence: `/app/outputs/apw_nonrel.log`

### Step 3: Scalar-relativistic RAPW calculation (no spin-orbit)
- Role: process
- Action: Perform a scalar-relativistic (mass-velocity and Darwin terms) all-electron DFT calculation for hcp Lu to obtain the total and partial densities of states (s, p, d, f) using the same crystal potential and k-point density.
- Evidence: `/app/outputs/rapw_scalar.log`

### Step 4: Full relativistic RAPW calculation with spin-orbit coupling
- Role: process
- Action: Perform a fully relativistic all-electron DFT calculation for hcp Lu including spin-orbit coupling to obtain spin-orbit-resolved partial densities of states (s1/2, p3/2, p1/2, d5/2, d3/2, f7/2, f5/2, g9/2, g7/2) with the same crystal potential and k-point density.
- Evidence: `/app/outputs/rapw_full_rel.log`

### Step 5: Extract effective electron numbers (non-relativistic and scalar-relativistic)
- Role: scored (load-bearing)
- Action: Integrate the filled valence bands from the non-relativistic and scalar-relativistic calculations to obtain effective valence electron numbers per atom for each angular momentum channel (s, p, d, f, g) and the interstitial region (n_out). Output the results as table1.csv.
- Output file: `/app/outputs/table1.csv`
- Format: csv
- Contract: CSV with columns: calculation (string), n_s (float), n_p (float), n_d (float), n_f (float), n_g (float), n_out (float). Two rows: APW and RAPW.
- Scoring: scored by hidden verifier

### Step 6: Extract spin-orbit-resolved effective electron numbers
- Role: scored (load-bearing)
- Action: Integrate the filled valence bands from the full relativistic calculation to obtain effective valence electron numbers for each spin-orbit-resolved channel (s1/2, p3/2, p1/2, d5/2, d3/2, f7/2, f5/2, g9/2, g7/2) and the interstitial region (n_out). Output the results as table2.csv.
- Output file: `/app/outputs/table2.csv`
- Format: csv
- Contract: CSV with columns: state (string), n_state (float). Ten rows: s1/2, p3/2, p1/2, d5/2, d3/2, f7/2, f5/2, g9/2, g7/2, n_out.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1.csv`
- `/app/outputs/table2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1.csv
- path: `/app/outputs/table1.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored Table 1 reproduction: effective electron numbers from non-relativistic and scalar-relativistic DFT calculations, compared against the paper's reported values with tolerances and verified trends.
- schema:
  - `type`: table
  - `required_columns`: `calculation`, `n_s`, `n_p`, `n_d`, `n_f`, `n_g`, `n_out`
  - `units`:
    - `n_s`: electrons/atom
    - `n_p`: electrons/atom
    - `n_d`: electrons/atom
    - `n_f`: electrons/atom
    - `n_g`: electrons/atom
    - `n_out`: electrons/atom
  - `description`: Effective valence electron numbers per atom for the two relativistic approximations (without spin-orbit). Two rows: APW (non-relativistic) and RAPW (scalar-relativistic).

### table2.csv
- path: `/app/outputs/table2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored Table 2 reproduction: spin-orbit-resolved electron numbers from the full relativistic DFT calculation, compared against the paper's reported values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `state`, `n_state`
  - `units`:
    - `n_state`: electrons/atom
  - `description`: Spin-orbit-resolved effective valence electron numbers from the fully relativistic calculation. Rows: s1/2, p3/2, p1/2, d5/2, d3/2, f7/2, f5/2, g9/2, g7/2, n_out.

Notes: The agent must use an all-electron DFT code (e.g., Elk, FLEUR) to perform three separate calculations. The exact method (APW, LAPW, FLAPW) can differ, but the resulting electron numbers should be within the stated tolerances. The checker will verify numerical agreement against the paper’s reported values and will perform internal consistency and trend checks (e.g., verifying that spin-orbit resolved components sum to the corresponding scalar-relativistic totals) without revealing which physical quantities are expected to increase or decrease.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "calculation",
          "n_s",
          "n_p",
          "n_d",
          "n_f",
          "n_g",
          "n_out"
        ],
        "units": {
          "n_s": "electrons/atom",
          "n_p": "electrons/atom",
          "n_d": "electrons/atom",
          "n_f": "electrons/atom",
          "n_g": "electrons/atom",
          "n_out": "electrons/atom"
        },
        "description": "Effective valence electron numbers per atom for the two relativistic approximations (without spin-orbit). Two rows: APW (non-relativistic) and RAPW (scalar-relativistic)."
      },
      "description": "Scored Table 1 reproduction: effective electron numbers from non-relativistic and scalar-relativistic DFT calculations, compared against the paper's reported values with tolerances and verified trends."
    },
    {
      "file": "table2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "state",
          "n_state"
        ],
        "units": {
          "n_state": "electrons/atom"
        },
        "description": "Spin-orbit-resolved effective valence electron numbers from the fully relativistic calculation. Rows: s1/2, p3/2, p1/2, d5/2, d3/2, f7/2, f5/2, g9/2, g7/2, n_out."
      },
      "description": "Scored Table 2 reproduction: spin-orbit-resolved electron numbers from the full relativistic DFT calculation, compared against the paper's reported values with tolerances."
    }
  ],
  "notes": "The agent must use an all-electron DFT code (e.g., Elk, FLEUR) to perform three separate calculations. The exact method (APW, LAPW, FLAPW) can differ, but the resulting electron numbers should be within the stated tolerances. The checker will verify numerical agreement against the paper’s reported values and will perform internal consistency and trend checks (e.g., verifying that spin-orbit resolved components sum to the corresponding scalar-relativistic totals) without revealing which physical quantities are expected to increase or decrease."
}
```

## How you are scored
Each scored artifact (`table1.csv` and `table2.csv`) is evaluated by a hidden verifier that compares the numerical values you produce against a reference, using appropriate tolerances. The verifier may also check required internal consistency (for example, that the sum of spin‑orbit‑resolved channels in table2 replicates the corresponding total in table1). The individual artifact scores are weighted and combined into the final reward. Providing only the expected numbers without executing the required calculations is not sufficient to obtain full credit.
