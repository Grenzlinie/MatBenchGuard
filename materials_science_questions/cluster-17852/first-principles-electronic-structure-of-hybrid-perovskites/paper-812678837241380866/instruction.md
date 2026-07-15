# DFT Band Gaps of Chiral MBA Perovskites

## Problem background
Hybrid organic-inorganic lead halide perovskites that incorporate chiral organic cations can exhibit circular dichroism and circularly polarized luminescence. A prerequisite for interpreting and designing such chiral optoelectronic materials is understanding their electronic band structure—in particular the magnitude of the fundamental band gap and whether the gap is direct or indirect. Density functional theory (DFT) calculations using the PBE functional, performed on the experimentally determined crystal structures, provide a standard computational route to these quantities. In this task we extract the DFT band structure substudy of a set of chiral methylbenzylamine (MBA) perovskites. The goal is to compute, from first principles, the PBE band gaps and band-gap type (direct/indirect) for three single-crystal perovskite compounds: (R)-MBAPbBr₃, (R)-MBAPbI₃, and (R)-MBA₂PbI₄. The band gap and gap type are essential electronic descriptors that remain an open quantity to compute from the provided crystal structures.

## Approach
First-principles plane-wave DFT calculations using the PBE exchange-correlation functional. The crystal structures of the three perovskite compounds (obtained from the Cambridge Crystallographic Data Centre, deposition numbers 1877049–1877055) are taken as static input—no structural relaxation is performed. A standard open-source DFT code (Quantum ESPRESSO) is used to compute the Kohn-Sham band structure for each compound in its primitive unit cell. From the band structure the valence band maximum (VBM) and conduction band minimum (CBM) are identified, and the band gap is determined as the difference between the CBM and VBM. The gap type is assigned by comparing the k-point coordinates of the VBM and CBM: if they occur at the same k-point the gap is direct, otherwise it is indirect. The computational workflow processes the three compounds independently and collects the resulting band gaps and types into a single tabular output.

## Reproduction target
1. Obtain the experimental crystal structures (CIF files) for (R)-MBAPbBr₃, (R)-MBAPbI₃, and (R)-MBA₂PbI₄ from the CCDC using deposit numbers 1877049–1877055.
2. For each compound, set up and run a PBE DFT band-structure calculation with Quantum ESPRESSO (no structural relaxation).
3. Extract the valence band maximum, conduction band minimum, and determine the band gap (eV) and whether the gap is direct or indirect.
4. Compile the results into a CSV file `/app/outputs/band_gaps.csv` with columns: `compound_name` (string), `band_gap_eV` (float, in eV), and `band_gap_type` (string, either "direct" or "indirect"). The file must contain one row for each of the three compounds.

## Assets

- Crystal structures of chiral MBA perovskites: https://www.ccdc.cam.ac.uk/structures/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotential library (SSSP): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT band structure calculation
- Role: process
- Action: Set up and run PBE DFT band-structure calculations with Quantum ESPRESSO for (R)-MBAPbBr₃, (R)-MBAPbI₃, and (R)-MBA₂PbI₄ using the CCDC crystal structures. Determine the valence band maximum (VBM), conduction band minimum (CBM), and whether the VBM and CBM occur at the same k-point (direct) or different k-points (indirect).
- Evidence: `/app/outputs/dft_outputs.log`

### Step 2: Compile band gaps and types
- Role: scored (load-bearing)
- Action: Write a CSV file with columns compound_name, band_gap_eV, band_gap_type that contains the computed band gap (eV) and gap type (direct or indirect) for each of the three compounds.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: compound_name:string,band_gap_eV:float,band_gap_type:string
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: PBE band gaps and gap type (direct/indirect) for (R)-MBAPbBr₃, (R)-MBAPbI₃, and (R)-MBA₂PbI₄.
- schema:
  - `type`: table
  - `required_columns`: `compound_name`, `band_gap_eV`, `band_gap_type`
  - `units`:
    - `band_gap_eV`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound_name",
          "band_gap_eV",
          "band_gap_type"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "PBE band gaps and gap type (direct/indirect) for (R)-MBAPbBr₃, (R)-MBAPbI₃, and (R)-MBA₂PbI₄."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that operates on your produced artifacts. The verifier reads `/app/outputs/band_gaps.csv` and compares the reported band gap and gap type for each of the three compounds against independently stored reference values. The comparison uses an appropriate numerical tolerance for the band gap and exact string matching for the gap type. A correct result for a compound requires both the band gap and the gap type to be correct; each compound contributes equally to the final score. The overall reward is a weighted combination of the per-compound scores, reported as a single float in [0,1]. Important: simply copying or reporting numbers from any external source (including the original publication) without genuinely executing the DFT workflow will not be detected by shape checks, but such fabricated results are unlikely to match the verifier's hidden reference values; the reward scales with the accuracy of your actual computations.
