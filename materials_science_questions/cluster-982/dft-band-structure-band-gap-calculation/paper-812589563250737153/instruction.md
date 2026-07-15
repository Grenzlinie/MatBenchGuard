# First‑Principles Band Gap Calculation of a Crystalline Solid

## Problem background
The recently reported crystalline solid solution Ba5.47Sr0.53Al4B14O33 exhibits a transparent optical window and a sharp ultraviolet absorption edge, suggesting potential use as a host for luminescent ions. Understanding its electronic properties — in particular the fundamental band gap and the orbital character of the states near the Fermi level — is essential to rationalising its optical behaviour and to designing related borate-based optoelectronic materials. First‑principles density functional theory (DFT) calculations provide a route to obtain these properties without fitting parameters to experimental spectra.

## Approach
The electronic band structure and the direct band gap at the centre of the first Brillouin zone (the Γ point) are computed using plane‑wave pseudopotential DFT. A supercell of the triclinic unit cell is built and one of the Ba atoms is replaced by Sr to approximate the experimentally determined Sr doping concentration of roughly 8–9 %. The geometry of the doped supercell is fully relaxed (atomic positions and lattice parameters) under the generalized‑gradient approximation (GGA‑PBE). Afterwards, the band energies are evaluated along the high‑symmetry k‑path of the supercell's first Brillouin zone. From this data the valence band maximum (VBM) and conduction band minimum (CBM) at Γ are located, and the direct band gap is extracted. The workflow yields both the raw band‑structure data and the band gap value.

## Reproduction target
Your goal is to compute, for the Sr‑doped supercell model described above, (i) the electronic band structure data along the high‑symmetry k‑path that includes the Γ point, and (ii) the direct band gap at Γ (in eV). The raw band energies must be saved in a text file with a simple machine‑readable format, and the band gap value must be written to a JSON file. The computed band gap must be consistent with the band‑structure data.

## Assets

- Crystal structure CIF for the target compound: https://www.ccdc.cam.ac.uk/structures/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA‑PBE ultrasoft pseudopotentials: http://www.quantum-espresso.org/pseudopotentials
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Supercell construction and Sr substitution
- Role: process
- Action: Download the CIF file for the target crystal structure (CCDC 1887143). Build a 2×1×1 supercell of the triclinic unit cell. Replace one Ba atom with Sr to approximate the Sr doping concentration (~8.8%). Save the modified structure for the next step.
- Evidence: `/app/outputs/supercell_structure.cif`

### Step 2: DFT geometry optimization
- Role: process
- Action: Using Quantum ESPRESSO (pw.x) with the GGA‑PBE functional and ultrasoft pseudopotentials, perform a full geometry relaxation of the doped supercell (atomic positions and cell parameters). Continue until the forces and energy converge to reasonable tolerances.
- Evidence: `/app/outputs/geometry_optimization.out`

### Step 3: Electronic band structure calculation
- Role: scored
- Action: Using the relaxed supercell, compute the electronic band structure along the high‑symmetry k‑path of the first Brillouin zone (including the Γ point). Use Quantum ESPRESSO bands.x or pw.x with explicit k‑point path. Save the raw band energies for every k‑point and every band.
- Output file: `/app/outputs/band_structure.dat`
- Format: txt
- Contract: Text file with header line containing two integers; data lines with three numeric columns (k‑point index, band index, energy in eV).
- Scoring: scored by hidden verifier

### Step 4: Extract direct band gap
- Role: scored (load-bearing)
- Action: From band_structure.dat, identify the valence band maximum (VBM) and conduction band minimum (CBM) at the Γ point, and compute the direct band gap. Write the gap value (in eV) to /app/outputs/band_gap.json.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"band_gap": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure.dat`
- `/app/outputs/band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure.dat
- path: `/app/outputs/band_structure.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Raw electronic band structure along the high‑symmetry path. Verified for structural consistency (non‑empty, correct line count, plausible energy range).
- schema:
  - `type`: text
  - `description`: First line: two integers (number of k‑points, number of bands). Each subsequent line: kpoint_index band_index energy_eV (indices starting from 1).

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed direct band gap at the Γ point. The value is compared to the paper‑reported DFT band gap with an allowed tolerance that accounts for differences in DFT code and pseudopotentials.
- schema:
  - `type`: object
  - `required`:
    - `band_gap`: float (eV)

Notes: The band gap is extracted from the computed band structure and must be consistent with it. Tolerance for the band gap is not disclosed to the solver.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "First line: two integers (number of k‑points, number of bands). Each subsequent line: kpoint_index band_index energy_eV (indices starting from 1)."
      },
      "description": "Raw electronic band structure along the high‑symmetry path. Verified for structural consistency (non‑empty, correct line count, plausible energy range)."
    },
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap": "float (eV)"
        }
      },
      "description": "Computed direct band gap at the Γ point. The value is compared to the paper‑reported DFT band gap with an allowed tolerance that accounts for differences in DFT code and pseudopotentials."
    }
  ],
  "notes": "The band gap is extracted from the computed band structure and must be consistent with it. Tolerance for the band gap is not disclosed to the solver."
}
```

## How you are scored
A hidden verifier scores your outputs independently. The band‑structure file is checked for structural integrity: existence, a correct header line, a plausible number of data lines, and physically sensible energy ranges. The band‑gap file is compared to a hidden reference value derived from the original study. A tolerance is applied that accommodates differences arising from the use of an open‑source DFT code and pseudopotential library instead of the proprietary code originally employed. Reporting a plausible value that is consistent with your own band‑structure data is required; simply guessing or copying a known literature value without performing the calculation will yield a poor score. The final reward is a weighted combination of the two scored artifacts.
