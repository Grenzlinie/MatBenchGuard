# DFT Electronic Structure Analysis for a Layered Superconductor

## Problem background
Superconducting layered carbide halides such as Y₂Br₂C₂ pose a challenge to conventional electron‑phonon pairing mechanisms. One hypothesis suggests that quasi‑molecular states derived from the C₂ units may hybridise with metal d orbitals near the Fermi level, potentially giving rise to features such as a flat band or a van Hove singularity that would enhance the density of states at Eₚ. A first‑principles electronic structure calculation on Y₂Br₂C₂ offers a direct test of this picture by determining the Fermi‑level density of states, the character of the bands crossing Eₚ, and whether any band exhibits a saddle point.

## Approach
The electronic structure will be calculated with density-functional theory (DFT), using a plane-wave pseudopotential code (LDA or GGA) and the experimentally determined crystal structure of Y₂Br₂C₂ (monoclinic C2/m). A self-consistent calculation provides the converged charge density; from this the band structure along a suitable high-symmetry k‑path (determined from the crystal symmetry, e.g., using a tool like SeeK-path) and the total density of states (DOS) are obtained. The bands crossing the Fermi level are then inspected: their orbital character and dispersion are determined. The analysis will reveal whether any band exhibits a saddle point near Eₚ and what its predominant orbital character is. The orbital character of the flat band is determined from the electronic wavefunction projection, and its dispersion near Γ is examined to assess whether a saddle point is present at Eₚ. The computational tools (a plane-wave DFT code and standard pseudopotentials) are publicly available. To ensure reproducibility, concrete convergence parameters are specified in the workflow steps.

## Reproduction target
Using the DFT output, compute:

1. **dos_at_ef** – the total density of states at the Fermi level, in units of states/eV per spin.
2. **saddle_point_present** – a boolean indicating whether the flat band exhibits a saddle point at Eₚ.
3. **flat_band_character** – a string describing the predominant orbital character of that flat band.
4. **k_path_description** – a string describing the high‑symmetry k‑point path used in the calculation.

Write these four items into a single JSON file at `/app/outputs/electronic_structure_results.json` following the schema described in the output contract. No other output is required for scoring.

## Assets

- Crystal structure of Y₂Br₂C₂
- Plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Standard pseudopotentials

## Workflow steps

### Step 1: Self-consistent DFT calculation
- Role: process
- Action: Perform a self-consistent DFT calculation using a plane-wave pseudopotential code (LDA or GGA) for the Y₂Br₂C₂ crystal structure (monoclinic C2/m, a=695.3 pm, b=376.4 pm, c=993.8 pm, β=99.98°, atomic positions: Y(0.4040,0,0.1485), Br(0.7901,0,0.3333), C(0.0861,0,0.0361)). Obtain the converged electronic charge density and the band structure along a high‑symmetry k‑path that you determine from the crystal symmetry (e.g., by using a tool like SeeK-path or by identifying the path from the literature). Use the following convergence guidelines to approach the reference results:
  - Plane‑wave kinetic energy cut‑off: at least 40 Ry (with a charge density cut‑off of 320 Ry if ultrasoft pseudopotentials are employed).
  - Monkhorst‑Pack k‑point grid for self‑consistency: at least 4×4×2; for the DOS calculation use a finer grid (e.g., 8×8×4).
  - Smearing method: Gaussian or Marzari‑Vanderbilt smearing of ≈0.01 Ry.
  - Check convergence of the total energy and the DOS at the Fermi level with respect to the cut‑off and k‑point grid; increase parameters if the value is not stable to within 0.1 eV⁻¹ Spin⁻¹.
- Evidence: (none required for scoring)

### Step 2: Extract electronic structure results
- Role: scored (load-bearing)
- Action: From the self-consistent DFT output, compute the total density of states (DOS) and extract its value at the Fermi level (dos_at_ef, in states/eV/spin). Identify the bands crossing E_F; determine their orbital character and dispersion. Identify the band that is relatively flat; examine whether it exhibits a saddle point near Γ and report as a boolean. Report the predominant orbital character of that flat band (flat_band_character) and the high‑symmetry k‑path actually used (k_path_description). Write the results to electronic_structure_results.json.
- Output file: `/app/outputs/electronic_structure_results.json`
- Format: json
- Contract: {"dos_at_ef": <float, states/eV/spin>, "saddle_point_present": <boolean>, "flat_band_character": <string>, "k_path_description": <string>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_structure_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_structure_results.json
- path: `/app/outputs/electronic_structure_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed total density of states at the Fermi level, whether the flat band exhibits a saddle point, its orbital character, and the high‑symmetry k‑path used.
- schema:
  - `type`: object
  - `required`:
    - `dos_at_ef`: float (states/eV/spin)
    - `saddle_point_present`: boolean
    - `flat_band_character`: string describing the orbital character of the flat band
    - `k_path_description`: string describing the k‑point path used in the calculation

Notes: The scoring exact‑match policy applies with hidden tolerances; dos_at_ef is compared to the paper‑reported reference value within an absolute tolerance. The verifier checks saddle_point_present, flat_band_character, and k_path_description against the expected results from the band structure analysis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "dos_at_ef": "float (states/eV/spin)",
          "saddle_point_present": "boolean",
          "flat_band_character": "string describing the orbital character of the flat band",
          "k_path_description": "string describing the k‑point path used in the calculation"
        }
      },
      "description": "The computed total density of states at the Fermi level, whether the flat band exhibits a saddle point, its orbital character, and the high‑symmetry k‑path used."
    }
  ],
  "notes": "The scoring exact‑match policy applies with hidden tolerances; dos_at_ef is compared to the paper‑reported reference value within an absolute tolerance. The verifier checks saddle_point_present, flat_band_character, and k_path_description against the expected results from the band structure analysis."
}
```

## How you are scored
A hidden verifier will read your `electronic_structure_results.json`. It compares each field:

- **dos_at_ef** is compared to a reference value using an absolute tolerance that accounts for computational variability between DFT codes.
- **saddle_point_present** is compared to the expected boolean value from the band structure analysis.
- **flat_band_character** is checked against the expected orbital character description.
- **k_path_description** is checked against the high-symmetry path used in the calculation.

These checks are combined with predetermined weights (the load-bearing scored step carries the majority of the reward) into a final reward between 0 and 1. Simply reporting guessed numbers without performing a genuine DFT calculation will not pass the verifier, because the tolerance and character checks are designed for results that come from an actual electronic structure calculation.