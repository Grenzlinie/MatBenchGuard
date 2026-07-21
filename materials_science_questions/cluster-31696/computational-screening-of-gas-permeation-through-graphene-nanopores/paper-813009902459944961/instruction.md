## Problem background

Two-dimensional membranes with sub-nanometer pores are promising for energy-efficient gas separation. Single-layer molybdenum disulfide (MoS2) filters with appropriately sized pores can exhibit high selectivity for gas pairs such as He/Ne and H2/He. An essential factor determining separation performance is the energy barrier a gas molecule must overcome to traverse a pore. Understanding and quantifying these barriers and the associated charge transfer is crucial for validating the proposed separation mechanism.

## Approach

We computationally evaluate the diffusion barriers and charge transfer for five gas species (He, Ne, H2, Ar, Kr) passing through the V_MoS6 pore in a MoS2 monolayer. The workflow uses density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and the optPBE van der Waals correction. The V_MoS6 pore is constructed by removing one Mo atom and three adjacent disulfur pairs (six S atoms) from a perfect MoS2 supercell, leaving an effective pore diameter of about 0.6 nm. The atomic positions are first relaxed. Then, for each gas, the minimum-energy path through the pore is obtained using the climbing-image nudged elastic band (CI-NEB) method, from which the diffusion barrier (energy difference between maximum and minimum along the path) is extracted. Additionally, Bader charge analysis is performed on a representative configuration (e.g., the molecule inside the pore) to quantify the net electron transfer from the gas to the MoS2 sheet.

## Reproduction target

Reproduce the diffusion energy barrier (in eV) and the net Bader charge loss (in electrons) for each of the five gases (He, Ne, H2, Ar, Kr) as they traverse the V_MoS6 nanopore. The final artifact is a CSV table with one row per gas containing the computed barrier and charge loss. The hidden verifier will evaluate the results against established reference values and check internal physical consistency, such as relative trends between gases, that are expected from the computational method.

## Assets

- **Open‑source DFT package** – e.g., Quantum ESPRESSO (https://www.quantum-espresso.org/) or equivalent plane‑wave DFT code supporting PBE, van der Waals corrections, and CI‑NEB.
- **Bader charge analysis tool** – the grid‑based Bader program from the Henkelman group (https://theory.cm.utexas.edu/henkelman/code/bader/) or equivalent, compatible with the charge density output of the chosen DFT code.
- **MoS2 monolayer structure** – the perfect MoS2 unit cell can be obtained from public databases such as the Materials Project (mp-2815) or constructed from standard lattice parameters (a ≈ 3.16 Å, space group P6̄m2). The agent must then manually introduce the V_MoS6 pore by removing one Mo atom and three adjacent disulfur pairs (six S atoms) as detailed in the workflow steps.

## Workflow steps

### Step 1: Construct V_MoS6 pore supercell
- Role: process
- Action: Build a periodic MoS2 supercell containing at least 108 atoms with a vacuum layer of at least 15 Å perpendicular to the sheet. Introduce the V_MoS6 pore by removing one Mo atom and three adjacent disulfur pairs (six S atoms), resulting in an effective pore diameter of approximately 0.6 nm. Save the atomic coordinates in a suitable format for the chosen DFT package.
- Evidence: `/app/outputs/pore_structure.xyz`

### Step 2: DFT geometry optimization of the pore
- Role: process
- Action: Using the chosen DFT package with PBE functional, optPBE van der Waals correction (or equivalent dispersion treatment), relax all atomic positions of the V_MoS6 supercell. Ensure a vacuum layer of at least 15 Å, converge forces tightly, and save the final relaxed coordinates.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 3: Compute diffusion barriers and Bader charges
- Role: scored (load-bearing)
- Action: For each of the five gas species (He, Ne, H2, Ar, Kr), set up a CI-NEB calculation using the same DFT functional. The initial and final states place the gas at least 15 Å above and below the MoS2 plane, respectively, with a linear interpolation as the initial path. Converge the band to a minimum-energy path and extract the diffusion barrier as the energy difference between the maximum and minimum along the path. For each gas, perform Bader charge analysis on a representative configuration where the molecule is located at the pore center (or the energy minimum inside the pore) and compute the net number of electrons lost from the gas to the MoS2 sheet. Collect all results in a single CSV file.
- Output file: `/app/outputs/diffusion_barriers_and_bader.csv`
- Format: csv
- Contract: Columns: `gas` (string, one of He, Ne, H2, Ar, Kr), `diffusion_barrier_eV` (floating-point number, in eV), `bader_charge_loss_e` (floating-point number, in elementary charge). One row per gas.
- Scoring: scored by hidden verifier

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diffusion_barriers_and_bader.csv
- path: `/app/outputs/diffusion_barriers_and_bader.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed diffusion barriers (eV) and Bader charge loss (e) for He, Ne, H2, Ar, Kr through the V_MoS6 nanopore.
- schema:
  - `type`: table
  - `required_columns`: `gas`, `diffusion_barrier_eV`, `bader_charge_loss_e`
  - `units`:
    - `diffusion_barrier_eV`: eV
    - `bader_charge_loss_e`: e

Notes: The verifier compares each value to reference data within defined tolerances and checks required relative trends among gases. No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diffusion_barriers_and_bader.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gas",
          "diffusion_barrier_eV",
          "bader_charge_loss_e"
        ],
        "units": {
          "diffusion_barrier_eV": "eV",
          "bader_charge_loss_e": "e"
        }
      },
      "description": "Computed diffusion barriers (eV) and Bader charge loss (e) for He, Ne, H2, Ar, Kr through the V_MoS6 nanopore."
    }
  ],
  "notes": "The verifier compares each value to reference data within defined tolerances and checks required relative trends among gases. No gold values are disclosed here."
}
```

## How you are scored

A hidden verifier independently reads your `diffusion_barriers_and_bader.csv` and compares the computed barriers and charge losses to reference values with defined tolerances. It also checks that the relative ordering and trends among gases are physically consistent with the computational method. Each condition carries a weight, and the final reward is a weighted sum. Simply reporting numbers from the literature without executing the DFT workflow will not satisfy the verification checks.
