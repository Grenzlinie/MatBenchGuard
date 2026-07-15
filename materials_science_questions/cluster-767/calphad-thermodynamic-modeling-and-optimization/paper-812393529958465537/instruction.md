# Ternary Feldspar Equilibrium Composition Calculation using TEREQUIL Algorithm

## Problem background
Ternary systems containing two coexisting phases are common in geology and materials science. The equilibrium compositions of the two phases at given temperature and pressure are determined by minimizing the total Gibbs free energy of the two-phase assemblage. This task recreates that calculation for the specific case of high-temperature ternary feldspars (Ca–Na–K feldspars). The target is the set of equilibrium mole fractions obtained by running a published derivative-free minimization algorithm with a given equation of state. Computing these equilibrium pairs tests whether the algorithm and thermodynamic model are correctly implemented.

## Approach
The algorithm performs an iterative search to minimize the total Gibbs free energy \( G_{\text{total}} = 0.5\,G_A(\mathbf{X}_A) + 0.5\,G_B(\mathbf{X}_B) \) for two phases \(A\) and \(B\), constrained so that the mean composition remains approximately constant. At each iteration, it alternates between two types of searches: first a “binary” search along the tie-line defined by the current composition pair, adjusting the phase fractions to minimize \(G_{\text{total}}\); then a “perpendicular” search where the compositions move in equal and opposite directions perpendicular to that tie-line while preserving the midpoint. The procedure repeats until convergence.

The Gibbs free energy of the feldspar solution is given by a Margules-type equation of state that includes excess free energy terms with parameters \(W_h, W_s, W_v\) (provided in the step instructions) and ideal mixing terms. The energy is evaluated in “user coordinates” \(X_{\text{or}}\) (orthoclase) and \(X_{\text{ab}}\) (albite), with \(X_{\text{an}} = 1 - X_{\text{or}} - X_{\text{ab}}\) (anorthite). The algorithm internally works in “proper” vector coordinates that satisfy the lever rule; the required forward and inverse coordinate transformations are as described in the step instructions.

You will implement the Gibbs function and coordinate transforms, then for each of three temperatures (700, 800, 900 °C) at 1 kbar, start from the initial guess (phase A: \(X_{\text{or}}=0.1, X_{\text{ab}}=0.8\); phase B: \(X_{\text{or}}=0.8, X_{\text{ab}}=0.1\)) and run the iterative minimization. The resulting equilibrium mole fractions are output as a CSV file.

## Reproduction target
Compute the equilibrium composition pairs for ternary feldspars at temperatures 700, 800, and 900 °C and pressure 1 kbar, starting from the initial guess (phase A: \(X_{\text{or}}=0.1, X_{\text{ab}}=0.8\); phase B: \(X_{\text{or}}=0.8, X_{\text{ab}}=0.1\)). For each temperature, output the final mole fractions \(X_{\text{or}}\), \(X_{\text{ab}}\), and \(X_{\text{an}}\) for both phases as a CSV file with columns: `temperature`, `phase`, `Xor`, `Xab`, `Xan`. The file should contain exactly six rows (one row per phase per temperature).

## Assets
No external datasets, pre-trained models, or online services are required. All necessary thermodynamic parameters and the algorithmic description are provided in this task. The implementation can be carried out in any programming language; typical choices include Python with NumPy or C.

## Workflow steps

### Step 1: Compute Equilibrium Composition Pairs
- Role: scored (load-bearing)
- Action: Implement the TEREQUIL derivative-free minimization algorithm and the Elkins & Grove (1990) Gibbs free energy equation of state for ternary feldspars. Use the Margules parameters from the paper's code listing. At each temperature (700, 800, 900 °C) and pressure 1 kbar, start from initial guess phase A (Xor=0.1, Xab=0.8), phase B (Xor=0.8, Xab=0.1). Compute the equilibrium compositions (Xor, Xab, Xan) for each phase. Write the results to equilibrium_pairs.csv.
- Output file: `/app/outputs/equilibrium_pairs.csv`
- Format: csv
- Contract: columns: temperature (float, degrees Celsius), phase (str, 'A' or 'B'), Xor (float), Xab (float), Xan (float). One row per phase per temperature (6 rows total).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_pairs.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_pairs.csv
- path: `/app/outputs/equilibrium_pairs.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed equilibrium composition pairs for ternary feldspar at 700, 800, and 900 °C and 1 kbar.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `phase`, `Xor`, `Xab`, `Xan`
  - `units`:
    - `temperature`: Celsius
    - `Xor`: mole fraction
    - `Xab`: mole fraction
    - `Xan`: mole fraction

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_pairs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "phase",
          "Xor",
          "Xab",
          "Xan"
        ],
        "units": {
          "temperature": "Celsius",
          "Xor": "mole fraction",
          "Xab": "mole fraction",
          "Xan": "mole fraction"
        }
      },
      "description": "Computed equilibrium composition pairs for ternary feldspar at 700, 800, and 900 °C and 1 kbar."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently re-implements the same algorithm and equation of state (using the same initial guesses and temperatures) to produce its own reference equilibrium composition pairs. It reads your `equilibrium_pairs.csv` and compares each mole fraction value (\(X_{\text{or}}\), \(X_{\text{ab}}\), \(X_{\text{an}}\)) to its reference, within a pre‑defined tolerance. Your reward is the fraction of the reported mole fraction values that are within tolerance. Reporting numbers without genuinely running the computation will not succeed because the tolerance is set to require an actual implementation.
