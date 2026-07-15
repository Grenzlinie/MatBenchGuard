# DFT+U Paramagnetic Phonon Model for UO₂

## Problem background
Accurate modelling of neutron interactions in uranium dioxide (UO₂) requires a thermal scattering law that captures crystal binding effects. A key ingredient is the partial phonon density of states (DOS) for uranium and oxygen, which governs the Debye‑Waller coefficient and inelastic scattering. Earlier semi‑empirical lattice dynamics models showed discrepancies in the temperature‑dependent mean‑square displacements. This task computes a first‑principles phonon model using spin‑polarised density functional theory with a Hubbard correction (DFT+U) for the uranium 5f electrons and a paramagnetic force‑averaging approximation.

## Approach
Perform spin‑polarised DFT+U calculations in the 1‑k antiferromagnetic configuration using the PBE exchange‑correlation functional and an effective on‑site Coulomb repulsion Ueff = 4 eV for uranium 5f electrons. Optimise the cubic lattice constant of UO₂. Then construct a 2×2×2 supercell of the optimised structure and compute Hellmann–Feynman forces for symmetry‑inequivalent atomic displacements. Average the forces with a paramagnetic weighting: for a displacement along a cubic axis, assign weight 2/3 to the forces from AFM configurations with magnetic moments perpendicular to the displacement and weight 1/3 to the configuration with moments parallel. From the resulting force‑constant matrix, use a direct‑method phonon code (Phonopy) to compute the partial phonon DOS for uranium and oxygen on a uniform energy grid. The partial DOS enables calculation of the Debye‑Waller coefficient at any temperature by integration.

## Reproduction target
Produce two scored artifacts: (1) the optimised cubic lattice constant of UO₂ from DFT+U, written to lattice_constant.json, and (2) the partial phonon density of states for uranium and oxygen, written to phonon_dos.json. A hidden verifier will check the lattice constant value against a reference obtained from the same calculation methodology and will recompute the Debye‑Waller coefficients at 300 K from the submitted DOS, comparing the results to a hidden reference.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP pseudopotentials (PBE, efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- UO₂ cubic Fluorite structure (Fm-3m, space group 225)

## Workflow steps

### Step 1: Lattice constant optimization
- Role: scored
- Action: Perform spin‑polarized DFT+U calculations on UO₂ in the 1‑k AFM configuration with U_eff = 4 eV for uranium 5f electrons and PBE exchange‑correlation functional. Optimize the cubic lattice parameter until energy and volume are converged, and write the final value.
- Output file: `/app/outputs/lattice_constant.json`
- Format: json
- Contract: { "lattice_constant_nm": number, "unit": "string (nm)" }
- Scoring: scored by hidden verifier

### Step 2: Supercell Hellmann–Feynman forces
- Role: process
- Action: Construct a 2×2×2 supercell (64 atoms) using the optimized lattice constant. For each symmetry‑inequivalent atomic displacement required by the direct method, run single‑point DFT calculations with the same functional, U_eff, and a k‑point mesh appropriate for the supercell. Collect the Hellmann–Feynman forces from each calculation.
- Evidence: `/app/outputs/forces.log`

### Step 3: Paramagnetic force averaging
- Role: process
- Action: Average the Hellmann–Feynman forces using the paper’s paramagnetic weighting: for displacements along a cubic axis, weight 2/3 to forces from AFM configurations with magnetic moments perpendicular to the displacement and 1/3 to the configuration with moments parallel. From the averaged forces, construct the force‑constant matrix.
- Evidence: `/app/outputs/force_constants.dat`

### Step 4: Phonon density of states calculation
- Role: scored (load-bearing)
- Action: From the force‑constant matrix and the crystal structure, use a direct‑method phonon code (e.g., Phonopy) to compute the partial phonon density of states for uranium and oxygen on a uniform energy grid. Write the energy grid and the two DOS arrays to the output file.
- Output file: `/app/outputs/phonon_dos.json`
- Format: json
- Contract: { "energy_eV": [number], "U_DOS": [number], "O_DOS": [number], "unit_DOS": "string (states/eV/atom)" }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constant.json`
- `/app/outputs/phonon_dos.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constant.json
- path: `/app/outputs/lattice_constant.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice constant of cubic UO₂ (Fm-3m). The checker verifies that the value is within 2% of the paper’s result.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_nm`: number
    - `unit`: string

### phonon_dos.json
- path: `/app/outputs/phonon_dos.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Partial phonon density of states for uranium and oxygen in UO₂. The checker recomputes the Debye‑Waller coefficient at 300 K from these arrays and compares the computed values to the paper’s reported Debye‑Waller coefficients with a tolerance of ±15%.
- schema:
  - `type`: object
  - `required`:
    - `energy_eV`: array of numbers
    - `U_DOS`: array of numbers
    - `O_DOS`: array of numbers
    - `unit_DOS`: string

Notes: Only the lattice constant and the phonon DOS are scored. The process steps (force calculations and paramagnetic averaging) are required but not directly scored; their execution is enforced by the load‑bearing nature of the phonon DOS step, which cannot be correctly produced without running those preceding steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constant.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_nm": "number",
          "unit": "string"
        }
      },
      "description": "Optimized lattice constant of cubic UO₂ (Fm-3m). The checker verifies that the value is within 2% of the paper’s result."
    },
    {
      "file": "phonon_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "energy_eV": "array of numbers",
          "U_DOS": "array of numbers",
          "O_DOS": "array of numbers",
          "unit_DOS": "string"
        }
      },
      "description": "Partial phonon density of states for uranium and oxygen in UO₂. The checker recomputes the Debye‑Waller coefficient at 300 K from these arrays and compares the computed values to the paper’s reported Debye‑Waller coefficients with a tolerance of ±15%."
    }
  ],
  "notes": "Only the lattice constant and the phonon DOS are scored. The process steps (force calculations and paramagnetic averaging) are required but not directly scored; their execution is enforced by the load‑bearing nature of the phonon DOS step, which cannot be correctly produced without running those preceding steps."
}
```

## How you are scored
A hidden verifier independently reads your output files. It checks that the lattice constant in lattice_constant.json is consistent with the value expected from the specified DFT+U protocol, and it computes the Debye‑Waller coefficients at 300 K from the partial phonon DOS you supply, comparing the results to a hidden reference. Each scored artifact contributes to the final reward according to its weight. The verifier’s checks are based on your deposited artifacts; reporting a number that resembles the paper is not sufficient — the submitted data must correctly reflect the workflow.
