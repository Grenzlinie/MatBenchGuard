# Reproduce ground-state U-V and V-T phase diagrams of the half-filled 3D Hubbard-Holstein model

## Problem background
The Hubbard-Holstein model describes electrons on a lattice subject to both on-site Hubbard repulsion (U) and coupling to local phonon modes (strength V). At half-filling, the competition between U and V determines whether the ground state is antiferromagnetic or charge-ordered, and whether insulating or metallic phases appear. While extensive studies exist in one and two dimensions, the three-dimensional (3D) case on an 8³ cubic lattice remains largely unexplored. This task computes the ground-state U-V phase diagram at low temperature and the V-T phase diagram at fixed U=8 for the half-filled 3D Hubbard-Holstein model using a semi-classical Monte Carlo method that treats phonons in the adiabatic limit. By calculating spin and charge structure factors, the density of states at the Fermi level, dc resistivity, and the bipolaronic order parameter across a grid of (U,V,T) parameters, the simulation resolves the phase boundaries and characterizes the various phases that emerge.

## Approach
The reproduction uses an exact diagonalization based semi-classical Monte Carlo (s-MC) approach with the traveling cluster approximation (TCA) to simulate the Hubbard-Holstein model on an 8×8×8 lattice at half-filling. The Hubbard interaction is decoupled via auxiliary classical fields (spin vectors), and the phonon degrees of freedom are treated as classical expansion/contraction modes. At each Monte Carlo step, the auxiliary fields are updated with the Metropolis algorithm, and the effective Hamiltonian is diagonalized to extract observables. Physical quantities—spin structure factor at wavevector (π,π,π), charge structure factor at (π,π,π), density of states at the Fermi level DOS(ω=0), dc resistivity (Kubo-Greenwood formula), and the bipolaronic order parameter—are recorded for every (U,V,T) configuration. Two parameter grids are required: (i) a set of (U,V) values at fixed low temperature T=0.005 to map the ground-state phase diagram, and (ii) for U=8, various V and temperatures (including T=0.005, 0.15, 0.25, 1.0) to capture the finite-temperature phase sequence. All raw simulation data are saved in a structured file and then post-processed to produce the two final scored CSV files.

## Reproduction target
Produce two CSV files that together capture the phase behavior of the half-filled 3D Hubbard-Holstein model:

1. `phase_diagram_UV.csv` — for each (U,V) point at T=0.005, report U, V, S(π,π,π), CO(π,π,π), DOS(ω=0), and dc resistivity.
2. `phase_diagram_VT_U8.csv` — for U=8, across a grid of V and T, report V, T, S(π,π,π), CO(π,π,π), DOS(ω=0), dc resistivity, and bipolaronic order parameter.

The parameter ranges should cover both antiferromagnetic and charge-ordered regimes, and the chosen V and T values should resolve the finite-temperature phases (including insulating and metallic bipolaronic states). You must implement the full microscopic simulation; the two CSV files are the only scored artifacts.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Semiclassical Monte Carlo simulation of Hubbard-Holstein model
- Role: process
- Action: Implement the semiclassical Monte Carlo method with exact diagonalization and traveling cluster approximation (TCA) for the one-band Hubbard-Holstein model on an 8×8×8 cubic lattice at half-filling. Use Metropolis updates on classical auxiliary fields (phonon coordinates, spin vectors) and solve the effective Hamiltonian at each step to obtain observables. Run for two parameter grids: (i) a grid of (U,V) values at fixed T=0.005 spanning charge-ordered and antiferromagnetic regimes, and (ii) for fixed U=8, a grid of (V,T) values (including T=0.005, 0.15, 0.25, 1.0) to capture the key phases. The (U,V) grid at T=0.005 must contain the points (U=8.4, V=4) and (U=8.5, V=4). For U=8, the (V,T) grid must include V=3.7 and 3.8 at temperatures T=0.005 and T=0.25. For each (U,V,T) point record the spin structure factor S(π,π,π), charge structure factor CO(π,π,π), density of states at the Fermi level DOS(ω=0), dc resistivity, and bipolaronic order parameter BPO. Save all raw data to /app/outputs/raw_simulation_data.npz.
- Evidence: `/app/outputs/raw_simulation_data.npz`

### Step 2: U-V ground-state phase diagram data extraction
- Role: scored (load-bearing)
- Action: From the raw data in /app/outputs/raw_simulation_data.npz, extract the observables for all (U,V) points at T=0.005. Produce a CSV file with columns: U, V, S_pi_pi_pi, CO_pi_pi_pi, DOS0, resistivity.
- Output file: `/app/outputs/phase_diagram_UV.csv`
- Format: csv
- Contract: U (float), V (float), S_pi_pi_pi (float), CO_pi_pi_pi (float), DOS0 (float), resistivity (float)
- Scoring: scored by hidden verifier

### Step 3: V-T phase diagram data extraction for U=8
- Role: scored (load-bearing)
- Action: From the raw data, extract the observables for U=8 across the required (V,T) grid. Produce a CSV file with columns: V, T, S_pi_pi_pi, CO_pi_pi_pi, DOS0, resistivity, bipolaronic_order_parameter.
- Output file: `/app/outputs/phase_diagram_VT_U8.csv`
- Format: csv
- Contract: V (float), T (float), S_pi_pi_pi (float), CO_pi_pi_pi (float), DOS0 (float), resistivity (float), bipolaronic_order_parameter (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_UV.csv`
- `/app/outputs/phase_diagram_VT_U8.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_UV.csv
- path: `/app/outputs/phase_diagram_UV.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Observables for each (U,V) at fixed T=0.005, constituting the ground-state phase diagram.
- schema:
  - `type`: table
  - `required_columns`: `U`, `V`, `S_pi_pi_pi`, `CO_pi_pi_pi`, `DOS0`, `resistivity`
  - `units`:
    - `U`: energy unit t
    - `V`: dimensionless
    - `S_pi_pi_pi`: arbitrary
    - `CO_pi_pi_pi`: arbitrary
    - `DOS0`: states per energy
    - `resistivity`: dimensionless (in units of ħ a / (π e²))

### phase_diagram_VT_U8.csv
- path: `/app/outputs/phase_diagram_VT_U8.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Observables for U=8, various V and T, forming the V-T phase diagram.
- schema:
  - `type`: table
  - `required_columns`: `V`, `T`, `S_pi_pi_pi`, `CO_pi_pi_pi`, `DOS0`, `resistivity`, `bipolaronic_order_parameter`
  - `units`:
    - `V`: dimensionless
    - `T`: temperature in units of t
    - `S_pi_pi_pi`: arbitrary
    - `CO_pi_pi_pi`: arbitrary
    - `DOS0`: states per energy
    - `resistivity`: dimensionless
    - `bipolaronic_order_parameter`: dimensionless

Notes: The hidden checker compares the agent's computed observables at key parameter points to paper-reported reference values/tolerances to verify the phase boundaries, first-order transitions, and absence of a metallic phase.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_UV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "V",
          "S_pi_pi_pi",
          "CO_pi_pi_pi",
          "DOS0",
          "resistivity"
        ],
        "units": {
          "U": "energy unit t",
          "V": "dimensionless",
          "S_pi_pi_pi": "arbitrary",
          "CO_pi_pi_pi": "arbitrary",
          "DOS0": "states per energy",
          "resistivity": "dimensionless (in units of ħ a / (π e²))"
        }
      },
      "description": "Observables for each (U,V) at fixed T=0.005, constituting the ground-state phase diagram."
    },
    {
      "file": "phase_diagram_VT_U8.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "V",
          "T",
          "S_pi_pi_pi",
          "CO_pi_pi_pi",
          "DOS0",
          "resistivity",
          "bipolaronic_order_parameter"
        ],
        "units": {
          "V": "dimensionless",
          "T": "temperature in units of t",
          "S_pi_pi_pi": "arbitrary",
          "CO_pi_pi_pi": "arbitrary",
          "DOS0": "states per energy",
          "resistivity": "dimensionless",
          "bipolaronic_order_parameter": "dimensionless"
        }
      },
      "description": "Observables for U=8, various V and T, forming the V-T phase diagram."
    }
  ],
  "notes": "The hidden checker compares the agent's computed observables at key parameter points to paper-reported reference values/tolerances to verify the phase boundaries, first-order transitions, and absence of a metallic phase."
}
```

## How you are scored
A hidden verifier reads the output CSV files and independently evaluates the physical consistency of the computed observables against reference expectations. It verifies that the data reflect correct phase ordering and transport behavior without disclosing exact thresholds. The exact reference values and tolerances are not disclosed. The final score is a weighted sum of the scores from each artifact; simply reporting plausible numbers without running the simulation will yield low reward.
