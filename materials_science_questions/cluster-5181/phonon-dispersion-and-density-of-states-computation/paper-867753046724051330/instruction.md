# Phonon frequencies and AARD for Ba2YIrO6 by DFPT

## Problem background
Ba2YIrO6 is a double perovskite iridate where the interplay of spin-orbit coupling, crystal field, and lattice degrees of freedom may stabilise exotic electronic phases. First-principles phonon frequencies are essential for interpreting Raman spectra and for understanding electron-lattice coupling in such systems. This task focuses on the computation of zone-centre phonon frequencies via density functional perturbation theory (DFPT) and the quantitative evaluation of the agreement with reference experimental Raman frequencies.

## Approach
The approach uses density functional theory (DFT) and density functional perturbation theory (DFPT) to compute phonon modes. A variable-cell DFT relaxation of the monoclinic Ba2YIrO6 structure is performed to obtain the optimal (theoretical) lattice constants. Two DFPT gamma-point phonon calculations are then carried out: one using the relaxed theoretical lattice constants, and another using the known experimental lattice constants without further relaxation. In each case, the computed phonon frequencies are collected, and their agreement with experimentally measured Raman peak frequencies is quantified by the average absolute relative difference (AARD). The calculations employ the PBE-GGA exchange-correlation functional with ultrasoft pseudopotentials and are fully re-implementable using the open-source Quantum ESPRESSO package.

## Reproduction target
Compute the DFPT gamma-point phonon frequencies of Ba2YIrO6 in the monoclinic P2_1/n structure using PBE-GGA ultrasoft pseudopotentials, a plane-wave cutoff of 30 Ry, a charge density cutoff of 350 Ry, and a 4×4×4 k-mesh. Perform a variable-cell DFT relaxation to obtain the theoretical lattice constants; then run DFPT phonon calculations separately for the theoretical lattice constants and for the experimental lattice constants (a=5.9028 Å, b=5.9029 Å, c=8.3500 Å, β=90.039°). Collect the 15 lowest-frequency Raman-active modes from each calculation, load the provided experimental reference frequencies, and compute the average absolute relative difference (AARD) for each set. Output the optimized lattice constants and a JSON object containing the two frequency lists and their corresponding AARD values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials (SSSP Efficiency PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Ba2YIrO6 monoclinic crystal structure
- Experimental Raman phonon frequencies

## Workflow steps

### Step 1: DFT geometry optimization
- Role: scored (load-bearing)
- Action: Perform variable-cell DFT relaxation of Ba2YIrO6 (monoclinic P2_1/n) using PBE ultrasoft pseudopotentials, plane-wave cutoff 30 Ry, charge density cutoff 350 Ry, and 4×4×4 k-mesh. Obtain optimized lattice constants and atomic positions. Write the optimized lattice parameters and a brief summary.
- Output file: `/app/outputs/step_01_optimized_structure.txt`
- Format: txt
- Contract: Plain text file containing the optimized lattice constants a, b, c (in Angstrom) and beta (in degrees); optionally the total energy.
- Scoring: scored by hidden verifier

### Step 2: DFPT phonon frequencies and AARD
- Role: scored (load-bearing)
- Action: Using the optimized structure from step_01, run a DFPT gamma-point phonon calculation (same pseudopotentials, cutoffs, and k-mesh) to compute frequencies for all Raman-active modes. Repeat the calculation using the experimental lattice constants (a=5.9028 Å, b=5.9029 Å, c=8.3500 Å, beta=90.039°) without structural relaxation. Collect the 15 lowest-frequency modes (or those corresponding to Raman-active symmetries) for each set. Load the experimental reference frequencies from experimental_frequencies.csv and compute the average absolute relative difference (AARD) for each set. Output all data as a JSON.
- Output file: `/app/outputs/step_02_phonon_frequencies.json`
- Format: json
- Contract: JSON object with keys: 'theoretical_lattice_constants_frequencies' (list of 15 floats), 'experimental_lattice_constants_frequencies' (list of 15 floats), 'aard_theoretical' (float), 'aard_experimental' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_optimized_structure.txt`
- `/app/outputs/step_02_phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_optimized_structure.txt
- path: `/app/outputs/step_01_optimized_structure.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Optimized crystal structure parameters from DFT relaxation; checked against reference theoretical lattice constants within a tolerance.
- schema:
  - `type`: text
  - `description`: Optimized lattice constants a, b, c (Angstrom) and beta (degrees).

### step_02_phonon_frequencies.json
- path: `/app/outputs/step_02_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: DFPT phonon frequencies and the resulting AARD values computed against the provided experimental reference frequencies.
- schema:
  - `type`: object
  - `required`: `theoretical_lattice_constants_frequencies`, `experimental_lattice_constants_frequencies`, `aard_theoretical`, `aard_experimental`
  - `properties`:
    - `theoretical_lattice_constants_frequencies`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 15
      - `maxItems`: 15
    - `experimental_lattice_constants_frequencies`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 15
      - `maxItems`: 15
    - `aard_theoretical`:
      - `type`: number
    - `aard_experimental`:
      - `type`: number

Notes: The first step scores the optimized lattice constants against the paper's theoretical values. The second step scores the recomputed AARD: the checker extracts the frequency lists, recomputes AARD versus hidden gold experimental frequencies, and compares each AARD to a corresponding hidden threshold. Frequencies are also validated to be positive and within a reasonable range.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_optimized_structure.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Optimized lattice constants a, b, c (Angstrom) and beta (degrees)."
      },
      "description": "Optimized crystal structure parameters from DFT relaxation; checked against reference theoretical lattice constants within a tolerance."
    },
    {
      "file": "step_02_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "theoretical_lattice_constants_frequencies",
          "experimental_lattice_constants_frequencies",
          "aard_theoretical",
          "aard_experimental"
        ],
        "properties": {
          "theoretical_lattice_constants_frequencies": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 15,
            "maxItems": 15
          },
          "experimental_lattice_constants_frequencies": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 15,
            "maxItems": 15
          },
          "aard_theoretical": {
            "type": "number"
          },
          "aard_experimental": {
            "type": "number"
          }
        }
      },
      "description": "DFPT phonon frequencies and the resulting AARD values computed against the provided experimental reference frequencies."
    }
  ],
  "notes": "The first step scores the optimized lattice constants against the paper's theoretical values. The second step scores the recomputed AARD: the checker extracts the frequency lists, recomputes AARD versus hidden gold experimental frequencies, and compares each AARD to a corresponding hidden threshold. Frequencies are also validated to be positive and within a reasonable range."
}
```

## How you are scored
A hidden verifier independently checks each stage's artifact. For the geometry optimization step (Step 1), the verifier examines the submitted optimized lattice constants and confirms they are physically reasonable and within expected bounds. For the phonon frequency step (Step 2), the verifier extracts the two frequency lists, recomputes the AARD against the hidden reference experimental frequencies, and assigns a score based on the resulting AARD values. The overall reward is a weighted combination of the scores from both stages. Reporting numbers is not sufficient—the artifacts must be produced through the computational protocol described in the workflow steps.
