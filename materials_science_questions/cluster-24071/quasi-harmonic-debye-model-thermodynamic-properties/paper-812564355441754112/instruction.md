# DFT elastic dipole tensors and migration-volume tensor for a vacancy in fcc Al

## Problem background
Point defects such as vacancies play a central role in diffusion and mechanical behavior of crystalline solids. In fcc metals, the formation and migration of vacancies are sensitive to the stress state, which affects material properties under load. The key parameters that quantify how a vacancy and its transition state couple to an applied stress are the elastic dipole tensors. These tensors, together with the elastic constants of the host crystal, determine the migration-volume tensor, which governs how the migration barrier changes with stress. Computing these tensors from first principles for aluminum provides a fundamental building block for predicting stress-dependent vacancy behavior.

## Approach
We use first-principles density functional theory (DFT) calculations to obtain the ground-state structure of a perfect fcc aluminum supercell and then introduce a single vacancy and its [110] jump transition state. In each case the atomic positions are relaxed at fixed cell shape and volume, and the residual stress is extracted. Following the Varvenne–Clouet mapping, the residual stress is converted into the elastic dipole tensor for the vacancy and for the transition state. Using the paper’s reported elastic constants for aluminum, we construct the stiffness tensor and its inverse (the compliance tensor), then compute the migration dipole as the difference of the two dipole tensors and finally the migration-volume tensor via contraction with the compliance tensor. All steps up to the final linear algebra are implemented with the open-source DFT code Quantum ESPRESSO and a standard PAW pseudopotential for Al.

## Reproduction target
Produce a JSON file containing the 3×3 elastic dipole tensor for the vacancy, the 3×3 elastic dipole tensor for the [110] transition state, and the 3×3 migration-volume tensor, all computed from a 3×3×3 fcc Al supercell using DFT and the linear elasticity relation. The file must be written to `/app/outputs/computed_tensors.json` with the exact structure described in the output contract. The tensors must be expressed in the conventional cubic frame; dipole components in eV, migration-volume components in Å³.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- PBE PAW pseudopotential for Al (Al.pbe-n-kjpaw_psl.1.0.0.UPF): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax perfect Al supercell
- Role: process
- Action: Construct a 3×3×3 fcc Al supercell (108 atoms) and relax the cell shape and atomic positions using DFT (Quantum ESPRESSO, PBE functional) to obtain the equilibrium lattice parameter and ground-state reference energy. This relaxed perfect cell is the baseline for defect calculations.
- Evidence: `/app/outputs/perfect_relaxation.log`

### Step 2: Compute vacancy elastic dipole tensor
- Role: process
- Action: Remove one Al atom from the relaxed supercell to introduce a single vacancy. Keep the supercell shape and volume fixed at the relaxed perfect-cell values, relax all atomic positions, and compute the residual stress tensor σ^res. Convert σ^res to the elastic dipole tensor P_vac via the Varvenne–Clouet mapping (P_ij = -V * σ^res_ij, corrected for periodic image contributions).
- Evidence: `/app/outputs/vacancy_dipole_calc.log`

### Step 3: Compute transition-state elastic dipole tensor
- Role: process
- Action: Build a supercell with an Al atom at the midpoint of a [110] jump between two vacant sites (i.e., two vacancies and one atom placed halfway between them). Fix the supercell shape and volume. Relax all atomic positions, compute the residual stress tensor, and obtain the transition-state elastic dipole P_ts via the same Varvenne–Clouet conversion.
- Evidence: `/app/outputs/ts_dipole_calc.log`

### Step 4: Compute migration dipole and migration-volume tensor
- Role: process
- Action: Calculate the migration dipole ΔP = P_ts - P_vac. Use the paper's elastic constants for Al (C11=105 GPa, C12=65 GPa, C44=33 GPa) to construct the stiffness tensor C and its inverse, the compliance tensor S. Compute the migration-volume tensor component-wise: ΔV_kl = Σ_{ij} ΔP_ij * S_ijkl. All operations are elementary linear algebra; no additional simulation is needed.
- Evidence: `/app/outputs/migration_computation.log`

### Step 5: Write final computed tensors to JSON
- Role: scored (load-bearing)
- Action: Collect the computed vacancy dipole, transition dipole, and migration-volume tensor (all as 3×3 matrices). Write them to computed_tensors.json in the specified format.
- Output file: `/app/outputs/computed_tensors.json`
- Format: json
- Contract: JSON object with keys "vacancy_dipole", "transition_dipole", "migration_volume_tensor", each a 3×3 matrix of floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_tensors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_tensors.json
- path: `/app/outputs/computed_tensors.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final computed tensors: vacancy elastic dipole P_vac, transition-state elastic dipole P_ts, and migration-volume tensor ΔV. Each is a 3x3 array of floats. The hidden checker compares every component to the paper's reference 3×3×3 supercell values within tolerances; score is fraction of components in agreement.
- schema:
  - `type`: object
  - `required`:
    - `vacancy_dipole`: list of list of float (3x3 matrix)
    - `transition_dipole`: list of list of float (3x3 matrix)
    - `migration_volume_tensor`: list of list of float (3x3 matrix)
  - `units`:
    - `vacancy_dipole`: eV
    - `transition_dipole`: eV
    - `migration_volume_tensor`: Å³

Notes: All DFT calculations must use the 3×3×3 supercell and the specified elastic constants. The solver may use external compute resources; only the final JSON must be placed under /app/outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_tensors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "vacancy_dipole": "list of list of float (3x3 matrix)",
          "transition_dipole": "list of list of float (3x3 matrix)",
          "migration_volume_tensor": "list of list of float (3x3 matrix)"
        },
        "units": {
          "vacancy_dipole": "eV",
          "transition_dipole": "eV",
          "migration_volume_tensor": "Å³"
        }
      },
      "description": "Final computed tensors: vacancy elastic dipole P_vac, transition-state elastic dipole P_ts, and migration-volume tensor ΔV. Each is a 3x3 array of floats. The hidden checker compares every component to the paper's reference 3×3×3 supercell values within tolerances; score is fraction of components in agreement."
    }
  ],
  "notes": "All DFT calculations must use the 3×3×3 supercell and the specified elastic constants. The solver may use external compute resources; only the final JSON must be placed under /app/outputs."
}
```

## How you are scored
Each workflow stage is assessed by a hidden verifier that independently checks the artifacts you produce. The final scored artifact is `computed_tensors.json`. The verifier compares every component of the vacancy dipole, transition dipole, and migration-volume tensor to hidden reference values and awards a score based on how many components fall within a prescribed numerical tolerance. The overall reward is a weighted sum of the per-artifact scores, with the computed tensors carrying the highest weight. Simply reporting numbers that match the reference without producing the required intermediate evidence will not receive full credit; the verifier also confirms that the expected process artifacts exist and are consistent with the final output.
