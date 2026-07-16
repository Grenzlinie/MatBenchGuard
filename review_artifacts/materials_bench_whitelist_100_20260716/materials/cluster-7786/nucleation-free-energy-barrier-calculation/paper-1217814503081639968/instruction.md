# Nucleation temperature vs substrate lattice mismatch from molecular dynamics simulations

## Problem background
Heterogeneous ice nucleation on foreign surfaces is a key process in atmospheric science, cryobiology, and materials design. The ice-nucleating ability of a substrate depends on both chemical interactions and the structural match between ice and the substrate lattice. To disentangle these effects, this work uses a pure ice-like substrate (water molecules with identical interactions) where only geometric mismatch (δ) is varied. The task quantifies the nucleation temperature T_n at a fixed reference rate for different mismatches, substrate rigidities, and crystal orientations, and extracts the dependence dT_n/dδ. All required inputs are publicly available: the mW water model, the ice Ih unit cell at coexistence, and the open-source LAMMPS code.

## Approach
The approach uses molecular dynamics simulations with the mW monatomic water model implemented in LAMMPS. For each substrate condition (rigid or flexible wells, pII/basal/pI orientation, mismatch δ=5,7,8%), an initial system is constructed by deforming the ice Ih orthorhombic unit cell by a factor f corresponding to the desired percent mismatch δ = 100·|f-1|, replicating the deformed cell to form a slab, and melting a portion at 300 K to create a liquid layer adjacent to a frozen substrate region. NVT ensemble simulations with a Nosé–Hoover thermostat and a 3 fs time step are then run at supercooled temperatures to observe nucleation events, identified by sudden drops in potential energy. For each temperature, the induction time t_ind is averaged over several independent trajectories, and the heterogeneous nucleation rate J = 1/(2 A t_ind) is computed, where A is the area of the substrate face exposed to the liquid. By performing simulations at several temperatures, J(T) curves are obtained for every system. Finally, for each system, the nucleation temperature T_n is defined as the temperature at which the nucleation rate reaches log10[J(m^{-2}s^{-1})] = 23.6, obtained by interpolation of the J(T) curve.

## Reproduction target
Compute the nucleation temperature T_n (the temperature at which log10[J(m^{-2}s^{-1})] = 23.6) for all 15 substrate systems listed in Step 4: rigid pII substrates at δ=5%, 7%, 8%; wells pII substrates from the flexibility study at δ=5%, 7%, 8%; wells basal substrates at δ=5%, 7%, 8%; wells pI substrates at δ=5%, 7%, 8%; and wells pII substrates from the orientation study at δ=5%, 7%, 8%. Report all T_n values in a single CSV file `nucleation_temperatures.csv` with columns: substrate_type (string: 'rigid' or 'wells'), orientation (string: 'basal', 'pI', or 'pII'), mismatch_delta (integer: 5, 7, or 8), T_n_K (float). The CSV must contain exactly 15 rows covering all the combinations above.

## Assets

- LAMMPS: https://www.lammps.org
- mW water model parameters: 10.1021/jp805227c
- Ice Ih orthorhombic unit cell at coexistence (Table I):
  - Box dimensions: Lx = 8.853 Å, Ly = 7.671 Å, Lz = 7.203 Å.
  - Fractional coordinates (16 molecules):
    x     y     z
    0.000 0.000 0.000
    0.500 0.000 0.000
    0.250 0.500 0.000
    0.750 0.500 0.000
    0.250 0.167 0.125
    0.750 0.167 0.125
    0.000 0.667 0.125
    0.500 0.667 0.125
    0.250 0.167 0.500
    0.750 0.167 0.500
    0.000 0.667 0.500
    0.500 0.667 0.500
    0.000 0.000 0.625
    0.500 0.000 0.625
    0.250 0.500 0.625
    0.750 0.500 0.625

## Workflow steps

### Step 1: System and substrate preparation
- Role: process
- Action: Generate initial configurations for all required substrate systems: rigid and wells substrates with δ=5%, 7%, 8% for the pII orientation; wells substrates with δ=5%, 7%, 8% for the basal and pI orientations. (1) Construct the ice Ih orthorhombic unit cell at coexistence; (2) stretch/compress the three unit-cell edges by factor f to achieve each percent mismatch δ = 100·|f-1|; (3) replicate the deformed unit cell to form a slab; (4) melt a portion at 300 K to create a liquid layer adjacent to a frozen substrate region. Write LAMMPS input data files for each system.
- Evidence: `/app/outputs/preparation.log`

### Step 2: NVT molecular dynamics simulations of heterogeneous nucleation
- Role: process
- Action: For each substrate configuration, run LAMMPS NVT ensemble simulations at a range of supercooled temperatures using the mW water model, the Nosé–Hoover thermostat, and a 3 fs time step. Record potential energy time series. Identify induction times (t_ind) from the first sudden potential-energy drop associated with ice nucleation and growth. Repeat trajectories for each temperature to obtain an average induction time.
- Evidence: none

### Step 3: Nucleation rate calculation
- Role: process
- Action: For each system and temperature, compute the heterogeneous nucleation rate J = 1/(2 A t_ind), where A is the area of the substrate face exposed to the liquid (factor 2 accounts for two interfaces). Record the base-10 logarithm of J (in m^{-2}s^{-1}) for each temperature, forming J(T) curves for every combination of mismatch, substrate type, and orientation.
- Evidence: none

### Step 4: Nucleation temperature determination and reporting
- Role: scored (load-bearing)
- Action: For each substrate system, interpolate the J(T) curve to find the temperature T_n at which log10[J(m^{-2}s^{-1})] = 23.6. Compile a CSV file `nucleation_temperatures.csv` with columns: substrate_type (string: 'rigid' or 'wells'), orientation (string: 'basal', 'pI', or 'pII'), mismatch_delta (integer: 5, 7, or 8), T_n_K (float). The CSV must contain exactly 15 rows covering all combinations: rigid pII at δ=5,7,8; wells pII from flexibility at δ=5,7,8; wells basal at δ=5,7,8; wells pI at δ=5,7,8; wells pII from orientation at δ=5,7,8.
- Output file: `/app/outputs/nucleation_temperatures.csv`
- Format: csv
- Contract: CSV with columns: substrate_type (string: 'rigid'/'wells'), orientation (string: 'basal'/'pI'/'pII'), mismatch_delta (integer: 5,7,8), T_n_K (float). Must contain exactly 15 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_temperatures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_temperatures.csv
- path: `/app/outputs/nucleation_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV of heterogeneous nucleation temperatures T_n (defined at log J = 23.6 m^{-2}s^{-1}) for all studied substrate conditions. The checker will validate the 15-row structure, compare each T_n value against a hidden reference with tolerance, compute the linear slope dT_n/dδ from the pII data and check it lies in an expected range, and verify the ordering trends (wells > rigid; pI > pII > basal).
- schema:
  - `type`: table
  - `required_columns`: `substrate_type`, `orientation`, `mismatch_delta`, `T_n_K`
  - `columns`:
    - `substrate_type`: string
    - `orientation`: string
    - `mismatch_delta`: integer
    - `T_n_K`: float
  - `num_rows`: 15

Notes: The slope and trend checks are internal to the hidden checker and do not require separate output artifacts; the CSV alone suffices. The substrate area A, number of molecules, and system dimensions are not scored outputs but must be documented in the preparation log to confirm correct construction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "substrate_type",
          "orientation",
          "mismatch_delta",
          "T_n_K"
        ],
        "columns": {
          "substrate_type": "string",
          "orientation": "string",
          "mismatch_delta": "integer",
          "T_n_K": "float"
        },
        "num_rows": 15
      },
      "description": "CSV of heterogeneous nucleation temperatures T_n (defined at log J = 23.6 m^{-2}s^{-1}) for all studied substrate conditions. The checker will validate the 15-row structure, compare each T_n value against a hidden reference with tolerance, compute the linear slope dT_n/dδ from the pII data and check it lies in an expected range, and verify the ordering trends (wells > rigid; pI > pII > basal)."
    }
  ],
  "notes": "The slope and trend checks are internal to the hidden checker and do not require separate output artifacts; the CSV alone suffices. The substrate area A, number of molecules, and system dimensions are not scored outputs but must be documented in the preparation log to confirm correct construction."
}
```

## How you are scored
A hidden verifier reads your `nucleation_temperatures.csv` and checks that it contains exactly 15 rows with the correct columns. It then compares each T_n value against a hidden reference with an appropriate tolerance, computes the linear slope dT_n/dδ from the pII data for both rigid and wells substrates, and verifies that the relative ordering of T_n across substrate types (wells vs rigid) and across orientations (pI, pII, basal) follows the physically expected trends. You must run the full simulation pipeline honestly; the verifier's hidden reference values are precise and are not guessable from public information alone.
