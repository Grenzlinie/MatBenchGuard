# Doping-driven magnetic phase diagram of monolayer MnCl2 from first-principles spin-spiral calculations

## Problem background
Monolayer manganese dichloride (MnCl2) is a two-dimensional transition metal dihalide that can host multiple magnetic orders, including ferromagnetic (FM), antiferromagnetic (AFM), and spiral (SP) states. Due to its potential for spintronic applications, understanding how carrier doping—introducing extra electrons or holes—shifts the magnetic ground state among these phases is of great interest. A possible doping-driven phase sequence has been predicted in this material, but the precise boundaries and the energy scales involved require first-principles verification. The goal of this task is to compute, from first principles, the magnetic ground state of monolayer MnCl2 as a function of lattice constant and carrier doping, producing a phase diagram that maps out the stable magnetic phases and their energetic competition.

## Approach
The ground state magnetic order in monolayer MnCl2 can be captured by spin-spiral density functional theory (DFT) calculations using the Generalized Bloch Theorem (GBT). In this approach, the magnetic moment of the Mn atoms rotates along a spiral vector q, parameterized by a dimensionless number φ that runs from 0 (ferromagnetic alignment, all spins parallel) to 1 (antiferromagnetic alignment, nearest-neighbour spins antiparallel). Intermediate values correspond to spiral configurations. For each chosen lattice constant and carrier doping, the total energy is computed as a function of φ. By comparing the energies of different spiral states, one identifies the φ that minimizes the total energy, from which the magnetic ground state (FM, AFM, or SP) and the energy difference relative to the ferromagnetic reference are extracted. Repeating this procedure across four distinct lattice constants and over a range of hole and electron doping values yields a phase diagram showing how the stable magnetic order changes with doping and lattice strain.

## Reproduction target
Produce a phase diagram of monolayer MnCl2 as a function of doping. Specifically, for each of the four lattice constants a = 3.501 Å, 3.686 Å, 3.747 Å, and 3.825 Å, and for doping levels d from -0.5 to +0.5 e/cell (step no larger than 0.05), determine the ground state magnetic phase by finding the spiral parameter φ that yields the lowest total energy. For every (a, d) pair compute ΔE = E(φ=0) − E(φ_lowest), i.e., the energy of the ferromagnetic state relative to the ground state. Report all results in a single CSV file with columns a (Å), d (e/cell), ground_state (string: FM, AFM, or SP), phi_lowest (float), and delta_E (eV). The file must contain one row per (a, d) combination and serve as the scored artifact for this task.

## Assets

- OPENMX (Open source package for Material eXplorer): http://www.openmx-square.org/

## Workflow steps

### Step 1: Model and input preparation
- Role: process
- Action: Construct the primitive unit cell of monolayer 1T-MnCl2 for lattice constants a=3.501, 3.686, 3.747, 3.825 Å with a vacuum layer. Prepare OPENMX input files for GBT spin-spiral calculations: appropriate pseudopotentials, basis sets, k-point mesh, cutoff energy, and doping levels d from -0.5 to 0.5 e/cell in steps ≤0.05. Define spiral vectors φ from 0 (FM) to 1 (AFM) with sufficient resolution to resolve the ground state.
- Evidence: none

### Step 2: DFT total energy calculations
- Role: process
- Action: Run self-consistent OPENMX total energy calculations for every combination of lattice constant a, doping d, and spiral vector φ. Record total energy E(a,d,φ) for all (a,d,φ) combinations. Use the same computational parameters (basis, k-mesh, cutoff) as in the model setup.
- Evidence: `/app/outputs/raw_energies.csv`

### Step 3: Extract magnetic phase diagram
- Role: scored (load-bearing)
- Action: For each (a,d) pair, find the spiral vector φ_lowest that minimises the total energy among all computed φ values. Compute ΔE = E(φ=0) − E(φ_lowest). Determine the ground state: 'FM' if φ_lowest=0, 'AFM' if φ_lowest=1, otherwise 'SP'. Output a CSV file with columns a, d, ground_state, phi_lowest, delta_E.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: a (float, Å), d (float, e/cell), ground_state (string, one of FM, AFM, SP), phi_lowest (float), delta_E (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The magnetic ground state (FM, AFM, SP) for each lattice constant and doping value, together with the minimising spiral parameter φ and the energy difference ΔE.
- schema:
  - `type`: table
  - `required_columns`: `a`, `d`, `ground_state`, `phi_lowest`, `delta_E`
  - `units`:
    - `a`: Å
    - `d`: e/cell
    - `delta_E`: eV

Notes: The phase diagram is derived from total-energy spin-spiral DFT calculations using the GBT. The checker will recompute phase intervals and compare them to hidden reference intervals with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "a",
          "d",
          "ground_state",
          "phi_lowest",
          "delta_E"
        ],
        "units": {
          "a": "Å",
          "d": "e/cell",
          "delta_E": "eV"
        }
      },
      "description": "The magnetic ground state (FM, AFM, SP) for each lattice constant and doping value, together with the minimising spiral parameter φ and the energy difference ΔE."
    }
  ],
  "notes": "The phase diagram is derived from total-energy spin-spiral DFT calculations using the GBT. The checker will recompute phase intervals and compare them to hidden reference intervals with appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your submitted phase_diagram.csv and independently checks the magnetic phase assignments and energy differences. The verifier derives phase intervals from your data and compares them against reference intervals; it also checks the ΔE values for consistency. Each stage’s artifact is evaluated, and the final reward (0 to 1) is a weighted combination that rewards correctly identified phase regions and accurate ΔE values while penalizing missing or inconsistent results. Simply reporting a number from the literature is not enough—your solution must be derived from a self-consistent computational workflow as described in the steps above.
