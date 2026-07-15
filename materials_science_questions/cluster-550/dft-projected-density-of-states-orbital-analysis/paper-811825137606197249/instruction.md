# DFT Breaking Force Analysis of Au-Octanedithiol Junctions via Adiabatic Elongation

## Problem background
Break junctions formed by thiol‑terminated molecules contacting Au electrodes are widely used to study single‑molecule conductance. The formation and failure mechanisms remain actively debated. Key open questions include: (1) Do the terminal hydrogen atoms of the –SH groups detach when the junction forms? (2) If they detach, do they adsorb onto the Au electrodes, and do they influence where and at what force the junction breaks? Answering these questions requires quantifying the breaking force and identifying the lowest‑energy bond‑breaking path for each plausible contact geometry. This task considers five representative junction configurations (T1–T5) of an octanedithiol molecule bridging Au(111) electrodes. The configurations differ in whether zero, one, or both terminal H atoms are retained, and whether a detached H is adsorbed near the Au atom that bonds to the sulfur. The goal is to compute, from first‑principles, the characteristic breaking force and the bond that fails for each configuration, and thereby clarify the role of the terminal H atom in the mechanical stability of the junction.

## Approach
The method relies on density‑functional theory (DFT) simulations using the SIESTA code with the PBE‑GGA functional and norm‑conserving pseudopotentials. The computational procedure starts with independent relaxations of the three subsystems that will form the junction: an isolated octanedithiol molecule, a Au(111) slab representing the substrate, and a tip model consisting of two Au layers plus a four‑atom pyramid. After obtaining equilibrium geometries and the reference Au–S bond lengths, the equilibrium adsorption sites of a detached H atom on the Au(111) surface (hollow site) and on the tip (bridge site) are determined. Using these results, five initial junction geometries are assembled: T1 (H retained at the tip side, detached at the substrate); T2 (H retained at the substrate side, detached at the tip); T3 (both H detached); T4 and T5 (both H detached, with one H re‑adsorbed at the tip or substrate near the Au–S contact). For each junction type, an adiabatic contraction/elongation simulation is performed: the junction is first contracted by 1–2 Å to ensure good electrical contact, then elongated in steps of 0.2 Å until breakdown. At each step the z‑coordinates of the two end Au layers are fixed, while all other atomic positions are relaxed until the force on every atom falls below 0.08 nN/atom. The total energy and the junction length (supercell dimension along the stretch direction) are recorded. The resulting energy‑vs‑length curves are analyzed to locate the breaking segment—the last linear segment before the energy plateau—and the average breaking force is computed as F = ΔE/ΔL. Visual inspection of the atomic coordinates at breakdown determines which bond fails (thiol–Au, S–Au, or H–Au). The procedure is repeated for all five junction types, producing a table of breaking forces and bond types, and raw energy‑length curves.

## Reproduction target
Execute the DFT contraction/elongation protocol described in the approach for the five junction types T1, T2, T3, T4, T5. From the simulation output, calculate the breaking force (in nN) and identify the breaking bond type for each junction. Write these results to `/app/outputs/breaking_forces.csv` with columns `junction_type` (T1–T5), `breaking_force_nN` (float), and `breaking_bond` (one of `thiol-Au`, `S-Au`, `H-Au`). Additionally, extract the total energy (eV) and junction length (Å) at every elongation step for all five types and write them to `/app/outputs/energy_curves.json`. The JSON object must have top‑level keys `"T1"` through `"T5"`, each mapping to an array of objects with fields `step_number` (int), `length_angstrom` (float), and `total_energy_eV` (float). The evaluation is performed entirely by an external checker; submitting the paper’s reported numbers is not sufficient.

## Assets

- SIESTA DFT code: https://gitlab.com/siesta-project/siesta
- Troullier-Martins norm-conserving pseudopotentials (Au, S, C, H)

## Workflow steps

### Step 1: Subsystem DFT relaxation
- Role: process
- Action: Using SIESTA (PBE-GGA, norm-conserving pseudopotentials, appropriate basis sets, 2x2x2 k-point sampling), independently relax the geometry of (i) an isolated octanedithiol molecule, (ii) a 3-layer Au(111) slab with a 3x3 lateral supercell (substrate), and (iii) a tip model consisting of two Au layers plus a four-atom pyramid. Note the optimized Au–S bond length.
- Evidence: `/app/outputs/subsystem_geometries.xyz`

### Step 2: Determine detached H adsorption sites on Au
- Role: process
- Action: Using SIESTA, relax a single H atom on the Au(111) substrate surface (hollow site) and on the Au tip (bridge site) to find equilibrium adsorption positions and H–Au distances. Record the position and distances for constructing junction types T4 and T5.
- Evidence: `/app/outputs/h_sites.json`

### Step 3: Assemble initial junction geometries T1–T5
- Role: process
- Action: Construct the five junction types (T1, T2, T3, T4, T5) from the relaxed subsystems. For T1/T2 keep one terminal H and detach the other; for T3 detach both; for T4/T5 detach both and place one H at the adsorption site found in step02. Set all Au–S bond lengths to the optimized value from step01. Use a single representative adsorption site and azimuthal angle per type (the paper reports that the main breaking features are independent of these).
- Evidence: `/app/outputs/initial_junctions.xyz`

### Step 4: Run adiabatic contraction/elongation DFT simulations
- Role: process
- Action: For each junction type (T1–T5): first contract the junction by approximately 1–2 Å, then elongate stepwise (0.2 Å per step) until breakdown. At each step fix the z-coordinates of the two end Au layers, relax all other coordinates until forces <0.08 nN/atom, and record total energy and junction length (supercell size in stretch direction). Output raw trajectories, energies, and junction lengths.
- Evidence: none

### Step 5: Compute breaking forces and bond types
- Role: scored (load-bearing)
- Action: From the raw simulation data of step04, for each junction type identify the breaking segment (the last linear energy-length segment before the plateau) and compute the average breaking force F = ΔE/ΔL. Inspect the atomic configurations at breakdown to determine which bond fails (thiol–Au, S–Au, or H–Au). Write the results to breaking_forces.csv.
- Output file: `/app/outputs/breaking_forces.csv`
- Format: csv
- Contract: columns: junction_type (str: T1, T2, T3, T4, T5), breaking_force_nN (float), breaking_bond (str: thiol-Au, S-Au, H-Au)
- Scoring: scored by hidden verifier

### Step 6: Produce energy–length curves
- Role: scored
- Action: From the raw simulation data of step04, extract the total energy (eV) and junction length (Å) at each elongation step for all five junction types and write them to energy_curves.json. The JSON object must have keys T1..T5, each holding a list of step objects with fields step_number, length_angstrom, total_energy_eV.
- Output file: `/app/outputs/energy_curves.json`
- Format: json
- Contract: JSON object with keys 'T1'..'T5'; each value is a list of objects: {step_number: int, length_angstrom: float, total_energy_eV: float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/breaking_forces.csv`
- `/app/outputs/energy_curves.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### breaking_forces.csv
- path: `/app/outputs/breaking_forces.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Breaking force (nN) and breaking bond type for each of the five junction types T1–T5, extracted from the DFT elongation simulations.
- schema:
  - `type`: table
  - `required_columns`: `junction_type`, `breaking_force_nN`, `breaking_bond`
  - `units`:
    - `breaking_force_nN`: nN

### energy_curves.json
- path: `/app/outputs/energy_curves.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Total energy vs junction length curves for each junction type, used to verify structural consistency (monotonic length increase, plateau after breakdown, presence of all five junction types).
- schema:
  - `type`: object
  - `required`:
    - `T1`: array of step objects
  - `items`:
    - `step_number`: int
    - `length_angstrom`: float
    - `total_energy_eV`: float

Notes: The breaking forces and bond types are compared against the paper's central reported values; energy curves are checked for monotonicity and presence of a post-break plateau. No gold values or tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "breaking_forces.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "junction_type",
          "breaking_force_nN",
          "breaking_bond"
        ],
        "units": {
          "breaking_force_nN": "nN"
        }
      },
      "description": "Breaking force (nN) and breaking bond type for each of the five junction types T1–T5, extracted from the DFT elongation simulations."
    },
    {
      "file": "energy_curves.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "T1": "array of step objects"
        },
        "items": {
          "step_number": "int",
          "length_angstrom": "float",
          "total_energy_eV": "float"
        }
      },
      "description": "Total energy vs junction length curves for each junction type, used to verify structural consistency (monotonic length increase, plateau after breakdown, presence of all five junction types)."
    }
  ],
  "notes": "The breaking forces and bond types are compared against the paper's central reported values; energy curves are checked for monotonicity and presence of a post-break plateau. No gold values or tolerances are revealed here."
}
```

## How you are scored
A hidden verifier script independently scores each output artifact and combines the scores into a single reward in the range [0,1]. For `breaking_forces.csv` it compares your submitted breaking force values and bond type labels against expected reference results. The accuracy of the forces contributes roughly 80% of the total reward (16% per junction type), and correctly assigning the breaking bond contributes roughly 20% (4% per type). For `energy_curves.json` the verifier checks structural consistency: monotonic increase of the junction length, the presence of an energy plateau after breakdown, and that data for all five junction types exist. The reward is a weighted sum of these components; structural checks carry a much smaller weight. The verifier operates entirely from your submitted artifacts and does not require network access. Simply reporting the reference values without genuinely executing the computational protocol will not pass.
