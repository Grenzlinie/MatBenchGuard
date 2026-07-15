# DFT/DFPT computation of band structure and dielectric properties of orthorhombic SrZrO3

## Problem background
Orthorhombic SrZrO3 (space group Pbnm) is a perovskite oxide with a high dielectric constant and wide band gap, making it a candidate for high-κ gate dielectrics and other electronic devices. Its electrical performance is determined by the electronic band structure—particularly the size and character of the band gap—the frequencies and symmetries of its zone‑center phonon modes, and the full dielectric tensor (electronic, ionic, and static contributions). This task reproduces a first‑principles computation of these three quantities using density functional theory (DFT) and density functional perturbation theory (DFPT).

## Approach
We use the open‑source ABINIT code to perform DFT and DFPT calculations. Starting from the experimental orthorhombic SrZrO3 structure (space group Pbnm), a full structural relaxation is carried out in the local density approximation (LDA) with norm‑conserving pseudopotentials. From the relaxed geometry, the electronic band structure is computed to obtain the indirect and direct band gaps. DFPT linear‑response calculations then yield the electronic dielectric tensor (ε∞), the Born effective charge tensors, and the analytical part of the force‑constant matrix. These ingredients are combined to build the full dynamical matrix, including the non‑analytic dipole‑dipole contribution, from which the zone‑center transverse‑optic (TO) and longitudinal‑optic (LO) phonon frequencies, their irreducible‑representation symmetries, and the mode effective charges and dielectric intensities for the infrared‑active (IR) modes are obtained. Summing the mode intensities gives the ionic dielectric tensor; combining it with ε∞ produces the static dielectric tensor. All results are written to structured JSON files for scoring.

## Reproduction target
Produce three scored JSON artifacts in /app/outputs:
- `band_gap.json`: the indirect and direct band gaps (eV).
- `phonon_modes.json`: the full list of zone‑center phonon modes; for each mode report the TO frequency, LO frequency, symmetry label (B1u, B2u, B3u, Ag, B1g, B2g, B3g, Au), mode type (IR/Raman/Silent), and for IR modes the scalar mode effective charge Z* and the dielectric intensity ε.
- `dielectric_tensor.json`: the electronic ε∞, ionic εᵢₒₙᵢ₋, and static ε₀ dielectric tensors (xx, yy, zz components) and their orientationally averaged values.

## Assets

- ABINIT: https://www.abinit.org/
- Pseudopotentials for Sr, Zr, O: https://www.abinit.org/downloads/pseudopotentials

## Workflow steps

### Step 1: Structure relaxation
- Role: process
- Action: Starting from the experimental orthorhombic SrZrO3 structure (space group Pbnm) with lattice constants a=5.796 Å, b=5.817 Å, c=8.205 Å and atomic positions (fractional): Sr (0.007,0.534,0.25), Zr (0,0,0), O1 (-0.107,-0.036,0.25), O2 (0.199,0.301,0.056), perform DFT structure relaxation (lattice parameters and atomic positions) using a suitable exchange-correlation functional (e.g., LDA). Force convergence < 10^{-2} eV/Å.
- Evidence: `/app/outputs/relaxed_structure.txt`

### Step 2: Electronic band structure and band gap
- Role: scored
- Action: Perform a self-consistent field (SCF) calculation followed by a non-self-consistent band structure calculation on the relaxed structure. Extract the indirect band gap from valence band maximum to conduction band minimum and the direct band gap. Report both values in eV.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"indirect_gap": float (eV), "direct_gap": float (eV)}
- Scoring: scored by hidden verifier

### Step 3: DFPT linear-response calculation
- Role: process
- Action: Using density functional perturbation theory (DFPT) within ABINIT on the relaxed structure, compute the electronic dielectric tensor (ε∞), the Born effective charge tensors for each atom, and the analytical part of the zone-center force constant matrix.
- Evidence: `/app/outputs/dfpt_output_summary.json`

### Step 4: Phonon frequency and symmetry analysis
- Role: scored (load-bearing)
- Action: Construct the dynamical matrix including the non-analytical long-range dipole-dipole contribution using the force constant matrix, Born charges, and ε∞. Diagonalize to obtain zone-center TO and LO phonon frequencies. Assign irreducible representations (IR: B1u, B2u, B3u; Raman: Ag, B1g, B2g, B3g; Silent: Au). For each IR mode, compute scalar mode effective charge Z*_λ and dielectric intensity ε_λ.
- Output file: `/app/outputs/phonon_modes.json`
- Format: json
- Contract: {"phonon_modes": [{"TO_frequency": float, "LO_frequency": float, "symmetry": string, "mode_type": "IR"|"Raman"|"Silent", "Z_star": float|null, "dielectric_intensity": float|null}]}
- Scoring: scored by hidden verifier

### Step 5: Dielectric tensor and static constant
- Role: scored (load-bearing)
- Action: Sum the mode dielectric intensities to obtain the ionic dielectric tensor ε^ionic components. Combine with ε∞ to obtain the static dielectric tensor ε^0 components and orientationally averaged static dielectric constant.
- Output file: `/app/outputs/dielectric_tensor.json`
- Format: json
- Contract: {"epsilon_infinity": {"xx": float, "yy": float, "zz": float, "average": float}, "epsilon_ionic": {"xx": float, "yy": float, "zz": float, "average": float}, "epsilon_0": {"xx": float, "yy": float, "zz": float, "average": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/phonon_modes.json`
- `/app/outputs/dielectric_tensor.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Indirect and direct band gaps computed from the DFT band structure.
- schema:
  - `type`: object
  - `required`:
    - `indirect_gap`: float (eV)
    - `direct_gap`: float (eV)

### phonon_modes.json
- path: `/app/outputs/phonon_modes.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Complete list of zone-center phonon modes with frequencies, symmetry, and dielectric contributions.
- schema:
  - `type`: object
  - `required`:
    - `phonon_modes`: array of objects
  - `items`:
    - `TO_frequency`: float (cm⁻¹)
    - `LO_frequency`: float (cm⁻¹)
    - `symmetry`: string
    - `mode_type`: string (IR, Raman, Silent)
    - `Z_star`: float (for IR modes, null otherwise)
    - `dielectric_intensity`: float (for IR modes, null otherwise)

### dielectric_tensor.json
- path: `/app/outputs/dielectric_tensor.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic, ionic, and static dielectric tensor components and orientationally averaged values.
- schema:
  - `type`: object
  - `required`:
    - `epsilon_infinity`: object {xx, yy, zz, average}
    - `epsilon_ionic`: object {xx, yy, zz, average}
    - `epsilon_0`: object {xx, yy, zz, average}

Notes: The scored outputs are compared against the paper's reported reference values with tolerances appropriate for DFT re-runs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "indirect_gap": "float (eV)",
          "direct_gap": "float (eV)"
        }
      },
      "description": "Indirect and direct band gaps computed from the DFT band structure."
    },
    {
      "file": "phonon_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "phonon_modes": "array of objects"
        },
        "items": {
          "TO_frequency": "float (cm⁻¹)",
          "LO_frequency": "float (cm⁻¹)",
          "symmetry": "string",
          "mode_type": "string (IR, Raman, Silent)",
          "Z_star": "float (for IR modes, null otherwise)",
          "dielectric_intensity": "float (for IR modes, null otherwise)"
        }
      },
      "description": "Complete list of zone-center phonon modes with frequencies, symmetry, and dielectric contributions."
    },
    {
      "file": "dielectric_tensor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_infinity": "object {xx, yy, zz, average}",
          "epsilon_ionic": "object {xx, yy, zz, average}",
          "epsilon_0": "object {xx, yy, zz, average}"
        }
      },
      "description": "Electronic, ionic, and static dielectric tensor components and orientationally averaged values."
    }
  ],
  "notes": "The scored outputs are compared against the paper's reported reference values with tolerances appropriate for DFT re-runs."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that independently compares each computed quantity against a reference standard. Band gaps, phonon frequencies, mode symmetries, dielectric intensities, and dielectric tensor components are all checked, and a weighted score is computed from the accuracy of every field. Running the actual DFT/DFPT workflow is mandatory; reporting a value without executing the calculations does not meet the task requirements.
