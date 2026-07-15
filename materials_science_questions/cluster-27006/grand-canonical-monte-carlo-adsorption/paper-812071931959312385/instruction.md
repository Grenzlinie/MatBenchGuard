# Methane Adsorption Isotherms and Phase Coexistence in a (30,30) Carbon Nanotube via Gauge-Cell Monte Carlo

## Problem background
Fluids confined in nanopores can undergo capillary phase transitions that differ markedly from bulk behavior. Single-walled carbon nanotubes (SWNTs) provide well-defined cylindrical confining geometries, making them ideal model systems for studying confinement-induced shifts in vapor–liquid coexistence and critical parameters. The gauge-cell Monte Carlo method is a molecular simulation technique that stabilizes the entire adsorption isotherm, including metastable and unstable regions that are inaccessible to standard grand canonical Monte Carlo (GCMC), and thereby enables direct determination of coexisting phases via a Maxwell equal-area construction. This task focuses on methane (C1), the simplest alkane, adsorbed in a (30,30) armchair SWNT. By computing the complete isotherm over a range of temperatures, you will extract vapor–liquid coexistence data and estimate the critical temperature and critical density, and then verify consistency with GCMC simulations.

## Approach
The core method is gauge-cell Monte Carlo simulation. Two simulation boxes are used: the main box contains the atomistic (30,30) SWNT, and a gauge cell of bulk fluid (periodic in all directions) acts as a chemical potential reservoir. The finite size of the gauge cell limits density fluctuations within the nanotube, allowing the fluid to explore stable, metastable, and unstable states along the adsorption isotherm. Configurational-bias Monte Carlo moves are employed to sample the positions and conformations of methane molecules efficiently. From the resulting isotherm (density vs. dimensionless configurational chemical potential) at subcritical temperatures, the saturation chemical potential and coexisting vapor and liquid densities are determined by applying the Maxwell equal-area condition. Using the coexistence data from several subcritical temperatures, the critical temperature and critical density are estimated by fitting a renormalization-group-based scaling relation. For comparison, grand canonical Monte Carlo simulations are also performed at the same thermodynamic conditions, and their densities are compared with those from the gauge-cell method in the stable and metastable regions.

## Reproduction target
The goal is to compute the full adsorption isotherms for methane in a (30,30) armchair SWNT from gauge-cell Monte Carlo simulations at 120, 140, 160, and 180 K, applying the Maxwell equal-area construction to the subcritical isotherms to obtain the saturation chemical potential and coexisting vapor/liquid densities, and fitting the critical temperature and critical density from those coexistence data. Additionally, grand canonical Monte Carlo simulations are run at the same temperatures, and the densities from both methods are compared in the stable/metastable region. The output consists of three CSV files: `isotherms_gcmc.csv` (density vs. chemical potential for all four temperatures), `coexistence.csv` (saturation chemical potential, vapor/liquid densities for 120, 140, 160 K, plus the fitted critical temperature and critical density), and `gcmc_comparison.csv` (densities from GCMC and gauge-cell MC and their difference).

## Assets

- Open-source molecular simulation code supporting configurational-bias and gauge-cell MC (e.g., Cassandra, Towhee, DL_MONTE)

## Workflow steps

### Step 1: System and force-field setup
- Role: process
- Action: Construct the (30,30) armchair SWNT geometry (radius derived from chiral index, length 30.74 Å, periodic along the axis). Define the united-atom methane Lennard-Jones parameters and carbon SWNT LJ parameters with Jorgensen combining rules. Set the spherical cutoff and gauge-cell dimensions. Record the key simulation parameters.
- Evidence: `/app/outputs/system_setup.txt`

### Step 2: Gauge-cell Monte Carlo isotherm simulation
- Role: scored
- Action: Run gauge-cell MC simulations for methane in the (30,30) SWNT at 120, 140, 160, and 180 K, using the specified move probabilities and cycle counts. Collect the overall density as a function of dimensionless configurational chemical potential. Output the complete isotherm data for all temperatures.
- Output file: `/app/outputs/isotherms_gcmc.csv`
- Format: csv
- Contract: columns: temperature (K), beta_mu_c (dimensionless), density (g/mL). One row per simulation point.
- Scoring: scored by hidden verifier

### Step 3: Maxwell equal-area construction and critical point
- Role: scored (load-bearing)
- Action: From the subcritical gauge-cell MC isotherms (120, 140, 160 K), determine the saturation chemical potential and coexisting vapor and liquid densities using the Maxwell equal-area condition. Fit the critical temperature and critical density using the renormalization-group-based equation from the coexistence data. Output the coexistence parameters and critical estimates.
- Output file: `/app/outputs/coexistence.csv`
- Format: csv
- Contract: The CSV has four columns: temperature, saturation_mu_c, vapor_density, liquid_density. For subcritical temperatures (120, 140, 160 K), these columns hold the saturation chemical potential and coexisting densities. After that, there are two extra rows where the first column (temperature) contains the string 'critical_temperature' or 'critical_density' and the second column (saturation_mu_c) holds the corresponding numeric value; the remaining columns are empty.
- Scoring: scored by hidden verifier

### Step 4: Grand canonical Monte Carlo simulation and method comparison
- Role: scored
- Action: Run GCMC simulations for methane in the same (30,30) SWNT at 120, 140, 160, and 180 K. At each chemical potential where both GCMC and gauge-cell MC produce a density in the stable or accessible metastable region, record the densities from both methods and their difference.
- Output file: `/app/outputs/gcmc_comparison.csv`
- Format: csv
- Contract: columns: temperature (K), beta_mu_c (dimensionless), density_gcmc (g/mL), density_gaugecell (g/mL), difference (g/mL). One row per chemical potential where both methods provided a density in the stable/metastable region.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/isotherms_gcmc.csv`
- `/app/outputs/coexistence.csv`
- `/app/outputs/gcmc_comparison.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### isotherms_gcmc.csv
- path: `/app/outputs/isotherms_gcmc.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Isotherm data from gauge-cell MC. The 180 K isotherm must be monotonic (density not decreasing as chemical potential increases).
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `beta_mu_c`, `density`
  - `units`:
    - `temperature`: K
    - `beta_mu_c`: dimensionless
    - `density`: g/mL

### coexistence.csv
- path: `/app/outputs/coexistence.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Coexistence parameters (saturation chemical potential, vapor/liquid densities) and fitted critical temperature and density.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `saturation_mu_c`, `vapor_density`, `liquid_density`
  - `units`:
    - `temperature`: K (or string for critical rows)
    - `saturation_mu_c`: dimensionless
    - `vapor_density`: g/mL
    - `liquid_density`: g/mL
  - `notes`: Rows for subcritical temperatures provide coexistence data. Two additional rows with temperature column 'critical_temperature' and 'critical_density' respectively hold the fitted critical values in the saturation_mu_c column.

### gcmc_comparison.csv
- path: `/app/outputs/gcmc_comparison.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Comparison of GCMC and gauge-cell MC densities in the stable/metastable regions. The absolute difference must be within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `beta_mu_c`, `density_gcmc`, `density_gaugecell`, `difference`
  - `units`:
    - `temperature`: K
    - `beta_mu_c`: dimensionless
    - `density_gcmc`: g/mL
    - `density_gaugecell`: g/mL
    - `difference`: g/mL

Notes: All outputs are plain text CSV files. The agent must write them to /app/outputs. The checker reads these files and compares against hidden paper-reported values and structural checks with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "isotherms_gcmc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "beta_mu_c",
          "density"
        ],
        "units": {
          "temperature": "K",
          "beta_mu_c": "dimensionless",
          "density": "g/mL"
        }
      },
      "description": "Isotherm data from gauge-cell MC. The 180 K isotherm must be monotonic (density not decreasing as chemical potential increases)."
    },
    {
      "file": "coexistence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "saturation_mu_c",
          "vapor_density",
          "liquid_density"
        ],
        "units": {
          "temperature": "K (or string for critical rows)",
          "saturation_mu_c": "dimensionless",
          "vapor_density": "g/mL",
          "liquid_density": "g/mL"
        },
        "notes": "Rows for subcritical temperatures provide coexistence data. Two additional rows with temperature column 'critical_temperature' and 'critical_density' respectively hold the fitted critical values in the saturation_mu_c column."
      },
      "description": "Coexistence parameters (saturation chemical potential, vapor/liquid densities) and fitted critical temperature and density."
    },
    {
      "file": "gcmc_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "beta_mu_c",
          "density_gcmc",
          "density_gaugecell",
          "difference"
        ],
        "units": {
          "temperature": "K",
          "beta_mu_c": "dimensionless",
          "density_gcmc": "g/mL",
          "density_gaugecell": "g/mL",
          "difference": "g/mL"
        }
      },
      "description": "Comparison of GCMC and gauge-cell MC densities in the stable/metastable regions. The absolute difference must be within tolerance."
    }
  ],
  "notes": "All outputs are plain text CSV files. The agent must write them to /app/outputs. The checker reads these files and compares against hidden paper-reported values and structural checks with tolerances."
}
```

## How you are scored
A hidden verifier will score each artifact independently and combine the scores into a final reward. The verifier checks that the 180 K isotherm in `isotherms_gcmc.csv` is monotonic, compares the saturation chemical potential and coexistence densities in `coexistence.csv` to reference values for the subcritical temperatures, compares the fitted critical temperature and critical density to reference values, and verifies that the absolute differences in `gcmc_comparison.csv` fall within a tolerance. The coexistence and critical parameters carry the largest weight, followed by the isotherm monotonicity check and the GCMC consistency check. Simply reporting the paper's numbers is not sufficient; the verifier validates that your submitted artifacts are consistent with the expected physics and values.
