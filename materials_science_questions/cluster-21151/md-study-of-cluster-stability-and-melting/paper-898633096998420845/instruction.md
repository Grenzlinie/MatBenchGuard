# Structural Transformations in Cu Nanoclusters: Combined HSA and PTMD Workflow

## Problem background
Metal nanoclusters exhibit size- and temperature-dependent structural motifs (icosahedron, decahedron, fcc, twin, etc.) that critically influence their properties. Computing the equilibrium probability of these motifs across the entire temperature range, from 0 K to melting, requires efficient sampling of the potential energy surface. The harmonic superposition approximation (HSA) accurately captures low-temperature behavior but fails at higher temperatures due to anharmonic effects and difficulty sampling the melting region. Parallel tempering molecular dynamics (PTMD) effectively samples high-temperature configurations and the melting transition. A combined approach leverages HSA for low temperatures and PTMD for high temperatures, stitching the results to obtain a complete picture. This task reproduces the combined workflow for Cu90 clusters using a Gupta interatomic potential.

## Approach
This workflow models the interactions between Cu atoms with a Gupta (tight-binding second moment approximation) potential. It first performs parallel tempering molecular dynamics across a ladder of replicas covering temperatures from room temperature to above the melting point, allowing the system to overcome barriers between structural motifs. The simulation collects a large pool of distinct local minima. These minima are then classified by structure type (icosahedron, decahedron, fcc, twin, mix, amorphous) using common neighbor analysis. Harmonic superposition approximation is applied to the minima: for each minimum, normal-mode frequencies are computed and used to construct its vibrational partition function, from which temperature-dependent occupation probabilities are derived. The HSA probabilities are accurate up to about 300 K. For higher temperatures, the relative abundances of motifs are obtained directly from the PTMD sampling. The two temperature regimes are joined at 300 K to produce a continuous probability curve from 0 K up to the melting point. The melting temperature is identified from the peak of the heat capacity curve computed from the PTMD simulation.

## Reproduction target
For the Cu90 nanocluster, run the combined HSA+PTMD workflow as detailed in the Workflow steps. Use the Gupta potential parameters from Baletto et al. and the replica temperatures specified in Step 1. The HSA analysis must be performed on all local minima within 1.2 eV of the global minimum. Stitch the HSA results (up to 300 K) with the PTMD results (above 300 K). Output the stitched motif probabilities (Ih, Dh, fcc, twin, mix, amorphous) at temperatures 300, 400, 500, 600, and 609 K into `/app/outputs/structural_distribution_Cu90.csv`. Compute the melting point from the peak of the heat capacity curve and write it to `/app/outputs/melting_point.txt`.

## Assets

- Gupta potential parameters for Cu (Baletto et al., J. Chem. Phys. 2002): https://doi.org/10.1063/1.1426372
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Python scientific stack

## Workflow steps

### Step 1: Parallel Tempering Molecular Dynamics (PTMD) for Cu90
- Role: process
- Action: Run PTMD simulations for a Cu90 cluster using the Gupta potential in LAMMPS. Use these replica temperatures: 300, 315, 331, 347, 365, 383, 402, 423, 444, 466, 490, 514, 540, 550, 558, 567, 575, 584, 592, 601, 609, 617, 626, 634, 643, 651, 659, 668, 676, 685, 693, 702, 710, 720, 746, 772, 800 K. Equilibrate for ~0.5 μs, then sample configurations every 125 ps after each swap attempt for a total sampling time of ~1–2 μs. Collect all local minima visited during the production run (distinct minima differing by at least 0.05 meV or different structure type).
- Evidence: `/app/outputs/ptmd_trajectory.log`

### Step 2: Harmonic Superposition Approximation (HSA) analysis
- Role: process
- Action: From the PTMD-sampled local minima, select those up to an energy cutoff of 1.2 eV above the global minimum (target ~10,000 distinct minima). Classify each minimum into a motif (Ih, Dh, fcc, twin, mix, amorphous) using Common Neighbor Analysis (CNA). For each minimum, compute the normal-mode frequencies via diagonalization of the Hessian. Evaluate the HSA probability as p_i(T) ∝ e^{-E_i^0/(k_B T)} · Z_i^vib / g_i, where the vibrational partition function Z_i^vib = ∏_{n=1}^{3N-6} e^{-ℏ ω_n / (2 k_B T)} / (1 − e^{-ℏ ω_n / (k_B T)}). Sum the normalized probabilities to obtain temperature-dependent motif probabilities up to 300 K.
- Evidence: `/app/outputs/hsa_minima_database.pkl`

### Step 3: Stitched structural distribution output
- Role: scored (load-bearing)
- Action: Combine the HSA motif probabilities (valid up to 300 K) and the PTMD motif probabilities (valid above 300 K) into a single continuous curve. At the stitching temperature 300 K, use the HSA values or an average if there is a small jump. Extract the probabilities of the six motifs (Ih, Dh, fcc, twin, mix, amorphous) at the exact temperatures 300, 400, 500, 600, and 609 K. Save these as a CSV file with columns Temperature, Motif, Probability.
- Output file: `/app/outputs/structural_distribution_Cu90.csv`
- Format: csv
- Contract: Columns: Temperature (float), Motif (string, one of Ih, Dh, fcc, twin, mix, amorphous), Probability (float between 0 and 1). Rows: 5 temperatures x 6 motifs = 30 rows.
- Scoring: scored by hidden verifier

### Step 4: Melting point determination
- Role: scored (load-bearing)
- Action: From the PTMD caloric curve (heat capacity C_V vs temperature), identify the temperature at which C_V reaches its maximum. Output this temperature (in Kelvin) to a single text file.
- Output file: `/app/outputs/melting_point.txt`
- Format: txt
- Contract: A single floating-point number in Kelvin (e.g., 609.0).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_distribution_Cu90.csv`
- `/app/outputs/melting_point.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_distribution_Cu90.csv
- path: `/app/outputs/structural_distribution_Cu90.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the equilibrium motif probabilities at 300, 400, 500, 600, and 609 K.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Motif`, `Probability`
  - `columns`:
    - `Temperature`: float (K)
    - `Motif`: string (one of Ih, Dh, fcc, twin, mix, amorphous)
    - `Probability`: float between 0 and 1
  - `shape`: 30 rows (5 temperatures × 6 motifs)

### melting_point.txt
- path: `/app/outputs/melting_point.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Text file containing the computed melting point (peak of heat capacity curve).
- schema:
  - `type`: text
  - `content`: A single floating-point number representing the melting temperature in Kelvin.

Notes: The hidden checker compares the CSV probabilities against digitized reference values from the paper's Fig. 1a and Fig. 3 with an absolute tolerance of 0.1. The melting point is compared to the paper-reported value (609 K) with a tolerance of 20 K. Full credit for all points within tolerance; reward scales with fraction of points within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_distribution_Cu90.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Motif",
          "Probability"
        ],
        "columns": {
          "Temperature": "float (K)",
          "Motif": "string (one of Ih, Dh, fcc, twin, mix, amorphous)",
          "Probability": "float between 0 and 1"
        },
        "shape": "30 rows (5 temperatures × 6 motifs)"
      },
      "description": "CSV file containing the equilibrium motif probabilities at 300, 400, 500, 600, and 609 K."
    },
    {
      "file": "melting_point.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "A single floating-point number representing the melting temperature in Kelvin."
      },
      "description": "Text file containing the computed melting point (peak of heat capacity curve)."
    }
  ],
  "notes": "The hidden checker compares the CSV probabilities against digitized reference values from the paper's Fig. 1a and Fig. 3 with an absolute tolerance of 0.1. The melting point is compared to the paper-reported value (609 K) with a tolerance of 20 K. Full credit for all points within tolerance; reward scales with fraction of points within tolerance."
}
```

## How you are scored
A hidden verifier reads your output files and compares the reported probabilities and melting point against reference values derived from the original study, using an appropriate tolerance. The reward is the fraction of data points (motif probabilities at the specified temperatures and the melting temperature) that fall within the allowed tolerance. To maximize your score, ensure that the simulation protocol is followed correctly and that the stitched probabilities and melting point are reported accurately. Submitting output files with incorrect formatting or missing data will lower your score.
