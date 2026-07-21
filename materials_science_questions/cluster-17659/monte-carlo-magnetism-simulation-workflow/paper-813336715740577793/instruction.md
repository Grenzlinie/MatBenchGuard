# Variable vs Fixed Sublattice Monte Carlo for Antiferromagnetic Potts Model

## Problem background
The three-state antiferromagnetic Potts model on a simple cubic lattice is a canonical frustrated spin system. At low temperatures the system orders in a broken‑sublattice‑symmetry (BSS) phase, and at high temperatures it becomes disordered. The nature of the ordering in the intermediate‑temperature region is controversial: some studies report a permutationally symmetric sublattice (PSS) phase, while others report a rotationally symmetric (RS) phase. The discrepancy may arise from the way the degeneracy of the two interpenetrating sublattices is handled when averaging Monte‑Carlo data. This task investigates which intermediate‑temperature phase emerges when sublattice degeneracy is accounted for correctly, by directly comparing two averaging methods — one that respects the instantaneous majority‑state sublattice (variable sublattice), and one that pins fixed physical sublattice labels (fixed sublattice). The results will demonstrate whether the PSS phase is a genuine thermodynamic phase or an artifact of incorrect averaging.

## Approach
We simulate the three-state antiferromagnetic Potts model on a L=36 simple cubic lattice with periodic boundary conditions using the Swendsen‑Wang cluster‑flipping Monte‑Carlo algorithm. At each temperature over the range 0.3–1.3 we record the instantaneous concentration of each Potts state on the two sublattices and the sublattice magnetizations. Two separate accumulation strategies are employed in parallel:

1. **Variable sublattice method** – after every Monte‑Carlo step, the sublattice that currently hosts the most frequent Potts state is identified as the “majority” sublattice, and statistics from that step are added to the corresponding running aggregates. This procedure correctly handles the six‑fold degeneracy arising from permutations of the three states and exchange of the two sublattices.
2. **Fixed sublattice method** – the physical sublattice labels A and B are kept fixed throughout the entire simulation; all statistics are added to the same physical sublattice regardless of where the majority state resides in a given step. This approach is prone to averaging over the two sublattices and may produce spurious signals.

From the accumulated statistics we compute ensemble‑averaged concentration curves and the sublattice‑magnetization order parameter M = |M_A − M_B| for both methods, allowing a direct comparison of the two averaging strategies.

## Reproduction target
Implement the described Monte‑Carlo simulation and analysis to produce the following three scored CSV files under /app/outputs:

- `concentrations_variable.csv` – temperature‑dependent concentrations of the Potts states on the majority and minority sublattices obtained with the variable sublattice method.
- `concentrations_fixed.csv` – temperature‑dependent concentrations on the fixed physical sublattices A and B obtained with the fixed sublattice method.
- `magnetization.csv` – the order parameter M = |M_A − M_B| versus temperature for both the variable and fixed methods.

All files must follow the schemas given in the workflow steps and output contract, with temperatures in strictly increasing order.

## Assets

- Python 3.8+
- NumPy: numpy

## Workflow steps

### Step 1: Run Monte Carlo simulation
- Role: process
- Action: Implement the three-state antiferromagnetic Potts model on a L=36 simple cubic lattice with periodic boundary conditions using the Swendsen-Wang cluster-flipping algorithm. For temperatures from T=0.3 to T=1.3, run equilibration and production Monte Carlo steps, recording per-MCS sublattice concentrations and magnetizations. Accumulate separate statistics for both the variable sublattice method (align by instantaneous majority-state sublattice) and the fixed sublattice method (pin physical sublattice labels).
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Write variable-method concentrations
- Role: scored
- Action: From the accumulated variable-sublattice statistics, compute the ensemble-averaged concentrations for the majority and minority sublattices at each temperature. Output a CSV file with columns T, majority_c1, majority_c2, majority_c3, minority_c1, minority_c2, minority_c3. T in increasing order.
- Output file: `/app/outputs/concentrations_variable.csv`
- Format: csv
- Contract: CSV header: T, majority_c1, majority_c2, majority_c3, minority_c1, minority_c2, minority_c3. All numeric. T in increasing order.
- Scoring: scored by hidden verifier

### Step 3: Write fixed-method concentrations
- Role: scored
- Action: From the accumulated fixed-sublattice statistics, compute the ensemble-averaged concentrations on physical sublattices A and B at each temperature. Output a CSV file with columns T, c1A, c2A, c3A, c1B, c2B, c3B. T in increasing order.
- Output file: `/app/outputs/concentrations_fixed.csv`
- Format: csv
- Contract: CSV header: T, c1A, c2A, c3A, c1B, c2B, c3B. All numeric. T in increasing order.
- Scoring: scored by hidden verifier

### Step 4: Write magnetization order parameter
- Role: scored (load-bearing)
- Action: Compute the sublattice magnetization order parameter M = |M_A - M_B| for both the variable and fixed sublattice methods from the accumulated statistics. Output a CSV file with columns T, M_variable, M_fixed. T in increasing order.
- Output file: `/app/outputs/magnetization.csv`
- Format: csv
- Contract: CSV header: T, M_variable, M_fixed. All numeric. T in increasing order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/concentrations_variable.csv`
- `/app/outputs/concentrations_fixed.csv`
- `/app/outputs/magnetization.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### concentrations_variable.csv
- path: `/app/outputs/concentrations_variable.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Concentration of Potts states on the two aggregated sublattices (majority and minority) as a function of temperature, obtained by variable sublattice averaging. The checker verifies the low-temperature BSS concentration pattern and the qualitative behavior across temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `majority_c1`, `majority_c2`, `majority_c3`, `minority_c1`, `minority_c2`, `minority_c3`
  - `units`: object

### concentrations_fixed.csv
- path: `/app/outputs/concentrations_fixed.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Concentration of Potts states on physical sublattices A and B as a function of temperature, obtained by fixed sublattice averaging. The checker verifies that this method produces PSS-like averaged results distinct from the variable method.
- schema:
  - `type`: table
  - `required_columns`: `T`, `c1A`, `c2A`, `c3A`, `c1B`, `c2B`, `c3B`
  - `units`: object

### magnetization.csv
- path: `/app/outputs/magnetization.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Magnetization order parameter M = |M_A - M_B| versus temperature for both the variable and fixed sublattice methods. The checker compares the values at selected temperatures against hidden paper-derived thresholds to confirm that the variable method yields stable BSS/RS ordering while the fixed method falsely suggests a PSS transition.
- schema:
  - `type`: table
  - `required_columns`: `T`, `M_variable`, `M_fixed`
  - `units`: object

Notes: All output files follow the described schema. The agent must produce the complete temperature range with T in increasing order. No gold thresholds are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "concentrations_variable.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "majority_c1",
          "majority_c2",
          "majority_c3",
          "minority_c1",
          "minority_c2",
          "minority_c3"
        ],
        "units": {}
      },
      "description": "Concentration of Potts states on the two aggregated sublattices (majority and minority) as a function of temperature, obtained by variable sublattice averaging. The checker verifies the low-temperature BSS concentration pattern and the qualitative behavior across temperature."
    },
    {
      "file": "concentrations_fixed.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "c1A",
          "c2A",
          "c3A",
          "c1B",
          "c2B",
          "c3B"
        ],
        "units": {}
      },
      "description": "Concentration of Potts states on physical sublattices A and B as a function of temperature, obtained by fixed sublattice averaging. The checker verifies that this method produces PSS-like averaged results distinct from the variable method."
    },
    {
      "file": "magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "M_variable",
          "M_fixed"
        ],
        "units": {}
      },
      "description": "Magnetization order parameter M = |M_A - M_B| versus temperature for both the variable and fixed sublattice methods. The checker compares the values at selected temperatures against hidden paper-derived thresholds to confirm that the variable method yields stable BSS/RS ordering while the fixed method falsely suggests a PSS transition."
    }
  ],
  "notes": "All output files follow the described schema. The agent must produce the complete temperature range with T in increasing order. No gold thresholds are exposed."
}
```

## How you are scored
A hidden verifier will independently score each of the three required CSV artifacts. For the concentration files the verifier checks the structural integrity of the data and verifies that the concentration distributions across temperature follow the physically expected patterns (BSS, RS, and a PSS‑like signature) without revealing the exact reference values. For the magnetization file the verifier compares your reported M_variable and M_fixed at selected temperatures against hidden, paper‑derived thresholds that distinguish the three phases. The final reward is a weighted sum of these per‑artifact scores, so you must produce all three files and satisfy both the structural and quantitative checks. Simply reporting the paper’s numbers without executing the simulation will not pass the hidden verifier.
