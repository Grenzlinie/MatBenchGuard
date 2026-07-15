# DFT Calculation of Defect Formation Energies and Diffusion Barriers for As‑Doped Silicon

## Problem background
Heavily arsenic-doped silicon exhibits complex dynamical phenomena including dopant deactivation, reactivation, and anomalous diffusion. Experimental observations show that upon annealing at moderate temperatures, the electrical activity drops abruptly, and at higher temperatures the activity can partially recover. Concurrently, arsenic diffusivity depends strongly on doping concentration, with enhanced diffusion found above a critical doping threshold. Understanding and controlling these phenomena requires an atomistic picture of the interactions between arsenic atoms and native point defects (vacancies and self-interstitials). A key open question is the formation energies and migration properties of various As‑vacancy and As‑interstitial complexes, and how they give rise to the observed macroscopic behavior.

## Approach
The approach uses first‑principles density functional theory (DFT) with the local density approximation (LDA) and plane‑wave pseudopotentials. Silicon and arsenic are described by standard LDA pseudopotentials; the silicon lattice constant is set to 5.42 Å. Total energy calculations are performed with the supercell method: 32‑atom supercells for defect formation energies, and 64‑atom supercells for migration barrier calculations. For each defect configuration (including pure Si bulk, As substitutional, an isolated vacancy, and a series of As‑vacancy and As‑interstitial complexes) atomic positions are relaxed until forces are negligible. Formation energies are then extracted from the total energies using the standard supercell formation energy formula with appropriate chemical potentials. Migration barriers for the AsV and As₂V complexes are obtained using nudged elastic band (NEB) or climbing‑image methods, dissecting the barrier into the component steps described in the workflow. The entire workflow is purely computational — the required inputs are public (crystal structure, pseudopotentials, open‑source DFT code) and all results are produced by re‑running the procedure.

## Reproduction target
Produce DFT‑calculated formation energies (in eV) for the following defect complexes: V (vacancy), AsV, As₂V, As₃V, As₄V, V₂, As₂V₂, As₄V₂, As₆V₂, As₂I, and As₄I. Output these as a CSV file with columns `defect`, `formation_energy_eV`, `total_energy_eV`, and `supercell_size`. Also compute the migration barriers and total diffusion activation energies for AsV and As₂V. Output these as a JSON file with top‑level keys `AsV` and `As₂V`, each containing `migration_barrier_eV` and `activation_energy_eV`. The activation energy is the sum of the formation energy and the migration barrier for each complex. All calculations must follow the DFT protocol outlined above: 32‑atom supercells for formation energies, 64‑atom supercells and NEB for migration barriers, LDA functional, relaxed atomic positions. Write the artifacts to `/app/outputs/defect_formation_energies.csv` and `/app/outputs/migration_barriers.json`.

## Assets

- Plane‑wave DFT code (LDA functional): Quantum ESPRESSO (pw.x) or equivalent
- Si pseudopotential (LDA): https://pseudopotentials.quantum-espresso.org/
- As pseudopotential (LDA): https://pseudopotentials.quantum-espresso.org/
- Si diamond structure (a=5.42 Å)

## Workflow steps

### Step 1: DFT Supercell Calculations for Formation Energies
- Role: process
- Action: Perform DFT supercell calculations for Si bulk, As substitutional, isolated vacancy, and all required defect complexes (V, AsV, As2V, As3V, As4V, V2, As2V2, As4V2, As6V2, As2I, As4I) using a plane‑wave LDA code in 32‑atom supercells, relax atomic positions, and obtain total energies. Record the raw total energies for later formation‑energy extraction.
- Evidence: `/app/outputs/formation_energies_raw_energies.txt`

### Step 2: Report Defect Formation Energies
- Role: scored
- Action: Compute the formation energy (in eV) for each defect complex from the DFT total energies using the standard supercell formation‑energy formula with chemical potentials. Output the results in a CSV file.
- Output file: `/app/outputs/defect_formation_energies.csv`
- Format: csv
- Contract: Columns: defect (string, e.g., 'As2V'), formation_energy_eV (float), total_energy_eV (float), supercell_size (int). Must include entries for at least: V, AsV, As2V, As3V, As4V, V2, As2V2, As4V2, As6V2, As2I, As4I.
- Scoring: scored by hidden verifier

### Step 3: DFT Migration Barrier Calculations for AsV and As2V
- Role: process
- Action: Calculate the migration energy barriers for AsV and As2V using NEB or climbing‑image methods in 64‑atom supercells. For AsV: determine the energy change when the vacancy moves from nearest‑neighbor to third‑neighbor position and the bare vacancy migration energy. For As2V: compute the migration energy along the ring‑exchange pathways. Record the raw barrier components.
- Evidence: `/app/outputs/migration_raw_data.json`

### Step 4: Report AsV and As2V Diffusion Activation Energies
- Role: scored (load-bearing)
- Action: Compute the total diffusion activation energy for AsV (formation energy of AsV plus the migration energy components) and for As2V (formation energy of As2V plus its migration barrier). Output the values as a JSON file.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: Top-level keys: 'AsV' and 'As2V'. Each value is an object with keys: 'migration_barrier_eV' (float, sum of barrier components), 'activation_energy_eV' (float, total diffusion activation energy = formation_energy + migration_barrier).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_formation_energies.csv`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_formation_energies.csv
- path: `/app/outputs/defect_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with formation energies for V, AsV, As2V, As3V, As4V, V2, As2V2, As4V2, As6V2, As2I, As4I. Checker compares formation_energy_eV to hidden reference values with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `formation_energy_eV`, `total_energy_eV`, `supercell_size`
  - `columns`:
    - `defect`: string
    - `formation_energy_eV`: float (eV)
    - `total_energy_eV`: float (eV)
    - `supercell_size`: int

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file with migration barrier and total activation energy for AsV and As2V. Checker compares activation_energy_eV to hidden reference values with an appropriate tolerance.
- schema:
  - `type`: object
  - `required`: `AsV`, `As2V`
  - `properties`:
    - `AsV`:
      - `type`: object
      - `required`: `migration_barrier_eV`, `activation_energy_eV`
      - `properties`:
        - `migration_barrier_eV`:
          - `type`: float
        - `activation_energy_eV`:
          - `type`: float
    - `As2V`:
      - `type`: object
      - `required`: `migration_barrier_eV`, `activation_energy_eV`
      - `properties`:
        - `migration_barrier_eV`:
          - `type`: float
        - `activation_energy_eV`:
          - `type`: float

Notes: Scores are based on result‑level comparison to reference formation energies and activation energies; relative ordering among defect pairs may also be checked. Tolerances accommodate typical DFT LDA supercell spread (±0.3 eV).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "formation_energy_eV",
          "total_energy_eV",
          "supercell_size"
        ],
        "columns": {
          "defect": "string",
          "formation_energy_eV": "float (eV)",
          "total_energy_eV": "float (eV)",
          "supercell_size": "int"
        }
      },
      "description": "CSV file with formation energies for V, AsV, As2V, As3V, As4V, V2, As2V2, As4V2, As6V2, As2I, As4I. Checker compares formation_energy_eV to hidden reference values with an appropriate tolerance."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "AsV",
          "As2V"
        ],
        "properties": {
          "AsV": {
            "type": "object",
            "required": [
              "migration_barrier_eV",
              "activation_energy_eV"
            ],
            "properties": {
              "migration_barrier_eV": {
                "type": "float"
              },
              "activation_energy_eV": {
                "type": "float"
              }
            }
          },
          "As2V": {
            "type": "object",
            "required": [
              "migration_barrier_eV",
              "activation_energy_eV"
            ],
            "properties": {
              "migration_barrier_eV": {
                "type": "float"
              },
              "activation_energy_eV": {
                "type": "float"
              }
            }
          }
        }
      },
      "description": "JSON file with migration barrier and total activation energy for AsV and As2V. Checker compares activation_energy_eV to hidden reference values with an appropriate tolerance."
    }
  ],
  "notes": "Scores are based on result‑level comparison to reference formation energies and activation energies; relative ordering among defect pairs may also be checked. Tolerances accommodate typical DFT LDA supercell spread (±0.3 eV)."
}
```

## How you are scored
A hidden verifier independently evaluates each scored workflow stage artifact. The verifier compares the formation energies and activation energies in your submitted files against hidden reference values that are consistent with the physical system; it may also check structural consistency, such as the relative ordering of formation energies among related complexes. The score for each artifact is weighted and combined to produce a final reward between 0 and 1. Simply reporting the paper’s numbers is not sufficient — you must generate results by running the described computational protocol, and the verifier will inspect the actual files you produce.
