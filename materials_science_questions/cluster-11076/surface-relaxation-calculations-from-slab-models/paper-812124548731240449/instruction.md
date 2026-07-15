## Problem background
Surface relaxation of fcc (001) metal surfaces is a fundamental phenomenon where the spacing between atomic layers near the surface deviates from the bulk interlayer distance. Understanding whether a surface undergoes outward expansion or inward contraction, and by how much, is important for predicting surface properties such as surface energy and reactivity. This task investigates multilayer relaxations for ten fcc metals using an atomistic potential approach.

## Approach
The modified embedded atom method (MEAM) is used as the interatomic potential. MEAM includes angular-dependent electron density contributions, making it capable of describing directional bonding. The total energy expression and embedding functions are taken from the original MEAM formalism (Baskes, Phys. Rev. B 46, 2727, 1992). Element-specific parameters (sublimation energy, equilibrium distance, decay factors, weighting factors) for the ten metals Cu, Ag, Au, Ni, Pd, Pt, Al, Pb, Rh, Ir are published in that work and should be used.

A slab model of the (001) surface is constructed for each metal: 21 atomic layers with 15×15 atoms per layer, periodic in the surface plane. The five central layers are fixed at bulk positions, while the top eight and bottom eight layers are allowed to relax only their z-coordinates (perpendicular to the surface). The total energy is minimized with respect to the relaxed z-coordinates using a gradient technique, yielding the relaxed atomic structure. From the relaxed and ideal structures, the interlayer spacing changes Δd_{n,n+1} (in % relative to bulk) for the first five interlayer pairs, and the surface energies (relaxed and unrelaxed, in mJ/m²) are computed.

## Reproduction target
For each of the ten fcc metals, perform the slab relaxation and compute: Δd12, Δd23, Δd34, Δd45, Δd56 (percent change in interlayer spacing), and the relaxed and unrelaxed surface energies. Write the results to a CSV file. The verifier will check these quantities against a trusted reference.

## Assets
- **LAMMPS** (Large-scale Atomic/Molecular Massively Parallel Simulator): required tool for energy minimization. Download from https://www.lammps.org/download.html.
- **Python 3** with standard numerical libraries (numpy, pandas) for post-processing.

## Workflow steps

### Step 1: Prepare MEAM potential and slab inputs
- Role: process
- Action: Set up the MEAM potential for each of the ten metals using the published parameter set. Create LAMMPS input scripts to build the 21-layer (001) slab with 15×15 atoms per layer, fix the middle five layers, and define the energy minimization that only relaxes z-coordinates.
- Evidence: `/app/outputs/setup_summary.json`

### Step 2: Run slab relaxation simulations
- Role: process
- Action: For each metal, run LAMMPS to perform the energy minimization and obtain the relaxed atomic coordinates. Also compute the total energy of the unrelaxed slab. Collect the final energies and relaxed z-positions.
- Evidence: `/app/outputs/relaxation_output.log`

### Step 3: Compute interlayer relaxations and surface energies
- Role: scored (load-bearing)
- Action: From the relaxed and unrelaxed data, calculate the percentage changes in interlayer spacing Δd12 through Δd56 relative to the bulk interlayer spacing for each metal, and the surface energies (relaxed and unrelaxed) in mJ/m². Write the results to a CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: One row per metal. Columns: `metal`, `Δd12_percent`, `Δd23_percent`, `Δd34_percent`, `Δd45_percent`, `Δd56_percent`, `surface_energy_relaxed`, `surface_energy_unrelaxed`. All values are floats except `metal` (string).
- Scoring: scored by hidden verifier

## Output files
- `/app/outputs/results.csv` (scored)
- `/app/outputs/setup_summary.json` (evidence for Step 1)
- `/app/outputs/relaxation_output.log` (evidence for Step 2)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed interlayer spacing changes (percent) and surface energies for ten fcc metals.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `Δd12_percent`, `Δd23_percent`, `Δd34_percent`, `Δd45_percent`, `Δd56_percent`, `surface_energy_relaxed`, `surface_energy_unrelaxed`
  - `units`:
    - `Δd12_percent`: %
    - `Δd23_percent`: %
    - `Δd34_percent`: %
    - `Δd45_percent`: %
    - `Δd56_percent`: %
    - `surface_energy_relaxed`: mJ/m²
    - `surface_energy_unrelaxed`: mJ/m²

Notes: The hidden verifier compares each value to a trusted reference derived from the paper's reported MEAM results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "Δd12_percent",
          "Δd23_percent",
          "Δd34_percent",
          "Δd45_percent",
          "Δd56_percent",
          "surface_energy_relaxed",
          "surface_energy_unrelaxed"
        ],
        "units": {
          "Δd12_percent": "%",
          "Δd23_percent": "%",
          "Δd34_percent": "%",
          "Δd45_percent": "%",
          "Δd56_percent": "%",
          "surface_energy_relaxed": "mJ/m²",
          "surface_energy_unrelaxed": "mJ/m²"
        }
      },
      "description": "Computed interlayer spacing changes (percent) and surface energies for ten fcc metals."
    }
  ],
  "notes": "The hidden verifier compares each value to a trusted reference derived from the paper's reported MEAM results."
}
```

## How you are scored
A hidden verifier reads your output CSV and compares each value (interlayer spacing changes and surface energies) against a trusted reference. The agreement is assessed with appropriate tolerances; reporting paper numbers without genuinely running the relaxations will not pass. The reward is the weighted combination of these checks.
