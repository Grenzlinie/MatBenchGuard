# DFT-based phonon and thermodynamic calculations for ZrB2, NbB2, and MoB2

## Problem background
Transition metal diborides ZrB2, NbB2, and MoB2 are promising candidates for heat-resistant and wear-resistant applications. A thorough understanding of their lattice dynamics and thermodynamic behavior—including phonon dispersions, frequencies, and temperature-dependent internal energy, free energy, entropy, and heat capacity—is important for predicting their performance under high-temperature conditions. This task asks you to compute these properties from first principles, filling a gap in the available data.

## Approach
The reproduction follows a computational workflow rooted in density functional theory (DFT) under the generalized gradient approximation. For each compound, you will perform a geometry optimization starting from the experimental AlB2-type structure (space group P6/mmm). Then, using a supercell approach and the direct (finite-displacement) method, you will compute Hellmann-Feynman forces to construct the force-constant matrix, obtain the phonon density of states, and extract the Gamma-point optical mode frequencies. Finally, within the harmonic approximation, you will evaluate the temperature-dependent thermodynamic functions from the total phonon density of states. The open-source tools SIESTA and Phonopy (or equivalent) provide the DFT and phonon engines; Troullier-Martins norm-conserving pseudopotentials complete the setup.

## Reproduction target
Your goal is to produce three CSV output files: (1) structural_data.csv containing the optimized lattice constants a, c (in Å) and nearest-neighbor bond distances X–B and B–B (in Å) for each compound; (2) gamma_frequencies.csv listing the Gamma-point optical phonon frequencies E1u, A2u, B1g, E2g (in meV) for each compound; and (3) thermodynamic_data.csv with columns compound, T_K, internal_energy_meV_per_cell, free_energy_meV_per_cell, entropy_meV_per_K, heat_capacity_meV_per_K, covering temperatures from 0 K to 2000 K in steps of at most 100 K. You must compute these quantities from scratch using DFT and phonon calculations; you cannot simply copy numbers from the literature.

## Assets

- SIESTA: https://departments.icmab.es/leo/siesta/
- Phonopy: phonopy
- Norm-conserving pseudopotentials: https://departments.icmab.es/leo/siesta/page/Databases.html

## Workflow steps

### Step 1: Geometry optimization and structural properties
- Role: scored
- Action: Perform DFT geometry optimization for ZrB2, NbB2, and MoB2 in the AlB2-type structure (space group P6/mmm) starting from experimental lattice parameters. Relax atomic positions and cell parameters until forces fall below a tight threshold. Extract the optimized lattice constants a, c (in Å) and the nearest-neighbor bond distances X–B and B–B (in Å).
- Output file: `/app/outputs/structural_data.csv`
- Format: csv
- Contract: columns: compound (string), a (float, Å), c (float, Å), X_B_distance (float, Å), B_B_distance (float, Å); 3 rows.
- Scoring: scored by hidden verifier

### Step 2: Phonon calculation and Gamma-point frequencies
- Role: scored
- Action: For each relaxed structure, build a supercell (e.g., the rhombohedral supercell used in the paper) and compute Hellmann-Feynman forces for atomic displacements using DFT. Use phonon software to obtain force constants, the total phonon density of states, and the phonon dispersion. Extract the Gamma-point optical mode frequencies (E1u, A2u, B1g, E2g) in meV. Save the total phonon DOS as an intermediate file.
- Output file: `/app/outputs/gamma_frequencies.csv`
- Format: csv
- Contract: columns: compound (string), E1u (meV, float), A2u (meV, float), B1g (meV, float), E2g (meV, float); 3 rows.
- Scoring: scored by hidden verifier

### Step 3: Harmonic thermodynamic properties
- Role: scored (load-bearing)
- Action: From the total phonon density of states obtained in the previous step, compute the temperature-dependent internal energy U(T), Helmholtz free energy F(T), entropy S(T), and constant-volume heat capacity Cv(T) for each compound using the harmonic approximation. Evaluate these quantities at temperatures from 0 K to 2000 K at steps of at most 100 K.
- Output file: `/app/outputs/thermodynamic_data.csv`
- Format: csv
- Contract: columns: compound (string), T_K (float), internal_energy_meV_per_cell (float), free_energy_meV_per_cell (float), entropy_meV_per_K (float), heat_capacity_meV_per_K (float); rows for temperatures from 0 to 2000 K with step ≤100 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_data.csv`
- `/app/outputs/gamma_frequencies.csv`
- `/app/outputs/thermodynamic_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_data.csv
- path: `/app/outputs/structural_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constants and bond lengths for ZrB2, NbB2, and MoB2.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a`, `c`, `X_B_distance`, `B_B_distance`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `X_B_distance`: Å
    - `B_B_distance`: Å

### gamma_frequencies.csv
- path: `/app/outputs/gamma_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Gamma-point optical phonon frequencies for the three compounds.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `E1u`, `A2u`, `B1g`, `E2g`
  - `units`:
    - `E1u`: meV
    - `A2u`: meV
    - `B1g`: meV
    - `E2g`: meV

### thermodynamic_data.csv
- path: `/app/outputs/thermodynamic_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent harmonic thermodynamic properties (internal energy, free energy, entropy, heat capacity) for ZrB2, NbB2, and MoB2 from 0 to 2000 K.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `T_K`, `internal_energy_meV_per_cell`, `free_energy_meV_per_cell`, `entropy_meV_per_K`, `heat_capacity_meV_per_K`
  - `units`:
    - `T_K`: K
    - `internal_energy_meV_per_cell`: meV
    - `free_energy_meV_per_cell`: meV
    - `entropy_meV_per_K`: meV/K
    - `heat_capacity_meV_per_K`: meV/K

Notes: The phonon_dos.csv file produced as evidence during the phonon calculation step is an intermediate artefact and is not part of the scored output contract. The thermodynamic step depends on it.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a",
          "c",
          "X_B_distance",
          "B_B_distance"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "X_B_distance": "Å",
          "B_B_distance": "Å"
        }
      },
      "description": "Optimized lattice constants and bond lengths for ZrB2, NbB2, and MoB2."
    },
    {
      "file": "gamma_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "E1u",
          "A2u",
          "B1g",
          "E2g"
        ],
        "units": {
          "E1u": "meV",
          "A2u": "meV",
          "B1g": "meV",
          "E2g": "meV"
        }
      },
      "description": "Gamma-point optical phonon frequencies for the three compounds."
    },
    {
      "file": "thermodynamic_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "T_K",
          "internal_energy_meV_per_cell",
          "free_energy_meV_per_cell",
          "entropy_meV_per_K",
          "heat_capacity_meV_per_K"
        ],
        "units": {
          "T_K": "K",
          "internal_energy_meV_per_cell": "meV",
          "free_energy_meV_per_cell": "meV",
          "entropy_meV_per_K": "meV/K",
          "heat_capacity_meV_per_K": "meV/K"
        }
      },
      "description": "Temperature-dependent harmonic thermodynamic properties (internal energy, free energy, entropy, heat capacity) for ZrB2, NbB2, and MoB2 from 0 to 2000 K."
    }
  ],
  "notes": "The phonon_dos.csv file produced as evidence during the phonon calculation step is an intermediate artefact and is not part of the scored output contract. The thermodynamic step depends on it."
}
```

## How you are scored
A hidden verifier independently scores each of the three artifacts against reference values and consistency conditions. The checker compares your computed lattice constants, bond lengths, Gamma-point frequencies, and thermodynamic functions at several temperature points to the expected results, using tolerances that account for the typical spread across independent DFT implementations. In addition, it checks physical trends: the heat capacity at 2000 K should approach the Dulong–Petit limit, entropy should increase monotonically with temperature, and internal energy should increase nearly linearly above 300 K. The per-artifact scores are weighted and combined into a final reward. Reporting the paper's numbers without executing the workflow will not pass the structural checks.
