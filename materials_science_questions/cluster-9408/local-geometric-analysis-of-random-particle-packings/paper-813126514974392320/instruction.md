# Compute Coordination Numbers for Random Sphere Packings Using the Maximal Disorder Model

## Problem background
Random packings of spheres are fundamental in granular materials, porous media, and the structure of liquids. A key descriptor is the coordination number — the number of spheres that touch or are geometrically adjacent to a given sphere. For ordered packings the coordination is well-defined, but for disordered packings it is not unique. This task implements a model that predicts the average contact coordination number for binary mixtures of spheres and the average number of geometric neighbours in monodisperse random packings.

## Approach
The model, called the maximal disorder model, assumes that a sphere immersed in a random packing perturbs only its immediate first shell of neighbours. For a large sphere of diameter d₂ in a bed of small spheres of diameter d₁, the contact coordination number follows from a simple geometric argument and the porosity of the bulk random packing. The porosity of a monodisperse random loose packing is taken as ε₀ = 0.36 (Scott, 1960). The model yields a closed-form expression for the average number of small spheres in contact with the large sphere:

C_c = (1 − ε₀) × ((d₁ + d₂)³ − d₂³) / d₁³.

For monodisperse packings, the integral coordination up to a distance L from a given sphere's center is:

C(L) = (1 − ε₀) × [ 8 × (L/d)³ − 1 ].

The number of geometric (Voronoi) neighbours is obtained by evaluating this integral at L = √2 d.

## Reproduction target
Compute the contact coordination numbers for ten diameter ratios d₁/d₂ = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0] using the formula above. Write the results to a CSV file with two columns (ratio and predicted coordination). Compute the predicted average geometric neighbour number for monodisperse spheres using the integral formula at L = √2 d and write that single number to a text file.

## Assets
No external datasets or pretrained models are needed. The only numerical parameter is the porosity ε₀ = 0.36 (from Scott, 1960), which can be hardcoded directly in your code.

## Workflow steps

### Step 1: Compute contact coordination for binary mixtures
- Role: scored (load-bearing)
- Action: For each diameter ratio r = d1/d2 in the list [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0], compute the contact coordination number using the maximal disorder model's formula that depends on the porosity ε0 = 0.36 (from Scott) and geometric arguments of the perturbed first layer. Write the results to a CSV file with no header, containing the ratio and the computed coordination number.
- Output file: `/app/outputs/contact_coordination.csv`
- Format: csv
- Contract: d1_d2,contact_coordination
- Scoring: scored by hidden verifier

### Step 2: Compute geometric neighbor number
- Role: scored
- Action: Evaluate the integral coordination formula of the maximal disorder model for monodisperse spheres at L = √2 d, using the same porosity ε0 = 0.36, to obtain the average geometric neighbor number. Write the result as a single floating-point number to a text file.
- Output file: `/app/outputs/geometric_neighbors.txt`
- Format: txt
- Contract: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/contact_coordination.csv`
- `/app/outputs/geometric_neighbors.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### contact_coordination.csv
- path: `/app/outputs/contact_coordination.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The checker will recompute the correct contact coordination value for each ratio using the model formula and compare it with the agent's submitted value within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `d1_d2`, `contact_coordination`
  - `delimiter`: ,
  - `no_header`: True

### geometric_neighbors.txt
- path: `/app/outputs/geometric_neighbors.txt`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: The checker will compute the correct geometric neighbor number from the model and compare it with the agent's submitted value within a tolerance.
- schema:
  - `type`: text
  - `shape`: scalar_float

Notes: Both outputs are generated solely from the publicly known maximal disorder model equations and the single porosity constant ε0=0.36. No experimental data or external assets are needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "contact_coordination.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "d1_d2",
          "contact_coordination"
        ],
        "delimiter": ",",
        "no_header": true
      },
      "description": "The checker will recompute the correct contact coordination value for each ratio using the model formula and compare it with the agent's submitted value within a tolerance."
    },
    {
      "file": "geometric_neighbors.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "shape": "scalar_float"
      },
      "description": "The checker will compute the correct geometric neighbor number from the model and compare it with the agent's submitted value within a tolerance."
    }
  ],
  "notes": "Both outputs are generated solely from the publicly known maximal disorder model equations and the single porosity constant ε0=0.36. No experimental data or external assets are needed."
}
```

## How you are scored
Your outputs are checked by a hidden verifier. For the contact coordination CSV, the verifier recomputes the expected coordination for each ratio and compares your values element-wise. For the geometric neighbours file, the verifier recomputes the expected number and compares it to yours. Your final score is a weighted combination of the accuracy on both artifacts.
