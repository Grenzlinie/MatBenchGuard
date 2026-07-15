# MD Simulation of Drug Diffusion in Functionalized BNNTs

## Problem background
Molecular dynamics (MD) simulation is used to study a drug delivery system based on boron nitride nanotubes (BNNTs). The goal is to understand the diffusion behavior of water and the anticancer drug carboplatin inside both pristine and hydroxyl‑functionalized BNNTs, and to evaluate the encapsulation of multiple drug molecules within the functionalized tube. The key quantities to compute are the self-diffusion coefficients of water and carboplatin, and the van der Waals interaction energies between the drug and the nanotube inner surface at different drug loadings. These quantities inform the viability of BNNTs as nanocarriers.

## Approach
The method uses classical MD with a combination of force fields: DREIDING parameters for boron atoms in BNNT, and the General AMBER Force Field (GAFF) for the remaining atoms. Partial charges are derived from density functional theory (DFT) optimizations at the B3LYP/3-21G level and restrained electrostatic potential (RESP) fitting at HF/6-31G** for the nanotube models, and similarly for the drug. A zigzag (18,0) BNNT (14 Å diameter, 40 Å length) is constructed in both pristine form and a hydroxyl‑functionalized variant bearing 18 –OH groups on one boron edge. Carboplatin models are built from its known crystal structure. For the diffusion study, a single drug molecule is initially placed near the tube entrance; for encapsulation, 1–5 drug molecules are placed inside the functionalized BNNT. All systems are solvated with TIP3P water. After energy minimization, heating, and equilibration, production MD simulations are run in the NPT ensemble with a Langevin thermostat and barostat. Self-diffusion coefficients are obtained from the slope of the mean-square displacement (MSD) in the axial direction, using Fickian diffusion D = (1/6) slope. Per-drug van der Waals and electrostatic interaction energies with the inner surface are averaged over the production trajectory.

## Reproduction target
Compute and report, as CSV files, the following:

1. For the pristine and functionalized BNNT systems with one drug outside and water present:
   - Self-diffusion coefficient (units 10⁻⁵ cm² s⁻¹) of water (labels: WAT_BNNT, WAT_FBNNT)
   - Self-diffusion coefficient of carboplatin (labels: Drug_BNNT, Drug_FBNNT, averaged over 10 independent replicas)

2. For the functionalized BNNT systems containing 1 to 5 carboplatin molecules inside:
   - Per-drug van der Waals interaction energy (kcal mol⁻¹) between all drug molecules and the inner surface
   - Per-drug electrostatic interaction energy (kcal mol⁻¹)

Write the diffusion results to `diffusion_coefficients.csv` and the energy results to `vdw_energies.csv`, following the format specified in the output contract. The target is the production of these computed quantities themselves; you do not need to match a particular figure or table from any external source.

## Assets

- Carboplatin PDB structure (entry QPT): https://www.rcsb.org/structure/QPT
- General AMBER Force Field (GAFF): AmberTools
- DREIDING force field parameters for boron: 10.1021/j100389a010
- Molecular dynamics engine (AMBER12 or equivalent)
- TIP3P water model
- Quantum chemistry code (GAMESS or equivalent)

## Workflow steps

### Step 1: BNNT model construction and RESP charge derivation
- Role: process
- Action: Build the pristine zigzag (18,0) BNNT (14 Å diameter, 40 Å length) and the hydroxyl‑functionalized BNNT (18 —OH groups on one B‑edge, H‑termination on the other edge). Optimize geometries at B3LYP/3‑21G level of theory using a quantum chemistry code. Derive restrained electrostatic potential (RESP) partial charges at HF/6‑31G** level. Save the resulting charges for B, N, O, H(N), H(O), H(B) to a file.
- Evidence: `/app/outputs/bnnt_charges.json`

### Step 2: Carboplatin model preparation
- Role: process
- Action: Obtain the carboplatin structure from PDB entry QPT. Assign GAFF atom types and bonded parameters. Compute RESP partial charges using the RESP module of AmberTools (or equivalent). Prepare topology and coordinate files for MD.
- Evidence: `/app/outputs/carboplatin.top`

### Step 3: System construction and solvation
- Role: process
- Action: Assemble six simulation systems: (i) drug_BNNT – one carboplatin placed 10 Å from the pristine BNNT entrance; (ii) 1‑ to 5‑drug_FBNNT – functionalized BNNT with 1 to 5 carboplatin molecules inside, with equivalent spacing. Solvate each system with ~7544 TIP3P water molecules in an octagonal box extending 12 Å from the solute surface. Generate combined topology and coordinate files for MD.
- Evidence: `/app/outputs/systems.tar`

### Step 4: MD production simulations
- Role: process
- Action: For each of the six systems, perform energy minimization (5000 steps of solvent relaxation + 5000 steps of solute relaxation), heat from 0 K to 300 K over 120 ps, NPT equilibration at 300 K and 1 atm for 200 ps, and a 10 ns production run with a 2 fs time step saving coordinates every 1 ps. Use Langevin thermostat/barostat, SHAKE on bonds containing hydrogen, particle mesh Ewald for electrostatics, 12 Å nonbonded cutoff. For drug_BNNT and 1‑drug_FBNNT, run at least 10 independent replicas using different initial velocities.
- Evidence: `/app/outputs/trajectories`

### Step 5: Diffusion coefficient calculation
- Role: scored (load-bearing)
- Action: From the trajectories of water inside drug_BNNT and 1‑drug_FBNNT, compute the mean‑square displacement (MSD) in the direction of the tube axis. From the 10 replicas of drug_BNNT and 1‑drug_FBNNT, compute the MSD of carboplatin and average over replicas. Fit the linear region of each MSD versus time curve; calculate the diffusion coefficient D = (1/6) × slope. Write the results to diffusion_coefficients.csv with columns: system (str), D (float, units 10⁻⁵ cm² s⁻¹). Systems: WAT_BNNT, WAT_FBNNT, Drug_BNNT, Drug_FBNNT.
- Output file: `/app/outputs/diffusion_coefficients.csv`
- Format: csv
- Contract: CSV with columns: system (str), D (float, units 10⁻⁵ cm² s⁻¹). Systems: WAT_BNNT, WAT_FBNNT, Drug_BNNT, Drug_FBNNT.
- Scoring: scored by hidden verifier

### Step 6: Non‑bonded interaction energy calculation
- Role: scored
- Action: From the trajectories of the five functionalized BNNT systems (1‑ to 5‑drug_FBNNT), compute the van der Waals and electrostatic interaction energies between all carboplatin molecules and the BNNT inner surface. Average the values per drug molecule over the entire production run. Write the results to vdw_energies.csv with columns: system (str, e.g. 1‑Drug_FBNNT), vdw_per_drug (float, kcal mol⁻¹), ele_per_drug (float, kcal mol⁻¹).
- Output file: `/app/outputs/vdw_energies.csv`
- Format: csv
- Contract: CSV with columns: system (str, e.g. 1‑Drug_FBNNT), vdw_per_drug (float, kcal mol⁻¹), ele_per_drug (float, kcal mol⁻¹). Five rows corresponding to drug numbers 1–5.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/diffusion_coefficients.csv`
- `/app/outputs/vdw_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diffusion_coefficients.csv
- path: `/app/outputs/diffusion_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Self‑diffusion coefficients of water and carboplatin inside pristine and functionalized BNNT. The values will be compared to hidden paper‑reported references within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `system`, `D`
  - `units`:
    - `D`: 10⁻⁵ cm² s⁻¹
  - `description`: Each row corresponds to one system (WAT_BNNT, WAT_FBNNT, Drug_BNNT, Drug_FBNNT) with its diffusion coefficient.

### vdw_energies.csv
- path: `/app/outputs/vdw_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per‑drug non‑bonded interaction energies between carboplatin and the functionalized BNNT inner surface at different drug loadings. Values will be compared to hidden paper‑reported references within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `system`, `vdw_per_drug`, `ele_per_drug`
  - `units`:
    - `vdw_per_drug`: kcal mol⁻¹
    - `ele_per_drug`: kcal mol⁻¹
  - `description`: Five rows (1‑Drug_FBNNT … 5‑Drug_FBNNT) with van der Waals and electrostatic energies per drug molecule. The system column contains the system name.

Notes: Only the reported diffusion coefficients and energies are scored; raw MD trajectories are not required as scored artifacts. The checker compares the agent's reported values to hidden paper‑reported target values with appropriate tolerances and also verifies the trend (higher diffusion in FBNNT).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diffusion_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "D"
        ],
        "units": {
          "D": "10⁻⁵ cm² s⁻¹"
        },
        "description": "Each row corresponds to one system (WAT_BNNT, WAT_FBNNT, Drug_BNNT, Drug_FBNNT) with its diffusion coefficient."
      },
      "description": "Self‑diffusion coefficients of water and carboplatin inside pristine and functionalized BNNT. The values will be compared to hidden paper‑reported references within tolerance."
    },
    {
      "file": "vdw_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "vdw_per_drug",
          "ele_per_drug"
        ],
        "units": {
          "vdw_per_drug": "kcal mol⁻¹",
          "ele_per_drug": "kcal mol⁻¹"
        },
        "description": "Five rows (1‑Drug_FBNNT … 5‑Drug_FBNNT) with van der Waals and electrostatic energies per drug molecule. The system column contains the system name."
      },
      "description": "Per‑drug non‑bonded interaction energies between carboplatin and the functionalized BNNT inner surface at different drug loadings. Values will be compared to hidden paper‑reported references within tolerance."
    }
  ],
  "notes": "Only the reported diffusion coefficients and energies are scored; raw MD trajectories are not required as scored artifacts. The checker compares the agent's reported values to hidden paper‑reported target values with appropriate tolerances and also verifies the trend (higher diffusion in FBNNT)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects each scored output file. For `diffusion_coefficients.csv`, the verifier compares your reported diffusion coefficients to a set of hidden reference values derived from the study's reported measurements, using a relative tolerance. It also checks that the diffusion in FBNNT is higher than in pristine BNNT for both water and carboplatin (a required trend). For `vdw_energies.csv`, the per-drug van der Waals energies are similarly compared to hidden reference values within a tolerance, and the trend across drug loadings is verified. The verifier does not require bit-identical agreement—small deviations due to implementation differences are accommodated. The final reward is a weighted combination of these checks; meeting the reference within tolerance and showing the correct trend earns full credit. Simply reporting a number without executing the workflow is insufficient because the hidden reference is not provided to you and the trend must arise from your computed data.
