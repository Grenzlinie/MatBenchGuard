# Lithium adsorption and diffusion on zigzag MoS2 nanoribbons

## Problem background
Two-dimensional MoS2 is a promising electrode material for lithium-ion batteries, and quasi-one-dimensional nanoribbons may further enhance lithium binding and mobility through edge effects. Understanding how Li atoms adsorb and migrate on zigzag MoS2 nanoribbons is important for designing better cathode materials. This task focuses on resolving the edge-dependent adsorption energies and diffusion barriers of Li on such nanoribbons.

## Approach
We use first-principles density functional theory (DFT) with the generalized gradient approximation (PBE functional). The computational workflow is adapted for an open-source DFT code (e.g., Quantum ESPRESSO) with projector augmented wave (PAW) pseudopotentials from the SSSP library. A 7-zigzag MoS2 nanoribbon is modelled with a vacuum layer, and the lattice constant is optimized. Reference total energies of the pristine monolayer and an isolated Li atom are calculated. Li adsorption energies are computed as E_ads = E_host + n*E_Li - E_nLi+host for various sites: at S- and Mo-terminated edges, in the middle region, and on the basal plane of 2D MoS2. Multi-Li edge configurations are also evaluated. Li diffusion barriers are obtained along selected paths using the nudged elastic band method or a static-relaxation climbing-image approach.

## Reproduction target
The goal is to compute:
1) the optimized lattice constant of the 7-ZZ-MoS2 nanoribbon.
2) single Li atom adsorption energies at six S-terminal sites, four Mo-terminal sites, four middle Mo-top sites, and three 2D MoS2 sites (Mo-top, S-top, valley-top).
3) two-Li atom adsorption energies at the S-terminal and Mo-terminal edge configurations (1-1N, 1-d, 1-1s and 7'-7N', 7'-a, 7'-1', 7'-7s').
4) diffusion barriers for Li migration along the S-terminal edge, Mo-terminal edge, from a middle site toward the S-terminal edge, from a middle a-site toward the Mo-terminal edge, and across the 2D monolayer.
All results are to be written as formatted output files and submitted under /app/outputs.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials library: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Prepare initial atomic structures
- Role: process
- Action: Generate initial supercell structures for: pristine 2D MoS2 monolayer, isolated Li atom in vacuum, pristine 7-ZZ-MoS2 nanoribbon, and Li-adsorbed configurations at the sites described in the paper (S-terminal, Mo-terminal, middle Mo-top sites, monolayer Mo-top/S-top/valley-top, and two-Li edge configurations).
- Evidence: none

### Step 2: Relax pristine 2D MoS2 monolayer
- Role: process
- Action: Perform a fixed-cell DFT geometry optimization of the 2D MoS2 monolayer to obtain its total energy, which serves as a reference for adsorption energy calculations.
- Evidence: `/app/outputs/E_MoS2_2D.json`

### Step 3: Compute isolated Li atom total energy
- Role: process
- Action: Perform a DFT calculation of an isolated Li atom in a large vacuum cell to obtain the reference energy E_Li used in the adsorption energy formula.
- Evidence: `/app/outputs/E_Li.json`

### Step 4: Optimize 7-ZZ-MoS2 nanoribbon and extract lattice constant
- Role: scored
- Action: Perform a variable-cell DFT geometry optimization (relax atomic positions and lattice vector) of the pristine 7-ZZ-MoS2 nanoribbon. Extract the relaxed lattice constant along the ribbon axis.
- Output file: `/app/outputs/lattice_constant.json`
- Format: json
- Contract: {"type":"object","properties":{"lattice_constant":{"type":"number","unit":"angstrom"}}}
- Scoring: scored by hidden verifier

### Step 5: Single Li adsorption energies
- Role: scored (load-bearing)
- Action: Perform DFT relaxations for single Li adatoms on the 2D MoS2 monolayer (Mo-top, S-top, valley-top) and on the 7-ZZ-MoS2 NR at distinct sites: S-terminal (sites 1,2,4,5,6), Mo-terminal (sites 4',5',6',7'), and four middle Mo-top sites (a,b,c,d). For each relaxed configuration compute the adsorption energy E_ads = E_host + n*E_Li - E_nLi+host using the reference energies obtained from step1 and step2, and the NR total energy from step3.
- Output file: `/app/outputs/single_li_adsorption.csv`
- Format: csv
- Contract: {"type":"table","required_columns":["site","energy_eV"],"units":{"energy_eV":"eV"}}
- Scoring: scored by hidden verifier

### Step 6: Two Li adsorption energies
- Role: scored
- Action: Perform DFT relaxations for two Li adatoms at the edge configurations: S-terminal (1-1N, 1-d, 1-1s) and Mo-terminal (7'-7N', 7'-a, 7'-1', 7'-7s'). For each configuration compute the total adsorption energy using the same formula and the reference energies from step1 and step2.
- Output file: `/app/outputs/two_li_adsorption.csv`
- Format: csv
- Contract: {"type":"table","required_columns":["configuration","energy_eV"],"units":{"energy_eV":"eV"}}
- Scoring: scored by hidden verifier

### Step 7: Li diffusion barriers
- Role: scored
- Action: Determine minimum energy paths for Li diffusion on 2D MoS2 and along several paths in the 7-ZZ-MoS2 NR (S-terminal edge, Mo-terminal edge, from a middle Mo-top site toward the S-terminal edge, and from a middle a-site toward the Mo-terminal edge) using NEB or a static-relaxation climbing-image method. Report the energy barrier (difference between saddle point and initial minimum) for each path.
- Output file: `/app/outputs/diffusion_barriers.csv`
- Format: csv
- Contract: {"type":"table","required_columns":["path","barrier_eV"],"units":{"barrier_eV":"eV"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constant.json`
- `/app/outputs/single_li_adsorption.csv`
- `/app/outputs/two_li_adsorption.csv`
- `/app/outputs/diffusion_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constant.json
- path: `/app/outputs/lattice_constant.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice constant of the 7-ZZ-MoS2 nanoribbon.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant`: number (unit: angstrom)

### single_li_adsorption.csv
- path: `/app/outputs/single_li_adsorption.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies of single Li atoms at all distinct sites on 2D MoS2 and the 7-ZZ-MoS2 NR.
- schema:
  - `type`: table
  - `required_columns`: `site`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### two_li_adsorption.csv
- path: `/app/outputs/two_li_adsorption.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies of two Li atoms at edge configurations.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### diffusion_barriers.csv
- path: `/app/outputs/diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy barriers for Li diffusion along different paths.
- schema:
  - `type`: table
  - `required_columns`: `path`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

Notes: All scored outputs will be compared to paper-reported reference values with predefined tolerances. The agent must compute these quantities using an open-source DFT implementation and the specified pseudopotentials, following the workflow described in the steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constant.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant": "number (unit: angstrom)"
        }
      },
      "description": "Optimized lattice constant of the 7-ZZ-MoS2 nanoribbon."
    },
    {
      "file": "single_li_adsorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Adsorption energies of single Li atoms at all distinct sites on 2D MoS2 and the 7-ZZ-MoS2 NR."
    },
    {
      "file": "two_li_adsorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Adsorption energies of two Li atoms at edge configurations."
    },
    {
      "file": "diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "path",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Energy barriers for Li diffusion along different paths."
    }
  ],
  "notes": "All scored outputs will be compared to paper-reported reference values with predefined tolerances. The agent must compute these quantities using an open-source DFT implementation and the specified pseudopotentials, following the workflow described in the steps."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently compares each scored file (lattice_constant.json, single_li_adsorption.csv, two_li_adsorption.csv, diffusion_barriers.csv) against a hidden reference derived from the published results. The verifier reads your files, extracts the reported values, and scores them according to a weighted rubric. The final reward combines the scores from each required artifact. Simply outputting the paper's numbers is insufficient; the values must be generated by running the described DFT workflow. The scoring is fully automated and does not require human visual inspection.
