# Planar Cohesive Energy Calculation for Al/AlAs(001) Interfaces

## Problem background
The epitaxial growth of Al thin films on AlAs(001) substrates can yield different stacking sequences, and the relative stability of these sequences is relevant for metal/semiconductor heterostructure devices. Adding a single monolayer of In at the interface can influence the preferred epitaxial relationship. This task computes planar cohesive energies from an empirical interatomic potential to quantify the energetics of these interfaces under coherent growth.

## Approach
The core idea is to use a universal empirical interatomic potential (the form given by Khor and Das Sarma) with parameters specifically fitted for Al, As, and In (Ito et al., J. Appl. Phys. 77, 4845, 1995). You will construct atomic configurations for four Al/AlAs(001) stacking sequences (denoted Al(001), Al(001)L, Al(110), Al(110)R) and for two sequences with 1 monolayer In at the interface (Al(001)/In and Al(110)/In). The substrate is AlAs(001) with the zinc blende structure, and the in‑plane lattice constant is fixed to that of AlAs (coherent growth). For each system, you relax the atomic positions and the out‑of‑plane lattice parameter by minimizing the total energy. From the relaxed geometries you then compute, for each atomic layer starting from the substrate side, the planar cohesive energy per atom and output all energies in a structured CSV file.

## Reproduction target
Produce a CSV file containing the layer‑resolved planar cohesive energies for all six interface configurations. The file must have exactly 60 rows (6 phases × 10 layers each) with columns: `phase` (string), `layer_index` (integer, 0‑based), `layer_label` (string, chemical symbol), and `energy` (float, eV/atom). The generated energies will be compared against hidden reference values to assess the accuracy of the computation.

## Assets

- Universal empirical interatomic potential parameters for Al, As, In: 10.1063/1.359508
- AlAs zinc blende crystal structure and lattice constant

## Workflow steps

### Step 1: Construct atomic configurations and perform geometry relaxation
- Role: process
- Action: Construct initial atomic coordinates for Al(001), Al(001)L, Al(110), Al(110)R on AlAs(001) and for Al(001) and Al(110) with 1 ML In at the interface, under coherent growth (in‑plane lattice fixed to AlAs lattice parameter). Relax atomic positions and out‑of‑plane (c‑axis) lattice parameter to minimize total energy using the universal empirical interatomic potential V_ij. Produce relaxed coordinates as evidence.
- Evidence: `/app/outputs/relaxed_coordinates.xyz`

### Step 2: Compute planar cohesive energies
- Role: scored (load-bearing)
- Action: For each relaxed configuration from step_01, compute the planar cohesive energy per atom for each atomic layer (starting from the substrate) and write all energies to a CSV file.
- Output file: `/app/outputs/planar_energies.csv`
- Format: csv
- Contract: Columns: phase (string), layer_index (int, 0‑based), layer_label (string, chemical symbol), energy (float, eV/atom). 60 rows total (6 phases × 10 layers each).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/planar_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### planar_energies.csv
- path: `/app/outputs/planar_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Layer‑resolved planar cohesive energies for Al(001), Al(001)L, Al(110), Al(110)R, Al(001)/In, and Al(110)/In on AlAs(001) under coherent growth. The hidden checker compares each energy to the paper‑reported values with an absolute tolerance and computes the interface energy differences (Al(001)−Al(110) without In and with In) to verify the headline stability claim.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `layer_index`, `layer_label`, `energy`
  - `units`:
    - `energy`: eV/atom

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "planar_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "layer_index",
          "layer_label",
          "energy"
        ],
        "units": {
          "energy": "eV/atom"
        }
      },
      "description": "Layer‑resolved planar cohesive energies for Al(001), Al(001)L, Al(110), Al(110)R, Al(001)/In, and Al(110)/In on AlAs(001) under coherent growth. The hidden checker compares each energy to the paper‑reported values with an absolute tolerance and computes the interface energy differences (Al(001)−Al(110) without In and with In) to verify the headline stability claim."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `planar_energies.csv` and independently compares each energy value to unpublished reference values using an absolute tolerance. It also computes the interface energy difference between Al(001) and Al(110) at the interface layer, both without In and with In, and compares those differences to hidden target values. The overall score is a weighted combination of per‑layer matches and the correctness of the energy differences. Simply reporting numbers without actually performing the configuration, relaxation, and energy calculation will not yield correct values; the verifier checks that your CSV is complete and that the values are physically plausible and match the expected pattern. The exact tolerances and reference values are not disclosed.
