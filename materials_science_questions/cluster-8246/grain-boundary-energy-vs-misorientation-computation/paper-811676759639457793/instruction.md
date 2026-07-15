## Problem background
L1₂ ordered intermetallic compounds (prototype Ni₃Al) exhibit intrinsic grain‑boundary brittleness at low temperatures. One proposed origin is that maintaining chemical order (site occupancy) at grain boundaries severely restricts the set of geometrically allowed dislocation – grain‑boundary reactions. Perfect grain‑boundary dislocations (GBDs) leave the boundary structure unchanged; their Burgers vectors must be vectors of the displacement‑shift‑complete (DSC) lattice. In an ordered L1₂ material both atomic positions AND site occupancies must be preserved, so the relevant DSC lattice is that of a primitive cubic (simple cubic) crystal, which is coarser than the fcc DSC lattice that preserves only atomic positions.

When a lattice dislocation impinges on a grain boundary it can be absorbed (dissociated into perfect GBDs) or transmitted (continued into the other grain, leaving a residual GBD in the boundary). The King & Chen geometrical criterion states that a reaction is geometrically allowed only if the residual Burgers vector left in the boundary plane belongs to the chosen DSC set. Enforcing site‑occupancy preservation (primitive‑cubic DSC) instead of only site‑geometry preservation (fcc DSC) therefore reduces the number of allowed reactions drastically — a result that may explain the brittleness.

## Approach
For a given grain‑boundary misorientation characterized by its coincidence‑site‑lattice index Σ, the DSC vector sets for a disordered (fcc) and an ordered (primitive cubic) boundary are constructed. Then, for each of the 30 representative Burgers vectors that occur during L1₂ deformation, the King & Chen test is applied twice — once using the fcc DSC set and once using the primitive‑cubic DSC set.

The absorption test checks whether an incoming Burgers vector itself belongs to the DSC set. The transmission (and transformation) test checks every ordered pair of an incoming vector and a possible outgoing vector (including their negatives, giving 2 × 30² = 1800 candidates) and accepts the reaction if the residue b_in − b_out (or an equivalent combination) lies in the DSC set.

For each Σ and each condition (disordered or ordered) the allowed absorption count and the allowed transmission count are recorded. The procedure is repeated for Σ = 3, 5, 7, 9, 11, 13. The counts differ depending on whether Σ is an integer multiple of 3.

## Reproduction target
Compute the allowed absorption and transmission reaction counts for the six Σ values listed above, under both the disordered (fcc‑DSC) and the ordered (primitive‑cubic DSC) conditions. The result must be written to a CSV file; the integer counts will be compared to a hidden reference derived from published work. The task requires no external data beyond the crystallographic definitions and the standard Burgers vectors listed below.

## Incoming Burgers vectors (30 total)
All vectors are given in units of the fcc lattice constant a. Slight numerical differences (e.g. sign choice) do not affect the counting.

**APB‑creating dislocations ⟨110⟩/2 (12 vectors)**  
[ 1, 1, 0]/2, [ 1,-1, 0]/2, [-1, 1, 0]/2, [-1,-1, 0]/2,  
[ 1, 0, 1]/2, [ 1, 0,-1]/2, [-1, 0, 1]/2, [-1, 0,-1]/2,  
[ 0, 1, 1]/2, [ 0, 1,-1]/2, [ 0,-1, 1]/2, [ 0,-1,-1]/2

**Shockley partials ⟨112⟩/6 (12 vectors)**  
[ 1, 1, 2]/6, [ 1,-1, 2]/6, [-1, 1, 2]/6, [-1,-1, 2]/6,  
[ 1, 1,-2]/6, [ 1,-1,-2]/6, [-1, 1,-2]/6, [-1,-1,-2]/6,  
[ 1, 2, 1]/6, [ 1,-2, 1]/6, [-1, 2, 1]/6, [-1,-2, 1]/6

**Super‑Shockley partials ⟨112⟩/3 (6 vectors)**  
[ 1, 1, 2]/3, [ 1,-1, 2]/3, [-1, 1, 2]/3,  
[ 1, 1,-2]/3, [ 1,-1,-2]/3, [-1, 1,-2]/3

## DSC vectors
For a given Σ, the DSC lattice can be constructed from the coincidence‑site lattice; it is the set of all translations that map lattice sites of one crystal onto those of the other. For an fcc bicrystal the DSC vectors are the vectors of the fcc lattice scaled by 1/Σ (for suitable Σ) and restricted to the boundary plane; for a simple‑cubic bicrystal they are the vectors of the simple‑cubic lattice scaled similarly. Standard crystallographic formulas (or a library such as ASE) can be used to generate the exact sets for each Σ. The counts in this task are independent of the specific boundary plane; any commonly used symmetric‑tilt construction that yields the correct DSC lattice dimensions is acceptable.

## Assets
No external datasets, models, or tools are required beyond standard numerical libraries (NumPy, optionally ASE). The crystallographic definitions and the list of Burgers vectors are provided above.

## Workflow steps

### Step 1: Enumeration of dislocation reaction counts (scored, load‑bearing)
- Role: scored (load‑bearing)
- Action: Write a program that for each Σ ∈ {3, 5, 7, 9, 11, 13} performs the following:
  1. Compute the DSC vector set for the disordered (fcc) boundary and the ordered (primitive cubic) boundary.  
  2. For each of the 30 incoming Burgers vectors, test absorption against both DSC sets: a reaction is allowed if the vector is itself a member of the set. Count the allowed absorptions for each condition.  
  3. For transmission/transformation, test all 1800 ordered pairs (b_in, b_out) where b_in runs over the 30 vectors and b_out runs over all 30 vectors and their negatives. A reaction is allowed if the residue b_in − b_out (or the equivalent vector in the boundary plane) belongs to the DSC set. Count the allowed transmissions for each condition.  
  4. For each (Σ, condition) combination, record the absorption count and the transmission count.
- Output file: /app/outputs/reaction_counts.csv
- Format: csv
- Contract: comma‑separated values with a header row. Columns: `sigma` (integer), `condition` (string, either `'disordered'` or `'ordered'`), `absorption_count` (integer), `transmission_count` (integer). Exactly one row per Σ and condition, presented in any order.
- Scoring: the hidden verifier compares `absorption_count` and `transmission_count` for each row to reference integers derived from published results; an exact match is required.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_counts.csv
- path: `/app/outputs/reaction_counts.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Allowed absorption and transmission reaction counts per Σ and boundary ordering condition.
- schema:
  - `type`: table
  - `required_columns`: `sigma`, `condition`, `absorption_count`, `transmission_count`
  - `units`:
    - `sigma`: integer
    - `condition`: category ('disordered' or 'ordered')
    - `absorption_count`: integer
    - `transmission_count`: integer

Notes: The verifier compares the integer counts in each row to hidden gold values derived from published results; exact match is required. No tolerances are applied because the enumeration is deterministic and yields the same integers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma",
          "condition",
          "absorption_count",
          "transmission_count"
        ],
        "units": {
          "sigma": "integer",
          "condition": "category ('disordered' or 'ordered')",
          "absorption_count": "integer",
          "transmission_count": "integer"
        }
      },
      "description": "Allowed absorption and transmission reaction counts per Σ and boundary ordering condition."
    }
  ],
  "notes": "The verifier compares the integer counts in each row to hidden gold values derived from published results; exact match is required. No tolerances are applied because the enumeration is deterministic and yields the same integers."
}
```

## How you are scored
A hidden verifier reads your `reaction_counts.csv` and compares each row's `absorption_count` and `transmission_count` to a hidden ground‑truth table derived from published values. Each correct row contributes equally to the final reward, which lies between 0 and 1. Simply reporting numbers without performing the actual King & Chen enumeration will not satisfy the scoring; the verifier expects the correct integer counts produced by a correct implementation of the geometrical criteria.
