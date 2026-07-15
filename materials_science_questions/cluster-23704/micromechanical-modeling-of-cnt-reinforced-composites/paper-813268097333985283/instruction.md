# CNT Bundle Irradiation and Mechanical Property Scaling

## Problem background
Carbon nanotube (CNT) bundles are promising building blocks for high-strength, tough composite fibres. However, the van der Waals forces that hold a bundle together are very weak in shear, causing poor load transfer and low toughness. Irradiating CNT bundles with carbon ions can create covalent inter-tube cross-links that dramatically enhance shear properties, but the same irradiation also introduces defects (vacancies, adatoms, larger holes) that may reduce the tensile strength of the individual tubes. This trade-off between improved shear and reduced tensile performance is influenced by the irradiation conditions, particularly the incident ion energy and the total fluence. Understanding how the resulting cross-link density controls interfacial shear modulus, shear strength, and frictional sliding stress, and how the size of irradiation-induced holes governs the remaining tensile strength, is essential for designing tough CNT fibres. This task aims to reproduce those quantitative scaling relationships by simulating the irradiation process and mechanical tests at the atomistic level.

## Approach
The reproduction uses classical molecular dynamics (MD) with a modified REBO (reactive empirical bond order) potential that includes an environment-dependent cutoff, enabling accurate bond breaking and re-forming during irradiation and mechanical loading.

**System setup**  
A hexagonal bundle of seven (26,0) single-walled carbon nanotubes (SWCNTs) is constructed. Each tube has a radius of 10.18 Å and a length of 59.6 Å. Periodic boundary conditions are applied along the tube axis to model an infinitely long bundle.

**Irradiation**  
Carbon ions are deposited at a fixed kinetic energy of 100 eV/ion. The fluence is varied by changing the number of deposition rings: 1 ring, 3 rings, and 5 rings, representing three distinct damage levels. The deposition atoms are fired toward the bundle with random trajectories within a ±28° angular spread. After each ring the system is relaxed and cooled, yielding three irradiated bundle configurations.

**Characterisation**  
For each irradiated configuration, the inter-tube links connecting the central CNT to the surrounding tubes are counted and converted to an areal inter-tube link density ρ (links per nm²) using a pre-defined reference shear area. The largest hole in any tube is also measured.

**Mechanical testing**  
- *Pull-out test*: The central CNT is pulled axially (0.025 Å every 0.25 ps) while the outer tube ends are fixed. Force vs. displacement is recorded under NVE dynamics at 0.5 K. The pull-out force is converted to interfacial shear stress using the reference shear area. From the resulting curve, the interface shear modulus (slope of the elastic region), the shear strength (stress at debond onset), and the average sliding stress (for displacement >8 Å) are extracted.
- *Tensile test*: The full bundle is stretched at the same displacement rate under NPT conditions at 0.5 K. Stress vs. strain is recorded until failure, giving the ultimate tensile strength and maximum strain, together with the previously measured largest hole size.

**Data analysis**  
For the three fluence conditions, the extracted properties are compiled into two CSV tables. The relationships between ρ and the three shear properties, and between the largest hole size and tensile strength, are then examined by regression to quantify how these mechanical properties scale.

## Reproduction target
Produce the two scored CSV files described in the workflow steps below (`shear_properties.csv` and `tensile_properties.csv`). The files must contain the per-condition data for the three irradiation fluences (100 eV/ion, 1/3/5 rings). The hidden verifier will use these tables to recompute the scaling relationships: linear fits of interface shear modulus (G), shear strength (τ_yield), and sliding stress (τ_sliding) versus areal inter-tube link density (ρ), and a power-law fit of ultimate tensile strength (UTS) versus largest hole size. The slopes and exponent obtained from your data will be compared against reference values to determine how closely your reproduction matches the expected physical trends.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- Modified REBO potential (environment-dependent cutoff): pair_style rebo in LAMMPS
- OVITO (optional visualization): https://www.ovito.org/

## Workflow steps

### Step 1: Build CNT bundle geometry and deposition rings
- Role: process
- Action: Construct the initial atomic model of a hexagonally arranged 7-tube (26,0) SWCNT bundle (radius 10.18 Å, tube length 59.6 Å) and set up the five rings of deposition carbon atoms with random trajectories within ±28° angular spread. Generate LAMMPS input geometry files.
- Evidence: `/app/outputs/geometry.log`

### Step 2: Carbon-ion irradiation simulations (100 eV, 1/3/5 rings)
- Role: process
- Action: Run MD simulations of carbon ion irradiation at 100 eV/ion using the modified REBO potential. Use 1, 3, and 5 deposition rings, corresponding to fluences of approximately 4×10¹³, 1.2×10¹⁴, and 2×10¹⁴ cm⁻². Apply periodic boundary conditions in the z-direction, fire in deposition rings sequentially, and relax/cool the system after each ring. Produce post-irradiation atomic structures (trajectory snapshots) for each condition.
- Evidence: `/app/outputs/irradiation.log`

### Step 3: Post-irradiation characterization of cross-links and defects
- Role: process
- Action: For each irradiated bundle, count the number of centre-tube inter-tube links (links between the centre CNT and outer tubes) and measure the largest hole size (largest distance across a hole). Compute the areal inter-tube link density ρ = count / A_SH, where A_SH is the pre-irradiation reference shear area defined as the area of outer-tube atoms within the modified REBO interaction distance of the centre tube. Output per-condition data: condition, ρ, largest hole size.
- Evidence: `/app/outputs/characterization.csv`

### Step 4: Pull-out mechanical tests on irradiated bundles
- Role: process
- Action: Perform MD centre-CNT pull-out tests on each irradiated bundle. Displace the centre tube axially in increments of 0.025 Å every 0.25 ps while fixing outer tube ends in the z-direction and applying periodic boundary conditions. Use velocity-rescaling thermostat at 0.5 K and an NVE ensemble. Record pull-out force F_pull versus displacement x for each condition.
- Evidence: `/app/outputs/pullout_raw.csv`

### Step 5: Tensile mechanical tests on irradiated bundles
- Role: process
- Action: Perform MD tensile tests on each irradiated bundle under NPT ensemble with periodic boundary conditions. Apply a constant strain rate of 10 m/s (displacement step 0.025 Å) along the tube axis at 0.5 K, allowing the simulation box to vary. Record tensile stress σ versus strain ε until failure for each condition.
- Evidence: `/app/outputs/tensile_raw.csv`

### Step 6: Extract scored shear properties
- Role: scored (load-bearing)
- Action: From the pull-out force-displacement data, convert force to interfacial shear stress using τ_int = F_pull / A_SH. Identify the elastic (linear) regime, debonding onset (end of linear region), and sliding regime (x > 8 Å). For each condition, compute: interface shear modulus μ (slope of the linear region), interface shear strength τ_y (stress at debonding onset), and average sliding stress τ. Compile the results together with the corresponding areal link density ρ from the characterization step into a CSV file.
- Output file: `/app/outputs/shear_properties.csv`
- Format: csv
- Contract: Columns: condition (string), rho (float, nm⁻²), G (float, GPa), tau_yield (float, GPa), tau_sliding (float, GPa)
- Scoring: scored by hidden verifier

### Step 7: Extract scored tensile properties
- Role: scored
- Action: From the tensile stress-strain curves, determine the ultimate tensile strength σ_ult and maximum strain ε_max for each irradiated condition. Combine with the corresponding largest hole size c (nm) from the characterization step. Save to CSV.
- Output file: `/app/outputs/tensile_properties.csv`
- Format: csv
- Contract: Columns: condition (string), UTS_GPa (float), max_strain (float), largest_hole_size_nm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/shear_properties.csv`
- `/app/outputs/tensile_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### shear_properties.csv
- path: `/app/outputs/shear_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-irradiation-condition interfacial shear properties and corresponding areal inter-tube link density. The hidden checker will perform linear regressions of G vs rho, tau_yield vs rho, and tau_sliding vs rho, and compare the slopes to reference values.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `rho`, `G`, `tau_yield`, `tau_sliding`
  - `units`:
    - `rho`: nm^-2
    - `G`: GPa
    - `tau_yield`: GPa
    - `tau_sliding`: GPa

### tensile_properties.csv
- path: `/app/outputs/tensile_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-irradiation-condition tensile properties and largest hole size. The hidden checker will fit a power law σ_ult ∝ c^{-m} to the data and compare the exponent to a reference value.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `UTS_GPa`, `max_strain`, `largest_hole_size_nm`
  - `units`:
    - `UTS_GPa`: GPa
    - `max_strain`: dimensionless
    - `largest_hole_size_nm`: nm

Notes: The checker uses the provided tables to recompute scaling relationships; no raw simulation files are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "shear_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "rho",
          "G",
          "tau_yield",
          "tau_sliding"
        ],
        "units": {
          "rho": "nm^-2",
          "G": "GPa",
          "tau_yield": "GPa",
          "tau_sliding": "GPa"
        }
      },
      "description": "Per-irradiation-condition interfacial shear properties and corresponding areal inter-tube link density. The hidden checker will perform linear regressions of G vs rho, tau_yield vs rho, and tau_sliding vs rho, and compare the slopes to reference values."
    },
    {
      "file": "tensile_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "UTS_GPa",
          "max_strain",
          "largest_hole_size_nm"
        ],
        "units": {
          "UTS_GPa": "GPa",
          "max_strain": "dimensionless",
          "largest_hole_size_nm": "nm"
        }
      },
      "description": "Per-irradiation-condition tensile properties and largest hole size. The hidden checker will fit a power law σ_ult ∝ c^{-m} to the data and compare the exponent to a reference value."
    }
  ],
  "notes": "The checker uses the provided tables to recompute scaling relationships; no raw simulation files are scored."
}
```

## How you are scored
After you submit the required output files to `/app/outputs`, a hidden verifier reads them and independently performs the following checks:

- **Format validation**: The verifier confirms that both CSV files contain the exact columns specified in the workflow steps and that all values are present and of the correct type.
- **Regression analyses**:  
  - It carries out linear regressions of G vs. ρ, τ_yield vs. ρ, and τ_sliding vs. ρ using your `shear_properties.csv`.  
  - It carries out a power-law fit (UTS ∝ c⁻ᵐ) using your `tensile_properties.csv`.
- **Comparison to reference**: The obtained slopes (three linear regressions) and the power-law exponent are compared to hidden reference values derived from the original study. The closeness of your computed scaling to those references determines the score for each regression.
- **Combined reward**: The final score weights the four regression comparisons (three shear slopes and one tensile exponent) and sums the weighted results. Reporting numbers without running the full MD workflow will not produce correct regressions and will not receive a high score.
