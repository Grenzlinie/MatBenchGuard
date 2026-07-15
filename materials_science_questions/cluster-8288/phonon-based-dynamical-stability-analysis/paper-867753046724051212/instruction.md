# Phonon stability and topological band inversion in a Bi bilayer with 4,6,8-atom rings

## Problem background
Two‑dimensional (2D) group V elemental bilayers are attractive because they combine a non‑zero band gap with high electron mobility. A new structure model for these bilayers, containing rings of 4, 6 and 8 atoms, has been proposed for the elements Bi, Sb and As. For Bi, the structure may exhibit nontrivial topological properties due to the strong spin‑orbit coupling (SOC) of the heavy Bi atoms. The goal of this task is to reproduce the key computational results that characterize the Bi 4(8)‑6 bilayer: its dynamical stability (phonon spectrum), its electronic band gaps with and without SOC, and its topological character as determined by parity eigenvalues and the Z₂ invariant. In addition, a tunable variant with more hexagon rings, denoted 4(8)‑6‑6, is studied to see how the properties change.

## Approach
The reproduction relies on first‑principles density functional theory (DFT) calculations using the open‑source Quantum ESPRESSO package with the PBE exchange‑correlation functional and plane‑wave basis. Structural relaxations are carried out for both the base Bi 4(8)‑6 bilayer (orthorhombic space group Pccm, with approximate lattice constants a=7.918 Å, b=13.050 Å and two distinct Wyckoff positions) and the tunable 4(8)‑6‑6 variant (a≈7.778 Å, b≈17.493 Å). Phonon dispersions are computed with the finite‑displacement method via Phonopy to assess dynamical stability. Electronic band structures are evaluated along high‑symmetry paths without and with SOC; the direct band gap at the Γ point is extracted for the base bilayer, while the band gap (direct or indirect) is extracted for the tunable variant.

The topological classification uses parity analysis. Because the structures possess inversion symmetry, the Z₂ topological invariant ν can be obtained from the product of parity eigenvalues at the four time‑reversal invariant momenta (TRIM): Γ, X, Y, M. For each occupied Kramers pair at each TRIM, the parity eigenvalue (±1) is computed from the DFT+SOC wave functions using Wannier90 (or equivalent interfacing). The product δ(K) at each TRIM is then formed, and ν is given by (−1)^ν = ∏_K δ(K). The task requires computing δ(K) for the base bilayer and for the tunable variant, and deriving the Z₂ invariant for the base system. The tunable variant’s SOC band gap is also extracted to test whether it exceeds the base bilayer’s SOC gap.

## Reproduction target
Produce the following seven output files, each containing recomputed quantities:

1. `step_01_phonon_stability.json` – maximum imaginary frequency from the phonon spectrum of the Bi 4(8)‑6 bilayer (a non‑positive value indicates dynamical stability).
2. `step_02_band_gap_noSOC.txt` – direct band gap at Γ (eV) without spin‑orbit coupling.
3. `step_03_band_gap_SOC.txt` – direct band gap at Γ (eV) with spin‑orbit coupling.
4. `step_04_parity_eigenvalues.json` – product of parity eigenvalues δ(K) at Γ, X, Y, M for the Bi 4(8)‑6 bilayer (each entry +1 or −1).
5. `step_05_Z2_invariant.txt` – integer 0 or 1 obtained from the parity products.
6. `step_06_tunable_parity.json` – δ(K) at the TRIM points for the Bi 4(8)‑6‑6 variant.
7. `step_07_tunable_gap_SOC.txt` – SOC band gap (eV) for the tunable variant.

The tunable gap must be compared to the base bilayer’s SOC gap to verify a larger gap in the variant. The parity eigenvalues for the tunable variant will be used by the verifier to derive the Z₂ invariant and to confirm the topological character; no additional Z₂ file is required for the variant. All these values are to be computed from scratch using the described DFT protocol and open‑source tools; the paper’s own reported values serve only as a hidden reference for the verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Wannier90: https://wannier.org/
- Z2Pack: https://z2pack.ethz.ch/
- WannierTools: https://github.com/quanshengwu/wannier_tools

## Workflow steps

### Step 1: DFT Relaxation of Bi 4(8)-6 bilayer
- Role: process
- Action: Build the initial crystal structure from the paper's description (space group Pccm, lattice constants a≈7.918 Å, b≈13.050 Å, two Wyckoff positions with buckling heights, bond lengths) and relax atomic positions and lattice vectors using DFT with Quantum ESPRESSO (PBE functional, plane-wave cutoff 500 eV, Monkhorst-Pack k-point grid 13×7×1).
- Evidence: none

### Step 2: Phonon stability of Bi 4(8)-6 bilayer
- Role: scored
- Action: Compute phonon dispersion with the finite displacement method (Phonopy) on the relaxed structure and determine the maximum imaginary frequency.
- Output file: `/app/outputs/step_01_phonon_stability.json`
- Format: json
- Contract: {"max_imaginary_frequency": number (in cm⁻¹ or THz)}
- Scoring: scored by hidden verifier

### Step 3: Band structure without SOC for Bi 4(8)-6
- Role: scored
- Action: Compute electronic band structure along the high-symmetry path without spin-orbit coupling and extract the direct band gap at the Γ point.
- Output file: `/app/outputs/step_02_band_gap_noSOC.txt`
- Format: txt
- Contract: single float
- Scoring: scored by hidden verifier

### Step 4: Band structure with SOC for Bi 4(8)-6
- Role: scored
- Action: Compute electronic band structure with spin-orbit coupling included and extract the direct band gap at the Γ point.
- Output file: `/app/outputs/step_03_band_gap_SOC.txt`
- Format: txt
- Contract: single float
- Scoring: scored by hidden verifier

### Step 5: Parity eigenvalues at TRIM for Bi 4(8)-6
- Role: scored (load-bearing)
- Action: Using the DFT+SOC wave functions and Wannier90 (or equivalent), compute parity eigenvalues for occupied Kramers pairs at the four TRIM points (Γ, X, Y, M) and output the product of parity eigenvalues δ(K) at each TRIM.
- Output file: `/app/outputs/step_04_parity_eigenvalues.json`
- Format: json
- Contract: {"Γ": int, "X": int, "Y": int, "M": int}
- Scoring: scored by hidden verifier

### Step 6: Z2 topological invariant from parity
- Role: scored (load-bearing)
- Action: Compute the Z2 topological invariant ν using the parity eigenvalue products (Eq. 2) and output the integer 0 or 1.
- Output file: `/app/outputs/step_05_Z2_invariant.txt`
- Format: txt
- Contract: single integer (0 or 1)
- Scoring: scored by hidden verifier

### Step 7: DFT Relaxation of Bi 4(8)-6-6 variant
- Role: process
- Action: Build the initial crystal structure for the 4(8)-6-6 variant (increased unit cell, a≈7.778 Å, b≈17.493 Å) and relax using DFT with the same parameters as the base bilayer.
- Evidence: none

### Step 8: Parity eigenvalues for 4(8)-6-6
- Role: scored
- Action: Compute parity eigenvalues at TRIM points for the relaxed 4(8)-6-6 structure using DFT+SOC and output the product δ(K) at each TRIM.
- Output file: `/app/outputs/step_06_tunable_parity.json`
- Format: json
- Contract: {"Γ": int, "X": int, "Y": int, "M": int}
- Scoring: scored by hidden verifier

### Step 9: SOC band gap for 4(8)-6-6
- Role: scored (load-bearing)
- Action: Compute band structure with SOC for the relaxed 4(8)-6-6 variant and output the electronic band gap.
- Output file: `/app/outputs/step_07_tunable_gap_SOC.txt`
- Format: txt
- Contract: single float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phonon_stability.json`
- `/app/outputs/step_02_band_gap_noSOC.txt`
- `/app/outputs/step_03_band_gap_SOC.txt`
- `/app/outputs/step_04_parity_eigenvalues.json`
- `/app/outputs/step_05_Z2_invariant.txt`
- `/app/outputs/step_06_tunable_parity.json`
- `/app/outputs/step_07_tunable_gap_SOC.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phonon_stability.json
- path: `/app/outputs/step_01_phonon_stability.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum imaginary frequency from the phonon spectrum; if ≤ 0, the structure is dynamically stable.
- schema:
  - `type`: object
  - `required`:
    - `max_imaginary_frequency`: number (in cm⁻¹ or THz)

### step_02_band_gap_noSOC.txt
- path: `/app/outputs/step_02_band_gap_noSOC.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Direct band gap at Γ computed without SOC, to be compared to the paper's value within tolerance.
- schema:
  - `type`: text
  - `description`: single float (eV) – direct band gap at Γ without spin-orbit coupling

### step_03_band_gap_SOC.txt
- path: `/app/outputs/step_03_band_gap_SOC.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Direct band gap at Γ computed with SOC, to be compared to the paper's value within tolerance.
- schema:
  - `type`: text
  - `description`: single float (eV) – direct band gap at Γ with spin-orbit coupling

### step_04_parity_eigenvalues.json
- path: `/app/outputs/step_04_parity_eigenvalues.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Product of parity eigenvalues δ(K) at the four TRIM points for the Bi 4(8)-6 bilayer.
- schema:
  - `type`: object
  - `required`:
    - `Γ`: integer (+1 or -1)
    - `X`: integer (+1 or -1)
    - `Y`: integer (+1 or -1)
    - `M`: integer (+1 or -1)

### step_05_Z2_invariant.txt
- path: `/app/outputs/step_05_Z2_invariant.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Z2 invariant derived from the parity products; must be 1 for a nontrivial topological state.
- schema:
  - `type`: text
  - `description`: single integer (0 or 1) – Z2 topological invariant ν

### step_06_tunable_parity.json
- path: `/app/outputs/step_06_tunable_parity.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Parity eigenvalue products at TRIMs for the tunable Bi 4(8)-6-6 variant; the checker will verify that the resulting Z2 invariant is 1 and that the parity pattern is nontrivial.
- schema:
  - `type`: object
  - `required`:
    - `Γ`: integer (+1 or -1)
    - `X`: integer (+1 or -1)
    - `Y`: integer (+1 or -1)
    - `M`: integer (+1 or -1)

### step_07_tunable_gap_SOC.txt
- path: `/app/outputs/step_07_tunable_gap_SOC.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: SOC band gap for the 4(8)-6-6 structure; must be greater than the base bilayer's SOC gap by at least 0.1 eV.
- schema:
  - `type`: text
  - `description`: single float (eV) – SOC band gap for the tunable variant

Notes: All artifacts are produced from open-source DFT calculations using Quantum ESPRESSO. Band gaps are compared to paper-reported values within relative tolerance 10% or absolute 0.05 eV. Parity eigenvalues must exactly match the known values for the Bi 4(8)-6 bilayer; the tunable variant's parity is audited structurally. The tunable gap must exceed the base gap, confirming the trend. The checker recomputes the Z2 invariant from the tunable parity product.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "max_imaginary_frequency": "number (in cm⁻¹ or THz)"
        }
      },
      "description": "Maximum imaginary frequency from the phonon spectrum; if ≤ 0, the structure is dynamically stable."
    },
    {
      "file": "step_02_band_gap_noSOC.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "single float (eV) – direct band gap at Γ without spin-orbit coupling"
      },
      "description": "Direct band gap at Γ computed without SOC, to be compared to the paper's value within tolerance."
    },
    {
      "file": "step_03_band_gap_SOC.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "single float (eV) – direct band gap at Γ with spin-orbit coupling"
      },
      "description": "Direct band gap at Γ computed with SOC, to be compared to the paper's value within tolerance."
    },
    {
      "file": "step_04_parity_eigenvalues.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Γ": "integer (+1 or -1)",
          "X": "integer (+1 or -1)",
          "Y": "integer (+1 or -1)",
          "M": "integer (+1 or -1)"
        }
      },
      "description": "Product of parity eigenvalues δ(K) at the four TRIM points for the Bi 4(8)-6 bilayer."
    },
    {
      "file": "step_05_Z2_invariant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "single integer (0 or 1) – Z2 topological invariant ν"
      },
      "description": "Z2 invariant derived from the parity products; must be 1 for a nontrivial topological state."
    },
    {
      "file": "step_06_tunable_parity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Γ": "integer (+1 or -1)",
          "X": "integer (+1 or -1)",
          "Y": "integer (+1 or -1)",
          "M": "integer (+1 or -1)"
        }
      },
      "description": "Parity eigenvalue products at TRIMs for the tunable Bi 4(8)-6-6 variant; the checker will verify that the resulting Z2 invariant is 1 and that the parity pattern is nontrivial."
    },
    {
      "file": "step_07_tunable_gap_SOC.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "single float (eV) – SOC band gap for the tunable variant"
      },
      "description": "SOC band gap for the 4(8)-6-6 structure; must be greater than the base bilayer's SOC gap by at least 0.1 eV."
    }
  ],
  "notes": "All artifacts are produced from open-source DFT calculations using Quantum ESPRESSO. Band gaps are compared to paper-reported values within relative tolerance 10% or absolute 0.05 eV. Parity eigenvalues must exactly match the known values for the Bi 4(8)-6 bilayer; the tunable variant's parity is audited structurally. The tunable gap must exceed the base gap, confirming the trend. The checker recomputes the Z2 invariant from the tunable parity product."
}
```

## How you are scored
Each of the seven output files is assessed by a hidden verifier that compares your computed values against predefined criteria (paper‑reported values, structural rules, or threshold checks) with appropriate tolerances. The checks are:

- Phonon stability: the maximum imaginary frequency must be ≤ 0.
- Band gaps: your computed gaps must agree with the reference values within a relative tolerance (or absolute) set by the verifier.
- Parity eigenvalues for the base bilayer: your δ(K) values are compared to the known exact parity products.
- Z₂ invariant: must be exactly 0 or 1 as determined by the parity products.
- Tunable parity: the verifier derives the Z₂ invariant from your δ(K) values and checks that the parity pattern yields a nontrivial topology.
- Tunable gap: the verifier checks that your computed gap exceeds the base SOC gap by a margin, and optionally compares it to a reference value.

A combined score is computed from the weighted outcomes of these checks. The highest reward is earned by faithfully executing the DFT workflow and computing the quantities from first principles; merely reporting paper values without doing the computation will not pass because the verifier may apply structural or tolerance criteria that require genuine recomputation.
