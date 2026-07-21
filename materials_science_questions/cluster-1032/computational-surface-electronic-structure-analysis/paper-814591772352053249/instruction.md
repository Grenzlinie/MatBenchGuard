# Layer-DMFT with embedding potential for IDHB surface

## Problem background
The Ising-like dynamic Hubbard (IDHB) model introduces a pseudo-spin auxiliary degree of freedom coupled to the electron occupation, which breaks electron-hole symmetry. In the anti-adiabatic limit, where the pseudo-spin energy scale is large compared to the hopping, the model maps to an effective correlated-hopping Hamiltonian: the hopping amplitude between sites depends on their local occupancies, taking different values when the sites are empty, singly occupied, or doubly occupied. This electron-hole asymmetry may affect how charge distributes between the interior and the surface of a semi-infinite lattice. The task is to compute, using dynamical mean-field theory (DMFT) with an embedding potential, the quasi-particle weight as a function of filling on a Bethe lattice (quantifying the asymmetry) and the layer-resolved electron densities for N surface layers coupled to a bulk substrate (revealing any surface charge redistribution).

## Approach
The core method is single-site DMFT with an exact-diagonalization impurity solver using a finite bath discretisation. The anti-adiabatic limit of the IDHB model yields an effective Hamiltonian with correlated hopping amplitudes t, t·S, and t·S² depending on the local occupancy of the two sites involved, where S = 1/√(1+g²) and g is the pseudo-spin coupling constant. The workflow has three conceptual stages. First, a Bethe-lattice DMFT benchmark: solve a single-impurity Anderson model self-consistently for a semi-circular density of states, extracting the quasi-particle weight Z from the self-energy at each filling. Second, a bulk cubic-lattice DMFT calculation: obtain the homogeneous self-energy for the substrate and construct the embedding potential that captures the effect of the semi-infinite bulk on the surface layers, using the recursive relation for the surface Green's function of a semi-infinite stack. Third, a layer-DMFT calculation: set up N explicit surface layers, each mapped to its own impurity model; the layer Green's functions include the embedding potential as a self-energy term on the deepest layer; the impurity models are solved by exact diagonalisation, and the layer self-energies are iterated together with the lattice Green's functions until self-consistency. The converged layer Green's functions yield the electron occupations per layer.

## Reproduction target
Produce two scored CSV files under /app/outputs.

1. **Quasi-particle weight vs filling** (`quasiparticle_weight.csv`): For the IDHB model on a Bethe lattice in the anti-adiabatic limit (omega0 = 50 taken as the large-scale limit), with on-site Coulomb U = 0, compute the quasi-particle weight Z as a function of electron filling n for coupling constants g = 0.5, 1.0, and 1.5. Cover the full filling range n ∈ [0, 2] with at least 10 filling points per g value.

2. **Layer-resolved electron densities** (`layer_densities.csv`): For a semi-infinite cubic lattice with intra-layer dispersion ε∥(k) = −2(cos kx + cos ky), inter-layer hopping t⊥ = t = 1, and N = 5 explicit surface layers, set the bulk filling to n_b = 1.8 and the coupling to g = 1.5 in the anti-adiabatic limit (omega0 = 50). Compute the electron occupation n_j for each layer j = 1, …, 5 at U = 0 and at U = 2.

## Assets

- NumPy: https://pypi.org/project/numpy
- SciPy: https://pypi.org/project/scipy

## Workflow steps

### Step 1: Bethe lattice DMFT benchmark for quasi-particle weight
- Role: scored
- Action: Implement single-site DMFT with exact diagonalization (6 bath sites) for the IDHB model in the anti-adiabatic limit (omega0=50) on a Bethe lattice. Compute the quasi-particle weight Z as a function of electron filling n for coupling constants g=0.5, 1.0, 1.5 at U=0. Write the Z(n) values to quasiparticle_weight.csv.
- Output file: `/app/outputs/quasiparticle_weight.csv`
- Format: csv
- Contract: Columns: g (float), filling (float), Z (float). At least 10 filling points per g covering the range.
- Scoring: scored by hidden verifier

### Step 2: Bulk DMFT for substrate self-energy and embedding potential
- Role: process
- Action: Perform single-site DMFT for a bulk cubic lattice substrate (intra-layer dispersion, inter-layer hopping) for the IDHB Hamiltonian in the anti-adiabatic limit. Obtain the bulk self-energy and construct the embedding potential using the recursive relation for the semi-infinite bulk Green's function.
- Evidence: none

### Step 3: Layer-DMFT simulation of semi-infinite surface with embedding
- Role: process
- Action: Set up the layer Hamiltonian for N=5 surface layers on a cubic lattice coupled to the semi-infinite bulk substrate. Initialize layer self-energies. Perform the embedding-DMFT loop: for each layer, map to a single-impurity Anderson model with 6 bath sites and solve by exact diagonalization to obtain layer self-energies; recompute on-site layer Green's functions using the embedding potential and DMFT self-consistency condition. Iterate until convergence.
- Evidence: none

### Step 4: Extraction of layer-resolved electron densities
- Role: scored (load-bearing)
- Action: From the converged layer-DMFT solution, compute the electron occupation n_j for each layer j=1..5 for bulk filling n_b=1.8, g=1.5, omega0=50, at U=0 and U=2. Write the layer densities to layer_densities.csv.
- Output file: `/app/outputs/layer_densities.csv`
- Format: csv
- Contract: Columns: layer (int, 1..5), U (float, one of [0.0,2.0]), n (float). One row per layer and U.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/quasiparticle_weight.csv`
- `/app/outputs/layer_densities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### quasiparticle_weight.csv
- path: `/app/outputs/quasiparticle_weight.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Quasi-particle weight Z vs electron filling for different coupling constants g.
- schema:
  - `type`: table
  - `required_columns`: `g`, `filling`, `Z`
  - `units`:
    - `g`: dimensionless
    - `filling`: dimensionless
    - `Z`: dimensionless

### layer_densities.csv
- path: `/app/outputs/layer_densities.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Layer-resolved electron density for N=5 surface layers.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `U`, `n`
  - `units`:
    - `layer`: integer index
    - `U`: t
    - `n`: electrons/site

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "quasiparticle_weight.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "g",
          "filling",
          "Z"
        ],
        "units": {
          "g": "dimensionless",
          "filling": "dimensionless",
          "Z": "dimensionless"
        }
      },
      "description": "Quasi-particle weight Z vs electron filling for different coupling constants g."
    },
    {
      "file": "layer_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "U",
          "n"
        ],
        "units": {
          "layer": "integer index",
          "U": "t",
          "n": "electrons/site"
        }
      },
      "description": "Layer-resolved electron density for N=5 surface layers."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently scores each scored output file and combines them by weight into a final reward in [0, 1]. For `quasiparticle_weight.csv`, the verifier compares your computed Z values against a hidden reference at selected fillings and checks structural trends (e.g. the dependence of Z on filling and coupling). For `layer_densities.csv`, the verifier compares each layer density to hidden reference values and verifies structural patterns across layers at each U. Reporting a number without genuinely executing the DMFT self-consistency loops will not receive credit, because the hidden tolerances are calibrated to the natural spread of an independent honest re-implementation. Install any required packages, run the complete workflow, and write both files to /app/outputs.
