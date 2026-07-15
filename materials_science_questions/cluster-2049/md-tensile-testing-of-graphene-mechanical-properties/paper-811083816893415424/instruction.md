# First-principles investigation of one-dimensional boron allotropes: mechanical and electronic properties

## Problem background
Recent advances in the synthesis of one-dimensional carbon chains (carbyne) and boron-based nanostructures have opened the door to exploring analogous one-dimensional allotropes of boron. The goal of this work is to investigate, from first principles, whether stable one-dimensional boron phases exist, and if so, what their structural, mechanical, and electronic properties are. Using density functional theory, we aim to identify candidate low-energy structures, compute their energy as a function of unit-cell length (the energy–strain relation), and extract key quantities: the cohesive energy difference between distinct phases, their tensile stiffnesses (the curvature of the energy minima), the equilibrium tension at which phase coexistence occurs, and the electronic band gap of a potentially semiconducting phase.

## Approach
We consider two candidate one-dimensional boron structures: a two-atom-wide staggered-row ribbon (R) and a single-atom linear chain (C). The primary computational tool is plane-wave density functional theory (DFT) using the PBE exchange–correlation functional with projector-augmented wave (PAW) pseudopotentials. For improved band-gap accuracy, a hybrid functional (HSE06) is employed for the electronic structure of the C phase. The workflow consists of: (1) constructing and relaxing both structures to their equilibrium geometries; (2) performing a series of fixed-cell total-energy calculations to obtain the energy–strain curves; (3) analyzing these curves to identify the two energy minima, derive the cohesive energy difference and tensile stiffnesses via quadratic fits, and determine the equilibrium tension for phase coexistence using the common-tangent construction; and (4) computing the band structure of the C phase in its antiferromagnetic ground state to extract the fundamental band gap.

## Reproduction target
Using DFT with the specified tools and pseudopotential, compute and deliver: (i) the raw energy–strain data for both R and C phases as a CSV file; (ii) the derived mechanical properties—cohesive energy difference between the R and C minima, the tensile stiffness of each phase, and the equilibrium tension—as a JSON file; and (iii) the electronic band gap of the C phase (computed with HSE06) as a plain text file containing a single float value in eV.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Boron PBE PAW pseudopotential (SSSP precision v1.3): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Build and relax the R and C one-dimensional boron structures
- Role: process
- Action: Construct the unit cells of the two-atom-wide staggered-row ribbon (R) and the single-atom linear chain (C). Perform variable-cell DFT relaxation using PBE with at least 10 Å vacuum and force convergence below 0.01 eV/Å to obtain equilibrium geometries.
- Evidence: `/app/outputs/relaxed_structures.xyz`

### Step 2: Compute energy–strain curves for R and C phases
- Role: scored (load-bearing)
- Action: For each phase, perform a series of fixed-cell DFT total-energy calculations (PBE) at unit-cell lengths corresponding to strains from approximately -5% to +15%. Record the total energy per unit cell as a function of cell length.
- Output file: `/app/outputs/step01_energy_strain.csv`
- Format: csv
- Contract: columns: phase (string: R or C), length (float, Å, unit-cell length along the periodic direction), energy (float, eV, total DFT energy per unit cell)
- Scoring: scored by hidden verifier

### Step 3: Extract cohesive energy difference, tensile stiffness and equilibrium tension
- Role: scored
- Action: From the energy–strain data, locate the two minima, fit the curvature around each minimum to obtain tensile stiffnesses, compute the cohesive energy difference between the minima, and determine the equilibrium tension via the common tangent construction. Report these derived quantities.
- Output file: `/app/outputs/step02_derived_properties.json`
- Format: json
- Contract: object with keys: cohesive_energy_difference (float, eV), tensile_stiffness_R (float, eV/Å), tensile_stiffness_C (float, eV/Å), equilibrium_tension (float, nN)
- Scoring: scored by hidden verifier

### Step 4: Compute the electronic band gap of the antiferromagnetic C phase
- Role: scored
- Action: Using the optimized C-phase structure and a hybrid functional (HSE06), perform a self-consistent field calculation and a band-structure calculation along the Γ→X path. Identify the antiferromagnetic ground state (bond-SDW) and extract the fundamental band gap. Write the band gap value in eV.
- Output file: `/app/outputs/step03_band_gap_C.txt`
- Format: txt
- Contract: single float in eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step01_energy_strain.csv`
- `/app/outputs/step02_derived_properties.json`
- `/app/outputs/step03_band_gap_C.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step01_energy_strain.csv
- path: `/app/outputs/step01_energy_strain.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw energy–strain CSV for both phases. The checker recomputes tensile stiffnesses, cohesive energy difference, and equilibrium tension from these points.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `length`, `energy`
  - `units`:
    - `length`: Å
    - `energy`: eV

### step02_derived_properties.json
- path: `/app/outputs/step02_derived_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported mechanical properties. The checker compares these against independently computed reference values derived from step01 and the paper's hidden targets.
- schema:
  - `type`: object
  - `required`:
    - `cohesive_energy_difference`: float
    - `tensile_stiffness_R`: float
    - `tensile_stiffness_C`: float
    - `equilibrium_tension`: float
  - `units`:
    - `cohesive_energy_difference`: eV
    - `tensile_stiffness_R`: eV/Å
    - `tensile_stiffness_C`: eV/Å
    - `equilibrium_tension`: nN

### step03_band_gap_C.txt
- path: `/app/outputs/step03_band_gap_C.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Electronic band gap of the C phase. The checker compares this value to the hidden reference (HSE06 band gap) within tolerance.
- schema:
  - `type`: text
  - `required`: single float value in eV

Notes: All mechanical quantities derived from step01_energy_strain.csv must be consistent with the energy–strain data. The checker does not rely solely on the self-reported values in step02; it recomputes from step01 and cross-checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step01_energy_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "length",
          "energy"
        ],
        "units": {
          "length": "Å",
          "energy": "eV"
        }
      },
      "description": "Raw energy–strain CSV for both phases. The checker recomputes tensile stiffnesses, cohesive energy difference, and equilibrium tension from these points."
    },
    {
      "file": "step02_derived_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cohesive_energy_difference": "float",
          "tensile_stiffness_R": "float",
          "tensile_stiffness_C": "float",
          "equilibrium_tension": "float"
        },
        "units": {
          "cohesive_energy_difference": "eV",
          "tensile_stiffness_R": "eV/Å",
          "tensile_stiffness_C": "eV/Å",
          "equilibrium_tension": "nN"
        }
      },
      "description": "Agent-reported mechanical properties. The checker compares these against independently computed reference values derived from step01 and the paper's hidden targets."
    },
    {
      "file": "step03_band_gap_C.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": "single float value in eV"
      },
      "description": "Electronic band gap of the C phase. The checker compares this value to the hidden reference (HSE06 band gap) within tolerance."
    }
  ],
  "notes": "All mechanical quantities derived from step01_energy_strain.csv must be consistent with the energy–strain data. The checker does not rely solely on the self-reported values in step02; it recomputes from step01 and cross-checks."
}
```

## How you are scored
A hidden verifier will independently score the submitted artifacts. For the energy–strain CSV, the verifier recomputes the mechanical properties (tensile stiffnesses, cohesive energy difference, equilibrium tension) and compares them to hidden reference values within appropriate tolerances. The derived-properties JSON is also checked for consistency with the CSV. The band-gap text file is compared against a hidden reference band-gap value. Each stage contributes a weighted portion to a final reward score between 0 and 1. Reporting numbers from the literature is not sufficient; the verifier assesses the results of your own DFT calculations.
