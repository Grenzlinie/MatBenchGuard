# Computational phase diagram of a binary alloy with TB-CPA-GPM-CVM

## Problem background
Predicting the solid-state phase diagram of a binary alloy from first principles is a central challenge in computational thermodynamics. A fully theoretical approach must combine electronic structure calculations that capture the alloy's energetic landscape with statistical mechanics methods that compute configurational free energies and phase equilibria. In this work the target system is a transition-metal binary where the pure elements prefer different crystal structures — one body-centred cubic and the other face-centred cubic. The question is whether a canonical tight-binding model, together with the coherent potential approximation (CPA) for disorder, the generalized perturbation method (GPM) for effective interactions, and the cluster-variation method (CVM) for free energy, can together predict a solid-state phase diagram containing both disordered solid solutions and ordered intermetallic compounds.

## Approach
The computational scheme is built on a tight-binding (TB) model that includes only d-orbitals, with all hopping parameters expressed through canonical Slater‑Koster rules (ddπ = ½|ddσ|, ddδ = 0, ddσ = −1.385 in canonical units). The two pure elements are distinguished solely by their numbers of d‑electrons (N_A, N_B) and a diagonal disorder parameter δ_d. The procedure has three stages. First, the recursion method provides Green’s functions for fcc and bcc lattices, and the single‑site CPA yields the energy of the completely disordered state, U_0^Φ(c), as a function of composition for both lattices. Second, the GPM is applied to the CPA effective‑medium Green’s functions to extract concentration‑dependent effective pair interactions: nearest‑neighbour (nn) interactions for fcc, and nn and next‑nearest‑neighbour (nnn) interactions for bcc. Third, these U_0(c) curves and pair interactions are fed into the CVM in the tetrahedron approximation. The configurational free energy is minimized for the disordered fcc (α) and bcc (β) phases and for a set of ordered superstructures (L1₂, L1₀ on fcc; B2, B32, D0₃ on bcc), and the stable phase at each temperature and composition is determined. The temperature scale is fixed by adopting a canonical d‑band width of 5 eV (1 canonical unit ≈ 4.5 eV). The calculation is carried out for N_A = 3, N_B = 8, and δ_d = 0.8; the liquid phase is not included.

## Reproduction target
Compute the solid‑state phase diagram of a binary alloy with N_A = 3, N_B = 8, and diagonal disorder δ_d = 0.8, using the TB‑CPA‑GPM‑CVM workflow. Produce three quantitative outputs: (i) the disordered‑state energy curves U_0(c) for both fcc (α) and bcc (β) lattices over the whole composition range (c = 0 to 1); (ii) the concentration‑dependent effective pair interactions V1_α(c), V1_β(c), V2_β(c) on the same grid; and (iii) the temperature–composition phase boundaries for all solid‑state phases — disordered fcc and bcc, ordered L1₂ (α′), B2 (β′), L1₀ (α″), B32, and D0₃ — including miscibility gaps and second‑order transitions. The phase diagram must be reported on the temperature scale derived from a canonical d‑band width of 5 eV. The liquid phase is excluded.

## Assets

- Python scientific computing stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Compute U0(c) via CPA
- Role: scored
- Action: Implement the canonical tight-binding d-orbital Hamiltonian with Slater-Koster parameters ddσ=-1.385 (c.u.), ddπ=½|ddσ|, ddδ=0, on fcc and bcc lattices. For a range of concentrations c of element B (0 to 1, step ≤0.1), use the recursion method to obtain Green's functions and the single-site CPA to evaluate the energy of the completely disordered state U0_Φ(c) for both fcc (α) and bcc (β) lattices. Set N_A=3, N_B=8, diagonal disorder δ_d=0.8. Write the resulting U0_α(c) and U0_β(c) to U0_curves.csv.
- Output file: `/app/outputs/U0_curves.csv`
- Format: csv
- Contract: Columns: concentration (float), U0_fcc (float, canonical units), U0_bcc (float, canonical units). Composition range 0 to 1 with step ≤0.1.
- Scoring: scored by hidden verifier

### Step 2: Extract V(c) via GPM
- Role: scored
- Action: Using the CPA output (effective medium Green's functions), apply the generalized perturbation method at lowest order to obtain concentration-dependent effective pair interactions: V1_alpha(c) for fcc nearest-neighbor, V1_beta(c) (nn) and V2_beta(c) (nnn) for bcc. Sample composition points consistent with the U0 grid and write the results to V_curves.csv.
- Output file: `/app/outputs/V_curves.csv`
- Format: csv
- Contract: Columns: concentration (float), V1_alpha (float, c.u.), V1_beta (float, c.u.), V2_beta (float, c.u.). Same composition points as U0_curves.csv.
- Scoring: scored by hidden verifier

### Step 3: Construct solid-state phase diagram
- Role: scored (load-bearing)
- Action: Using the U0(c) curves and V(c) curves, minimize the CVM configurational free energy in the tetrahedron approximation for all candidate solid-state phases: disordered fcc (α), disordered bcc (β), ordered fcc L1₂ (α'), ordered bcc B2 (β'), L1₀ (α''), B32, D0₃. Determine the stable phase at each temperature and composition. Output the phase boundaries (temperature vs. composition) for all multiphase regions, miscibility gaps, and second-order transitions. Temperature scaling: 1 c.u. ≈ 4.5 eV, canonical d-band width 5 eV.
- Output file: `/app/outputs/phase_boundaries.json`
- Format: json
- Contract: JSON object with key 'boundaries' whose value is a list of boundary objects. Each boundary object has 'phase1' (string), 'phase2' (string), 'points' (list of {T: float (K), c: float}). Include boundaries for α/β miscibility gap, α/α' (L1₂), β/β' (B2) phase regions, and any second-order transitions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/U0_curves.csv`
- `/app/outputs/V_curves.csv`
- `/app/outputs/phase_boundaries.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### U0_curves.csv
- path: `/app/outputs/U0_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Disordered-state reference energies U0 for fcc and bcc lattices as functions of composition.
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `U0_fcc`, `U0_bcc`
  - `units`:
    - `concentration`: dimensionless fraction
    - `U0_fcc`: canonical units (c.u.)
    - `U0_bcc`: canonical units (c.u.)

### V_curves.csv
- path: `/app/outputs/V_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective pair interactions from GPM for fcc (V1_alpha) and bcc (V1_beta, V2_beta).
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `V1_alpha`, `V1_beta`, `V2_beta`
  - `units`:
    - `concentration`: dimensionless fraction
    - `V1_alpha`: canonical units (c.u.)
    - `V1_beta`: canonical units (c.u.)
    - `V2_beta`: canonical units (c.u.)

### phase_boundaries.json
- path: `/app/outputs/phase_boundaries.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Phase diagram boundaries for solid-state phases, excluding liquid.
- schema:
  - `type`: object
  - `required`: `boundaries`
  - `items`:
    - `type`: object
    - `phase1`: string
    - `phase2`: string
    - `points`: list of {T: number (K), c: number (dimensionless fraction)}
  - `units`:
    - `T`: Kelvin
    - `c`: dimensionless fraction

Notes: The hidden reference values are extracted from the paper's reported U0(c), V(c), and phase boundaries. Tolerances are set according to expected toolchain variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "U0_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "U0_fcc",
          "U0_bcc"
        ],
        "units": {
          "concentration": "dimensionless fraction",
          "U0_fcc": "canonical units (c.u.)",
          "U0_bcc": "canonical units (c.u.)"
        }
      },
      "description": "Disordered-state reference energies U0 for fcc and bcc lattices as functions of composition."
    },
    {
      "file": "V_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "V1_alpha",
          "V1_beta",
          "V2_beta"
        ],
        "units": {
          "concentration": "dimensionless fraction",
          "V1_alpha": "canonical units (c.u.)",
          "V1_beta": "canonical units (c.u.)",
          "V2_beta": "canonical units (c.u.)"
        }
      },
      "description": "Effective pair interactions from GPM for fcc (V1_alpha) and bcc (V1_beta, V2_beta)."
    },
    {
      "file": "phase_boundaries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "boundaries"
        ],
        "items": {
          "type": "object",
          "phase1": "string",
          "phase2": "string",
          "points": "list of {T: number (K), c: number (dimensionless fraction)}"
        },
        "units": {
          "T": "Kelvin",
          "c": "dimensionless fraction"
        }
      },
      "description": "Phase diagram boundaries for solid-state phases, excluding liquid."
    }
  ],
  "notes": "The hidden reference values are extracted from the paper's reported U0(c), V(c), and phase boundaries. Tolerances are set according to expected toolchain variation."
}
```

## How you are scored
A hidden verifier independently inspects each of the three output files: `U0_curves.csv`, `V_curves.csv`, and `phase_boundaries.json`. The verifier checks that the submitted curves are smooth and exhibit the expected physical trends, that the effective‑pair‑interaction ratios respect known stability rules, and that the phase boundaries are consistent with the topology of the computed free‑energy landscape. The check is made against published reference data for the same parameters (N_A=3, N_B=8, δ_d=0.8). Every output carries a weight, and your final reward is the weighted sum of the individual stage scores. Self‑reported aggregate numbers are not sufficient; the verifier examines the full curves and boundary lists you submit.
