# Defect Percolation in Bidispersed Sphere Packings on a Sphere

## Problem background
Packings of bidispersed spherical particles on a spherical surface exhibit a structural transition in which the network of topological defects (non‑hexatic particles) can percolate as the size disparity (bidispersity) increases. In monodispersed packings, defects form isolated chains (scars) due to curvature frustration; bidispersity may cause these scars to grow and connect. This task investigates the percolation properties of the non‑hexatic subgraph in jammed bidispersed sphere packings on a unit sphere, and compares them with a random‑site percolation model on the monodispersed neighbor graph. The key quantities to determine are the connectedness probability of the non‑hexatic and hexatic subgraphs as a function of the non‑hexatic fraction, the size of the largest connected component, and the fractal dimension of clusters at the percolation threshold.

## Approach
The simulation workflow consists of two main branches that are then compared.

1. **Bidispersed packings**: Generate jammed configurations of N=800 spheres with varying bidispersity b and stoichiometry χ (fraction of large particles). A surface relaxation algorithm (random sequential adsorption, diffusion sweeps, surface radius contraction with adaptive step, and iterative unjamming via linear programming) is used to produce ensembles of arrested packings that are artificially aged to jamming. For each configuration, a radical tessellation on the sphere builds the neighbor graph and assigns coordination numbers. Particles with coordination number ≠6 are identified as non‑hexatic; the fraction 1‑φ6 of such particles defines the defect density p. From the ensemble at each b, percolation statistics are compiled as a function of p: the probability that the non‑hexatic subgraph is connected, the probability that the complementary hexatic subgraph remains connected, and the normalized size of the largest connected component. For χ=0.5, cluster radii (arclength distance) are computed and a power‑law fit extracts the fractal dimension D near the percolation threshold.

2. **Random‑site percolation model**: A monodispersed jammed packing (b=0, N=800) is generated, and its neighbor graph serves as the fixed lattice. Random‑site percolation is performed: for many values of the selected fraction p, sites are randomly chosen, and connectivity probabilities of the selected and unselected subgraphs, largest component size, and cluster radii are averaged over many trials. The fractal dimension D is fitted at the same p as for the bidispersed case.

The outputs are percolation curves for three stoichiometries (χ=0.5, 0.1, 0.9) and the fractal dimensions for χ=0.5, allowing the agreement between the bidispersed defect percolation and the random‑site model to be assessed.

## Reproduction target
Produce the following artifacts under /app/outputs:

- `percolation_curves_chi0.5.csv`: a CSV file with columns `p`, `prob_connected_nonhexatic`, `prob_hexatic_connected`, `largest_comp_fraction`, covering p from 0 to 1 in steps of ≤0.05, derived from the bidispersed packings at χ=0.5.
- `percolation_curves_chi0.1.csv`: same format, for χ=0.1.
- `percolation_curves_chi0.9.csv`: same format, for χ=0.9.
- `fractal_dimension_chi0.5.txt`: a plain text file containing two lines:
  `Fractal dimension D (bidispersed): <value>`
  `Fractal dimension D (random-site): <value>`
  where the values are the fitted fractal dimensions at the percolation threshold (p where the non‑hexatic subgraph becomes connected) for the bidispersed (χ=0.5) and random‑site percolation models.

The percolation curves must be computed from the ensemble of jammed packings and the random‑site model as described in the workflow steps.

## Assets

- numpy: numpy
- scipy: scipy
- networkx: networkx

## Workflow steps

### Step 1: Generate bidispersed jammed packings
- Role: process
- Action: Implement a surface relaxation algorithm (random sequential absorption, diffusion sweeps, surface radius reduction, iterative unjamming via linear programming) to generate ensembles of jammed bidispersed sphere packings on a unit sphere. Produce configurations for χ=0.5 (bidispersity b from 0 to 0.7, Δb≈0.005), χ=0.1 and χ=0.9 (selected b covering percolation region), N=800 particles, ~20 independent configurations per condition.
- Evidence: `/app/outputs/gen_bidisp_packings.log`

### Step 2: Construct neighbor graphs via radical tessellation
- Role: process
- Action: For each jammed packing, compute the radical tessellation on the sphere and construct the adjacency neighbor graph, assigning coordination numbers to all particles.
- Evidence: `/app/outputs/build_neighbor_graphs.log`

### Step 3: Compute non-hexatic subgraph percolation statistics
- Role: process
- Action: From the bidispersed neighbor graphs, identify non-hexatic particles (coordination number ≠6), compute the non‑hexatic fraction 1-φ6 for each configuration. Using the ensemble at each b, derive percolation statistics as a function of p=1-φ6: probability that the non-hexatic subgraph is connected, probability that the hexatic subgraph remains connected, size of the largest connected component. For χ=0.5, also compute cluster radii (Eq. (1) using arclength distance) and fit the fractal dimension D near the percolation threshold p≈0.65.
- Evidence: `/app/outputs/nonhexatic_percolation.log`

### Step 4: Run random-site percolation on monodispersed neighbor graph
- Role: process
- Action: Generate a monodispersed jammed packing (b=0, N=800) and build its neighbor graph. Perform random-site percolation: for many values of selected fraction p (0 to 1), randomly select sites and for many trials compute connectivity probabilities of selected/unselected subgraphs, size of the largest connected component. Also compute cluster radii and fit the fractal dimension D at p=0.65.
- Evidence: `/app/outputs/random_percolation_model.log`

### Step 5: Save percolation curves for χ=0.5
- Role: scored
- Action: Write the percolation statistics for χ=0.5 as a function of p to CSV.
- Output file: `/app/outputs/percolation_curves_chi0.5.csv`
- Format: csv
- Contract: CSV with header: p,prob_connected_nonhexatic,prob_hexatic_connected,largest_comp_fraction. Each row is a p value.
- Scoring: scored by hidden verifier

### Step 6: Save percolation curves for χ=0.1
- Role: scored
- Action: Write the percolation statistics for χ=0.1 as a function of p to CSV.
- Output file: `/app/outputs/percolation_curves_chi0.1.csv`
- Format: csv
- Contract: CSV with header: p,prob_connected_nonhexatic,prob_hexatic_connected,largest_comp_fraction.
- Scoring: scored by hidden verifier

### Step 7: Save percolation curves for χ=0.9
- Role: scored
- Action: Write the percolation statistics for χ=0.9 as a function of p to CSV.
- Output file: `/app/outputs/percolation_curves_chi0.9.csv`
- Format: csv
- Contract: CSV with header: p,prob_connected_nonhexatic,prob_hexatic_connected,largest_comp_fraction.
- Scoring: scored by hidden verifier

### Step 8: Save fractal dimensions at percolation threshold
- Role: scored (load-bearing)
- Action: Write the fitted fractal dimension D from bidispersed clusters (χ=0.5) and from the random-site percolation model, both at p≈0.65.
- Output file: `/app/outputs/fractal_dimension_chi0.5.txt`
- Format: txt
- Contract: Plain text with two lines: 'Fractal dimension D (bidispersed): <float>' and 'Fractal dimension D (random-site): <float>'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/percolation_curves_chi0.5.csv`
- `/app/outputs/percolation_curves_chi0.1.csv`
- `/app/outputs/percolation_curves_chi0.9.csv`
- `/app/outputs/fractal_dimension_chi0.5.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### percolation_curves_chi0.5.csv
- path: `/app/outputs/percolation_curves_chi0.5.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Percolation curves for stoichiometry χ=0.5: connectedness probabilities of non-hexatic and hexatic subgraphs and size of largest connected component as functions of the non-hexatic fraction p=1-φ6.
- schema:
  - `type`: table
  - `required_columns`: `p`, `prob_connected_nonhexatic`, `prob_hexatic_connected`, `largest_comp_fraction`
  - `units`:
    - `p`: fraction (dimensionless)
    - `prob_connected_nonhexatic`: probability [0,1]
    - `prob_hexatic_connected`: probability [0,1]
    - `largest_comp_fraction`: fraction [0,1]

### percolation_curves_chi0.1.csv
- path: `/app/outputs/percolation_curves_chi0.1.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Percolation curves for χ=0.1.
- schema:
  - `type`: table
  - `required_columns`: `p`, `prob_connected_nonhexatic`, `prob_hexatic_connected`, `largest_comp_fraction`
  - `units`:
    - `p`: fraction
    - `prob_connected_nonhexatic`: probability [0,1]
    - `prob_hexatic_connected`: probability [0,1]
    - `largest_comp_fraction`: fraction [0,1]

### percolation_curves_chi0.9.csv
- path: `/app/outputs/percolation_curves_chi0.9.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Percolation curves for χ=0.9.
- schema:
  - `type`: table
  - `required_columns`: `p`, `prob_connected_nonhexatic`, `prob_hexatic_connected`, `largest_comp_fraction`
  - `units`:
    - `p`: fraction
    - `prob_connected_nonhexatic`: probability [0,1]
    - `prob_hexatic_connected`: probability [0,1]
    - `largest_comp_fraction`: fraction [0,1]

### fractal_dimension_chi0.5.txt
- path: `/app/outputs/fractal_dimension_chi0.5.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Fractal dimension D fitted from cluster scaling at percolation threshold (p≈0.65) for the bidispersed packings (χ=0.5) and the random-site percolation model.
- schema:
  - `type`: text
  - `required`:
  - `items`: object

Notes: The solving agent is expected to generate the full ensemble of jammed packings and neighbor graphs; the percolation CSVs and fractal dimension are the scored deliverables. Checker will evaluate structural consistency (percolation threshold location, curve shape) and compare D values to hidden references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "percolation_curves_chi0.5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "prob_connected_nonhexatic",
          "prob_hexatic_connected",
          "largest_comp_fraction"
        ],
        "units": {
          "p": "fraction (dimensionless)",
          "prob_connected_nonhexatic": "probability [0,1]",
          "prob_hexatic_connected": "probability [0,1]",
          "largest_comp_fraction": "fraction [0,1]"
        }
      },
      "description": "Percolation curves for stoichiometry χ=0.5: connectedness probabilities of non-hexatic and hexatic subgraphs and size of largest connected component as functions of the non-hexatic fraction p=1-φ6."
    },
    {
      "file": "percolation_curves_chi0.1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "prob_connected_nonhexatic",
          "prob_hexatic_connected",
          "largest_comp_fraction"
        ],
        "units": {
          "p": "fraction",
          "prob_connected_nonhexatic": "probability [0,1]",
          "prob_hexatic_connected": "probability [0,1]",
          "largest_comp_fraction": "fraction [0,1]"
        }
      },
      "description": "Percolation curves for χ=0.1."
    },
    {
      "file": "percolation_curves_chi0.9.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "prob_connected_nonhexatic",
          "prob_hexatic_connected",
          "largest_comp_fraction"
        ],
        "units": {
          "p": "fraction",
          "prob_connected_nonhexatic": "probability [0,1]",
          "prob_hexatic_connected": "probability [0,1]",
          "largest_comp_fraction": "fraction [0,1]"
        }
      },
      "description": "Percolation curves for χ=0.9."
    },
    {
      "file": "fractal_dimension_chi0.5.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": [],
        "items": {}
      },
      "description": "Fractal dimension D fitted from cluster scaling at percolation threshold (p≈0.65) for the bidispersed packings (χ=0.5) and the random-site percolation model."
    }
  ],
  "notes": "The solving agent is expected to generate the full ensemble of jammed packings and neighbor graphs; the percolation CSVs and fractal dimension are the scored deliverables. Checker will evaluate structural consistency (percolation threshold location, curve shape) and compare D values to hidden references."
}
```

## How you are scored
A hidden verifier independently reads each output artifact and compares it against reference criteria derived from the paper’s results. The percolation CSV files are checked for structural consistency: the shape of the curves (e.g., sigmoidal rise of the non‑hexatic probability, complementary drop of the hexatic probability), the percolation threshold location, and the largest component fraction behavior. The fractal dimensions are compared to hidden reference values with appropriate tolerances. The reward is a weighted combination of these checks. Simply reporting numbers without executing the simulation will not pass the structural audits, because the curves must be derived directly from the ensemble of generated packings.
