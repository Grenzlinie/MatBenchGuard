# PBE Band Gap of Ordered BaGe8As14 Sodalite Structure

## Problem background
BaGe₈As₁₄ is a newly reported semiconducting sodalite-type cage compound. The electronic band gap and its direct/indirect character determine its potential as a thermoelectric material. Density functional theory (DFT) with the PBE functional can be used to calculate the band structure from the experimentally determined crystal structure, and reproducing this calculation is a critical step in validating the theoretical picture.

## Approach
The workflow constructs an ordered structural model from the experimental crystal structure (CCDC 2015241) to resolve site disorder and produce a unit cell suitable for band structure calculations. Then, using a plane-wave pseudopotential DFT code (such as Quantum ESPRESSO) with standard PBE pseudopotentials, a self-consistent field calculation and a band structure calculation along a high-symmetry k-path are performed. From the resulting electronic bands, the minimum band gap, its direct/indirect classification, and the k-points of the valence band maximum and conduction band minimum are extracted.

## Reproduction target
Produce a JSON file (`band_gap_results.json`) containing: the minimum band gap (in eV), the direct gap at the VBM k-point, a boolean flag indicating whether the gap is indirect, and the fractional k-point coordinates of the VBM and CBM. The calculation must be based solely on the ordered P-43m structural model derived from CCDC 2015241.

## Assets

- Experimental crystal structure of BaGe8As14 (CCDC 2015241): https://www.ccdc.cam.ac.uk/structures/
- Plane-wave DFT code (Quantum ESPRESSO or equivalent): https://www.quantum-espresso.org
- PBE pseudopotentials for Ba, Ge, As: SSSP or PSLibrary

## Workflow steps

### Step 1: Construct ordered structural model in P-43m
- Role: process
- Action: Retrieve the experimental CIF (CCDC 2015241) of BaGe8As14 (space group I-43m) and build an ordered structural model in space group P-43m suitable for DFT. Resolve the mixed Ge/As occupancy and Ba disorder as described in the paper, producing a crystal structure file that can be used as input for a band structure calculation.
- Evidence: `/app/outputs/ordered_structure.cif`

### Step 2: DFT PBE band structure and band gap
- Role: scored (load-bearing)
- Action: Using a plane-wave DFT code with the PBE functional and standard pseudopotentials, perform a self-consistent field calculation on the ordered P-43m model and compute the electronic band structure along a k-path that includes the Brillouin zone points where the valence band maximum and conduction band minimum are expected. Extract the global minimum band gap, its direct/indirect character, and the fractional k-point coordinates of the VBM and CBM. Output the results as described in the output schema.
- Output file: `/app/outputs/band_gap_results.json`
- Format: json
- Contract: {"gap_min": float (eV), "direct_gap": float (eV), "indirect_gap": bool, "vbm_kpoint": [float, float, float], "cbm_kpoint": [float, float, float]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_results.json
- path: `/app/outputs/band_gap_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Minimum band gap (indirect), direct gap at the VBM k-point, a flag stating whether the gap is indirect, and the k-points of the VBM and CBM.
- schema:
  - `type`: object
  - `required`:
    - `gap_min`: number (eV)
    - `direct_gap`: number (eV)
    - `indirect_gap`: boolean
    - `vbm_kpoint`: array of 3 numbers (crystal coordinates)
    - `cbm_kpoint`: array of 3 numbers (crystal coordinates)

Notes: The hidden checker compares gap_min to the paper's PBE value within a tolerance window and verifies that indirect_gap is true (VBM and CBM at different k-points). The k-point lists are checked for structural consistency but are not scored numerically beyond that.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gap_min": "number (eV)",
          "direct_gap": "number (eV)",
          "indirect_gap": "boolean",
          "vbm_kpoint": "array of 3 numbers (crystal coordinates)",
          "cbm_kpoint": "array of 3 numbers (crystal coordinates)"
        }
      },
      "description": "Minimum band gap (indirect), direct gap at the VBM k-point, a flag stating whether the gap is indirect, and the k-points of the VBM and CBM."
    }
  ],
  "notes": "The hidden checker compares gap_min to the paper's PBE value within a tolerance window and verifies that indirect_gap is true (VBM and CBM at different k-points). The k-point lists are checked for structural consistency but are not scored numerically beyond that."
}
```

## How you are scored
Your submitted `band_gap_results.json` is inspected by a hidden verifier. The verifier compares your reported gap_min and indirect_gap to a reference that represents the expected outcome of a correct DFT-PBE calculation for this system, with a tolerance that accounts for typical differences between DFT implementations and pseudopotentials. The score is higher the closer your values are to the expected outcome; a completely wrong gap or misclassification of the gap type will yield a low score. The construction of the ordered model (`ordered_structure.cif`) is a required process step but is not scored directly—the correctness of the band gap implicitly depends on it. The final reward is determined solely by the verifier's assessment of the band gap output.
