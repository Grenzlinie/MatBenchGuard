# Phonon dispersion from EAM potential with third-neighbor interactions

## Problem background
Transition metals such as Ni and Pd are widely studied because of their technological and fundamental importance. Accurate interatomic potentials are needed to predict vibrational properties. The Embedded Atom Method (EAM) is a semi-empirical scheme that approximates the total energy as a sum of an embedding function and a pair repulsion. When only nearest-neighbour interactions are kept, the EAM can reproduce elastic constants and low-frequency vibrations, but it often fails to predict phonon frequencies at the Brillouin-zone boundary. Introducing longer-range contributions, in particular force constants from third-neighbour pair interactions, may correct this deficiency. This task asks you to re-derive a modified EAM that includes third-neighbour corrections and to test whether the resulting phonon dispersion agrees with neutron-scattering experiments.

## Approach
The total energy of an fcc metal is written in the EAM form: a sum of an embedding energy F(ρ) (modelled by a cubic spline) and a pairwise term Z^2(R)/R. An effective charge Z(R) and the embedding function F(ρ) are represented by spline knots. Beyond the first-neighbour pair interactions, third-neighbour force constants φ₃′ and φ₃″ are introduced to modify the force field. The unknown parameters (spline knots, φ₃′, φ₃″) are obtained by fitting to several target quantities: the lattice constant a₀, cohesive energy E_coh, cubic elastic constants C₁₁, C₁₂, C₄₄, vacancy-formation energy E_vf, and zone-boundary phonon frequencies at the X and L points extracted from published neutron-scattering data for Ni (Birgeneau et al., 1964) and Pd (Muller & Brockhouse, 1971). Once the potential is fitted, the dynamical matrix for the fcc lattice is constructed and diagonalized along the [100], [110], [111] high-symmetry directions, giving the full phonon dispersion at a dense set of wavevectors. The resulting frequencies are compared against experimental measurements.

## Reproduction target
Fit an EAM potential for fcc Ni and Pd that incorporates third-neighbour force constants, using the experimental lattice constant, cohesive energy, elastic constants, vacancy-formation energy, and zone-boundary phonon frequencies from the public neutron-scattering datasets of Birgeneau et al. (1964) for Ni and Muller & Brockhouse (1971) for Pd as fitting targets. Then use the fitted potential to compute phonon frequencies for both metals along the [100], [110], and [111] directions at q-points spaced no larger than 0.02 in reduced units (q_reduced = 0.0 to 0.5). Output the frequencies for all branches in the file `/app/outputs/phonon_frequencies.csv` according to the schema described below. The aim is to produce dispersion curves that agree closely with the experimental data on which they are ultimately evaluated.

## Assets

- Experimental phonon dispersion of Ni (Birgeneau et al., 1964): 10.1103/PhysRev.136.A1359
- Experimental phonon dispersion of Pd (Muller & Brockhouse, 1971): 10.1139/p71-119
- EAM simulation and dynamics code

## Workflow steps

### Step 1: Fit EAM potential with third-neighbor interactions for Ni and Pd
- Role: process
- Action: Fit the embedded atom method (EAM) potential for fcc Ni and Pd. The potential includes a nearest-neighbor pair repulsion φ(R) and embedding function F(ρ) described by cubic splines, plus third-neighbor force-constant parameters φ3' and φ3'' that modify the force field beyond the first shell. Fit targets: experimental lattice constant a0, cohesive energy E_coh, cubic elastic constants C11, C12, C44, vacancy-formation energy E_vf, and zone-boundary phonon frequencies at X and L points extracted from published neutron scattering data (Birgeneau et al. for Ni; Muller & Brockhouse for Pd). Represent the embedding function and effective charge Z(R) as splines; optimize the spline knots and third-neighbor parameters. Output the final fitted parameters (spline knots, φ3', φ3'') in a log file.
- Evidence: `/app/outputs/eam_fit_log.txt`

### Step 2: Compute phonon dispersion curves for Ni and Pd
- Role: scored (load-bearing)
- Action: Using the fitted EAM potential, construct the dynamical matrix for fcc Ni and Pd at a dense set of wavevectors along high-symmetry directions [100], [110], [111]. Diagonalize to obtain phonon frequencies for all branches (LA, TA, etc.). Output the frequencies at q-points from q_reduced=0.0 to the zone boundary (0.5) with spacing no larger than 0.02.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: metal (str: 'Ni' or 'Pd'), direction (str: '[100]', '[110]', '[111]'), q_reduced (float, in units of 2π/a), branch (str: e.g., 'LA', 'TA[001]', 'TA[1-10]'), frequency_THz (float). Each row represents a single phonon branch at a given q-point.
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
- target_policy: threshold_or_better
- description: Computed phonon frequencies. The hidden checker will calculate mean absolute percentage error against experimental reference data and score full credit if the error is ≤5%.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `direction`, `q_reduced`, `branch`, `frequency_THz`

Notes: Only the phonon_frequencies.csv is scored; the fitting log is for evidence that the potential was fitted, not scored. The dispersion must include both Ni and Pd, all high-symmetry directions, all branches, and a dense q-point grid.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "direction",
          "q_reduced",
          "branch",
          "frequency_THz"
        ]
      },
      "description": "Computed phonon frequencies. The hidden checker will calculate mean absolute percentage error against experimental reference data and score full credit if the error is ≤5%."
    }
  ],
  "notes": "Only the phonon_frequencies.csv is scored; the fitting log is for evidence that the potential was fitted, not scored. The dispersion must include both Ni and Pd, all high-symmetry directions, all branches, and a dense q-point grid."
}
```

## How you are scored
Your submission is scored by a hidden verifier that compares the phonon frequencies in `phonon_frequencies.csv` against experimental reference values (not provided to you). The verifier computes an error metric that measures the deviation between your reported frequencies and the hidden gold; you receive a higher reward when your error is smaller and the dispersion curves are physically reasonable. The fitting log `eam_fit_log.txt` is required as evidence that the potential was fitted, but its content is not directly scored; only the phonon_frequencies.csv carries reward. The final score is a weighted combination, with the bulk of the weight on the accuracy of the phonon dispersion. Reporting numbers that are not the result of a genuine fitting and diagonalization pipeline will not lead to a good score.
