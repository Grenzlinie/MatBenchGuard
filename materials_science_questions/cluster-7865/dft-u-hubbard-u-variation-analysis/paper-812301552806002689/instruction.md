# Spin-Polarized Molecular Orbital LDA Calculations on Hydrogen Clusters

## Problem background
Conventional local-density approximation (LDA) band‑structure calculations for layered cuprates yield a metallic state, in contradiction to the experimentally observed antiferromagnetic (AF) insulating ground state. The origin of this discrepancy is not fully understood. One hypothesis is that the failure arises from the use of delocalised basis functions rather than from the LDA functional itself. To test this idea, this work investigates whether a molecular orbital method employing localised atomic orbitals can produce an antiferromagnetic state within the conventional LDA. The target system consists of three hydrogen clusters (H₂, H₈, H₁₈) with deliberately large interatomic separations, which provide a simple model with one electron per atom – analogous to the half‑filled d‑band situation in cuprates. The task is to compute, from first principles, the average magnetic moment per hydrogen atom and the HOMO–LUMO energy gaps for these clusters under both spin‑unpolarised and spin‑polarised treatments.

## Approach
Carry out spin‑polarised molecular orbital calculations within the LDA using Slater’s Xα exchange‑correlation potential with α = 0.7. The basis set consists of numerically generated hydrogen 1s atomic orbitals that are obtained by solving the radial Schrödinger equation with an additional confining well potential (radius = 0.8 × a_H, depth = –2.0 a.u.). Matrix elements of the Hamiltonian and overlap are evaluated by diophantine numerical integration using 500 sampling points per hydrogen atom. Three hydrogen clusters are studied, all defined with a lattice parameter a_H = 0.126 nm: H₂ (atoms at (±a_H, 0, 0)), H₈ (atoms at (±a_H, ±a_H, ±1.25 a_H)), and H₁₈ (atoms at (b, b′, c) where b,b′ = ±2a_H, 0 and c = ±1.25 a_H). For each cluster, a spin‑unpolarised run yields the HOMO–LUMO gap. Then, starting from a broken‑symmetry initial spin arrangement, a spin‑polarised run yields the average magnetic moment per hydrogen atom (in μB) and the corresponding HOMO–LUMO gap. All six magnetic moments and six gaps are recorded for comparison between the spin treatments.

## Reproduction target
Implement the computational protocol described above and write all results to a single JSON file at /app/outputs/results.json. The JSON object must contain exactly these numeric fields, with the specified units:

- H2_magnetic_moment, H8_magnetic_moment, H18_magnetic_moment (μB)
- H2_gap_spin_unpolarized, H8_gap_spin_unpolarized, H18_gap_spin_unpolarized (eV)
- H2_gap_spin_polarized, H8_gap_spin_polarized, H18_gap_spin_polarized (eV)

The file must strictly follow this schema; no additional fields or deviations are permitted. The values are to be obtained by faithfully executing the workflow steps, not by any other means.

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate numerical atomic basis functions
- Role: process
- Action: Solve the radial Schrödinger equation for hydrogen 1s orbitals with a confining well potential (radius = 0.8 × a_H, depth = -2.0 a.u.) to produce tabulated radial functions that cover the cluster region.
- Evidence: `/app/outputs/basis_H_1s.npy`

### Step 2: Define cluster geometries
- Role: process
- Action: Create Cartesian coordinate arrays for H₂ (atoms at (±a_H,0,0)), H₈ (atoms at (±a_H,±a_H,±1.25a_H)), and H₁₈ (atoms at (b_H,b'_H,c_H) where b_H,b'_H = ±2a_H,0 and c_H = ±1.25a_H) with a_H = 0.126 nm.
- Evidence: `/app/outputs/coordinates.txt`

### Step 3: Perform MO-LDA calculations and collect results
- Role: scored (load-bearing)
- Action: For each cluster (H₂, H₈, H₁₈): (1) Run a spin-unpolarized molecular orbital LDA calculation (Xα, α=0.7) using the generated basis functions and diophantine integration with 500 sampling points per atom. Compute the HOMO-LUMO energy gap. (2) Run a spin-polarized calculation starting from a broken-symmetry spin configuration. Compute the average magnetic moment per hydrogen atom and the HOMO-LUMO gap. Write all six magnetic moments and six gaps to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with exactly these numeric fields: H2_magnetic_moment, H8_magnetic_moment, H18_magnetic_moment (units: μB); H2_gap_spin_unpolarized, H8_gap_spin_unpolarized, H18_gap_spin_unpolarized, H2_gap_spin_polarized, H8_gap_spin_polarized, H18_gap_spin_polarized (units: eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the averaged magnetic moments and HOMO-LUMO energy gaps for H2, H8, and H18 hydrogen clusters computed with spin-polarized and spin-unpolarized molecular orbital LDA.
- schema:
  - `type`: object
  - `required`: `H2_magnetic_moment`, `H8_magnetic_moment`, `H18_magnetic_moment`, `H2_gap_spin_unpolarized`, `H8_gap_spin_unpolarized`, `H18_gap_spin_unpolarized`, `H2_gap_spin_polarized`, `H8_gap_spin_polarized`, `H18_gap_spin_polarized`
  - `properties`:
    - `H2_magnetic_moment`:
      - `type`: number
      - `unit`: μB
    - `H8_magnetic_moment`:
      - `type`: number
      - `unit`: μB
    - `H18_magnetic_moment`:
      - `type`: number
      - `unit`: μB
    - `H2_gap_spin_unpolarized`:
      - `type`: number
      - `unit`: eV
    - `H8_gap_spin_unpolarized`:
      - `type`: number
      - `unit`: eV
    - `H18_gap_spin_unpolarized`:
      - `type`: number
      - `unit`: eV
    - `H2_gap_spin_polarized`:
      - `type`: number
      - `unit`: eV
    - `H8_gap_spin_polarized`:
      - `type`: number
      - `unit`: eV
    - `H18_gap_spin_polarized`:
      - `type`: number
      - `unit`: eV

Notes: All values are determined by the computational procedure; tolerances for comparison will be applied in the hidden grading to account for implementation and numerical integration differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "H2_magnetic_moment",
          "H8_magnetic_moment",
          "H18_magnetic_moment",
          "H2_gap_spin_unpolarized",
          "H8_gap_spin_unpolarized",
          "H18_gap_spin_unpolarized",
          "H2_gap_spin_polarized",
          "H8_gap_spin_polarized",
          "H18_gap_spin_polarized"
        ],
        "properties": {
          "H2_magnetic_moment": {
            "type": "number",
            "unit": "μB"
          },
          "H8_magnetic_moment": {
            "type": "number",
            "unit": "μB"
          },
          "H18_magnetic_moment": {
            "type": "number",
            "unit": "μB"
          },
          "H2_gap_spin_unpolarized": {
            "type": "number",
            "unit": "eV"
          },
          "H8_gap_spin_unpolarized": {
            "type": "number",
            "unit": "eV"
          },
          "H18_gap_spin_unpolarized": {
            "type": "number",
            "unit": "eV"
          },
          "H2_gap_spin_polarized": {
            "type": "number",
            "unit": "eV"
          },
          "H8_gap_spin_polarized": {
            "type": "number",
            "unit": "eV"
          },
          "H18_gap_spin_polarized": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Contains the averaged magnetic moments and HOMO-LUMO energy gaps for H2, H8, and H18 hydrogen clusters computed with spin-polarized and spin-unpolarized molecular orbital LDA."
    }
  ],
  "notes": "All values are determined by the computational procedure; tolerances for comparison will be applied in the hidden grading to account for implementation and numerical integration differences."
}
```

## How you are scored
A hidden verifier will read /app/outputs/results.json and compare each of the nine numerical fields against a reference value (the paper‑reported result for the same quantity) within a predetermined tolerance. Each field that falls within its tolerance band earns partial credit. The total reward, a float between 0 and 1, is the weighted sum of these per‑field credits. The scoring does not reward approximate guesses; it requires that the numbers originate from a correct implementation of the specified molecular‑orbital LDA procedure. No part of the hidden gold or tolerances is given to you; compute the values from first principles as described in the workflow steps.
