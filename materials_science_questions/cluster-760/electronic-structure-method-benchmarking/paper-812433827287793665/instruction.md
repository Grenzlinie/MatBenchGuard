# Conformational analysis and NMR chemical shift calculation of bicyclo[3.3.1]nonan-9-one

## Problem background
Bicyclo[3.3.1]nonan-9-one (BNO) exhibits conformational flexibility, with three possible conformers: twin‑chair (CC), boat‑chair (BC), and twisted twin‑boat (BB). The relative stability and structural features of these conformers are critical for understanding whether BNO can exhibit orientational disorder in the solid state. Quantum chemical calculations can predict the free energy difference between the CC and BC forms, quantify intramolecular strain (e.g., endo‑hydrogen repulsion distances in the CC conformer), and provide spectroscopic signatures via 13C nuclear magnetic resonance (NMR) chemical shifts. Reproducing these quantities using an open‑source quantum chemistry package validates the computational protocol and provides insight into the molecule’s conformational landscape.

## Approach
The reproduction is carried out with density functional theory (DFT) and ab initio methods implemented in an open‑source quantum chemistry package (e.g., Psi4). Initial three‑dimensional structures of the CC, BC, and BB conformers are constructed using a molecular builder or chemical knowledge. Full geometry optimizations are then performed at the B3LYP level with a triple‑zeta basis set including diffuse and polarization functions on all heavy atoms. To confirm that each optimized structure is a genuine minimum and to obtain thermal corrections, harmonic vibrational frequency calculations are run at the same level of theory, yielding the Gibbs free energy at 298.15 K. From these energies the free energy difference between the BC and CC conformers is computed. For the optimized CC conformer, the non‑bonded distance between the two endo hydrogens is extracted, providing a measure of steric strain. Finally, the isotropic 13C NMR chemical shift of the carbonyl carbon (C9) is calculated using the gauge‑independent atomic orbital (GIAO) method with a larger, augmented basis set, evaluated on the B3LYP‑optimized CC geometry. All calculations are performed with an open‑source replacement for the commercial Gaussian 98 package originally used in the published study.

## Reproduction target
Using an open‑source quantum chemistry package (e.g., Psi4) and a molecule builder (e.g., RDKit), construct the CC and BC conformers of bicyclo[3.3.1]nonan‑9‑one. Optimize both conformers at the B3LYP/6‑311+G(d) level, perform vibrational frequency calculations to confirm they are local minima, and obtain the Gibbs free energy at 298.15 K for each. Compute ΔG1 = G(BC) – G(CC) in kcal/mol. From the optimized CC conformer, extract the intramolecular distance between the endo hydrogens H31 and H71 (in Å). Then, using the optimized CC geometry, run a single‑point GIAO NMR calculation at the B3LYP/6‑311+G(2d,2p) level and report the isotropic 13C chemical shift of the carbonyl carbon C9 (in ppm). Round all three values to three decimal places and write them as a JSON object with keys "delta_G1_BNO", "H31_H71_distance_BNO_CC", and "chemical_shift_C9_BNO_CC" to the file `/app/outputs/results.json`.

## Assets

- Psi4 (open-source quantum chemistry package): https://psicode.org
- RDKit: conda install -c conda-forge rdkit
- Open Babel: conda install -c conda-forge openbabel

## Workflow steps

### Step 1: Build initial geometries of BNO conformers (CC, BC, BB)
- Role: process
- Action: Using a molecular builder (e.g., RDKit) or chemical knowledge, generate initial 3D coordinates for the twin-chair (CC), boat-chair (BC), and twisted twin-boat (BB) conformers of bicyclo[3.3.1]nonan-9-one. The bicyclo[3.3.1]nonane skeleton consists of two fused cyclohexane rings sharing the bridgehead carbons (C1 and C5) and the carbonyl carbon C9 (the ketone oxygen is bonded to C9). C3 and C7 are the central carbons of the two three-carbon bridges, each bearing two hydrogen atoms. The endo hydrogens on C3 and C7 — those directed inward across the molecular cavity — are labeled H31 and H71; they are the hydrogens that approach closest to each other in the CC conformer. In all subsequent calculations, consistently label the carbonyl carbon as C9, the endo hydrogen on C3 as H31, and the endo hydrogen on C7 as H71.
- Evidence: `/app/outputs/initial_conformers.xyz`

### Step 2: Geometry optimization at B3LYP/6-311+G(d)
- Role: process
- Action: Perform full geometry optimizations of the CC, BC, and BB conformers using the B3LYP functional and the 6-311+G(d) basis set. Save the optimized Cartesian coordinates and total energies for each conformer.
- Evidence: `/app/outputs/optimized_geometries.log`

### Step 3: Vibrational frequency analysis and thermochemistry
- Role: process
- Action: Run harmonic vibrational frequency calculations at the same B3LYP/6-311+G(d) level on each optimized conformer. Confirm that all conformers have zero imaginary frequencies (local minima). From the frequency output, extract the Gibbs free energy at 298.15 K for each conformer.
- Evidence: `/app/outputs/frequency_output.log`

### Step 4: Compute scored quantities and write results.json
- Role: scored (load-bearing)
- Action: From the thermochemistry of CC and BC, compute ΔG1 = G(BC) – G(CC) in kcal/mol. From the optimized CC conformer geometry, measure the distance between the two endo hydrogens H31 and H71 (in Å). Using the optimized CC geometry, perform a single-point GIAO NMR calculation at the B3LYP/6-311+G(2d,2p) level and report the isotropic 13C chemical shift of the carbonyl carbon C9 (in ppm). Round all values to three decimal places. Write a JSON object with keys "delta_G1_BNO", "H31_H71_distance_BNO_CC", and "chemical_shift_C9_BNO_CC" to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"delta_G1_BNO": "number (kcal/mol)", "H31_H71_distance_BNO_CC": "number (Å)", "chemical_shift_C9_BNO_CC": "number (ppm)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Three key numerical quantities reproduced from the paper's BNO calculations: the free energy difference between BC and CC conformers, the H31…H71 distance in the CC conformer, and the isotropic 13C chemical shift of C9.
- schema:
  - `type`: object
  - `required`:
    - `delta_G1_BNO`: number (kcal/mol)
    - `H31_H71_distance_BNO_CC`: number (Å)
    - `chemical_shift_C9_BNO_CC`: number (ppm)

Notes: The solving agent must use an open-source quantum chemistry package (e.g., Psi4). The BB conformer is built and optimized but its results are not scored; it is included to follow the full computational protocol of the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_G1_BNO": "number (kcal/mol)",
          "H31_H71_distance_BNO_CC": "number (Å)",
          "chemical_shift_C9_BNO_CC": "number (ppm)"
        }
      },
      "description": "Three key numerical quantities reproduced from the paper's BNO calculations: the free energy difference between BC and CC conformers, the H31…H71 distance in the CC conformer, and the isotropic 13C chemical shift of C9."
    }
  ],
  "notes": "The solving agent must use an open-source quantum chemistry package (e.g., Psi4). The BB conformer is built and optimized but its results are not scored; it is included to follow the full computational protocol of the paper."
}
```

## How you are scored
Your submitted `/app/outputs/results.json` is automatically evaluated by a hidden verifier. The verifier compares each of the three numeric values (ΔG1, H31···H71 distance, and 13C chemical shift of C9) against a set of hidden reference values, using tolerances appropriate for an open‑source quantum chemistry implementation. You receive a score between 0.0 and 1.0: each value that falls within the tolerance contributes proportionally to the total score. To obtain a perfect score, all three values must be computed correctly. Reproducing the entire workflow, from initial geometry building to the final single‑point NMR calculation, is necessary to achieve the required accuracy.
