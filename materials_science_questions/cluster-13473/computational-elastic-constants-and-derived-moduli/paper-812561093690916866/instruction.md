# MD Simulation of Functionalized Graphene/NBR Composites: Mechanical and Tribological Properties

## Problem background
Nitrile rubber (NBR) composites reinforced by graphene sheets (GNS) are promising candidates for high‑performance polymer nanocomposites due to their oil resistance and mechanical strength. However, pristine graphene tends to agglomerate in the polymer matrix, limiting its effectiveness. Functionalizing the graphene surface with polar groups such as hydroxyl (‑OH), carboxyl (‑COOH), or ester (‑COOCH₃) is expected to improve the dispersion and interfacial adhesion, leading to enhanced stiffness (Young’s modulus, shear modulus, bulk modulus) and improved tribological behaviour (lower coefficient of friction and abrasion rate). This task uses all‑atom molecular dynamics simulations to quantify these effects and to compare the relative performance of the four GNS/NBR composites.

## Approach
The approach employs classical molecular dynamics with a publicly available force field (e.g., OPLS‑AA or CHARMM). Four atomistic models are built: a periodic unit cell containing a single‑layer graphene sheet (pristine or with 32 uniformly distributed functional groups) embedded in an NBR matrix (20‑repeat‑unit chains, acrylonitrile:butadiene ratio 1:1, target density 0.97 g cm⁻³). The exact numbers of NBR chains per composite are taken from Table 1 of the reference paper: **20 chains** for PGNS/NBR (pristine), OH‑GNS/NBR, and COOH‑GNS/NBR, and **19 chains** for COOCH₃‑GNS/NBR. After geometry optimisation and equilibration (NVT then NPT at 298 K and 101 kPa), the mechanical properties are computed via the constant‑strain method: small strains are applied in the three Cartesian directions, the virial stress is obtained from the last 40 frames of a subsequent 200 ps NVT run, and the stiffness/compliance tensors yield directional Young’s moduli, as well as the Voigt‑Reuss‑Hill averaged shear and bulk moduli. Tribological performance is evaluated using a three‑layer friction model: a top Fe slab (0.28×0.28×1.71 nm³) slides over each composite under a controlled normal indentation while the bottom Fe slab (4.58×2.86×1.71 nm³) is fixed, and the coefficient of friction (ratio of lateral to normal force) and abrasion rate (fraction of NBR atoms that leave the matrix) are recorded. The workflow produces a single CSV file consolidating all computed quantities for the four composites.

## Reproduction target
Using an open‑source molecular dynamics engine, compute the following quantities for each of the four composites (pristine GNS/NBR, COOCH₃‑GNS/NBR, OH‑GNS/NBR, COOH‑GNS/NBR): directional Young’s moduli (E_X, E_Y, E_Z, average E_Avg), Voigt‑ and Reuss‑averaged shear moduli (G_V, G_R), Voigt‑ and Reuss‑averaged bulk moduli (B_V, B_R), the Hill‑averaged shear modulus (G_H), the Hill‑averaged bulk modulus (B_H), the coefficient of friction (COF), and the abrasion rate (AR). Report all values in a single CSV file named results.csv with one row per composite, using the composite names pristine, COOCH3, OH, and COOH. The target is to obtain these properties by faithfully executing the molecular dynamics protocol; the specific numerical results will be evaluated by the verifier based on internal consistency and hidden reference checks.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- Molecular mechanics force field for polymers and graphene (e.g., OPLS-AA, CHARMM)

## Workflow steps

### Step 1: Model construction and equilibration
- Role: process
- Action: Construct atomistic models of four composites: pristine GNS in NBR, and GNS functionalized with -COOCH3, -OH, -COOH groups in NBR. For each, build a periodic unit cell of size **4.5 × 3.0 × 3.0 nm³**. Place a single-layer graphene sheet (~3.92×2.41 nm², edge-hydrogenated, 32 functional groups per sheet for functionalized GNS) at the centre of the cell and pack NBR chains (20 repeat units, acrylonitrile:butadiene 1:1) to reach a target density of 0.97 g/cm³. The number of NBR chains must be: 20 for pristine, 20 for OH‑GNS/NBR, 20 for COOH‑GNS/NBR, and 19 for COOCH₃‑GNS/NBR. Perform geometry optimization (conjugate gradient, energy convergence 10⁻⁵ kcal/mol), then NVT equilibration (298 K, 1 ns) and NPT equilibration (298 K, 101 kPa, 1 ns) using the chosen force field. The pressure and temperature can be controlled with standard algorithms (e.g., Nosé‑Hoover or Berendsen).

### Step 2: Mechanical property calculation via constant-strain MD
- Role: process
- Action: For each equilibrated composite, run an additional NVT simulation at 298 K for 200 ps, sampling the last 40 snapshots. Apply the constant-strain method: impose small strains (max amplitude 0.003) in X, Y, Z directions (four levels each), relax internal coordinates, compute virial stress, build stiffness matrix C_ij and compliance matrix S_ij. Compute directional Young's moduli E_i, average E_Avg, and Voigt-Reuss-Hill averaged shear modulus G_H and bulk modulus B_H from the tensors.

### Step 3: Tribological simulation and COF/AR calculation
- Role: process
- Action: Construct three-layer friction models. Take the equilibrated composite model and extend the simulation box in the z‑direction to form a final box size of approximately **4.58 × 2.86 × 5.0 nm³**. Place the composite in the middle, a bottom Fe slab (**4.58 × 2.86 × 1.71 nm³**) at the bottom, and a top Fe slab (**0.28 × 0.28 × 1.71 nm³**) at the top. Perform energy minimization, then five‑cycle annealing (150–350 K, NVT, 200 ps per cycle). Subsequently, perform shear loading in the **NVT ensemble at 298 K**: fix the bottom Fe atoms, indent the top Fe slab by **0.03 nm**, and translate it laterally at **0.1 Å/ps** for **600 ps**. During the shear stage, maintain the temperature at 298 K using a thermostat. Compute coefficient of friction **COF = F_f / F_n**, where F_f is the time-averaged lateral force on the top Fe layer and F_n is the time-averaged normal force. Compute abrasion rate **AR** (in percent) as the percentage of NBR atoms that leave the matrix: an atom is considered to have left if its displacement from its initial position exceeds **0.5 nm**.

### Step 4: Collect and write results
- Role: scored (load-bearing)
- Action: Collect the computed mechanical and tribological properties for the four composites and write a CSV file containing all required values.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Columns: composite (string), E_X (float, GPa), E_Y (float, GPa), E_Z (float, GPa), E_Avg (float, GPa), G_R (float, GPa), G_V (float, GPa), G_H (float, GPa), B_R (float, GPa), B_V (float, GPa), B_H (float, GPa), COF (float), AR (float). One row per composite with composite names: pristine, COOCH3, OH, COOH.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing the computed mechanical moduli, coefficient of friction, and abrasion rate for each of the four composites: pristine, COOCH3, OH, COOH. The checker will verify basic sanity (all moduli positive, G_H in (0.1,10) GPa, COF in (0,1)) and consistency with the simulation protocol.
- schema:
  - `type`: table
  - `required_columns`: `composite`, `E_X`, `E_Y`, `E_Z`, `E_Avg`, `G_R`, `G_V`, `G_H`, `B_R`, `B_V`, `B_H`, `COF`, `AR`
  - `units`:
    - `E_X`: GPa
    - `E_Y`: GPa
    - `E_Z`: GPa
    - `E_Avg`: GPa
    - `G_R`: GPa
    - `G_V`: GPa
    - `G_H`: GPa
    - `B_R`: GPa
    - `B_V`: GPa
    - `B_H`: GPa
    - `COF`: dimensionless
    - `AR`: percentage

Notes: The task uses a public open-source force field instead of the proprietary COMPASS force field; therefore absolute numerical values may differ from the paper. All construction parameters (cell sizes, functionalization details, NBR chain length and numbers, simulation durations) are provided in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "composite",
          "E_X",
          "E_Y",
          "E_Z",
          "E_Avg",
          "G_R",
          "G_V",
          "G_H",
          "B_R",
          "B_V",
          "B_H",
          "COF",
          "AR"
        ],
        "units": {
          "E_X": "GPa",
          "E_Y": "GPa",
          "E_Z": "GPa",
          "E_Avg": "GPa",
          "G_R": "GPa",
          "G_V": "GPa",
          "G_H": "GPa",
          "B_R": "GPa",
          "B_V": "GPa",
          "B_H": "GPa",
          "COF": "dimensionless",
          "AR": "percentage"
        }
      },
      "description": "CSV file containing the computed mechanical moduli, coefficient of friction, and abrasion rate for each of the four composites: pristine, COOCH3, OH, COOH. The checker will verify basic sanity (all moduli positive, G_H in (0.1,10) GPa, COF in (0,1)) and consistency with the simulation protocol."
    }
  ],
  "notes": "The task uses a public open-source force field instead of the proprietary COMPASS force field; therefore absolute numerical values may differ from the paper. All construction parameters (cell sizes, functionalization details, NBR chain length and numbers, simulation durations) are provided in the instruction."
}
```