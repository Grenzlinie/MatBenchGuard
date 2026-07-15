# Chiral Phonon Analysis in a Chiral 2D Halide Perovskite

## Problem background
Chiral phonons are lattice vibrations that carry spin angular momentum due to a crystal's lack of inversion and mirror symmetries. In two-dimensional hybrid halide perovskites, chirality can be introduced by incorporating chiral organic cations, which distort the inorganic framework. Understanding whether such materials host chiral phonons and quantifying their spin and associated angular momentum transport is of fundamental and practical interest, as phonon angular momentum can be detected in heat transport experiments and couples to electron spin. This task investigates the chiral phonon properties of the 2D perovskite (S-MBA)₂PbI₄ (space group P2₁2₁2₁).

## Approach
The harmonic phonon dispersion and eigenvectors are computed from a pre-trained machine-learning force field (MLFF) that reproduces density functional theory (SCAN) accuracy, using the supercell approach. The phonon circular polarization (phonon spin) s_{q,σ}^α is evaluated for each mode from the polarization vectors and spin-1 matrices. The analysis focuses on low-energy modes (below 25 meV) and on paths along the crystal axes. The antisymmetry relation s_{q,σ}^α = −s_{−q,σ}^α, a consequence of time-reversal symmetry, is checked. The intrinsic phonon angular momentum response tensor α^{αβ} is then computed at 300 K from the phonon spins, group velocities, and equilibrium occupation numbers (without the relaxation time τ). The diagonal components are compared to assess anisotropy.

## Reproduction target
Compute the harmonic phonons of (S-MBA)₂PbI₄ using the publicly available crystal structure and the pre-trained MLFF. From the obtained phonon data, produce three scored artifacts: (i) low-energy chirality statistics (maximum |s| and count of modes with |s|≥0.25 among modes below 25 meV), (ii) antisymmetry deviation max |s_{q,σ}^x + s_{−q,σ}^x| along the Γ‑X path, and (iii) diagonal components α^{xx}, α^{yy}, α^{zz} of the intrinsic response tensor at 300 K, without multiplying by τ. The hidden verifier will check these artifacts for consistency with the expected behaviour.

## Assets

- Crystal structure of (S-MBA)2PbI4: 10.1038/s41467-020-18440-w
- Pre-trained ML force field for (S-MBA)2PbI4: 10.1021/acs.jpclett.4c01591
- phonopy: phonopy
- NumPy: numpy

## Workflow steps

### Step 1: Harmonic phonon calculation
- Role: process
- Action: Using the crystal structure of (S-MBA)2PbI4 (space group P2₁2₁2₁) and the pre-trained machine-learning force field from Pols et al., compute harmonic phonon frequencies, eigenvectors, and group velocities on a fine q-point grid covering the Brillouin zone, including paths Γ‑X, Γ‑Y, Γ‑Z and the negative directions. Use phonopy with the supercell approach.
- Evidence: none

### Step 2: Low-energy chirality statistics
- Role: scored
- Action: For every phonon mode with frequency < 25 meV, compute the circular polarization s_{q,σ}^α using the normalized polarization vectors and the spin-1 matrices S^α (α=x,y,z). Record the maximum |s| among these modes and count how many modes satisfy |s| ≥ 0.25.
- Output file: `/app/outputs/low_energy_chirality.json`
- Format: json
- Contract: {"max_s": "float", "count_s_above_quarter": "int", "total_low_energy_modes": "int"}
- Scoring: scored by hidden verifier

### Step 3: Antisymmetry check for Γ‑X path
- Role: scored
- Action: Along the Γ‑X path, for each band, compute the deviation of the antisymmetry relation: |s_{q,σ}^x + s_{-q,σ}^x|. Determine the maximum deviation across all bands and report whether it is consistent (small deviation).
- Output file: `/app/outputs/antisymmetry_check.json`
- Format: json
- Contract: {"q_path": "string", "deviation_max": "float", "consistent": "bool"}
- Scoring: scored by hidden verifier

### Step 4: Phonon angular momentum response tensor
- Role: scored (load-bearing)
- Action: Using the phonon spins, group velocities, frequencies, and the Bose-Einstein distribution at 300 K, compute the diagonal components of the intrinsic response tensor: α^{αα} = -(ħ/V) Σ_{q,σ} s_{q,σ}^α v_{q,σ}^α (∂f₀/∂T). Do not multiply by the relaxation time τ. Report α^{xx}, α^{yy}, α^{zz}.
- Output file: `/app/outputs/response_tensor.json`
- Format: json
- Contract: {"alpha_xx": "float", "alpha_yy": "float", "alpha_zz": "float", "temperature": 300, "units_explanation": "J s m⁻² K⁻¹ without τ"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/low_energy_chirality.json`
- `/app/outputs/antisymmetry_check.json`
- `/app/outputs/response_tensor.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### low_energy_chirality.json
- path: `/app/outputs/low_energy_chirality.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Low-energy chirality statistics: maximum |s|, count of modes with |s|≥0.25, and total modes <25 meV.
- schema:
  - `type`: object
  - `required`: `max_s`, `count_s_above_quarter`, `total_low_energy_modes`
  - `items`: object
  - `units`:
    - `max_s`: dimensionless
    - `count_s_above_quarter`: integer count
    - `total_low_energy_modes`: integer count

### antisymmetry_check.json
- path: `/app/outputs/antisymmetry_check.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Antisymmetry check for Γ‑X: maximum deviation and consistency flag.
- schema:
  - `type`: object
  - `required`: `q_path`, `deviation_max`, `consistent`
  - `items`: object
  - `units`:
    - `q_path`: crystallographic path label
    - `deviation_max`: dimensionless
    - `consistent`: boolean

### response_tensor.json
- path: `/app/outputs/response_tensor.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Intrinsic response tensor components at 300 K, without relaxation time τ.
- schema:
  - `type`: object
  - `required`: `alpha_xx`, `alpha_yy`, `alpha_zz`, `temperature`, `units_explanation`
  - `items`: object
  - `units`:
    - `alpha_xx`: J s m⁻² K⁻¹
    - `alpha_yy`: J s m⁻² K⁻¹
    - `alpha_zz`: J s m⁻² K⁻¹

Notes: All values are the agent's computed results; the checker will evaluate consistency with paper relations, not absolute exact numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "low_energy_chirality.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "max_s",
          "count_s_above_quarter",
          "total_low_energy_modes"
        ],
        "items": {},
        "units": {
          "max_s": "dimensionless",
          "count_s_above_quarter": "integer count",
          "total_low_energy_modes": "integer count"
        }
      },
      "description": "Low-energy chirality statistics: maximum |s|, count of modes with |s|≥0.25, and total modes <25 meV."
    },
    {
      "file": "antisymmetry_check.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "q_path",
          "deviation_max",
          "consistent"
        ],
        "items": {},
        "units": {
          "q_path": "crystallographic path label",
          "deviation_max": "dimensionless",
          "consistent": "boolean"
        }
      },
      "description": "Antisymmetry check for Γ‑X: maximum deviation and consistency flag."
    },
    {
      "file": "response_tensor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "alpha_xx",
          "alpha_yy",
          "alpha_zz",
          "temperature",
          "units_explanation"
        ],
        "items": {},
        "units": {
          "alpha_xx": "J s m⁻² K⁻¹",
          "alpha_yy": "J s m⁻² K⁻¹",
          "alpha_zz": "J s m⁻² K⁻¹"
        }
      },
      "description": "Intrinsic response tensor components at 300 K, without relaxation time τ."
    }
  ],
  "notes": "All values are the agent's computed results; the checker will evaluate consistency with paper relations, not absolute exact numbers."
}
```

## How you are scored
A hidden verifier reads your three JSON output files. Each stage carries a weight, and the verifier compares your reported values to hidden criteria that capture the essential conclusions of the original study (signs, relative magnitudes, threshold exceedances). The final reward is the weighted combination of these stage scores. Reporting plausible numbers that merely match prior expectations without genuine computation will not earn credit; the evaluation is designed to reward an accurate reproduction of the computational pipeline.
