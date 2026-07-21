# Monte Carlo Kakutani Distance Simulation for Ising Systems

## Problem background
The Kakutani distance provides a notion of closeness between probability measures on a configuration space, and can serve as a tool to study real-space renormalization-group flows. When the measures are Gibbs distributions on a lattice system (such as the Ising model), the squared Kakutani distance can be computed by Monte Carlo sampling. The paper demonstrates that such computations are feasible for small Ising systems, both for direct comparison of two known Hamiltonians and for the case where one Hamiltonian is produced by a decimation (block-spin) transformation and is not known in closed form. The task is to reproduce the Monte Carlo estimates of squared Kakutani distances for a set of Ising lattice setups and temperature pairs, providing numerical evidence for the method's applicability.

## Approach
The core idea is to use the identity that the Kakutani distance between two Gibbs measures with known Hamiltonians S and T can be rewritten as an average with respect to the mean Hamiltonian U = (S+T)/2. Concretely, the squared distance can be expressed in terms of averages over Monte Carlo configurations generated according to the Boltzmann weight e^{-U}. Thus, by implementing a heat-bath Markov chain that samples from this weight, one can accumulate an estimate of the distance. For the 2D Ising model, the Hamiltonian is the standard nearest-neighbour ferromagnetic interaction, and the heat-bath algorithm updates each spin probabilistically based on its neighbours. For the 1D chain, the method additionally requires a decimation estimator: at each step, the (unknown) weight of the renormalized Hamiltonian is approximated by simple random sampling over the preimages of the decimated configuration. This approach is applied to compute squared Kakutani distances between Ising Gibbs measures on periodic 8×8 and 4×4 lattices for a range of inverse temperatures, and for a 4-spin 1D chain under a decimation factor 2. All distances are reported in a structured JSON file.

## Reproduction target
Implement and run Monte Carlo simulations for the 2D Ising model on periodic 8×8 and 4×4 lattices and for a 1D periodic Ising chain with decimation. Compute squared Kakutani distances for the following experimental conditions:
- 8×8 lattice, inverse temperature pairs β = 0.1·n and β' = 0.1·(n+1) for n = 1,…,6, with both a cold start (all spins up) and a hot start (random configuration). For each start, perform two independent runs of 10000 random site selections each. Output the two run values for each (n, start) pair.
- 4×4 lattice, same temperature pairs with a cold start, n = 1,…,6, plus a finer grid at high temperatures: β = 0.01·n, β' = 0.01·(n+1) for n = 1,…,9, also with a cold start and 10000 random site selections each. Output a single Monte Carlo estimate per n.
- 1D periodic chain of 4 spins, decimation factor 2. Compute the squared distance for the matched renormalized pair (original inverse temperature β = 0.1, renormalized β' derived from the exact decimation formula) after 6000 random site selections, using N=10 preimage samples in the decimation estimator. Also compute the distance for the nonmatching pair (β0 = β1 = 0.1) after 8100 random site selections with the same N=10. Output both values.
All computed squared distances must be written to /app/outputs/kakutani_distances.json following the output schema.

## Assets
No external datasets, models, or proprietary tools are required. The Ising model Hamiltonian and the heat-bath Monte Carlo algorithm are standard components of statistical mechanics, described in any textbook on the subject. The agent should implement them from the algorithm description provided in the approach and workflow steps. No downloads or pre-trained models are needed; the entire simulation is built from scratch.

## Workflow steps

### Step 1: Monte Carlo Kakutani distance simulation and reporting
- Role: scored (load-bearing)
- Action: Implement and run Monte Carlo simulations for the 2D Ising model on 8×8 and 4×4 periodic lattices and for a 1D periodic Ising chain with decimation, using heat-bath dynamics. For the 2D cases, compute squared Kakutani distances using the mean-Hamiltonian estimator (described in the Approach) at inverse temperature pairs β=(0.1)n, β'=(0.1)(n+1) (n=1..6) for both cold and hot starts, each with two independent runs of 10000 random site selections. For the 4×4 high-temperature case, compute squared distances using the mean-Hamiltonian estimator at β=(0.01)n, β'=(0.01)(n+1) (n=1..9) with a cold start and 10000 selections. For the 1D chain with decimation factor 2, compute distances using the decimation estimator (described in the Approach) with N=10 preimage samples for the matched renormalized pair (β=0.1, β'~0.0099) after 6000 selections and the nonmatching pair (β0=β1=0.1) after 8100 selections. Aggregate all computed squared distances into the output JSON.
- Output file: `/app/outputs/kakutani_distances.json`
- Format: json
- Contract: Object with keys: '8x8_cold' (array of objects, each with 'n' (int, 1-6), 'delta_sq_run1' (float), 'delta_sq_run2' (float)); '8x8_hot' (same structure); '4x4_fine' (array of objects, each with 'n' (int, 1-9), 'delta_sq_mc' (float)); '1d_decimation' (object with 'matched_pair' (float) and 'nonmatching_pair' (float)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kakutani_distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kakutani_distances.json
- path: `/app/outputs/kakutani_distances.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed squared Kakutani distances for all experimental conditions from the MC simulations.
- schema:
  - `type`: object
  - `required`:
    - `8x8_cold`: array of objects with n (int), delta_sq_run1 (float), delta_sq_run2 (float)
    - `8x8_hot`: array of objects with n (int), delta_sq_run1 (float), delta_sq_run2 (float)
    - `4x4_fine`: array of objects with n (int), delta_sq_mc (float)
    - `1d_decimation`: object with matched_pair (float), nonmatching_pair (float)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: All values are squared Kakutani distances (unitless). The checker compares each reported value against hidden paper references with appropriate tolerances; Monte Carlo run-to-run spread is expected.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kakutani_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "8x8_cold": "array of objects with n (int), delta_sq_run1 (float), delta_sq_run2 (float)",
          "8x8_hot": "array of objects with n (int), delta_sq_run1 (float), delta_sq_run2 (float)",
          "4x4_fine": "array of objects with n (int), delta_sq_mc (float)",
          "1d_decimation": "object with matched_pair (float), nonmatching_pair (float)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Computed squared Kakutani distances for all experimental conditions from the MC simulations."
    }
  ],
  "notes": "All values are squared Kakutani distances (unitless). The checker compares each reported value against hidden paper references with appropriate tolerances; Monte Carlo run-to-run spread is expected."
}
```

## How you are scored
A hidden verifier reads your output file kakutani_distances.json and compares each reported squared Kakutani distance against expected reference values obtained by the same Monte Carlo procedure. Because Monte Carlo estimates have inherent run-to-run variation, the verifier applies appropriate tolerances. For the 8×8 and 4×4 lattices, the verifier checks that the values lie within a tolerance band based on the expected statistical spread. For the 1D decimation distances, the verifier uses a tighter absolute tolerance. Additionally, a structural check verifies that the peak in the 8×8 cold-start curve occurs at an intermediate temperature index (n=3 or n=4). Each field contributes a fraction of the total score, which is combined into a final reward between 0 and 1. Reporting numbers alone is not sufficient – they must be the result of an actual Monte Carlo simulation consistent with the described protocol.
