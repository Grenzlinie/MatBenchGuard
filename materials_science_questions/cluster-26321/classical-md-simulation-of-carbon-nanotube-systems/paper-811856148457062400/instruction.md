# MD/DFT Simulation of Hydroelectric Voltage in Water-Filled SWCNT

## Problem background
Nanoscale power cells and energy harvesting devices have attracted attention for powering tiny wireless or implantable systems without batteries. Single-walled carbon nanotubes (SWCNTs) filled with polar liquids, particularly water, have been proposed as a means to generate hydroelectric voltage via coupling between water dipoles and charge carriers in the tube. However, the quantitative charge redistribution and terminal voltage produced by this effect need to be established through first-principles simulation. This task addresses the computation of the terminal voltage across a water-filled (6,6) SWCNT from a combined molecular dynamics and density functional theory pipeline.

## Approach
The computational pipeline combines two complementary simulation techniques. First, molecular dynamics (MD) with the TIP4P water model simulates the filling of an uncapped armchair (6,6) SWCNT of length 12.3 Å and diameter 8.14 Å. A constant force on bulk water outside the tube mimics an osmotic pressure, driving water molecules into the nanotube to form a single-file chain. From the MD trajectory, several representative instantaneous configurations (including the tube, confined water, and near-entrance water) are extracted. Second, density functional theory (DFT) at the B3LYP/6-31G** level (with tight SCF convergence) is used on each configuration to compute partial charges via the CHELPG scheme. Finally, from the CHELPG charges and atomic coordinates, the axial-averaged total charges on the left and right halves of the tube are computed, and the electrostatic potential difference between the two ends (the terminal voltage) is evaluated via Coulomb’s law in a point-charge approximation. Averaging over the configurations yields the reported quantities.

## Reproduction target
Produce the computed terminal voltage ΔU and the axial‑averaged total charges Q_left and Q_right for the water‑filled (6,6) SWCNT by running the complete MD→DFT pipeline. Specifically, output (1) a CSV file containing the CHELPG partial charges for all atoms in each of the four extracted configurations (columns: config_id, atom_index, element, x, y, z, charge) and (2) a JSON file reporting the terminal voltage in mV and the end charges in elementary charge. The values must be physically plausible and self-consistent with the charges in the CSV.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- TIP4P water model force field
- Open-source DFT code supporting B3LYP/6-31G** and CHELPG charges (e.g., PySCF, ORCA, Psi4): https://py.scf.org or https://orcaforum.kofo.mpg.de/
- SWCNT geometry generator (e.g., LAMMPS nanotube builder or equivalent script)

## Workflow steps

### Step 1: Build SWCNT and MD simulation setup
- Role: process
- Action: Construct the (6,6) SWCNT (length 12.3 Å, diameter 8.14 Å) and a water reservoir with TIP4P water; set up LAMMPS simulation with a constant force on bulk water to simulate osmotic pressure.
- Evidence: none

### Step 2: Run MD water filling simulation
- Role: process
- Action: Execute MD simulation at 300 K for 10 ns (1.0 fs time step) using LAMMPS to produce atomic trajectories; extract four representative instantaneous configurations that include the SWCNT, confined water, and near-entrance water molecules.
- Evidence: none

### Step 3: DFT calculation of CHELPG partial charges
- Role: scored (load-bearing)
- Action: For each of the four configurations, run DFT (B3LYP/6-31G** with tight SCF convergence) using an open-source code (e.g., PySCF, ORCA) and compute CHELPG partial charges for all atoms. Save the charges, coordinates, config_id, and element to a CSV.
- Output file: `/app/outputs/cheLPG_charges.csv`
- Format: csv
- Contract: CSV with columns: config_id (int), atom_index (int), element (str), x (float, Å), y (float, Å), z (float, Å), charge (float, e). Contains data for four configurations (config_id 1–4).
- Scoring: scored by hidden verifier

### Step 4: Compute terminal voltage and axial charges
- Role: scored
- Action: Using the CHELPG charges and atomic coordinates from the four configurations, compute the axial-averaged total charges on the left and right tube ends and the electrostatic potential at both ends via Coulomb's law (point-charge approximation). Average over configurations to obtain Q_left, Q_right, and ΔU. Report as JSON.
- Output file: `/app/outputs/terminal_voltage.json`
- Format: json
- Contract: JSON object with keys: delta_U_mV (float, in mV), Q_left_e (float, in elementary charge), Q_right_e (float, in e), description (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cheLPG_charges.csv`
- `/app/outputs/terminal_voltage.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cheLPG_charges.csv
- path: `/app/outputs/cheLPG_charges.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CHELPG partial charges for all atoms in four instantaneous configurations (config_id 1–4). Columns: config_id int, atom_index int, element string, x/y/z float in Å, charge float in elementary charge e.
- schema:
  - `type`: table
  - `required_columns`: `config_id`, `atom_index`, `element`, `x`, `y`, `z`, `charge`
  - `units`:
    - `x`: Å
    - `y`: Å
    - `z`: Å
    - `charge`: e

### terminal_voltage.json
- path: `/app/outputs/terminal_voltage.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reported terminal voltage (ΔU in mV) and axial-averaged total charges on left and right tube ends (in elementary charge), averaged over the four configurations.
- schema:
  - `type`: object
  - `required`:
    - `delta_U_mV`: float
    - `Q_left_e`: float
    - `Q_right_e`: float
    - `description`: string
  - `units`:
    - `delta_U_mV`: mV
    - `Q_left_e`: e
    - `Q_right_e`: e

Notes: The derived values should be self-consistent with the cheLPG_charges.csv; the checker will verify internal consistency and compare reported values to a hidden reference within tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cheLPG_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "config_id",
          "atom_index",
          "element",
          "x",
          "y",
          "z",
          "charge"
        ],
        "units": {
          "x": "Å",
          "y": "Å",
          "z": "Å",
          "charge": "e"
        }
      },
      "description": "CHELPG partial charges for all atoms in four instantaneous configurations (config_id 1–4). Columns: config_id int, atom_index int, element string, x/y/z float in Å, charge float in elementary charge e."
    },
    {
      "file": "terminal_voltage.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_U_mV": "float",
          "Q_left_e": "float",
          "Q_right_e": "float",
          "description": "string"
        },
        "units": {
          "delta_U_mV": "mV",
          "Q_left_e": "e",
          "Q_right_e": "e"
        }
      },
      "description": "Reported terminal voltage (ΔU in mV) and axial-averaged total charges on left and right tube ends (in elementary charge), averaged over the four configurations."
    }
  ],
  "notes": "The derived values should be self-consistent with the cheLPG_charges.csv; the checker will verify internal consistency and compare reported values to a hidden reference within tolerances."
}
```

## How you are scored
A hidden verifier will score your outputs as follows:
- The `cheLPG_charges.csv` will be checked for valid structure, correct column types, and that it contains exactly four configurations. The verifier will recompute axial‑averaged total charges from the CSV and compare them with those reported in `terminal_voltage.json` for internal consistency.
- The `terminal_voltage.json` will be scored by comparing the reported `delta_U_mV`, `Q_left_e`, and `Q_right_e` to a hidden reference (derived from the expected methodology) using appropriate tolerances that account for differences in DFT codes, pseudopotentials/basis sets, and sampling.

The final reward is a weighted combination of these scores; producing the required outputs through the actual MD/DFT computation is necessary to hit the tolerances. Simply reporting numbers without executing the pipeline will not suffice.
