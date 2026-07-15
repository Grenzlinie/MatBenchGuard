# DFT calculation of band gaps and dielectric functions for Sb_xBi_{1-x}I_3 alloys

## Problem background
Sb_xBi_{1-x}I_3 alloys are wide-band-gap materials with potential for room-temperature gamma-ray detection and non-linear optical applications. Understanding how the electronic and optical properties change with the Sb content is important for tailoring these materials. The central computational question is to determine the composition-dependent trend of the fundamental band-gap energies and the dielectric response of the pure SbI₃ end member from first-principles calculations.

## Approach
The approach combines pseudopotential plane-wave density-functional-theory (DFT) structural relaxation with full-potential linearized augmented plane wave (FPLAPW) calculations. For each alloy composition, the equilibrium lattice constants are first obtained by minimizing the total energy, using a generalized gradient approximation (GGA) for the exchange-correlation functional. From these relaxed structures, self-consistent scalar-relativistic FPLAPW calculations within GGA produce the ground-state electronic structure. The fundamental band gaps are read directly from the resulting band energies without any empirical shift. For the SbI₃ composition, the imaginary part of the transverse dielectric function is computed from the momentum matrix elements on a dense k-point mesh, and the real part is obtained via a Kramers–Kronig transformation. This workflow directly yields the quantities of interest: unshifted band gaps for the alloy series and the complete dielectric function for the pure SbI₃ compound.

## Reproduction target
Produce three scored artifacts:
1) A CSV file (`band_gaps.csv`) containing the computed unshifted band-gap energies (in eV) for the six alloy compositions x = 0.0, 0.1, 0.3, 0.5, 0.9, 1.0.
2) A CSV file (`epsilon2.csv`) with the imaginary part of the transverse dielectric function ε₂(ω) for the composition x = 1.0 (pure SbI₃), sampled over an energy range of 0–10 eV with sufficient resolution to resolve spectral features.
3) A CSV file (`epsilon1.csv`) with the corresponding real part ε₁(ω) obtained via Kramers–Kronig transformation on the same energy grid.

## Assets

- Elk (FPLAPW): https://elk.sourceforge.io/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Perform total-energy minimization for each alloy composition (x=0.0,0.1,0.3,0.5,0.9,1.0) using a pseudopotential plane-wave DFT code to obtain equilibrium lattice constants a, c and internal parameter z in the trigonal crystal symmetry. Record the relaxed parameters.
- Evidence: `/app/outputs/lattice_constants.csv`

### Step 2: FPLAPW self-consistent field calculation
- Role: process
- Action: For each composition, using the relaxed structures, run scalar-relativistic FPLAPW self-consistent calculations with a GGA functional to obtain the self-consistent potential, wavefunctions, and band energies. Save convergence information.
- Evidence: `/app/outputs/scf_convergence.json`

### Step 3: Extract unshifted band gaps
- Role: scored (load-bearing)
- Action: From the FPLAPW band structure of each composition, identify the fundamental band gap (difference between valence band maximum and conduction band minimum) without applying any shift. Write the unshifted band-gap energies to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: columns: x (float), band_gap_unshifted (float) in eV; rows for x=0.0,0.1,0.3,0.5,0.9,1.0.
- Scoring: scored by hidden verifier

### Step 4: Compute imaginary dielectric function ε₂(ω)
- Role: scored
- Action: For x=1.0, compute the imaginary part of the transverse dielectric function ε₂(ω) from the FPLAPW electronic structure using momentum matrix elements on a dense k-mesh. Write epsilon2.csv.
- Output file: `/app/outputs/epsilon2.csv`
- Format: csv
- Contract: columns: energy (float in eV), epsilon2 (float); energy range approximately 0–10 eV with sufficient resolution (≥200 points) to capture spectral features.
- Scoring: scored by hidden verifier

### Step 5: Compute real dielectric function ε₁(ω)
- Role: scored
- Action: Using ε₂(ω) from step_04, perform a Kramers‑Kronig transformation to obtain the real part ε₁(ω). Write epsilon1.csv on the same energy grid as epsilon2.csv.
- Output file: `/app/outputs/epsilon1.csv`
- Format: csv
- Contract: columns: energy (float in eV), epsilon1 (float); same energy grid as epsilon2.csv.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/epsilon2.csv`
- `/app/outputs/epsilon1.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed unshifted band-gap energies for six alloy compositions.
- schema:
  - `type`: table
  - `required_columns`: `x`, `band_gap_unshifted`
  - `units`:
    - `band_gap_unshifted`: eV

### epsilon2.csv
- path: `/app/outputs/epsilon2.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Imaginary part of the dielectric function for SbI3.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `epsilon2`
  - `units`:
    - `energy`: eV

### epsilon1.csv
- path: `/app/outputs/epsilon1.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Real part of the dielectric function for SbI3.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `epsilon1`
  - `units`:
    - `energy`: eV

Notes: The band gap checker will apply a rigid shift and compare to the reference composition-dependent trend. The dielectric function checker will compare peak positions and overall spectral shape to reference curves. Tolerances accommodate toolchain variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "band_gap_unshifted"
        ],
        "units": {
          "band_gap_unshifted": "eV"
        }
      },
      "description": "Computed unshifted band-gap energies for six alloy compositions."
    },
    {
      "file": "epsilon2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "epsilon2"
        ],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Imaginary part of the dielectric function for SbI3."
    },
    {
      "file": "epsilon1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "epsilon1"
        ],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Real part of the dielectric function for SbI3."
    }
  ],
  "notes": "The band gap checker will apply a rigid shift and compare to the reference composition-dependent trend. The dielectric function checker will compare peak positions and overall spectral shape to reference curves. Tolerances accommodate toolchain variations."
}
```

## How you are scored
A hidden verifier will independently assess each of the three output files. For `band_gaps.csv`, the verifier checks that the composition-dependent trend is consistent with a hidden reference and that a suitable rigid shift, when applied, aligns with the expected behavior. For `epsilon2.csv` and `epsilon1.csv`, the verifier compares the positions of major spectral peaks and the overall curve shape against reference dielectric spectra. Each artifact contributes a weighted score, and the final reward is the combined score over all artifacts. Simply reporting numbers from the literature is not acceptable; the artifacts must be generated by executing the described computational workflow.
