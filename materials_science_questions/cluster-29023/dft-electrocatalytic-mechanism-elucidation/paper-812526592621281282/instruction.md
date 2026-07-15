# DFT-Based Study of Doping Effects on the Oxygen Reduction Reaction on Co–gN₄

## Problem background
The oxygen reduction reaction (ORR) is the key cathode process in fuel cells, and improving its kinetics is critical for device performance. Single-atom catalysts (SACs) with a Co–N₄ moiety embedded in a graphene matrix (Co–gN₄) are a promising class of platinum-free catalysts. Doping the carbon support with non-metal elements (e.g., B, N, P) can alter the electronic structure and adsorption properties, potentially improving ORR activity. Density functional theory (DFT) combined with the computational hydrogen electrode (CHE) model provides a route to compute free-energy profiles, overpotentials, and charge distributions, allowing systematic investigation of doping effects. This task undertakes such a computational study for undoped Co–gN₄ and for two representative doped variants.

## Approach
Construct periodic slab models of a monolayer graphene supercell containing a Co–N₄ moiety. Doped models are created by substituting a carbon atom adjacent to nitrogen with B (BNC‑1) or P (PNC‑1). For each catalyst variant, perform spin-polarized DFT calculations with a GGA-PBE functional and a dispersion correction. Geometry optimizations and vibrational frequency analyses are carried out for the clean surface and for each adsorbed ORR intermediate (O₂*, OOH*, O*, OH*). Gibbs free energies are obtained at T = 298.15 K by adding zero-point energy and entropy corrections to the electronic total energies. Using the CHE model at U = 0 V and pH = 0, the free energies of the intermediates are referenced to H₂O and H₂, yielding the free-energy diagram. The overpotential is derived from the largest positive free-energy change among the four proton–electron transfer steps. Mulliken population analysis yields the atomic charge on the Co center. The entire workflow is performed with open‑source DFT tools (e.g., Quantum ESPRESSO) and is applicable to any periodic DFT code supporting the required functionals and corrections.

## Reproduction target
Compute and report the ORR free-energy profile for undoped Co–gN₄, BNC‑1, and PNC‑1. Specifically, for each catalyst produce the Gibbs free energies of the four intermediates (O₂*, OOH*, O*, OH*) at U = 0 V relative to the clean surface and H₂O/H₂ references, calculate the overall overpotential (in V), and extract the Mulliken charge of the Co atom (in e). Collect all results into a single CSV file, `/app/outputs/orr_data.csv`, with columns: Model, State_2 (eV), State_3 (eV), State_4 (eV), State_5 (eV), Overpotential (V), Co_Mulliken_charge.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
- PBE pseudopotential library (e.g., SSSP, PSlibrary): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build atomistic models for undoped Co–gN₄, BNC-1, and PNC-1
- Role: process
- Action: Construct periodic slab models: a monolayer graphene supercell (94 C atoms) with lattice a=14.76 Å, b=17.0434 Å, c=20.0 Å. Introduce a Co–N₄ moiety by replacing a C₆ ring with Co coordinated to four N atoms. For BNC-1, replace the carbon atom at site 1 (adjacent to N) with B; for PNC-1, replace it with P. Output geometry files for subsequent DFT runs.
- Evidence: `/app/outputs/initial_structures.extxyz`

### Step 2: DFT geometry optimization and vibrational frequency analysis
- Role: process
- Action: Perform spin-polarized DFT relaxations for the clean surface of each model and for the four adsorbed states (O₂*, OOH*, O*, OH*) on each catalyst. Use GGA-PBE functional with dispersion correction and a 5×4×1 k-point grid. Converge forces to <0.02 eV/Å. For the clean surfaces and each adsorbed state, compute harmonic vibrational frequencies to obtain zero-point energies and entropies (T=298.15 K) for free energy corrections.
- Evidence: `/app/outputs/optimized_trajectories.tar.gz`

### Step 3: Compute total energies and Mulliken charges
- Role: process
- Action: From the optimized geometries, run single-point energy calculations to obtain the total energies of the clean slab and each adsorbed state. Perform Mulliken population analysis to extract the atomic charge on Co. Also record the vibrational free-energy contributions (ZPE – TΔS) for each state.
- Evidence: `/app/outputs/raw_dft_data.json`

### Step 4: Compile ORR free-energy profile and overpotential into CSV
- Role: scored (load-bearing)
- Action: Compute the Gibbs free energies of O₂*, OOH*, O*, OH* relative to the clean surface and the H₂O/H₂ references using the computational hydrogen electrode model at U=0 V. Determine the free-energy diagram for each catalyst and identify the potential-limiting step and overpotential. Collect the state energies (ΔG for steps 2–5), overpotential, and Co Mulliken charge for the undoped, BNC-1, and PNC-1 models. Write the data to /app/outputs/orr_data.csv.
- Output file: `/app/outputs/orr_data.csv`
- Format: csv
- Contract: Columns: Model (string), State_2 (float eV), State_3 (float eV), State_4 (float eV), State_5 (float eV), Overpotential (float V), Co_Mulliken_charge (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/orr_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### orr_data.csv
- path: `/app/outputs/orr_data.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed free energies of ORR intermediates at U=0 V (steps 2–5), overpotential, and Co Mulliken charge for undoped Co–gN₄, BNC-1, and PNC-1. The checker verifies that overpotentials meet paper-consistent thresholds and that the Mulliken charge trend matches the paper-derived direction.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `State_2`, `State_3`, `State_4`, `State_5`, `Overpotential`, `Co_Mulliken_charge`
  - `units`:
    - `State_2`: eV
    - `State_3`: eV
    - `State_4`: eV
    - `State_5`: eV
    - `Overpotential`: V
    - `Co_Mulliken_charge`: e

Notes: Scoring combines threshold-or-better for overpotentials and a trend check for Mulliken charges. The potential-limiting step must be consistent with the hidden paper-derived profile (the checker will compute the step from the free energies). Tolerances are chosen to accommodate different DFT implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "orr_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "State_2",
          "State_3",
          "State_4",
          "State_5",
          "Overpotential",
          "Co_Mulliken_charge"
        ],
        "units": {
          "State_2": "eV",
          "State_3": "eV",
          "State_4": "eV",
          "State_5": "eV",
          "Overpotential": "V",
          "Co_Mulliken_charge": "e"
        }
      },
      "description": "Computed free energies of ORR intermediates at U=0 V (steps 2–5), overpotential, and Co Mulliken charge for undoped Co–gN₄, BNC-1, and PNC-1. The checker verifies that overpotentials meet paper-consistent thresholds and that the Mulliken charge trend matches the paper-derived direction."
    }
  ],
  "notes": "Scoring combines threshold-or-better for overpotentials and a trend check for Mulliken charges. The potential-limiting step must be consistent with the hidden paper-derived profile (the checker will compute the step from the free energies). Tolerances are chosen to accommodate different DFT implementations."
}
```

## How you are scored
Your submission is scored by a hidden verifier that inspects `/app/outputs/orr_data.csv`. The verifier evaluates: (1) whether the overpotential for each catalyst meets hidden paper-derived thresholds (tolerances accounting for legitimate DFT-toolchain spread), (2) that the potential-limiting step (as determined from the free-energy profile) is consistent with the paper's expected rate-determining step, and (3) that the relative trend in Co Mulliken charge between BNC‑1 and undoped Co–gN₄ matches the hidden direction. The exact limiting step and the sign of the trend are not disclosed. The scores from these checks are combined into a final reward between 0 and 1. The intermediate process steps (model building, DFT optimizations, raw data collection) are not individually scored, but their successful execution is required to produce a valid scored artifact.
