# Spin-polarized DFT study of Si doping in a Heusler supercell

## Problem background
The quaternary Heusler alloy CoFeTiAl is a compensated semiconductor with a non-magnetic ground state. Substituting a small fraction of the aluminium atoms by silicon introduces extra valence electrons without a local magnetic ion, potentially inducing a diluted ferromagnetic state through spin-splitting of the electronic bands. First-principles density functional theory (DFT) calculations are used to investigate how Si doping alters the electronic structure, the magnetic moment per formula unit, and the band gap. This task asks you to perform those DFT calculations on a Si-doped supercell and extract the resulting magnetic and electronic properties.

## Approach
Use spin-polarized plane-wave DFT with the generalized gradient approximation in the Perdew–Burke–Ernzerhof (GGA-PBE) parametrisation and ultrasoft pseudopotentials. Build a 2×2×2 supercell of the quaternary Heusler structure (Co at A, Fe at C, Ti at B, Al at D) and replace one Al atom by Si, corresponding to a doping level x = 3.125%. Relax the atomic positions and lattice parameters to their equilibrium values, then perform a self-consistent field (SCF) calculation to obtain the ground-state charge and spin densities. From the SCF output, extract the magnetic moment on each atom. Run a non-self-consistent spin-resolved density of states (DOS) calculation on a fine k-point mesh covering an energy window of at least ±5 eV around the Fermi level. From the DOS, determine the band gap by identifying the highest occupied and lowest unoccupied states across both spin channels. Workflow steps below detail the exact artefacts to produce.

## Reproduction target
Compute the total magnetic moment per formula unit of CoFeTiAl with 3.125% Si doping (one Si atom in a 2×2×2 supercell) from spin-polarized DFT and write it to `moment_per_fu.txt`. Output the per-atom magnetic moments in `atomic_moments.csv` and the spin-resolved total density of states in `dos_data.csv`. From the DOS data, extract the band gap and write it to `bandgap.txt`. These four artefacts constitute the primary numerical evidence for the electronic and magnetic state of the doped system.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- SSSP pseudopotentials for Co, Fe, Ti, Al, Si (GGA-PBE ultrasoft): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Prepare Si-doped supercell structure
- Role: process
- Action: Build a 2×2×2 supercell of CoFeTiAl with the quaternary Heusler structure (Co at A, Fe at C, Ti at B, Al at D) and experimental lattice parameter ~5.8551 Å. Replace one Al atom by Si to obtain the Si doping level of x=3.125%. Output the initial atomic coordinates in a standard format suitable for DFT input.
- Evidence: `/app/outputs/supercell.cif`

### Step 2: Geometry optimization
- Role: process
- Action: Perform spin-polarized DFT geometry relaxation of the Si-doped supercell using GGA-PBE exchange-correlation functional and suitable ultrasoft pseudopotentials. Allow cell shape and atomic positions to relax until forces are converged.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 3: Spin-polarized SCF and DOS calculation
- Role: process
- Action: Using the relaxed structure, run a spin-polarized self-consistent field (SCF) calculation followed by a non-self-consistent density-of-states (DOS) calculation on a fine k-point mesh to obtain the spin-resolved total density of states over an energy range of at least [-5,5] eV around the Fermi level.
- Evidence: `/app/outputs/scf_output.log`

### Step 4: Extract atomic magnetic moments
- Role: scored (load-bearing)
- Action: From the SCF output, parse the magnetic moment on each atom and write a CSV file with columns: atom_index, species, magnetic_moment (μ_B). Every atom in the supercell must appear as one row.
- Output file: `/app/outputs/atomic_moments.csv`
- Format: csv
- Contract: CSV with header: atom_index, species, magnetic_moment
- Scoring: scored by hidden verifier

### Step 5: Compute total magnetic moment per formula unit
- Role: scored
- Action: Sum all atomic moments from atomic_moments.csv and divide by 32 (the number of formula units in the supercell) to obtain the total magnetic moment per formula unit (μ_B/f.u.). Write this single floating-point number to a text file.
- Output file: `/app/outputs/moment_per_fu.txt`
- Format: txt
- Contract: A single floating-point number
- Scoring: scored by hidden verifier

### Step 6: Output spin-resolved density of states
- Role: scored (load-bearing)
- Action: From the computed DOS data, generate a CSV file with columns: energy (eV), spin_up_dos (states/eV), spin_down_dos (states/eV). The energy range must cover at least -5 eV to +5 eV relative to the Fermi level.
- Output file: `/app/outputs/dos_data.csv`
- Format: csv
- Contract: CSV with header: energy, spin_up_dos, spin_down_dos
- Scoring: scored by hidden verifier

### Step 7: Extract band gap
- Role: scored
- Action: From dos_data.csv, identify the highest occupied energy (below the Fermi level) and the lowest unoccupied energy (above the Fermi level) across both spin channels. Compute the band gap in eV and write it to a text file.
- Output file: `/app/outputs/bandgap.txt`
- Format: txt
- Contract: A single floating-point number
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/atomic_moments.csv`
- `/app/outputs/moment_per_fu.txt`
- `/app/outputs/dos_data.csv`
- `/app/outputs/bandgap.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### atomic_moments.csv
- path: `/app/outputs/atomic_moments.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-atom magnetic moments from the spin-polarized DFT calculation. The checker will recompute the total magnetic moment and check delocalization.
- schema:
  - `type`: table
  - `required_columns`: `atom_index`, `species`, `magnetic_moment`
  - `units`:
    - `magnetic_moment`: μ_B

### moment_per_fu.txt
- path: `/app/outputs/moment_per_fu.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Agent-reported total magnetic moment per formula unit (μ_B/f.u.). The checker compares it to the value recomputed from atomic_moments.csv.
- schema:
  - `type`: text

### dos_data.csv
- path: `/app/outputs/dos_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spin-resolved total density of states over [-5,5] eV around the Fermi level. The checker recomputes the band gap from this data.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `spin_up_dos`, `spin_down_dos`
  - `units`:
    - `energy`: eV
    - `spin_up_dos`: states/eV
    - `spin_down_dos`: states/eV

### bandgap.txt
- path: `/app/outputs/bandgap.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Agent-reported band gap in eV. The checker compares it to the value recomputed from dos_data.csv.
- schema:
  - `type`: text

Notes: The checker recomputes the total magnetic moment from atomic_moments.csv by summing all atomic moments and dividing by 32, then compares against the paper's reported value. It also verifies that all atomic moments are below 0.01 μ_B (delocalization). The band gap is recomputed from dos_data.csv as the difference between the highest occupied and lowest unoccupied states across both spin channels and compared against the paper's reported gap. Both comparisons use appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "atomic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom_index",
          "species",
          "magnetic_moment"
        ],
        "units": {
          "magnetic_moment": "μ_B"
        }
      },
      "description": "Per-atom magnetic moments from the spin-polarized DFT calculation. The checker will recompute the total magnetic moment and check delocalization."
    },
    {
      "file": "moment_per_fu.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text"
      },
      "description": "Agent-reported total magnetic moment per formula unit (μ_B/f.u.). The checker compares it to the value recomputed from atomic_moments.csv."
    },
    {
      "file": "dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "spin_up_dos",
          "spin_down_dos"
        ],
        "units": {
          "energy": "eV",
          "spin_up_dos": "states/eV",
          "spin_down_dos": "states/eV"
        }
      },
      "description": "Spin-resolved total density of states over [-5,5] eV around the Fermi level. The checker recomputes the band gap from this data."
    },
    {
      "file": "bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text"
      },
      "description": "Agent-reported band gap in eV. The checker compares it to the value recomputed from dos_data.csv."
    }
  ],
  "notes": "The checker recomputes the total magnetic moment from atomic_moments.csv by summing all atomic moments and dividing by 32, then compares against the paper's reported value. It also verifies that all atomic moments are below 0.01 μ_B (delocalization). The band gap is recomputed from dos_data.csv as the difference between the highest occupied and lowest unoccupied states across both spin channels and compared against the paper's reported gap. Both comparisons use appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently recomputes the total magnetic moment per formula unit by summing all atomic moments in `atomic_moments.csv` and dividing by 32, then compares the result to a reference value. It also recomputes the band gap from `dos_data.csv` and compares to a second reference value. Additional structural checks (e.g., that the magnetic moment is delocalised, that DOS data are non-negative and cover the required energy range) contribute a small fraction of the score. Each stage's contribution is weighted and summed to a final reward between 0 and 1. Merely reporting numbers without the underlying DFT artefacts will not yield a positive score.
