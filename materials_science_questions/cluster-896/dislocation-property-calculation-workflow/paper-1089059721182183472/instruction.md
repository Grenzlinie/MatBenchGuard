# Reproduce Theoretical Strain Field around a Dislocation using Barnett's Solution and Compare with BCDI Measurements

## Problem background
Hydrogen embrittlement in structural alloys, particularly austenitic stainless steels, poses a significant challenge for the durability of hydrogen production and transport infrastructure. One proposed mechanism, hydrogen-enhanced localized plasticity (HELP), suggests that hydrogen atoms accumulate near dislocation cores, reducing their elastic stress fields—a phenomenon known as hydrogen elastic shielding—and thereby facilitating dislocation motion. However, directly measuring such subtle hydrogen-induced changes in the strain field around a single dislocation in a bulk material has been experimentally difficult. This task aims to quantify the elastic shielding effect by comparing experimental strain measurements, obtained via in situ Bragg coherent X-ray diffraction imaging (BCDI) on a 316 stainless steel grain during hydrogen charging, with a hydrogen-free theoretical model of the dislocation strain field.

## Approach
The approach computes a theoretical, hydrogen-free strain field for a dislocation using the elastic Barnett solution for triangular dislocation loops and compares it with experimental BCDI strain maps. Starting from the known dislocation geometry (node positions, Burgers vector b = a0/2[110], Poisson's ratio ν=0.28, lattice parameter a0), the elastic strain tensor is calculated and projected onto the [111] direction to obtain a model strain field ε111,model. Angular line profiles are extracted at a fixed radius of 30 nm from the dislocation core, for both the theoretical model and for the experimental ε111 volumes at the initial (pre-charge) and final (post-charge) hydrogen charging states. The maximum and minimum strain values around these profiles are then computed to quantify any change in the experimental strain field that may be attributed to hydrogen elastic shielding.

## Reproduction target
Using the BCDI reconstruction dataset (Zenodo 10.5281/zenodo.14503567), compute the hydrogen-free theoretical ε111 strain field around the large dislocation via the Barnett solution. From this model and the provided experimental strain maps, extract circular line profiles at a 30 nm radius from the dislocation core at the initial (pre-charge) and final (post-charge) time points. Determine the maximum and minimum ε111 values from these profiles. The aim is to reproduce the theoretical strain pattern and to quantify the difference between the experimental strain at the two hydrogen states, thereby providing a measure of hydrogen elastic shielding.

## Assets

- BCDI reconstruction dataset: 10.5281/zenodo.14503567

## Workflow steps

### Step 1: Compute hydrogen-free theoretical strain field
- Role: process
- Action: Using the dislocation node positions for the large dislocation, the known Burgers vector b = a0/2[110], Poisson's ratio nu=0.28, and lattice parameter a0, compute the elastic strain field tensor via the Barnett solution for a triangular dislocation loop. Project the tensor onto the [111] direction to obtain epsilon_111,model. Save the resulting 3D array as theoretical_eps111.npy.
- Evidence: `/app/outputs/theoretical_eps111.npy`

### Step 2: Extract radial strain profiles
- Role: scored (load-bearing)
- Action: For each time point (at least the initial pre-charge and the final post-charge time), identify the dislocation core position in the experimental epsilon_111 volume and in the theoretical epsilon_111,model. Draw a circular line profile at a radius of 30 nm, sampling angles from 0 to 2π (radians) measured from the Burgers vector direction. Compile the experimental and theoretical strain values into strain_profiles.csv.
- Output file: `/app/outputs/strain_profiles.csv`
- Format: csv
- Contract: Columns: time (float, hours relative to start of charging), angle (float, radians from Burgers vector direction), theoretical_eps111 (float, strain), experimental_eps111 (float, strain). One row per angle (from 0 to 2π) at a fixed radius of 30 nm for each time point.
- Scoring: scored by hidden verifier

### Step 3: Compute max and min strain values
- Role: scored
- Action: From the line profiles in strain_profiles.csv, identify the angular positions of the maximum and minimum strain values. Average the strain over a ±π/8 window around each extremum to obtain robust max and min values for both theoretical and experimental strains at each time point. Output the results to max_min_values.csv.
- Output file: `/app/outputs/max_min_values.csv`
- Format: csv
- Contract: Columns: time (float, hours), max_theoretical (float), min_theoretical (float), max_experimental (float), min_experimental (float). The max and min are the averaged values over a π/4 range around the peak and trough respectively.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strain_profiles.csv`
- `/app/outputs/max_min_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strain_profiles.csv
- path: `/app/outputs/strain_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Circular line profile at 30 nm radius around the dislocation core, giving angular strain data from both the theoretical model and the experimental reconstruction.
- schema:
  - `type`: table
  - `required_columns`: `time`, `angle`, `theoretical_eps111`, `experimental_eps111`
  - `units`:
    - `time`: hours
    - `angle`: radians
    - `theoretical_eps111`: strain
    - `experimental_eps111`: strain

### max_min_values.csv
- path: `/app/outputs/max_min_values.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Averaged maximum and minimum strain values from the radial profiles, used to quantify the strain reduction due to hydrogen elastic shielding.
- schema:
  - `type`: table
  - `required_columns`: `time`, `max_theoretical`, `min_theoretical`, `max_experimental`, `min_experimental`
  - `units`:
    - `time`: hours
    - `max_theoretical`: strain
    - `min_theoretical`: strain
    - `max_experimental`: strain
    - `min_experimental`: strain

Notes: The checker will independently recompute the theoretical strain field using the Barnett solution and the same dislocation geometry/elastic constants. It will then extract the radial profiles and max/min values and compare them to the submitted artifacts. The scored target is the quantitative evidence of hydrogen elastic shielding (strain reduction).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strain_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "angle",
          "theoretical_eps111",
          "experimental_eps111"
        ],
        "units": {
          "time": "hours",
          "angle": "radians",
          "theoretical_eps111": "strain",
          "experimental_eps111": "strain"
        }
      },
      "description": "Circular line profile at 30 nm radius around the dislocation core, giving angular strain data from both the theoretical model and the experimental reconstruction."
    },
    {
      "file": "max_min_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "max_theoretical",
          "min_theoretical",
          "max_experimental",
          "min_experimental"
        ],
        "units": {
          "time": "hours",
          "max_theoretical": "strain",
          "min_theoretical": "strain",
          "max_experimental": "strain",
          "min_experimental": "strain"
        }
      },
      "description": "Averaged maximum and minimum strain values from the radial profiles, used to quantify the strain reduction due to hydrogen elastic shielding."
    }
  ],
  "notes": "The checker will independently recompute the theoretical strain field using the Barnett solution and the same dislocation geometry/elastic constants. It will then extract the radial profiles and max/min values and compare them to the submitted artifacts. The scored target is the quantitative evidence of hydrogen elastic shielding (strain reduction)."
}
```

## How you are scored
A hidden verifier independently recomputes the theoretical strain field, extracts the same radial profiles, and computes the maximum and minimum strain values. It compares your submitted artifacts to its independently generated references. For the theoretical strain profile, the agreement is evaluated pointwise. For the max/min values, the verifier checks whether the change in experimental strain between the initial and final charging states is consistent with the paper's reported hydrogen elastic shielding. Each scored artifact contributes a weighted fraction to the final reward. Reporting final values alone is insufficient; the verifier recomputes intermediate quantities from your raw outputs and the provided public inputs. The exact tolerances and weighting are determined by the verifier and are not disclosed.
