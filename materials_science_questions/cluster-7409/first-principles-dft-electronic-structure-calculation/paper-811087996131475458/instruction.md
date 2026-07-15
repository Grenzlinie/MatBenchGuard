# Ti-Interstitial-Induced Oxygen Aggregation and Conduction Path in TiO2 via Car-Parrinello Molecular Dynamics

## Problem background
Titanium dioxide (TiO₂) is a key material for resistive random-access memory (ReRAM), where conductive filaments control resistance switching.   Ti interstitials are one type of defect that can alter the local bonding and electronic structure. This task investigates the atomic-scale dynamics of a rutile TiO₂ system containing two Ti interstitials, using Car–Parrinello molecular dynamics (CPMD).   The goal is to determine how the interstitial ions evolve over time and whether they induce local changes such as charge redistribution on oxygen ions, changes in Ti–Ti connectivities, and modifications of the electronic band gap.   The simulation output will reveal the time-resolved structural and electronic properties that underlie possible conduction path formation.

## Approach
A first-principles Car–Parrinello molecular dynamics simulation is performed on a 2×2×4 rutile TiO₂ supercell with two Ti interstitials at specified positions.   The simulation is carried out with a plane-wave DFT code, using a PBE exchange-correlation functional, a plane-wave cutoff of 70 Ry, a fictitious electron mass of 500 a.u., and a time step of 0.1 fs.   After pre-heating to 300 K, a Nosé–Hoover thermostat runs for 3 ps.   Snapshot geometries are extracted at five time points (0, 0.5, 1, 2, 3 ps).   For each snapshot, a single-point DFT calculation with spin polarization and a 3×3×2 k-point grid provides per-atom Mulliken charges, Cartesian coordinates, and the Kohn–Sham band gap.   From the raw data, the evolution of oxygen ion aggregation (identified by positive Mulliken charge and short O–O distances) and Ti–Ti bonding character along the [010] direction, as well as the band gap trend, are compiled.   These observables are the quantitative foundation for assessing the formation of a conduction path.

## Reproduction target
You must produce two scored artifacts from the CPMD simulation and post-processing:
- A CSV file (`mulliken_and_positions.csv`) containing, for every atom at each snapshot, the time, atom index, element, Cartesian coordinates (x,y,z in Å), and Mulliken charge (in e).
- A plain text file (`band_gaps.txt`) listing the snapshot time and the Kohn–Sham band gap (eV) on each line.

The hidden verifier will read these raw outputs and independently recompute:
- The time evolution of oxygen-ion pairs (O–O distance below a threshold and both atoms carrying a positive Mulliken charge), to see whether the number of such pairs changes across the snapshots.
- Whether Ti–Ti bonds along the [010] direction (with distances in a certain range) appear at later snapshots, indicating a connected conduction path.
- Whether the band gap of the equilibrated (later-time) snapshots falls below a cutoff consistent with metallic character.

Your raw data must enable the verifier to carry out these checks; the trends and thresholds are hidden and will be compared to the reference behavior.

## Assets

- Open-source DFT code with Car-Parrinello MD (e.g., CP2K or Quantum ESPRESSO): https://www.cp2k.org/download or https://www.quantum-espresso.org/download
- Troullier-Martin norm-conserving pseudopotentials for Ti and O (or equivalent SG15/PseudoDojo): https://pseudopotentials.quantum-espresso.org/upf_files/
- Python scientific stack (numpy, ase): numpy,ase

## Workflow steps

### Step 1: Build initial supercell structure
- Role: process
- Action: Construct a 2×2×4 rutile TiO2 supercell (lattice a=b=9.188 Å, c=11.836 Å) from the primitive rutile cell. Insert two Ti interstitials at fractional coordinates (7.258, 7.258, 4.248) and (7.258, 7.258, 10.166). Save the atomic positions as initial_structure.xyz.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: Run Car-Parrinello molecular dynamics simulation
- Role: process
- Action: Run Car-Parrinello molecular dynamics on the initial structure using an open-source plane-wave DFT code capable of CPMD (e.g., CP2K or Quantum ESPRESSO). Settings: PBE-GGA exchange-correlation, plane-wave cutoff 70 Ry, fictitious electron mass 500 a.u., time step 0.1 fs. Pre-heat ions to 300 K, then apply Nosé-Hoover thermostat for 30000 steps (3 ps). Extract snapshot geometries at 0, 0.5, 1, 2, and 3 ps.
- Evidence: `/app/outputs/snapshots.xyz`

### Step 3: Compute per-atom Mulliken charges and atomic positions
- Role: scored (load-bearing)
- Action: For each snapshot at 0, 0.5, 1, 2, and 3 ps, perform a single-point DFT calculation with PBE, spin polarization, and a 3×3×2 k-point grid. Output a CSV file containing for every atom: time_ps, atom_index, element, x (Å), y (Å), z (Å), mulliken_charge (e).
- Output file: `/app/outputs/mulliken_and_positions.csv`
- Format: csv
- Contract: CSV with columns: time_ps (float), atom_index (int), element (str), x (float, Å), y (float, Å), z (float, Å), mulliken_charge (float, e). One row per atom per snapshot.
- Scoring: scored by hidden verifier

### Step 4: Compute Kohn-Sham band gaps
- Role: scored
- Action: For each snapshot, compute the Kohn-Sham band gap (eV) from the electronic structure calculation. Write a plain-text file with two columns: time_ps and band_gap_eV.
- Output file: `/app/outputs/band_gaps.txt`
- Format: txt
- Contract: Space-separated columns: time_ps (float) band_gap_eV (float). One row per snapshot.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mulliken_and_positions.csv`
- `/app/outputs/band_gaps.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mulliken_and_positions.csv
- path: `/app/outputs/mulliken_and_positions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-atom Mulliken charges and Cartesian coordinates for all atoms at each snapshot. The verifier recomputes O-ion pair counts (positive Mulliken charge and O-O distance < 3.0 Å) and Ti-Ti bond presence from this data.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `atom_index`, `element`, `x`, `y`, `z`, `mulliken_charge`
  - `units`:
    - `x`: Å
    - `y`: Å
    - `z`: Å
    - `mulliken_charge`: e

### band_gaps.txt
- path: `/app/outputs/band_gaps.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Kohn-Sham band gap (eV) at each snapshot. The verifier checks that for snapshots at 0.5, 1, 2, and 3 ps the band gap is ≤ 0.15 eV (metallic).
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

Notes: The verifier will recompute the O-ion pair counts and Ti-Ti bond existence from mulliken_and_positions.csv, and evaluate the band gap threshold from band_gaps.txt. No other scored outputs are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mulliken_and_positions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "atom_index",
          "element",
          "x",
          "y",
          "z",
          "mulliken_charge"
        ],
        "units": {
          "x": "Å",
          "y": "Å",
          "z": "Å",
          "mulliken_charge": "e"
        }
      },
      "description": "Per-atom Mulliken charges and Cartesian coordinates for all atoms at each snapshot. The verifier recomputes O-ion pair counts (positive Mulliken charge and O-O distance < 3.0 Å) and Ti-Ti bond presence from this data."
    },
    {
      "file": "band_gaps.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Kohn-Sham band gap (eV) at each snapshot. The verifier checks that for snapshots at 0.5, 1, 2, and 3 ps the band gap is ≤ 0.15 eV (metallic)."
    }
  ],
  "notes": "The verifier will recompute the O-ion pair counts and Ti-Ti bond existence from mulliken_and_positions.csv, and evaluate the band gap threshold from band_gaps.txt. No other scored outputs are required."
}
```

## How you are scored
A hidden grading program examines your two output files.   It extracts the O-ion pair counts, the presence of certain Ti–Ti bonds, and the band gap values from your data.   Each of these derived quantities is compared against a hidden set of expected trends and thresholds (derived from the reference study but not disclosed).   The checks are weighted; meeting each condition contributes a fraction of the total score.   The final reward is a number between 0 and 1, with higher values indicating closer agreement with the expected physical behavior.   There is no need for your code to match any particular implementation – what matters is that the structural and electronic data you provide faithfully reflects the underlying simulation results and allows the verifier to detect the relevant patterns.
