# DFT Benchmark: Ground-State Geometries and Harmonic Frequencies of Small Silicon Nitride Clusters

## Problem background
Small silicon nitride clusters (SiₙNₘ) are the building blocks of bulk silicon nitride materials, which possess exceptional mechanical, thermal, and dielectric properties. Understanding the structure and bonding of these clusters is important for applications ranging from thin‑film deposition to astrophysics. A theoretical benchmark is needed to identify a computational method that accurately predicts the equilibrium geometries and harmonic vibrational frequencies of the simplest clusters, SiN, SiN₂, and Si₂N. The present task reproduces the ground‑state benchmarking at the selected level of theory, B3LYP/6‑311G(d), to verify its accuracy for these clusters.

## Approach
The approach uses density functional theory (DFT) with the hybrid B3LYP exchange‑correlation functional and the 6‑311G(d) basis set. For each of the three benchmark clusters—the diatomic SiN (doublet, linear), the triatomic SiN₂ (asymmetric linear SiNN, triplet), and the triatomic Si₂N (symmetric linear SiNSi, doublet)—a geometry optimization is performed to obtain the equilibrium geometry, followed by a harmonic frequency calculation at the same level. The extracted bond lengths (Si–N and N–N) and vibrational frequencies (in cm⁻¹) constitute the benchmark results.

## Reproduction target
The target is to compute the equilibrium bond distances (Si–N and N–N, in Å) and the full set of harmonic vibrational frequencies (in cm⁻¹) for SiN, SiN₂, and Si₂N at the B3LYP/6‑311G(d) level. The results must be compiled into a CSV file (`benchmark_summary.csv`) with columns `system`, `r_SiN`, `r_NN`, `freq1`, `freq2`, `freq3`. The raw geometry files (XYZ) and frequency files for each cluster must also be saved. The verifier will compare the computed values against hidden reference data.

## Assets

- ORCA quantum chemistry software: https://orcaforum.kofo.mpg.de/
- 6‑311G(d) basis set: ORCA

## Workflow steps

### Step 1: Optimize ground‑state geometry of SiN
- Role: scored
- Action: Construct an initial linear SiN molecule (doublet, Si–N separation ~1.6 Å) and perform a DFT geometry optimization at the B3LYP/6‑311G(d) level using an open‑source quantum‑chemistry package. Save the final Cartesian coordinates (in Angstrom) as a standard XYZ file.
- Output file: `/app/outputs/sin_optimized.xyz`
- Format: other
- Contract: Standard XYZ format: first line – number of atoms; second line – comment; following lines – element, x, y, z (in Å) for each atom. The file contains two atoms: Si and N.
- Scoring: scored by hidden verifier

### Step 2: Compute harmonic vibrational frequencies of SiN
- Role: scored
- Action: Using the optimized SiN geometry, perform a harmonic frequency calculation at the B3LYP/6‑311G(d) level. Write all real harmonic frequencies (in cm⁻¹, one per line, in ascending order) to a plain‑text file.
- Output file: `/app/outputs/sin_frequencies.txt`
- Format: txt
- Contract: One frequency (cm⁻¹) per line, sorted in ascending order. The diatomic molecule has exactly one vibrational mode.
- Scoring: scored by hidden verifier

### Step 3: Optimize ground‑state geometry of SiN₂
- Role: scored
- Action: Construct an initial asymmetric linear Si–N–N molecule (triplet) with bond lengths ~1.8 Å (Si–N) and ~1.15 Å (N–N) and optimize at the B3LYP/6‑311G(d) level. Save the final atomic coordinates as a standard XYZ file.
- Output file: `/app/outputs/sin2_optimized.xyz`
- Format: other
- Contract: Standard XYZ format: first line – number of atoms (3); second line – comment; following lines – element, x, y, z (in Å). Atoms: Si, N, N (in the order Si–N–N).
- Scoring: scored by hidden verifier

### Step 4: Compute harmonic vibrational frequencies of SiN₂
- Role: scored
- Action: Perform a harmonic frequency calculation on the optimized SiN₂ geometry at the B3LYP/6‑311G(d) level. Write all real frequencies (cm⁻¹, one per line, ascending) to a text file.
- Output file: `/app/outputs/sin2_frequencies.txt`
- Format: txt
- Contract: One frequency (cm⁻¹) per line, in ascending order; exactly three lines.
- Scoring: scored by hidden verifier

### Step 5: Optimize ground‑state geometry of Si₂N
- Role: scored
- Action: Construct an initial symmetric linear Si–N–Si molecule (doublet, Si–N ~1.64 Å) and optimize at the B3LYP/6‑311G(d) level. Save the final coordinates as a standard XYZ file.
- Output file: `/app/outputs/si2n_optimized.xyz`
- Format: other
- Contract: Standard XYZ format: first line – number of atoms (3); second line – comment; following lines – element, x, y, z (in Å). Atoms: Si, N, Si.
- Scoring: scored by hidden verifier

### Step 6: Compute harmonic vibrational frequencies of Si₂N
- Role: scored
- Action: Perform a harmonic frequency calculation on the optimized Si₂N geometry at the B3LYP/6‑311G(d) level. Write all real frequencies (cm⁻¹, one per line, ascending) to a text file.
- Output file: `/app/outputs/si2n_frequencies.txt`
- Format: txt
- Contract: One frequency (cm⁻¹) per line, in ascending order; exactly three lines.
- Scoring: scored by hidden verifier

### Step 7: Compile benchmark summary CSV
- Role: scored (load-bearing)
- Action: From the three optimized XYZ files, extract the equilibrium bond distances: Si–N for SiN; N–N and Si–N for SiN₂; Si–N for Si₂N. From the three frequency files, extract all harmonic frequencies. Compile a CSV file with the following columns: system (string), r_SiN (float, Å, null if not applicable), r_NN (float, Å, null if not applicable), freq1 (float, cm⁻¹), freq2 (float, cm⁻¹, null if not present), freq3 (float, cm⁻¹, null if not present). Frequencies must be listed in ascending order.
- Output file: `/app/outputs/benchmark_summary.csv`
- Format: csv
- Contract: CSV with header: system, r_SiN, r_NN, freq1, freq2, freq3. r_SiN and r_NN are bond lengths in Å (null if not applicable). freq1, freq2, freq3 are harmonic frequencies in cm⁻¹ in ascending order (null if not present). The CSV must contain one row per system (SiN, SiN2, Si2N) with the corresponding computed values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sin_optimized.xyz`
- `/app/outputs/sin_frequencies.txt`
- `/app/outputs/sin2_optimized.xyz`
- `/app/outputs/sin2_frequencies.txt`
- `/app/outputs/si2n_optimized.xyz`
- `/app/outputs/si2n_frequencies.txt`
- `/app/outputs/benchmark_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sin_optimized.xyz
- path: `/app/outputs/sin_optimized.xyz`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: The checker parses this file to extract the Si–N bond length (in Å) and compares it to the hidden reference value within tolerances.
- schema:
  - `type`: other
  - `description`: Standard XYZ file; see step output_schema.

### sin_frequencies.txt
- path: `/app/outputs/sin_frequencies.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: The checker reads all frequencies and compares them to the hidden reference frequencies within tolerances.
- schema:
  - `type`: text
  - `description`: One frequency per line; see step output_schema.

### sin2_optimized.xyz
- path: `/app/outputs/sin2_optimized.xyz`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: The checker extracts the Si–N and N–N bond distances and compares them to the hidden reference values.
- schema:
  - `type`: other
  - `description`: Standard XYZ file; see step output_schema.

### sin2_frequencies.txt
- path: `/app/outputs/sin2_frequencies.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: The checker compares the reported frequencies to the hidden reference values.
- schema:
  - `type`: text
  - `description`: Three frequencies; see step output_schema.

### si2n_optimized.xyz
- path: `/app/outputs/si2n_optimized.xyz`
- format: other
- purpose: scored
- target_policy: metric_recompute
- description: The checker extracts the Si–N bond distance and compares it to the hidden reference value.
- schema:
  - `type`: other
  - `description`: Standard XYZ file; see step output_schema.

### si2n_frequencies.txt
- path: `/app/outputs/si2n_frequencies.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: The checker compares the reported frequencies to the hidden reference values.
- schema:
  - `type`: text
  - `description`: Three frequencies; see step output_schema.

### benchmark_summary.csv
- path: `/app/outputs/benchmark_summary.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The checker verifies internal consistency (CSV values match those extracted from the raw XYZ/txt files) and then compares the reported bond lengths and frequencies to the paper’s hidden reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `system`, `r_SiN`, `r_NN`, `freq1`, `freq2`, `freq3`
  - `units`:
    - `r_SiN`: Å
    - `r_NN`: Å
    - `freq1`: cm⁻¹
    - `freq2`: cm⁻¹
    - `freq3`: cm⁻¹

Notes: The solver must use an open‑source quantum‑chemistry package (ORCA, Psi4, PySCF …). All geometries are standard linear isomers as described. The hidden checker does NOT require exact reproduction of the paper’s output; tolerances account for typical implementation‑induced variations in DFT results (~±0.01 Å for bond lengths, ~±15 cm⁻¹ for frequencies).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sin_optimized.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "other",
        "description": "Standard XYZ file; see step output_schema."
      },
      "description": "The checker parses this file to extract the Si–N bond length (in Å) and compares it to the hidden reference value within tolerances."
    },
    {
      "file": "sin_frequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "One frequency per line; see step output_schema."
      },
      "description": "The checker reads all frequencies and compares them to the hidden reference frequencies within tolerances."
    },
    {
      "file": "sin2_optimized.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "other",
        "description": "Standard XYZ file; see step output_schema."
      },
      "description": "The checker extracts the Si–N and N–N bond distances and compares them to the hidden reference values."
    },
    {
      "file": "sin2_frequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Three frequencies; see step output_schema."
      },
      "description": "The checker compares the reported frequencies to the hidden reference values."
    },
    {
      "file": "si2n_optimized.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "other",
        "description": "Standard XYZ file; see step output_schema."
      },
      "description": "The checker extracts the Si–N bond distance and compares it to the hidden reference value."
    },
    {
      "file": "si2n_frequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "description": "Three frequencies; see step output_schema."
      },
      "description": "The checker compares the reported frequencies to the hidden reference values."
    },
    {
      "file": "benchmark_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "r_SiN",
          "r_NN",
          "freq1",
          "freq2",
          "freq3"
        ],
        "units": {
          "r_SiN": "Å",
          "r_NN": "Å",
          "freq1": "cm⁻¹",
          "freq2": "cm⁻¹",
          "freq3": "cm⁻¹"
        }
      },
      "description": "The checker verifies internal consistency (CSV values match those extracted from the raw XYZ/txt files) and then compares the reported bond lengths and frequencies to the paper’s hidden reference values within tolerances."
    }
  ],
  "notes": "The solver must use an open‑source quantum‑chemistry package (ORCA, Psi4, PySCF …). All geometries are standard linear isomers as described. The hidden checker does NOT require exact reproduction of the paper’s output; tolerances account for typical implementation‑induced variations in DFT results (~±0.01 Å for bond lengths, ~±15 cm⁻¹ for frequencies)."
}
```

## How you are scored
Your submission is scored by a hidden verifier. For each workflow stage, the verifier reads the required output files, recomputes the physical quantities (bond distances, frequencies), verifies the consistency between the summary CSV and the raw geometry and frequency files, and then compares your computed values against hidden reference values with appropriate tolerances. The final score is a weighted combination of the scores for all stages, reflecting the fraction of compared quantities that fall within tolerance. Full credit is given when the computed values meet or exceed the reference accuracy.
