# HSE06 Band Gap Calculation for LaB3C3 Clathrate

## Problem background
LaB₃C₃ is a lanthanum-filled carbon–boron clathrate that crystallizes in the cubic bipartite sodalite structure (Type‑VII clathrate). In this framework, La atoms are encapsulated within truncated octahedral cages built from alternating boron and carbon atoms. The balanced electron count between the trivalent La³⁺ guest and the [B₃C₃]³⁻ host framework suggests that this material may be a semiconductor, with the electronic states determined by the covalent B–C bonds and the La d orbitals. First‑principles electronic structure calculations can predict whether this compound has an indirect band gap and its magnitude. The objective of this task is to compute the HSE06 hybrid functional band gap and identify the k‑point locations of the valence band maximum and conduction band minimum.

## Approach
The electronic structure of LaB₃C₃ is investigated with density functional theory (DFT). The workflow begins with the published crystal structure, which is first relaxed to its equilibrium geometry. A full relaxation of atomic positions and cell parameters is performed using the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation. Using the relaxed structure, the electronic band structure is computed with the Heyd–Scuseria–Ernzerhof (HSE06) screened hybrid functional, which provides a more accurate description of the band gap for semiconductors. The band structure is evaluated along a standard high‑symmetry k‑point path for the cubic space group Pm 3̅n, connecting the Γ, X, M, R, and L points. From this band structure the valence band maximum (VBM) and conduction band minimum (CBM) are identified, and the indirect band gap — the minimum energy difference between VBM and CBM at different k‑points — is determined. The result is reported in eV together with the fractional k‑point coordinates of the VBM and CBM.

## Reproduction target
Produce a JSON file `/app/outputs/band_gap_result.json` with exactly the following three fields:
- `indirect_gap_ev`: the indirect HSE06 band gap of LaB₃C₃ (in eV).
- `vbm_kpoint`: a list `[x, y, z]` of the fractional coordinates of the k‑point where the valence band maximum is located.
- `cbm_kpoint`: a list `[x, y, z]` of the fractional coordinates of the k‑point where the conduction band minimum is located.

To obtain these values you must:
1. Retrieve the LaB₃C₃ crystal structure (CCDC deposition 2010831) and convert it into a suitable input file for your chosen DFT code.
2. Perform a full geometry relaxation (atomic positions and cell parameters) using DFT with the PBE functional and an appropriate pseudopotential set. Log the relaxation run.
3. Using the relaxed structure, perform an HSE06 band structure calculation along the high‑symmetry k‑point path for the cubic Pm 3̅n space group that includes Γ, X, M, R, and L points. Identify the indirect gap and the VBM/CBM k‑point positions from the computed band structure.

The final `band_gap_result.json` must reflect the HSE06 results obtained on the relaxed geometry.

## Assets

- CCDC deposition 2010831 (LaB3C3 crystal structure): https://www.ccdc.cam.ac.uk/structures/
- DFT code with HSE06 support: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Obtain crystal structure
- Role: process
- Action: Download the CIF file for LaB3C3 from CCDC deposition 2010831 and convert it to a suitable input file for the chosen DFT code.
- Evidence: `/app/outputs/crystal_structure.cif`

### Step 2: DFT geometry relaxation
- Role: process
- Action: Perform a full relaxation of atomic positions and cell parameters using DFT (PBE functional) with appropriate pseudopotentials and k-point sampling. Symmetry may be fixed during relaxation.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: HSE06 band structure and band gap
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, compute the electronic band structure with the HSE06 hybrid functional along a standard high-symmetry path for cubic Pm-3n (including Γ, X, M, R, L). Identify the valence band maximum (VBM) and conduction band minimum (CBM), determine the indirect band gap, and save the results.
- Output file: `/app/outputs/band_gap_result.json`
- Format: json
- Contract: {"indirect_gap_ev": float, "vbm_kpoint": [x, y, z], "cbm_kpoint": [x, y, z]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_result.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_result.json
- path: `/app/outputs/band_gap_result.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed indirect band gap and the k-point positions of the valence band maximum and conduction band minimum.
- schema:
  - `type`: object
  - `required`:
    - `indirect_gap_ev`: number
    - `vbm_kpoint`: array
    - `cbm_kpoint`: array
  - `units`:
    - `indirect_gap_ev`: eV
    - `vbm_kpoint`: fractional coordinates of VBM
    - `cbm_kpoint`: fractional coordinates of CBM

Notes: The solver must report the indirectly determined band gap and VBM/CBM positions. The hidden checker compares these values to expected reference results with an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "indirect_gap_ev": "number",
          "vbm_kpoint": "array",
          "cbm_kpoint": "array"
        },
        "units": {
          "indirect_gap_ev": "eV",
          "vbm_kpoint": "fractional coordinates of VBM",
          "cbm_kpoint": "fractional coordinates of CBM"
        }
      },
      "description": "Computed indirect band gap and the k-point positions of the valence band maximum and conduction band minimum."
    }
  ],
  "notes": "The solver must report the indirectly determined band gap and VBM/CBM positions. The hidden checker compares these values to expected reference results with an appropriate tolerance."
}
```

## How you are scored
Your solution is evaluated by a hidden automated verifier. For the scored step (HSE06 band structure and band gap), the verifier reads your `band_gap_result.json` and compares the reported indirect gap and VBM/CBM positions against reference results. The comparison uses a tolerance that accommodates legitimate differences between DFT codes, pseudopotentials, and calculation settings, while ensuring that the computation was performed correctly. If your reported values fall within the tolerance, you receive full credit; larger deviations result in partial or no credit. The two preceding non‑scored steps (obtaining the crystal structure and running the geometry relaxation) are required and the verifier checks that the expected evidence files (`crystal_structure.cif` and `relaxation.log`) exist, but they do not directly contribute to the reward. The final reward is based solely on the scored artifact.
