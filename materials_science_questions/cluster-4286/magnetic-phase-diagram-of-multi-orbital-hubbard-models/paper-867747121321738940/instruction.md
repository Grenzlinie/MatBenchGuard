# Hall number crossover and Fermi surface pockets from spiral antiferromagnetism

## Problem background
In hole-doped cuprate superconductors, measurements of the Hall number n_H reveal a rapid crossover near optimal doping: at low doping n_H is close to the hole density p, while at higher doping it approaches 1+p. Understanding the mechanism behind this change—whether it originates from a Fermi surface reconstruction driven by an ordered phase—is a central open question. The spiral antiferromagnetic (AF) state, with an incommensurate ordering wavevector, is one candidate that could modify the electronic structure and transport properties. This task reproduces key predictions of the spiral AF mean-field model: the doping-dependent Hall number n_H(p) and the associated Fermi surface pocket areas, to examine the viability of this scenario.

## Approach
The reproduction implements a mean-field theory of spiral antiferromagnetism. The physical system is described by a single-band tight-binding model with hopping parameters t and t′ on a square lattice. Antiferromagnetic order enters via a mean-field Hamiltonian with a gap A(p) that closes linearly with hole doping p above a critical doping p*. For each doping, the optimal incommensurability η(p) of the spiral wavevector is obtained by minimizing the fermionic ground-state energy at fixed gap. The resulting 2×2 Hamiltonian is diagonalized over the Brillouin zone to yield the quasiparticle bands and the orthogonal transformation matrix. Using these bands, the weak-field longitudinal and Hall conductivity integrals are evaluated at zero temperature. The Hall coefficient R_H and the Hall number n_H = (R_H e)^(-1) are then computed as functions of p. Finally, at a representative doping, all closed zero-energy Fermi surface pockets are identified from the band structure and their enclosed momentum-space areas and hole/electron character are determined.

## Reproduction target
Compute the Hall number n_H as a function of hole doping p for p in the range 0.02 to 0.25, using the spiral mean-field model with a linear closing gap ansatz (the gap is zero above a critical doping p*=0.19). The required output is a CSV table of p versus n_H. In addition, at the fixed doping p=0.10, identify all closed Fermi surface pockets, determine their type (hole or electron) and count, and compute the area of each pocket in units of (2π/a)², where a is the lattice constant. This second output should be a CSV table listing the pocket type, number of pockets, and area per pocket.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Determine incommensurability η(p)
- Role: process
- Action: For a grid of doping values p (spanning the range where the AF gap is non-zero), use the tight-binding parameters t=1, t'=-0.35, and a chemical potential μ that yields hole doping p. Assign the antiferromagnetic gap A(p) via the linear closing ansatz A(p)=α(p*−p)Θ(p*−p) with p*=0.19 and α calibrated such that A(0.08)=0.63. For each p, minimize the fermionic ground-state energy with respect to the incommensurability η (defining Q=(π−2πη,π)) to obtain the optimal η(p).
- Evidence: `/app/outputs/eta_vs_doping.csv`

### Step 2: Compute quasiparticle bands
- Role: process
- Action: For each doping p (same grid as in step1), construct the 2x2 spiral mean-field Hamiltonian matrix H_MF(k) on a sufficiently fine momentum mesh covering the Brillouin zone, using the dispersion ξ_k = −2t(cos kx+cos ky)−4t'cos kx cos ky−μ, the AF gap A(p) from the linear ansatz, and the incommensurability η(p) from step1. Diagonalize to obtain the two quasiparticle bands E_{k,1/2} and the orthogonal transformation matrix U_k. Store the bands and transformation for use in later steps.
- Evidence: `/app/outputs/bands.npz`

### Step 3: Hall number n_H(p)
- Role: scored (load-bearing)
- Action: Using the quasiparticle bands from step2, compute the Hall number n_H as a function of doping p. Evaluate the weak-field longitudinal conductivity σ_αα (α=x,y) and Hall conductivity σ_H from the band structure integrals (Eqs. (6) and (7) of the paper) at zero temperature, then compute the Hall coefficient R_H = σ_H/(σ_xx σ_yy) and the Hall number n_H = (R_H e)^{-1} where e is the elementary charge. Output a table of p versus n_H for p in [0.02, 0.25] in steps of approximately 0.01, covering both the ordered (p<p*) and paramagnetic (p>p*) regimes.
- Output file: `/app/outputs/hall_number_vs_doping.csv`
- Format: csv
- Contract: CSV with two columns: p (float) and n_H (float). The p values should cover [0.02, 0.25] in steps of about 0.01. n_H is the computed Hall number at each doping.
- Scoring: scored by hidden verifier

### Step 4: Fermi surface pocket areas at p=0.10
- Role: scored
- Action: Using the quasiparticle bands for doping p=0.10 (from step2), locate all closed zero-energy Fermi surface pockets (E_{k,i}=0). For each pocket, compute its enclosed momentum-space area S in units of (2π/a)^2, determine its type (hole or electron), and count the number of such pockets. Output the results.
- Output file: `/app/outputs/pocket_areas.csv`
- Format: csv
- Contract: CSV with columns: pocket_type (string, either 'hole' or 'electron'), number_of_pockets (int), area_per_pocket (float, area in units of (2π/a)^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hall_number_vs_doping.csv`
- `/app/outputs/pocket_areas.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hall_number_vs_doping.csv
- path: `/app/outputs/hall_number_vs_doping.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Hall number n_H as a function of doping p, computed from the spiral mean-field model with linear gap ansatz. The checker compares the reported n_H(p) curve to the reference values derived from the paper.
- schema:
  - `type`: table
  - `required_columns`: `p`, `n_H`
  - `units`:
    - `p`: hole doping (dimensionless)
    - `n_H`: Hall number (dimensionless, in units of elementary charge e)

### pocket_areas.csv
- path: `/app/outputs/pocket_areas.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fermi surface pocket areas at doping p=0.10. The checker compares the number of hole/electron pockets and their areas to the theoretical expectation (two hole pockets each of area ≈0.05 (2π/a)^2) from the spiral AF model.
- schema:
  - `type`: table
  - `required_columns`: `pocket_type`, `number_of_pockets`, `area_per_pocket`
  - `units`:
    - `area_per_pocket`: momentum-space area in units of (2π/a)^2

Notes: The Hall number curve should be computed with the linear gap ansatz A(p)=α(p*−p)Θ(p*−p) calibrated by A(0.08)=0.63, t=1, t'=−0.35. Only the spiral state is considered; the commensurate Néel state and CDW coexistence are omitted. The reference gold values for n_H(p) are taken from the paper's Fig. 2, and the pocket areas from the theoretical relation S_IAF = (2π/a)^2 * p/2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hall_number_vs_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "n_H"
        ],
        "units": {
          "p": "hole doping (dimensionless)",
          "n_H": "Hall number (dimensionless, in units of elementary charge e)"
        }
      },
      "description": "Hall number n_H as a function of doping p, computed from the spiral mean-field model with linear gap ansatz. The checker compares the reported n_H(p) curve to the reference values derived from the paper."
    },
    {
      "file": "pocket_areas.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pocket_type",
          "number_of_pockets",
          "area_per_pocket"
        ],
        "units": {
          "area_per_pocket": "momentum-space area in units of (2π/a)^2"
        }
      },
      "description": "Fermi surface pocket areas at doping p=0.10. The checker compares the number of hole/electron pockets and their areas to the theoretical expectation (two hole pockets each of area ≈0.05 (2π/a)^2) from the spiral AF model."
    }
  ],
  "notes": "The Hall number curve should be computed with the linear gap ansatz A(p)=α(p*−p)Θ(p*−p) calibrated by A(0.08)=0.63, t=1, t'=−0.35. Only the spiral state is considered; the commensurate Néel state and CDW coexistence are omitted. The reference gold values for n_H(p) are taken from the paper's Fig. 2, and the pocket areas from the theoretical relation S_IAF = (2π/a)^2 * p/2."
}
```

## How you are scored
Your output artifacts are scored automatically by a hidden verifier. The verifier reads `hall_number_vs_doping.csv` and compares your reported n_H values against internal reference results derived from the model, using tolerances that allow for legitimate differences arising from discretization and implementation choices. It also checks `pocket_areas.csv` for the correct number of hole/electron pockets and compares the area values within a tolerance. Each scored stage is assigned a weight, and the final reward is the weighted sum of the stage scores. Simply reporting numbers known from the literature is not sufficient; the verifier expects the quantities to emerge from the ordered computational workflow you executed.
