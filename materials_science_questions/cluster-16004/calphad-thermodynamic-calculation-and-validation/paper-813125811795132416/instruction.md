# CALPHAD Thermodynamic Calculation of Binary Phase Diagram Tie-Lines

## Problem background
The prediction of stable phase compositions and phase boundaries in binary alloy systems is essential for materials design and process optimisation. The CALPHAD (CALculation of PHAse Diagrams) method describes the Gibbs energy of each phase as a function of composition and temperature, and finds equilibria by solving a set of nonlinear equations. However, traditional solution techniques require good initial guesses and manual intervention to select physically meaningful tie‑lines, especially when several phases—both of variable composition (disordered solutions) and of fixed composition (stoichiometric compounds)—compete. This task implements an algorithm that autonomically constructs the minimum Gibbs energy envelope, partitions the composition range into feasible segments, and uses an iterative U‑algorithm to enumerate all possible two‑phase equilibria and select the globally stable ones without any user tuning. The algorithm is applied to the Ni‑Al binary system using well‑established thermodynamic parameters from the literature. You are asked to compute the stable tie‑line endpoints (mole fraction of Al) for three temperatures and to output them in a structured CSV file.

## Approach
At each temperature, the algorithm first builds the minimum Gibbs energy function G̃(x) = min_i G^i(x,T) across all variable‑composition phases (liquid, FCC, BCC) by finding the lowest‑energy envelope. The composition axis is then divided into intervals where G̃ is convex and free of inflection points, forming regions that can host tie‑line endpoints. Phases of constant composition (Ni₃Al, Ni₂Al₃, NiAl₃) whose Gibbs energy lies above this envelope are discarded; the surviving fixed‑composition points further split the convex segments. Within each resulting segment a (possibly dummy) minimum is identified. For every pair of segments, candidate tie‑lines of type 1⊗1 (between two variable‑composition phases), 1⊗0/0⊗1 (between a variable‑composition phase and a constant‑composition phase), and 0⊗0 (between two constant‑composition phases) are constructed iteratively via the U‑algorithm, which solves for the common tangent that equalises chemical potentials. Finally, all candidate conodes are compared to retain only the globally stable ones—those that give the lowest Gibbs energy for the two‑phase mixture. The procedure yields a set of discrete tie‑lines at each temperature, defining the equilibrium state of the system.

## Reproduction target
Implement the autonomic binary phase diagram algorithm in Python, using the Ni‑Al thermodynamic parameters provided in this instruction. Run the algorithm at the three temperatures: 700 K, 1200 K, and 1500 K. For each temperature, write the globally stable tie‑line endpoints to the file `/app/outputs/tielines_NiAl.csv` with exactly the following columns:

- Temperature (floating‑point number, in K),
- Phase1_ID (string identifier for the first phase),
- Phase1_Composition (floating‑point number, mole fraction Al),
- Phase2_ID (string identifier for the second phase),
- Phase2_Composition (floating‑point number, mole fraction Al).

Phase identifiers must be from the set: `L`, `FCC`, `BCC`, `Ni3Al`, `Ni2Al3`, `NiAl3`. Each row represents one global‑stable tie‑line connecting two distinct coexisting phases; the order of the two phases is not significant. The CSV file must contain exactly one row per global‑stable tie‑line that exists at each temperature.

## Assets

- Ni-Al thermodynamic parameters (Kaufman & Nesor, 1978): 10.1016/0364-5916(78)90032-4
- Python 3 with NumPy and SciPy

## Workflow steps

### Step 1: Prepare thermodynamic inputs
- Role: process
- Action: Gather the thermodynamic Gibbs energy expressions and parameters for all phases in the Ni-Al system from Kaufman & Nesor (1978): Liquid, FCC, BCC (disordered solutions) and compounds Ni3Al, Ni2Al3, NiAl3 (constant composition). Also define the temperature grid: 700 K, 1200 K, 1500 K. These parameters are used as input to the algorithm.
- Evidence: none

### Step 2: Implement autonomic binary phase diagram algorithm
- Role: process
- Action: Implement the autonomic algorithm described in the instruction: (1) construct the minimum Gibbs energy function G̃(x) = min_i G^i(x,T); (2) segment the composition range and subdivide at inflection points to obtain convex feasible regions; (3) exclude constant-composition phases above the envelope; (4) break segments at surviving constant-phase compositions; (5) if multiple constant phases remain, build the G_{0⊗0} envelope; (6) locate minima (true/dummy) on each segment; (7) enumerate two-phase equilibria of types 1⊗1 and 1⊗0/0⊗1 using the U-algorithm; (8) select global-stable conodes at each temperature. The implementation must be in Python.
- Evidence: none

### Step 3: Compute and output tie-lines
- Role: scored (load-bearing)
- Action: Run the implemented algorithm for T = 700, 1200, 1500 K and save the globally stable tie-line endpoints to tielines_NiAl.csv. Each row contains one tie-line with the temperature and the two phases' identifiers and compositions.
- Output file: `/app/outputs/tielines_NiAl.csv`
- Format: csv
- Contract: CSV with columns: Temperature (float, K), Phase1_ID (string), Phase1_Composition (float, mole fraction Al), Phase2_ID (string), Phase2_Composition (float, mole fraction Al). One row per global-stable tie-line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tielines_NiAl.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tielines_NiAl.csv
- path: `/app/outputs/tielines_NiAl.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the globally stable tie-line endpoints (phase compositions in mole fraction Al) for the Ni-Al system at 700 K, 1200 K, and 1500 K. Each row is a tie-line with the temperature and the two coexisting phase identifiers and compositions.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Phase1_ID`, `Phase1_Composition`, `Phase2_ID`, `Phase2_Composition`
  - `units`:
    - `Temperature`: K
    - `Phase1_Composition`: mole fraction Al
    - `Phase2_Composition`: mole fraction Al

Notes: The checker will group rows by temperature and compare tie-lines against hidden gold values within a tolerance. Phase identifiers must match the following set: L, FCC, BCC, Ni3Al, Ni2Al3, NiAl3.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tielines_NiAl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Phase1_ID",
          "Phase1_Composition",
          "Phase2_ID",
          "Phase2_Composition"
        ],
        "units": {
          "Temperature": "K",
          "Phase1_Composition": "mole fraction Al",
          "Phase2_Composition": "mole fraction Al"
        }
      },
      "description": "CSV file containing the globally stable tie-line endpoints (phase compositions in mole fraction Al) for the Ni-Al system at 700 K, 1200 K, and 1500 K. Each row is a tie-line with the temperature and the two coexisting phase identifiers and compositions."
    }
  ],
  "notes": "The checker will group rows by temperature and compare tie-lines against hidden gold values within a tolerance. Phase identifiers must match the following set: L, FCC, BCC, Ni3Al, Ni2Al3, NiAl3."
}
```

## How you are scored
Your submitted output file `tielines_NiAl.csv` will be evaluated by an automated verifier. The verifier groups the rows by temperature and compares your list of tie‑lines against a hidden reference set that corresponds to the correct, thermodynamically stable tie‑lines for the given parameters. A tie‑line is considered correct if it connects the same two phases and its endpoint compositions fall within a predetermined tolerance. Missing tie‑lines, extra tie‑lines, or incorrect phase assignments reduce the score. The final reward is a weighted combination of scores across all workflow stages; for this task, nearly all weight comes from the correctness of the tie‑line output. Because the reference tie‑lines can only be obtained by properly implementing the described algorithm, simply guessing or fabricating endpoint values will not yield a high score.
