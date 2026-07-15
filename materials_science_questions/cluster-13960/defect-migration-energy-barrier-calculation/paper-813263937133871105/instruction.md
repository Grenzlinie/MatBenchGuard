# Defect formation energies and migration barriers in h-BNC₂ sheets

## Problem background
Hybrid hexagonal boron‑nitride‑carbon (h‑BNC₂) sheets are two‑dimensional materials composed of separate carbon and hexagonal boron‑nitride domains. Structural defects such as single vacancies, double vacancies, and Stone–Wales defects can strongly influence the electronic, magnetic, and transport properties of these sheets. Quantitative knowledge of the formation energetics, magnetic moments, and the barriers for defect migration and formation/healing is essential for predicting defect stability and guiding experimental synthesis.

## Approach
The computational approach uses spin‑polarized density functional theory (DFT) within the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation, employing plane‑wave basis sets and pseudopotentials. The system is modeled as an 80‑atom h‑BNC₂ supercell containing a phase‑separated zigzag interface between C and BN regions (C–N and C–B interfaces), with a lattice constant of 2.5 Å and a vacuum spacing of 12 Å. Several defect configurations are constructed by removing atoms or rotating bonds at selected sites. For each defect, the total energy and magnetic moment are obtained from a full geometry relaxation. Reference chemical potentials for C, B, and N are computed from separate DFT calculations on pristine graphene, α‑boron, and an isolated N₂ molecule using the same functional and pseudopotentials. Energy barriers for vacancy migration and for the formation/healing of a Stone–Wales defect are determined with the nudged elastic band (NEB) method. All calculations are carried out with the open‑source Quantum ESPRESSO package (pw.x for relaxations and neb.x for NEB).

## Reproduction target
Compute and report the formation energies and total magnetic moments for the following defects: single vacancies at sites C1, C3, N1, B1, and C5; and the double vacancy CC1. Additionally, compute the energy barrier for the C1→N1 single‑vacancy migration, and the formation and healing barriers of the SW1‑N Stone–Wales defect. The reported values must be consistent with the relative ordering of defect stabilities and the characteristic barrier heights expected from the chemistry and structure of h‑BNC₂ sheets. The hidden verifier will assess both the absolute numeric values and the qualitative agreement with the expected trends.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials for B, C, N: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build atomistic structures
- Role: process
- Action: Construct the 80-atom h-BNC₂ supercell with phase-separated zigzag C–N and C–B interfaces, lattice constant 2.5 Å, 12 Å vacuum. Generate initial coordinates for the pristine cell and for defect configurations: single vacancies C1, C3, N1, B1, C5; double vacancy CC1; initial and final states for C1→N1 vacancy migration; SW1-N Stone-Wales defect (rotated CN bond at the C–N interface by 90°). Save a log of the generated structures.
- Evidence: `/app/outputs/structures_log.txt`

### Step 2: Optimize pristine supercell
- Role: process
- Action: Perform a spin-polarized DFT geometry relaxation of the pristine supercell using Quantum ESPRESSO pw.x with the PBE functional and suitable pseudopotentials. Relax all internal coordinates until forces are below 0.01 eV/Å while keeping cell dimensions fixed. Store the relaxed geometry and the reference total energy E_pristine.
- Evidence: `/app/outputs/pristine_relax.out`

### Step 3: Compute reference chemical potentials
- Role: process
- Action: Perform separate spin-polarized DFT calculations with the same settings (PBE functional, same pseudopotentials) to obtain per-atom energies for: a pristine graphene sheet (for μ_C), α‑boron crystal (for μ_B), and an isolated N₂ molecule (for μ_N). These energies serve as reference chemical potentials.
- Evidence: `/app/outputs/reference_potentials.out`

### Step 4: Relax defect supercells
- Role: process
- Action: For each defect configuration (C1, C3, N1, B1, C5, CC1), perform spin-polarized DFT relaxations with the same settings as the pristine relaxation. Extract the total energy and total magnetic moment (difference of spin-up and spin-down occupations) for each relaxed cell. Keep the relaxed structures for later NEB steps.
- Evidence: `/app/outputs/defect_relax_summary.log`

### Step 5: NEB migration path for C1→N1
- Role: process
- Action: Set up a nudged elastic band calculation using Quantum ESPRESSO neb.x with the relaxed C1‑vacancy and N1‑vacancy supercells as endpoints. Use a linear interpolation to generate intermediate images, and run the NEB with the same DFT parameters. Extract the minimum energy barrier from the converged path.
- Evidence: `/app/outputs/neb_migration.log`

### Step 6: NEB barriers for SW1-N Stone-Wales defect
- Role: process
- Action: Set up a NEB calculation with the relaxed pristine cell and the relaxed SW1-N defect cell as endpoints. Generate a plausible bond-rotation path for the CN bond and run the NEB. Extract both the forward (formation) and reverse (healing) energy barriers.
- Evidence: `/app/outputs/neb_sw.log`

### Step 7: Compile results into scored CSV
- Role: scored (load-bearing)
- Action: Using the total energies and magnetic moments from defect relaxations, the barrier values from the NEB calculations, and the reference chemical potentials, compute formation energies via E_f = E_defect + Σ n_X μ_X − E_pristine. Populate a CSV file with rows for C1, C3, N1, B1, C5, CC1 (columns: defect, formation_energy, total_magnetic_moment). Add extra rows for barriers: 'C1_N1' with formation_energy = migration barrier (magnetic_moment empty), 'SW1N_formation' with formation_energy = SW1-N formation barrier, 'SW1N_healing' with formation_energy = SW1-N healing barrier.
- Output file: `/app/outputs/defect_properties.csv`
- Format: csv
- Contract: Columns: defect (string), formation_energy (numeric, eV), total_magnetic_moment (numeric, μB). Rows for C1, C3, N1, B1, C5, CC1. Additional rows: 'C1_N1' with formation_energy = migration barrier and magnetic_moment empty; 'SW1N_formation' with formation_energy = SW1-N formation barrier; 'SW1N_healing' with formation_energy = SW1-N healing barrier.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_properties.csv
- path: `/app/outputs/defect_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The scored CSV file with computed formation energies and magnetic moments for single and double vacancies, and barrier energies for vacancy migration and Stone-Wales defect formation/healing. Values are compared to the paper's reported numbers within hidden tolerances; relative ordering trends are also verified.
- schema:
  - `type`: table
  - `required`:
    - `defect`: string
    - `formation_energy`: numeric
    - `total_magnetic_moment`: numeric
  - `required_columns`: `defect`, `formation_energy`, `total_magnetic_moment`
  - `units`:
    - `formation_energy`: eV
    - `total_magnetic_moment`: μB

Notes: The CSV file must contain all listed rows. The formation_energy column holds both defect formation energies and barrier values (for the barrier rows). The total_magnetic_moment column is empty for barrier rows. The exact schema and rows are detailed in the step description.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required": {
          "defect": "string",
          "formation_energy": "numeric",
          "total_magnetic_moment": "numeric"
        },
        "required_columns": [
          "defect",
          "formation_energy",
          "total_magnetic_moment"
        ],
        "units": {
          "formation_energy": "eV",
          "total_magnetic_moment": "μB"
        }
      },
      "description": "The scored CSV file with computed formation energies and magnetic moments for single and double vacancies, and barrier energies for vacancy migration and Stone-Wales defect formation/healing. Values are compared to the paper's reported numbers within hidden tolerances; relative ordering trends are also verified."
    }
  ],
  "notes": "The CSV file must contain all listed rows. The formation_energy column holds both defect formation energies and barrier values (for the barrier rows). The total_magnetic_moment column is empty for barrier rows. The exact schema and rows are detailed in the step description."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact and combines the scores by predetermined weights to produce a final reward in [0,1]. The verifier compares your computed formation energies, magnetic moments, and barriers against hidden reference values derived from the literature. It also checks that the relative ordering of the reported defect energies and the general characteristics of the barriers (e.g., their magnitudes relative to each other) are physically reasonable for this material system. Simply reporting a number is insufficient; you must execute the full workflow and record evidence at each step. The scoring rewards correct absolute values together with the reproduction of the expected qualitative trends.
