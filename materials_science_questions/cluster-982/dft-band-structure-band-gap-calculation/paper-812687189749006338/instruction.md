# First-Principles Band Gap Calculation for Pb_xCd_{1-x}S Semiconductor Alloy

## Problem background
Ternary semiconductor alloys of the form Pb_xCd_{1-x}S possess a tunable electronic band gap that depends on the Pb content x, making them candidates for solar absorber layers. First-principles calculations can predict the compositional dependence of the band gap, providing insights that complement experimental measurements. This task focuses on computing the direct band gap at the Gamma point for a set of compositions using density functional theory and related techniques.

## Approach
The band gaps are obtained through a first-principles workflow that combines plane-wave density functional theory (DFT) with the HSE06 hybrid functional and spin–orbit coupling, followed by Wannierization and tight-binding interpolation. Two end-member reference calculations are performed: pristine CdS in its hexagonal (wurtzite) structure and PbS forced into the same hexagonal structure with lattice parameters extrapolated from the alloy series. The DFT wavefunctions are projected onto Wannier orbitals to construct real-space tight-binding Hamiltonians for both end members. The tight-binding parameters (on-site energies and hopping integrals) are then linearly interpolated for intermediate Pb concentrations, and the interpolated Hamiltonian is diagonalized at the Gamma point to extract the fundamental direct band gap for each composition.

## Reproduction target
Produce a single CSV file, `step_01_band_gaps.csv`, that reports the computed direct band gap at the Gamma point (in eV) for each of the five Pb_xCd_{1-x}S compositions: x = 0, 0.02, 0.05, 0.10, 0.17. The file must contain two columns, `x` and `band_gap_eV`, with one row per composition in the given order. The band gap values must be derived from the full DFT + Wannier + interpolation workflow; simply reporting literature numbers is not acceptable.

## Assets

- Plane-wave DFT code with HSE06 and spin-orbit coupling (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP or PseudoDojo): https://www.materialscloud.org/discover/sssp/
- Wannier90: http://www.wannier.org/

## Workflow steps

### Step 1: DFT reference calculation for pristine CdS
- Role: process
- Action: Perform a self-consistent DFT calculation using the HSE06 hybrid functional with spin-orbit coupling for hexagonal CdS (wurtzite structure) with experimental lattice parameters a=4.1408 Å, c=6.71346 Å and atomic positions Cd at (0,0,0) and S at (1/3,2/3,1/2). Compute wavefunctions and eigenvalues on a k-point mesh suitable for Wannierization. Save the wavefunction output.
- Evidence: `/app/outputs/cds_output.log`

### Step 2: DFT reference calculation for PbS in the same hexagonal structure
- Role: process
- Action: Perform a self-consistent DFT+HSE+SOC calculation for PbS assuming the same hexagonal crystal structure as CdS. Use lattice constants extrapolated from the paper's linear fits: a=4.364 Å, c=7.523 Å (x=1). Atomic positions: Pb at (0,0,0) and S at (1/3,2/3,1/2). Compute wavefunctions and eigenvalues on the same k-point mesh as for CdS. Save the wavefunction output.
- Evidence: `/app/outputs/pbs_output.log`

### Step 3: Wannierization and construction of tight-binding Hamiltonians
- Role: process
- Action: Using the DFT wavefunctions and eigenvalues from CdS and PbS, run Wannier90 to obtain maximally localized Wannier functions with a basis including Cd(s,p) / Pb(s,p) and S(p) orbitals. Export the tight-binding Hamiltonian matrices (on-site energies and hopping integrals) for each end member.
- Evidence: `/app/outputs/tb_hamiltonians.tar.gz`

### Step 4: Tight-binding interpolation and band gap extraction
- Role: scored (load-bearing)
- Action: For each Pb content x in [0, 0.02, 0.05, 0.10, 0.17], linearly interpolate the on-site energies and hopping integrals of CdS and PbS with weights (1-x) and x. Construct the interpolated Hamiltonian at the Γ point, diagonalize it, and compute the fundamental direct band gap (energy difference between the topmost valence band and the lowest conduction band at Γ). Write the results to a CSV file with columns x and band_gap_eV.
- Output file: `/app/outputs/step_01_band_gaps.csv`
- Format: csv
- Contract: Two columns: 'x' (float, Pb content) and 'band_gap_eV' (float, direct band gap in eV). Five rows, one per composition in the order x = 0, 0.02, 0.05, 0.10, 0.17.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_band_gaps.csv
- path: `/app/outputs/step_01_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Direct band gap at the Γ point for five Pb_xCd_{1-x}S compositions. The band_gap_eV values must be positive and strictly decreasing with increasing x.
- schema:
  - `type`: table
  - `required_columns`: `x`, `band_gap_eV`
  - `units`:
    - `x`: dimensionless (molar fraction)
    - `band_gap_eV`: eV
  - `description`: The CSV must contain exactly five rows corresponding to x=0, 0.02, 0.05, 0.10, 0.17 (in this order).

Notes: The hidden grader will compare the reported band_gap_eV values to reference theoretical values from the paper, allowing an absolute tolerance of 0.15 eV, and additionally verify that the values form a monotonically decreasing sequence. Full credit requires all values within tolerance and the monotonic trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "band_gap_eV"
        ],
        "units": {
          "x": "dimensionless (molar fraction)",
          "band_gap_eV": "eV"
        },
        "description": "The CSV must contain exactly five rows corresponding to x=0, 0.02, 0.05, 0.10, 0.17 (in this order)."
      },
      "description": "Direct band gap at the Γ point for five Pb_xCd_{1-x}S compositions. The band_gap_eV values must be positive and strictly decreasing with increasing x."
    }
  ],
  "notes": "The hidden grader will compare the reported band_gap_eV values to reference theoretical values from the paper, allowing an absolute tolerance of 0.15 eV, and additionally verify that the values form a monotonically decreasing sequence. Full credit requires all values within tolerance and the monotonic trend."
}
```

## How you are scored
Your submitted CSV file is scored by a hidden verifier that independently compares the reported band gaps to a set of reference values derived from the underlying theory, and also examines the physical self-consistency of the band gap sequence across the composition range. Additional checks verify that you have properly executed the required process steps (end-member DFT calculations and Wannierization). The final reward is a weighted combination of these criteria; merely copying numbers from a publication will not satisfy the verifier.
