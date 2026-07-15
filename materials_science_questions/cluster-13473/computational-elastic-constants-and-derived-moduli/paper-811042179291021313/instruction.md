# MD Determination of Glass Transition Temperature of PMMA via Density Method

## Problem background
The glass transition temperature (Tg) of amorphous and semi-crystalline polymers marks the boundary between a rubbery, viscous state and a rigid, glassy state. It is a key design parameter because it controls mechanical stiffness, thermal expansion, and processing windows. Polymethylmethacrylate (PMMA) is a widely used thermoplastic whose Tg influences applications from automotive to biomedical devices. Molecular dynamics (MD) simulations can predict Tg by cooling a polymer melt and monitoring how macroscopic properties—such as density or volume—change with temperature. As the system passes through the glass transition, the temperature dependence of these properties changes slope, and the intersection of two linear regimes gives an estimate of Tg. The goal of this task is to simulate isotactic PMMA using a united-atom force field and determine its Tg via the density/volume method at a specified cooling rate, producing both the raw density–temperature data and the computed transition temperature.

## Approach
A united-atom model of isotactic PMMA is built, where hydrogen atoms are implicitly included in the carbon groups to reduce computational cost. The interatomic interactions are described by the Okada force field, which includes bond stretching, angle bending, dihedral and improper torsions, and a Lennard-Jones non‑bonded potential. The system consists of three chains each with 100 monomers. An initial configuration is generated in a periodic box, energy is minimized, and the melt is equilibrated at high temperature (600 K) and zero pressure using an NPT ensemble. After equilibration, the system is cooled continuously from 600 K down to 300 K at a constant cooling rate while recording density at regular temperature intervals. The density–temperature curve is then converted to reduced volume (V−V₀)/V₀, where V₀ is taken at the starting temperature. The glass transition temperature is identified by fitting two linear segments to the reduced-volume curve—one for the rubbery regime and one for the glassy regime—and finding the temperature at which the two fitted lines intersect, using an orthogonal distance regression technique.

## Reproduction target
Reproduce the glass transition temperature of isotactic PMMA determined by the density/volume method at a cooling rate of 20 K/ns. The system is three chains each containing 100 united‑atom monomers. After equilibration, perform an NPT cooling run from 600 K to 300 K at exactly 20 K/ns, and record temperature and density at intervals of no more than 10 K. From this data, compute the reduced volume (V−V₀)/V₀ and fit two linear segments to obtain the intersection temperature—the glass transition temperature Tg. Output two files: (1) the density‑vs‑temperature data as a CSV, and (2) the computed Tg in Kelvin as a plain text file.

## Assets

- LAMMPS: https://lammps.sandia.gov/
- Okada et al. united-atom force field for PMMA: 10.1016/S1089-3156(00)00015-5

## Workflow steps

### Step 1: Generate initial PMMA configuration
- Role: process
- Action: Build an initial configuration of 3 linear isotactic PMMA chains, each with 100 monomers, using a united-atom model in a 40 Å cubic simulation box. Generate a LAMMPS data file (system.data) containing atom coordinates and bonding topology.
- Evidence: `/app/outputs/system.data`

### Step 2: Energy minimization and melt equilibration
- Role: process
- Action: Perform conjugate gradient energy minimization, thermal annealing (NVT from 600 K to 300 K and back), and then equilibrate the melt at 600 K and zero pressure using the NPT ensemble for 5 ns. Record the relaxation of the end-to-end vector autocorrelation to confirm equilibration.
- Evidence: `/app/outputs/equilibration.log`

### Step 3: Cooling production run
- Role: process
- Action: Starting from the equilibrated melt at 600 K, run NPT ensemble MD cooling from 600 K down to 300 K at a constant cooling rate of 20 K/ns (total 15 ns). Record temperature and density at intervals of no more than 10 K. Save the simulation log as cooling.log.
- Evidence: `/app/outputs/cooling.log`

### Step 4: Extract density vs temperature
- Role: scored (load-bearing)
- Action: Parse the cooling simulation log (cooling.log) and produce a CSV file containing temperature and density at each recorded step.
- Output file: `/app/outputs/density_vs_temperature.csv`
- Format: csv
- Contract: Two columns with a header row: temperature,density. Units: temperature (K), density (g/cm^3).
- Scoring: scored by hidden verifier

### Step 5: Determine glass transition temperature
- Role: scored
- Action: Using the density data, compute the reduced volume (V-V0)/V0 where V0 is the volume at 600 K, perform piecewise linear fitting (orthogonal distance regression) to the reduced-volume vs temperature curve, and output the intersection temperature as the glass transition temperature Tg.
- Output file: `/app/outputs/tg_from_density.txt`
- Format: txt
- Contract: Single numeric value in Kelvin, no extra text.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/density_vs_temperature.csv`
- `/app/outputs/tg_from_density.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### density_vs_temperature.csv
- path: `/app/outputs/density_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw density vs. temperature data from the cooling simulation, used by the checker to recompute the glass transition temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `density`
  - `units`:
    - `temperature`: K
    - `density`: g/cm^3

### tg_from_density.txt
- path: `/app/outputs/tg_from_density.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Agent-reported Tg computed from density data via piecewise linear fitting of reduced volume.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the glass transition temperature in Kelvin.

Notes: The checker recomputes Tg from density_vs_temperature.csv using orthogonal distance regression on reduced volume and compares both the recomputed Tg and the agent's reported Tg to a hidden reference value (with tolerance). The CSV must contain at least 30 data points and cover from above 550 K to below 400 K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "density_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "density"
        ],
        "units": {
          "temperature": "K",
          "density": "g/cm^3"
        }
      },
      "description": "Raw density vs. temperature data from the cooling simulation, used by the checker to recompute the glass transition temperature."
    },
    {
      "file": "tg_from_density.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the glass transition temperature in Kelvin."
      },
      "description": "Agent-reported Tg computed from density data via piecewise linear fitting of reduced volume."
    }
  ],
  "notes": "The checker recomputes Tg from density_vs_temperature.csv using orthogonal distance regression on reduced volume and compares both the recomputed Tg and the agent's reported Tg to a hidden reference value (with tolerance). The CSV must contain at least 30 data points and cover from above 550 K to below 400 K."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored workflow stage's output artifact. For the density‑temperature CSV, the verifier checks that it contains at least 30 data points spanning temperatures above 550 K and below 400 K. For the glass transition temperature, the verifier recomputes Tg from your submitted CSV using the same piecewise linear fitting procedure and compares both the recomputed Tg and your reported Tg to a hidden reference value. Each stage is assigned a weight, and the final score is the weighted sum. Reporting the paper's numbers without executing the full simulation and analysis pipeline will result in a low score because the verifier's own recomputation of Tg from your density data must agree with your reported Tg and both must match the hidden reference within an allowed tolerance.
