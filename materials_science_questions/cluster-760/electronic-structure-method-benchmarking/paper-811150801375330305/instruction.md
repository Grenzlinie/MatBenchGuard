# Relative energies and temperature-dependent isomer populations of protonated ammonia clusters H+(NH3)n (n=4-9)

## Problem background
Protonated ammonia clusters H+(NH3)n are fundamental models for proton solvation in ammonia, directly relevant for pKa predictions and solvation energy estimations. All prior theoretical and experimental investigations of these clusters have assumed only branched linear structural motifs. This work addresses whether the true structural landscape is richer by systematically searching for all possible stable isomers of protonated ammonia clusters of sizes n = 4 through 9. The task is to determine zero-point corrected relative energies and temperature-dependent isomer populations, which together reveal the degree to which previously unexplored topologies—such as cyclic, branched cyclic, double cyclic, triple cyclic, and their branched counterparts—contribute to the cluster ensemble.

## Isomer naming convention
The topologies referred to in the results follow a compact notation: Ln (linear), BLn (branched linear), Cn (cyclic), BCn (branched cyclic), DCn (double cyclic), TCn (triple cyclic), BTCn (branched triple cyclic), BDCn (branched double cyclic), and Can (cage). For a given topology and cluster size n, when multiple distinct isomers exist, they are numbered in order of increasing relative energy (e.g., BL5_1, BL5_2, BC7_1, BC7_2). The agent must use this exact naming pattern in all output files.

## Approach
The reproduction workflow starts by generating initial guess geometries for a wide range of hydrogen-bond network topologies covering linear, branched linear, cyclic, branched cyclic, double cyclic, triple cyclic, branched double cyclic, and branched triple cyclic arrangements. These candidates are obtained using a global minima search with the ABCluster code supplemented by intuitive construction. Each candidate structure is then optimised at the M06-2X/6-31++G(d,p) level of density functional theory, with harmonic vibrational frequency calculations to confirm true minima and to provide thermodynamic corrections. From the optimised outputs, zero-point corrected electronic energies are extracted and used to compute relative energies (in kcal/mol) for every isomer of each cluster size, as well as the canonical probability distributions at 25 K and 100 K using the harmonic free energies. The quantitative comparisons reveal whether isomers beyond the branched linear motif are stable and, for larger clusters, how temperature shifts the population between motif types.

## Reproduction target
For cluster sizes n = 4, 5, 6, 7, 8, 9, produce a file `relative_energies.json` that lists every optimised isomer and its zero-point corrected relative energy (kcal/mol) referenced to the global minimum of that cluster size. For the three largest sizes n = 7, 8, 9, produce a file `population_n7_n9.json` giving the canonical probability distribution of all isomers at temperatures T = 25 K and T = 100 K. The agent must run the full computational pipeline—structure generation, DFT optimisation, frequency analysis, and post-processing—to compute these numbers; simply reporting literature values is not in scope.

## Assets

- ABCluster global minima search code: https://github.com/jzhang2015/ABCluster
- M06-2X density functional: implemented in ORCA, Psi4, Gaussian, etc.
- 6-31++G(d,p) basis set: standard basis set library
- Quantum chemistry package (e.g., ORCA or Psi4): https://orcaforum.kofo.mpg.de/ or https://psicode.org/

## Workflow steps

### Step 1: Generate initial guess structures
- Role: process
- Action: Generate initial guess geometries for all isomers of H+(NH3)n (n=4-9) covering branched linear, linear, cyclic, branched cyclic, double cyclic, triple cyclic, branched double cyclic, and branched triple cyclic topologies. Use ABCluster global optimisation and intuitive hydrogen-bond network construction as described in the method.
- Evidence: `/app/outputs/generated_xyz_files.tar.gz`

### Step 2: M06-2X/6-31++g(d,p) geometry optimisation and frequency calculation
- Role: process
- Action: For each candidate structure, perform geometry optimisation at the M06-2X/6-31++g(d,p) level with tight convergence criteria and an ultrafine integration grid using a quantum chemistry package. Compute harmonic vibrational frequencies to confirm each stationary point is a true local minimum and obtain thermodynamic corrections. Save the optimisation output logs.
- Evidence: `/app/outputs/optimization_logs.tar.gz`

### Step 3: Compute relative energies
- Role: scored (load-bearing)
- Action: From the optimisation outputs, extract zero-point corrected electronic energies (E0). For each cluster size n, identify the global minimum and compute the relative energy ΔE = E0 – E0(global min) in kcal/mol for all isomers. Write the results to `relative_energies.json`.
- Output file: `/app/outputs/relative_energies.json`
- Format: json
- Contract: JSON object with keys 'n=4', 'n=5', ..., 'n=9'. Each value is an array of objects, each with required keys 'isomer' (string) and 'rel_energy' (number, kcal/mol), and an optional key 'point_group' (string).
- Scoring: scored by hidden verifier

### Step 4: Compute temperature-dependent populations
- Role: scored
- Action: For n=7,8,9, compute the canonical probability distribution P(T) at T=25 K and T=100 K using harmonic free energies derived from the M06-2X electronic energies and vibrational frequencies, according to the canonical expression. Write the results to `population_n7_n9.json`.
- Output file: `/app/outputs/population_n7_n9.json`
- Format: json
- Contract: JSON object with keys 'n=7', 'n=8', 'n=9'. Each value is an object with keys '25K' and '100K', each mapping isomer name (string) to probability (number, sum ≈ 1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.json`
- `/app/outputs/population_n7_n9.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.json
- path: `/app/outputs/relative_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zero-point corrected relative energies of all identified H+(NH3)n isomers for n=4-9.
- schema:
  - `type`: object
  - `required`:
    - `n=4`: array
    - `n=5`: array
    - `n=6`: array
    - `n=7`: array
    - `n=8`: array
    - `n=9`: array
  - `items`:
    - `isomer`: string
    - `rel_energy`: number (kcal/mol)

### population_n7_n9.json
- path: `/app/outputs/population_n7_n9.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Canonical probability distributions of H+(NH3)n isomers for n=7-9 at T=25 K and 100 K.
- schema:
  - `type`: object
  - `required`:
    - `n=7`: object
    - `n=8`: object
    - `n=9`: object
  - `items`:
    - `25K`: object mapping isomer to probability
    - `100K`: object mapping isomer to probability

Notes: The hidden checker compares the reported relative energies and populations against paper-reported values with appropriate tolerances. The agent must produce the quantities by actually running the computations; the hidden gold is not revealed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "n=4": "array",
          "n=5": "array",
          "n=6": "array",
          "n=7": "array",
          "n=8": "array",
          "n=9": "array"
        },
        "items": {
          "isomer": "string",
          "rel_energy": "number (kcal/mol)"
        }
      },
      "description": "Zero-point corrected relative energies of all identified H+(NH3)n isomers for n=4-9."
    },
    {
      "file": "population_n7_n9.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "n=7": "object",
          "n=8": "object",
          "n=9": "object"
        },
        "items": {
          "25K": "object mapping isomer to probability",
          "100K": "object mapping isomer to probability"
        }
      },
      "description": "Canonical probability distributions of H+(NH3)n isomers for n=7-9 at T=25 K and 100 K."
    }
  ],
  "notes": "The hidden checker compares the reported relative energies and populations against paper-reported values with appropriate tolerances. The agent must produce the quantities by actually running the computations; the hidden gold is not revealed."
}
```

## How you are scored
A hidden verifier independently scores each stage's output artifact (`relative_energies.json` and `population_n7_n9.json`). It compares your computed quantities to reference values derived from the original paper using appropriate tolerances and structural checks (presence of required topologies and correct qualitative trends). The final reward is a weighted sum of the stage scores. Producing the paper’s reported numbers without actually executing the computational workflow will not satisfy the verifier—it expects values that emerge from a genuine reproduction run.
