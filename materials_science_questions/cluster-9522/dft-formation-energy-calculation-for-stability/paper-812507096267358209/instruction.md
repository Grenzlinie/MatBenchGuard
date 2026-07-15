# DFT Formation Energy and d-band Center for Antiperovskite (Pd,Ni)NNi3

## Problem background
Palladium-based electrocatalysts are attractive for oxygen reduction reactions in fuel cells, but they suffer from poor stability in acidic operating conditions. An antiperovskite nitride material with nominal composition (Pd<sub>0.7</sub>Ni<sub>0.3</sub>)NNi<sub>3</sub> has been synthesised, and its thermodynamic stability and electronic structure have been investigated using density functional theory (DFT). The DFT study aims to quantify how the antiperovskite crystal structure and a Pd‑terminated surface influence bulk stability and surface catalytic activity.

## Approach
First-principles density-functional theory (DFT) with plane-wave basis sets is applied to compute total energies of different phases. The bulk formation energy of (Pd<sub>0.7</sub>Ni<sub>0.3</sub>)NNi<sub>3</sub> is determined by subtracting the total energies of elemental reference phases — fcc Pd, fcc Ni, and an isolated N<sub>2</sub> molecule — from the total energy of the relaxed antiperovskite unit cell. To assess the surface electronic activity, a slab model of the (100) surface terminated with a Pd monolayer is constructed, relaxed, and the projected density of states (PDOS) of the surface Pd atoms is computed. The d‑band center is then extracted from that PDOS by integrating the energy‑weighted density.

## Reproduction target
Carry out the DFT workflow and deliver two files in JSON format:  
- `total_energies.json`: total energies per simulation cell (eV) for the antiperovskite bulk, fcc Pd, fcc Ni, and the N<sub>2</sub> gas molecule.  
- `dband_center.json`: the d‑band center (eV) of the Pd atoms on the (100) surface slab, referenced to the Fermi level.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Standard solid-state pseudopotentials (SSSP) library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare DFT input structures
- Role: process
- Action: Generate DFT input files (pw.x input) for fcc Pd, fcc Ni, N2 molecule, and the antiperovskite (Pd0.7Ni0.3)NNi3 bulk unit cell using the lattice constant of 3.79 Å and A-site occupancy of 70% Pd.
- Evidence: `/app/outputs/input_files_generated.txt`

### Step 2: Compute elemental reference total energies
- Role: process
- Action: Run DFT total energy calculations (self-consistent) for fcc Pd, fcc Ni, and the isolated N2 molecule using Quantum ESPRESSO with SSSP pseudopotentials.
- Evidence: `/app/outputs/reference_energies.log`

### Step 3: Compute antiperovskite bulk total energy
- Role: process
- Action: Relax the antiperovskite bulk unit cell (volume relaxation) and compute its total energy using Quantum ESPRESSO.
- Evidence: `/app/outputs/bulk_relax.log`

### Step 4: Write formation energy raw data
- Role: scored
- Action: Collect the final total energies from the previous steps and write them to total_energies.json.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: Object with keys: antiperovskite (eV, float), Pd_fcc (eV, float), Ni_fcc (eV, float), N2_gas (eV, float).
- Scoring: scored by hidden verifier

### Step 5: Build Pd-terminated (100) slab model
- Role: process
- Action: Using the optimized bulk antiperovskite structure, build a (100) surface slab model with a Pd monolayer termination (Pd/ae-PdNNi).
- Evidence: `/app/outputs/slab_structure.pdb`

### Step 6: Relax slab and compute projected DOS
- Role: process
- Action: Relax the slab (fix bottom layers, relax top layers) and compute the projected density of states (PDOS) for surface Pd atoms.
- Evidence: `/app/outputs/pdos_data.dat`

### Step 7: Calculate d-band center
- Role: scored (load-bearing)
- Action: Compute the d-band center (eV) of Pd surface atoms from the PDOS using the integral of energy times density divided by total density, and save the result to dband_center.json.
- Output file: `/app/outputs/dband_center.json`
- Format: json
- Contract: Object with key d_band_center (eV, float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`
- `/app/outputs/dband_center.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energies of the reference phases and the antiperovskite bulk per simulation cell, used to recompute the formation energy.
- schema:
  - `type`: object
  - `required`:
    - `antiperovskite`: number (eV)
    - `Pd_fcc`: number (eV)
    - `Ni_fcc`: number (eV)
    - `N2_gas`: number (eV)

### dband_center.json
- path: `/app/outputs/dband_center.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The d-band center of the surface Pd atoms relative to the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `d_band_center`: number (eV)

Notes: The hidden checker recomputes the formation energy from total_energies.json and compares to a hidden reference value. The d-band center is compared directly. Tolerances are set to absorb DFT-implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "antiperovskite": "number (eV)",
          "Pd_fcc": "number (eV)",
          "Ni_fcc": "number (eV)",
          "N2_gas": "number (eV)"
        }
      },
      "description": "Total energies of the reference phases and the antiperovskite bulk per simulation cell, used to recompute the formation energy."
    },
    {
      "file": "dband_center.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "d_band_center": "number (eV)"
        }
      },
      "description": "The d-band center of the surface Pd atoms relative to the Fermi level."
    }
  ],
  "notes": "The hidden checker recomputes the formation energy from total_energies.json and compares to a hidden reference value. The d-band center is compared directly. Tolerances are set to absorb DFT-implementation spread."
}
```

## How you are scored
A hidden verifier will inspect your submitted output files. For `total_energies.json`, the verifier recomputes the bulk formation energy per formula unit from your reported total energies and compares it to an independent hidden reference value, accepting results within a predetermined tolerance. For `dband_center.json`, the verifier compares your reported d‑band center directly to a hidden reference value under a tolerance that accounts for methodology spread. Both components contribute weighted portions to a final reward between 0 and 1.
