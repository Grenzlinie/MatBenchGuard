# Electronic conductivity in aluminum-graphene composites from ab initio calculations

## Problem background
Aluminum-graphene composites have been reported to exhibit enhanced electrical conductivity compared to pure aluminum, but the detailed electronic mechanism and the role of the interfacial structure and graphene layer count remain open questions. This task investigates the electronic and transport properties of Al(111) interfaces with single- and double-layer graphene under compression using density functional theory. The aim is to compute the electronic density of states at the Fermi level, the electronic conductivity, the work function, and the atomic charge redistribution as a function of the aluminium–graphene distance, and to determine the temperature dependence of the conductivity from ab initio molecular dynamics. The task quantifies the conductivity enhancement and the influence of graphene layers on the electronic structure of the composite relative to a pure aluminium baseline.

## Approach
The approach is based on plane-wave density functional theory with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional. An orthorhombic Al(111) slab containing a stacking fault is used as the metal matrix. Single-layer (SL) or AB-stacked double-layer (DL) graphene is placed above the slab to form an interface. The Al–graphene interfacial distance is systematically reduced to model compression; for each compressed configuration the atomic positions are relaxed while the cell dimensions are kept fixed. From the relaxed structures, static single-point calculations are performed to extract the electronic structure, including the projected density of states, Fermi level, charge density, and electrostatic potential. The electronic conductivity at 300 K is computed using the Kubo–Greenwood formula. Charge transfer is quantified via Bader analysis, and the work function is obtained from the planar-averaged electrostatic potential. Selected models are further studied with ab initio molecular dynamics in the canonical ensemble at temperatures from 100 K to 600 K; for each temperature, snapshots are collected and used to compute the average conductivity and its standard deviation. The workflow produces two tables: one listing static electronic properties for all distances, and one listing temperature-dependent average conductivities for a subset of models.

## Reproduction target
Compute and report the following in the specified output files:
1. In `electronic_properties.csv`, for the pure aluminium slab, the SL composite, and the DL composite at a set of imposed Al–G distances (see the workflow steps), the Fermi level, the squared electronic density of states at the Fermi level, the electronic conductivity at 300 K, the work function, and the average Bader charges on interfacial Al and C atoms.
2. In `temperature_conductivity.csv`, for the most compressed DL and SL models and the pure Al baseline, the average electronic conductivity and its standard deviation at each temperature from 100 K to 600 K in 50 K steps, obtained from ab initio molecular dynamics and the Kubo–Greenwood formula.
The goal is to quantify how the conductivity and electronic properties change with decreasing Al–G distance, and to characterise the temperature dependence of the conductivity for the composites relative to pure aluminium.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader charge analysis code (Henkelman group): https://theory.cm.utexas.edu/henkelman/code/bader/
- PBE pseudopotentials (SSSP precision library): https://www.materialscloud.org/discover/sssp/table/toolkit

## Workflow steps

### Step 1: Model construction
- Role: process
- Action: Build atomistic models of a pure Al(111) slab (with stacking fault), single-layer (SL) and double-layer (DL, AB-stacked) Al-graphene composites. Set initial interfacial distances d_Al-G for SL (3.48, 3.42, 3.36, 3.31, 3.28, 3.21, 3.16, 3.09 Å) and DL (3.48, 3.42, 3.36, 3.30, 3.24, 3.18, 3.12, 3.06, 3.00, 2.96 Å) as in the supplementary material. Write structure files for all models.
- Evidence: `/app/outputs/model_files`

### Step 2: DFT geometry relaxation
- Role: process
- Action: For each model, relax atomic positions at fixed cell dimensions using plane-wave DFT (PBE functional) with a suitable kinetic-energy cutoff and k-point sampling. Record the final interfacial distance and external pressure. Output relaxed structure files.
- Evidence: `/app/outputs/relaxation_outputs`

### Step 3: Static DFT electronic structure and charge density
- Role: process
- Action: For each relaxed structure, run single-point DFT calculations to obtain wavefunctions, eigenvalues, projected density of states (PDOS), charge density, and electrostatic potential (for work function). Save relevant output files for post-processing.
- Evidence: `/app/outputs/static_dft_outputs`

### Step 4: Electronic properties and static conductivity
- Role: scored (load-bearing)
- Action: Post-process DFT outputs to compute: Fermi level (from eigenvalues), density of states at Fermi level N(Ef) (from PDOS), squared density N²(Ef), electronic conductivity at 300 K via the Kubo-Greenwood formula (using wavefunctions and eigenvalues), work function (from planar-averaged electrostatic potential), and Bader charges on interfacial Al and C atoms. Assemble results in a CSV with columns: model_type, initial_d_Al_G, final_d_Al_G, Fermi_level, N2_Ef, conductivity_300K, work_function, avg_bader_charge_C, avg_bader_charge_Al. One row per model.
- Output file: `/app/outputs/electronic_properties.csv`
- Format: csv
- Contract: model_type,initial_d_Al_G,final_d_Al_G,Fermi_level,N2_Ef,conductivity_300K,work_function,avg_bader_charge_C,avg_bader_charge_Al
- Scoring: scored by hidden verifier

### Step 5: Ab initio molecular dynamics
- Role: process
- Action: For selected models (DL_2.97, DL_3.41, SL_3.01, SL_3.40, pure_Al), run AIMD simulations in the NVT ensemble at temperatures from 100 to 600 K in steps of 50 K. Each simulation runs for 3 ps with a 1.5 fs timestep. Retain the final 10 snapshots per temperature for conductivity calculations.
- Evidence: `/app/outputs/aimd_trajectories`

### Step 6: Temperature-dependent conductivity
- Role: scored (load-bearing)
- Action: For each snapshot from step5, compute conductivity via the Kubo-Greenwood formula (using single-point DFT calculations on each snapshot). Average over the 10 snapshots per temperature per model and compute standard deviation. Write results to a CSV with columns: model_id, temperature, average_conductivity, std_conductivity.
- Output file: `/app/outputs/temperature_conductivity.csv`
- Format: csv
- Contract: model_id,temperature,average_conductivity,std_conductivity
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.csv`
- `/app/outputs/temperature_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.csv
- path: `/app/outputs/electronic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electronic properties and static conductivity at 300 K for pure Al, SL, and DL models. The hidden checker compares the computed values to paper-reported reference data with tolerances and verifies trends (e.g., conductivity increase with decreasing d_Al-G).
- schema:
  - `type`: table
  - `required_columns`: `model_type`, `initial_d_Al_G`, `final_d_Al_G`, `Fermi_level`, `N2_Ef`, `conductivity_300K`, `work_function`, `avg_bader_charge_C`, `avg_bader_charge_Al`
  - `units`:
    - `initial_d_Al_G`: Å
    - `final_d_Al_G`: Å
    - `Fermi_level`: eV
    - `N2_Ef`: arb. units
    - `conductivity_300K`: S/cm
    - `work_function`: eV
    - `avg_bader_charge_C`: e-
    - `avg_bader_charge_Al`: e-

### temperature_conductivity.csv
- path: `/app/outputs/temperature_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent average conductivity and standard deviation from AIMD snapshots for selected models. The hidden checker compares the average conductivity values to reference data and checks that DL_2.97 exhibits non-monotonic behaviour (increase between 300 and 400 K) while other models show monotonic decrease.
- schema:
  - `type`: table
  - `required_columns`: `model_id`, `temperature`, `average_conductivity`, `std_conductivity`
  - `units`:
    - `temperature`: K
    - `average_conductivity`: S/cm
    - `std_conductivity`: S/cm

Notes: The checker uses hidden reference values from the paper and enforces required relative trends (monotonicity, non-monotonic peak) together with numeric tolerances. No solver should try to match the paper's exact numbers; faithfully execute the workflow, and the checker will assess the result.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_type",
          "initial_d_Al_G",
          "final_d_Al_G",
          "Fermi_level",
          "N2_Ef",
          "conductivity_300K",
          "work_function",
          "avg_bader_charge_C",
          "avg_bader_charge_Al"
        ],
        "units": {
          "initial_d_Al_G": "Å",
          "final_d_Al_G": "Å",
          "Fermi_level": "eV",
          "N2_Ef": "arb. units",
          "conductivity_300K": "S/cm",
          "work_function": "eV",
          "avg_bader_charge_C": "e-",
          "avg_bader_charge_Al": "e-"
        }
      },
      "description": "Electronic properties and static conductivity at 300 K for pure Al, SL, and DL models. The hidden checker compares the computed values to paper-reported reference data with tolerances and verifies trends (e.g., conductivity increase with decreasing d_Al-G)."
    },
    {
      "file": "temperature_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_id",
          "temperature",
          "average_conductivity",
          "std_conductivity"
        ],
        "units": {
          "temperature": "K",
          "average_conductivity": "S/cm",
          "std_conductivity": "S/cm"
        }
      },
      "description": "Temperature-dependent average conductivity and standard deviation from AIMD snapshots for selected models. The hidden checker compares the average conductivity values to reference data and checks that DL_2.97 exhibits non-monotonic behaviour (increase between 300 and 400 K) while other models show monotonic decrease."
    }
  ],
  "notes": "The checker uses hidden reference values from the paper and enforces required relative trends (monotonicity, non-monotonic peak) together with numeric tolerances. No solver should try to match the paper's exact numbers; faithfully execute the workflow, and the checker will assess the result."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `electronic_properties.csv` and `temperature_conductivity.csv`. The verifier first checks that the files are correctly formatted and contain all required columns. It then compares your reported values to reference values derived from the original study, using tolerances that account for differences between DFT codes and numerical implementations. The verifier also checks that the data respect physically required relative trends (e.g., monotonic variation with interfacial distance, distinct temperature behaviour for different models). Your final score is a weighted combination of the scores for each artifact. Simply reporting numbers that match the paper’s published results is not sufficient; you must perform the DFT calculations and post-processing as described in the workflow steps to obtain self-consistent results.
