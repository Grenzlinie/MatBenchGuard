# Structural Goodness-of-Fit of Ca-Mn Oxides to Natural OEC Cubane

## Problem background
The natural oxygen-evolving complex (OEC) in photosystem II contains a CaMn₄O₅ cubane-like cluster. Synthetic Ca–Mn oxides, such as Ca₂Mn₃O₈ and CaMn₂O₄, contain local atomic arrangements that resemble this cubane. Quantifying how closely these oxide subunits match the natural OEC structure is important for understanding structure–performance relationships. The goodness-of-fit metric ω, obtained by least-squares superimposition of a cubane-like subunit onto the natural cubane, provides a numerical measure of structural similarity; a smaller ω indicates a closer match.

## Approach
The similarity assessment follows a least-squares superimposition procedure. First, the atomic coordinates of the natural OEC cubane are placed in a Cartesian reference frame with the Ca atom at the origin and two O atoms defining the xy-plane; the remaining coordinates are computed from known interatomic distances. Next, for each oxide crystal, a CaMn₄Oₓ cubane-like subunit is identified within the unit cell. This subunit can be superimposed on the reference cubane in three distinct orientation configurations, each defined by a set of rotational alignments. For each orientation, the oxide subunit is rotated to minimize the sum of squared coordinate differences between corresponding atoms, and the residual ω = sqrt( Σ [(x_i − x_ci)² + (y_i − y_ci)² + (z_i − z_ci)²] ) is computed. The result is six ω values—three per compound—that quantify how well each rotated subunit fits the natural cubane.

## Reproduction target
Compute the goodness-of-fit ω for Ca₂Mn₃O₈ and CaMn₂O₄ for all three orientation configurations, as illustrated in the original publication. Output the six values as a JSON file with keys 'Ca2Mn3O8' and 'CaMn2O4', each mapping to a list of three floating-point numbers, in the order of the orientations.

## Assets

- Natural OEC cubane atomic coordinates: https://www.rcsb.org/structure/3ZMT
- Ca₂Mn₃O₈ crystal structure: https://materialsproject.org/materials/mp-18893/
- CaMn₂O₄ crystal structure: https://materialsproject.org/materials/mvc-6593/
- Python scientific computing stack: numpy, scipy

## Workflow steps

### Step 1: Compute goodness-of-fit ω values for Ca₂Mn₃O₈ and CaMn₂O₄
- Role: scored (load-bearing)
- Action: Fetch the OEC cubane coordinates from PDB 3ZMT, and the crystal structures of Ca₂Mn₃O₈ (mp-18893) and CaMn₂O₄ (mvc-6593) from Materials Project. Extract the relevant atoms and orient the OEC cubane in a Cartesian coordinate system with Ca at origin. Identify the cubane-like subunits in the oxide structures and define the three orientation configurations per compound. Implement the least-squares superimposition procedure to compute the goodness-of-fit ω for each orientation. Output the six ω values as a JSON file.
- Output file: `/app/outputs/step_01_goodness_of_fit.json`
- Format: json
- Contract: {"Ca2Mn3O8": [float, float, float], "CaMn2O4": [float, float, float]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_goodness_of_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_goodness_of_fit.json
- path: `/app/outputs/step_01_goodness_of_fit.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Goodness-of-fit ω values for Ca₂Mn₃O₈ and CaMn₂O₄, each as a list of three floating-point numbers corresponding to the three orientation configurations described in the paper.
- schema:
  - `type`: object
  - `required`:
    - `Ca2Mn3O8`: array of three floats
    - `CaMn2O4`: array of three floats

Notes: The checker will recompute ω values using the same atomic coordinates and the same least-squares fitting procedure. The agent's submitted ω values will be compared against the checker's recomputed values within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_goodness_of_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Ca2Mn3O8": "array of three floats",
          "CaMn2O4": "array of three floats"
        }
      },
      "description": "Goodness-of-fit ω values for Ca₂Mn₃O₈ and CaMn₂O₄, each as a list of three floating-point numbers corresponding to the three orientation configurations described in the paper."
    }
  ],
  "notes": "The checker will recompute ω values using the same atomic coordinates and the same least-squares fitting procedure. The agent's submitted ω values will be compared against the checker's recomputed values within a tolerance."
}
```

## How you are scored
A hidden verifier will independently recompute the ω values using the same public atomic coordinates (OEC cubane from PDB 3ZMT, Ca₂Mn₃O₈ from Materials Project mp-18893, CaMn₂O₄ from mvc-6593) and the same least-squares superimposition method. Your submitted ω values will be compared against the verifier's recomputed values. You earn full credit if your values lie within an acceptable tolerance of the verifier's, and partial credit if they are close. The verifier assigns a reward score between 0 and 1 that reflects the accuracy of your computed ω values; simply reporting numbers that do not correspond to a correct computation will receive no credit.
