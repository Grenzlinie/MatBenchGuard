# Phonon Dispersion in Distorted 2D Peierls Phase

## Problem background
The Peierls phase in a two-dimensional (2D) half-filled square-lattice Su-Schrieffer-Heeger (SSH) model exhibits static lattice distortions with multiple wavevectors parallel to the nesting vector Q=(π,π). Different distortion patterns—different combinations of Fourier components—can have the same ground-state energy but modify the Brillouin zone, leading to distinct phonon branch structures and gap positions. This task investigates the phonon dispersion (squared frequencies ω² as a function of wavevector q) at zero temperature for two such distortion patterns, with the goal of capturing how the pattern affects the dispersion.

## Approach
The task is to implement the 2D SSH Hamiltonian on an N×N square lattice with periodic boundary conditions. For two predefined distortion patterns—pattern (a) containing Fourier components Q=(π,π) and Q/2, and pattern (b) containing Q, Q/4, and 3Q/4—self-consistently determine the electronic eigenstates at T=0 and λ=0.65. Using these electronic states, construct the phonon dynamical matrix K_{a,b}(q1,q2;q') for the group index q'=0, as described in the model. Diagonalize this matrix for each allowed wavevector q along (q,q) in the reduced-Brillouin-zone to obtain the squared phonon frequencies. Output the dispersion (ω² vs q) as CSV files with branches sorted in ascending order.

## Reproduction target
Compute the T=0 phonon dispersion curves (squared frequencies ω² as a function of reduced-zone wavevector q along the diagonal) for two static distortion patterns on a 64×64 square lattice at λ=0.65. For pattern (a) with Fourier components Q and Q/2, write the sorted ω² values for each q to `dispersion_pattern_a.csv`. For pattern (b) with Q, Q/4, and 3Q/4, write them to `dispersion_pattern_b.csv`. The objective is to produce the dispersion data; the verifier will subsequently confirm that the number of branches per q and the presence and positions of phonon gaps in the extended zone scheme correctly reflect each distortion pattern.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve static Peierls distortions and electronic structure
- Role: process
- Action: Self-consistently solve the 2D SSH model on a 64×64 square lattice at T=0 with electron‑lattice coupling λ=0.65 for two distortion patterns: pattern (a) with Fourier components Q=(π,π) and Q/2, and pattern (b) with Q, Q/4, and 3Q/4. Determine electronic eigenenergies and wavefunction coefficients for both patterns.
- Evidence: `/app/outputs/static_distortion_data.npz`

### Step 2: Construct phonon dynamical matrices
- Role: process
- Action: For each distortion pattern, construct the 2N×2N dynamical matrix K_{a,b}(q1,q2;q') with group index q'=0, using the electronic states from the static solution, following the matrix definition in the paper.
- Evidence: `/app/outputs/phonon_matrices.npz`

### Step 3: Output phonon dispersion for pattern (a)
- Role: scored (load-bearing)
- Action: For pattern (a), diagonalize the phonon dynamical matrix at each reduced-zone wavevector q = 0, …, N/4 along (q,q). Write the sorted squared phonon frequencies ω² for each q to dispersion_pattern_a.csv.
- Output file: `/app/outputs/dispersion_pattern_a.csv`
- Format: csv
- Contract: A CSV file with header row 'q' followed by columns named 'omega2_0', 'omega2_1', ... up to the number of branches for the pattern. The columns are sorted in ascending order of squared frequency. q is an integer representing q*N/(2π). omega2_i are floats.
- Scoring: scored by hidden verifier

### Step 4: Output phonon dispersion for pattern (b)
- Role: scored (load-bearing)
- Action: For pattern (b), diagonalize the phonon dynamical matrix at each reduced-zone wavevector q = 0, …, N/8 along (q,q). Write the sorted squared phonon frequencies ω² for each q to dispersion_pattern_b.csv.
- Output file: `/app/outputs/dispersion_pattern_b.csv`
- Format: csv
- Contract: A CSV file with header row 'q' followed by columns named 'omega2_0', 'omega2_1', ... up to the number of branches for the pattern. The columns are sorted in ascending order of squared frequency. q is an integer representing q*N/(2π). omega2_i are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_pattern_a.csv`
- `/app/outputs/dispersion_pattern_b.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_pattern_a.csv
- path: `/app/outputs/dispersion_pattern_a.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion for pattern (a). Used to verify branch count and gap positions after unfolding to extended zone.
- schema:
  - `type`: table
  - `columns`:
    - `name`: q
    - `type`: integer
    - `name_pattern`: omega2_\d+
    - `type`: float
    - `sorted`: True
  - `description`: Phonon dispersion for pattern (a) at T=0, λ=0.65, N=64, q'=0. First column is q (integer), remaining columns are squared frequencies sorted ascending; exact number of columns depends on the distortion pattern's branch count.

### dispersion_pattern_b.csv
- path: `/app/outputs/dispersion_pattern_b.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion for pattern (b). Used to verify branch count and gap positions after unfolding to extended zone.
- schema:
  - `type`: table
  - `columns`:
    - `name`: q
    - `type`: integer
    - `name_pattern`: omega2_\d+
    - `type`: float
    - `sorted`: True
  - `description`: Phonon dispersion for pattern (b) at T=0, λ=0.65, N=64, q'=0. First column is q (integer), remaining columns are squared frequencies sorted ascending; exact number of columns depends on the distortion pattern's branch count.

Notes: The checker parses the header to determine the number of omega2 columns (branch count) and then performs structural audit (branch count and gaps). The contract does not prescribe a fixed number of columns, so the agent cannot see the expected branch count.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_pattern_a.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "q",
            "type": "integer"
          },
          {
            "name_pattern": "omega2_\\d+",
            "type": "float",
            "sorted": true
          }
        ],
        "description": "Phonon dispersion for pattern (a) at T=0, λ=0.65, N=64, q'=0. First column is q (integer), remaining columns are squared frequencies sorted ascending; exact number of columns depends on the distortion pattern's branch count."
      },
      "description": "Phonon dispersion for pattern (a). Used to verify branch count and gap positions after unfolding to extended zone."
    },
    {
      "file": "dispersion_pattern_b.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "q",
            "type": "integer"
          },
          {
            "name_pattern": "omega2_\\d+",
            "type": "float",
            "sorted": true
          }
        ],
        "description": "Phonon dispersion for pattern (b) at T=0, λ=0.65, N=64, q'=0. First column is q (integer), remaining columns are squared frequencies sorted ascending; exact number of columns depends on the distortion pattern's branch count."
      },
      "description": "Phonon dispersion for pattern (b). Used to verify branch count and gap positions after unfolding to extended zone."
    }
  ],
  "notes": "The checker parses the header to determine the number of omega2 columns (branch count) and then performs structural audit (branch count and gaps). The contract does not prescribe a fixed number of columns, so the agent cannot see the expected branch count."
}
```

## How you are scored
A hidden verifier independently examines each output CSV. For pattern (a) it checks that there are exactly 8 distinct ω² values per q, unfolds the data to the original Brillouin zone, and detects a phonon gap at q=π/2. For pattern (b) it checks for 16 distinct values per q and gaps at q=π/4, π/2, and 3π/4 in the unfolded scheme. The final reward is a weighted combination of the results from each stage; simply reporting numbers without actually running the self-consistent electronic solution and matrix diagonalization will yield zero reward.
