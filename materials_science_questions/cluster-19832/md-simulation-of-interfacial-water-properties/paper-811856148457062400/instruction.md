# Reproduce Voltage Generation in Water-Filled SWCNT via MD and DFT

## Problem background
Water molecules confined inside a single-walled carbon nanotube (SWCNT) can form an oriented dipole chain. The interaction between the water dipoles and the charge carriers in the nanotube can induce electron redistribution, potentially generating a voltage across the tube ends. This task quantifies this effect by computing the resulting electrostatic potential difference and the charge redistribution on the nanotube using a combined molecular dynamics and density functional theory approach.

## Approach
The overall approach is to first simulate the filling of an uncapped (6,6) armchair SWCNT with water molecules at room temperature using classical MD, applying a driving force to mimic osmotic pressure, until a stable single-file water chain forms inside the tube. Then, a representative configuration of the system (nanotube and the confined and near-entrance water molecules) is used for an electronic structure calculation with DFT (B3LYP functional, 6-31G** basis set). Partial atomic charges are computed using the CHELPG scheme, from which the total charges on the left and right ends of the tube are determined, and the electrostatic potential difference between the two ends is evaluated via the Coulomb integral over the charge distribution. This method allows computation of the terminal voltage and the end charges from first principles.

## Reproduction target
Run the MD simulation to obtain a water-filled SWCNT configuration; perform a DFT calculation on that configuration using B3LYP/6-31G**; compute the CHELPG charges; then calculate the total charges Q_left and Q_right (in elementary charge e) and the electrostatic potential difference ΔU (in mV) between the two tube ends. Write the results to `/app/outputs/dft_results.json` as a JSON object with keys `delta_U_mV`, `Q_left_e`, and `Q_right_e`.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- Open-source electronic structure code (e.g., PySCF, ORCA, NWChem): https://pyscf.org
- TIP4P water model parameters
- (6,6) armchair SWCNT geometry

## Workflow steps

### Step 1: MD simulation of water filling in uncharged SWCNT
- Role: process
- Action: Run a LAMMPS simulation of an uncapped armchair (6,6) SWCNT (length ~12.3 Å, diameter ~8.14 Å) with TIP4P water at 300 K. Apply a constant force to bulk water to simulate osmotic pressure, pushing water into the tube. Run for 10 ns with a 1 fs timestep to obtain the equilibrium single-file water chain trajectory.
- Evidence: `/app/outputs/md_log.txt`

### Step 2: Extract representative DFT configuration
- Role: process
- Action: From the MD trajectory, select at least one instantaneous configuration that includes the SWCNT and all confined and near-entrance water molecules. Save the atomic coordinates in a format suitable for DFT input (e.g., .xyz or Gaussian input file).
- Evidence: `/app/outputs/config.xyz`

### Step 3: DFT calculation and terminal voltage computation
- Role: scored (load-bearing)
- Action: Perform a DFT calculation on the extracted water-filled CNT configuration using the B3LYP functional and 6-31G** basis set with tight SCF convergence. Compute partial atomic charges via the CHELPG scheme. From the CHELPG charges, compute the total charges on the leftmost and rightmost tube ends (Q_left, Q_right in e) by axial averaging, and calculate the electrostatic potential difference ΔU = U_right - U_left (in mV) using the Coulomb integral over the charge distribution. Write the results to dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: JSON object with keys 'delta_U_mV' (number), 'Q_left_e' (number), 'Q_right_e' (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the DFT-derived terminal voltage difference and end charges.
- schema:
  - `type`: object
  - `required`: `delta_U_mV`, `Q_left_e`, `Q_right_e`
  - `description`: Terminal voltage in mV between tube ends and total CHELPG charges on left and right ends in units of elementary charge.

Notes: No gold values or tolerances are exposed. The hidden checker compares the submitted values against paper-reported reference values with appropriate tolerances and verifies the polarity (Q_left_e > 0, Q_right_e < 0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_U_mV",
          "Q_left_e",
          "Q_right_e"
        ],
        "description": "Terminal voltage in mV between tube ends and total CHELPG charges on left and right ends in units of elementary charge."
      },
      "description": "Scored artifact containing the DFT-derived terminal voltage difference and end charges."
    }
  ],
  "notes": "No gold values or tolerances are exposed. The hidden checker compares the submitted values against paper-reported reference values with appropriate tolerances and verifies the polarity (Q_left_e > 0, Q_right_e < 0)."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/dft_results.json` and compares the submitted values against hidden reference results with tolerances that account for differences in DFT implementation and numerical settings. The verifier also checks that the computed end charges have the correct polarity relative to the water dipole orientation. The final reward (between 0 and 1) combines these criteria. Reporting the reference numbers without genuinely running the pipeline will not pass because the tolerances are chosen to accept legitimate toolchain variation but not arbitrary guesses.
