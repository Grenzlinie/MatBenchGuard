# DFT Adsorption on Transition Metal Doped Rhodium Clusters

## Problem background
Transition-metal clusters are model catalysts whose adsorption properties toward small molecules can be tuned by doping with a single heteroatom. This task recreates a representative set of density-functional theory (DFT) calculations that quantify how doping a Rh4 tetrahedron with a 3d or 4d atom changes the cluster's stability, magnetic moment, and its ability to bind gas molecules (CO, CO2, N2, NO, O2, N2O, NO2). The ultimate goal is to compute the binding energies, magnetic moments, physical and chemical adsorption energies, and the energy barriers for O2 dissociation on pure and doped rhodium clusters using an open-source DFT code.

## Approach
The calculations use spin-polarized DFT with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional, as implemented in the GPAW code coupled with the Atomic Simulation Environment (ASE). Each cluster and cluster-molecule complex is placed in a cubic supercell with periodic boundary conditions. For pure Rh4 and selected doped clusters (Rh3X with X = Fe, Ru, Ti, Cr, Tc), the geometries are fully optimized to obtain ground-state total energies, bond lengths, and magnetic moments. Reference energies for isolated atoms and gas-phase molecules are computed under identical settings. Adsorption energies are then evaluated as the total energy difference: E_ads = E(cluster) + E(molecule) – E(complex), where a positive value indicates an exothermic adsorption. For the O2 dissociation reaction, the minimum energy path is mapped using the climbing-image nudged elastic band (CI-NEB) method to extract the activation barrier on several clusters. The workflow contrasts the behavior of pure Rh4 with that of the doped clusters, revealing how the dopant identity modulates stability, magnetism, and chemical reactivity.

## Reproduction target
The reproduction target is a single JSON file, `computed_properties.json`, placed at `/app/outputs`, that contains the following ground-state properties computed from the DFT workflow described above:
- The nearest-neighbor Rh–Rh bond length, average binding energy per atom, and total integer magnetic moment of the optimized pure Rh4 cluster.
- The average binding energies and magnetic moments of Rh3Fe and Rh3Ru.
- Physical adsorption energies (positive) of NO, CO, CO2, and N2 on both Rh4 and Rh3Ti.
- Chemical adsorption energies (positive) of O2, N2O, and NO2 on Rh4 and Rh3Fe.
- O2 dissociation energy barriers on Rh4, Rh3Cr, and Rh3Tc.

All adsorption energies must be computed using the definition E_ads = E(cluster) + E(molecule) – E(complex). The reported values must be positive (exothermic adsorption). The magnetic moments are required as integer values (units of µB). The exact key names and structure of the JSON file are specified in the output contract.

## Assets

- GPAW: gpaw
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Geometry optimization of bare Rh4 and selected Rh3X clusters
- Role: process
- Action: Construct a 14 Å cubic supercell containing a Rh4 tetrahedron. Perform spin‑polarized DFT geometry optimization (PBE, energy convergence 1e‑6 eV, force convergence 0.005 eV/Å) to obtain the ground‑state geometry, total energy, and magnetic moment. Then, for each dopant X = Fe, Ru, Ti, Cr, Tc, substitute one Rh atom in the optimized Rh4 geometry, re‑optimize, and record total energies and magnetic moments.
- Evidence: `/app/outputs/cluster_optimization.log`

### Step 2: Calculation of isolated atom and molecule reference energies
- Role: process
- Action: Compute spin‑polarized total energies of isolated atoms Rh, Fe, Ru, Ti, Cr, Tc and isolated molecules CO, CO2, N2, NO, O2, N2O, NO2 in the same cubic supercell, using identical DFT parameters. These reference energies are needed to evaluate binding and adsorption energies.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Adsorption geometry optimization
- Role: process
- Action: For each combination (Rh4 + molecule) and (Rh3Ti + molecule) where molecule = NO, CO, CO2, N2, and for (Rh4 + molecule) and (Rh3Fe + molecule) where molecule = O2, N2O, NO2, place the molecule at plausible high‑symmetry adsorption sites on the cluster, perform DFT geometry optimization, and record the lowest total energy for each system. The initial cluster geometries are taken from step01.
- Evidence: `/app/outputs/adsorption_complexes_energies.json`

### Step 4: NEB barrier calculations for O2 dissociation
- Role: process
- Action: For O2 adsorption on Rh4, Rh3Cr, and Rh3Tc, build initial (physisorbed O2) and final (dissociated O atoms) structures from step03 results. Run climbing‑image nudged elastic band (CI-NEB) calculations with force convergence 0.01 eV/Å to obtain the minimum energy path and extract the energy barrier (energy difference between transition state and initial state). Use the same DFT parameters as previous steps.
- Evidence: `/app/outputs/o2_barriers.json`

### Step 5: Compute and output target properties
- Role: scored (load-bearing)
- Action: Using the total energies from the previous steps, compute average binding energies (E_b = [3*E(Rh) + E(X) − E(Rh3X)]/4), adsorption energies (E_ads = E(cluster) + E(molecule) − E(complex)), magnetic moments, and the Rh4 bond length from the optimized geometry. Collect all results into a single JSON file named computed_properties.json exactly following the output schema.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: A JSON object with keys: Rh4_bond_length (float, Å), Rh4_avg_binding_energy (float, eV), Rh4_magnetic_moment (integer, μB), Rh3Fe_avg_binding_energy (float, eV), Rh3Fe_magnetic_moment (integer, μB), Rh3Ru_avg_binding_energy (float, eV), Rh3Ru_magnetic_moment (integer, μB), physical_adsorption_energies (object with keys: Rh4_NO, Rh4_CO, Rh4_CO2, Rh4_N2, Rh3Ti_NO, Rh3Ti_CO, Rh3Ti_CO2, Rh3Ti_N2; values in eV), chemical_adsorption_energies (object with keys: Rh4_O2, Rh4_N2O, Rh4_NO2, Rh3Fe_O2, Rh3Fe_N2O, Rh3Fe_NO2; values in eV), O2_barriers (object with keys: Rh4, Rh3Cr, Rh3Tc; values in eV). All adsorption energies are positive (E_ads computed by Eq. 3). Magnetic moments are integer values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: All target computed properties for the cluster series. The hidden checker compares each numeric value to paper‑reported reference values within appropriate tolerances, and verifies selectivity orders.
- schema:
  - `type`: object
  - `required`: `Rh4_bond_length`, `Rh4_avg_binding_energy`, `Rh4_magnetic_moment`, `Rh3Fe_avg_binding_energy`, `Rh3Fe_magnetic_moment`, `Rh3Ru_avg_binding_energy`, `Rh3Ru_magnetic_moment`, `physical_adsorption_energies`, `chemical_adsorption_energies`, `O2_barriers`
  - `properties`:
    - `Rh4_bond_length`:
      - `type`: number
      - `unit`: Å
      - `description`: Nearest-neighbour Rh–Rh bond length in the optimized Rh4 tetrahedron.
    - `Rh4_avg_binding_energy`:
      - `type`: number
      - `unit`: eV
      - `description`: Average binding energy per atom of Rh4, computed as [4*E(Rh) - E(Rh4)]/4.
    - `Rh4_magnetic_moment`:
      - `type`: integer
      - `unit`: μB
      - `description`: Total magnetic moment of the Rh4 cluster.
    - `Rh3Fe_avg_binding_energy`:
      - `type`: number
      - `unit`: eV
      - `description`: Average binding energy per atom of Rh3Fe, computed as [3*E(Rh) + E(Fe) - E(Rh3Fe)]/4.
    - `Rh3Fe_magnetic_moment`:
      - `type`: integer
      - `unit`: μB
      - `description`: Total magnetic moment of the Rh3Fe cluster.
    - `Rh3Ru_avg_binding_energy`:
      - `type`: number
      - `unit`: eV
      - `description`: Average binding energy per atom of Rh3Ru, computed as [3*E(Rh) + E(Ru) - E(Rh3Ru)]/4.
    - `Rh3Ru_magnetic_moment`:
      - `type`: integer
      - `unit`: μB
      - `description`: Total magnetic moment of the Rh3Ru cluster.
    - `physical_adsorption_energies`:
      - `type`: object
      - `properties`:
        - `Rh4_NO`:
          - `type`: number
          - `unit`: eV
        - `Rh4_CO`:
          - `type`: number
          - `unit`: eV
        - `Rh4_CO2`:
          - `type`: number
          - `unit`: eV
        - `Rh4_N2`:
          - `type`: number
          - `unit`: eV
        - `Rh3Ti_NO`:
          - `type`: number
          - `unit`: eV
        - `Rh3Ti_CO`:
          - `type`: number
          - `unit`: eV
        - `Rh3Ti_CO2`:
          - `type`: number
          - `unit`: eV
        - `Rh3Ti_N2`:
          - `type`: number
          - `unit`: eV
      - `required`: `Rh4_NO`, `Rh4_CO`, `Rh4_CO2`, `Rh4_N2`, `Rh3Ti_NO`, `Rh3Ti_CO`, `Rh3Ti_CO2`, `Rh3Ti_N2`
    - `chemical_adsorption_energies`:
      - `type`: object
      - `properties`:
        - `Rh4_O2`:
          - `type`: number
          - `unit`: eV
        - `Rh4_N2O`:
          - `type`: number
          - `unit`: eV
        - `Rh4_NO2`:
          - `type`: number
          - `unit`: eV
        - `Rh3Fe_O2`:
          - `type`: number
          - `unit`: eV
        - `Rh3Fe_N2O`:
          - `type`: number
          - `unit`: eV
        - `Rh3Fe_NO2`:
          - `type`: number
          - `unit`: eV
      - `required`: `Rh4_O2`, `Rh4_N2O`, `Rh4_NO2`, `Rh3Fe_O2`, `Rh3Fe_N2O`, `Rh3Fe_NO2`
    - `O2_barriers`:
      - `type`: object
      - `properties`:
        - `Rh4`:
          - `type`: number
          - `unit`: eV
        - `Rh3Cr`:
          - `type`: number
          - `unit`: eV
        - `Rh3Tc`:
          - `type`: number
          - `unit`: eV
      - `required`: `Rh4`, `Rh3Cr`, `Rh3Tc`

Notes: The reference_match policy is used: the checker holds the paper‑reported hidden gold and tolerances. The agent must produce positive adsorption energies using the definition E_ads = E(cluster) + E(molecule) − E(complex). Selectivity orders (physical: NO > CO > CO2 ≥ N2; chemical: O2 > NO2 > N2O) are expected but not explicitly enforced in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Rh4_bond_length",
          "Rh4_avg_binding_energy",
          "Rh4_magnetic_moment",
          "Rh3Fe_avg_binding_energy",
          "Rh3Fe_magnetic_moment",
          "Rh3Ru_avg_binding_energy",
          "Rh3Ru_magnetic_moment",
          "physical_adsorption_energies",
          "chemical_adsorption_energies",
          "O2_barriers"
        ],
        "properties": {
          "Rh4_bond_length": {
            "type": "number",
            "unit": "Å",
            "description": "Nearest-neighbour Rh–Rh bond length in the optimized Rh4 tetrahedron."
          },
          "Rh4_avg_binding_energy": {
            "type": "number",
            "unit": "eV",
            "description": "Average binding energy per atom of Rh4, computed as [4*E(Rh) - E(Rh4)]/4."
          },
          "Rh4_magnetic_moment": {
            "type": "integer",
            "unit": "μB",
            "description": "Total magnetic moment of the Rh4 cluster."
          },
          "Rh3Fe_avg_binding_energy": {
            "type": "number",
            "unit": "eV",
            "description": "Average binding energy per atom of Rh3Fe, computed as [3*E(Rh) + E(Fe) - E(Rh3Fe)]/4."
          },
          "Rh3Fe_magnetic_moment": {
            "type": "integer",
            "unit": "μB",
            "description": "Total magnetic moment of the Rh3Fe cluster."
          },
          "Rh3Ru_avg_binding_energy": {
            "type": "number",
            "unit": "eV",
            "description": "Average binding energy per atom of Rh3Ru, computed as [3*E(Rh) + E(Ru) - E(Rh3Ru)]/4."
          },
          "Rh3Ru_magnetic_moment": {
            "type": "integer",
            "unit": "μB",
            "description": "Total magnetic moment of the Rh3Ru cluster."
          },
          "physical_adsorption_energies": {
            "type": "object",
            "properties": {
              "Rh4_NO": {
                "type": "number",
                "unit": "eV"
              },
              "Rh4_CO": {
                "type": "number",
                "unit": "eV"
              },
              "Rh4_CO2": {
                "type": "number",
                "unit": "eV"
              },
              "Rh4_N2": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Ti_NO": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Ti_CO": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Ti_CO2": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Ti_N2": {
                "type": "number",
                "unit": "eV"
              }
            },
            "required": [
              "Rh4_NO",
              "Rh4_CO",
              "Rh4_CO2",
              "Rh4_N2",
              "Rh3Ti_NO",
              "Rh3Ti_CO",
              "Rh3Ti_CO2",
              "Rh3Ti_N2"
            ]
          },
          "chemical_adsorption_energies": {
            "type": "object",
            "properties": {
              "Rh4_O2": {
                "type": "number",
                "unit": "eV"
              },
              "Rh4_N2O": {
                "type": "number",
                "unit": "eV"
              },
              "Rh4_NO2": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Fe_O2": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Fe_N2O": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Fe_NO2": {
                "type": "number",
                "unit": "eV"
              }
            },
            "required": [
              "Rh4_O2",
              "Rh4_N2O",
              "Rh4_NO2",
              "Rh3Fe_O2",
              "Rh3Fe_N2O",
              "Rh3Fe_NO2"
            ]
          },
          "O2_barriers": {
            "type": "object",
            "properties": {
              "Rh4": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Cr": {
                "type": "number",
                "unit": "eV"
              },
              "Rh3Tc": {
                "type": "number",
                "unit": "eV"
              }
            },
            "required": [
              "Rh4",
              "Rh3Cr",
              "Rh3Tc"
            ]
          }
        }
      },
      "description": "All target computed properties for the cluster series. The hidden checker compares each numeric value to paper‑reported reference values within appropriate tolerances, and verifies selectivity orders."
    }
  ],
  "notes": "The reference_match policy is used: the checker holds the paper‑reported hidden gold and tolerances. The agent must produce positive adsorption energies using the definition E_ads = E(cluster) + E(molecule) − E(complex). Selectivity orders (physical: NO > CO > CO2 ≥ N2; chemical: O2 > NO2 > N2O) are expected but not explicitly enforced in this contract."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the `computed_properties.json` file you produce. The verifier first checks that all required keys are present and that every value is of the correct type (number, integer, object). It then compares your computed numeric results against reference values derived from the original investigation, using appropriate tolerances for bond lengths, binding energies, adsorption energies, and barriers. It also verifies that the trends among the adsorption energies (the relative ordering of NO, CO, CO2, N2 and of O2, NO2, N2O) are consistent with the expected physical behavior of these systems. The final score is a weighted combination of these checks. Reporting numbers that happen to match the reference without having actually performed the DFT calculations will not earn a high score, because the check includes structural and trend consistency that requires a self-consistent set of energetics.
