# Buckling onset strain of hydrogenated graphyne under uniaxial compression

## Problem background
Graphyne is a two-dimensional carbon allotrope formed by inserting acetylenic linkages (carbon–carbon triple bonds) into a graphene-like honeycomb network. Its mechanical stability under compressive loads is critical for load-bearing applications in nanocomposites. When graphyne is functionalized with hydrogen adatoms, its morphology and bonding character change, potentially altering its resistance to buckling. The central question is **what is the buckling onset strain of pristine graphyne, and how does that strain vary when hydrogen atoms are adsorbed at different surface coverages**, under uniaxial compression at a very low temperature that suppresses thermal fluctuations.

## Approach
The reproduction uses classical molecular dynamics (MD) simulations performed with the LAMMPS package and the AIREBO potential, which captures C–C and C–H interactions. First, an atomically precise model of a pristine graphyne sheet (20 nm long, 4.4 nm wide, containing 3125 carbon atoms with single acetylenic linkages in a honeycomb arrangement) is built. Randomly distributed hydrogen adatoms are then added at a series of coverages spanning 0–50 %. For each configuration, the system is equilibrated in an NPT ensemble at 0.01 K and subsequently compressed uniaxially with simply supported boundary conditions (the ends are free to rotate but fixed in the out-of-plane direction) at a controlled strain rate. During compression the square-average out-of-plane displacement ⟨h²⟩ is recorded as a function of applied strain. The buckling onset point is identified by the sudden upturn in ⟨h²⟩; the strain at which this occurs is the buckling onset strain. This procedure is repeated for every hydrogen coverage, yielding the full set of onset strains.

## Reproduction target
Produce a single comma-separated value (CSV) file, `/app/outputs/buckling_onset_strains.csv`, that reports the buckling onset strain for every hydrogen coverage: 0 %, 0.15 %, 1 %, 5 %, 10 %, 15 %, 20 %, 25 %, 30 %, 40 %, and 50 %. The CSV must have the columns `H_coverage` (numeric coverage in percent) and `buckling_onset_strain` (numeric strain in percent). The values must come from the MD buckling simulations as described in the workflow steps.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- AIREBO potential file (CH.airebo)

## Workflow steps

### Step 1: Construct pristine graphyne model
- Role: process
- Action: Generate initial atomic coordinates for a rectangular graphyne sheet (20 nm × 4.4 nm, 3125 carbon atoms) with single acetylenic linkages in a honeycomb arrangement. Write a LAMMPS data file.
- Evidence: `/app/outputs/pristine_graphyne.data`

### Step 2: Hydrogenate graphyne at various coverages
- Role: process
- Action: Randomly add hydrogen adatoms to the pristine graphyne sheet at the coverages listed in Table 1: 0, 0.15, 1, 5, 10, 15, 20, 25, 30, 40, 50%. For each coverage, produce a separate LAMMPS data file.
- Evidence: `/app/outputs/hydrogenated_configurations`

### Step 3: Run MD buckling simulations
- Role: process
- Action: For each hydrogenated configuration, run a LAMMPS MD simulation with the AIREBO potential: equilibrate in NPT at 0.01 K, then compress uniaxially with simply supported boundary conditions (ends free to rotate, no z-displacement) at a strain rate of 0.85×10⁻³ ps⁻¹ in NVT, recording the square-average out-of-plane displacement ⟨h²⟩ as a function of compressive strain.
- Evidence: `/app/outputs/simulation_trajectories`

### Step 4: Detect and report buckling onset strains
- Role: scored (load-bearing)
- Action: For each hydrogen coverage, analyse the ⟨h²⟩ vs. strain data and identify the strain where ⟨h²⟩ suddenly increases (the buckling onset point). Collect these strains and write them to a CSV file.
- Output file: `/app/outputs/buckling_onset_strains.csv`
- Format: csv
- Contract: CSV with columns: H_coverage (percentage, float), buckling_onset_strain (percentage, float). Must include rows for coverages: 0, 0.15, 1, 5, 10, 15, 20, 25, 30, 40, 50.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/buckling_onset_strains.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### buckling_onset_strains.csv
- path: `/app/outputs/buckling_onset_strains.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Buckling onset strains for each hydrogen coverage, to be compared against the paper's reference values.
- schema:
  - `type`: table
  - `required_columns`: `H_coverage`, `buckling_onset_strain`
  - `units`:
    - `H_coverage`: %
    - `buckling_onset_strain`: %

Notes: The checker will compare each strain to the hidden gold with an absolute tolerance and verify the coverage-dependent trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "buckling_onset_strains.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "H_coverage",
          "buckling_onset_strain"
        ],
        "units": {
          "H_coverage": "%",
          "buckling_onset_strain": "%"
        }
      },
      "description": "Buckling onset strains for each hydrogen coverage, to be compared against the paper's reference values."
    }
  ],
  "notes": "The checker will compare each strain to the hidden gold with an absolute tolerance and verify the coverage-dependent trend."
}
```

## How you are scored
A hidden verifier independently reads your `buckling_onset_strains.csv`. For each coverage, the reported onset strain is compared against a set of expected values, with a tolerance that accounts for legitimate toolchain variation. The verifier also checks that the coverage‑dependent pattern (e.g., the overall shape of the strain‑vs‑coverage curve) is physically sensible and consistent with the reference data. No single numeric target is revealed here; faithfully following the MD protocol is essential. The final score is a weighted combination of per‑coverage accuracy and trend adherence.
