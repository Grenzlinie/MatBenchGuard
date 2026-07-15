# Energetics of a⟨011⟩ edge dislocation decomposition in NiAl using embedded atom method

## Problem background
NiAl intermetallic single crystals deformed along the ⟨100⟩ 'hard' orientation exhibit exceptionally high strength at low temperatures and a brittle-to-ductile transition at intermediate temperatures. Experimental TEM observations suggest that a⟨011⟩ edge dislocations decompose into two sessile a⟨010⟩ dislocations, which could explain the low mobility and the mechanical properties. This task reproduces the core energetics of these dislocations using embedded-atom method (EAM) atomistic simulations, providing the mechanistic basis for the decomposition.

## Approach
The workflow employs EAM molecular statics and dynamics to model an a[01-1] edge dislocation in NiAl. First, a cylindrical supercell (radius 10 nm) containing the dislocation is constructed using anisotropic elasticity theory with the given NiAl elastic constants (c11=200 GPa, c12=120 GPa, c44=120 GPa). The outer 1 nm of atoms are held fixed. The perfect dislocation core is relaxed via energy minimization using the Rao et al. (1991) EAM potential. The core energy is computed from the total energy within a 9 nm radius, referenced to stoichiometric NiAl chemical potentials. To study the transformation, a pure shear stress (0.04 strain, ≈1250 MPa) is applied on the (022) glide plane and molecular dynamics at 0 K drives the perfect core into a decomposed configuration of two a⟨010⟩ dislocations. After removing the shear stress and re-relaxing, the energy and separation of the decomposed cores are evaluated. The key comparison is whether the decomposed configuration has lower core energy than the perfect one, and whether decomposition occurs under the applied shear.

## Reproduction target
Compute the core energy of the perfect a[01-1] edge dislocation in NiAl (within a 9 nm radius) and the core energy of its decomposed two-a⟨010⟩ configuration after shear-induced transformation. Determine the separation distance between the a⟨010⟩ cores and confirm whether decomposition has occurred. The resulting energies and structural metrics must be reported in the specified JSON artifacts. The reproduction does not involve any experimental TEM images or weak-beam simulations; it is a purely computational task using publicly available EAM potential parameters and elastic constants.

## Assets

- NiAl EAM potential (Rao et al. 1991): 10.1557/PROC-213-125
- Elastic constants of NiAl
- LAMMPS (or equivalent EAM-capable MD code): https://lammps.org

## Workflow steps

### Step 1: Generate initial perfect dislocation configuration
- Role: process
- Action: Using the elastic constants of NiAl, construct a cylindrical supercell (radius 10 nm) with an a[0-1-1] edge dislocation on the (022) glide plane. Fix a 1 nm thick outer ring of atoms. The atomic positions should follow the anisotropic elasticity displacement field.
- Evidence: none

### Step 2: Compute perfect core energy
- Role: scored
- Action: Using the Rao et al. EAM potential, relax the perfect core via energy minimization (fix outer atoms). Compute the total energy E_T(r) within a radius r=9 nm using the chemical potential referencing for stoichiometric NiAl. Output the energy as specified.
- Output file: `/app/outputs/perfect_core.json`
- Format: json
- Contract: {"radius_nm": 9.0, "energy_J_per_m": <float>}
- Scoring: scored by hidden verifier

### Step 3: Decompose core under applied shear stress
- Role: process
- Action: Impose a pure shear strain of 0.04 (approx 1250 MPa) on the (022) plane and run molecular dynamics at 0 K using the EAM potential to induce decomposition of the perfect core into two a<010> dislocations. After decomposition, remove the shear stress and relax the structure (energy minimization) to obtain the zero-stress decomposed configuration.
- Evidence: none

### Step 4: Compute decomposed core energy and separation
- Role: scored (load-bearing)
- Action: From the relaxed decomposed configuration, compute E_T(r) for r=9 nm using the same chemical potentials. Determine the separation distance between the two a<010> dislocation cores. Verify that decomposition occurred and report the energy, separation, and a boolean confirmation.
- Output file: `/app/outputs/decomposed_core.json`
- Format: json
- Contract: {"radius_nm": 9.0, "energy_J_per_m": <float>, "separation_nm": <float>, "decomposition_confirmed": <boolean>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/perfect_core.json`
- `/app/outputs/decomposed_core.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### perfect_core.json
- path: `/app/outputs/perfect_core.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Core energy of the perfect a[01-1] edge dislocation in NiAl computed within a 9 nm radius. The value will be compared to the paper-reported result within an appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `radius_nm`: number
    - `energy_J_per_m`: number
  - `units`:
    - `radius_nm`: nm
    - `energy_J_per_m`: J/m

### decomposed_core.json
- path: `/app/outputs/decomposed_core.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Core energy (9 nm radius), separation between a<010> dislocation cores, and boolean confirmation for the decomposed a[01-1] edge configuration. Energy and separation are compared to paper values within tolerances, and the boolean must be true.
- schema:
  - `type`: object
  - `required`:
    - `radius_nm`: number
    - `energy_J_per_m`: number
    - `separation_nm`: number
    - `decomposition_confirmed`: boolean
  - `units`:
    - `radius_nm`: nm
    - `energy_J_per_m`: J/m
    - `separation_nm`: nm

Notes: The agent must obtain the Rao et al. (1991) EAM potential from the public literature (or equivalent published parameters). The workflow is purely computational; no experimental TEM images or weak-beam simulations are required. All necessary elastic constants are stated in the resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "perfect_core.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "radius_nm": "number",
          "energy_J_per_m": "number"
        },
        "units": {
          "radius_nm": "nm",
          "energy_J_per_m": "J/m"
        }
      },
      "description": "Core energy of the perfect a[01-1] edge dislocation in NiAl computed within a 9 nm radius. The value will be compared to the paper-reported result within an appropriate tolerance."
    },
    {
      "file": "decomposed_core.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "radius_nm": "number",
          "energy_J_per_m": "number",
          "separation_nm": "number",
          "decomposition_confirmed": "boolean"
        },
        "units": {
          "radius_nm": "nm",
          "energy_J_per_m": "J/m",
          "separation_nm": "nm"
        }
      },
      "description": "Core energy (9 nm radius), separation between a<010> dislocation cores, and boolean confirmation for the decomposed a[01-1] edge configuration. Energy and separation are compared to paper values within tolerances, and the boolean must be true."
    }
  ],
  "notes": "The agent must obtain the Rao et al. (1991) EAM potential from the public literature (or equivalent published parameters). The workflow is purely computational; no experimental TEM images or weak-beam simulations are required. All necessary elastic constants are stated in the resources."
}
```

## How you are scored
A hidden verifier independently checks each scored workflow stage's output artifact (perfect_core.json and decomposed_core.json). The verifier reads your reported energies, separation distance, and decomposition confirmation; compares them to hidden reference values within an appropriate tolerance; checks that the decomposed energy is lower than the perfect energy; and confirms that the separation lies in a physically plausible range and that decomposition_confirmed is true. The final reward is a weighted combination of these checks. Simply reporting numbers without genuinely executing the workflow will not pass these structural and tolerance constraints.
