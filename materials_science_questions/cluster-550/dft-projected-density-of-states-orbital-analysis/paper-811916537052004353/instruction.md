# DFT Work Function Comparison of Nb and NbC

## Problem background
Amorphous carbon (a-C) films are promising field electron emitters, and their performance can be improved by inserting a metallic buffer layer.  When a niobium (Nb) buffer layer is placed between the a-C film and the silicon substrate, subsequent annealing leads to the formation of a niobium carbide (NbC) phase at the a-C/Nb interface.  This carbide phase is hypothesised to lower the interface barrier and thereby enhance electron injection from the substrate into the a-C film.  This task reproduces the first‑principles density functional theory (DFT) calculation that compares the work functions of Nb and NbC in order to evaluate that hypothesis.

## Approach
The approach uses density functional theory with the GGA‑PW91 exchange‑correlation functional.  The bulk lattice constants of Nb (body‑centred cubic) and NbC (rock‑salt structure) are first optimised.  From these optimised structures, slab models are constructed: a Nb(110) surface and a NbC(100) surface, each containing 10 atomic layers and at least 15 Å of vacuum perpendicular to the surface.  For each slab a self‑consistent field calculation is performed, and the work function is obtained as the difference between the electrostatic potential in the vacuum region and the Fermi energy.  The two computed work functions are then compared.  The calculations are carried out with Quantum ESPRESSO, an open‑source DFT code, using publicly available GGA‑PW91 pseudopotentials for Nb and C.

## Reproduction target
Using DFT with the GGA‑PW91 functional, compute the work functions of bulk Nb and NbC from the slab models described above.  Report both values (in eV) in the JSON file `/app/outputs/workfunction_values.json`.  The hidden verifier will check whether the work function of NbC is indeed lower than that of Nb, consistent with the physical hypothesis.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PW91 pseudopotentials for Nb and C: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Bulk lattice optimization
- Role: process
- Action: Optimize bulk Nb (bcc) and NbC (rocksalt) lattice constants via DFT variable-cell relaxation using GGA-PW91 pseudopotentials.
- Evidence: `/app/outputs/bulk_optimization.log`

### Step 2: Work function of Nb slab
- Role: process
- Action: Construct a Nb(110) slab (10 atomic layers, >15 Angstrom vacuum) using the optimized lattice constant, run a self-consistent calculation, and compute the work function as the vacuum potential minus the Fermi energy.
- Evidence: `/app/outputs/nb_slab_workfunction.log`

### Step 3: Work function of NbC slab
- Role: process
- Action: Construct a NbC(100) slab (10 atomic layers, >15 Angstrom vacuum) using the optimized lattice constant, run a self-consistent calculation, and compute the work function.
- Evidence: `/app/outputs/nbc_slab_workfunction.log`

### Step 4: Collect work functions
- Role: scored (load-bearing)
- Action: Write the computed work function values (in eV) into workfunction_values.json with keys Nb_workfunction_eV and NbC_workfunction_eV.
- Output file: `/app/outputs/workfunction_values.json`
- Format: json
- Contract: {"Nb_workfunction_eV": <float>, "NbC_workfunction_eV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/workfunction_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### workfunction_values.json
- path: `/app/outputs/workfunction_values.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The computed work functions of Nb and NbC. The checker verifies that the NbC work function is lower than the Nb work function.
- schema:
  - `type`: object
  - `required`: `Nb_workfunction_eV`, `NbC_workfunction_eV`
  - `properties`:
    - `Nb_workfunction_eV`:
      - `type`: number
      - `description`: Work function of Nb in eV
    - `NbC_workfunction_eV`:
      - `type`: number
      - `description`: Work function of NbC in eV

Notes: The scoring is based on the structural ordering (NbC_workfunction_eV < Nb_workfunction_eV). The exact values are method-dependent and are not targeted; only the relative ordering is scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "workfunction_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "Nb_workfunction_eV",
          "NbC_workfunction_eV"
        ],
        "properties": {
          "Nb_workfunction_eV": {
            "type": "number",
            "description": "Work function of Nb in eV"
          },
          "NbC_workfunction_eV": {
            "type": "number",
            "description": "Work function of NbC in eV"
          }
        }
      },
      "description": "The computed work functions of Nb and NbC. The checker verifies that the NbC work function is lower than the Nb work function."
    }
  ],
  "notes": "The scoring is based on the structural ordering (NbC_workfunction_eV < Nb_workfunction_eV). The exact values are method-dependent and are not targeted; only the relative ordering is scored."
}
```

## How you are scored
A hidden verifier independently inspects the scored artifact (`workfunction_values.json`).  It reads the two work function values and verifies that `NbC_workfunction_eV` < `Nb_workfunction_eV`.  It may also check that both values lie within a plausible range (4–10 eV).  The reward is based on whether these structural criteria are satisfied; the exact numerical values are not compared against a fixed target.  Reporting approximate numbers that happen to satisfy the inequality without genuinely executing the DFT workflow will not meet the requirement, because the verifier also cross‑checks the logged evidence of intermediate calculation steps.
