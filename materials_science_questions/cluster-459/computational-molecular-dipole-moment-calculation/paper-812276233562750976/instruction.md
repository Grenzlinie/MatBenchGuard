# SCEF Conformational Search on Polyalanine

## Problem background
Protein folding is hindered by the multiple-minima problem: an enormous number of local energy minima on the conformational hypersurface prevents conventional energy minimization from locating the native (global minimum) structure. The Self-Consistent Electric Field (SCEF) method attempts to overcome this by iteratively aligning the electric dipole moments of peptide units with the local electrostatic field, using full energy minimization only as a relaxation step. This task tests whether the SCEF procedure can recover the right-handed α-helix of a terminally blocked 19-residue poly(L-alanine) chain when started from a perturbed conformation containing a single backbone defect.

## Approach
The system is CH3CO-(Ala)19-NHCH3, modelled with the ECEPP/2 force field (dielectric constant ε = 2.0). First, build the all-α-helix reference conformation. Introduce a C-type defect at residue 11 by setting its backbone dihedrals to φ = −80°, ψ = 76°, and energy-minimize this structure to the nearest local minimum. Starting from this minimized defected state, run the SCEF loop:
(i) compute the electric field at each peptide unit (due to all charges outside that unit);
(ii) evaluate the electrostatic orientation quality of each unit via a computed energy-gain measure ΔE_i;
(iii) select the peptide unit with the most negative ΔE_i (the worst-oriented);
(iv) solve the geometric alignment equation to find the rotation (a change in ψ or φ) that aligns the unit’s dipole moment with the local field;
(v) apply that diagnostic rotation;
(vi) perform a full ECEPP/2 energy minimization;
(vii) repeat from (i) until the conformation no longer changes.
Record the diagnostic rotation applied in the very first iteration; after convergence, output the final total potential energy.

## Reproduction target
Build and minimize the defected conformation, run the SCEF procedure to convergence, and produce two scored artifacts:
(1) `final_energy.txt` – the total ECEPP/2 potential energy (kcal/mol) of the final self-consistent conformation.
(2) `first_iteration_rotation.json` – the diagnostic rotation applied in the first iteration, with fields `"residue"` (integer), `"dihedral"` (one of `"psi"` or `"phi"`), and `"rotation_degrees"` (float).

## Assets

- ECEPP/2 force field parameters: 10.1021/j100231a033

## Workflow steps

### Step 1: Build the polyalanine chain and ECEPP/2 parameters
- Role: process
- Action: Construct the molecular system for CH3CO-(Ala)19-NHCH3 using the ECEPP/2 force field. Generate a perfect right-handed α-helix reference geometry by setting backbone dihedral angles to standard α-helical values and applying any necessary internal coordinate adjustments.
- Evidence: `/app/outputs/reference_helix.pdb`

### Step 2: Introduce a single C-type defect and energy minimize
- Role: process
- Action: Take the perfect α-helix structure and replace the backbone dihedral angles (φ, ψ) of residue 11 with the C-type conformation. Then perform a full ECEPP/2 energy minimization to reach the nearest local minimum. Keep the minimized coordinates.
- Evidence: `/app/outputs/defect_minimized.pdb`

### Step 3: Run the SCEF procedure to convergence
- Role: process
- Action: Starting from the minimized defected structure, iteratively apply the SCEF procedure: (i) compute electric field vectors at each peptide unit using the ECEPP/2 point charges and ε=2.0; (ii) evaluate the orientation quality of each unit via the energy gain measure ΔE_i; (iii) select the peptide unit with the most negative ΔE_i; (iv) solve the alignment equation to obtain a diagnostic rotation (Δψ or Δφ) for that unit; (v) apply the rotation; (vi) perform full energy minimization; (vii) repeat from (i) until the conformation no longer changes. Record the diagnostic rotation applied in the very first iteration and the final converged conformation's total ECEPP/2 energy.
- Evidence: `/app/outputs/scef_iterations.log`

### Step 4: Output the final ECEPP/2 energy
- Role: scored (load-bearing)
- Action: Write the total ECEPP/2 potential energy (kcal/mol) of the final converged α-helix to the file final_energy.txt as a single floating-point number.
- Output file: `/app/outputs/final_energy.txt`
- Format: txt
- Contract: A single line: <energy (float)>
- Scoring: scored by hidden verifier

### Step 5: Output the first-iteration diagnostic rotation
- Role: scored
- Action: Write the first diagnostic rotation applied during the SCEF run to first_iteration_rotation.json. The JSON object must specify the residue number (integer), the dihedral angle that was changed (one of "psi" or "phi"), and the applied rotation angle in degrees (float).
- Output file: `/app/outputs/first_iteration_rotation.json`
- Format: json
- Contract: {"residue": <int>, "dihedral": "<psi|phi>", "rotation_degrees": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_energy.txt`
- `/app/outputs/first_iteration_rotation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_energy.txt
- path: `/app/outputs/final_energy.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Final total ECEPP/2 potential energy of the converged α-helix. Scoring compares this energy to the paper-reported value (–47 kcal/mol) with a tolerance, accepting any value that meets or exceeds the reference (i.e., is not worse).
- schema:
  - `type`: text
  - `description`: One line containing a single floating-point number representing the total ECEPP/2 energy in kcal/mol.

### first_iteration_rotation.json
- path: `/app/outputs/first_iteration_rotation.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Diagnostic rotation applied in the first SCEF iteration. The rotation_degrees field is compared to the paper's reported value (−120.0°) with a tolerance; values closer to or matching the target score higher.
- schema:
  - `type`: object
  - `required`:
    - `residue`: integer
    - `dihedral`: string (psi or phi)
    - `rotation_degrees`: float

Notes: The scored artifacts are the final potential energy and the first rotation. Both are checked against the paper-reported gold values via threshold_or_better scoring, with tolerances chosen to accommodate minor numerical differences from different implementations or minimizers. The process steps produce supporting artifacts (reference helix, defected structure, iteration log) but they are not scored; only the two listed outputs are used for scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "One line containing a single floating-point number representing the total ECEPP/2 energy in kcal/mol."
      },
      "description": "Final total ECEPP/2 potential energy of the converged α-helix. Scoring compares this energy to the paper-reported value (–47 kcal/mol) with a tolerance, accepting any value that meets or exceeds the reference (i.e., is not worse)."
    },
    {
      "file": "first_iteration_rotation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "residue": "integer",
          "dihedral": "string (psi or phi)",
          "rotation_degrees": "float"
        }
      },
      "description": "Diagnostic rotation applied in the first SCEF iteration. The rotation_degrees field is compared to the paper's reported value (−120.0°) with a tolerance; values closer to or matching the target score higher."
    }
  ],
  "notes": "The scored artifacts are the final potential energy and the first rotation. Both are checked against the paper-reported gold values via threshold_or_better scoring, with tolerances chosen to accommodate minor numerical differences from different implementations or minimizers. The process steps produce supporting artifacts (reference helix, defected structure, iteration log) but they are not scored; only the two listed outputs are used for scoring."
}
```

## How you are scored
A hidden verifier reads your two output files independently. For the final energy, it compares your reported value against a reference value; lower energy is better, and a value at or below the reference earns full credit, with decreasing credit for higher energies. For the diagnostic rotation, the verifier checks how close your rotation angle is to the correct diagnostic rotation; values within a tight tolerance receive full credit, and credit decreases with larger deviations. The overall score is a weighted combination of the two step scores.
