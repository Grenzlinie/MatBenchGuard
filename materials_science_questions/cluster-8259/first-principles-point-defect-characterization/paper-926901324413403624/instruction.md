# First-principles band structure of CrOCl/NbSe₂ heterostructure with and without Cr vacancies

## Problem background
Van der Waals heterostructures that combine an antiferromagnetic insulator with an s-wave superconductor offer a route to engineering unconventional superconducting states. In a CrOCl/NbSe₂ heterostructure, monolayer CrOCl is an antiferromagnetic insulator with a large band gap, while NbSe₂ is a metallic superconductor. When these two materials are stacked, charge transfer and the superconducting proximity effect may occur if the electronic bands of CrOCl align with the Fermi level of NbSe₂. A key open question is what role structural defects — specifically Cr vacancies — play in enabling this band alignment. This task reproduces the first-principles analysis addressing that question: by computing the electronic band structure of the heterostructure both without and with specifically arranged Cr vacancies, one can determine whether the CrOCl valence bands shift to overlap the NbSe₂ Fermi level, a prerequisite for proximitized superconductivity.

## Approach
Construct slab supercell models of a monolayer CrOCl placed on a few-layer NbSe₂ substrate. The orthorhombic CrOCl and hexagonal 2H-NbSe₂ crystal structures are used to build the heterostructure with a suitable supercell matching. Prepare two configurations: (i) a pristine heterostructure with no intentional defects, and (ii) a defective heterostructure in which two Cr atoms are removed, selecting one Cr from each of the two antiferromagnetic sublattices so that the net antiferromagnetic order is preserved. For each configuration, perform first-principles density functional theory (DFT) calculations using a generalized gradient approximation (GGA) functional and standard pseudopotentials. Carry out a self-consistent field (SCF) calculation to obtain the ground state charge density, followed by a non-self-consistent band structure calculation along a high-symmetry k-path that samples the Brillouin zone. Extract the Kohn-Sham eigenvalues and shift the energy scale so that the Fermi level of the metallic NbSe₂ subsystem is set to 0 eV. From the resulting band energies, isolate the band(s) of CrOCl character near the Fermi level to determine their energy position.

## Reproduction target
Compute, for both the pristine and the two-Cr-vacancy heterostructures, the energy gap between the highest occupied CrOCl-derived valence band and the Fermi level (0 eV). Report the raw band energies in CSV format for auditing, and produce a JSON summary containing two gap values (in eV) and a boolean flag that indicates whether, in the defective case, the CrOCl valence bands cross the Fermi level (i.e., the gap is ≤ 0 eV). The target is to determine whether the introduction of the described Cr vacancies causes the CrOCl valence bands to overlap the NbSe₂ Fermi level, thereby enabling charge transfer.

## Assets

- Crystal structure of CrOCl
- Crystal structure of 2H-NbSe₂
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Build pristine and defective slab models
- Role: process
- Action: Construct slab supercell models of monolayer CrOCl on a few-layer NbSe₂ substrate. Build two configurations: (i) pristine heterostructure; (ii) heterostructure with two Cr vacancies, removing one Cr atom from each of the two antiferromagnetic sublattices to preserve AFM order. Generate Quantum ESPRESSO input files (structure + k-path) for band structure calculations.
- Evidence: `/app/outputs/slab_model_files.txt`

### Step 2: Run DFT band structure calculations
- Role: process
- Action: Run DFT self-consistent field (SCF) calculations followed by non-self-consistent band structure calculations using Quantum ESPRESSO (pw.x, bands.x) on both pristine and defective slab models. Use a suitable functional (GGA) and pseudopotentials. Collect the band energies along a high-symmetry k-path.
- Evidence: `/app/outputs/dft_output.log`

### Step 3: Extract band structures to CSV
- Role: scored
- Action: Parse the DFT output (bands.dat or equivalent) and write the band energies to step_01_band_structures.csv. Include rows for both pristine and defective systems, with Fermi level shifted to 0 eV.
- Output file: `/app/outputs/step_01_band_structures.csv`
- Format: csv
- Contract: CSV file with header: system,k_path_index,band_index,energy (eV). The 'system' column contains 'pristine' or 'defective'. All energies are in eV relative to the Fermi level set to 0.
- Scoring: scored by hidden verifier

### Step 4: Analyze band overlap
- Role: scored (load-bearing)
- Action: Using the extracted band data or direct DFT output, determine the energy gap between the highest occupied CrOCl valence band and the Fermi level (0 eV) for both pristine and defective systems. Compute the overlap condition (true if defective gap ≤ 0). Write results to step_02_overlap_analysis.json.
- Output file: `/app/outputs/step_02_overlap_analysis.json`
- Format: json
- Contract: JSON object with keys: pristine_gap (float, in eV), defective_gap (float, in eV), overlap (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_structures.csv`
- `/app/outputs/step_02_overlap_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_structures.csv
- path: `/app/outputs/step_01_band_structures.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band energies along a high-symmetry k-path for pristine and defective CrOCl/NbSe₂ heterostructures. Columns: system (pristine or defective), k_path_index (integer), band_index (integer), energy (eV, relative to Fermi level). The CSV provides the raw data for structural audit (approximate energy range, band count, and consistency with the overlap analysis).
- schema:
  - `type`: table
  - `required_columns`: `system`, `k_path_index`, `band_index`, `energy`
  - `units`:
    - `energy`: eV

### step_02_overlap_analysis.json
- path: `/app/outputs/step_02_overlap_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Analysis of band overlap with the NbSe₂ Fermi level. Pristine gap (positive indicates insulating CrOCl), defective gap (non-positive indicates CrOCl valence bands cross the Fermi level), and a boolean overlap flag that is true only for the defective case.
- schema:
  - `type`: object
  - `required`:
    - `pristine_gap`: float (eV)
    - `defective_gap`: float (eV)
    - `overlap`: boolean

Notes: This task reproduces only the DFT band-structure subresult (Cr vacancies causing CrOCl valence bands to overlap NbSe₂ EF). The scoring is structural: the verifier checks that pristine_gap > 0, defective_gap ≤ 0, and the overlap boolean is consistent. The band structure CSV is audited for basic shape and energy range. No absolute numeric targets from the paper are used; the acceptable tolerance on the gap zero crossing is ±0.1 eV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_structures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "k_path_index",
          "band_index",
          "energy"
        ],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Band energies along a high-symmetry k-path for pristine and defective CrOCl/NbSe₂ heterostructures. Columns: system (pristine or defective), k_path_index (integer), band_index (integer), energy (eV, relative to Fermi level). The CSV provides the raw data for structural audit (approximate energy range, band count, and consistency with the overlap analysis)."
    },
    {
      "file": "step_02_overlap_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "pristine_gap": "float (eV)",
          "defective_gap": "float (eV)",
          "overlap": "boolean"
        }
      },
      "description": "Analysis of band overlap with the NbSe₂ Fermi level. Pristine gap (positive indicates insulating CrOCl), defective gap (non-positive indicates CrOCl valence bands cross the Fermi level), and a boolean overlap flag that is true only for the defective case."
    }
  ],
  "notes": "This task reproduces only the DFT band-structure subresult (Cr vacancies causing CrOCl valence bands to overlap NbSe₂ EF). The scoring is structural: the verifier checks that pristine_gap > 0, defective_gap ≤ 0, and the overlap boolean is consistent. The band structure CSV is audited for basic shape and energy range. No absolute numeric targets from the paper are used; the acceptable tolerance on the gap zero crossing is ±0.1 eV."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier. Two output files are scored: the band structure CSV (`step_01_band_structures.csv`) and the overlap analysis JSON (`step_02_overlap_analysis.json`). The verifier reads both files and checks them against hidden references derived from the paper's findings. The CSV is audited for structural consistency (expected columns, plausible energy ranges, and internal agreement with the JSON summary). The JSON is scored primarily on the agreement of the computed gaps and the overlap flag with the known physical trend — the pristine system should exhibit a positive gap, while the defective system should yield a non-positive gap — with a small tolerance to accommodate numerical differences between DFT implementations. Each scored artifact carries a weight, and the final reward is the weighted sum. Merely reporting numbers without executing the required DFT calculations is not sufficient; the verifier checks that the submitted data are consistent with a genuine computation.
