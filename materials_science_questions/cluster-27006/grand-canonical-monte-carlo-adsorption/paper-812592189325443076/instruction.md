# Reverse Monte Carlo carbon pore model generation and adsorption isotherm simulation

## Problem background
Porous carbons are important industrial adsorbents, but their complex pore morphology is often approximated by simple slit‑pore models that cannot capture connectivity, edge effects, or non‑planar pore shapes. This work develops a reverse Monte Carlo (RMC) method that, starting from rigid polyaromatic carbon plates, refines an atomistic model to reproduce a target carbon‑carbon radial distribution function (g(r)) while maintaining a prescribed carbon density. The resulting structures exhibit realistic non‑slit‑like porosity and can be used for subsequent adsorption simulations.

## Approach
The task follows a computational pipeline in four stages:

1. **Generate a target structure via molecular dynamics.** Build an initial carbon plate configuration in a 50 Å periodic cubic cell with a target density of 1.138 g/cm³, a mean of 35 rings per plate, and a standard deviation of 10. Perform NVT molecular dynamics at 300 K using a Lennard‑Jones potential for carbon‑carbon interactions (σ = 3.40 Å, ε/kB = 28 K). Collect the carbon‑carbon radial distribution function g_target(r).

2. **Reverse Monte Carlo refinement.** Create an independent initial structure with a density of 1.10 g/cm³ and exactly 20 rings per plate. Run RMC cycles that alternate configurational moves (50/50 translate/rotate) with ring creation/annihilation moves, plus plate creation/annihilation moves when the instantaneous density deviates from the target by more than a few percent. Accept a move only if the chi‑squared deviation between the current and target g(r) decreases. Continue until convergence, yielding the MODEL structure.

3. **Structural characterization of the MODEL.** From the MODEL, compute the carbon density (g/cm³), the average number of rings per plate, the standard deviation of ring count, the number of carbons per plate, the porosity (reentrant‑surface definition using a nitrogen probe, cutoff distance σ_NC – 0.5 σ_NN), and the geometric accessible surface area (probe distance σ_NC). The Lennard‑Jones cross‑interaction parameters are σ_NC = 3.36 Å, ε_NC/kB = 61.4 K; the nitrogen self‑interaction is σ_NN = 3.75 Å, ε_NN/kB = 95.2 K.

4. **Grand canonical Monte Carlo simulation of nitrogen adsorption.** Use the spherical Lennard‑Jones model for nitrogen and perform GCMC at 77 K in the MODEL structure. Relate chemical potential to absolute pressure via a virial expansion truncated at the second virial coefficient B = –210.36 cm³/mol. Run at a series of pressures up to at least 0.133 bar, equilibrate thoroughly, and collect loading statistics. Convert the average loading to cm³ (STP) per gram of carbon. Save the isotherm as the required CSV.

## Reproduction target
Your objective is to execute the full pipeline and report two scored artifacts: (i) the structural properties of the MODEL carbon (density, ring‑plate statistics, porosity, surface area), and (ii) the nitrogen adsorption isotherm at 77 K. The hidden verifier will compare your computed values against reference values obtained from the same computational protocol, checking the structural agreement and that the isotherm exhibits the expected shape and loading magnitude.

## Assets
This task does not require any external datasets, pre‑trained models, or proprietary tools. All necessary Lennard‑Jones interaction parameters and the nitrogen second virial coefficient are provided in the Approach section. The workflow can be implemented using standard open‑source molecular simulation and Monte Carlo libraries.

## Workflow steps

### Step 1: Generate TARGET carbon structure via MD
- Role: process
- Action: Build an initial carbon plate configuration in a periodic cubic simulation cell using the specified target density, mean rings per plate, and standard deviation. Perform NVT molecular dynamics at 300 K with Lennard-Jones interactions (C-C parameters provided). Equilibrate and collect the carbon-carbon radial distribution function g_target(r). Save the g(r) data for downstream RMC.
- Evidence: `/app/outputs/target_gr.csv`

### Step 2: RMC refinement to produce MODEL structure
- Role: process
- Action: Create an independent initial carbon structure with a different density and fixed plate ring count. Run reverse Monte Carlo cycles (alternating configurational and ring moves, with density-regulation plate moves) using the target g(r) as reference and the chi-square acceptance criterion. Continue until convergence. Save the final MODEL atomistic configuration.
- Evidence: `/app/outputs/model_structure.xyz`

### Step 3: Characterize MODEL structural properties
- Role: scored
- Action: From the MODEL structure, compute density (g/cm³), average number of rings per plate, standard deviation of ring count, number of carbons per plate, porosity using a nitrogen probe (reentrant surface definition with given Lennard-Jones parameters), and geometric accessible surface area (m²/g) using the accessible surface definition. Write the results as a single‑row CSV with the columns specified in the contract.
- Output file: `/app/outputs/model_structural_properties.csv`
- Format: csv
- Contract: CSV with header row and one data row. Columns: density_g_per_cm3,avg_rings_per_plate,std_dev_rings,carbons_per_plate,porosity,surface_area_m2_per_g. All values are numeric.
- Scoring: scored by hidden verifier

### Step 4: Compute N2 adsorption isotherm on MODEL via GCMC
- Role: scored (load-bearing)
- Action: Perform Grand Canonical Monte Carlo simulations of nitrogen (spherical Lennard-Jones model, parameters provided) adsorbed in the MODEL carbon structure at 77 K. Relate chemical potential to absolute pressure using a virial expansion truncated at the second virial coefficient (B value provided). Run at a series of pressures up to at least 0.133 bar. Convert average loading to cm³ (STP) per gram of carbon. Output a CSV with columns pressure_bar and loading_cm3stp_per_g, covering the full pressure range with enough points to resolve the isotherm shape.
- Output file: `/app/outputs/model_isotherm.csv`
- Format: csv
- Contract: CSV with header row and multiple data rows. Columns: pressure_bar,loading_cm3stp_per_g. Pressures should cover 0 to at least 0.133 bar. All values are numeric.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_structural_properties.csv`
- `/app/outputs/model_isotherm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_structural_properties.csv
- path: `/app/outputs/model_structural_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Single-row CSV containing the key structural properties of the MODEL carbon. The checker compares these values to reference values derived from the paper's Table 1 with absolute tolerances.
- schema:
  - `type`: table
  - `required_columns`: `density_g_per_cm3`, `avg_rings_per_plate`, `std_dev_rings`, `carbons_per_plate`, `porosity`, `surface_area_m2_per_g`
  - `units`:
    - `density_g_per_cm3`: g/cm3
    - `avg_rings_per_plate`: ring count
    - `std_dev_rings`: ring count
    - `carbons_per_plate`: count
    - `porosity`: fraction
    - `surface_area_m2_per_g`: m2/g

### model_isotherm.csv
- path: `/app/outputs/model_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Table of the nitrogen adsorption isotherm. The checker verifies that the loading at a reference pressure exceeds a threshold and that the isotherm shape exhibits a characteristic cusp (capillary condensation).
- schema:
  - `type`: table
  - `required_columns`: `pressure_bar`, `loading_cm3stp_per_g`
  - `units`:
    - `pressure_bar`: bar
    - `loading_cm3stp_per_g`: cm3 STP per gram carbon

Notes: All Lennard-Jones parameters and necessary constants (second virial coefficient, etc.) are provided in the task instructions; no external data files are required. The checker uses hidden gold values extracted from the paper's Table 1 and digitized isotherm from Figure 10.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_structural_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "density_g_per_cm3",
          "avg_rings_per_plate",
          "std_dev_rings",
          "carbons_per_plate",
          "porosity",
          "surface_area_m2_per_g"
        ],
        "units": {
          "density_g_per_cm3": "g/cm3",
          "avg_rings_per_plate": "ring count",
          "std_dev_rings": "ring count",
          "carbons_per_plate": "count",
          "porosity": "fraction",
          "surface_area_m2_per_g": "m2/g"
        }
      },
      "description": "Single-row CSV containing the key structural properties of the MODEL carbon. The checker compares these values to reference values derived from the paper's Table 1 with absolute tolerances."
    },
    {
      "file": "model_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_bar",
          "loading_cm3stp_per_g"
        ],
        "units": {
          "pressure_bar": "bar",
          "loading_cm3stp_per_g": "cm3 STP per gram carbon"
        }
      },
      "description": "Table of the nitrogen adsorption isotherm. The checker verifies that the loading at a reference pressure exceeds a threshold and that the isotherm shape exhibits a characteristic cusp (capillary condensation)."
    }
  ],
  "notes": "All Lennard-Jones parameters and necessary constants (second virial coefficient, etc.) are provided in the task instructions; no external data files are required. The checker uses hidden gold values extracted from the paper's Table 1 and digitized isotherm from Figure 10."
}
```

## How you are scored
A hidden verifier reads your two CSV output files. For `model_structural_properties.csv`, each numeric column is compared to a reference value within an appropriate tolerance. For `model_isotherm.csv`, the verifier checks that the loading at a reference condition meets an expected threshold and that the overall isotherm shape is physically reasonable (e.g., consistent with microporous adsorption). The total reward is a weighted sum of the structural score (~60 %) and the isotherm score (~40 %). Full credit is given when your results meet or exceed the expected quality, and the score decreases as the computed values deviate from the reference.
