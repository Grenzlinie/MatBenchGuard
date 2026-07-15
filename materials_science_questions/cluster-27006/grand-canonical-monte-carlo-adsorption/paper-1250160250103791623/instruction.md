# Pore-centred adsorption analysis using kernel density estimation and GCMC simulations

## Problem background
Understanding gas adsorption in hierarchical porous materials requires separating the contributions of different pore environments. This task implements a statistical method that uses kernel density estimation (KDE) and DBSCAN clustering to partition the pore space of a metal-organic framework (MOF) into distinct size-labelled regions, and combines these regions with grand canonical Monte Carlo (GCMC) simulations of argon adsorption. The goal is to compute pore-specific adsorption isotherms and pore-centred radial distribution functions from which the nature of pore-filling mechanisms can be inferred.

## Approach
The computational workflow consists of (a) building a supercell of the MOF structure, (b) running a geometric pore analysis tool to obtain probe points with local pore-size values, (c) applying Gaussian kernel density estimation (KDE) to the probe point sizes to produce a continuous pore-size density function, from which characteristic pore sizes and boundaries are identified, and each probe point is labelled by pore category (e.g., small, medium, large), (d) applying DBSCAN clustering to the labelled probe points to identify individual pore centres, (e) performing Grand Canonical Monte Carlo simulations of Ar adsorption at 87 K over a range of pressures, and (f) post-processing the simulation snapshots to compute the total adsorption isotherm, the isotherms decomposed into contributions from each pore category, and the radial distribution of Ar atoms from each pore centre at selected pressures.

## Reproduction target
Reproduce the computational pipeline for the MOF DUT‑32: (a) generate a supercell with minimum dimension >12 Å; (b) run Zeo++ to produce probe points with local pore‑size samples; (c) apply Gaussian KDE with bandwidth 2.0 Å to obtain a continuous pore‑size density and assign pore‑size labels; (d) cluster labelled probe points with DBSCAN to locate pore centres; (e) run GCMC simulations of Ar adsorption at 87 K for 75 logarithmically spaced pressure points from 1e‑5 to 1 bar; (f) compute the total adsorption isotherm, pore‑specific isotherms, and radial distributions at three selected pressures. The required output artifacts are the five CSV files listed under "Output files" with the specified columns and formats.

## Assets

- DUT-32 crystal structure: 10.1039/C4CC00113C
- Zeo++: https://github.com/zeoplusplus/zeopp-lsmo
- YAFF: https://github.com/molmod/yaff
- statsmodels: statsmodels
- scikit-learn: scikit-learn
- Supercell construction utility (e.g., ASE or pymatgen): ase | pymatgen

## Workflow steps

### Step 1: Build DUT-32 supercell
- Role: process
- Action: Generate a supercell of DUT-32 from the published crystal structure so that the minimum cell length is greater than 12 Å. Store the supercell geometry (e.g., as a CIF file) for downstream use.
- Evidence: `/app/outputs/dut32_supercell.cif`

### Step 2: Zeo++ geometric analysis
- Role: process
- Action: Run Zeo++ on the supercell with a probe radius of 3.4 Å to compute the Ar-accessible pore volume and the point-wise pore-size distribution (--vpsd flag). Save the probe point coordinates and associated largest-sphere diameters.
- Evidence: `/app/outputs/zeopp_vpsd_output.txt`

### Step 3: KDE pore-size density and partitioning
- Role: scored
- Action: Using the probe point diameters from Zeo++, fit a kernel density estimate with a Gaussian kernel and bandwidth h=2.0 Å. Sample the density function at 200 evenly spaced points from 0 to 40 Å. Identify local maxima and minima to define characteristic pore diameters and boundaries; assign each probe point a pore-size label (e.g., 1,2,3) based on the minima.
- Output file: `/app/outputs/kde_pore_size_dut32.csv`
- Format: csv
- Contract: Two columns: pore_diameter_A (float), density (float, unitless). 200 rows.
- Scoring: scored by hidden verifier

### Step 4: DBSCAN pore centre identification
- Role: scored
- Action: For each pore-size category obtained in Step 2, apply DBSCAN clustering to the labelled probe points to identify individual pore instances. Compute the geometric centre of each cluster. Output the Cartesian coordinates of each pore centre.
- Output file: `/app/outputs/pore_centers_dut32.csv`
- Format: csv
- Contract: Four columns: pore_label (int, 1,2,3), x_A (float), y_A (float), z_A (float).
- Scoring: scored by hidden verifier

### Step 5: GCMC Ar adsorption simulation
- Role: process
- Action: Perform grand canonical Monte Carlo simulations of argon in the DUT-32 supercell at 87 K, using YAFF with the Lennard-Jones parameters from Table 2 of the paper. Run 75 logarithmically spaced pressure points from 1e-5 to 1 bar. For each pressure, execute 1e7 Monte Carlo steps (insertion, deletion, translation with equal probability), discarding the first 5e6 as equilibration. Save trajectory snapshots (e.g., every 1000 cycles) for post-processing.
- Evidence: `/app/outputs/gcmc_trajectory.dcd`

### Step 6: Total adsorption isotherm
- Role: scored (load-bearing)
- Action: From the GCMC production averages, extract the argon uptake (loading in mmol/g) at each pressure and compile the adsorption isotherm.
- Output file: `/app/outputs/adsorption_isotherm_dut32.csv`
- Format: csv
- Contract: Two columns: pressure_bar (float), loading_mmol_g (float). 75 rows, logarithmically spaced from 1e-5 to 1 bar.
- Scoring: scored by hidden verifier

### Step 7: Pore-specific isotherms
- Role: scored (load-bearing)
- Action: For each GCMC snapshot, assign every argon atom to the nearest probe point (using the pore labels from Step 2) and tally the loading per pore category. Average over the production snapshots to obtain the loading as a function of pressure for each pore. Write the three pore isotherms.
- Output file: `/app/outputs/pore_isotherms_dut32.csv`
- Format: csv
- Contract: Four columns: pressure_bar (float), pore1_loading_mmol_g (float), pore2_loading_mmol_g (float), pore3_loading_mmol_g (float). Same pressure grid as the total isotherm.
- Scoring: scored by hidden verifier

### Step 8: Pore-centred radial distributions
- Role: scored (load-bearing)
- Action: At three selected pressure points (labelled P3, P4, P5 as in Figure 6 of the paper), compute the radial distribution of argon atoms from each pore centre (Step 3). Output the radial density profiles for each pore at each pressure.
- Output file: `/app/outputs/radial_distribution_dut32.csv`
- Format: csv
- Contract: Five columns: pressure_point (str, 'P3','P4','P5'), pore_label (int), radius_A (float), density_arb (float). Multiple rows per pressure and pore.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kde_pore_size_dut32.csv`
- `/app/outputs/pore_centers_dut32.csv`
- `/app/outputs/adsorption_isotherm_dut32.csv`
- `/app/outputs/pore_isotherms_dut32.csv`
- `/app/outputs/radial_distribution_dut32.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kde_pore_size_dut32.csv
- path: `/app/outputs/kde_pore_size_dut32.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Continuous pore-size density function from KDE; 200 rows from 0 to 40 Å. Characteristic pore diameters are compared to paper values within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `pore_diameter_A`, `density`
  - `units`:
    - `pore_diameter_A`: Angstrom
    - `density`: unitless

### pore_centers_dut32.csv
- path: `/app/outputs/pore_centers_dut32.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Coordinates of pore centres; the number of distinct pore labels (3 clusters) and their geometric separation are checked.
- schema:
  - `type`: table
  - `required_columns`: `pore_label`, `x_A`, `y_A`, `z_A`
  - `units`:
    - `x_A`: Angstrom
    - `y_A`: Angstrom
    - `z_A`: Angstrom

### adsorption_isotherm_dut32.csv
- path: `/app/outputs/adsorption_isotherm_dut32.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total Ar adsorption isotherm at 87 K; step pressure is compared to paper reference.
- schema:
  - `type`: table
  - `required_columns`: `pressure_bar`, `loading_mmol_g`
  - `units`:
    - `pressure_bar`: bar
    - `loading_mmol_g`: mmol/g

### pore_isotherms_dut32.csv
- path: `/app/outputs/pore_isotherms_dut32.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pore-specific isotherms; checked for cooperative filling (all pore loadings increase at the same step pressure).
- schema:
  - `type`: table
  - `required_columns`: `pressure_bar`, `pore1_loading_mmol_g`, `pore2_loading_mmol_g`, `pore3_loading_mmol_g`
  - `units`:
    - `pressure_bar`: bar
    - `pore1_loading_mmol_g`: mmol/g
    - `pore2_loading_mmol_g`: mmol/g
    - `pore3_loading_mmol_g`: mmol/g

### radial_distribution_dut32.csv
- path: `/app/outputs/radial_distribution_dut32.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Radial distribution profiles; presence of expected adsorption sites (e.g., peak at ~12 Å for p2) and overall peak patterns are assessed.
- schema:
  - `type`: table
  - `required_columns`: `pressure_point`, `pore_label`, `radius_A`, `density_arb`
  - `units`:
    - `radius_A`: Angstrom
    - `density_arb`: arbitrary units

Notes: All outputs are for DUT-32 only. The GCMC simulation (step_4) is computationally intensive; the solving agent may use external compute resources. The verification uses T0 result-level comparison against hidden paper-reported values and structural checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kde_pore_size_dut32.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pore_diameter_A",
          "density"
        ],
        "units": {
          "pore_diameter_A": "Angstrom",
          "density": "unitless"
        }
      },
      "description": "Continuous pore-size density function from KDE; 200 rows from 0 to 40 Å. Characteristic pore diameters are compared to paper values within a tolerance."
    },
    {
      "file": "pore_centers_dut32.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pore_label",
          "x_A",
          "y_A",
          "z_A"
        ],
        "units": {
          "x_A": "Angstrom",
          "y_A": "Angstrom",
          "z_A": "Angstrom"
        }
      },
      "description": "Coordinates of pore centres; the number of distinct pore labels (3 clusters) and their geometric separation are checked."
    },
    {
      "file": "adsorption_isotherm_dut32.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_bar",
          "loading_mmol_g"
        ],
        "units": {
          "pressure_bar": "bar",
          "loading_mmol_g": "mmol/g"
        }
      },
      "description": "Total Ar adsorption isotherm at 87 K; step pressure is compared to paper reference."
    },
    {
      "file": "pore_isotherms_dut32.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_bar",
          "pore1_loading_mmol_g",
          "pore2_loading_mmol_g",
          "pore3_loading_mmol_g"
        ],
        "units": {
          "pressure_bar": "bar",
          "pore1_loading_mmol_g": "mmol/g",
          "pore2_loading_mmol_g": "mmol/g",
          "pore3_loading_mmol_g": "mmol/g"
        }
      },
      "description": "Pore-specific isotherms; checked for cooperative filling (all pore loadings increase at the same step pressure)."
    },
    {
      "file": "radial_distribution_dut32.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_point",
          "pore_label",
          "radius_A",
          "density_arb"
        ],
        "units": {
          "radius_A": "Angstrom",
          "density_arb": "arbitrary units"
        }
      },
      "description": "Radial distribution profiles; presence of expected adsorption sites (e.g., peak at ~12 Å for p2) and overall peak patterns are assessed."
    }
  ],
  "notes": "All outputs are for DUT-32 only. The GCMC simulation (step_4) is computationally intensive; the solving agent may use external compute resources. The verification uses T0 result-level comparison against hidden paper-reported values and structural checks."
}
```

## How you are scored
A hidden verifier scores each output artifact independently. For `kde_pore_size_dut32.csv`, it compares the location and shape of the continuous pore‑size density to hidden reference values (peak locations and separation). For `pore_centers_dut32.csv`, it validates that the clustering identifies the expected number of pore clusters and that each has a well‑defined centre. For `adsorption_isotherm_dut32.csv`, it checks that the isotherm steps occur at a pressure consistent with a hidden reference. For `pore_isotherms_dut32.csv`, it verifies that all pore categories show a marked simultaneous increase in loading at a consistent pressure (cooperative filling signature). For `radial_distribution_dut32.csv`, it evaluates that the radial density profiles contain the expected adsorption features (e.g., a peak near the pore surface) and follow the correct trend across pressure points. The total reward is a weighted sum of the per‑artifact scores; the load‑bearing isotherm steps carry the highest weight. Merely reporting the paper’s numbers without correct internal consistency will not pass the checks.
