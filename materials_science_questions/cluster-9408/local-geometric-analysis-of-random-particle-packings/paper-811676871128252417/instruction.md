# Discrete Mechanical Compaction and Properties of Random Sphere Packings

## Problem background
Understanding the properties of granular materials is crucial for applications ranging from powder processing to soil mechanics. A discrete mechanical model can simulate the compaction of a collection of spheres, producing a random three-dimensional packing. The goal is to generate such a packing computationally and to quantify its structural and transport characteristics—including coordination number, local density distribution, percolation behavior, and effective electrical/thermal conductivity—so that these quantities can be compared with experimental observations. The task is to reconstruct the simulation pipeline that yields these properties for a computer-generated packing.

## Approach
The reproduction follows a two-stage computational approach. First, an initial isotropic random packing of equal spheres is created using a growth-and-displacement algorithm that expands spheres and resolves overlaps, yielding a loose packing around a target density. Second, a discrete mechanical model is applied to compact this initial packing hydrostatically. In this model, each particle obeys force equilibrium; contacts follow a normal stiffness that stiffens dramatically when spheres overlap (Hertzian-like) while a soft stabilizing force is applied to nearby non-contacting spheres. The simulation is integrated incrementally under hydrostatic velocity boundary conditions and frictionless planar walls on three faces, recording the evolution of relative density, bulk modulus, coordination number, and maximum interpenetration. Once the final dense packing is obtained, several analyses are performed: a Voronoi tessellation yields local relative densities; site percolation simulations on the contact network determine the percolation threshold; and discrete transport (flux-balance) calculations for mixtures of high- and low-conductivity spheres give the effective conductivity as a function of conducting fraction. The conductivity data are finally fit to percolation power-law forms to extract scaling exponents. All stages are implemented from scratch using Python and standard scientific libraries.

## Reproduction target
Produce the final packing and its key properties through the simulation pipeline, and output the following scored artifacts: (1) the final sphere coordinates, radii, and contact list; (2) the time-series of relative density, bulk modulus, coordination number, and maximum interpenetration during compaction; (3) the Voronoi local density for each particle; (4) the site percolation threshold of the packing; (5) the normalized effective conductivity at a range of conducting site fractions; and (6) the fitted conductivity exponents and percolation threshold. All results are derived from the computer-generated packing and are checked against reference values by an automated verifier.

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Initial random packing generation
- Role: process
- Action: Generate an isotropic initial random packing of 2000 equal spheres in a cubic box using the Bernal/Mason/Finney algorithm (incremental sphere growth and overlap displacement) until a packing density of approximately 0.58 is reached. Save the resulting particle positions and radii to initial_packing.json.
- Evidence: `/app/outputs/initial_packing.json`

### Step 2: Discrete mechanical compaction simulation
- Role: process
- Action: Starting from the initial packing, run the discrete mechanical model that enforces nodewise force equilibrium, uses Hertzian-like stiffening for overlaps (normal modulus piecewise: 1.0 when L>2R, 1e15*sqrt(1-L/(2R)) when L≤2R), soft stabilizing contacts (modulus 1.0) for spheres within 1.1R, and tangential modulus 1.0. Apply frictionless walls at x=0,y=0,z=0 and hydrostatic velocity boundary conditions. Integrate incrementally with time steps chosen so maximum interpenetration < 0.001R. Record the evolution of relative density, bulk modulus, coordination number, and maximum interpenetration; output the time-series as mechanics.csv and retain the final particle coordinates and contacts for the next step.
- Evidence: `/app/outputs/mechanics.csv`

### Step 3: Final packing state (scored)
- Role: scored (load-bearing)
- Action: From the simulation, write the final compacted packing: sphere center coordinates, radii, and contact list (particle index pairs i,j) to packing_state.json.
- Output file: `/app/outputs/packing_state.json`
- Format: json
- Contract: JSON object with keys 'particles' (array of objects {id: int, x: float, y: float, z: float, radius: float}) and 'contacts' (array of objects {i: int, j: int}).
- Scoring: scored by hidden verifier

### Step 4: Mechanical properties during compaction (scored)
- Role: scored
- Action: From the time-series recorded during compaction, extract and write the data to mechanical_props.csv with columns: relative_density, bulk_modulus, coordination_number, max_interpenetration. Include at least 10 rows spanning the density range from initial to final packing.
- Output file: `/app/outputs/mechanical_props.csv`
- Format: csv
- Contract: CSV with columns relative_density (float, dimensionless), bulk_modulus (float), coordination_number (float), max_interpenetration (float, in units of particle radius).
- Scoring: scored by hidden verifier

### Step 5: Voronoi local densities (scored)
- Role: scored
- Action: Using the particle centers and box size, compute the Voronoi tessellation of the final packing. For each particle calculate its local relative density (ratio of particle volume to Voronoi cell volume). Write one density per line to voronoi_densities.csv.
- Output file: `/app/outputs/voronoi_densities.csv`
- Format: csv
- Contract: CSV with a single column 'local_density' (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 6: Site percolation threshold (scored)
- Role: scored
- Action: From the contact graph in packing_state.json, simulate site percolation: randomly label spheres as A or B with varying site fractions of A, check for a spanning A–A cluster across the packing. Use finite‑size scaling (as applicable) to determine the critical site fraction (percolation threshold). Write the threshold value to percolation_threshold.txt.
- Output file: `/app/outputs/percolation_threshold.txt`
- Format: txt
- Contract: A single decimal number (float), in plain text.
- Scoring: scored by hidden verifier

### Step 7: Effective conductivity simulation (scored)
- Role: scored
- Action: Using the contact network from packing_state.json, assign conductivities: high-conductivity spheres (conductance 1e12 * c_low), low-conductivity spheres (c_low = 1), and series conductance for mixed contacts. For at least 20 values of the conducting site fraction vf between 0 and 1, solve the discrete flux-balance equations with a potential gradient across two opposing faces and insulating conditions on others. Compute the normalized effective conductivity C_eff for each vf. Write the results to conductivity_data.csv.
- Output file: `/app/outputs/conductivity_data.csv`
- Format: csv
- Contract: CSV with columns 'vf' (float, dimensionless, site fraction of conducting spheres) and 'C_eff' (float, normalized effective conductivity, dimensionless). At least 20 rows.
- Scoring: scored by hidden verifier

### Step 8: Conductivity scaling fit (scored)
- Role: scored
- Action: Fit the conductivity data from step_07 to the percolation power-law forms C/C0 = [vc/(vc - vf)]^n_l for vf < vc and C/C1 = [(vf - vc)/(1 - vc)]^n_u for vf > vc, using the percolation threshold from step_06 as vc. Output a JSON file with the fitted exponents n_l, n_u and the threshold vc used.
- Output file: `/app/outputs/conductivity_fit.json`
- Format: json
- Contract: JSON object with keys 'n_l' (float), 'n_u' (float), and 'v_c' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/packing_state.json`
- `/app/outputs/mechanical_props.csv`
- `/app/outputs/voronoi_densities.csv`
- `/app/outputs/percolation_threshold.txt`
- `/app/outputs/conductivity_data.csv`
- `/app/outputs/conductivity_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### packing_state.json
- path: `/app/outputs/packing_state.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final packing particle coordinates, radii, and contact list. The hidden checker recomputes coordination number distribution statistics from this artifact.
- schema:
  - `type`: object
  - `required`:
    - `particles`: array of {id: int, x: float, y: float, z: float, radius: float}
    - `contacts`: array of {i: int, j: int}

### mechanical_props.csv
- path: `/app/outputs/mechanical_props.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Compaction evolution: bulk modulus, coordination number, and maximum interpenetration as functions of relative density. The hidden checker compares reported values at selected densities with paper reference values.
- schema:
  - `type`: table
  - `required_columns`: `relative_density`, `bulk_modulus`, `coordination_number`, `max_interpenetration`
  - `units`:
    - `relative_density`: dimensionless
    - `bulk_modulus`: arbitrary units consistent with simulation
    - `coordination_number`: dimensionless
    - `max_interpenetration`: units of particle radius

### voronoi_densities.csv
- path: `/app/outputs/voronoi_densities.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Local relative density for each particle from Voronoi tessellation. The checker recomputes mean and standard deviation of the distribution from these values.
- schema:
  - `type`: table
  - `required_columns`: `local_density`
  - `units`:
    - `local_density`: dimensionless

### percolation_threshold.txt
- path: `/app/outputs/percolation_threshold.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Single number: the site percolation threshold (critical site fraction). Checker compares it to a hidden reference value within a tolerance.
- schema:
  - `type`: text

### conductivity_data.csv
- path: `/app/outputs/conductivity_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Effective conductivity vs. conducting site fraction. The checker verifies shape, sufficient data points, and uses them for internal consistency checks (refitting exponents).
- schema:
  - `type`: table
  - `required_columns`: `vf`, `C_eff`
  - `units`:
    - `vf`: dimensionless
    - `C_eff`: dimensionless (normalized effective conductivity)

### conductivity_fit.json
- path: `/app/outputs/conductivity_fit.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted percolation scaling exponents and the percolation threshold used. The checker compares n_l and n_u against hidden reference values.
- schema:
  - `type`: object
  - `required`:
    - `n_l`: float
    - `n_u`: float
    - `v_c`: float

Notes: The hidden checker recomputes key statistics from the raw packing state and Voronoi densities, compares mechanical properties and percolation threshold against hidden reference values, and refits conductivity exponents for internal consistency. All tolerances are chosen to accommodate legitimate run-to-run variation due to random seed, discretisation, and implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "packing_state.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "particles": "array of {id: int, x: float, y: float, z: float, radius: float}",
          "contacts": "array of {i: int, j: int}"
        }
      },
      "description": "Final packing particle coordinates, radii, and contact list. The hidden checker recomputes coordination number distribution statistics from this artifact."
    },
    {
      "file": "mechanical_props.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "relative_density",
          "bulk_modulus",
          "coordination_number",
          "max_interpenetration"
        ],
        "units": {
          "relative_density": "dimensionless",
          "bulk_modulus": "arbitrary units consistent with simulation",
          "coordination_number": "dimensionless",
          "max_interpenetration": "units of particle radius"
        }
      },
      "description": "Compaction evolution: bulk modulus, coordination number, and maximum interpenetration as functions of relative density. The hidden checker compares reported values at selected densities with paper reference values."
    },
    {
      "file": "voronoi_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "local_density"
        ],
        "units": {
          "local_density": "dimensionless"
        }
      },
      "description": "Local relative density for each particle from Voronoi tessellation. The checker recomputes mean and standard deviation of the distribution from these values."
    },
    {
      "file": "percolation_threshold.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text"
      },
      "description": "Single number: the site percolation threshold (critical site fraction). Checker compares it to a hidden reference value within a tolerance."
    },
    {
      "file": "conductivity_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "vf",
          "C_eff"
        ],
        "units": {
          "vf": "dimensionless",
          "C_eff": "dimensionless (normalized effective conductivity)"
        }
      },
      "description": "Effective conductivity vs. conducting site fraction. The checker verifies shape, sufficient data points, and uses them for internal consistency checks (refitting exponents)."
    },
    {
      "file": "conductivity_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "n_l": "float",
          "n_u": "float",
          "v_c": "float"
        }
      },
      "description": "Fitted percolation scaling exponents and the percolation threshold used. The checker compares n_l and n_u against hidden reference values."
    }
  ],
  "notes": "The hidden checker recomputes key statistics from the raw packing state and Voronoi densities, compares mechanical properties and percolation threshold against hidden reference values, and refits conductivity exponents for internal consistency. All tolerances are chosen to accommodate legitimate run-to-run variation due to random seed, discretisation, and implementation differences."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each required output file. For packing-based statistics, the verifier may recompute quantities such as coordination number distributions and local density moments from your raw data. For mechanical properties and conductivity exponents, the verifier compares your reported values with reference targets using tolerances that account for legitimate run-to-run variability (stemming from random seeds, discretization, and implementation details). The conductivity data may be refitted to check internal consistency. Each stage is weighted to form a total score between 0 and 1; simply printing a number without generating the underlying artifacts will not pass.
