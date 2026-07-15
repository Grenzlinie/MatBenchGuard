# Ab initio calculation of band gap, phonon modes, and dielectric tensor of orthorhombic SrZrO3

## Problem background
Strontium zirconate (SrZrO₃) is a perovskite oxide with promising high-κ dielectric properties for capacitor and gate-dielectric applications. Understanding its electronic band structure, phonon modes, and dielectric tensor is key to predicting and optimizing its performance. This task asks you to compute these properties for the room-temperature orthorhombic phase (space group *Pbnm*) from first principles, using density functional theory (DFT) and density functional perturbation theory (DFPT).

## Approach
You will perform a series of DFT calculations using a plane-wave basis set and norm-conserving pseudopotentials within the local density approximation (LDA). The computational pipeline, to be implemented with the open-source ABINIT code (or an equivalent DFT engine), consists of: (1) structural relaxation starting from the experimental crystal structure, (2) calculation of Born effective charges and the electronic dielectric tensor via DFPT linear response, (3) electronic band structure and band gap extraction, (4) zone-center phonon frequency calculation (TO and LO) with symmetry assignments, mode effective charges, and dielectric intensities, and (5) assembly of the electronic, ionic, and static dielectric tensors. The method avoids any empirical parameters and uses only standard LDA and publicly available pseudopotentials. The goal is to reproduce the quantities that determine how the material responds to electric fields and its characteristic vibrational signatures.

## Reproduction target
Produce three scored output files by following the workflow steps:

*   **band_gap.json**: the indirect band gap (valence band maximum to conduction band minimum) and the direct band gap at the Γ point, both in eV, along with a label indicating the gap type.
*   **phonon_frequencies.csv**: a table of TO and LO phonon frequencies (cm⁻¹), symmetry labels, scalar mode effective charges, and dielectric intensities for all 25 IR-active modes of orthorhombic SrZrO₃.
*   **dielectric_tensor.json**: the diagonal components (xx, yy, zz) and the orientationally averaged values of the electronic, ionic, and static dielectric tensors.

Your results will be compared to known reference values obtained from the literature under the same computational conditions.

## Assets

- ABINIT software: https://www.abinit.org/
- LDA norm-conserving pseudopotentials for Sr, Zr, O: http://www.abinit.org/psp-tables
- Initial orthorhombic SrZrO3 crystal structure (Pbnm): 10.1103/PhysRevB.59.4023

## Workflow steps

### Step 1: Structural relaxation
- Role: process
- Action: Using DFT with the local density approximation and a plane-wave basis, relax the lattice constants and atomic positions of orthorhombic SrZrO₃ (space group Pbnm, 4 formula units) until forces are converged. The initial structure is the experimental geometry from the literature (Kennedy et al., 1999).
- Evidence: none

### Step 2: Born effective charges and electronic dielectric tensor
- Role: process
- Action: Using density functional perturbation theory (DFPT) linear response with the same DFT parameters as the relaxation, compute the Born effective charge tensors for every atom and the high‑frequency (electronic) dielectric tensor from the relaxed geometry. These are inputs for subsequent phonon and dielectric calculations.
- Evidence: none

### Step 3: Electronic band structure and band gap
- Role: scored
- Action: From the relaxed geometry, compute the electronic band structure along high‑symmetry paths in the orthorhombic Brillouin zone. Determine the indirect band gap (valence band maximum to conduction band minimum) and the direct band gap at the Γ point. Write the results to band_gap.json.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"indirect_gap_eV": <float>, "direct_gap_Gamma_eV": <float>, "band_gap_type": "indirect"}
- Scoring: scored by hidden verifier

### Step 4: IR-active phonon frequencies, mode effective charges, and dielectric intensities
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, Born effective charges, and electronic dielectric tensor, compute the zone-center phonon frequencies (TO and LO) for all IR-active modes via DFPT including the non-analytical contribution that produces LO-TO splitting. Compute for each IR mode the scalar mode effective charge and the dielectric intensity. Write a CSV file with one row per IR-active mode (25 modes, excluding acoustic modes) with columns: TO frequency (cm⁻¹), LO frequency (cm⁻¹), symmetry label, scalar mode effective charge (dimensionless), and dielectric intensity (dimensionless).
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Header: TO_cm1,LO_cm1,symmetry,Z_star,epsilon. Each row: float,float,string(B1u/B2u/B3u),float,float. Exactly 25 data rows.
- Scoring: scored by hidden verifier

### Step 5: Static dielectric tensor
- Role: scored (load-bearing)
- Action: From the computed Born effective charges, electronic dielectric tensor, phonon eigenvectors, and unit cell volume, compute the ionic contribution to the static dielectric tensor by summing over all IR-active modes. Assemble the full static dielectric tensor with electronic, ionic, and total components along the principal axes (xx, yy, zz) and the orientationally averaged value. Write the results to dielectric_tensor.json.
- Output file: `/app/outputs/dielectric_tensor.json`
- Format: json
- Contract: {"electronic": {"xx": float, "yy": float, "zz": float, "average": float}, "ionic": {"xx": float, "yy": float, "zz": float, "average": float}, "static": {"xx": float, "yy": float, "zz": float, "average": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/dielectric_tensor.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The indirect band gap (eV), direct band gap at Γ (eV), and a string confirming the indirect nature of the gap.
- schema:
  - `type`: object
  - `required`:
    - `indirect_gap_eV`: number
    - `direct_gap_Gamma_eV`: number
    - `band_gap_type`: string

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies (TO and LO in cm⁻¹), symmetry label (B1u, B2u, or B3u), scalar mode effective charge, and dielectric intensity for each of the 25 IR-active modes.
- schema:
  - `type`: table
  - `required_columns`: `TO_cm1`, `LO_cm1`, `symmetry`, `Z_star`, `epsilon`
  - `units`:
    - `TO_cm1`: cm^{-1}
    - `LO_cm1`: cm^{-1}
    - `Z_star`: dimensionless
    - `epsilon`: dimensionless

### dielectric_tensor.json
- path: `/app/outputs/dielectric_tensor.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic, ionic, and static dielectric tensor diagonal components (xx, yy, zz) and their orientationally averaged values.
- schema:
  - `type`: object
  - `required`:
    - `electronic`:
      - `xx`: number
      - `yy`: number
      - `zz`: number
      - `average`: number
    - `ionic`:
      - `xx`: number
      - `yy`: number
      - `zz`: number
      - `average`: number
    - `static`:
      - `xx`: number
      - `yy`: number
      - `zz`: number
      - `average`: number

Notes: The agent must perform the full DFT/DFPT workflow and produce the three scored artifacts that correspond to the main headline quantities of the paper: band gap, phonon spectrum, and dielectric tensor. Tolerances and reference values are kept hidden for grading.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "indirect_gap_eV": "number",
          "direct_gap_Gamma_eV": "number",
          "band_gap_type": "string"
        }
      },
      "description": "The indirect band gap (eV), direct band gap at Γ (eV), and a string confirming the indirect nature of the gap."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "TO_cm1",
          "LO_cm1",
          "symmetry",
          "Z_star",
          "epsilon"
        ],
        "units": {
          "TO_cm1": "cm^{-1}",
          "LO_cm1": "cm^{-1}",
          "Z_star": "dimensionless",
          "epsilon": "dimensionless"
        }
      },
      "description": "Phonon frequencies (TO and LO in cm⁻¹), symmetry label (B1u, B2u, or B3u), scalar mode effective charge, and dielectric intensity for each of the 25 IR-active modes."
    },
    {
      "file": "dielectric_tensor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "electronic": {
            "xx": "number",
            "yy": "number",
            "zz": "number",
            "average": "number"
          },
          "ionic": {
            "xx": "number",
            "yy": "number",
            "zz": "number",
            "average": "number"
          },
          "static": {
            "xx": "number",
            "yy": "number",
            "zz": "number",
            "average": "number"
          }
        }
      },
      "description": "Electronic, ionic, and static dielectric tensor diagonal components (xx, yy, zz) and their orientationally averaged values."
    }
  ],
  "notes": "The agent must perform the full DFT/DFPT workflow and produce the three scored artifacts that correspond to the main headline quantities of the paper: band gap, phonon spectrum, and dielectric tensor. Tolerances and reference values are kept hidden for grading."
}
```

## How you are scored
Your submission will be evaluated automatically by a hidden verifier that reads the three output files described above. Each artifact is scored separately:

- The band gap values are compared to reference data with a tolerance appropriate for LDA-DFT calculations.
- The phonon table is checked for correctness of the number of IR-active modes, symmetry labels, and the TO and LO frequencies, as well as the mode effective charges and dielectric intensities, within physically reasonable margins.
- The dielectric tensor is compared component by component to expected values, including the orientationally averaged static constant.

The verifier combines these scores into a single reward in [0,1] reflecting the overall reproduction quality. It does not require an exact match; small deviations arising from implementation details (pseudopotential choice, code version, etc.) are allowed. Simply reporting the expected numbers without performing the full DFT/DFPT workflow will not meet the required precision and will result in a low score.
