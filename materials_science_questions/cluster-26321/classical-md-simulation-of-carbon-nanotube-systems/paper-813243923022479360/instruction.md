# Classical MD Simulation of Peptide Spontaneous Insertion into Armchair Single-Walled Carbon Nanotubes

## Problem background
Carbon nanotubes (CNTs) are promising carriers for biomolecular drug delivery. Understanding how a therapeutic peptide interacts with and inserts into single-walled CNTs is essential for designing CNT-based delivery devices. This task investigates the spontaneous insertion of the HIV replication inhibitor peptide (HRIP, a 21-residue peptide) into armchair SWCNTs of different diameters using classical molecular dynamics simulations. The goal is to determine which tube diameter yields the most favorable encapsulation—strong binding coupled with minimal conformational change of the peptide. The simulation metrics to compute serve as quantitative measures of the peptide–CNT interactions and the effect of tube size on encapsulation dynamics and peptide structure.

## Approach
The approach uses classical all-atom molecular dynamics (MD) simulations in explicit water. The peptide structure (HRIP) is obtained from the Protein Data Bank entry 1RPB. Five armchair (n,n) SWCNTs with indices n=16,17,18,19,20 and a length of 3.19 nm are constructed as uncapped tubes. The peptide is first equilibrated alone in TIP3P water. For each tube diameter, a simulation system is assembled by placing the peptide near the nanotube opening with an initial center‑of‑mass separation of about 2 Å and solvating the complex with TIP3P water; sodium ions are added to neutralize the system. The CHARMM27 all‑atom force field is used for the peptide, and the carbon atoms of the CNT are treated as fixed and uncharged with van der Waals parameters taken from graphite. All simulations are performed in the isothermal‑isobaric (NPT) ensemble at 310 K and 101.3 kPa using Langevin dynamics for temperature control and the Nosé‑Hoover Langevin barostat for pressure control. Short‑range van der Waals interactions are truncated at 12 Å, particle‑mesh Ewald sums handle electrostatic interactions, and the integration timestep is 2 fs. Each HRIP–CNT system is simulated for 27.5 ns. From the trajectories, three quantitative outputs are extracted: (i) the time evolution of the normalized center‑of‑mass distance between the peptide and the CNT, the instantaneous van der Waals interaction energy, and the backbone root‑mean‑square deviation (RMSD) for the (17,17) CNT system; (ii) the mean and standard deviation of the van der Waals interaction energy over the last 12.5 ns (15–27.5 ns) for all five tube diameters; (iii) the mean and standard deviation of the peptide radius of gyration over the same 15–27.5 ns window for all five tube diameters. These quantities capture the insertion dynamics, the strength of encapsulation, and the peptide conformational changes as a function of CNT diameter.

## Reproduction target
The reproduction target is to execute the simulation and analysis pipeline and produce three CSV files under `/app/outputs`:

- **step_01_d_energy_rmsd.csv**: Time series for the (17,17) CNT system with columns `time_ns` (ns), `d_d0` (normalized center‑of‑mass distance, dimensionless), `Evdw_int_kcal_mol` (van der Waals interaction energy in kcal/mol), `RMSD_A` (backbone RMSD in Å). The time series must cover the full 27.5 ns with at least 1000 evenly spaced points.

- **step_02_interaction_strengths.csv**: Summary table with columns `cnt_index` (16,17,18,19,20), `mean_Evdw_int_kcal_mol` (kcal/mol), and `std_Evdw_int_kcal_mol` (kcal/mol), computed from the trajectories over the time interval 15–27.5 ns for each tube size.

- **step_03_rg.csv**: Summary table with columns `cnt_index` (16,17,18,19,20), `mean_Rg_A` (Å), and `std_Rg_A` (Å), representing the mean radius of gyration and its standard deviation over 15–27.5 ns for each tube size.

The overall objective is to demonstrate that the simulations faithfully capture spontaneous insertion and provide the encapsulation strength and peptide structural integrity as a function of tube diameter.

## Assets

- HRIP peptide structure (PDB entry 1RPB): https://www.rcsb.org/structure/1RPB
- CHARMM27 all-atom force field: http://mackerell.umaryland.edu/CHARMM_ff_params.html
- TIP3P water model
- Graphite CNT van der Waals parameters: 10.1021/jp0107472
- NAMD molecular dynamics engine: https://www.ks.uiuc.edu/Research/namd/
- VMD visualization and analysis suite: https://www.ks.uiuc.edu/Research/vmd/

## Workflow steps

### Step 1: Retrieve HRIP structure from PDB
- Role: process
- Action: Download the atomic coordinates of HRIP (HIV replication inhibitor peptide) from Protein Data Bank entry 1RPB. This provides the initial peptide topology and conformation.
- Evidence: `/app/outputs/hrrip.pdb`

### Step 2: Construct armchair SWCNTs
- Role: process
- Action: Build uncapped armchair single-walled carbon nanotubes with chirality indices (n,n) for n=16,17,18,19,20, each having a length of 3.19 nm. Use a suitable CNT builder to generate atomic coordinates.
- Evidence: `/app/outputs/cnt_coordinates.pdb`

### Step 3: Equilibrate HRIP in water
- Role: process
- Action: Run a 1 ns NPT molecular dynamics simulation of HRIP solvated in a periodic box of TIP3P water molecules at 310 K and 101.3 kPa using the CHARMM27 force field. This stabilizes the peptide structure before interaction with CNTs.
- Evidence: `/app/outputs/equilibrated_hrrip.pdb`

### Step 4: Assemble HRIP‑CNT simulation systems
- Role: process
- Action: For each CNT size, combine the equilibrated HRIP with the CNT, aligning them along the tube axis with an initial center‑of‑mass separation of approximately 2 Å. Solvate the complex in TIP3P water, add sodium ions to neutralize the system, and create the necessary topology and coordinate files for NAMD.
- Evidence: `/app/outputs/system_setup.log`

### Step 5: Run production MD simulations
- Role: process
- Action: Perform NPT molecular dynamics simulations for each HRIP‑CNT system (n=16–20) for 27.5 ns at 310 K and 101.3 kPa using Langevin dynamics (damping 5 ps⁻¹ on non‑hydrogen atoms), a 2 fs timestep, 12 Å Lennard‑Jones cutoff (pairlist 13.5 Å), and particle mesh Ewald for electrostatics. Carbon atoms of the CNT are fixed and uncharged; use the CHARMM27 force field with graphite parameters for CNT–peptide van der Waals interactions.
- Evidence: `/app/outputs/simulation_complete.txt`

### Step 6: Analyze (17,17) CNT trajectory
- Role: scored
- Action: From the (17,17) CNT trajectory, compute the normalized center‑of‑mass distance d/d₀, the instantaneous van der Waals interaction energy Evdw‑int, and the backbone RMSD of HRIP as functions of time. Output a CSV file with equally spaced time points covering 0–27.5 ns (at least 1000 rows).
- Output file: `/app/outputs/step_01_d_energy_rmsd.csv`
- Format: csv
- Contract: CSV with columns: time_ns (float), d_d0 (float), Evdw_int_kcal_mol (float), RMSD_A (float). At least 1000 rows covering 0–27.5 ns.
- Scoring: scored by hidden verifier

### Step 7: Compute mean interaction strengths for all CNTs
- Role: scored (load-bearing)
- Action: For each CNT size (n=16–20), compute the mean and standard deviation of the van der Waals interaction energy Evdw‑int over the time window 15–27.5 ns. Output a summary CSV.
- Output file: `/app/outputs/step_02_interaction_strengths.csv`
- Format: csv
- Contract: CSV with columns: cnt_index (integer 16,17,18,19,20), mean_Evdw_int_kcal_mol (float), std_Evdw_int_kcal_mol (float).
- Scoring: scored by hidden verifier

### Step 8: Compute radii of gyration for all CNTs
- Role: scored
- Action: For each CNT size, compute the mean and standard deviation of the HRIP radius of gyration Rg over the time window 15–27.5 ns. Output a summary CSV.
- Output file: `/app/outputs/step_03_rg.csv`
- Format: csv
- Contract: CSV with columns: cnt_index (integer 16,17,18,19,20), mean_Rg_A (float), std_Rg_A (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_d_energy_rmsd.csv`
- `/app/outputs/step_02_interaction_strengths.csv`
- `/app/outputs/step_03_rg.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_d_energy_rmsd.csv
- path: `/app/outputs/step_01_d_energy_rmsd.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of normalized center-of-mass distance, van der Waals interaction energy, and backbone RMSD for the (17,17) CNT system. The checker recomputes the mean interaction energy over 15–27.5 ns and checks the trend of d/d0.
- schema:
  - `type`: table
  - `required_columns`: `time_ns`, `d_d0`, `Evdw_int_kcal_mol`, `RMSD_A`
  - `units`:
    - `time_ns`: ns
    - `d_d0`: unitless
    - `Evdw_int_kcal_mol`: kcal/mol
    - `RMSD_A`: angstrom

### step_02_interaction_strengths.csv
- path: `/app/outputs/step_02_interaction_strengths.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Mean and standard deviation of the van der Waals interaction energy for each tube size over the time window 15–27.5 ns. The checker compares each mean to the paper's reference values within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `cnt_index`, `mean_Evdw_int_kcal_mol`, `std_Evdw_int_kcal_mol`
  - `units`:
    - `cnt_index`: integer
    - `mean_Evdw_int_kcal_mol`: kcal/mol
    - `std_Evdw_int_kcal_mol`: kcal/mol

### step_03_rg.csv
- path: `/app/outputs/step_03_rg.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Mean and standard deviation of the radius of gyration of HRIP for each tube size over the time window 15–27.5 ns. The checker compares each mean to the paper's reference values within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `cnt_index`, `mean_Rg_A`, `std_Rg_A`
  - `units`:
    - `mean_Rg_A`: angstrom
    - `std_Rg_A`: angstrom

Notes: All scored artifacts are re-derived from the simulation trajectories. The checker will recompute the mean interaction energy from the (17,17) time series and cross-validate with the summary file. Tolerances are hidden and account for legitimate run-to-run variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_d_energy_rmsd.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ns",
          "d_d0",
          "Evdw_int_kcal_mol",
          "RMSD_A"
        ],
        "units": {
          "time_ns": "ns",
          "d_d0": "unitless",
          "Evdw_int_kcal_mol": "kcal/mol",
          "RMSD_A": "angstrom"
        }
      },
      "description": "Time series of normalized center-of-mass distance, van der Waals interaction energy, and backbone RMSD for the (17,17) CNT system. The checker recomputes the mean interaction energy over 15–27.5 ns and checks the trend of d/d0."
    },
    {
      "file": "step_02_interaction_strengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cnt_index",
          "mean_Evdw_int_kcal_mol",
          "std_Evdw_int_kcal_mol"
        ],
        "units": {
          "cnt_index": "integer",
          "mean_Evdw_int_kcal_mol": "kcal/mol",
          "std_Evdw_int_kcal_mol": "kcal/mol"
        }
      },
      "description": "Mean and standard deviation of the van der Waals interaction energy for each tube size over the time window 15–27.5 ns. The checker compares each mean to the paper's reference values within a hidden tolerance."
    },
    {
      "file": "step_03_rg.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cnt_index",
          "mean_Rg_A",
          "std_Rg_A"
        ],
        "units": {
          "mean_Rg_A": "angstrom",
          "std_Rg_A": "angstrom"
        }
      },
      "description": "Mean and standard deviation of the radius of gyration of HRIP for each tube size over the time window 15–27.5 ns. The checker compares each mean to the paper's reference values within a hidden tolerance."
    }
  ],
  "notes": "All scored artifacts are re-derived from the simulation trajectories. The checker will recompute the mean interaction energy from the (17,17) time series and cross-validate with the summary file. Tolerances are hidden and account for legitimate run-to-run variability."
}
```

## How you are scored
A hidden checker independently evaluates each scored artifact and combines the results into a final reward using a weighted scheme.

- **step_01_d_energy_rmsd.csv**: The checker re‑computes the mean van der Waals interaction energy over 15–27.5 ns from your time series and cross‑checks it against the (17,17) entry in `step_02_interaction_strengths.csv`; it also assesses whether the `d/d0` curve follows the expected insertion trend (overall decrease to small values with subsequent oscillations) and whether the RMSD profile shows a plausible conformational adjustment and stabilization. Agreement with the expected reference behavior contributes to the reward.

- **step_02_interaction_strengths.csv**: Each of the five mean interaction energies is compared against hidden reference values. The reward is higher when your computed means are close to those references, allowing for legitimate run‑to‑run variability.

- **step_03_rg.csv**: Similarly, each mean radius of gyration is compared against hidden reference values, with a tolerance that accounts for expected spread.

The total reward is the weighted sum of scores from the three artifacts, with `step_02` receiving the largest weight because it is load‑bearing for the main claim. Numeric tolerances and reference values are concealed. Simply printing the paper’s reported numbers without running the simulations will not pass the cross‑validation and trend checks.
