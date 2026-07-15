# Ab initio phonon dispersion of free-standing graphene monolayer

## Problem background
Knowledge of phonon characteristics in honeycomb-layer materials such as graphene is important for applications ranging from ultrahard coatings to superconductivity. Phonon dispersion curves can be measured by high-resolution electron energy-loss spectroscopy (HREELS), but the experimental setup is demanding. Ab initio density-functional theory (DFT) calculations provide an independent, fully computational route to obtain phonon dispersions and can complement or validate experimental data. This task reproduces the ab initio phonon calculation of a free-standing graphene monolayer, isolating the purely computational component of a combined HREELS+DFT investigation.

## Approach
The graphene monolayer is modeled using a rectangular supercell of 32 carbon atoms with an in-plane lattice constant of 2.46 Å (the bulk graphite value). Using a DFT code capable of phonon calculations (e.g., Quantum ESPRESSO, Abinit), compute the total energy and Hellmann–Feynman forces for the equilibrium geometry and for configurations with small atomic displacements. Extract force constants up to the 16th nearest neighbour, construct the dynamical matrix, and diagonalise it to obtain the phonon frequencies at the Γ, M, and K high-symmetry points of the two-dimensional surface Brillouin zone. The calculation should be performed for a free-standing monolayer (no substrate). Report frequencies for all six branches: longitudinal acoustic (LA), transverse acoustic (TA), out-of-plane acoustic (ZA), longitudinal optical (LO), transverse optical (TO), and out-of-plane optical (ZO).

## Reproduction target
Produce a CSV file containing the phonon frequencies at the three high-symmetry points. The CSV must have the columns: k_point (one of 'Gamma', 'M', 'K'), branch (one of 'LA','TA','ZA','LO','TO','ZO'), and frequency_cm1 (float, in inverse centimetres). Each combination of k-point and branch must appear exactly once, giving 18 rows. The values must be computed from your DFT phonon calculation.

## Assets

- Open-source DFT code for phonon calculations (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Carbon pseudopotential for DFT (e.g., from SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct the graphene supercell model
- Role: process
- Action: Construct a rectangular supercell of a graphene monolayer containing 32 carbon atoms with an in-plane lattice constant of 2.46 Å. Prepare the necessary input files for the chosen DFT code (e.g., atomic positions, cell vectors, pseudopotential files) to enable a subsequent phonon calculation using the finite-displacement or density-functional perturbation theory (DFPT) method.
- Evidence: `/app/outputs/supercell_input.in`

### Step 2: Compute phonon frequencies at high-symmetry points
- Role: scored (load-bearing)
- Action: Perform DFT total-energy and force calculations on the 32-atom graphene supercell to obtain Hellmann–Feynman forces for displaced atomic configurations. Extract force constants up to the 16th nearest neighbor, construct the dynamical matrix, and diagonalize it to compute phonon frequencies. Report the frequencies (in cm⁻¹) for all six phonon branches (LA, TA, ZA, LO, TO, ZO) at the Γ, M, and K high-symmetry points of the surface Brillouin zone. Write the results to the output CSV file.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: k_point (string: Gamma/M/K), branch (string: LA/TA/ZA/LO/TO/ZO), frequency_cm1 (float). Each k_point has six rows, one per branch.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed phonon frequencies at Γ, M, K for each phonon branch. The hidden checker compares each frequency against the paper's theoretical reference values using per-branch tolerances and structural checks (e.g., LO/TO degeneracy at Γ).
- schema:
  - `type`: table
  - `required_columns`: `k_point`, `branch`, `frequency_cm1`
  - `units`:
    - `frequency_cm1`: cm^{-1}

Notes: The reference values are the DFT phonon frequencies digitized from Figure 4 of the source paper. Tolerances are set to absorb spread from different DFT implementations while requiring a genuine calculation. Additional structural checks (branch ordering, degeneracies) are included but carry low weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_point",
          "branch",
          "frequency_cm1"
        ],
        "units": {
          "frequency_cm1": "cm^{-1}"
        }
      },
      "description": "Computed phonon frequencies at Γ, M, K for each phonon branch. The hidden checker compares each frequency against the paper's theoretical reference values using per-branch tolerances and structural checks (e.g., LO/TO degeneracy at Γ)."
    }
  ],
  "notes": "The reference values are the DFT phonon frequencies digitized from Figure 4 of the source paper. Tolerances are set to absorb spread from different DFT implementations while requiring a genuine calculation. Additional structural checks (branch ordering, degeneracies) are included but carry low weight."
}
```

## How you are scored
Your submitted `phonon_frequencies.csv` is evaluated by a hidden verifier. The verifier compares each frequency against a hidden reference set of phonon frequencies digitised from the original theoretical study. The comparison uses per-branch tolerances: optical branches (LO, TO, ZO) are allowed a larger tolerance than acoustic branches (LA, TA, ZA) to account for inevitable spread between different DFT codes and pseudopotentials. Additionally, the verifier performs structural checks: the LO and TO branches must be degenerate at the Γ point, and optical branches must lie at higher frequencies than acoustic branches throughout. The final reward is a numerical score between 0 and 1 based on how many frequencies fall within their tolerance and whether the structural constraints are satisfied.
