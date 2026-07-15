# Dislocation-Mediated bcc-hcp Transformation in Beryllium

## Problem background
The bcc-to-hcp martensitic transformation in beryllium is of fundamental interest for understanding material response at extreme pressures. The Burgers mechanism describes a shear-plus-shuffle pathway that transforms the bcc lattice into hcp. However, the energetic barrier along this path may be high, and the transformation under pure pressure may not occur spontaneously at the thermodynamic transition pressure. Screw dislocations could provide local shear strains that facilitate the transformation, lower the barrier, and lead to variant selection and hysteresis. This task examines these hypotheses using first-principles calculations.

## Approach
Using density functional theory (DFT) with the ABINIT package and the PBE exchange-correlation functional, we compute the energy landscape of the Burgers transformation path. First, in a defect-free bcc crystal, the total energy is minimized with respect to the shuffle order parameter η for a range of shear order parameter s to obtain the minimum energy path (MEP) at three constant volumes (lattice parameters a0 = 3.592, 3.786, 4.110 bohrs). Then, a 540-atom supercell is constructed containing a quadrupolar arrangement of screw dislocations with Burgers vector ±½[111]. The supercell is relaxed, and two types of transformations are simulated: (i) shear-induced transformation at constant volume by applying the Burgers shear and relaxing atomic positions, and (ii) pressure-induced transformation by varying the lattice parameter and relaxing at each volume, going forward and reverse to capture hysteresis. Structure identification (bcc, hcp, or mixed) is performed via adaptive common neighbor analysis or equivalent.

## Reproduction target
Produce a CSV file (dislocation_free_MEP.csv) containing the MEP data for the three lattice parameters, a CSV file (shear_transformation_energy.csv) containing shear-induced transformation data with dislocations, and a CSV file (pressure_volume_hysteresis.csv) containing pressure-volume data for a full forward-reverse cycle. The hidden verifier will check that the dislocation-free MEP barriers decrease with increasing lattice parameter, that the shear-induced transformation with dislocations occurs at a lower shear than in the dislocation-free case, and that the pressure-volume curve exhibits a hysteresis loop with forward and reverse transition pressures within expected ranges.

## Assets

- ABINIT: https://www.abinit.org/download
- JTH PAW pseudopotentials for Be: https://www.abinit.org/downloads/PAW2
- OVITO: https://www.ovito.org/

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct a non-orthogonal supercell containing a quadrupolar arrangement of ±½[111] screw dislocations in bcc Be using the Bravais vectors defined in the paper with integer parameters m=30, n=18, giving a 540-atom supercell. Generate the initial atomic positions in the bcc structure with the inserted dislocation dipole. Output a supercell configuration file suitable for ABINIT input.
- Evidence: `/app/outputs/supercell_input.in`

### Step 2: Relax bcc screw dislocation dipole
- Role: process
- Action: Perform DFT ionic relaxation of the constructed 540-atom supercell using ABINIT with PBE functional, plane-wave cutoff 20 Ha, 1×1×16 k-point grid, and the JTH Be PAW potential. Converge forces to <5×10⁻⁴ Ha/bohr. This yields the relaxed atomic positions for the bcc phase containing a locally relaxed screw dislocation dipole.
- Evidence: `/app/outputs/relaxed_bcc_positions.xsf`

### Step 3: Dislocation-free MEP calculation
- Role: scored (load-bearing)
- Action: For each lattice parameter a0 = 3.592, 3.786, 4.110 bohrs, use a conventional 2-atom bcc cell and apply the tensorial Burgers transformation interpolation (shear s and shuffle η) with ideal c/a=√(8/3). For a grid of s ∈ [0,1], minimize the total energy with respect to η using ABINIT relaxations. Record the optimized η and the corresponding energy (relative to bcc), pressure, and von Mises stress along the MEP.
- Output file: `/app/outputs/dislocation_free_MEP.csv`
- Format: csv
- Contract: columns: a0 (float), s (float), eta (float), energy_meV_per_atom (float), pressure_GPa (float), von_Mises_stress_GPa (float)
- Scoring: scored by hidden verifier

### Step 4: Shear-induced transformation with dislocations
- Role: scored
- Action: Take the relaxed bcc supercell from step_1 at a0=3.592 bohrs. Apply a stepwise global shear deformation (s from 0 to 1) on the (1-10) plane at constant volume using the Burgers interpolation. For each s, relax all ionic positions with ABINIT. After each relaxation, record the total energy, pressure, and the fraction of atoms identified as hcp via an appropriate structure analysis (e.g., adaptive common neighbor analysis).
- Output file: `/app/outputs/shear_transformation_energy.csv`
- Format: csv
- Contract: columns: s (float), total_energy_eV (float), pressure_GPa (float), hcp_fraction (float)
- Scoring: scored by hidden verifier

### Step 5: Pressure-induced transformation with dislocations
- Role: scored
- Action: Starting from the relaxed bcc supercell from step_1 at a0=3.592 bohrs, simulate the pressure-induced transformation by varying the lattice parameter a0 from 3.592 to 4.740 bohrs in steps (forward) and then back to 3.592 bohrs (reverse). At each volume, fully relax ionic positions with ABINIT. Record the pressure and label the overall phase (bcc, hcp, or mixed) based on local structure analysis.
- Output file: `/app/outputs/pressure_volume_hysteresis.csv`
- Format: csv
- Contract: columns: volume_bohr3_per_atom (float), pressure_GPa (float), phase_label (string: 'bcc', 'hcp', or 'mixed')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dislocation_free_MEP.csv`
- `/app/outputs/shear_transformation_energy.csv`
- `/app/outputs/pressure_volume_hysteresis.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dislocation_free_MEP.csv
- path: `/app/outputs/dislocation_free_MEP.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Minimum-energy path data for the dislocation-free bcc-to-hcp transformation at three lattice parameters. The checker will recompute the energy barrier and verify its magnitude, trend, and maximum shift against a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `a0`, `s`, `eta`, `energy_meV_per_atom`, `pressure_GPa`, `von_Mises_stress_GPa`
  - `units`:
    - `a0`: bohr
    - `s`: dimensionless
    - `eta`: dimensionless
    - `energy_meV_per_atom`: meV/atom
    - `pressure_GPa`: GPa
    - `von_Mises_stress_GPa`: GPa

### shear_transformation_energy.csv
- path: `/app/outputs/shear_transformation_energy.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Stepwise shear-induced transformation data with dislocations. The checker will verify that hcp nucleation occurs at a shear value lower than the dislocation-free case, with hcp_fraction > 0.1 for s < 0.27.
- schema:
  - `type`: table
  - `required_columns`: `s`, `total_energy_eV`, `pressure_GPa`, `hcp_fraction`
  - `units`:
    - `s`: dimensionless
    - `total_energy_eV`: eV
    - `pressure_GPa`: GPa
    - `hcp_fraction`: dimensionless (0-1)

### pressure_volume_hysteresis.csv
- path: `/app/outputs/pressure_volume_hysteresis.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Pressure-volume hysteresis data for the pressure-induced transformation cycle with dislocations. The checker will verify forward transformation onset pressure between 80-100 GPa and reverse onset between 110-130 GPa.
- schema:
  - `type`: table
  - `required_columns`: `volume_bohr3_per_atom`, `pressure_GPa`, `phase_label`
  - `units`:
    - `volume_bohr3_per_atom`: bohr^3/atom
    - `pressure_GPa`: GPa
    - `phase_label`: string ('bcc', 'hcp', or 'mixed')

Notes: The dislocation-free MEP data must cover a0 = 3.592, 3.786, 4.110 bohrs. The shear transformation data is for forward direction only at a0=3.592 bohrs. The pressure hysteresis covers a full forward-reverse cycle.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dislocation_free_MEP.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0",
          "s",
          "eta",
          "energy_meV_per_atom",
          "pressure_GPa",
          "von_Mises_stress_GPa"
        ],
        "units": {
          "a0": "bohr",
          "s": "dimensionless",
          "eta": "dimensionless",
          "energy_meV_per_atom": "meV/atom",
          "pressure_GPa": "GPa",
          "von_Mises_stress_GPa": "GPa"
        }
      },
      "description": "Minimum-energy path data for the dislocation-free bcc-to-hcp transformation at three lattice parameters. The checker will recompute the energy barrier and verify its magnitude, trend, and maximum shift against a hidden reference."
    },
    {
      "file": "shear_transformation_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "total_energy_eV",
          "pressure_GPa",
          "hcp_fraction"
        ],
        "units": {
          "s": "dimensionless",
          "total_energy_eV": "eV",
          "pressure_GPa": "GPa",
          "hcp_fraction": "dimensionless (0-1)"
        }
      },
      "description": "Stepwise shear-induced transformation data with dislocations. The checker will verify that hcp nucleation occurs at a shear value lower than the dislocation-free case, with hcp_fraction > 0.1 for s < 0.27."
    },
    {
      "file": "pressure_volume_hysteresis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume_bohr3_per_atom",
          "pressure_GPa",
          "phase_label"
        ],
        "units": {
          "volume_bohr3_per_atom": "bohr^3/atom",
          "pressure_GPa": "GPa",
          "phase_label": "string ('bcc', 'hcp', or 'mixed')"
        }
      },
      "description": "Pressure-volume hysteresis data for the pressure-induced transformation cycle with dislocations. The checker will verify forward transformation onset pressure between 80-100 GPa and reverse onset between 110-130 GPa."
    }
  ],
  "notes": "The dislocation-free MEP data must cover a0 = 3.592, 3.786, 4.110 bohrs. The shear transformation data is for forward direction only at a0=3.592 bohrs. The pressure hysteresis covers a full forward-reverse cycle."
}
```

## How you are scored
Each of the three scored output files will be independently evaluated by a hidden checker. The checker will parse the CSVs and compare the contained data to reference criteria (e.g., the presence of a hysteresis loop, relative ordering of barriers, or threshold exceedance). Each stage contributes a weighted fraction to the final reward, which is a float between 0 and 1. Producing files that satisfy the trends and thresholds outlined in the output contract yields the maximum reward. Note that reporting the paper's numbers alone is insufficient; the artifacts must be generated through the prescribed workflow.
