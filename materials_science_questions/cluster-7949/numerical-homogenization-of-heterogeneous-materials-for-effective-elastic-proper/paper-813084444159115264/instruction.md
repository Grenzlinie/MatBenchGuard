# Numerical Homogenization of Effective Stiffness Matrix via FFT for γ/γ' Microstructures

## Problem background
Nickel-base superalloys derive their high-temperature strength from a two-phase γ/γ′ microstructure consisting of a softer γ matrix reinforced by harder γ′ precipitates. Due to the lattice mismatch between the phases and the inhomogeneous plastic deformation that develops during service, significant internal stresses arise within the microstructure. These internal stresses strongly influence creep, fatigue, and rafting behavior. This work addresses the need for an efficient numerical method to compute the spatially resolved internal stresses from given eigenstrains (the sum of plastic and misfit strains) without performing a full-field simulation at every evaluation point. The core idea is to divide the representative volume element (RVE) into a small number of regions with approximately uniform deformation and to establish a linear relationship between the eigenstrains in those regions and the resulting region-averaged internal stresses. The linear map is an effective stiffness matrix constructed by solving an elastic boundary value problem once, using the Fast Fourier Transformation (FFT) method. The primary tasks are to compute this effective stiffness matrix for a cubic γ′ precipitate RVE and to quantify its accuracy by comparing stresses predicted by the effective stiffness relation with those obtained from full-field FFT calculations for a representative eigenstrain set.

## Approach
A 3D periodic RVE containing a cubic γ′ precipitate is discretized on a regular grid and partitioned into four regions: three orthogonal γ channels (x, y, z) and the central precipitate. Each region is assigned its own eigenstrain tensor (6 components). The linear effective stiffness assumption states that the region-averaged internal stress vector (24 components, 6 for each region) is the product of a 24×24 effective stiffness matrix and the eigenstrain vector. To construct this matrix, unit eigenstrain components are applied one by one; for each loading, the full-field elastic solution is obtained via an FFT-based solver with periodic boundary conditions, and the resulting stress field is averaged over each region to give one column of the matrix. After building the matrix, its predictive accuracy is assessed by comparing the internal stresses from the matrix multiplication to a full-field FFT solution for a specific eigenstrain set. The deviation between the two methods is quantified by the absolute percentage difference of each stress component, yielding a maximum and an average deviation over all 24 components. The workflow consists of three stages: RVE setup and region assignment, computation of the effective stiffness matrix, and validation/error reporting.

## Reproduction target
Compute the 24×24 effective stiffness matrix for the cubic γ′ precipitate RVE (grid 32×32×32, precipitate 28×28×28, channel width 4) using the unit eigenstrain loading procedure and the FFT elastic solver with periodic boundary conditions. After computing the matrix, apply the eigenstrain set defined in the validation step to the RVE, calculate the region-averaged internal stresses via the effective stiffness matrix and via full-field FFT, and determine the absolute percentage deviation for each of the 24 stress components. Report the maximum and the average of those 24 deviations.

## Assets

- Elastic constants of γ and γ′ phases for Ni-base superalloy from Demtröder et al. (2015): 10.1002/mawe.201500408

## Workflow steps

### Step 1: RVE preparation and region assignment
- Role: process
- Action: Create a 32×32×32 discretized RVE with a cubic γ′ precipitate (28×28×28) and three orthogonal γ channels (28×28×4 each). Assign each grid point to one of four regions: x-channel, y-channel, z-channel, or precipitate. Define periodic boundary conditions and assign the elastic constants for γ and γ′ according to Demtröder et al. (2015). Save the region mask and metadata.
- Evidence: `/app/outputs/rve_metadata.json`

### Step 2: Compute effective stiffness matrix
- Role: scored (load-bearing)
- Action: Apply 24 unit eigenstrain components one at a time: for each of the 6 strain components (11,22,33,12,13,23) in each of the 4 regions, set that component to 1.0 for grid points in its region (edge/corner points receive averages of adjacent channels) and 0 for all others. Solve the elastic constraint problem using the FFT method with periodic boundary conditions to obtain the full internal stress field. Average the resulting stresses over each region to obtain 24 values; these form one column of the 24×24 effective stiffness matrix C″. Repeat for all 24 components to fill the matrix. Save the matrix as a 2D list.
- Output file: `/app/outputs/effective_stiffness_matrix.json`
- Format: json
- Contract: A JSON list of 24 lists, each inner list containing 24 floating-point numbers, representing the effective stiffness matrix C″.
- Scoring: scored by hidden verifier

### Step 3: Validate internal stresses and report deviations
- Role: scored (load-bearing)
- Action: Assign the following eigenstrains to the four regions (x-channel, y-channel, z-channel, precipitate), each as a list of 6 strain components (11,22,33,12,13,23): x-channel: [0.7,0.8,0.9,0.8,0.7,0.6]; y-channel: [0.5,0.4,0.3,0.2,0.1,0.0]; z-channel: [1.0,0.1,0.2,0.3,0.4,0.5]; precipitate: [0.1,0.2,0.3,0.4,0.5,0.6]. Compute region-averaged internal stresses by two methods: (i) via the effective stiffness matrix C″ (matrix-vector product with the eigenstrain vector), and (ii) by directly applying the eigenstrains to the RVE and performing a full-field FFT solution. For each of the 24 stress components, calculate the absolute percentage deviation between the two methods. Report the maximum and average deviation over all 24 components.
- Output file: `/app/outputs/validation_summary.json`
- Format: json
- Contract: A JSON object with keys 'max_deviation_percent' (float) and 'avg_deviation_percent' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_stiffness_matrix.json`
- `/app/outputs/validation_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_stiffness_matrix.json
- path: `/app/outputs/effective_stiffness_matrix.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The effective stiffness matrix C″ constructed via unit eigenstrain FFT solves.
- schema:
  - `type`: array
  - `items`:
    - `type`: array
    - `items`:
      - `type`: number
  - `description`: 24x24 matrix of floats

### validation_summary.json
- path: `/app/outputs/validation_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum and average absolute percentage deviation of region-averaged internal stresses between the full-field FFT method and the effective stiffness method for the Table 2 eigenstrain set.
- schema:
  - `type`: object
  - `required`: `max_deviation_percent`, `avg_deviation_percent`
  - `properties`:
    - `max_deviation_percent`:
      - `type`: number
    - `avg_deviation_percent`:
      - `type`: number

Notes: The checker compares the submitted effective stiffness matrix to a hidden reference matrix using element-wise tolerances, and compares the reported deviations to the paper's published values using tolerance thresholds. The hidden gold values and tolerances are not disclosed to the solving agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_stiffness_matrix.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "array",
          "items": {
            "type": "number"
          }
        },
        "description": "24x24 matrix of floats"
      },
      "description": "The effective stiffness matrix C″ constructed via unit eigenstrain FFT solves."
    },
    {
      "file": "validation_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "max_deviation_percent",
          "avg_deviation_percent"
        ],
        "properties": {
          "max_deviation_percent": {
            "type": "number"
          },
          "avg_deviation_percent": {
            "type": "number"
          }
        }
      },
      "description": "Maximum and average absolute percentage deviation of region-averaged internal stresses between the full-field FFT method and the effective stiffness method for the Table 2 eigenstrain set."
    }
  ],
  "notes": "The checker compares the submitted effective stiffness matrix to a hidden reference matrix using element-wise tolerances, and compares the reported deviations to the paper's published values using tolerance thresholds. The hidden gold values and tolerances are not disclosed to the solving agent."
}
```

## How you are scored
A hidden verifier independently scores both required artifacts. The submitted effective stiffness matrix is compared element-wise against a reference matrix obtained by an honest implementation of the same public procedure; the agreement is assessed with appropriate tolerances. The reported maximum and average deviations are compared to the expected accuracy levels of the effective stiffness method for this configuration. The final reward is a weighted combination of the scores from the stiffness matrix stage and the validation stage. Reporting arbitrary numbers without faithfully executing the FFT-based workflow will not produce artifacts that match the hidden references.
