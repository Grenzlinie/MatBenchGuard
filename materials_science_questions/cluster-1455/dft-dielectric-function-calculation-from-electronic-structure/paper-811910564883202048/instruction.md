# DFT Dielectric Response of Ba1-xCaxZrO3 Perovskite Solid Solutions

## Problem background
Barium calcium zirconate (Ba1-xCaxZrO3) solid solutions are promising dielectric materials for wireless communication devices. The pure end members BaZrO3 and CaZrO3 have well-characterized static dielectric constants, but the solid solution's response is not a simple linear interpolation between the two end members. Understanding how the dielectric constant varies with Ca content is crucial for designing high-κ dielectrics, yet the composition dependence remains debated. This task uses first-principles density functional theory (DFT) to compute the directionally averaged static dielectric constant ε at several Ca fractions and to determine whether ε changes monotonically with x or follows a more complex trend.

## Approach
We use plane-wave DFT within the local density approximation (LDA) and norm-conserving pseudopotentials. The approach constructs 2×2×2 supercells of the ABO3 perovskite structure for Ca mole fractions x = 0, 0.125, 0.25, and 0.5, with Ca substituting for Ba in a way that minimizes Ca–Ca interactions at low concentrations. For each composition, we relax the atomic positions and lattice parameters to obtain the equilibrium geometry. After relaxation, density functional perturbation theory (DFPT) at the Γ point provides the dielectric tensor; the directionally averaged static dielectric constant ε is the mean of the diagonal components. By comparing ε across the four compositions, we can assess the compositional trend.

## Reproduction target
Produce a CSV file (dielectric_constants.csv) containing the computed ε for the four Ca fractions (x = 0, 0.125, 0.25, 0.5). The values should be derived from fully relaxed supercells and DFPT dielectric calculations. The primary scientific goal is to determine the dependence of ε on x using these computed points: does ε increase monotonically, decrease monotonically, or exhibit a nonmonotonic behavior (e.g., an initial increase followed by a decrease, or the opposite)? The reported data must support this analysis.

## Assets

- ABINIT: https://www.abinit.org/
- OPIUM pseudopotential generator: http://opium.sourceforge.net
- PseudoDojo LDA norm-conserving pseudopotentials: http://www.pseudo-dojo.org

## Workflow steps

### Step 1: Generate supercell structures
- Role: process
- Action: Construct 2×2×2 supercells of Ba1−xCaxZrO3 for compositions x = 0, 0.125, 0.25, 0.5, with appropriate Ca substitution arrangements (e.g., placing Ca at maximally separated A-site positions for low concentrations).
- Evidence: `/app/outputs/supercells_generated.log`

### Step 2: DFT structural relaxation
- Role: process
- Action: For each supercell, relax atomic positions and lattice constants using DFT-LDA with norm-conserving pseudopotentials. Use an open-source DFT code (e.g., ABINIT). Converge forces to obtain equilibrium geometries.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 3: Compute dielectric constants
- Role: scored (load-bearing)
- Action: For each relaxed structure, perform a DFPT response function calculation at the Γ point to obtain the diagonal elements of the dielectric tensor. Compute the directionally averaged static dielectric constant ε as the mean of the diagonal components. Save a CSV with one row per composition (x = 0, 0.125, 0.25, 0.5) and columns 'composition_x' and 'epsilon'.
- Output file: `/app/outputs/dielectric_constants.csv`
- Format: csv
- Contract: CSV with header: composition_x,epsilon. composition_x is the Ca mole fraction (float). epsilon is the directionally averaged static dielectric constant (dimensionless float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dielectric_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dielectric_constants.csv
- path: `/app/outputs/dielectric_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static dielectric constant (directionally averaged) for each specified BCZ composition (x=0, 0.125, 0.25, 0.5). The checker compares the values and their trend to a hidden reference from the paper.
- schema:
  - `type`: table
  - `required_columns`: `composition_x`, `epsilon`
  - `description`: composition_x (float): Ca mole fraction. epsilon (float): directionally averaged static dielectric constant (dimensionless).

Notes: Only the dielectric constants are scored; phonon frequencies and structural parameters are not evaluated. The compositions are x = 0, 0.125, 0.25, and 0.5.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dielectric_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_x",
          "epsilon"
        ],
        "description": "composition_x (float): Ca mole fraction. epsilon (float): directionally averaged static dielectric constant (dimensionless)."
      },
      "description": "Static dielectric constant (directionally averaged) for each specified BCZ composition (x=0, 0.125, 0.25, 0.5). The checker compares the values and their trend to a hidden reference from the paper."
    }
  ],
  "notes": "Only the dielectric constants are scored; phonon frequencies and structural parameters are not evaluated. The compositions are x = 0, 0.125, 0.25, and 0.5."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted dielectric constants and the associated trend. The verifier compares each ε value to a reference obtained with a similar computational setup, and checks whether the observed trend (monotonic vs. nonmonotonic and its direction) matches the expected physical behavior for this material. The reward is a weighted sum: accuracy of the individual ε values and the correctness of the trend both contribute. Executing the full workflow—supercell construction, structural relaxation, and DFPT response calculation—is essential; merely guessing or fabricating values will not satisfy the verifier.
