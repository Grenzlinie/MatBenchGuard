# DFT band gaps of pristine and defective ZnO polymorphs

## Problem background
Zinc oxide (ZnO) in its ambient wurtzite phase is a wide-band-gap semiconductor (~3.1–3.4 eV), limiting its photocatalytic activity to ultraviolet light. There is strong interest in narrowing its band gap so that it can absorb visible light as well. One avenue is to stabilize the high-pressure rocksalt polymorph of ZnO, either pure or with point defects such as oxygen vacancies. First-principles density functional theory (DFT) calculations can predict the band gaps of these structural variants and reveal how phase and defects each contribute to gap reduction. In this task you will compute the band gaps of ZnO in four distinct configurations using spin-polarized hybrid-functional DFT.

## Approach
Use an open-source periodic DFT code (Quantum ESPRESSO) with a hybrid exchange-correlation functional (e.g., PBE0 or HSE06). Build unit cells for both wurtzite and rocksalt ZnO using known experimental lattice constants, relax the internal coordinates, then construct 2×2×2 (wurtzite) and 2×2×1 (rocksalt) supercells containing 16 Zn and 16 O atoms. To model the effect of oxygen vacancies, remove one oxygen atom and place a ghost basis function at that site, creating a vacancy concentration of 6.25 at.%. Run spin-polarized single-point calculations on four models: pristine wurtzite, vacancy-containing wurtzite, pristine rocksalt, and vacancy-containing rocksalt. From the resulting density of states (DOS), extract the band gap as the energy difference between the valence band maximum and the conduction band minimum.

## Reproduction target
Perform the DFT calculations and report the band gaps (in eV) for the four ZnO configurations in a single JSON file. The file must contain exactly the following four fields: 'ideal_wurtzite', 'wurtzite_vacancy', 'ideal_rocksalt', 'rocksalt_vacancy', each a floating-point number. Write the file as `/app/outputs/band_gaps.json`.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE efficiency or similar) for Zn and O: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Prepare initial primitive cells
- Role: process
- Action: Create primitive unit cells for wurtzite ZnO (hexagonal, P63mc) with lattice parameters a=3.25 Å, c=5.21 Å, and for rocksalt ZnO (cubic, Fm-3m) with a=4.28 Å, using the experimental lattice constants from the paper.
- Evidence: `/app/outputs/primitive_cells.xyz`

### Step 2: Geometry relaxation of primitive cells
- Role: process
- Action: Perform spin-polarized DFT geometry optimization of the primitive cells (keeping the lattice vectors fixed) using a hybrid functional (e.g., PBE0 or HSE06) to obtain relaxed internal coordinates. Use Quantum ESPRESSO’s pw.x with appropriate k-point sampling and energy cutoffs.
- Evidence: none

### Step 3: Construct supercells and introduce oxygen vacancies
- Role: process
- Action: Build a 2×2×2 supercell for wurtzite (16 Zn + 16 O atoms) and a 2×2×1 supercell for rocksalt (16 Zn + 16 O atoms) by replicating the relaxed primitive cells. From each supercell, create an oxygen-vacancy model by removing one O atom and placing a ‘ghost’ basis function at that site, yielding four configurations: (1) ideal wurtzite, (2) wurtzite with 6.25 at.% O vacancy, (3) ideal rocksalt, (4) rocksalt with 6.25 at.% O vacancy.
- Evidence: none

### Step 4: Run DFT electronic structure calculations
- Role: process
- Action: For each of the four supercells, perform a spin-polarized DFT single-point calculation using a hybrid functional (PBE0 or HSE06) to compute the total and projected density of states (DOS). Use sufficient k-point mesh and energy cutoffs to converge the electronic structure.
- Evidence: none

### Step 5: Extract band gaps and write result file
- Role: scored (load-bearing)
- Action: For each of the four configurations, determine the band gap from the computed DOS (difference between the valence band maximum and conduction band minimum). Write a JSON file `band_gaps.json` with keys 'ideal_wurtzite', 'wurtzite_vacancy', 'ideal_rocksalt', 'rocksalt_vacancy' and values as the band gap in eV.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: JSON object with four float fields: 'ideal_wurtzite', 'wurtzite_vacancy', 'ideal_rocksalt', 'rocksalt_vacancy'; each value is the band gap in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-calculated band gaps for the four ZnO configurations in eV. The hidden checker compares each value to the paper's reference with an appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `ideal_wurtzite`: number (eV)
    - `wurtzite_vacancy`: number (eV)
    - `ideal_rocksalt`: number (eV)
    - `rocksalt_vacancy`: number (eV)

Notes: Only the band_gaps.json file is scored. The hidden checker uses an absolute tolerance to account for differences between the original CRYSTAL14/B3LYP calculations and the open-source hybrid-DFT approach (Quantum ESPRESSO with PBE0/HSE06).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ideal_wurtzite": "number (eV)",
          "wurtzite_vacancy": "number (eV)",
          "ideal_rocksalt": "number (eV)",
          "rocksalt_vacancy": "number (eV)"
        }
      },
      "description": "DFT-calculated band gaps for the four ZnO configurations in eV. The hidden checker compares each value to the paper's reference with an appropriate tolerance."
    }
  ],
  "notes": "Only the band_gaps.json file is scored. The hidden checker uses an absolute tolerance to account for differences between the original CRYSTAL14/B3LYP calculations and the open-source hybrid-DFT approach (Quantum ESPRESSO with PBE0/HSE06)."
}
```

## How you are scored
Your submitted `band_gaps.json` is the only scored artifact. A hidden verifier reads the file, compares each of the four band gap values to a hidden reference for the corresponding configuration, and awards a fraction of full credit based on how many values fall within an absolute tolerance. You are not told the reference values or the tolerance; they are chosen to accommodate legitimate differences between DFT codes and functionals. The overall reward is the fraction of band gaps that meet the tolerance criterion.
