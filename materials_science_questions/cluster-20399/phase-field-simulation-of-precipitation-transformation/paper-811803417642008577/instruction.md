# CVM Order-Disorder Transition on 2D Square Lattice

## Problem background
For a binary alloy on a two-dimensional square lattice, the competition between chemical ordering and thermal disorder leads to an order-disorder phase transition. The Cluster Variation Method (CVM) is a systematic approach to compute the configurational entropy and free energy of such systems. In the CVM square approximation, the free energy is expressed in terms of cluster probabilities that respect the lattice symmetry and the nearest-neighbor interactions. The long-range order (LRO) parameter quantifies the degree of order; it is 1 for a perfectly ordered phase and 0 for a completely disordered phase. This task investigates the temperature dependence of the LRO for a binary A–B square lattice at the equiatomic composition, using the CVM square approximation with specified pair interaction energies.

## Approach
The system is a square lattice divided into two interpenetrating sublattices α and β. At 50 at.% composition and with nearest-neighbor interactions only, the configurational free energy per lattice point is given by the CVM square approximation:

f = ω ∑_{i,j} e_{ij} y_{ij}^{αβ} − k_B T [ 2 ∑_{i,j} L(y_{ij}^{αβ}) − 1/2 (∑_i L(x_i^α) + ∑_j L(x_j^β)) − ∑_{i,j,k,l} L(w_{ijkl}) ]

where ω=4 (half the coordination number), e_{ij} are the nearest-neighbor pair interaction energies, x_i^α (x_j^β) is the point probability of atom i (j) on sublattice α (β), y_{ij}^{αβ} is the pair probability for an i–j pair bridging α and β, w_{ijkl} is the probability of the four-atom square cluster, and L(z) = z ln z − z. The indices i, j, k, l run over the two species A and B. The pair probabilities and point probabilities are expressed as marginal sums of the square cluster probabilities. The chosen energy parameters are e_AA = e_BB = 1 and e_AB = 0, which sets the energy scale and normalizes all temperatures to units of e_AA.

The free energy is minimized with respect to the square cluster probabilities w_{ijkl} under the normalization constraint ∑ w_{ijkl} = 1, yielding the equilibrium cluster distribution at each temperature. From these, the point correlation functions are obtained and the long-range order parameter is defined as LRO = x_A^α − x_A^β (which equals 1 for perfect order and 0 for complete disorder). The minimization is performed numerically for a series of reduced temperatures T/e_AA ranging from 0 to 3. The computational workflow consists of a single step: solve the constrained minimization at each temperature and output the resulting LRO values.

## Reproduction target
Produce a CSV file containing the long-range order parameter LRO as a function of the reduced temperature T/e_AA. The table must span the temperature range from 0 to 3 with sufficient density (at least enough points to clearly resolve the order-disorder transition). The LRO should be close to 1 at very low temperature and drop to values near zero above the transition, demonstrating the second-order nature of the order-disorder transition.

## Assets

- Python scientific packages (numpy, scipy): https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Compute LRO vs Temperature
- Role: scored (load-bearing)
- Action: Implement the Cluster Variation Method (CVM) square approximation free energy for a binary A-B square lattice at 50 at.% composition (Eq. 12 in the paper's text) with nearest-neighbor pair interaction energies e_AA = e_BB = 1, e_AB = 0 (energy unit e_AA). Minimize the free energy with respect to the square cluster probabilities at each temperature in a range from T/e_AA = 0 to 3, obtaining the equilibrium cluster probabilities. Derive the Long Range Order (LRO) parameter from the point correlation functions. Output a CSV with two columns: temperature_normalized (float) and LRO (float), containing data points sufficient to resolve the order-disorder transition.
- Output file: `/app/outputs/step_01_lro_vs_temperature.csv`
- Format: csv
- Contract: temperature_normalized (float), LRO (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lro_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lro_vs_temperature.csv
- path: `/app/outputs/step_01_lro_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Long-range order parameter as a function of normalized temperature computed from the CVM square approximation for a binary A-B square lattice at 1:1 stoichiometry.
- schema:
  - `type`: table
  - `required_columns`: `temperature_normalized`, `LRO`
  - `units`:
    - `temperature_normalized`: dimensionless (T/e_AA)
    - `LRO`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lro_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_normalized",
          "LRO"
        ],
        "units": {
          "temperature_normalized": "dimensionless (T/e_AA)",
          "LRO": "dimensionless"
        }
      },
      "description": "Long-range order parameter as a function of normalized temperature computed from the CVM square approximation for a binary A-B square lattice at 1:1 stoichiometry."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated automatically by a hidden verifier. The verifier reads the uploaded CSV and extracts the transition temperature, defined as the lowest reduced temperature at which LRO falls below 0.01. This transition temperature is compared to a reference value (not disclosed to you) using an absolute tolerance. Additionally, the verifier checks the overall shape of the LRO vs. temperature curve at several fixed temperatures: near T/e_AA = 0.1 (expecting LRO close to 1), around T/e_AA = 2.0 (expecting an intermediate value), and near T/e_AA = 2.5 (expecting LRO essentially zero). The final score is a weighted combination: 70% for transition temperature accuracy and 30% for the consistency of the curve shape at the designated checkpoints. Ensure your CSV is densely sampled and that the LRO values are derived directly from the equilibrium cluster probabilities obtained from the free-energy minimization.
