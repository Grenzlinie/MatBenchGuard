# Monte Carlo Simulation of Wetting Transitions for H₂ and Ne on Alkali Metal Surfaces

## Problem background
Adsorption of light gases on alkali metal surfaces exhibits ultraweak interactions that give rise to rich wetting phenomena. Depending on the temperature and the strength of the gas–surface potential, an adsorbed film may grow continuously up to saturation (complete wetting) or remain limited to low coverage until the bulk vapour–liquid transition occurs (incomplete wetting). Predicting these regimes requires accurate simulation of adsorption isotherms using grand canonical Monte Carlo (GCMC) methods, both classical and quantum (path-integral). This task asks you to compute such isotherms for hydrogen on rubidium and neon on model alkali surfaces, and to determine the wetting behaviour from the resulting coverage curves.

## Approach
The core idea is to simulate adsorption directly in the grand canonical ensemble, where the chemical potential (or pressure) is controlled and the number of adsorbed molecules is sampled by Monte Carlo moves. For neon, classical GCMC is used with Lennard‑Jones Ne–Ne interactions and a gas–surface potential of the form V(z) = 4C³/(27D²z⁹) − C/z³, where the well depth D models different alkali surfaces. For hydrogen, quantum effects are included via a path‑integral formulation (PI‑GCMC) with the Silvera–Goldman H₂–H₂ potential and a Rb–H₂ adsorption potential. A multiple‑time‑step hybrid Monte Carlo algorithm evolves the paths. The simulation box is periodic in the lateral directions with a repulsive wall to suppress capillary condensation, and the bead‑bead cutoff respects the molecular size. By scanning the chemical potential (for H₂) or pressure (for Ne) across the transition region, you build an adsorption isotherm. The wetting classification follows from the isotherm shape: a sharp coverage jump at saturation signals incomplete wetting, while a continuous increase toward the saturation level indicates complete wetting. Your task is to implement these simulations and produce the isotherm files under the conditions specified in the workflow steps.

## Reproduction target
Produce two CSV files corresponding to the two sets of simulations:
- `/app/outputs/neon_isotherms.csv`: Ne coverage as a function of pressure for four (temperature, well depth D) conditions — (34.3 K, 75 K), (34.3 K, 50 K), (40.7 K, 50 K), and (40.7 K, 14 K). At least 8 pressure points per condition must be included so the isotherm shape can be resolved.
- `/app/outputs/hydrogen_isotherms.csv`: H₂ coverage as a function of reduced chemical potential μ* (μ* = μ/ε, ε = 32.21 K) for three temperatures — 18 K, 22 K, and 30 K. At least 10 μ* points per temperature are required, covering the transition region.

The hidden verifier will analyze your submitted isotherms to determine whether each condition exhibits incomplete wetting (a sharp jump in coverage) or complete wetting (continuous monotonic growth). Your simulation parameters and protocol must be chosen so that the isotherms faithfully reflect the physics of the system, as described in the workflow steps and the assets provided.

## Assets

- Silvera–Goldman H₂–H₂ potential: 10.1063/1.436090
- Cheng et al. Rb–H₂ adsorption potential (1993): 10.1103/PhysRevLett.70.1854
- Lennard‑Jones parameters for Ne
- Cheng et al. Rb–Ne gas‑surface potential (1993): 10.1103/PhysRevB.48.18214
- Multiple‑time‑step PI‑HMC algorithm (Tuckerman et al. 1993): 10.1063/1.464397
- Open‑source GCMC simulation code (e.g., RASPA, Cassandra, custom implementation): https://iraspa.org/raspa/

## Workflow steps

### Step 1: Neon GCMC simulation
- Role: scored (load-bearing)
- Action: Run classical grand canonical Monte Carlo (GCMC) simulations for Ne adsorption on model alkali metal surfaces. Use Lennard‑Jones Ne–Ne interactions (ε=33.9 K, σ=2.78 Å) and the Rb–Ne gas‑surface potential V(z)=4C³/(27D²z⁹)−C/z³ with well depth D. Simulation box: 27.8×27.8×75 Å³, periodic in x,y, hard repulsive wall at z=75 Å. Perform simulations at the following (T, D) conditions: (34.3 K, D=75 K), (34.3 K, D=50 K), (40.7 K, D=50 K), (40.7 K, D=14 K). For each condition, scan pressure to obtain an adsorption isotherm (coverage vs. pressure). Write results to a CSV file.
- Output file: `/app/outputs/neon_isotherms.csv`
- Format: csv
- Contract: Columns: temperature_K (int), well_depth_D_K (float), pressure (float), coverage (float). At least 8 pressure points per condition covering the isotherm.
- Scoring: scored by hidden verifier

### Step 2: Hydrogen path‑integral GCMC simulation
- Role: scored (load-bearing)
- Action: Run path‑integral grand canonical Monte Carlo (PI‑GCMC) simulations for H₂ on Rb. Use the Silvera–Goldman H₂–H₂ potential (ε=32.21 K, σ=3.003 Å) and the Rb–H₂ potential from Cheng et al. (1993). Simulation box: periodic in x,y, lateral dimensions >10σ, repulsive wall separation >6σ, bead‑bead cutoff 5σ. Employ multiple‑time‑step PI‑HMC with move probabilities (displace 0.1, creation 0.45, deletion 0.45). Perform simulations at T=18 K, 22 K, and 30 K, scanning the reduced chemical potential μ* = μ/ε (ε=32.21 K) around the phase transition region. For each temperature, record coverage as function of μ*. Write results to a CSV file.
- Output file: `/app/outputs/hydrogen_isotherms.csv`
- Format: csv
- Contract: Columns: temperature_K (int), reduced_chemical_potential (float), coverage (float). At least 10 points per temperature covering the transition region.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/neon_isotherms.csv`
- `/app/outputs/hydrogen_isotherms.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### neon_isotherms.csv
- path: `/app/outputs/neon_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ne adsorption isotherms; the checker classifies wetting/non‑wetting from coverage at the highest pressure for each condition, without requiring absolute units.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `well_depth_D_K`, `pressure`, `coverage`
  - `units`:
    - `temperature_K`: K
    - `well_depth_D_K`: K
    - `pressure`: arbitrary units
    - `coverage`: arbitrary consistent units

### hydrogen_isotherms.csv
- path: `/app/outputs/hydrogen_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: H₂ adsorption isotherms; the checker identifies the μ* interval of the abrupt coverage jump (incomplete wetting) and verifies continuous monotonic growth at 30 K (complete wetting).
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `reduced_chemical_potential`, `coverage`
  - `units`:
    - `temperature_K`: K
    - `reduced_chemical_potential`: unitless
    - `coverage`: arbitrary consistent units

Notes: The checker uses structural audit and threshold logic: for hydrogen, it locates the μ* range where coverage jumps by >80% and checks it falls within paper‑reported intervals; for neon, it classifies wetting by whether the coverage at the highest pressure exceeds or stays below hidden fractional thresholds. All values of potential parameters and conditions needed for simulation are provided in the action descriptions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "neon_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "well_depth_D_K",
          "pressure",
          "coverage"
        ],
        "units": {
          "temperature_K": "K",
          "well_depth_D_K": "K",
          "pressure": "arbitrary units",
          "coverage": "arbitrary consistent units"
        }
      },
      "description": "Ne adsorption isotherms; the checker classifies wetting/non‑wetting from coverage at the highest pressure for each condition, without requiring absolute units."
    },
    {
      "file": "hydrogen_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "reduced_chemical_potential",
          "coverage"
        ],
        "units": {
          "temperature_K": "K",
          "reduced_chemical_potential": "unitless",
          "coverage": "arbitrary consistent units"
        }
      },
      "description": "H₂ adsorption isotherms; the checker identifies the μ* interval of the abrupt coverage jump (incomplete wetting) and verifies continuous monotonic growth at 30 K (complete wetting)."
    }
  ],
  "notes": "The checker uses structural audit and threshold logic: for hydrogen, it locates the μ* range where coverage jumps by >80% and checks it falls within paper‑reported intervals; for neon, it classifies wetting by whether the coverage at the highest pressure exceeds or stays below hidden fractional thresholds. All values of potential parameters and conditions needed for simulation are provided in the action descriptions."
}
```

## How you are scored
A hidden verifier reads your two CSV files and applies a structural audit. For hydrogen, the verifier examines the coverage as a function of μ* at each temperature: at low temperatures it checks whether the coverage exhibits an abrupt jump within a specific μ* interval (indicating incomplete wetting), while at 30 K it checks for continuous, monotonic growth (complete wetting). For neon, the verifier classifies each (T, D) condition as wetting or non‑wetting based on the coverage level at the highest pressure, relative to a hidden reference threshold. The exact numeric intervals and thresholds are not disclosed. Your reward is computed by weighting the correct classification for each condition across both stages. Producing isotherms whose shape correctly captures the expected wetting behaviour is what earns credit; simply reporting numbers without genuine simulation does not.
