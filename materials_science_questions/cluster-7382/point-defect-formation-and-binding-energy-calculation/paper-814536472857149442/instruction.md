# Calculation of point defect pair interaction energies in bcc-Fe

## Problem background
Point defects and their interactions control precipitation, hardening, and embrittlement in bcc Fe-based alloys. Effective pair interaction energies between substitutional solutes and vacancies are essential input for kinetic and thermodynamic models, but they are not directly measurable. First-principles density functional theory (DFT) calculations can provide a systematic database of such interactions. This task targets a representative subset of solute pairs (Al, Cu, S and vacancies) and requires the computation of their interaction energies in ferromagnetic bcc Fe using a plane-wave DFT approach.

## Approach
The approach uses a supercell method based on DFT. A 128-atom (4×4×4) bcc Fe supercell is constructed at the experimental lattice constant. Total energies are computed for several configurations: a defect-free supercell, supercells with a single substitutional solute (Al, Cu, S or a vacancy), and supercells with two defects placed at the first three nearest-neighbour coordination shells. For each defect pair, the effective pair interaction energy is obtained as V_n = E(pq;n) + E0 − E_p − E_q, where E(pq;n) is the energy of the pair supercell at shell n, E_p and E_q are the single-defect energies, and E0 is the defect-free energy. All calculations employ the Perdew–Burke–Ernzerhof (PBE) functional under the generalized gradient approximation, with full internal atomic relaxation while keeping the supercell volume fixed. The workflow is carried out using an open-source plane-wave DFT code and standard GGA-PBE pseudopotentials.

## Reproduction target
Reproduce the effective pair interaction energies V_n (n = 1, 2, 3) for the following defect pairs in ferromagnetic bcc Fe: Al-Al, Cu-Cu, S-S, Al-Cu, Al-Vac, Cu-Vac, and S-Vac. The calculations must include full atomic relaxation and be performed with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO or GPAW) using GGA-PBE pseudopotentials. Present the results as a JSON object where each pair key maps to an array of three floats [V_1, V_2, V_3] (in eV). Example: {"Al-Al": [0.13, 0.13, 0.01]}.

## Assets

- Open-source plane-wave DFT code: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table
- bcc Fe crystal structure: 10.1038/sdata.2018.148

## Workflow steps

### Step 1: Generate supercell structures
- Role: process
- Action: Construct a 128-atom (4x4x4) bcc Fe supercell with lattice constant a=0.286 nm. Generate all required supercell input files: defect-free, single substitutional defects for Al, Cu, S and a vacancy, and pair-defect supercells for Al-Al, Cu-Cu, S-S, Al-Cu, Al-Vac, Cu-Vac, S-Vac at the 1st, 2nd, and 3rd nearest-neighbour shell distances. Write the structures in the input format of the chosen DFT code.
- Evidence: `/app/outputs/structures.tar.gz`

### Step 2: Run DFT total energy calculations
- Role: process
- Action: Perform static DFT calculations with full atomic relaxation (internal coordinates, fixed cell volume) for every supercell generated in step_01. Use the GGA-PBE exchange-correlation functional, a plane-wave cutoff of 350 eV, a 4x4x4 Monkhorst-Pack k-mesh, and convergence criteria of 1e-6 eV/atom on total energy and 1e-2 eV/Å on forces. Save the converged total energies (in eV) for each supercell to /app/outputs/total_energies.json.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Compute and export interaction energies
- Role: scored (load-bearing)
- Action: From the total energies in /app/outputs/total_energies.json, compute effective pair interaction energies for each defect pair (Al-Al, Cu-Cu, S-S, Al-Cu, Al-Vac, Cu-Vac, S-Vac) and each shell n=1,2,3 using the formula V_n = E(pq;n) + E_0 - E_p - E_q, where E(pq;n) is the energy of the pair supercell at shell n, E_p and E_q are the single-defect energies, and E_0 is the defect-free energy. Write the results to /app/outputs/interaction_energies.json.
- Output file: `/app/outputs/interaction_energies.json`
- Format: json
- Contract: A JSON object with keys 'Al-Al', 'Cu-Cu', 'S-S', 'Al-Cu', 'Al-Vac', 'Cu-Vac', 'S-Vac'. Each key maps to an array of three floats representing V_1, V_2, V_3 (in eV). Example: {"Al-Al": [0.13, 0.13, 0.01]}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.json
- path: `/app/outputs/interaction_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Effective pair interaction energies (eV) for the specified defect pairs at 1st, 2nd, and 3rd nearest-neighbour coordination shells.
- schema:
  - `type`: object
  - `properties`:
    - `Al-Al`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `Cu-Cu`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `S-S`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `Al-Cu`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `Al-Vac`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `Cu-Vac`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `S-Vac`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
  - `required`: `Al-Al`, `Cu-Cu`, `S-S`, `Al-Cu`, `Al-Vac`, `Cu-Vac`, `S-Vac`

Notes: The verifier compares the reported interaction energies to the paper's published PAW-VASP relaxed values with a tolerance of 0.05 eV per entry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "Al-Al": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "Cu-Cu": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "S-S": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "Al-Cu": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "Al-Vac": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "Cu-Vac": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "S-Vac": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          }
        },
        "required": [
          "Al-Al",
          "Cu-Cu",
          "S-S",
          "Al-Cu",
          "Al-Vac",
          "Cu-Vac",
          "S-Vac"
        ]
      },
      "description": "Effective pair interaction energies (eV) for the specified defect pairs at 1st, 2nd, and 3rd nearest-neighbour coordination shells."
    }
  ],
  "notes": "The verifier compares the reported interaction energies to the paper's published PAW-VASP relaxed values with a tolerance of 0.05 eV per entry."
}
```

## How you are scored
Your submission is scored by a hidden verifier. The verifier reads your interaction_energies.json, extracts the V_n value for each defect pair and coordination shell, and compares it to reference values obtained from the same physical setup using a tolerance appropriate for the spread between different plane-wave DFT implementations. The final score (0–1) is the fraction of (pair, shell) entries that fall within the tolerance. Achieving a high score requires running the complete DFT pipeline; reporting numbers without performing the calculations will not yield accurate enough values to pass the tolerance checks.
