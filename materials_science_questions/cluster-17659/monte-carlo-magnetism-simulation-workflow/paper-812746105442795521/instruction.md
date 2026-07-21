# Recursive Multicanonical Spin-Glass Simulation with Finite-Size Scaling

## Problem background
Spin glasses are magnetic systems with quenched random exchange interactions that lead to frustration and many degenerate low-energy configurations. Canonical Monte Carlo simulations of spin glasses suffer from severe slowing down at low temperatures because the system becomes trapped in free-energy valleys. To overcome this, the multicanonical ensemble was introduced, which flattens the energy histogram by using temperature-like parameters that depend on the energy, allowing the simulation to tunnel between high- and low-energy regions. In this task you will implement a recursive multicanonical Monte Carlo method for the 2D Edwards-Anderson Ising spin glass and compute quantitative measures of the method's performance: the ergodicity time and its scaling with system size, as well as the infinite-volume ground-state energy and entropy via finite-size scaling.

## Approach
The multicanonical ensemble weights configurations by exp[-β(E)E+α(E)], where β(E) is chosen to make the energy probability density approximately constant over a chosen energy range from E_max (the maximum energy, taken as 0) down to the ground-state energy E_min. The function α(E) is determined from β(E) by a self-consistency condition. The key is to determine β(E) recursively: start with β(E)=0, perform a short multicanonical simulation to obtain an energy histogram, then update β(E) in the region where the histogram is reliable (above a minimal reliable energy) using the ratio of counts at neighboring energy bins. The recursion is repeated, progressively lowering the accessible energy, until the ground state is reached. After determining the weights, a long production multicanonical simulation is run to measure the ergodicity time τ_L^e (the average number of sweeps to go from E_max to E_min and back), the ground-state energy per spin, and, using the known total number of states Z(0)=2^N, the ground-state entropy per spin. Finally, finite-size scaling of the ground-state energy and entropy versus inverse system volume yields infinite-volume estimates e^0 and s^0, and a log-log fit of τ_L^e versus lattice size L gives the ergodicity time scaling exponent. You will implement the entire pipeline: weight determination, production simulation, and finite-size scaling analysis.

## Reproduction target
Implement the recursive multicanonical weight determination and production simulation for the 2D Edwards-Anderson Ising spin glass with random nearest-neighbor interactions J_ij = ±1, periodic boundary conditions, and the constraint sum J_ij = 0 for each disorder realization. Run the method for lattice sizes L = 4, 12, 24, 48, using 5-10 independent disorder realizations per size. For each realization, obtain the ergodicity time, ground-state energy per spin, and ground-state entropy per spin. Aggregate the results over realizations to compute mean values and standard errors for each L. Perform the following finite-size scaling analyses: (a) a linear fit of the ground-state energy per spin versus 1/V (V=L^2) to obtain the infinite-volume energy e^0 and its error; (b) a linear fit of the ground-state entropy per spin versus 1/V to obtain the infinite-volume entropy s^0 and its error; (c) a log-log fit of the ergodicity time τ_L^e versus L to extract the scaling exponent and its error. Write all final quantities, with uncertainties, to the JSON file `results.json` in the format specified in the output contract.

## Assets

- NumPy: numpy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Recursive multicanonical weight determination
- Role: process
- Action: For each lattice size L in {4,12,24,48} and each disorder realization (5-10 realizations per size), implement the recursive multicanonical weight determination scheme. Start with β^0(E)=0, run Monte Carlo simulations to obtain energy histograms P^n(E), compute median and minimal reliable energies, update β(E) and α(E) using the piecewise recursion rule, and iterate until the ground-state energy E^0 is reached. Store the final weight functions for each realization.
- Evidence: `/app/outputs/recursion_progress.json`

### Step 2: Production multicanonical simulation and measurement
- Role: process
- Action: Using the determined weight functions, perform a long multicanonical simulation for each realization. Measure the ergodicity time τ_L^e (average number of sweeps needed to traverse from E_max to E_min and back). Record the ground-state energy per spin and, using the spectral density normalization Z(0)=2^N, the ground-state entropy per spin. Also record β_max = β(E^0). Accumulate these observables per realization and per L.
- Evidence: `/app/outputs/simulation_measurements.json`

### Step 3: Aggregate, finite-size scaling, and report final results
- Role: scored (load-bearing)
- Action: Aggregate the measured quantities across realizations for each L to compute means and errors (standard error). Perform finite-size scaling: linear fit of ground-state energy per spin vs 1/V to obtain infinite-volume energy e^0 and its error; linear fit of ground-state entropy per spin vs 1/V to obtain infinite-volume entropy s^0 and its error. Perform a log-log fit of ergodicity time τ_L^e vs L to extract the scaling exponent and its error. Write all final results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"L_values": [4,12,24,48], "ergodicity_times": {"4": {"mean": float, "error": float}, "12": {"mean": float, "error": float}, "24": {"mean": float, "error": float}, "48": {"mean": float, "error": float}}, "scaling_exponent": float, "scaling_error": float, "energy_infinite": float, "energy_error": float, "entropy_infinite": float, "entropy_error": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final finite-size scaling results: infinite-volume ground-state energy per spin (e^0) and entropy per spin (s^0), ergodicity time scaling exponent, and per-lattice ergodicity times with uncertainties.
- schema:
  - `type`: object
  - `required`:
    - `L_values`: array of int
    - `ergodicity_times`:
      - `4`:
        - `mean`: float
        - `error`: float
      - `12`:
        - `mean`: float
        - `error`: float
      - `24`:
        - `mean`: float
        - `error`: float
      - `48`:
        - `mean`: float
        - `error`: float
    - `scaling_exponent`: float
    - `scaling_error`: float
    - `energy_infinite`: float
    - `energy_error`: float
    - `entropy_infinite`: float
    - `entropy_error`: float

Notes: All quantities are dimensionless unless specified. The ergodicity time is measured in MC sweeps. The checker will compare the reported values to paper-reported references within appropriate relative and absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "L_values": "array of int",
          "ergodicity_times": {
            "4": {
              "mean": "float",
              "error": "float"
            },
            "12": {
              "mean": "float",
              "error": "float"
            },
            "24": {
              "mean": "float",
              "error": "float"
            },
            "48": {
              "mean": "float",
              "error": "float"
            }
          },
          "scaling_exponent": "float",
          "scaling_error": "float",
          "energy_infinite": "float",
          "energy_error": "float",
          "entropy_infinite": "float",
          "entropy_error": "float"
        }
      },
      "description": "Final finite-size scaling results: infinite-volume ground-state energy per spin (e^0) and entropy per spin (s^0), ergodicity time scaling exponent, and per-lattice ergodicity times with uncertainties."
    }
  ],
  "notes": "All quantities are dimensionless unless specified. The ergodicity time is measured in MC sweeps. The checker will compare the reported values to paper-reported references within appropriate relative and absolute tolerances."
}
```

## How you are scored
The verifier reads your `results.json` and compares each quantity to hidden reference values that represent the expected outcomes of the procedure. The reference values are derived from the original study, with tolerances that accommodate the variability inherent in Monte Carlo simulations and implementation choices. Your score is determined by how closely your results match the reference: for each quantity, if your value falls within the allowed tolerance, you earn full credit for that component; if it exceeds the tolerance, credit decreases monotonically with the deviation. The final reward is a weighted sum of the component scores, with the ergodicity times, scaling exponent, energy, and entropy carrying the bulk of the weight. Intermediate evidence files (`recursion_progress.json`, `simulation_measurements.json`) must be present and consistent with the pipeline but are not numerically scored. Only the execution of the full multicanonical simulation pipeline can produce results within the tolerance; shortcuts or guessed values will not pass the verifier's checks.
