# Canonical Monte Carlo Simulations of NaCl Electrolyte in Carbon Nanotubes: Radial Distribution Functions and Hydration Numbers

## Problem background
Confined aqueous NaCl solutions inside single-walled carbon nanotubes (CNTs) display hydrogen bonding and ion hydration structures that differ markedly from bulk electrolyte. Understanding how the CNT diameter alters intermolecular correlations and ion dehydration is important for applications such as nanofiltration, ion channels, and supercapacitors. This task uses canonical ensemble Monte Carlo (CEMC) simulations to compute radial distribution functions (RDFs) and hydration numbers for NaCl solutions in CNTs of three diameters and in bulk, providing quantitative structural information about confinement effects.

## Approach
Canonical ensemble Monte Carlo (CEMC) simulations are performed at 300 K for NaCl aqueous solution in single-walled CNTs of three diameters and in a bulk reference. The water molecules are described by the TIP5P five-site model, and Lennard-Jones plus Coulomb interactions are assigned to Na⁺, Cl⁻, and carbon atoms using published force-field parameters. Long-range electrostatics are handled with Ewald summation and Lorentz-Berthelot mixing rules. Simulation cells containing CNTs are embedded between graphene sheets to prevent external adsorption. After equilibration, trajectories are analyzed to compute RDFs for Na⁺–water, Cl⁻–water, and water–water pairs. From the RDFs, the first-peak positions (nearest-neighbor distances) are determined, and hydration numbers are obtained by integrating the ion–water RDFs up to the first minimum.

## Reproduction target
Run CEMC simulations for four systems: bulk electrolyte and NaCl solution confined in CNTs with diameters of 0.8 nm (referred to as 1nm_CNT), 1.7 nm (2nm_CNT), and 2.7 nm (3nm_CNT). Construct the systems according to the specifications given in the workflow steps, using the TIP5P water model and the force-field parameters listed. After equilibration, compute the radial distribution functions for water–water, Na⁺–water, and Cl⁻–water correlations. Extract the nearest-neighbor distances from the first peak of each RDF. Determine the hydration numbers of Na⁺ and Cl⁻ by integrating the respective ion–water RDFs up to the first minimum. Report all results in a single JSON file, `/app/outputs/results.json`, following the exact schema described in the output contract.

## Assets

- DL_MONTE Monte Carlo simulation package: https://github.com/dlmonte/dlmonte

## Workflow steps

### Step 1: System Preparation
- Role: process
- Action: Construct initial simulation cells for the four systems: (i) bulk electrolyte (5.0×5.0×5.0 nm, 38 Na+, 38 Cl-, 3800 water), (ii) 0.8 nm CNT, (iii) 1.7 nm CNT, (iv) 2.7 nm CNT. For CNT systems, embed a 6.1-nm-long single-walled CNT in a 10.0×5.66×5.54 nm box with graphene sheets, and place 30 Na+, 30 Cl-, 3000 water molecules randomly. Assign Lennard-Jones and Coulomb parameters for TIP5P water, Na+, Cl-, and carbon as specified in the paper. Use Lorentz-Berthelot mixing rules and Ewald summation.
- Evidence: `/app/outputs/preparation_info.txt`

### Step 2: CEMC Simulation
- Role: process
- Action: Run canonical ensemble Monte Carlo simulations at 300 K for each system. Perform at least 10⁷ MC steps to ensure equilibrium, attempting equal numbers of ion and water moves and exchange moves. Save trajectory snapshots for analysis.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Radial Distribution Functions and Hydration Numbers
- Role: scored (load-bearing)
- Action: From the simulation snapshots, compute radial distribution functions (RDFs) for Na+-water, Cl--water, and water-water pairs. Determine the first-peak positions (nearest-neighbor distances) for each pair in each system. Compute hydration numbers of Na+ and Cl- by integrating the ion-water RDF up to the first minimum. Report all distances (nm) and hydration numbers in the specified JSON structure.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"systems": [{"name": "bulk|1nm_CNT|2nm_CNT|3nm_CNT", "water_water_nn_distance": <float>, "Na_water_nn_distance": <float>, "Cl_water_nn_distance": <float>, "Na_hydration_number": <float>, "Cl_hydration_number": <float>}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Nearest-neighbor distances and hydration numbers for Na+ and Cl- in bulk electrolyte and CNT-confined systems.
- schema:
  - `type`: object
  - `required`: `systems`
  - `properties`:
    - `systems`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `water_water_nn_distance`, `Na_water_nn_distance`, `Cl_water_nn_distance`, `Na_hydration_number`, `Cl_hydration_number`
        - `properties`:
          - `name`:
            - `type`: string
            - `enum`: `bulk`, `1nm_CNT`, `2nm_CNT`, `3nm_CNT`
          - `water_water_nn_distance`:
            - `type`: number
            - `minimum`: 0
          - `Na_water_nn_distance`:
            - `type`: number
            - `minimum`: 0
          - `Cl_water_nn_distance`:
            - `type`: number
            - `minimum`: 0
          - `Na_hydration_number`:
            - `type`: number
            - `minimum`: 0
          - `Cl_hydration_number`:
            - `type`: number
            - `minimum`: 0

Notes: The task reproduces the simulation-predicted structural results. The experimental ERDF comparison is not part of the scored artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "systems"
        ],
        "properties": {
          "systems": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "water_water_nn_distance",
                "Na_water_nn_distance",
                "Cl_water_nn_distance",
                "Na_hydration_number",
                "Cl_hydration_number"
              ],
              "properties": {
                "name": {
                  "type": "string",
                  "enum": [
                    "bulk",
                    "1nm_CNT",
                    "2nm_CNT",
                    "3nm_CNT"
                  ]
                },
                "water_water_nn_distance": {
                  "type": "number",
                  "minimum": 0
                },
                "Na_water_nn_distance": {
                  "type": "number",
                  "minimum": 0
                },
                "Cl_water_nn_distance": {
                  "type": "number",
                  "minimum": 0
                },
                "Na_hydration_number": {
                  "type": "number",
                  "minimum": 0
                },
                "Cl_hydration_number": {
                  "type": "number",
                  "minimum": 0
                }
              }
            }
          }
        }
      },
      "description": "Nearest-neighbor distances and hydration numbers for Na+ and Cl- in bulk electrolyte and CNT-confined systems."
    }
  ],
  "notes": "The task reproduces the simulation-predicted structural results. The experimental ERDF comparison is not part of the scored artifact."
}
```

## How you are scored
Your submitted `results.json` will be evaluated by a hidden verifier. The verifier compares the reported nearest-neighbor distances for water–water, Na⁺–water, and Cl⁻–water pairs to reference values obtained from a correct implementation of the simulation protocol, using a suitable numerical tolerance. It also checks that the set of hydration numbers across the four systems (bulk and the three CNT diameters) correctly reflects the effect of CNT confinement—i.e., whether the numbers indicate that a particular CNT diameter promotes or hinders ion hydration relative to bulk. Both checks contribute to the final score, and no single numeric value alone is sufficient to pass.
