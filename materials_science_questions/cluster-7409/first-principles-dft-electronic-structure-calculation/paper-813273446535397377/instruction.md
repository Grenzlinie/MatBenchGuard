# Local octahedral rotation near oxygen vacancy in perovskite oxide

## Problem background
Perovskite SrTiO3 exhibits a rich variety of phenomena that are intimately linked to oxygen vacancies. Understanding the atomistic and electronic structure of an isolated oxygen vacancy is essential, yet earlier theoretical descriptions did not account for local structural distortions. This task investigates whether an oxygen vacancy induces a local oxygen-octahedron rotation in an otherwise cubic SrTiO3 lattice, analogous to the anti-ferrodistortive rotation seen in its low-temperature tetragonal phase. The goal is to compute, through first-principles simulation, the maximum rotation angles near the vacancy and verify that octahedra far from the vacancy remain unrotated, thereby quantifying the proposed local rotation effect.

## Approach
The core idea is that a local oxygen-octahedron rotation can be energetically favorable around an oxygen vacancy even when the bulk lattice is expanded to stabilize the cubic phase. To test this, a 320-atom supercell is constructed in the oxygen-octahedron rotated structure (ORS) with a lattice constant a = 4.06 Å and an initial rotation angle θ = 6.5° about the c-axis. Two symmetry-distinct neutral vacancy sites are studied: V_Ra (oxygen displaced by the rotation) and V_Rc (oxygen on the rotation axis). Full structural relaxation is performed for each supercell using the HSE06 hybrid density functional with Γ‑only k‑point sampling until all forces are below 0.05 eV/Å. After relaxation, the oxygen-octahedron rotation angle is computed for every TiO6 octahedron. The maximum rotation angle among octahedra near the vacancy is extracted for each vacancy type, together with the average rotation angle of octahedra far from the vacancy to confirm that the long-range structure remains cubic.

## Reproduction target
Construct a 320-atom SrTiO3 supercell in the oxygen-octahedron rotated structure (ORS) with the prescribed lattice constant and initial rotation. Introduce a single neutral oxygen vacancy at the V_Ra site and, separately, at the V_Rc site. Carry out a full HSE06 relaxation of each supercell until forces on all atoms are below 0.05 eV/Å. For each relaxed structure, calculate the oxygen-octahedron rotation angle for every TiO6 octahedron and report: the maximum rotation angle among octahedra near the V_Ra vacancy, the maximum rotation angle among octahedra near the V_Rc vacancy, and the average rotation angle of octahedra far from the vacancy. Write these three values to the JSON file `rotation_angles.json` in the `/app/outputs` directory with the keys `V_Ra_max_theta`, `V_Rc_max_theta`, and `far_theta_avg` (all in degrees).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build ORS supercell and vacancy models
- Role: process
- Action: Construct a 320‑atom SrTiO3 supercell in the oxygen‑octahedron rotated structure (ORS) with lattice constant a = 4.06 Å and initial rotation angle θ = 6.5° about the c‑axis. Create two supercell structure files: one containing a neutral oxygen vacancy at the V_Ra site (oxygen displaced by the rotation) and one containing a neutral oxygen vacancy at the V_Rc site (oxygen on the rotation axis).
- Evidence: `/app/outputs/supercell_structures.bundle`

### Step 2: HSE06 relaxation and rotation analysis
- Role: scored (load-bearing)
- Action: Perform full structural relaxation (forces < 0.05 eV/Å) of the V_Ra and V_Rc supercells using the HSE06 hybrid functional with Γ‑only k‑point sampling. After relaxation, compute the oxygen‑octahedron rotation angle θ for each TiO6 octahedron. Extract the maximum θ among octahedra near the vacancy for V_Ra (V_Ra_max_theta), the maximum θ near the vacancy for V_Rc (V_Rc_max_theta), and the average θ of octahedra far from the vacancy (far_theta_avg).
- Output file: `/app/outputs/rotation_angles.json`
- Format: json
- Contract: object with keys V_Ra_max_theta (float, degrees), V_Rc_max_theta (float, degrees), far_theta_avg (float, degrees)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rotation_angles.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rotation_angles.json
- path: `/app/outputs/rotation_angles.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum local octahedron rotation angles near the oxygen vacancy for the V_Ra and V_Rc species, the average rotation angle of octahedra far from the vacancy, and the GGA+U-calculated localized in‑gap state energies for V_Ra and V_Rc relative to the CBM. The checker compares all values to the paper’s reported values (with tolerance) and verifies that the far‑field remains unrotated (θ≈0°).
- schema:
  - `type`: object
  - `required`:
    - `V_Ra_max_theta`: number (degrees)
    - `V_Rc_max_theta`: number (degrees)
    - `far_theta_avg`: number (degrees)
    - `V_Ra_E_gap`: number (eV below CBM)
    - `V_Rc_E_gap`: number (eV below CBM)

Notes: The hidden grading uses result‑level comparison (T0): the agent’s reported values are compared to the paper’s numbers within generous tolerances. No raw structural data are required from the agent; only the listed fields in the specified JSON format.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rotation_angles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V_Ra_max_theta": "number (degrees)",
          "V_Rc_max_theta": "number (degrees)",
          "far_theta_avg": "number (degrees)",
          "V_Ra_E_gap": "number (eV below CBM)",
          "V_Rc_E_gap": "number (eV below CBM)"
        }
      },
      "description": "Maximum local octahedron rotation angles near the oxygen vacancy for the V_Ra and V_Rc species, the average rotation angle of octahedra far from the vacancy, and the GGA+U-calculated localized in‑gap state energies for V_Ra and V_Rc relative to the CBM. The checker compares all values to the paper’s reported values (with tolerance) and verifies that the far‑field remains unrotated (θ≈0°)."
    }
  ],
  "notes": "The hidden grading uses result‑level comparison (T0): the agent’s reported values are compared to the paper’s numbers within generous tolerances. No raw structural data are required from the agent; only the listed fields in the specified JSON format."
}
```

## How you are scored
Your submission is automatically evaluated by a hidden verifier that reads the output file `rotation_angles.json` and compares the three reported angles to scientifically expected ranges. The verifier checks that the maximum rotation near each vacancy falls within plausible bounds and that the far-field average is consistent with negligible rotation. It also verifies the file format and that all required keys are present. The overall score is a weighted combination of the individual checks; a high score requires a faithful execution of the simulation pipeline producing physically meaningful rotation angles. Simply hardcoding or guessing numbers without performing the required computation will not yield a valid reward.
