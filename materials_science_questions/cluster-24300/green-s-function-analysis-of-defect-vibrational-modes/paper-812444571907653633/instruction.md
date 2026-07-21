# Green's Function Analysis of Defect Vibrational Modes in InP

## Problem background
Substitutional impurities in zincblende semiconductors introduce localized, gap, and band vibrational modes whose frequencies depend on the impurity mass and the perturbation of interatomic forces. This task focuses on InP, a III-V semiconductor with a wide phonon gap. A Green's function technique using a rigid-ion model (RIM 11) can predict the F2-symmetry mode frequencies for isolated substitutional defects, providing insight into the force‑constant changes caused by the impurity.

## Approach
The approach uses a Green's function formalism applied to a defect crystal. The perfect host lattice dynamics are described by a rigid‑ion model with eleven force‑constant parameters (RIM 11) fitted to neutron scattering and infrared data for InP. The impurity is modelled by a mass change on the substituted site and a uniform scaling of the nearest‑neighbour force constants, quantified by a single parameter t. The key quantity is the 3×3 F2 symmetry block of the defect‑space Green's function matrix g* and perturbation matrix δl*. The mode frequency is the root of Re[det(I – g*·δl*)] = 0. The agent implements the host dynamical matrix, computes the necessary Green's function components by summing over a fine k‑point mesh in the Brillouin zone, assembles the F2 block matrices for each impurity case, and solves the secular determinant for the frequency.

**Note on omitted step:** The RIM 11 parameter‑fitting stage (which used experimental phonon frequencies, elastic constants, and two‑phonon IR absorption peaks) is deliberately omitted. The required experimental data for the Σ‑branch dispersion and the fine IR absorption curve are not available in machine‑readable form, and the fitting involved heuristic matching of histogram peaks that cannot be fully automated. The 11 parameters are taken from the published literature and are provided as fixed inputs below.

## Reproduction target
Compute the F2‑symmetry vibrational mode frequencies for two substitutional impurities in InP:

1. Boron (mass 11 u) substituting on the indium site, with a force‑constant change parameter t = +0.25.
2. Arsenic (mass 75 u) substituting on the phosphorus site, with t = +0.07.

Write the results to `/app/outputs/impurity_frequencies.csv` with columns: `impurity_site`, `impurity_mass` (in atomic mass units), `force_constant_change_t`, and `computed_frequency` (in cm⁻¹). The computed frequency is the solution to the secular equation described in the workflow steps.

## Assets

- Python with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute host lattice Green's function components
- Role: process
- Action: Implement the perfect-crystal dynamical matrix for InP using the RIM 11 rigid-ion model parameters (a0=2.9343 Å, M1=30.93 u, M2=114.82 u, Z=0.82, A=-0.365, B=-0.100, C1=-0.017, D1=-0.003, E1=+0.05, F1=-0.071, C2=-0.043, D2=-0.120, E2=+0.110, F2=+0.177, all short-range constants in 10⁵ dyne/cm). Compute the 12 required Green's function components G_αβ(κκ'; ω²) by summing over a fine k-point mesh in the Brillouin zone for a frequency grid covering 0 to 2*ω_LO. Save the components as a NumPy archive for later use.
- Evidence: `/app/outputs/green_functions.npz`

### Step 2: Solve for F2 impurity vibrational mode frequencies
- Role: scored (load-bearing)
- Action: For two impurity cases: (i) B substituting on the In site (impurity mass 11 u, force-constant change parameter t=+0.25); (ii) As substituting on the P site (impurity mass 75 u, t=+0.07). Construct the 3×3 F2 symmetry block matrices g* and δl* using the pre-computed Green's function components. Solve for the frequency where Re[det(I - g*·δl*)] = 0, identifying the localized mode frequency for B/In (above the phonon maximum) and the gap mode for As/P (between acoustic and optical bands). Write the results to impurity_frequencies.csv.
- Output file: `/app/outputs/impurity_frequencies.csv`
- Format: csv
- Contract: impurity_site (str), impurity_mass (float), force_constant_change_t (float), computed_frequency (float, cm⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/impurity_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### impurity_frequencies.csv
- path: `/app/outputs/impurity_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed vibrational mode frequencies (F2 symmetry) for two impurity-host pairs. The computed frequency is the solution of the secular determinant; the checker compares it to the experimental reference within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `impurity_site`, `impurity_mass`, `force_constant_change_t`, `computed_frequency`
  - `units`:
    - `impurity_mass`: atomic mass units (u)
    - `computed_frequency`: cm⁻¹

Notes: Only the F2 symmetry modes are computed. The host Green's functions are constructed from the RIM 11 parameter set given in the paper. The agent must implement the Brillouin zone summation and secular equation root-finding. The experimental frequencies for B/In and As/P are not disclosed in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "impurity_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity_site",
          "impurity_mass",
          "force_constant_change_t",
          "computed_frequency"
        ],
        "units": {
          "impurity_mass": "atomic mass units (u)",
          "computed_frequency": "cm⁻¹"
        }
      },
      "description": "Computed vibrational mode frequencies (F2 symmetry) for two impurity-host pairs. The computed frequency is the solution of the secular determinant; the checker compares it to the experimental reference within a hidden tolerance."
    }
  ],
  "notes": "Only the F2 symmetry modes are computed. The host Green's functions are constructed from the RIM 11 parameter set given in the paper. The agent must implement the Brillouin zone summation and secular equation root-finding. The experimental frequencies for B/In and As/P are not disclosed in this contract."
}
```

## How you are scored
A hidden verifier reads your CSV output and compares each computed frequency to the experimentally known mode frequency for the same impurity and t value. The reward is a weighted combination of the accuracy of the two reported frequencies: large deviations lower the score. The verifier uses a tolerance that accounts for typical numerical and implementation differences. Simply reporting the correct numbers without a faithful implementation of the Green's function method is unlikely to succeed. The verifier also checks that the CSV contains the required columns and that the file is well‑formed.
