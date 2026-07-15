# Compute Phonon Dispersion in Alkali Metals and Their Sodium‑Based Binary Alloys using a Local Pseudopotential

## Problem background
Phonon dispersion curves are fundamental for understanding lattice dynamics, thermal properties, and electron‑phonon interactions in solids. This task concerns the computation of phonon dispersion curves for five alkali metals (Li, Na, K, Rb, Cs) and four equiatomic sodium‑based binary alloys (Na0.5Li0.5, Na0.5K0.5, Na0.5Rb0.5, Na0.5Cs0.5) within the framework of a local model potential and real‑space Born–von Karman sums. The alloys are treated via a pseudo‑alloy‑atom (PAA) model. The influence of exchange‑correlation effects is investigated by comparing two screening descriptions: a simple Hartree screening and the more advanced Ichimaru–Utsumi local‑field correction. The goal is to obtain the full set of phonon frequencies along the high‑symmetry directions that result from this treatment.

## Approach
You must implement a computational pipeline based on a local pseudopotential approach. The electron‑ion interaction is described by an empty‑core pseudopotential (Gajjar form), which depends on the valence, atomic volume, and a single core‑radius parameter for each pure element. For the alloys, use the pseudo‑alloy‑atom (PAA) model with a linear mixing rule at equiatomic composition to obtain effective parameters. For each material, compute the energy‑wavenumber characteristic F(q) from the bare‑ion pseudopotential and the dielectric screening, using both a Hartree dielectric function alone and the Ichimaru–Utsumi local‑field correction added. From F(q), evaluate the tangential and radial interatomic force constants by numerical integration up to a large momentum cutoff. Sum these force constants over the first several coordination shells of the bcc lattice to build the dynamical matrix at a dense grid of wave‑vectors along the [100], [110], and [111] directions. Solve the resulting secular determinant to obtain the three phonon eigenfrequencies per q‑point. The final deliverable is a CSV file containing the computed frequencies for all five pure metals and four alloys, for both screening conditions.

## Reproduction target
Produce the complete phonon dispersion curves for the five pure alkali metals (Li, Na, K, Rb, Cs) and the four equiatomic sodium‑based binary alloys (Na0.5Li0.5, Na0.5K0.5, Na0.5Rb0.5, Na0.5Cs0.5), along the high‑symmetry directions [100], [110], and [111], using both Hartree (H) and Ichimaru–Utsumi (IU) exchange‑correlation screening. For each material × direction × screening combination, use a grid of at least 50 reduced wave‑vectors spanning 0 to 1. The output file `/app/outputs/phonon_dispersion.csv` must contain columns: material, direction, q_reduced, branch (L, T1, T2), screening (H or IU), frequency (in THz). All 9 materials, 3 directions, 2 screening conditions, and three branches must be covered.

## Assets

- Pure metal properties and Gajjar pseudopotential parameters: 10.1007/s11706-008-0039-z
- Ichimaru–Utsumi local field correction function: 10.1103/PhysRevB.24.7385
- Static Hartree dielectric function

## Workflow steps

### Step 1: Prepare material parameters and lattice shell vectors
- Role: process
- Action: Collect pure element properties (Z, Ω0, kF, M, rC) for Li, Na, K, Rb, Cs; compute pseudo‑alloy‑atom parameters for equiatomic Na‑based binary alloys (Na0.5Li0.5, Na0.5K0.5, Na0.5Rb0.5, Na0.5Cs0.5) using linear mixing rules with X=0.5; generate BCC lattice vectors and list up to 33 neighbor‑shell vectors with distances.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Compute phonon dispersion curves
- Role: scored (load-bearing)
- Action: Implement the Gajjar empty‑core pseudopotential; compute the energy wave‑number characteristic F(q) with both Hartree and Ichimaru–Utsumi screening; evaluate tangential (Kt) and radial (Kr) force constants via numerical integration up to 40 kF using the integrals given in the methodology; construct the dynamical matrix via Born–von Karman sum over 33 neighbor shells; solve the secular determinant for phonon frequencies at a grid of q‑points along [100], [110], [111] directions for all five pure alkali metals and four equiatomic alloys. Output all computed frequencies in phonon_dispersion.csv.
- Output file: `/app/outputs/phonon_dispersion.csv`
- Format: csv
- Contract: CSV with header: material,direction,q_reduced,branch,screening,frequency. material: one of Li, Na, K, Rb, Cs, Na0.5Li0.5, Na0.5K0.5, Na0.5Rb0.5, Na0.5Cs0.5. direction: one of 100,110,111. q_reduced: float in [0,1]. branch: one of L, T1, T2. screening: H or IU. frequency: float (THz).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_dispersion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_dispersion.csv
- path: `/app/outputs/phonon_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Main reproduction target: phonon dispersion frequencies computed using the Gajjar empty‑core pseudopotential with both Hartree and Ichimaru–Utsumi exchange‑correlation screening. The verifier recomputes frequencies independently and scores based on mean absolute percentage error against the number of materials and alloys.
- schema:
  - `type`: table
  - `required_columns`: `material`, `direction`, `q_reduced`, `branch`, `screening`, `frequency`
  - `units`:
    - `frequency`: THz
    - `q_reduced`: dimensionless
  - `description`: CSV containing phonon frequencies for all 9 materials (5 pure + 4 alloys), 3 high‑symmetry directions ([100], [110], [111]), 2 screening functions (H, IU), and 3 branches (L, T1, T2) per q‑point. At least 50 q‑points per direction per material per screening.

Notes: The verifier will recompute frequencies using the same physical model with identical parameters and numerical cutoffs. Agreement is quantified by mean absolute percentage error (MAPE) across all reported entries, with a threshold‑based scoring policy. Additional structural checks may include ordering of longitudinal vs transverse branches and monotonic trends with atomic mass.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "direction",
          "q_reduced",
          "branch",
          "screening",
          "frequency"
        ],
        "units": {
          "frequency": "THz",
          "q_reduced": "dimensionless"
        },
        "description": "CSV containing phonon frequencies for all 9 materials (5 pure + 4 alloys), 3 high‑symmetry directions ([100], [110], [111]), 2 screening functions (H, IU), and 3 branches (L, T1, T2) per q‑point. At least 50 q‑points per direction per material per screening."
      },
      "description": "Main reproduction target: phonon dispersion frequencies computed using the Gajjar empty‑core pseudopotential with both Hartree and Ichimaru–Utsumi exchange‑correlation screening. The verifier recomputes frequencies independently and scores based on mean absolute percentage error against the number of materials and alloys."
    }
  ],
  "notes": "The verifier will recompute frequencies using the same physical model with identical parameters and numerical cutoffs. Agreement is quantified by mean absolute percentage error (MAPE) across all reported entries, with a threshold‑based scoring policy. Additional structural checks may include ordering of longitudinal vs transverse branches and monotonic trends with atomic mass."
}
```

## How you are scored
A hidden verifier will independently re‑implement the same physical model (same pseudopotential, screening functions, integration parameters, and shell summation) and recompute the phonon frequencies for every combination present in your CSV. The verifier will compare your submitted frequencies against its own reference values using mean absolute percentage error (MAPE) across all rows. The reward decreases as the error increases; a solution that closely reproduces the model’s predictions receives a high score. Additional structural checks, such as the correct ordering of longitudinal versus transverse branches, may also contribute to the final score. Reporting numbers without performing the actual computation will not satisfy the verifier, because it compares the frequencies themselves, not the summary statistics.
