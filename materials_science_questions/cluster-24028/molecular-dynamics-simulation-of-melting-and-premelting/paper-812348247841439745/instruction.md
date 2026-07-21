# MD Simulation of Gold Icosahedra Assemblies: Thermal Diffusion and Planarity

## Problem background
Gold nanoparticles and their one- and two-dimensional assemblies are promising building blocks for nanotechnology due to their unique optical, electronic, and structural properties. Understanding the thermal stability and structural evolution of these nanostructures is critical for device applications. In this work, molecular dynamics simulations are used to study the assembly of small gold icosahedral clusters into nanowires and nanofilms, and to investigate their thermal behavior and structural thresholds at elevated temperatures.

## Approach
The study employs classical molecular dynamics with the many-body embedded-atom method (EAM) potential specifically parameterized for gold, which accurately reproduces bulk melting and surface reconstructions. Ideal Mackay icosahedra of 55 and 147 atoms are first equilibrated at 300 K, then placed in contact to form linear chains of 5 and 10 clusters (nanowires) and 5×5 square arrays (nanofilms). The assemblies are further equilibrated at 300 K, followed by stepwise heating from 300 K to 1400 K in 100 K increments, with full equilibration at each temperature. From the resulting trajectories, the mean-square displacement of atoms in the nanowires is used to derive diffusion coefficients via linear fits, while the in-plane dimensions and thickness of the nanofilms are measured to compute planarity ratios. These metrics quantify the onset of melting and loss of film integrity as temperature rises.

## Reproduction target
For each of the four nanowire assemblies (5 × 55, 10 × 55, 5 × 147, 10 × 147 atoms) compute the diffusion coefficient (in Å²/ps) at temperatures 300, 600, 800, 900, 1000, 1100, 1200, 1300, and 1400 K. For the two nanofilm assemblies (5×5 of 55-atom clusters and 5×5 of 147-atom clusters) compute the planarity ratio (in-plane diameter divided by thickness) at the same temperature set. Determine, for each nanowire assembly, the lowest temperature at which the diffusion coefficient exceeds a hidden threshold indicative of liquid-like diffusive behavior (melting onset). For each nanofilm assembly, determine the highest temperature at which the planarity ratio remains above a hidden threshold defining a stable film morphology.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov/download.html
- Ercolessi-Adams EAM potential for gold: https://www.ctcms.nist.gov/potentials/Download/Au/Au_Ercolessi.eam.fcc

## Workflow steps

### Step 1: Prepare isolated icosahedral clusters
- Role: process
- Action: Generate ideal Mackay icosahedra of 55 and 147 atoms, anneal and quench, then equilibrate at 300 K using the Ercolessi-Adams EAM potential.
- Evidence: none

### Step 2: Assemble clusters into nanowires and nanofilms
- Role: process
- Action: Place the pre-equilibrated icosahedra in contact to form linear nanowires of 5 and 10 clusters and 5x5 square nanofilms, for both 55- and 147-atom clusters.
- Evidence: none

### Step 3: Equilibrate assemblies at 300 K
- Role: process
- Action: Run MD simulation for 1e6 time steps (7.1 ns) at 300 K on each assembled structure to obtain stable room-temperature configurations.
- Evidence: none

### Step 4: Stepwise heating MD simulations
- Role: process
- Action: For each equilibrated assembly, perform stepwise heating from 300 K to 1400 K in 100 K increments, equilibrating 1e6 time steps at each temperature.
- Evidence: none

### Step 5: Diffusion coefficient analysis for nanowires
- Role: scored (load-bearing)
- Action: From the heating trajectories, compute mean-square displacements (MSD) for each nanowire assembly (5x55, 10x55, 5x147, 10x147) at each temperature. Save raw MSD data to nanowire_msd.csv. Perform linear fits of MSD vs time to obtain diffusion coefficients D, and save them to nanowire_diffusion.csv.
- Output file: `/app/outputs/nanowire_diffusion.csv`
- Format: csv
- Contract: CSV with columns: assembly (str), temperature (float, K), diffusion_coefficient (float, Å^2/ps).
- Scoring: scored by hidden verifier

### Step 6: Planarity analysis for nanofilms
- Role: scored (load-bearing)
- Action: From the heating trajectories, compute the thickness and average in-plane dimension for each nanofilm assembly (5x5 of 55-atom clusters and 5x5 of 147-atom clusters) at each temperature. Calculate planarity_ratio = (in-plane diameter) / thickness and save to nanofilm_planarity.csv.
- Output file: `/app/outputs/nanofilm_planarity.csv`
- Format: csv
- Contract: CSV with columns: assembly (str), temperature (float, K), planarity_ratio (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nanowire_diffusion.csv`
- `/app/outputs/nanofilm_planarity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nanowire_diffusion.csv
- path: `/app/outputs/nanowire_diffusion.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Diffusion coefficients for the four nanowire assemblies (5x55, 10x55, 5x147, 10x147) at each temperature. Melting onset is indicated when D exceeds a system-dependent threshold.
- schema:
  - `type`: table
  - `required_columns`: `assembly`, `temperature`, `diffusion_coefficient`
  - `units`:
    - `temperature`: K
    - `diffusion_coefficient`: Å^2/ps

### nanofilm_planarity.csv
- path: `/app/outputs/nanofilm_planarity.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Planarity ratio (in-plane diameter / thickness) for the two nanofilm assemblies (5x5 of 55-atom clusters, 5x5 of 147-atom clusters) at each temperature. A ratio >= 2.0 indicates a stable film morphology.
- schema:
  - `type`: table
  - `required_columns`: `assembly`, `temperature`, `planarity_ratio`
  - `units`:
    - `temperature`: K
    - `planarity_ratio`: dimensionless

Notes: The agent must run the full MD pipeline; the checker compares the reported D and planarity ratio values against hidden paper-derived thresholds, using threshold_or_better policy. No exact gold values are given in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nanowire_diffusion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "assembly",
          "temperature",
          "diffusion_coefficient"
        ],
        "units": {
          "temperature": "K",
          "diffusion_coefficient": "Å^2/ps"
        }
      },
      "description": "Diffusion coefficients for the four nanowire assemblies (5x55, 10x55, 5x147, 10x147) at each temperature. Melting onset is indicated when D exceeds a system-dependent threshold."
    },
    {
      "file": "nanofilm_planarity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "assembly",
          "temperature",
          "planarity_ratio"
        ],
        "units": {
          "temperature": "K",
          "planarity_ratio": "dimensionless"
        }
      },
      "description": "Planarity ratio (in-plane diameter / thickness) for the two nanofilm assemblies (5x5 of 55-atom clusters, 5x5 of 147-atom clusters) at each temperature. A ratio >= 2.0 indicates a stable film morphology."
    }
  ],
  "notes": "The agent must run the full MD pipeline; the checker compares the reported D and planarity ratio values against hidden paper-derived thresholds, using threshold_or_better policy. No exact gold values are given in the public contract."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently reads your output CSV files. For each nanowire assembly, the verifier compares your reported diffusion coefficients against pre-defined reference thresholds, granting full credit if the values meet or surpass the expected regime (low D at low T, high D at high T) and partial credit otherwise. For the nanofilm assemblies, the planarity ratios are similarly compared against reference thresholds. Each scored artifact carries a weight, and your final reward is a weighted average. The verifier does not run the full MD simulations; it only evaluates the final reported quantities. Ensure that the CSV files strictly follow the required schema; shape checks contribute minimal weight.
