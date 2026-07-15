# Computational Study of Magnetism in Ni Nano-clusters

## Problem background
Transition-metal nano-clusters exhibit magnetic properties that differ strongly from the bulk, with total magnetic moment per atom oscillating as a function of cluster size. Understanding these oscillations requires accounting for both spin and orbital contributions, as well as surface enhancement and quantum confinement effects. In the case of Ni_n clusters (n ~ 10–60), experiments have revealed distinct features: a sharp minimum near n=13 and other minima at larger sizes, along with an overall enhancement over the bulk moment. Reproducing these observations from a physics-based tight-binding model is an open challenge that tests our understanding of nano-cluster magnetism.

## Approach
We adopt a self-consistent tight-binding framework that combines bulk d-band Hamiltonian with Slater-Koster hopping and spin-orbit coupling, intra-atomic d-d Coulomb and exchange interactions that drive spin and orbital polarization, an empty s' orbital attached to each surface atom with a coordination-dependent hopping to simulate electron spillover, and a surface valence orbital shift proportional to the s' occupation. The Hamiltonian parameters are taken from standard bulk fits, with Hubbard U = 2.6 eV, Stoner exchange I = 1.12 eV, and SOC strength ξ = 0.073 eV. The self-consistent solution starts from a non-polarized density matrix, adds a small spin polarization, and iterates until the single-site density matrices converge. Orbital and spin moments are extracted from the converged density matrix. The computations are applied to the MIAL icosahedral cluster structures for sizes n=9–60, excluding six sizes that may have structural artifacts.

## Reproduction target
Produce a CSV file, total_moments.csv, containing the cluster size n and the average total magnetic moment per atom (sum of spin and orbital contributions, in Bohr magnetons) for each Ni_n cluster with n from 9 to 60, except n=21,29,33,37,40,59. The moments must be obtained from the self-consistent tight-binding model implemented with U = 2.6 eV. The goal is to capture the overall magnitude and the characteristic size-dependent oscillations of the magnetic moment, including the existence and positions of local minima.

## Assets

- MIAL Ni_n cluster geometries: 10.1103/PhysRevB.54.5961

## Workflow steps

### Step 1: Obtain Ni cluster geometries
- Role: process
- Action: Obtain or generate the Cartesian coordinates of Ni_n clusters for sizes n=9–60, excluding n=21,29,33,37,40,59 as suspect structures. Use the MIAL icosahedral growth structures described in the literature. The structures should be in a form suitable for constructing the tight-binding Hamiltonian.
- Evidence: `/app/outputs/geometries_summary.txt`

### Step 2: Self-consistent tight-binding simulation
- Role: process
- Action: Implement the full tight-binding Hamiltonian including bare hopping, spin-orbit coupling (ξ=0.073 eV), intra-atomic d-d interaction with U=2.6 eV and Stoner exchange I=1.12 eV, an empty surface s' orbital coupled to surface atoms, and a surface valence orbital shift. Use the bulk TB parameters (orbital energies, hopping integrals) from standard references. The hopping to the surface s' orbital is given by t^{ss'}(Z_{i'}) = V_{ss'σ} √(Z_max - Z_{i'}) with V_{ss'σ} = -2.460 eV and Z_max = 15.8. The surface valence orbital energy shift is Δε_{i'}(n_{s'}^{i'}) = χ n_{s'}^{i'} with χ = 2.3 eV. For each cluster geometry, start from a non-polarized density matrix, turn on interactions, and iterate until self-consistency of the single-site density matrices. Store the converged density matrices.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Compute total magnetic moments
- Role: scored (load-bearing)
- Action: From the self-consistent single-site density matrices, compute per-atom spin and orbital magnetic moments using the standard operators (spin via Pauli matrices, orbital via angular momentum matrices in the d-orbital basis). Calculate the average total magnetic moment per atom (spin+orbital) for each cluster size, excluding the six suspect clusters (n=21,29,33,37,40,59). Write the results to total_moments.csv with columns: n (cluster size) and total_moment_per_atom (in Bohr magnetons).
- Output file: `/app/outputs/total_moments.csv`
- Format: csv
- Contract: Columns: n (integer), total_moment_per_atom (float, Bohr magnetons).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_moments.csv
- path: `/app/outputs/total_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average total magnetic moment per atom (spin+orbital) for each Ni_n cluster size n=9–60, excluding n=21,29,33,37,40,59. Each row corresponds to one cluster size.
- schema:
  - `type`: table
  - `required_columns`: `n`, `total_moment_per_atom`
  - `units`:
    - `n`: integer (cluster size)
    - `total_moment_per_atom`: float (Bohr magnetons)

Notes: The hidden checker compares the reported total moments to reference values obtained from a published source and verifies the presence of oscillation minima.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "total_moment_per_atom"
        ],
        "units": {
          "n": "integer (cluster size)",
          "total_moment_per_atom": "float (Bohr magnetons)"
        }
      },
      "description": "Average total magnetic moment per atom (spin+orbital) for each Ni_n cluster size n=9–60, excluding n=21,29,33,37,40,59. Each row corresponds to one cluster size."
    }
  ],
  "notes": "The hidden checker compares the reported total moments to reference values obtained from a published source and verifies the presence of oscillation minima."
}
```

## How you are scored
A hidden verifier will compare your total_moments.csv against reference values and check for the presence and correct locations of local minima in the size dependence. The final reward combines moment accuracy and minima correctness, weighted appropriately. The verifier uses a reasonable tolerance to account for implementation differences. Simply returning expected values without running the simulation will not succeed because the verifier expects a consistent physical result derived from the Hamiltonian.
