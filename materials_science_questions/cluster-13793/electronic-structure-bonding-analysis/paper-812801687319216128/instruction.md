# Si-doping effects on structural stability of iron oxide nanoparticles during delithiation via QMD simulations

## Problem background
Biogenous iron oxide nanoparticles (BIOX) that are naturally doped with silicon (Si) show excellent cyclability when used as lithium-ion battery anodes, but the atomistic origin of this stability is not fully understood. First-principles quantum molecular dynamics (QMD) simulations provide a direct way to probe how Si-doping influences the structural response of Fe2O3 nanoparticles to lithiation and delithiation. Reproducing the simulation-derived structural metrics—kinetic energy of ejected lithium ions, geometric deformation, bond-topology changes, and Li-O bond covalency—sheds light on the mechanisms that could make Si-doped nanoparticles more resilient during electrochemical cycling.

## Approach
The workflow constructs two atomistic models: a Si-free Fe2O3 nanoparticle (Fe24O36) and a Si-doped Fe2O3–SiO2 nanoparticle (Fe18O27Si6O12), each surrounded by 19 LiPF6 electrolyte units in a cubic simulation cell of side 18.26 Å. Spin-polarized density functional theory (DFT) with GGA+U and projector augmented-wave potentials is used to perform molecular dynamics at 500 K. The simulation proceeds in three stages: thermalization of the neutral cell, lithiation by injecting 18 extra electrons, and delithiation by removing those electrons. From the resulting trajectories, post-processing extracts: (i) the average kinetic energy of Li atoms that dissociate from the nanoparticle as a function of time, (ii) the translationally and rotationally minimized root-mean-square displacement D of all nanoparticle atoms, (iii) the Hamming distance DH that counts bond-breakage and bond-formation events, and (iv) bond overlap population (BOP) distributions for Li-O bonds immediately before and after electron removal. The comparison between Si-free and Si-doped systems under identical conditions isolates the effect of Si-doping on structural stability. Any open-source DFT code capable of spin-polarized GGA+U PAW calculations (e.g., Quantum ESPRESSO) and standard Python scientific libraries are sufficient to carry out the simulations and analyses.

## Reproduction target
Using open-source DFT software and Python, set up the nanoparticle-electrolyte models and perform the three-stage QMD protocol. From the delithiation trajectories, compute and write to CSV files: (1) a time series of the average kinetic energy of Li atoms that become dissociated from the nanoparticle, for both Si-free and Si-doped systems; (2) a time series of the minimized root-mean-square displacement D for the nanoparticle atoms in the two systems; (3) a time series of the Hamming distance DH quantifying bond-topology changes for both systems; (4) a histogram of Li-O bond overlap populations extracted from the lithiated snapshot just before electron removal, for both systems; (5) a second BOP histogram from the snapshot immediately after electron removal. The time series must span the delithiation window (0–1.82 ps) with at least 10 equally spaced time points. The histograms must share a consistent binning scheme. The produced artifacts will be inspected by a hidden verifier that assesses whether the simulated trends are physically consistent with the effect of Si-doping on nanoparticle stability.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Python3 with numpy, scipy, matplotlib: https://pypi.org/

## Workflow steps

### Step 1: Simulation cell setup and equilibration
- Role: process
- Action: Construct Si-free (Fe24O36) and Si-doped (Fe18O27Si6O12) nanoparticle models in 19 LiPF6 electrolyte in a cubic cell of side 18.26 Å, and perform initial thermalization using DFT-based molecular dynamics for 1.33 ps at 500 K.
- Evidence: `/app/outputs/equilibration_log.txt`

### Step 2: Lithiation simulation
- Role: process
- Action: Inject 18 extra electrons into the simulation cell and run DFT-MD for 4.84 ps at 500 K for both Si-free and Si-doped systems.
- Evidence: `/app/outputs/lithiation_simulation_log.txt`

### Step 3: Delithiation simulation
- Role: process
- Action: Remove 18 electrons from the lithiated cells and run DFT-MD for 1.82 ps at 500 K for both systems.
- Evidence: `/app/outputs/delithiation_simulation_log.txt`

### Step 4: Kinetic energy of dissociated Li atoms
- Role: scored (load-bearing)
- Action: From the delithiation trajectories, identify Li atoms that dissociate from the nanoparticle by the end of the simulation, then compute their average kinetic energy as a function of time. Output the time series for both Si-free and Si-doped systems.
- Output file: `/app/outputs/kinetic_energy.csv`
- Format: csv
- Contract: CSV with columns: time_ps (float), avg_ke_si_free_eV (float), avg_ke_si_doped_eV (float). At least 10 time points from 0 to 1.82 ps.
- Scoring: scored by hidden verifier

### Step 5: Geometric deformation (minimized RMSD)
- Role: scored (load-bearing)
- Action: For each delithiation trajectory, compute the translationally and rotationally minimized root-mean-square displacement D for all nanoparticle atoms, using the initial delithiation configuration as reference. Output the time series for both systems.
- Output file: `/app/outputs/geometric_deformation.csv`
- Format: csv
- Contract: CSV with columns: time_ps (float), D_si_free_angstrom (float), D_si_doped_angstrom (float). Same time points as kinetic_energy.csv.
- Scoring: scored by hidden verifier

### Step 6: Bond-topology change (Hamming distance)
- Role: scored (load-bearing)
- Action: Compute the Hamming distance DH between bond adjacency matrices at the initial delithiation time and each subsequent time for both systems. Output the time series.
- Output file: `/app/outputs/hamming_distance.csv`
- Format: csv
- Contract: CSV with columns: time_ps (float), DH_si_free (float), DH_si_doped (float). Same time points.
- Scoring: scored by hidden verifier

### Step 7: Bond overlap population before electron removal
- Role: scored
- Action: Perform Mulliken bond overlap population analysis on the final lithiated snapshot (just before electron removal) for Li-O bonds. Output a histogram of BOP values for both systems.
- Output file: `/app/outputs/bop_before.csv`
- Format: csv
- Contract: CSV with columns: bop_value (float), frequency_si_free (float), frequency_si_doped (float). Histogram bins across the BOP range.
- Scoring: scored by hidden verifier

### Step 8: Bond overlap population immediately after electron removal
- Role: scored
- Action: Perform the same BOP analysis on the snapshot immediately after removing electrons (early delithiation). Output the histogram.
- Output file: `/app/outputs/bop_after.csv`
- Format: csv
- Contract: CSV with columns: bop_value (float), frequency_si_free (float), frequency_si_doped (float). Histogram bins.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kinetic_energy.csv`
- `/app/outputs/geometric_deformation.csv`
- `/app/outputs/hamming_distance.csv`
- `/app/outputs/bop_before.csv`
- `/app/outputs/bop_after.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kinetic_energy.csv
- path: `/app/outputs/kinetic_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time evolution of the average kinetic energy of Li atoms that dissociated from the nanoparticle during delithiation. The Si-doped system is expected to show a gentler rise compared to the Si-free system.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `avg_ke_si_free_eV`, `avg_ke_si_doped_eV`
  - `units`:
    - `time_ps`: ps
    - `avg_ke_si_free_eV`: eV
    - `avg_ke_si_doped_eV`: eV

### geometric_deformation.csv
- path: `/app/outputs/geometric_deformation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Translationally and rotationally minimized root-mean-square displacement D for nanoparticle atoms. Si-doped system should show consistently lower D values.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `D_si_free_angstrom`, `D_si_doped_angstrom`
  - `units`:
    - `time_ps`: ps
    - `D_si_free_angstrom`: angstrom
    - `D_si_doped_angstrom`: angstrom

### hamming_distance.csv
- path: `/app/outputs/hamming_distance.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Hamming distance quantifying bond-topology changes. Si-doped system is expected to have about 30% lower average DH than Si-free.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `DH_si_free`, `DH_si_doped`
  - `units`:
    - `time_ps`: ps
    - `DH_si_free`: dimensionless
    - `DH_si_doped`: dimensionless

### bop_before.csv
- path: `/app/outputs/bop_before.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Histogram of bond overlap populations for Li-O bonds before electron removal. Si-free should exhibit a sharp peak at positive bond orders.
- schema:
  - `type`: table
  - `required_columns`: `bop_value`, `frequency_si_free`, `frequency_si_doped`
  - `units`:
    - `bop_value`: dimensionless
    - `frequency_si_free`: count
    - `frequency_si_doped`: count

### bop_after.csv
- path: `/app/outputs/bop_after.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Histogram of bond overlap populations for Li-O bonds immediately after electron removal. Si-free should exhibit a sharp peak at negative bond orders (anti-bonding).
- schema:
  - `type`: table
  - `required_columns`: `bop_value`, `frequency_si_free`, `frequency_si_doped`
  - `units`:
    - `bop_value`: dimensionless
    - `frequency_si_free`: count
    - `frequency_si_doped`: count

Notes: All time series are expected to cover at least 10 points from 0 to 1.82 ps. Histograms must use consistent bins. The checker verifies structural trends, not absolute values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kinetic_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "avg_ke_si_free_eV",
          "avg_ke_si_doped_eV"
        ],
        "units": {
          "time_ps": "ps",
          "avg_ke_si_free_eV": "eV",
          "avg_ke_si_doped_eV": "eV"
        }
      },
      "description": "Time evolution of the average kinetic energy of Li atoms that dissociated from the nanoparticle during delithiation. The Si-doped system is expected to show a gentler rise compared to the Si-free system."
    },
    {
      "file": "geometric_deformation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "D_si_free_angstrom",
          "D_si_doped_angstrom"
        ],
        "units": {
          "time_ps": "ps",
          "D_si_free_angstrom": "angstrom",
          "D_si_doped_angstrom": "angstrom"
        }
      },
      "description": "Translationally and rotationally minimized root-mean-square displacement D for nanoparticle atoms. Si-doped system should show consistently lower D values."
    },
    {
      "file": "hamming_distance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "DH_si_free",
          "DH_si_doped"
        ],
        "units": {
          "time_ps": "ps",
          "DH_si_free": "dimensionless",
          "DH_si_doped": "dimensionless"
        }
      },
      "description": "Hamming distance quantifying bond-topology changes. Si-doped system is expected to have about 30% lower average DH than Si-free."
    },
    {
      "file": "bop_before.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bop_value",
          "frequency_si_free",
          "frequency_si_doped"
        ],
        "units": {
          "bop_value": "dimensionless",
          "frequency_si_free": "count",
          "frequency_si_doped": "count"
        }
      },
      "description": "Histogram of bond overlap populations for Li-O bonds before electron removal. Si-free should exhibit a sharp peak at positive bond orders."
    },
    {
      "file": "bop_after.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "bop_value",
          "frequency_si_free",
          "frequency_si_doped"
        ],
        "units": {
          "bop_value": "dimensionless",
          "frequency_si_free": "count",
          "frequency_si_doped": "count"
        }
      },
      "description": "Histogram of bond overlap populations for Li-O bonds immediately after electron removal. Si-free should exhibit a sharp peak at negative bond orders (anti-bonding)."
    }
  ],
  "notes": "All time series are expected to cover at least 10 points from 0 to 1.82 ps. Histograms must use consistent bins. The checker verifies structural trends, not absolute values."
}
```

## How you are scored
A hidden verifier independently reads your CSV artifacts and scores each one according to structural criteria that encode the key physical phenomena being investigated. The verifier checks properties such as the shape of the kinetic energy evolution, the relative magnitudes of D and DH between the two systems, and the presence or absence of specific peaks in the BOP distributions. Each artifact receives a normalized score based on how well it reproduces the expected structural patterns, and the final reward is a weighted combination of these per-artifact scores. The exact scoring functions and acceptance thresholds are not disclosed. You are not required to match any particular numerical value from the literature; the reward reflects how faithfully the simulated behavior captures the underlying physics under the prescribed protocol.
