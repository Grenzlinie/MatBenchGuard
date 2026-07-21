# Submonolayer Melting of CO₂ on Graphite: Herringbone Structure and Melting Temperatures from Molecular Dynamics

## Problem background
Carbon dioxide molecules physisorbed on the basal plane of graphite can form ordered solid monolayers. At submonolayer coverages, the adsorbate may adopt a two‑sublattice herringbone packing in which the molecular axes lie nearly parallel to the surface but are tilted relative to each other. This task computes the minimum‑energy structure of such a herringbone solid and determines its thermal stability—specifically, the temperature at which the orientational order melts—using two different models of the CO₂ intermolecular interaction.

## Approach
Two molecular models are employed: MOM (three‑site Lennard‑Jones plus point charges) and PRC1 (exp‑6 non‑electrostatic interactions plus point charges, with a charge distribution that preserves the quadrupole moment). The molecule–surface interaction is described by the Steele Fourier expansion of the graphite basal plane, parameterised via combining rules from the standard carbon Lennard‑Jones parameters.

First, energy minimisations of a two‑molecule unit cell are performed for each model, starting from a herringbone arrangement. The minimisation searches over the cell lengths a, b, the cell angle α_cell, and the molecular positions and orientations, yielding the incommensurate ground‑state structure.

Second, the minimised unit cell is used to construct a strip geometry at coverage θ = 0.5: 128 molecules are placed in a 59.1 Å × 68.2 Å simulation box that spans the x‑direction, bordered by empty surface along y. Microcanonical (NVE) molecular‑dynamics simulations are run at several temperatures between 100 K and 130 K. The herringbone orientational order parameter OP_herr is computed against temperature. The melting temperature is estimated as the midpoint of the sharp drop in OP_herr.

## Reproduction target
For both the MOM and PRC1 models, compute the equilibrium herringbone structure and the submonolayer melting temperature.

• Minimum‑energy herringbone structure: obtain the incommensurate two‑sublattice unit cell (dimensions a, b, cell angle α_cell), the molecular orientation angles β₁ and β₂, the height z of the molecules above the surface, the coverage θ, and the potential energy per molecule V/N. Write these to `step_02_min_energy_structure.json`.

• Melting temperature: from the temperature dependence of OP_herr, estimate the melting point of the herringbone solid for each model and write the values to `step_01_melting_temperatures.json`.

## Assets

- LAMMPS molecular dynamics package: https://lammps.sandia.gov/
- Graphite basal-plane structure and Steele potential parameters: 10.1016/0039-6028(73)90264-1
- Python with numpy, scipy, matplotlib: PyPI

## Workflow steps

### Step 1: Prepare interaction potentials
- Role: process
- Action: Implement the CO₂–CO₂ intermolecular potentials (MOM and PRC1) and the molecule–graphite surface potential via the Steele expansion for CO₂ on graphite. Use published potential parameters: MOM (three-site Lennard-Jones + point charges), PRC1 (exp-6 non-electrostatic + point charges with reduced number of charges preserving the quadrupole moment). The molecule–surface term uses the Steele Fourier expansion with combining rules from Lennard-Jones carbon parameters (σ=3.4 Å, ε=28 K) or equivalent exp-6 parameters.
- Evidence: none

### Step 2: Energy minimization of herringbone structures
- Role: scored
- Action: For the MOM and PRC1 models, perform energy minimization of a two-molecule unit cell to find the incommensurate herringbone ground state. Vary cell parameters (a, b, cell angle α_cell), molecular positions and orientations. Minimize the total potential energy including intermolecular interactions truncated at a centre-of-mass cutoff and the surface potential. Extract the unit-cell parameters, molecular orientation angles β₁ and β₂, height z of molecules above the surface, coverage θ, and potential energy per molecule V/N. Report the results in the output file.
- Output file: `/app/outputs/step_02_min_energy_structure.json`
- Format: json
- Contract: {"MOM": {"a": "float (Å)", "b": "float (Å)", "alpha_cell": "float (deg)", "beta1": "float (deg)", "beta2": "float (deg)", "z": "float (Å)", "theta": "float", "energy_per_molecule": "float (K)"}, "PRC1": {"a": "float (Å)", "b": "float (Å)", "alpha_cell": "float (deg)", "beta1": "float (deg)", "beta2": "float (deg)", "z": "float (Å)", "theta": "float", "energy_per_molecule": "float (K)"}}
- Scoring: scored by hidden verifier

### Step 3: Molecular dynamics and melting temperature estimation
- Role: scored (load-bearing)
- Action: Using the energy-minimized herringbone unit cells, construct a simulation cell of 59.1 Å × 68.2 Å and fill it with 128 molecules arranged in a rectangular strip spanning the x-direction to achieve a coverage θ=0.5. Run NVE molecular-dynamics simulations for both MOM and PRC1 models at several temperatures between 100 K and 130 K. For each temperature, equilibrate the system and then compute the herringbone order parameter OP_herr = (2/N_sublattice) Σ_{i∈sublattice} cos(2 φ_i), where φ_i is the angle between the projection of the molecular axis onto the surface and the x-axis of the simulation cell; assign molecules to a sublattice based on the sign of their orientation angle relative to the glide line (the two sublattices have opposite signs). Analyze the temperature dependence of OP_herr to locate the melting temperature (the midpoint of the sharp drop). Report the estimated melting temperatures for MOM and PRC1.
- Output file: `/app/outputs/step_01_melting_temperatures.json`
- Format: json
- Contract: {"MOM_melting_T": "float (K)", "PRC1_melting_T": "float (K)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_melting_temperatures.json`
- `/app/outputs/step_02_min_energy_structure.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_melting_temperatures.json
- path: `/app/outputs/step_01_melting_temperatures.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Estimated melting temperatures of the submonolayer herringbone solid for MOM and PRC1 models as obtained from MD simulations.
- schema:
  - `type`: object
  - `required`:
    - `MOM_melting_T`: float (K)
    - `PRC1_melting_T`: float (K)

### step_02_min_energy_structure.json
- path: `/app/outputs/step_02_min_energy_structure.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Minimum-energy incommensurate herringbone structures: unit-cell parameters, molecular orientations, height, coverage, and potential energy per molecule for MOM and PRC1.
- schema:
  - `type`: object
  - `required`:
    - `MOM`:
      - `a`: float (Å)
      - `b`: float (Å)
      - `alpha_cell`: float (deg)
      - `beta1`: float (deg)
      - `beta2`: float (deg)
      - `z`: float (Å)
      - `theta`: float
      - `energy_per_molecule`: float (K)
    - `PRC1`:
      - `a`: float (Å)
      - `b`: float (Å)
      - `alpha_cell`: float (deg)
      - `beta1`: float (deg)
      - `beta2`: float (deg)
      - `z`: float (Å)
      - `theta`: float
      - `energy_per_molecule`: float (K)

Notes: Tolerances for each parameter will be applied individually; the hidden gold is the paper's reported values. The MD melting temperature scoring allows a ±6 K window to account for statistical and implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_melting_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "MOM_melting_T": "float (K)",
          "PRC1_melting_T": "float (K)"
        }
      },
      "description": "Estimated melting temperatures of the submonolayer herringbone solid for MOM and PRC1 models as obtained from MD simulations."
    },
    {
      "file": "step_02_min_energy_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "MOM": {
            "a": "float (Å)",
            "b": "float (Å)",
            "alpha_cell": "float (deg)",
            "beta1": "float (deg)",
            "beta2": "float (deg)",
            "z": "float (Å)",
            "theta": "float",
            "energy_per_molecule": "float (K)"
          },
          "PRC1": {
            "a": "float (Å)",
            "b": "float (Å)",
            "alpha_cell": "float (deg)",
            "beta1": "float (deg)",
            "beta2": "float (deg)",
            "z": "float (Å)",
            "theta": "float",
            "energy_per_molecule": "float (K)"
          }
        }
      },
      "description": "Minimum-energy incommensurate herringbone structures: unit-cell parameters, molecular orientations, height, coverage, and potential energy per molecule for MOM and PRC1."
    }
  ],
  "notes": "Tolerances for each parameter will be applied individually; the hidden gold is the paper's reported values. The MD melting temperature scoring allows a ±6 K window to account for statistical and implementation differences."
}
```

## How you are scored
A hidden verifier inspects your output files and compares them against reference values derived from the literature. Each scored artifact—`step_02_min_energy_structure.json` and `step_01_melting_temperatures.json`—is checked independently, and the separate scores are combined by weight into a final reward. The verifier uses appropriate tolerances to account for different implementations; you do not need to hit exact numbers. Only the contents of the JSON files are evaluated; your code, intermediate logs, and raw simulation data are not examined. Submit physically plausible numbers that reflect the modelled system; values far from the expected magnitudes will receive little or no credit.
