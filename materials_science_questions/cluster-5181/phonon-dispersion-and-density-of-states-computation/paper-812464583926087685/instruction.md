# Phonon dispersion computation for A3C60 fullerides

## Problem background
Alkali-metal-doped fullerene A3C60 crystallizes in the Fm-3m structure with one C60 molecule and three A+ cations per primitive cell. Understanding the low-energy external (phonon) vibrations of these materials is important for interpreting their physical properties, including superconductivity. Because the C60 balls are large and the material is metallic with strong electron screening, the interactions between ions are short ranged. This allows a force-constant matrix approach to be used, where each C60 molecule is treated as a rigid unit with both translational and librational degrees of freedom, while the alkali cations have only translational degrees of freedom. The task is to compute the resulting phonon dispersion curves along the principal symmetry directions of the Brillouin zone, using the symmetry-constrained force-constant matrices and numerical parameters given in the literature.

## Approach
The method assembles a 15×15 dynamical matrix for the primitive cell, incorporating three translational degrees of freedom for each of the four ions (one C60 and three A+) plus three librational degrees of freedom for the C60 molecule. The real-space force-constant matrices Φ between relevant ion pairs are constructed using the explicit algebraic forms derived from the space-group symmetries of Fm-3m and the short-range nature of the interactions. These forms contain a set of free parameters (α1, β1, γ1, δ1, α2, β2, α3, β3, α4, β4, α, β, γ, a, b, c, p, q), and numerical values are provided for them together with the masses and moment of inertia. The mass matrix is set to a diagonal form with appropriate mass and inertia values (conveniently chosen as 1 in scaled units, with the force-constant parameters scaled accordingly, as frequencies are reported in dimensionless units). The dynamical matrix D(q) = m^{-1/2} D0(q) m^{-1/2} is constructed for each wavevector q along the Δ, Σ, and Λ directions by performing a Fourier transform of the real-space force-constant matrices. Diagonalization yields the squared frequencies ω²; taking the positive square root gives the phonon frequencies in units of (α1/m_A)^{1/2}.

## Reproduction target
Produce the complete set of phonon frequencies for all 15 branches at 21 equidistant q-points (q from 0 to 1 in steps of 0.05) along each of the three high-symmetry directions: Δ (x,0,0), Σ (x,x,0), and Λ (x,x,x). Output the results as a CSV file with columns direction, q_red, branch (0 to 14 sorted by increasing frequency at each q), and frequency (in dimensionless units). The CSV must contain exactly 945 data rows.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Set up crystal structure, mass matrix, and force-constant matrices
- Role: process
- Action: Define the primitive cell of A3C60 (space group Fm-3m) with one C60 molecule at the origin and three A+ cations at the tetrahedral and octahedral sites. Assign three translational degrees of freedom to each ion and three additional librational degrees of freedom to the C60 molecule, giving 15 DOF total. Build the mass matrix m^cryst as a diagonal matrix with suitable mass and moment of inertia values (conveniently set to 1 in scaled units). Using the explicit symmetry-constrained force-constant matrix forms Φ(12), Φ(13), Φ(14), Φ(34), Φ(44) from the paper, plug in the numerical parameter values (α1/mA=1, β1/mA=0.2, γ1/mA=0.15, δ1/mA=0.1, α2/mA=1.2, β2/mA=1.1, α3/√(mAM)=0.6, β3/√(mAM)=0.5, α4/√(mAM)=0.4, β4/√(mAM)=0.05, α/M=0.15, β/M=0.02, γ/M=0.11, a/I0=0.09, b/I0=0.01, c/I0=0.06, p/√(MI0)=0.03, q/√(MI0)=0.01) after appropriate scaling to the chosen masses and moment of inertia. Assemble the real-space force-constant blocks for all required ion pairs.
- Evidence: `/app/outputs/fc_matrices.json`

### Step 2: Compute phonon dispersion frequencies
- Role: scored (load-bearing)
- Action: For each of the three symmetry directions Δ: (x,0,0), Σ: (x,x,0), Λ: (x,x,x) with x = 0, 0.05, 0.10, ..., 1.0 (21 points each), construct the 15×15 dynamical matrix D(q) = m^cryst^{-1/2} D0(q) m^cryst^{-1/2}, where D0(q) is the Fourier transform of the real-space force-constant matrices from the previous step. Diagonalize D(q) to obtain squared frequencies ω²; take the positive square root to yield ω in units of (α₁/m_A)^{1/2}. Sort the 15 eigenvalues in ascending order for each q. Write the results to a CSV file.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: CSV file with header: direction, q_red, branch, frequency. direction is one of 'Delta', 'Sigma', 'Lambda'. q_red is a float in [0.0, 1.0] in steps of 0.05. branch is an integer from 0 to 14, sorted ascending by eigenvalue at that q. frequency is a float in units of (alpha₁/m_A)^{1/2}. Exactly 3 × 21 × 15 = 945 data rows, not including header.
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
- target_policy: exact_match
- description: File containing the computed phonon frequencies for all branches and q-points. The hidden checker recomputes the frequencies from the same force-constant matrices and compares each value with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `q_red`, `branch`, `frequency`
  - `units`:
    - `frequency`: (alpha₁/m_A)^{1/2}

Notes: The agent must set m_A, M, I0 to convenient values (e.g., 1) and scale the parameters accordingly, because frequencies are reported in dimensionless units. The scientific correctness depends on correctly implementing the force-constant matrices and the Brillouin-zone Fourier transform, not on the absolute mass choice.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "q_red",
          "branch",
          "frequency"
        ],
        "units": {
          "frequency": "(alpha₁/m_A)^{1/2}"
        }
      },
      "description": "File containing the computed phonon frequencies for all branches and q-points. The hidden checker recomputes the frequencies from the same force-constant matrices and compares each value with an absolute tolerance."
    }
  ],
  "notes": "The agent must set m_A, M, I0 to convenient values (e.g., 1) and scale the parameters accordingly, because frequencies are reported in dimensionless units. The scientific correctness depends on correctly implementing the force-constant matrices and the Brillouin-zone Fourier transform, not on the absolute mass choice."
}
```

## How you are scored
A hidden verifier will evaluate your output. The verifier independently builds the same dynamical matrix from the same force-constant forms and parameter values, solves for the eigenvalues at the identical set of q-points, and compares each frequency in your CSV to its own recomputed value. A frequency is considered correct if it falls within a strict absolute tolerance (the comparison is deterministic, so correct implementations should match to near machine precision). Your reward is proportional to the fraction of frequencies that pass this check. The intermediate evidence file fc_matrices.json is not scored; only the final frequencies in phonon_frequencies.csv contribute to your score.
