# Pressure-driven band-structure evolution and quantum transport in a puckered 2D semiconductor

## Problem background
Monolayer black phosphorus (MBP) is a puckered two-dimensional semiconductor with highly anisotropic mechanical and electronic properties. Its open, corrugated structure can undergo large vertical compression, which in turn may significantly alter its band structure and charge transport characteristics. Understanding how vertical compression modifies the electronic properties of pure MBP is important for applications in flexible electronics and pressure sensing. In this task, we investigate the evolution of the band gap (magnitude and direct/indirect character) and the quantum transmission in pure MBP two-probe devices when subjected to a range of vertical compression ratios. The goal is to compute these relationships using first-principles methods and to produce systematic, physically meaningful trends.

## Approach
We use first-principles density functional theory (DFT) and non-equilibrium Green's function (NEGF) methods to study monolayer black phosphorus under vertical compression. First, the atomic structure of an MBP unit cell is partially relaxed for compression ratios R_C = 0%, 5%, 10%, 15%, 20%, 25%, and 30% using Quantum ESPRESSO. In these relaxations the zigzag lattice constant is fixed at 3.298 Å while the armchair lattice constant and the vertical layer spacing are allowed to vary. Next, for each relaxed structure we compute the DFT band structure (also with Quantum ESPRESSO) and extract the band gap and its character (direct, indirect, or metallic by band overlap). Finally, two-probe transport devices are constructed for both the zigzag and armchair transport directions. In each device the leads are set to the highly compressed metallic phase (R_C = 30%) and the central scattering region has a length of 24 unit cells with a compression ratio equal to one of the relaxed values. Using the SIESTA code with the TranSiesta NEGF-DFT module, we compute the transmission coefficient at the Fermi level T(E_F) for each device. The method relies on standard PBE exchange‑correlation, norm-conserving pseudopotentials, and atomic-orbital basis sets for transport. By comparing the band‑gap and transmission curves at different compression ratios, we obtain a quantitative picture of how vertical pressure controls the electronic and transport properties of pure MBP.

## Reproduction target
Produce two CSV files under `/app/outputs`:

- `band_gap_vs_RC.csv`: For each compression ratio (0%, 5%, 10%, 15%, 20%, 25%, 30%), report the band gap in eV and the gap type (direct, indirect, or metallic).
- `transmission_vs_RC.csv`: For each compression ratio, report the transmission coefficient at the Fermi level for the zigzag device (T_zigzag_24L) and the armchair device (T_armchair_24L), both with a central region length of 24 unit cells.

The target is to reproduce the qualitative physical behaviour as a function of compression: how the band gap evolves from the freestanding state to high compression, and how the transmission differs between the two chiralities. The evaluation will judge whether the computed curves exhibit the correct systematic trends (e.g., changes in gap character, transition from semiconducting to metallic, distinct pressure responses in the two device orientations). Exact numerical agreement with any particular reference is not required; the focus is on obtaining physically consistent, reproducible trends.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SIESTA with TranSiesta: https://siesta-project.org/siesta/
- Pseudopotentials (PBE) for phosphorus: SSSP efficiency library or SIESTA pseudopotential repository

## Workflow steps

### Step 1: Partial relaxation of MBP under compression
- Role: process
- Action: Using Quantum ESPRESSO, relax monolayer black phosphorus unit cells with the zigzag lattice constant fixed (3.298 Å) and the armchair lattice constant and vertical layer distance allowed to relax. Generate structures for compression ratios R_C = 0%, 5%, 10%, 15%, 20%, 25%, 30%. Save the relaxed structures for subsequent steps.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Compute band gap vs compression
- Role: scored (load-bearing)
- Action: For each relaxed structure from step_relax, compute the DFT band structure using Quantum ESPRESSO. Determine the band gap (in eV) and the type (direct, indirect, or metallic by band overlap). Output the results in band_gap_vs_RC.csv.
- Output file: `/app/outputs/band_gap_vs_RC.csv`
- Format: csv
- Contract: columns: compression_ratio (int), band_gap_eV (float), gap_type (string: direct, indirect, metallic)
- Scoring: scored by hidden verifier

### Step 3: Compute transmission coefficient vs compression
- Role: scored
- Action: Using the relaxed structures, construct two-probe devices for zigzag and armchair orientations. Each device has leads at R_C=30% and a central region at the given R_C, with length equal to 24 unit cells. Compute the transmission coefficient at the Fermi level using SIESTA/TranSiesta. Write results to transmission_vs_RC.csv.
- Output file: `/app/outputs/transmission_vs_RC.csv`
- Format: csv
- Contract: columns: compression_ratio (int), T_zigzag_24L (float), T_armchair_24L (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_vs_RC.csv`
- `/app/outputs/transmission_vs_RC.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_vs_RC.csv
- path: `/app/outputs/band_gap_vs_RC.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gap values and character (direct/indirect/metallic) at each compression ratio.
- schema:
  - `type`: table
  - `required_columns`: `compression_ratio`, `band_gap_eV`, `gap_type`
  - `units`: object

### transmission_vs_RC.csv
- path: `/app/outputs/transmission_vs_RC.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Transmission coefficient at the Fermi level for zigzag and armchair devices of length 24L at each compression ratio.
- schema:
  - `type`: table
  - `required_columns`: `compression_ratio`, `T_zigzag_24L`, `T_armchair_24L`
  - `units`: object

Notes: The band gap trend must show a direct-to-indirect transition near 5% compression and metallization near 25-30% compression. The transmission curves must exhibit chirality-dependent behaviors: zigzag devices pressure-stable at low compression and increasing above 20%; armchair devices decrease then increase. Exact values are not scored; structural trends and transition thresholds are assessed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_vs_RC.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compression_ratio",
          "band_gap_eV",
          "gap_type"
        ],
        "units": {}
      },
      "description": "Band gap values and character (direct/indirect/metallic) at each compression ratio."
    },
    {
      "file": "transmission_vs_RC.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compression_ratio",
          "T_zigzag_24L",
          "T_armchair_24L"
        ],
        "units": {}
      },
      "description": "Transmission coefficient at the Fermi level for zigzag and armchair devices of length 24L at each compression ratio."
    }
  ],
  "notes": "The band gap trend must show a direct-to-indirect transition near 5% compression and metallization near 25-30% compression. The transmission curves must exhibit chirality-dependent behaviors: zigzag devices pressure-stable at low compression and increasing above 20%; armchair devices decrease then increase. Exact values are not scored; structural trends and transition thresholds are assessed."
}
```

## How you are scored
A hidden verifier independently examines each scored artifact. It checks the format and completeness of the CSV files and then evaluates the computed curves against a set of hidden structural checks derived from the paper. The checks include:
- Logical consistency: the band-gap curve and gap-type sequence must be physically plausible; for example, the gap magnitude may decrease at high compression and the character may change, possibly leading to a metallic state if the gap closes.
- Chirality‑dependent differences: the transmission curves for the zigzag and armchair devices must be distinct, possibly exhibiting different stability, monotonicity, or non‑monotonic behaviour.
- Approximate location of critical features: the verifier looks for abrupt changes in the gap type or transmission that occur near expected compression ratios, based on the underlying physics.
The final reward (0.0–1.0) is a weighted sum of the scores from each check, with the largest weight placed on the overall qualitative trends. Formatting errors or missing data lead to partial penalties. Reporting only a single number or copying the paper’s values without producing consistent curves will result in a low reward.
