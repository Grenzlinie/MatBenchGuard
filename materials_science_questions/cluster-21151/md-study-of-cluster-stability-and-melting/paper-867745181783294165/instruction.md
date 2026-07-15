# Microcanonical Caloric Curve and Icosahedral‑to‑Decahedral Transition in Ni Clusters via Molecular Dynamics

## Problem background
Small atomic clusters can adopt non-crystalline structures, such as icosahedra and decahedra, because the competition between surface and interior energies shifts at the nanoscale. When such a cluster is in a solid-liquid coexistence state, the solid-liquid interface further influences the energetic balance, potentially driving structural changes in the remaining solid core. This task investigates whether a 1415‑atom nickel cluster, which at zero temperature is predicted to have an icosahedral ground state, undergoes a structural transition in the presence of a coexisting melt. By computing the microcanonical caloric curve (temperature vs total energy) and analyzing the local structure of the solid atoms, you will determine whether the solid transforms from an icosahedral to a decahedral morphology near the melting point and, if so, at what energy the transition occurs.

## Approach
The central method is constant‑energy (microcanonical) molecular dynamics (MD) simulation using the embedded‑atom method (EAM) potential for nickel developed by Foiles et al. (1986). Starting from a perfect 1415‑atom icosahedral cluster, you will perform a sequence of NVE simulations at a fine grid of total energies, spanning from the solid regime to just above the melting point. At each energy, you will equilibrate the system, then compute the temperature from the time‑averaged kinetic energy. To characterize the solid–liquid coexistence, you will analyze the distribution of atomic diffusion coefficients: atoms whose diffusion coefficients fall into a liquid‑like peak are classified as liquid; the remainder are solid. For the solid atoms, you will apply Common Neighbor Analysis (CNA) to count the number of atoms in bulk face‑centered‑cubic (fcc) positions. Because an icosahedron contains only a limited number of fcc‑like environments while a decahedron contains many, a sharp increase in the fcc count signals a structural change. You will carry out this analysis for a heating sequence (increasing total energy) and then for a cooling cycle that starts from the same initial cluster and traces the reverse path, recording the caloric curve during both phases. Finally, you will examine the heating curve to detect the precise total energy at which the temperature exhibits a discontinuous jump and the fcc count rises abruptly—this identifies the icosahedral‑to‑decahedral transition energy.

## Reproduction target
Your objective is to produce three scored artifacts. First, from the heating simulation, create a CSV file (heating_caloric_curve.csv) with the caloric curve and the fcc atom count as functions of total energy. Second, from the heating–cooling cycle, create an analogous CSV file (cooling_caloric_curve.csv) documenting the cooling branch. Third, from the heating curve, extract the single total energy value (in eV/atom) at which the icosahedral‑to‑decahedral transition is observed, and write it to a text file (transition_energy.txt). The transition is defined by a simultaneous jump in temperature and sharp increase in the number of fcc atoms.

## Assets

- EAM Ni potential (Foiles et al. 1986): https://www.ctcms.nist.gov/potentials/system/Ni.html
- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- Python with numpy, scipy, ase: pip install numpy scipy ase

## Workflow steps

### Step 1: Heating caloric curve and fcc atom count for the 1415‑atom icosahedron
- Role: scored (load-bearing)
- Action: Construct a 1415‑atom icosahedral Ni cluster using the EAM potential. Perform a sequence of constant‑energy (NVE) MD simulations at total energies from -3.83 eV/atom to -3.755 eV/atom (increment 0.6 meV/atom, timestep 2 fs, equilibration 150 000 steps, averaging 150 000 steps). For each energy compute the temperature from the averaged kinetic energy, classify atoms as solid or liquid via the bimodality of diffusion coefficients, apply Common Neighbor Analysis (CNA) to the solid atoms, and count the number of atoms in bulk fcc positions. Write a CSV file with columns total_energy (eV/atom), temperature (K), num_fcc_atoms (integer).
- Output file: `/app/outputs/heating_caloric_curve.csv`
- Format: csv
- Contract: total_energy (float, eV/atom), temperature (float, K), num_fcc_atoms (int)
- Scoring: scored by hidden verifier

### Step 2: Heating‑cooling cycle caloric curve and fcc atom count
- Role: scored
- Action: Starting from the same initial 1415‑atom icosahedron, run a constant‑energy MD heating‑cooling cycle: heat from -3.83 eV/atom until the structural transition is observed, then cool back to -3.83 eV/atom at the same rate (same energy increment, equilibration, and averaging). Record total energy, temperature, and number of fcc atoms (as in step 01) during the cooling phase. Write a CSV with columns total_energy, temperature, num_fcc_atoms.
- Output file: `/app/outputs/cooling_caloric_curve.csv`
- Format: csv
- Contract: total_energy (float, eV/atom), temperature (float, K), num_fcc_atoms (int)
- Scoring: scored by hidden verifier

### Step 3: Identification of the icosahedral‑to‑decahedral transition energy
- Role: scored
- Action: From the heating_caloric_curve.csv produced in step 01, detect the total energy (eV/atom) at which the icosahedral‑to‑decahedral transition occurs, signalled by a simultaneous jump in temperature and sharp increase in num_fcc_atoms. Write this single floating‑point number (the energy value) to a text file.
- Output file: `/app/outputs/transition_energy.txt`
- Format: txt
- Contract: A single floating‑point number (e.g. -3.77) in eV/atom
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heating_caloric_curve.csv`
- `/app/outputs/cooling_caloric_curve.csv`
- `/app/outputs/transition_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heating_caloric_curve.csv
- path: `/app/outputs/heating_caloric_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Heating caloric curve and fcc atom count used for shape audit and transition detection.
- schema:
  - `type`: table
  - `required_columns`: `total_energy`, `temperature`, `num_fcc_atoms`
  - `units`:
    - `total_energy`: eV/atom
    - `temperature`: K
    - `num_fcc_atoms`: dimensionless

### cooling_caloric_curve.csv
- path: `/app/outputs/cooling_caloric_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Cooling caloric curve and fcc atom count for hysteresis verification.
- schema:
  - `type`: table
  - `required_columns`: `total_energy`, `temperature`, `num_fcc_atoms`
  - `units`:
    - `total_energy`: eV/atom
    - `temperature`: K
    - `num_fcc_atoms`: dimensionless

### transition_energy.txt
- path: `/app/outputs/transition_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Transition energy identified from the heating curve.
- schema:
  - `type`: text
  - `units`: eV/atom

Notes: The agent must obtain the Foiles et al. (1986) EAM potential and use an MD engine (LAMMPS recommended). The checker will audit the shape of the caloric curves and compare the reported transition energy to the hidden gold with a small tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heating_caloric_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_energy",
          "temperature",
          "num_fcc_atoms"
        ],
        "units": {
          "total_energy": "eV/atom",
          "temperature": "K",
          "num_fcc_atoms": "dimensionless"
        }
      },
      "description": "Heating caloric curve and fcc atom count used for shape audit and transition detection."
    },
    {
      "file": "cooling_caloric_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_energy",
          "temperature",
          "num_fcc_atoms"
        ],
        "units": {
          "total_energy": "eV/atom",
          "temperature": "K",
          "num_fcc_atoms": "dimensionless"
        }
      },
      "description": "Cooling caloric curve and fcc atom count for hysteresis verification."
    },
    {
      "file": "transition_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "eV/atom"
      },
      "description": "Transition energy identified from the heating curve."
    }
  ],
  "notes": "The agent must obtain the Foiles et al. (1986) EAM potential and use an MD engine (LAMMPS recommended). The checker will audit the shape of the caloric curves and compare the reported transition energy to the hidden gold with a small tolerance."
}
```

## How you are scored
A hidden verifier will independently evaluate each output. The verifier will check the overall shape of the heating caloric curve: at low energies the cluster should be solid and have a relatively low fcc count, while at high energies it should be liquid with a near‑zero fcc count, and the transition should appear as a discontinuity. The cooling curve will be examined for the expected hysteresis (no reverse transition). The transition energy you report will be compared to a reference value within a small tolerance. Your final reward is a weighted combination of these checks, with the transition energy accuracy carrying the largest weight. Note that simply reporting the paper's published numbers does not guarantee full credit—the verifier expects the artifacts to be physically consistent and to result from the described simulation protocol.
