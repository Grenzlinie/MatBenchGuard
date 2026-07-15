# DFT Calculation of Poisson's Ratios in 2D Group-IV Monochalcogenides

## Problem background
Two-dimensional group-IV monochalcogenide monolayers (SnS, SnSe, GeS, GeSe) adopt a puckered honeycomb structure with four atomic planes. Under in-plane tension, these materials can exhibit a counterintuitive mechanical response: a negative out-of-plane Poisson's ratio, where the monolayer thickens when stretched. This auxetic behaviour may be tuned by external stimuli, making such monolayers candidates for smart nanoscale devices. The task is to compute the Poisson's ratios of the four neutral monolayers and to quantify how the ratios of GeSe respond to electron doping and to large uniaxial strain.

## Approach
Use density-functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) generalized-gradient approximation and projector-augmented wave pseudopotentials. An open-source plane-wave DFT code (e.g., Quantum ESPRESSO) replaces the proprietary code employed in the original study. The monolayer unit cells are placed in a supercell with vacuum in the out-of-plane direction.

For each neutral monolayer, relax the atomic positions and in-plane lattice parameters. Then apply uniaxial strain along the armchair (x) and zigzag (y) directions within a small symmetric range, relaxing atomic positions at each strain, and record the resulting transverse strains. Poisson's ratios are obtained from the linear slope of the transverse strain versus applied strain. For GeSe, repeat the strain-evaluation protocol at several electron doping concentrations (extra electrons per atom) and also sweep the armchair strain from zero up to 0.14. Fit linear regressions to the strain data to extract the Poisson coefficients for each material and condition.

## Reproduction target
Compute the intrinsic out-of-plane Poisson's ratios ν_zx and ν_zy of charge-neutral SnS, SnSe, GeS, and GeSe monolayers, as well as the in-plane Poisson's ratios ν_yx and ν_xy. Three scored output files are produced:

1. **poisson_ratios_neutral.csv** – ν_zx, ν_zy, ν_yx, ν_xy for each of the four materials.
2. **poisson_zy_doping.csv** – ν_zy of GeSe as a function of electron doping (0, 0.025, 0.050, 0.075, 0.100 e⁻/atom).
3. **poisson_zx_strain.csv** – ν_zx of GeSe as a function of applied uniaxial strain ε_x (from 0 to 0.14).

All Poisson's ratios are defined as ν_ij = −∂ε_i/∂ε_j, where ε_j is the applied strain and ε_i is a transverse strain. The transverse strains are measured from the relaxed unit-cell dimensions after atomic relaxation at each strain point.

## Assets

- Quantum ESPRESSO (or other open-source DFT code): https://www.quantum-espresso.org
- Pseudopotentials for Sn, Ge, S, Se (PBE): Standard Solid-State Pseudopotentials (SSSP) library or GBRV library
- Crystal structures of MX monolayers

## Workflow steps

### Step 1: DFT geometry optimization of pristine monolayers
- Role: process
- Action: Perform DFT geometry optimization of SnS, SnSe, GeS, GeSe monolayer unit cells using PBE functional. Relax atomic positions and in-plane cell parameters until forces are below a tight convergence threshold.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Uniaxial strain simulations for neutral monolayers
- Role: process
- Action: For each relaxed monolayer, apply uniaxial strains ε_x and ε_y in the range -2% to 2% (several points), relax atomic positions at each strain, and record the resulting transverse strains ε_y, ε_z (for ε_x loading) and ε_x, ε_z (for ε_y loading).
- Evidence: `/app/outputs/neutral_strain_data.csv`

### Step 3: Compute neutral Poisson's ratios
- Role: scored (load-bearing)
- Action: From the strain data of neutral monolayers, fit linear slopes ∂ε_i/∂ε_j in the applied strain range [-0.02, 0.02] and compute ν_ij = -∂ε_i/∂ε_j for each material and loading direction. Output the Poisson's ratios for SnS, SnSe, GeS, GeSe.
- Output file: `/app/outputs/poisson_ratios_neutral.csv`
- Format: csv
- Contract: material (string), v_zx (float), v_zy (float), v_yx (float), v_xy (float)
- Scoring: scored by hidden verifier

### Step 4: Electron doping simulations for GeSe
- Role: process
- Action: For GeSe monolayer, perform DFT calculations with electron doping concentrations of 0, 0.025, 0.050, 0.075, 0.100 e⁻/atom. For each doping level, relax the structure and then apply uniaxial strain ε_y in the range -2% to 2%. Record the transverse strains ε_z and ε_x.
- Evidence: `/app/outputs/doping_strain_data.csv`

### Step 5: Compute doping-tuned Poisson's ratio
- Role: scored (load-bearing)
- Action: For each electron doping concentration, fit linear slopes from the doping strain data and compute ν_zy. Report ν_zy as a function of doping.
- Output file: `/app/outputs/poisson_zy_doping.csv`
- Format: csv
- Contract: doping_electrons_per_atom (float), v_zy (float)
- Scoring: scored by hidden verifier

### Step 6: Strain engineering simulations for GeSe
- Role: process
- Action: For the relaxed GeSe monolayer, apply large uniaxial strain ε_x in steps from 0 to 0.14. At each strain, relax atomic positions and record transverse strains to enable computation of ν_zx.
- Evidence: `/app/outputs/strain_eng_data.csv`

### Step 7: Compute strain-engineered Poisson's ratio
- Role: scored (load-bearing)
- Action: From the strain engineering data, compute ν_zx at each ε_x value. Report ν_zx as a function of applied uniaxial strain ε_x.
- Output file: `/app/outputs/poisson_zx_strain.csv`
- Format: csv
- Contract: strain_eps_x (float), v_zx (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/poisson_ratios_neutral.csv`
- `/app/outputs/poisson_zy_doping.csv`
- `/app/outputs/poisson_zx_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### poisson_ratios_neutral.csv
- path: `/app/outputs/poisson_ratios_neutral.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Poisson's ratios for charge-neutral SnS, SnSe, GeS, GeSe monolayers. The checker compares each ratio to the paper's reported values within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `material`, `v_zx`, `v_zy`, `v_yx`, `v_xy`
  - `units`: object

### poisson_zy_doping.csv
- path: `/app/outputs/poisson_zy_doping.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: ν_zy of GeSe as a function of electron doping. The checker validates the trend and values against paper-reported doping response.
- schema:
  - `type`: table
  - `required_columns`: `doping_electrons_per_atom`, `v_zy`
  - `units`: object

### poisson_zx_strain.csv
- path: `/app/outputs/poisson_zx_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: ν_zx of GeSe as a function of applied uniaxial strain ε_x. The checker validates the trend and values against paper-reported strain response.
- schema:
  - `type`: table
  - `required_columns`: `strain_eps_x`, `v_zx`
  - `units`: object

Notes: The checker compares the agent's reported Poisson's ratios to the paper-reported reference values using tolerances suitable for open-source DFT re-implementation. No gold values or tolerances are disclosed publicly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "poisson_ratios_neutral.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "v_zx",
          "v_zy",
          "v_yx",
          "v_xy"
        ],
        "units": {}
      },
      "description": "Poisson's ratios for charge-neutral SnS, SnSe, GeS, GeSe monolayers. The checker compares each ratio to the paper's reported values within a hidden tolerance."
    },
    {
      "file": "poisson_zy_doping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping_electrons_per_atom",
          "v_zy"
        ],
        "units": {}
      },
      "description": "ν_zy of GeSe as a function of electron doping. The checker validates the trend and values against paper-reported doping response."
    },
    {
      "file": "poisson_zx_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_eps_x",
          "v_zx"
        ],
        "units": {}
      },
      "description": "ν_zx of GeSe as a function of applied uniaxial strain ε_x. The checker validates the trend and values against paper-reported strain response."
    }
  ],
  "notes": "The checker compares the agent's reported Poisson's ratios to the paper-reported reference values using tolerances suitable for open-source DFT re-implementation. No gold values or tolerances are disclosed publicly."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files and compares them to reference values. Each scored output (the three files listed above) contributes an independent reward component; the final reward is a weighted combination. The verifier checks that the reported numbers are reasonable and follow expected physical trends. Reporting a number alone is not sufficient – the pipeline must execute the workflow steps, and the outputs must be placed in the correct paths and formats. The verifier's tolerances and reference values are not disclosed; the task is to carry out the protocol faithfully and produce the required artifact, not to guess a specific target.
