# Phonon dispersion computation of germanium via rigid-ion pseudo-atom model with perturbative exchange-correlation

## Problem background
Germanium is a prototypical covalent semiconductor. Computing its phonon dispersion – the frequencies of lattice vibrations as a function of wavevector – is important for understanding thermal, elastic, and transport properties. First-principles methods are accurate but computationally heavy. An alternative is to build a physically motivated model where each ion carries a "pseudo-atom" consisting of a rigid central part and halves of the nearest-neighbor bond charges, and then calculate the phonon frequencies from a quantum-mechanical dynamical matrix. This task asks you to implement such a model and produce the phonon frequencies for germanium along the high-symmetry Gamma–X and Gamma–L directions.

## Approach
You will construct a rigid-ion pseudo-atom model for diamond-structure germanium. Each pseudo-atom has:
- a **central part** whose charge distribution is given by the unscreened pseudopotential (the average of Ga and As form factors from Chelikowsky and Cohen, Phys. Rev. B 13, 826 (1976))
- **four bond-charge halves**, one for each nearest-neighbor bond, placed at the correct fractional coordinates. Each half has a spherically symmetric charge density C(1+γr)e^{−γr} with γ = 4.65 atomic units and total charge 1/ε(0,0).

From this model you will compute the electronic part of the dynamical matrix at the Hartree level by transforming the pseudo-atom charge densities to reciprocal space and summing over reciprocal lattice vectors. The ion–ion part is computed with the Ewald method. You will then add an exchange–correlation (XC) contribution: using first-order perturbation theory in the Kohn–Sham local-density approximation (α = 0.8) you will compute the attractive force constant between the two halves of each bond charge and incorporate it into the dynamical matrix. Finally you will diagonalize the total dynamical matrix at a set of q-points along the Gamma–X and Gamma–L directions to obtain the phonon eigenfrequencies.

## Reproduction target
Produce a CSV file `/app/outputs/phonon_frequencies.csv` that contains the real phonon eigenfrequencies (in THz) for each branch – LA, TA, LO, TO – at a dense set of q-points along two symmetry directions:
- Gamma–X: from (0,0,0) to (1,0,0) in reciprocal lattice units
- Gamma–L: from (0,0,0) to (0.5,0.5,0.5) in reciprocal lattice units.
The file must have the columns qx, qy, qz, branch, frequency_THz as described in the output contract. The task is complete when this artifact is written.

## Assets

- Chelikowsky-Cohen pseudopotential form factors for Ga and As (averaged for Ge): 10.1103/PhysRevB.13.826
- Walter-Cohen dielectric function model for Ge: 10.1103/PhysRevB.2.1821
- Python scientific computing stack (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Construct pseudo-atom model for germanium
- Role: process
- Action: Define the unscreened pseudopotential as average of Ga and As form factors from Chelikowsky-Cohen. Parameterize bond charge shape using γ=4.65 au and total charge 1/ε(0,0). Set up diamond lattice (a ≈ 5.65 Å) and assign bond-charge halves at correct fractional coordinates. Construct central part distribution from pseudopotential and dielectric function as given in the model description.
- Evidence: `/app/outputs/model_setup.json`

### Step 2: Compute Hartree-level dynamical matrix electronic contributions
- Role: process
- Action: For each q-point of interest, calculate the ion-ion interaction via Ewald method and the electronic contribution using the pseudo-atom charge densities transformed to reciprocal space. Sum over a sufficiently dense set of reciprocal lattice vectors to assemble the dynamical matrix D_αβ(q) without exchange-correlation effects.
- Evidence: `/app/outputs/hartree_matrix_check.json`

### Step 3: Compute exchange-correlation contribution to dynamical matrix
- Role: process
- Action: Evaluate the XC energy contribution arising from the overlap of bond charge halves, using the perturbative Kohn-Sham local-density approximation with parameter α=0.8. Compute the resulting nearest-neighbor attractive force constant and add it to the dynamical matrix obtained in step02.
- Evidence: `/app/outputs/xc_contribution.json`

### Step 4: Solve eigenvalue problem and output phonon frequencies
- Role: scored (load-bearing)
- Action: Diagonalize the total dynamical matrix (Hartree + XC) for a set of q-points along the Γ–X direction (from (0,0,0) to (1,0,0) in reciprocal lattice units) and along Γ–L (from (0,0,0) to (0.5,0.5,0.5)). Write the resulting real eigenfrequencies (in THz) for each branch (LA, TA, LO, TO) to phonon_frequencies.csv.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: CSV with header: qx, qy, qz, branch, frequency_THz. q coordinates in reciprocal lattice units.
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
- description: Phonon frequencies of germanium along high-symmetry directions, computed using the pseudo-atom model with exchange-correlation. The frequencies are compared against a hidden reference (experimental data) within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `qx`, `qy`, `qz`, `branch`, `frequency_THz`
  - `units`:
    - `frequency_THz`: THz

Notes: The checker computes mean absolute error per branch against a hidden experimental reference. All frequencies must be real (no imaginary part).

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
          "qx",
          "qy",
          "qz",
          "branch",
          "frequency_THz"
        ],
        "units": {
          "frequency_THz": "THz"
        }
      },
      "description": "Phonon frequencies of germanium along high-symmetry directions, computed using the pseudo-atom model with exchange-correlation. The frequencies are compared against a hidden reference (experimental data) within a tolerance."
    }
  ],
  "notes": "The checker computes mean absolute error per branch against a hidden experimental reference. All frequencies must be real (no imaginary part)."
}
```

## How you are scored
After you submit, a hidden verifier will read your `phonon_frequencies.csv` and compare the frequencies against a hidden reference dataset. The verifier will compute a mean absolute error per branch and produce a combined score between 0 and 1. Only the artifact you write under `/app/outputs/` is evaluated; intermediate evidence files (e.g. `model_setup.json`) are not scored but are required to document your workflow. Reporting a number similar to the paper is not enough – you must demonstrate the full computational pipeline.
