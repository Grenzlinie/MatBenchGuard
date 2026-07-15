# Hard-Sphere Tilt Boundary Densification Analysis

## Problem background
Grain boundary structure and energy strongly influence the mechanical, chemical, and transport properties of polycrystalline materials. In this work, the focus is on symmetric coincidence tilt boundaries in hard-sphere f.c.c. crystals. The boundary is modelled as an interface between two identical half-crystals in an f.c.c. lattice of hard spheres (unit sphere diameter, no overlap allowed), constructed via the coincidence site lattice (CSL) geometry. By systematically translating the half-crystals relative to each other, one can find mechanically stable configurations that maximise density without atom overlap. A key physical question is whether a relative translation along the tilt axis (Z-translation) can produce a denser configuration and alter the sizes of voids (holes) in the boundary plane. The quantitative characterisation of such boundaries involves computing the excess volume (a normalised measure of the extra volume associated with the boundary compared to a perfect crystal) and the diameters of the largest interstitial and substitutional spheres that can be placed at the boundary. The present task examines a single, well-defined example — the [100] Σ5 tilt boundary — and computes these properties for configurations without and with Z-translation, providing insight into the general effect of tilt-axis translations on boundary densification.

## Approach
The computational approach consists of three stages:

1. **Boundary construction and geometry optimisation.** Build a bicrystal of the [100] Σ5 symmetric tilt boundary using the CSL construction for an f.c.c. hard-sphere lattice. Translate the two half-crystals parallel and perpendicular to the tilt axis to find the mechanically stable (overlap-free) configuration that maximises the density, first without any relative translation along the tilt axis (ΔZ=0) and then with a prescribed Z-translation of ΔZ=0.326. The atom coordinates for both configurations are saved as reference for subsequent analysis.

2. **Excess volume and interstitial hole size.** For each configuration, construct a parallelepiped spanning one boundary period (its faces are defined by the boundary period vectors and the atom positions inside the two half-crystals). From the parallelepiped volume V and the number of spheres N it contains, compute the excess volume per atomic area using the standard normalisation: atomic volume Ω = 0.70711 (unit sphere diameter), V* = (V − N Ω)/Ω, normalised boundary area A* = A/Ω^{2/3}, and excess volume V_EX = V*/A*. Independently, find the largest sphere that can be placed in the interstices of the boundary (the maximum interstitial diameter) by numerically searching for the biggest sphere that fits without overlapping any atom centres. Both quantities are reported in units of the atom diameter.

3. **Substitutional hole size (for the denser, Z-translated configuration).** For the configuration with ΔZ=0.326, sequentially remove each atom and determine the largest sphere that can fit into the resulting vacancy. The maximum such diameter across all atom removals is recorded as the maximum substitutional hole diameter.

The key comparison is between the no-Z and with-Z configurations: a significant change in excess volume and interstitial diameter would indicate densification due to the tilt-axis translation. The substitutional hole size further characterises the packing stability of the denser configuration.

## Reproduction target
Compute and report the following quantities for the [100] Σ5 symmetric tilt grain boundary in hard-sphere f.c.c.:

- **Without Z-translation (ΔZ=0):** excess volume V_EX and maximum interstitial sphere diameter (units of atom diameter).
- **With Z-translation (ΔZ=0.326):** excess volume V_EX and maximum interstitial sphere diameter (units of atom diameter).
- **Maximum substitutional hole diameter** for the configuration with Z-translation (units of atom diameter).

All results must be saved in the specified CSV files under `/app/outputs` (see workflow steps and output contract). The computed values should follow the definitions given in the approach section: excess volume via the normalised V*/A* formula with Ω=0.70711, and hole diameters from numerical sphere packing without atom overlap.

## Assets

- Python scientific computing environment

## Workflow steps

### Step 1: Boundary model construction
- Role: process
- Action: Construct the [100] Σ5 symmetric tilt grain boundary bicrystal from hard spheres in f.c.c. lattice using coincidence site lattice (CSL) geometry. Find mechanically stable configurations that maximize density without atom overlap: first without relative translation along tilt axis (ΔZ=0), then with a translation ΔZ=0.326 along tilt axis. Save atom coordinates for both configurations to separate files.
- Evidence: `/app/outputs/atom_coords_noZ.csv`

### Step 2: No-Z excess volume and maximum interstitial diameter
- Role: scored
- Action: From the no-Z configuration (step1 output), compute the excess volume using the paper's definition: atomic volume Ω=0.70711 for unit sphere diameter, construct a parallelepiped spanning one boundary period with volume V and containing N spheres, boundary period area A. Compute V* = (V − NΩ)/Ω, A* = A/Ω^{2/3}, and excess volume V_EX = V*/A*. Compute the largest interstitial sphere diameter (units of atom diameter) by numerical sphere packing. Write results to a CSV.
- Output file: `/app/outputs/step_01_noZ_results.csv`
- Format: csv
- Contract: CSV with columns: condition, excess_volume, max_interstitial_diameter. One row with condition='no_Z'.
- Scoring: scored by hidden verifier

### Step 3: With-Z excess volume and maximum interstitial diameter
- Role: scored
- Action: From the with-Z configuration (step1 output), compute the excess volume and maximum interstitial diameter using the same definitions as step2. Write results to a CSV.
- Output file: `/app/outputs/step_02_withZ_results.csv`
- Format: csv
- Contract: CSV with columns: condition, excess_volume, max_interstitial_diameter. One row with condition='with_Z'.
- Scoring: scored by hidden verifier

### Step 4: With-Z maximum substitutional hole diameter
- Role: scored (load-bearing)
- Action: From the with-Z configuration, sequentially remove each atom and find the largest sphere that fits into the resulting hole. Report the maximum such diameter (units of atom diameter). Write to a CSV.
- Output file: `/app/outputs/step_03_substitutional.csv`
- Format: csv
- Contract: CSV with columns: condition, max_substitutional_diameter. One row with condition='with_Z'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_noZ_results.csv`
- `/app/outputs/step_02_withZ_results.csv`
- `/app/outputs/step_03_substitutional.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_noZ_results.csv
- path: `/app/outputs/step_01_noZ_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Excess volume and maximum interstitial diameter for the configuration without Z-translation.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `excess_volume`, `max_interstitial_diameter`
  - `units`:
    - `condition`: string (exact: no_Z)
    - `excess_volume`: normalized excess volume V_EX (unitless)
    - `max_interstitial_diameter`: units of atom diameter

### step_02_withZ_results.csv
- path: `/app/outputs/step_02_withZ_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Excess volume and maximum interstitial diameter for the configuration with Z-translation.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `excess_volume`, `max_interstitial_diameter`
  - `units`:
    - `condition`: string (exact: with_Z)
    - `excess_volume`: normalized excess volume V_EX (unitless)
    - `max_interstitial_diameter`: units of atom diameter

### step_03_substitutional.csv
- path: `/app/outputs/step_03_substitutional.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum substitutional hole diameter for the densest configuration. The acceptance threshold is ≤1.0 atom diameters.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `max_substitutional_diameter`
  - `units`:
    - `condition`: string (exact: with_Z)
    - `max_substitutional_diameter`: units of atom diameter

Notes: All outputs are deterministic given the reconstruction procedure. The checker compares reported values against hidden gold from the paper's reported numbers with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_noZ_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "excess_volume",
          "max_interstitial_diameter"
        ],
        "units": {
          "condition": "string (exact: no_Z)",
          "excess_volume": "normalized excess volume V_EX (unitless)",
          "max_interstitial_diameter": "units of atom diameter"
        }
      },
      "description": "Excess volume and maximum interstitial diameter for the configuration without Z-translation."
    },
    {
      "file": "step_02_withZ_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "excess_volume",
          "max_interstitial_diameter"
        ],
        "units": {
          "condition": "string (exact: with_Z)",
          "excess_volume": "normalized excess volume V_EX (unitless)",
          "max_interstitial_diameter": "units of atom diameter"
        }
      },
      "description": "Excess volume and maximum interstitial diameter for the configuration with Z-translation."
    },
    {
      "file": "step_03_substitutional.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "max_substitutional_diameter"
        ],
        "units": {
          "condition": "string (exact: with_Z)",
          "max_substitutional_diameter": "units of atom diameter"
        }
      },
      "description": "Maximum substitutional hole diameter for the densest configuration. The acceptance threshold is ≤1.0 atom diameters."
    }
  ],
  "notes": "All outputs are deterministic given the reconstruction procedure. The checker compares reported values against hidden gold from the paper's reported numbers with appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares each of the three scored output files (`step_01_noZ_results.csv`, `step_02_withZ_results.csv`, `step_03_substitutional.csv`) to reference values derived from the published analysis. The verifier checks that the correct columns and conditions are present and that the reported numeric values lie within acceptable tolerances. Each scored step contributes to the final reward; the exact weighting is predetermined and uniform across all submissions. Simply producing files with the right structure is not sufficient — the reported quantities must be produced by the specified computation and must match the hidden reference. The verifier runs automatically and returns a single reward score between 0 and 1, where a higher score indicates a more accurate reproduction.
