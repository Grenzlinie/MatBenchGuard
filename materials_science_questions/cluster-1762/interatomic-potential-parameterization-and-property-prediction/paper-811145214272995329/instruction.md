# Metallic Cluster Ground-State Energy and Magic Numbers

## Problem background
Metallic clusters exhibit striking size-dependent stability and energetics, making them important for nanotechnology and catalysis. A central question is predicting which cluster sizes are especially stable (magic numbers) and knowing their ground-state binding energies. The quasi-classical linearized Thomas-Fermi theory provides a simplified description of the bonding electrons in large, heavy-metal clusters, yielding effective inter-ionic potentials and closed-form expressions for the energy. This allows the computation of equilibrium geometries and mass-abundance spectra, from which magic numbers emerge. This task requires you to implement that theory for a homo-atomic iron cluster and compute its ground-state energy per atom across a range of sizes, as well as identify the geometric magic numbers.

## Approach
Implement the linearized Thomas-Fermi model for a homo-atomic metallic cluster composed of heavy ions. Start by estimating the effective valence charge z* for iron using a standard atomic screening formula that depends on the atomic number and nominal valence. The electronic structure is described as a slightly inhomogeneous electron liquid; linearization introduces a screening wavevector q that is treated variationally. This leads to an inter-ionic potential of screened Coulomb (Buckingham) form expressed in dimensionless coordinates x = q r. The potential energy of a given ionic configuration is the sum of pairwise interactions. The kinetic energy and exchange energy have simple analytical forms in terms of q and z*.

For each cluster size N from 2 to 80, find equilibrium geometries (isomers) by minimizing the total potential energy over dimensionless coordinates with a gradient-based method. For each geometry, determine the optimal screening wavevector q by minimizing the quasi-classical energy (kinetic plus potential), then add the exchange energy to obtain the total binding energy. The lowest energy among the isomers is the ground-state energy for that N. Record the energy per atom in eV.

From the sequence of ground-state energies across N, compute the mass-abundance spectrum D(N) = E(N+1) + E(N-1) - 2E(N). Positive local maxima of D(N) indicate geometric magic numbers: cluster sizes that are particularly stable.

## Reproduction target
For a homo-atomic iron (Fe) cluster with effective valence charge z* = 0.57, produce two scored outputs:
1. A CSV file `ground_state_energies.csv` containing the ground-state binding energy per atom (in eV) for every cluster size N from 2 to 80.
2. A JSON array `geometric_magic_numbers.json` listing those cluster sizes N (integers) that are geometric magic numbers, identified as positive local maxima of the mass-abundance spectrum D(N).

## Assets

- SciPy: scipy

## Workflow steps

### Step 1: Estimate effective valence charge for Fe
- Role: process
- Action: Compute the effective valence charge z* for Fe (atomic number Z=26, nominal valence z=2) using the atomic screening formula: q = 0.84 * Z^(1/3), R = 1 a.u., z* = z * (1 + q*R) * exp(-q*R). Save the computed value for later use.
- Evidence: `/app/outputs/zstar.txt`

### Step 2: Compute ground-state energies for Fe clusters
- Role: process
- Action: For each cluster size N from 2 to 80, minimize the total potential energy over dimensionless coordinates using gradient descent to find equilibrium geometries (isomers). For each geometry, compute the variational screening wavevector q that minimizes the quasi-classical energy (kinetic + potential), then add exchange energy to obtain total binding energy. Select the lowest energy as the ground-state energy for that N. Record the energy per atom in eV.
- Evidence: `/app/outputs/energies_raw.json`

### Step 3: Save ground-state energies as CSV
- Role: scored
- Action: Write the ground-state binding energy per atom for each cluster size N to a CSV file with columns N (integer) and energy_per_atom (float, eV).
- Output file: `/app/outputs/ground_state_energies.csv`
- Format: csv
- Contract: Columns: N (integer), energy_per_atom (float)
- Scoring: scored by hidden verifier

### Step 4: Compute geometric magic numbers
- Role: scored (load-bearing)
- Action: From the ground-state energies E(N), compute the mass-abundance spectrum D(N) = E(N+1) + E(N-1) - 2E(N) for N from 2 to 79. Identify the N where D(N) is a positive local maximum (greater than both neighbors). Output a JSON array of these N (integers).
- Output file: `/app/outputs/geometric_magic_numbers.json`
- Format: json
- Contract: JSON array of integers, e.g. [6, 11, 13, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ground_state_energies.csv`
- `/app/outputs/geometric_magic_numbers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ground_state_energies.csv
- path: `/app/outputs/ground_state_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ground-state binding energy per atom for Fe clusters of sizes N=2..80.
- schema:
  - `type`: table
  - `required_columns`: `N`, `energy_per_atom`
  - `units`:
    - `energy_per_atom`: eV

### geometric_magic_numbers.json
- path: `/app/outputs/geometric_magic_numbers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: List of cluster sizes N that are geometric magic numbers.
- schema:
  - `type`: array
  - `items`:
    - `type`: integer

Notes: The checker will compare the energy per atom at N=13 to a hidden reference, and match the list of magic numbers to a hidden gold list.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ground_state_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "energy_per_atom"
        ],
        "units": {
          "energy_per_atom": "eV"
        }
      },
      "description": "Ground-state binding energy per atom for Fe clusters of sizes N=2..80."
    },
    {
      "file": "geometric_magic_numbers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "integer"
        }
      },
      "description": "List of cluster sizes N that are geometric magic numbers."
    }
  ],
  "notes": "The checker will compare the energy per atom at N=13 to a hidden reference, and match the list of magic numbers to a hidden gold list."
}
```

## How you are scored
A hidden verifier will examine your output files. The `ground_state_energies.csv` and `geometric_magic_numbers.json` are both scored against reference results derived from the paper's reported findings. Each artifact contributes a weighted share to the final reward. You must produce the required outputs in the exact formats specified; the verifier checks both the structure (columns, types) and the numerical content. Simply reporting a number without the computation will not earn credit; the verifier expects the outputs to reflect a genuine execution of the described workflow.
