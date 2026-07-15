# Compression-induced funnel transformation for 38-atom Lennard-Jones cluster

## Problem background
The 38-atom Lennard-Jones (LJ) cluster has a complex potential energy surface (PES) with a face-centred-cubic (fcc) truncated octahedron global minimum and a competing funnel of icosahedral low-energy structures. Adding a harmonic compressive term to the LJ potential can alter the PES topography, potentially changing the energy gap between the fcc global minimum and the lowest icosahedral minimum, and the distribution of minima between the two funnels. Understanding how compression strength affects these properties is important for global optimization of atomic clusters.

## Approach
We use the compressed Lennard-Jones (CLJ) energy function E_CLJ = E_LJ + μ_comp Σ_i |r_i - r_com|² / σ², where μ_comp parametrizes the compression. For several values of μ_comp, we sample a representative set of low-energy minima of the 38-atom cluster using a PES exploration method (e.g., basin-hopping or eigenvector-following). For each sampled minimum we record its energy and a structural descriptor (such as bond-order parameters) that distinguishes fcc-like and icosahedral structures. After sampling, we identify the lowest-energy fcc minimum and the lowest-energy icosahedral minimum to compute ΔE = E_icos - E_fcc. We also classify every minimum as belonging to either the fcc funnel or the icosahedral funnel (based on structural similarity and the energy at which the two funnels connect), and count the numbers n_fcc and n_icos. The ratio n_fcc/n_icos reflects the relative basin size of the fcc funnel. This analysis is performed for μ_comp = 0, 0.25, 1, and 5 ε (ε is the LJ well depth).

## Reproduction target
Produce and write to clj38_analysis_results.json three arrays: mu_comp (values 0, 0.25, 1, 5 ε), Delta_E (the corresponding ΔE values computed as described), and n_fcc_n_icos_ratio (the corresponding ratios n_fcc/n_icos). The arrays must be in order of increasing μ_comp. The verifier will use these arrays to check whether the energy gap and funnel ratio exhibit monotonic behaviour with compression.

## Assets

- Basin-hopping code (Cambridge Cluster Database): http://brian.ch.cam.ac.uk/software.html
- Reference LJ38 fcc truncated octahedron structure: http://brian.ch.cam.ac.uk/CCD.html
- Reference LJ38 lowest icosahedral structure: http://brian.ch.cam.ac.uk/CCD.html

## Workflow steps

### Step 1: PES sampling for CLJ38
- Role: process
- Action: Implement the compressed Lennard-Jones (CLJ) energy function E_CLJ = E_LJ + μ_comp Σ_i |r_i - r_com|²/σ². For each compression strength μ_comp in {0, 0.25, 1, 5} ε, use basin-hopping or eigenvector-following (or an equivalent PES exploration method) to sample a representative set of low-energy minima of the 38-atom cluster. Record the coordinates, energies, and structure descriptors (e.g., Q_comp or bond-order parameters) for every sampled minimum.
- Evidence: `/app/outputs/clj38_minima_energies.csv`

### Step 2: CLJ38 funnel analysis and trend extraction
- Role: scored (load-bearing)
- Action: From the sampled minima for each μ_comp: (a) Identify the lowest-energy minimum with fcc-like structure (truncated octahedron) and the lowest-energy minimum with icosahedral structure. Compute the energy difference ΔE = E_icos - E_fcc. (b) Classify every sampled minimum into the fcc funnel or the icosahedral funnel using structural similarity (e.g., bond-order parameters) or the method described in the paper. Compute the numbers of minima in each funnel, n_fcc and n_icos, and their ratio n_fcc / n_icos. Write all results to clj38_analysis_results.json as arrays in order of increasing μ_comp.
- Output file: `/app/outputs/clj38_analysis_results.json`
- Format: json
- Contract: {
  "mu_comp": [0, 0.25, 1, 5],
  "Delta_E": [float, float, float, float],
  "n_fcc_n_icos_ratio": [float, float, float, float]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/clj38_analysis_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### clj38_analysis_results.json
- path: `/app/outputs/clj38_analysis_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Extracted energy differences and funnel population ratios for CLJ38 at μ_comp = 0, 0.25, 1, 5 ε, used to verify the monotonic trends: Delta_E must be strictly increasing and n_fcc_n_icos_ratio must be non-decreasing.
- schema:
  - `type`: object
  - `required`:
    - `mu_comp`: array of four numbers (ε units)
    - `Delta_E`: array of four numbers (ε units)
    - `n_fcc_n_icos_ratio`: array of four dimensionless numbers
  - `items`:
    - `mu_comp_item`: float
    - `Delta_E_item`: float
    - `ratio_item`: float

Notes: The checker will verify that the returned arrays satisfy the structural relations: Delta_E[i+1] > Delta_E[i] and n_fcc_n_icos_ratio[i+1] >= n_fcc_n_icos_ratio[i] for i=0..2. The agent may use any robust PES sampling method; the computed values will differ from the paper’s exact numbers, but the monotonic trends should be preserved.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "clj38_analysis_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "mu_comp": "array of four numbers (ε units)",
          "Delta_E": "array of four numbers (ε units)",
          "n_fcc_n_icos_ratio": "array of four dimensionless numbers"
        },
        "items": {
          "mu_comp_item": "float",
          "Delta_E_item": "float",
          "ratio_item": "float"
        }
      },
      "description": "Extracted energy differences and funnel population ratios for CLJ38 at μ_comp = 0, 0.25, 1, 5 ε, used to verify the monotonic trends: Delta_E must be strictly increasing and n_fcc_n_icos_ratio must be non-decreasing."
    }
  ],
  "notes": "The checker will verify that the returned arrays satisfy the structural relations: Delta_E[i+1] > Delta_E[i] and n_fcc_n_icos_ratio[i+1] >= n_fcc_n_icos_ratio[i] for i=0..2. The agent may use any robust PES sampling method; the computed values will differ from the paper’s exact numbers, but the monotonic trends should be preserved."
}
```

## How you are scored
Each step's output is independently verified by a hidden checker. The primary scored artifact is clj38_analysis_results.json. The checker reads the file, verifies that the arrays are of the correct length and order, and then evaluates whether the Delta_E values strictly increase (each successive larger) and whether the n_fcc_n_icos_ratio values are non-decreasing (each successive at least as large as the previous). Reward is assigned based on how well the computed arrays satisfy these structural relations. The result of the analysis in clj38_analysis_results.json carries the majority of the task weight. Additionally, the checker may verify that the JSON file is well-formed and contains the expected keys. The hidden verifier does not use a fixed target value; it only checks monotonicity and correctness of the produced numbers relative to the submitted arrays.
