# Unit-cell volumes and Li-ion migration barriers of LiNafion·nDMSO nanothreads

## Problem background
Polymer electrolytes based on lithiated Nafion membranes swollen by dimethyl sulfoxide (DMSO) are candidates for lithium batteries because they can provide high room-temperature ionic conductivity while retaining mechanical stability. The degree of swelling, and the energy barriers to lithium-ion migration between available sites in the solvated polymer matrix, are key quantities that control transport. Periodic quantum-chemical modeling of infinite LiNafion·nDMSO nanothreads with increasing DMSO content (n = 0, 1, 8, 16) allows one to compute these properties from first principles.

## Approach
The task uses periodic density functional theory (PBE functional, projector-augmented wave pseudopotentials) to model the polymer-solvent system as infinite strands repeated in space. First, initial unit-cell models for five compositions are constructed: dry LiNafion (n=0), one DMSO per repeating unit (n=1), two isomeric forms of LiNafion·8DMSO, and LiNafion·16DMSO. Full variable-cell relaxation is performed for each structure to obtain the equilibrium lattice parameters and atomic positions. From the relaxed cells the unit-cell volumes are extracted. For the two highest DMSO loadings (n=8 and n=16) the energy profile for lithium-ion migration between equivalent sites is mapped using the climbing-image nudged-elastic-band (CI-NEB) method, yielding the activation barrier for ionic hopping. All calculations are carried out with an open-source DFT package.

## Reproduction target
Compute, using an open-source periodic DFT code, the equilibrium unit-cell volumes (in Å³) for the five LiNafion·nDMSO structures (n=0, n=1, n=8 isomer‑1, n=8 isomer‑2, n=16) and the Li-ion migration barriers (in eV) for the n=8 and n=16 systems. Write the five volumes to a JSON file `volumes.json` with keys `structure1`, `structure2`, `structure3`, `structure4`, `structure6` and the two barriers to `barriers.json` with keys `n8` and `n16`. The output artifacts must conform to the schemas defined in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE PAW pseudopotentials: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build initial structures
- Role: process
- Action: Construct initial periodic unit cells for LiNafion (structure 1), LiNafion·DMSO (structure 2), two isomers of LiNafion·8DMSO (structures 3 and 4), and LiNafion·16DMSO (structure 6) based on the Nafion backbone and DMSO molecular geometry, using the published unit-cell parameters as a starting guess.
- Evidence: `/app/outputs/initial_structures`

### Step 2: Geometry optimization
- Role: process
- Action: Perform full variable-cell DFT geometry optimization for all five structures using PBE functional, PAW pseudopotentials, plane‑wave cutoff 400 eV, and a 4×2×2 Monkhorst–Pack k‑mesh; relax both atomic coordinates and cell parameters until convergence.
- Evidence: `/app/outputs/relax_outputs`

### Step 3: Compute unit-cell volumes
- Role: scored
- Action: From the optimized structures, extract the unit-cell volumes (in Å³) for structures 1, 2, 3, 4, and 6 and write them to a JSON file.
- Output file: `/app/outputs/volumes.json`
- Format: json
- Contract: {"type": "object", "properties": {"structure1": {"type": "number", "description": "Volume of LiNafion (n=0) in Å³"}, "structure2": {"type": "number", "description": "Volume of LiNafion·DMSO (n=1) in Å³"}, "structure3": {"type": "number", "description": "Volume of LiNafion·8DMSO isomer1 in Å³"}, "structure4": {"type": "number", "description": "Volume of LiNafion·8DMSO isomer2 in Å³"}, "structure6": {"type": "number", "description": "Volume of LiNafion·16DMSO in Å³"}}}
- Scoring: scored by hidden verifier

### Step 4: Compute NEB migration barriers
- Role: scored (load-bearing)
- Action: Perform NEB calculations for lithium-ion migration between equivalent sites in the optimized LiNafion·8DMSO (structure 3 or 4) and LiNafion·16DMSO (structure 6) and compute the energy barriers in eV.
- Output file: `/app/outputs/barriers.json`
- Format: json
- Contract: {"type": "object", "properties": {"n8": {"type": "number", "description": "Migration barrier for n=8 in eV"}, "n16": {"type": "number", "description": "Migration barrier for n=16 in eV"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/volumes.json`
- `/app/outputs/barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### volumes.json
- path: `/app/outputs/volumes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed unit-cell volumes for the five LiNafion·nDMSO periodic structures.
- schema:
  - `type`: object
  - `required`:
    - `structure1`: number (volume in Å³)
    - `structure2`: number (volume in Å³)
    - `structure3`: number (volume in Å³)
    - `structure4`: number (volume in Å³)
    - `structure6`: number (volume in Å³)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `structure1`: Å³
    - `structure2`: Å³
    - `structure3`: Å³
    - `structure4`: Å³
    - `structure6`: Å³

### barriers.json
- path: `/app/outputs/barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: NEB‑computed Li‑ion migration barriers for the n=8 and n=16 systems.
- schema:
  - `type`: object
  - `required`:
    - `n8`: number (barrier in eV)
    - `n16`: number (barrier in eV)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `n8`: eV
    - `n16`: eV

Notes: Volumes are compared to published reference values with a relative tolerance. Valid barriers must fall within the reported 0.2–0.3 eV window and satisfy n8 ≥ n16 (structural consistency).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "volumes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "structure1": "number (volume in Å³)",
          "structure2": "number (volume in Å³)",
          "structure3": "number (volume in Å³)",
          "structure4": "number (volume in Å³)",
          "structure6": "number (volume in Å³)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "structure1": "Å³",
          "structure2": "Å³",
          "structure3": "Å³",
          "structure4": "Å³",
          "structure6": "Å³"
        }
      },
      "description": "Computed unit-cell volumes for the five LiNafion·nDMSO periodic structures."
    },
    {
      "file": "barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "n8": "number (barrier in eV)",
          "n16": "number (barrier in eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "n8": "eV",
          "n16": "eV"
        }
      },
      "description": "NEB‑computed Li‑ion migration barriers for the n=8 and n=16 systems."
    }
  ],
  "notes": "Volumes are compared to published reference values with a relative tolerance. Valid barriers must fall within the reported 0.2–0.3 eV window and satisfy n8 ≥ n16 (structural consistency)."
}
```

## How you are scored
A hidden verifier will read your `volumes.json` and `barriers.json`. Each scored artifact is compared against reference data that defines the acceptable range and expected structural trend for the quantities. The reward is a weighted combination of the individual stage scores; reporting the paper's published numbers is not sufficient—you must generate the computed results from the DFT workflow. The verifier does not require a specific absolute value for every structure but instead checks that the results satisfy physical consistency (e.g., expected swelling behavior and barrier magnitude) and fall within tolerances corresponding to a correct reproduction with a comparable DFT setup. All stages contribute to the final reward.
