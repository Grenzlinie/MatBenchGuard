# Arsenic vacancy migration barrier in zincblende GaAs via first-principles nudged elastic band calculations

## Problem background
GaAs nanowires are used in a range of optoelectronic and electronic nanodevices. Point defects such as arsenic vacancies (V_As) introduced during growth strongly influence the material's electronic properties and diffusion characteristics. Understanding the migration of As vacancies in the zincblende (ZB) polytype of GaAs is important for designing post-growth annealing treatments and for predicting device performance. This task focuses on computing the energy barriers that govern V_As diffusion in ZB GaAs.

## Approach
The migration barriers are computed using first-principles density functional theory (DFT) within the generalized gradient approximation (GGA) and the projector augmented-wave (PAW) method. The host crystal is modeled with a 216-atom supercell of zincblende GaAs containing a single As vacancy. The minimum energy path for an As atom hopping into the vacancy is sampled via the nudged elastic band (NEB) method. To capture the effect of doping, both the positively charged (V_As^+) and negatively charged (V_As^-) vacancy states are considered. All calculations are performed using the open-source Quantum ESPRESSO package, replacing the proprietary VASP code employed in the original study. The workflow involves: (i) optimizing the bulk GaAs lattice constant, (ii) constructing the supercell and generating initial/final vacancy configurations, (iii) relaxing the endpoint structures, and (iv) running NEB to obtain the energy profile. The migration barrier for each charge state is then extracted as the maximum energy difference between the initial minimum and any point along the path.

## Reproduction target
The objective is to produce two files: (i) a CSV file with the raw NEB energy profile for V_As^+ and V_As^- (neb_profiles.csv), and (ii) a JSON file containing the extracted migration barriers (migration_barriers.json). The NEB profile must include at least 7 images between the endpoints for each charge state and record the total energy of each image. The migration barrier for each charge state is defined as the difference between the highest energy along the path and the energy of the initial minimum. The task is considered successful if the computed barriers are physically reasonable and the NEB profile exhibits the expected structural features (e.g., two saddle points and an intermediate minimum).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ga PAW pseudopotential: PSlibrary or SSSP
- As PAW pseudopotential: PSlibrary or SSSP

## Workflow steps

### Step 1: Bulk structure optimization
- Role: process
- Action: Optimize the lattice constant of zincblende GaAs using plane-wave DFT (e.g., Quantum ESPRESSO pw.x) with the chosen pseudopotentials to obtain the equilibrium lattice constant a0.
- Evidence: `/app/outputs/bulk_energy_vs_volume.csv`

### Step 2: Supercell construction and V_As structures
- Role: process
- Action: Create a 216-atom supercell (3x3x3) of ZB GaAs using the optimized lattice constant. Generate initial and final configurations: a perfect supercell with an As vacancy at a chosen site, and the same supercell after a neighboring As atom hops into the vacancy. Prepare input files for DFT relaxations of each charge state.
- Evidence: `/app/outputs/supercell_structures.txt`

### Step 3: Relax initial and final V_As configurations
- Role: process
- Action: Perform DFT relaxation (pw.x) of the V_As structures in charge states +1 and -1 with a homogeneous background charge. Save the relaxed atomic coordinates for the initial and final states of each charge state.
- Evidence: `/app/outputs/relaxed_structures.log`

### Step 4: NEB energy profile calculation
- Role: scored (load-bearing)
- Action: Using the relaxed initial and final configurations for V_As^+ and V_As^-, run nudged elastic band calculations (e.g., QE's neb.x or a custom NEB script) with at least 7 images between the endpoints. Record the total energy of each image (including endpoints) along the minimum energy path in a CSV file.
- Output file: `/app/outputs/neb_profiles.csv`
- Format: csv
- Contract: CSV: charge_state (str, 'V_As^+' or 'V_As^-'), image_index (int, 0-based), energy (float, eV)
- Scoring: scored by hidden verifier

### Step 5: Migration barrier extraction
- Role: scored
- Action: From the NEB energy profile, determine the overall migration barrier for each charge state as the maximum energy difference between the initial minimum and any point along the path. Output the barriers in a JSON file.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: JSON: {'V_As_plus_barrier': float, 'V_As_minus_barrier': float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/neb_profiles.csv`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### neb_profiles.csv
- path: `/app/outputs/neb_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw NEB energy profile: for each charge state (V_As^+, V_As^-), each image along the path has an energy in eV.
- schema:
  - `type`: table
  - `required_columns`: `charge_state`, `image_index`, `energy`
  - `units`:
    - `energy`: eV

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The extracted migration barriers for the two charge states.
- schema:
  - `type`: object
  - `required`:
    - `V_As_plus_barrier`: number
    - `V_As_minus_barrier`: number
  - `units`:
    - `V_As_plus_barrier`: eV
    - `V_As_minus_barrier`: eV

Notes: The checker will recompute barriers from neb_profiles.csv and compare them to the hidden gold values with tolerance. The migration_barriers.json is also verified for consistency with the CSV-derived barriers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "neb_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "charge_state",
          "image_index",
          "energy"
        ],
        "units": {
          "energy": "eV"
        }
      },
      "description": "Raw NEB energy profile: for each charge state (V_As^+, V_As^-), each image along the path has an energy in eV."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "V_As_plus_barrier": "number",
          "V_As_minus_barrier": "number"
        },
        "units": {
          "V_As_plus_barrier": "eV",
          "V_As_minus_barrier": "eV"
        }
      },
      "description": "The extracted migration barriers for the two charge states."
    }
  ],
  "notes": "The checker will recompute barriers from neb_profiles.csv and compare them to the hidden gold values with tolerance. The migration_barriers.json is also verified for consistency with the CSV-derived barriers."
}
```

## How you are scored
The hidden verifier reads the two scored output files and independently evaluates them. For neb_profiles.csv, the checker recomputes the migration barriers for each charge state and compares them to reference values using appropriate tolerances; it also verifies that the NEB path contains at least seven images, two saddle points, and an intermediate shallow minimum. For migration_barriers.json, the checker compares the reported barriers to the values it derived from the CSV to ensure consistency, and then compares them to hidden reference barriers. The two stages are weighted; the raw NEB profile carries the highest weight. The final reward is a weighted combination of the scores from each stage. A submission that merely reports plausible numbers without a consistent raw NEB profile will not earn full credit.
