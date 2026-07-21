# MC loop-flip acceptance rates in biquadratic Heisenberg model

## Problem background
Classical Heisenberg antiferromagnets on the geometrically frustrated pyrochlore lattice can develop spin-ice type degeneracies at low temperatures. When biquadratic interactions (of strength b > 0) are added, the system enters a nematic phase in which spins spontaneously select a common axis while still obeying local 'two-up two-down' ice rules. Standard single-spin-flip Monte Carlo simulations fail to sample the degenerate ice-rule manifold efficiently at low temperature due to large energy barriers. A loop algorithm that flips entire closed chains of alternating spins can overcome this barrier, but its efficiency strongly depends on how the spins on a loop are updated. This work compares three different loop-flip methods — flip_xyz, flip_parallel, and rotate — and investigates which method yields the highest acceptance rate as a function of the biquadratic coupling b at low temperature.

## Approach
We implement the classical bilinear-biquadratic Heisenberg model on a pyrochlore lattice with system size 16×8³ spins (nearest-neighbor exchange J = 1, biquadratic coupling b > 0) and an extended loop algorithm. Because the Hamiltonian is O(3) symmetric and lacks a fixed anisotropy axis, the projection axis needed to build loops is determined on the fly: a small random subset of tetrahedra is chosen, and an iterative procedure refines a unit vector whose direction approximates the common axis selected by the biquadratic interaction. Using this axis, spins are painted black or white according to the sign of their projection. A closed loop of alternating black/white spins is then constructed; after a loop is formed, all its spins are updated using one of three methods: (1) flip_xyz — invert every spin component, (2) flip_parallel — reverse only the component parallel to the projection axis while preserving the perpendicular component, or (3) rotate — cyclically permute the spins along the loop. For each b value in {0.05, 0.1, 0.2, 0.5, 1.0, 1.5}, we perform Monte Carlo simulations at a very low temperature T = 0.02, combining single-spin updates (Marsaglia’s method) for ergodicity with loop updates, and record the average acceptance rates P_xyz, P_parallel, and P_rotate. By comparing these rates, we can identify the most efficient loop-flip method in different b regimes.

## Reproduction target
Produce a CSV file (acceptance_rates.csv) containing the estimated acceptance rates of the three loop-flip methods for each biquadratic coupling strength b in {0.05, 0.1, 0.2, 0.5, 1.0, 1.5} at T = 0.02. The columns must be: b, P_xyz, P_parallel, P_rotate. Each row corresponds to one b value. The acceptance rates are computed from sufficiently long Monte Carlo simulations that implement the model and the extended loop algorithm as described above. The goal is to correctly capture how the relative efficiency of the three flip methods changes with b.

## Assets

- Python: python3
- NumPy: numpy

## Workflow steps

### Step 1: Compute loop-flip acceptance rates at T=0.02
- Role: scored (load-bearing)
- Action: Implement the classical bilinear-biquadratic Heisenberg model on a pyrochlore lattice (system size 16×8³ spins, J=1) and the extended loop algorithm with on-the-fly projection axis determination. For each biquadratic coupling strength b in {0.05, 0.1, 0.2, 0.5, 1.0, 1.5}, perform Monte Carlo simulations at T=0.02 using single-spin flips and loop flips with three methods: flip_xyz, flip_parallel, rotate. Measure and record the acceptance rates P_xyz, P_parallel, P_rotate for each b value.
- Output file: `/app/outputs/acceptance_rates.csv`
- Format: csv
- Contract: CSV file with columns: b (float), P_xyz (float), P_parallel (float), P_rotate (float). Each row corresponds to one b value. Values should be in [0,1].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/acceptance_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### acceptance_rates.csv
- path: `/app/outputs/acceptance_rates.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Acceptance rates of loop-flip methods at T=0.02 as a function of b. The ordering among the three methods at specific b values is verified.
- schema:
  - `type`: table
  - `required_columns`: `b`, `P_xyz`, `P_parallel`, `P_rotate`
  - `units`: object

Notes: The acceptance rates are scored by checking that the relative ordering at b=0.05, 0.2, and 1.5 matches the expected structural pattern (e.g., P_parallel > P_rotate > P_xyz at small b, etc.) with a small numerical tolerance for stochastic noise.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "acceptance_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "b",
          "P_xyz",
          "P_parallel",
          "P_rotate"
        ],
        "units": {}
      },
      "description": "Acceptance rates of loop-flip methods at T=0.02 as a function of b. The ordering among the three methods at specific b values is verified."
    }
  ],
  "notes": "The acceptance rates are scored by checking that the relative ordering at b=0.05, 0.2, and 1.5 matches the expected structural pattern (e.g., P_parallel > P_rotate > P_xyz at small b, etc.) with a small numerical tolerance for stochastic noise."
}
```

## How you are scored
A hidden verifier will check your acceptance_rates.csv. The verifier does not demand exact numerical agreement with published values; instead, it performs a structural audit: it checks that the relative ordering among P_xyz, P_parallel, and P_rotate at several chosen b values matches an expected pattern. For example, it may verify which method is largest, which is smallest, and whether one dominates the others in a certain range, all within a small tolerance to account for stochastic noise and implementation differences. Each checked condition contributes a fraction of the final reward. Providing only a reasonable CSV that follows the required schema and contains values in [0,1] is insufficient; the ordering between the methods must respect the hidden structural criteria derived from the physics of the model.
