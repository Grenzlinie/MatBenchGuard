# Lattice distortion and equivalent strain prediction in equimolar complex alloys

## Problem background
Chemically disordered equimolar complex alloys, often called high-entropy alloys, can exhibit atomic-scale lattice distortion that influences their mechanical properties. Mixing elements of different sizes introduces local residual strains, but a quantitative understanding of the overall lattice distortion in a random solid solution is challenging because there is no clear distinction between solvent and solute. This task focuses on a series of Fe–Co–Ni–Cr–Mn face-centred cubic (FCC) alloys. Using first-principles density functional theory (DFT) and analytical modelling, we aim to characterize the magnitude of the atomic-scale lattice distortion and to test whether a simple geometric-elastic model can predict the average lattice strain and the resulting lattice constants.

## Approach
The reproduction proceeds in two linked routes: a DFT route that directly simulates the alloys and extracts the lattice distortion, and a theoretical route that predicts the distortion from only the atomic sizes of the pure elements and the alloy’s elastic constants.

For the DFT route, special quasirandom structures (SQS) are generated for each alloy to represent a chemically disordered random FCC solid solution. DFT calculations are performed using the GGA-PBE exchange-correlation functional with PAW pseudopotentials and a non‑spin‑polarized setup. First, the pristine lattice constant is obtained by relaxing the cell volume while keeping atomic positions fixed. Then a full relaxation of ions, cell shape, and volume yields the distorted structure. The cubic elastic constants C11 and C12 are computed by applying small strains to the distorted cell and monitoring the energy change. From the relaxed atomic positions, the local Lagrangian strain tensor is constructed, and an effective equivalent strain γ_i^eq is defined for each atom that combines the local hydrostatic and von Mises shear components weighted by the elastic constants. The overall lattice distortion is quantified by the average equivalent strain γ^DFT = sqrt( Σ_i (γ_i^eq)² / n ), where n is the number of atoms.

For the theoretical route, the lattice constants of the pure FCC elements are computed with the same DFT settings to obtain their effective atomic radii. Using a geometric model that accounts for efficient atomic packing, the radial strain fluctuation ε^fluc = sqrt( Σ_i c_i ε_i² ) is calculated, where c_i is the composition and ε_i is the residual radial strain around element i. The model predicts a critical equivalent strain γ^th = 0.5 * sqrt( 2(1+ν)/(1–2ν) ) * ε^fluc, with ν the Poisson ratio derived from C11 and C12. The same model also provides theoretical estimates of the pristine and distorted lattice constants. The key scientific question is whether the DFT-computed γ^DFT agrees with the theoretically predicted γ^th, and whether the model reproduces the DFT lattice constants.

## Reproduction target
For each of the 11 equimolar FCC alloys (FeNi, FeCr, FeCo, CoNi, CoCr, FeCoNi, FeCoCr, FeCrNi, CoNiCr, FeCoNiCr, FeCoNiCrMn), carry out the DFT and analytical workflow described in the steps below and compile the following quantities into a single CSV file:
- a_pristine_DFT (Å): the pristine (undistorted) lattice constant from volume‑only relaxation
- a_distorted_DFT (Å): the lattice constant after full relaxation
- c11 (GPa) and c12 (GPa): the two independent cubic elastic constants
- gamma_DFT (dimensionless): the average equivalent strain obtained from the distorted atomic positions
- eps_fluc (dimensionless): the radial strain fluctuation from the geometric model
- gamma_th (dimensionless): the theoretical critical equivalent strain predicted by the model

The resulting CSV must have one row per alloy, exactly 11 rows, with the column headers as listed. The file must be written to /app/outputs/alloy_results.csv.

## Assets

- ATAT (Alloy Theoretic Automated Toolkit): https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for Fe, Co, Ni, Cr, Mn: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Generate Special Quasirandom Structures
- Role: process
- Action: Using ATAT's mcsqs tool, generate SQS supercells for the 11 equimolar FCC alloys (FeNi, FeCr, FeCo, CoNi, CoCr, FeCoNi, FeCoCr, FeCrNi, CoNiCr, FeCoNiCr, FeCoNiCrMn) with chemically disordered FCC lattices. Supercell sizes: 32 atoms for binaries, 108 atoms for ternaries and quaternaries, 120 atoms for quinary.
- Evidence: `/app/outputs/sqs_structures.json`

### Step 2: Compute lattice constants of pure FCC elements
- Role: process
- Action: Using DFT (Quantum ESPRESSO) with GGA-PBE and PAW pseudopotentials, perform variable-cell relaxations or energy-vs-volume scans for pure FCC Fe, Co, Ni, Cr, Mn to determine their equilibrium lattice constants at 0 K. Non-spin-polarized calculations.
- Evidence: `/app/outputs/pure_element_lattice_constants.json`

### Step 3: Determine pristine lattice constants via volume relaxation
- Role: process
- Action: For each alloy SQS, perform DFT calculations relaxing only the cell volume (fixed atomic positions and cell shape) to map energy vs. volume, fit the third-order Birch-Murnaghan equation of state, and extract the equilibrium pristine lattice constant a_pristine_DFT.
- Evidence: `/app/outputs/pristine_lattice_constants.json`

### Step 4: Full relaxation to obtain distorted structures
- Role: process
- Action: Starting from the pristine SQS structures at their equilibrium volumes, relax all ionic positions, cell shape, and volume simultaneously to obtain the distorted structures. Record the final distorted lattice constant a_distorted_DFT.
- Evidence: `/app/outputs/distorted_lattice_constants.json`

### Step 5: Calculate elastic constants C11 and C12
- Role: process
- Action: Using the distorted structures, apply small elastic strains (e.g., volume-conserving tetragonal shear) and compute the resulting energy changes to extract the cubic elastic constants C11 and C12. Derive the polycrystalline Poisson's ratio ν.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 6: Compute equivalent strain γ^DFT from atomic positions
- Role: process
- Action: For each alloy's distorted structure, compute the local deformation gradient tensor for each atom, derive the Lagrangian strain tensor, the local hydrostatic strain ε^m, the von Mises equivalent shear strain γ^Mises, and then the effective equivalent strain γ_i^eq using the expression that combines hydrostatic and shear components weighted by elastic constants. Finally, compute the average equivalent strain γ^DFT = sqrt( Σ_i (γ_i^eq)^2 / n ).
- Evidence: `/app/outputs/gamma_dft.json`

### Step 7: Compute theoretical γ^th and lattice constants
- Role: process
- Action: Using the pure-element lattice constants and the alloy Poisson's ratio ν, compute the radial strain fluctuation ε^fluc = sqrt( Σ_i c_i ε_i^2 ) via the geometric model (based on efficient atomic packing and residual radial strains). Then calculate the theoretical critical equivalent strain γ^th = 0.5 * sqrt( 2(1+ν)/(1-2ν) ) * ε^fluc and the theoretical lattice constants a^th (pristine and distorted) according to the analytical model.
- Evidence: `/app/outputs/theoretical_values.json`

### Step 8: Compile final results table
- Role: scored (load-bearing)
- Action: Compile all computed quantities into a single CSV file with columns: alloy, a_pristine_DFT (Å), a_distorted_DFT (Å), c11 (GPa), c12 (GPa), gamma_DFT (dimensionless), eps_fluc (dimensionless), gamma_th (dimensionless). One row per alloy, 11 rows total.
- Output file: `/app/outputs/alloy_results.csv`
- Format: csv
- Contract: Columns: alloy (string), a_pristine_DFT (float, Å), a_distorted_DFT (float, Å), c11 (float, GPa), c12 (float, GPa), gamma_DFT (float, dimensionless), eps_fluc (float, dimensionless), gamma_th (float, dimensionless). Headers must match exactly.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alloy_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alloy_results.csv
- path: `/app/outputs/alloy_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV containing the final DFT-computed and analytically-predicted quantities for all 11 equimolar FCC alloys.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `a_pristine_DFT`, `a_distorted_DFT`, `c11`, `c12`, `gamma_DFT`, `eps_fluc`, `gamma_th`
  - `units`:
    - `a_pristine_DFT`: Å
    - `a_distorted_DFT`: Å
    - `c11`: GPa
    - `c12`: GPa
    - `gamma_DFT`: dimensionless
    - `eps_fluc`: dimensionless
    - `gamma_th`: dimensionless

Notes: The checker compares the agent's reported gamma_DFT and gamma_th for each alloy against the paper-reported gold values (non-magnetic, Table 1) using per-quantity tolerances. The reward is the fraction of alloys for which both gamma_DFT and gamma_th match within tolerance. Additional columns (lattice constants, elastic constants) are required for completeness but carry no separate scoring weight.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alloy_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "a_pristine_DFT",
          "a_distorted_DFT",
          "c11",
          "c12",
          "gamma_DFT",
          "eps_fluc",
          "gamma_th"
        ],
        "units": {
          "a_pristine_DFT": "Å",
          "a_distorted_DFT": "Å",
          "c11": "GPa",
          "c12": "GPa",
          "gamma_DFT": "dimensionless",
          "eps_fluc": "dimensionless",
          "gamma_th": "dimensionless"
        }
      },
      "description": "CSV containing the final DFT-computed and analytically-predicted quantities for all 11 equimolar FCC alloys."
    }
  ],
  "notes": "The checker compares the agent's reported gamma_DFT and gamma_th for each alloy against the paper-reported gold values (non-magnetic, Table 1) using per-quantity tolerances. The reward is the fraction of alloys for which both gamma_DFT and gamma_th match within tolerance. Additional columns (lattice constants, elastic constants) are required for completeness but carry no separate scoring weight."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/alloy_results.csv and compares the gamma_DFT and gamma_th values you report for each alloy against reference values (non‑magnetic). The comparison uses per‑quantity tolerances that are chosen to account for the legitimate spread expected when moving from one DFT code/pseudopotential set to another. The score is the fraction of alloys for which both gamma_DFT and gamma_th fall within the tolerance. The remaining columns (lattice constants, elastic constants) are required for completeness but do not carry independent scoring weight. Note that simply copying numbers from the paper is insufficient; the verifier expects results that are internally consistent with the DFT and analytical calculations you perform. Only results derived from a proper execution of the workflow will match the hidden gold within tolerance.
