# Bilayer Water Phase Diagram: Compression and Superheating Limits via MD Simulations

## Problem background
Bilayer water confined in a graphene nanocapillary (separation h=9.0 Å) exhibits distinct polymorphic phases under varying temperature and lateral pressure. Mapping the compression-limit and superheating-limit phase boundaries is important for understanding confined water/ice thermodynamics and stability in nanoscale environments. This task aims to reproduce the key quantitative boundaries of these phase diagrams through molecular dynamics simulations.

## Approach
The approach uses classical molecular dynamics (MD) with the LAMMPS simulator. A bilayer water system is constructed between two parallel graphene sheets separated by 9.0 Å, with two water reservoirs. Interatomic potentials are the TIP4P/2005 water model and Lennard-Jones parameters for water-graphene interactions. The compression-limit phase diagram is obtained by isothermal-isobaric simulations at selected temperatures (240–300 K) where lateral pressure is increased stepwise; phase transitions (BL-A, BL-VHDI, BL-AAI) are identified from changes in potential energy, mean-squared displacement, and water occupancy. The superheating limit is probed by heating stable configurations (BL-VHDI and BL-AAI) at selected lateral pressures and detecting melting from abrupt changes in potential energy or diffusivity. The workflow consists of system construction, compression simulations, extraction of superheating starting structures, and heating simulations.

## Reproduction target
The target is to produce two CSV tables. The first, 'compression_limit_transitions.csv', reports the lateral pressures at which bilayer water transitions from BL-A to BL-VHDI and from BL-VHDI to BL-AAI, for each temperature in {240, 260, 280, 300} K. The second, 'superheating_limit_melting.csv', reports the melting temperatures of BL-VHDI and BL-AAI at lateral pressures 1.0, 2.0, 3.0, and 4.0 GPa. Use NaN where a transition does not occur or a phase is not stable. The values must be determined from MD simulation observables as described in the workflow steps.

## Assets

- LAMMPS: https://www.lammps.org
- TIP4P/2005 water model parameters: 10.1063/1.2121687
- Carbon-oxygen/hydrogen LJ parameters: https://doi.org/10.1021/jp034631+

## Workflow steps

### Step 1: System construction and force field parameterization
- Role: process
- Action: Construct initial simulation cell with two parallel graphene sheets separated by h=9.0 Å, channel dimensions 42.60 Å x 36.89 Å. Add two water reservoirs (1000 molecules each) connected to the channel. Set up periodic boundary conditions. Define interatomic potentials: TIP4P/2005 for water, Lennard-Jones parameters for carbon-oxygen/hydrogen interactions as specified in the simulation methodology. Prepare the system for LAMMPS MD runs.
- Evidence: none

### Step 2: Compression simulations and transition identification
- Role: scored (load-bearing)
- Action: For each temperature T in {240, 260, 280, 300} K, run MD simulations in the isothermal-isobaric (NPzzT) ensemble. Increase lateral pressure P_zz gradually from 0.1 to 5.0 GPa stepwise. Monitor potential energy per molecule, mean-squared displacement (MSD), number of water molecules in the channel, and oxygen-oxygen radial distribution function g_O-O(r) to identify phase transitions. Determine the lateral pressures at which the system transforms: BL-A to BL-VHDI, and BL-VHDI to BL-AAI. Where a transition does not occur at a given T, mark as NaN. Output the identified transition pressures.
- Output file: `/app/outputs/compression_limit_transitions.csv`
- Format: csv
- Contract: Columns: temperature (float, K), P_BL_A_to_BL_VHDI (float, GPa, NaN if not observed), P_BL_VHDI_to_BL_AAI (float, GPa, NaN if not observed). Example row: 240, 1.2, 4.1
- Scoring: scored by hidden verifier

### Step 3: Prepare superheating initial configurations
- Role: process
- Action: From the compression simulation trajectories, extract snapshots of stable BL-VHDI (e.g., at P_zz=2.0 GPa) and BL-AAI (e.g., at P_zz=4.0 GPa) to serve as starting structures for the superheating runs.
- Evidence: none

### Step 4: Superheating simulations and melting identification
- Role: scored
- Action: For selected lateral pressures P_zz = 1.0, 2.0, 3.0, 4.0 GPa, run heating MD simulations (temperature ramp) starting from BL-VHDI and BL-AAI configurations. Identify the melting temperature of each phase from abrupt changes in potential energy per molecule or MSD. Where a phase is not stable or melting not observed, mark as NaN. Output the melting points.
- Output file: `/app/outputs/superheating_limit_melting.csv`
- Format: csv
- Contract: Columns: lateral_pressure (float, GPa), T_melt_BL_VHDI (float, K, NaN if not observed), T_melt_BL_AAI (float, K, NaN if not observed).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/compression_limit_transitions.csv`
- `/app/outputs/superheating_limit_melting.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### compression_limit_transitions.csv
- path: `/app/outputs/compression_limit_transitions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Compression-limit transition pressures for bilayer water at four temperatures. The hidden checker compares each reported pressure to the paper's gold value with an absolute tolerance. NaN is used if a transition is not observed at that temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `P_BL_A_to_BL_VHDI`, `P_BL_VHDI_to_BL_AAI`
  - `units`:
    - `temperature`: K
    - `P_BL_A_to_BL_VHDI`: GPa
    - `P_BL_VHDI_to_BL_AAI`: GPa

### superheating_limit_melting.csv
- path: `/app/outputs/superheating_limit_melting.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Superheating-limit melting temperatures for BL-VHDI and BL-AAI bilayer ice at four lateral pressures. The hidden checker compares each reported temperature to the paper's gold value with an absolute tolerance. NaN is used when the phase is not stable or melting is not observed.
- schema:
  - `type`: table
  - `required_columns`: `lateral_pressure`, `T_melt_BL_VHDI`, `T_melt_BL_AAI`
  - `units`:
    - `lateral_pressure`: GPa
    - `T_melt_BL_VHDI`: K
    - `T_melt_BL_AAI`: K

Notes: The task reproduces the key quantitative boundaries of the compression-limit and superheating-limit phase diagrams. Only the specified CSV entries are required; trends (temperature threshold, monotonicity of T_melt_BL_AAI, local maximum for BL-VHDI) are verified as additional checks in the hidden checker but do not require separate output files.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "compression_limit_transitions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "P_BL_A_to_BL_VHDI",
          "P_BL_VHDI_to_BL_AAI"
        ],
        "units": {
          "temperature": "K",
          "P_BL_A_to_BL_VHDI": "GPa",
          "P_BL_VHDI_to_BL_AAI": "GPa"
        }
      },
      "description": "Compression-limit transition pressures for bilayer water at four temperatures. The hidden checker compares each reported pressure to the paper's gold value with an absolute tolerance. NaN is used if a transition is not observed at that temperature."
    },
    {
      "file": "superheating_limit_melting.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lateral_pressure",
          "T_melt_BL_VHDI",
          "T_melt_BL_AAI"
        ],
        "units": {
          "lateral_pressure": "GPa",
          "T_melt_BL_VHDI": "K",
          "T_melt_BL_AAI": "K"
        }
      },
      "description": "Superheating-limit melting temperatures for BL-VHDI and BL-AAI bilayer ice at four lateral pressures. The hidden checker compares each reported temperature to the paper's gold value with an absolute tolerance. NaN is used when the phase is not stable or melting is not observed."
    }
  ],
  "notes": "The task reproduces the key quantitative boundaries of the compression-limit and superheating-limit phase diagrams. Only the specified CSV entries are required; trends (temperature threshold, monotonicity of T_melt_BL_AAI, local maximum for BL-VHDI) are verified as additional checks in the hidden checker but do not require separate output files."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the two CSV files. The verifier compares each reported transition pressure and melting temperature to a hidden reference value determined from the original study, using absolute tolerances. It also checks that the set of reported values satisfies certain structural relationships (e.g., monotonicity or the presence of a local extremum) expected from the underlying physics. The final score is a weighted combination of numerical accuracy (within tolerance) and compliance with these structural checks. Reporting the paper's exact numbers is not necessary; an honest re‑simulation that yields values within tolerance of the hidden references and respects the physical trends earns full credit.
