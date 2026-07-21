## Problem background

Understanding how magnetization reverses in antiferromagnetic systems under nonuniform magnetic fields is important for magnetic materials science. In an antiferromagnet, spins on neighbouring sublattices point in opposite directions; applying a spatially oscillating field—positive on one sublattice, negative on the other—can switch the magnetization. The switching field depends on temperature and reveals different reversal mechanisms: coherent rotation at very low temperatures, nucleation of reversed-spin bubbles followed by domain‑wall propagation at intermediate temperatures, and thermally activated local spin flips plus wall motion at higher temperatures. Reproducing the switching curve and identifying the temperature boundaries of these regimes provides a quantitative check of the underlying statistical‑mechanics model.

## Approach

The system is a two‑dimensional square Ising lattice of size 1000×1000 with nearest‑neighbour antiferromagnetic exchange (coupling constant J = −1) and periodic boundary conditions. Spins are initialised in an antiferromagnetic order: one sublattice all “down”, the other all “up”.

After thermalising the lattice (≈1000 Monte Carlo steps), a spatially oscillating magnetic field is applied: the reduced field on the two sublattices is +h and −h respectively, where h = −H/(4J). The net magnetisation is monitored while h is scanned, and the critical switching field for each temperature is taken as the value of h at which the net magnetisation reverses sign.

The simulation is run for a set of reduced temperatures t = T/Tc (with Tc given by the exact Onsager value for the square Ising model, Tc = −0.567296326 J). The output is a switching curve h(t). This curve exhibits three regimes: a low‑temperature region where h is high and changes little; an intermediate‑temperature plateau where the switching field is roughly constant; and a high‑temperature region where h decreases monotonically. From the curve we extract the temperatures that bound the plateau, t₁ and t₂, and the average switching field on the plateau, h_plateau.

## Reproduction target

Implement the Monte Carlo simulation described above for reduced temperatures t = 0.02, 0.03, …, 0.20 (or a finer grid that spans this range). For each t, thermalise the lattice, apply the oscillating field, and determine the critical switching field h. From the resulting h(t) curve, identify the onset of the plateau (temperature t₁), the end of the plateau (temperature t₂), and the average switching field on the plateau (h_plateau). Save these three values in the machine‑readable output file specified below.

## Assets

- **Python** (runtime) – standard Python ≥3.8  
- **NumPy** (package) – numerical library for efficient array operations and random number generation (`numpy`, available via standard PyPI mirrors)  

## Workflow steps

### Step 1: Monte Carlo simulation of the switching curve
- Role: process
- Action: Implement a Monte Carlo simulation of a 2D antiferromagnetic Ising model on a 1000×1000 square lattice with nearest‑neighbour exchange J = −1 and periodic boundary conditions. Initialize the spins antiferromagnetically. For each reduced temperature t = 0.02, 0.03, …, 0.20 (or a finer grid), thermalise for ~1000 Monte Carlo steps, then apply a spatially oscillating magnetic field (+h, −h) on the two sublattices. Scan h and record the critical switching field where the net magnetisation changes sign. Save the (t, h) pairs as a CSV file with two columns: `t` and `h`.
- Evidence: `/app/outputs/switching_curve.csv`

### Step 2: Extract temperature regimes from the switching curve
- Role: scored (load‑bearing)
- Action: From the switching curve data in `/app/outputs/switching_curve.csv`, identify the low‑temperature region where h is near its maximum, the flat plateau region, and the high‑temperature monotonic decrease. Determine the temperature t₁ at which the plateau begins, the temperature t₂ at which it ends, and the average switching field h_plateau on the plateau. Write these three values to a single JSON object.
- Output file: `/app/outputs/regimes.json`
- Format: json
- Contract: `{"t1": <float>, "t2": <float>, "h_plateau": <float>}`
- Scoring: scored by hidden verifier

## Output files

All output files must be placed under `/app/outputs`.

- `/app/outputs/switching_curve.csv` – (t, h) data from the Monte Carlo simulation  
- `/app/outputs/regimes.json` – extracted regime boundaries and plateau height  

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### regimes.json
- path: `/app/outputs/regimes.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted temperature regime boundaries t1, t2 and plateau height h_plateau from the simulation's switching curve.
- schema:
  - `type`: object
  - `required`:
    - `t1`: float
    - `t2`: float
    - `h_plateau`: float

Notes: The verifier compares the values in regimes.json against a hidden gold standard derived from the paper's reported results, within tolerances. Full credit if all three are within tolerance; otherwise proportional credit per correct value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "regimes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "t1": "float",
          "t2": "float",
          "h_plateau": "float"
        }
      },
      "description": "Extracted temperature regime boundaries t1, t2 and plateau height h_plateau from the simulation's switching curve."
    }
  ],
  "notes": "The verifier compares the values in regimes.json against a hidden gold standard derived from the paper's reported results, within tolerances. Full credit if all three are within tolerance; otherwise proportional credit per correct value."
}
```

## How you are scored

A hidden verifier independently evaluates each workflow stage artifact. The scored artifact `regimes.json` is compared against a reference gold standard that represents the physical regime boundaries extracted from a correct simulation. Your submission receives credit proportional to the number of values that fall within the required tolerances. Simply reporting a number from memory or from a paper is not sufficient—the verifier checks that the values plausibly follow from the simulation you ran.
