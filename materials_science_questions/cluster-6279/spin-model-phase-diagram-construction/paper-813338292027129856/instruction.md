# Spin-1 Bose Gas Mixture Ground State Energy Minimization

## Problem background
We consider a mixture of two species of spin-1 Bose gases with both intraspecies and interspecies spin-exchange interactions in a weak magnetic field. Under the single-mode approximation, the many-body Hamiltonian reduces to a model of coupled giant spins. The ground state is characterized by three integer quantum numbers: the total spin of species a (S_a), the total spin of species b (S_b), and the total spin of the mixture (S), with the magnetic field favouring the fully stretched state S_z = S. These numbers are determined by minimizing the energy

E(S_a, S_b, S) = (c^a - c^{ab}) * [S_a*(S_a+1)]/2 + (c^b - c^{ab}) * [S_b*(S_b+1)]/2 + c^{ab} * [S*(S+1)]/2 - γ * B * S

subject to the triangular constraint |S_a - S_b| ≤ S ≤ S_a + S_b and the allowed ranges 0 ≤ S_a ≤ N_a, 0 ≤ S_b ≤ N_b, where N_a and N_b are the conserved atom numbers, c^a and c^b are intraspecies spin coupling strengths, c^{ab} is the interspecies spin coupling strength, B is the magnetic field magnitude, and γ (identical for both species) is the gyromagnetic ratio. The resulting ground-state spin values (S_a^m, S_b^m, S^m) define the phase diagram of the mixture across different coupling and field regimes. Your task is to compute these spin quantum numbers for a representative set of parameter points.

## Approach
The ground state is obtained by a discrete minimization of the energy over integer S_a, S_b, and S within their allowed ranges and the triangular constraint. The problem has no external data; it is a purely computational optimization over a finite set of integer triples. Implement a solver that, for each supplied parameter tuple (c^a, c^b, c^{ab}, B, N_a, N_b), evaluates all permissible combinations and selects the triple that minimizes the energy. The magnetic field term −γ B S favours the largest possible S consistent with the other terms, so the global minimum is always found with S_z = S. You will then apply this solver to a predefined grid of parameter points that spans the main physical regimes: zero interspecies coupling (c^{ab}=0), ferromagnetic interspecies coupling (c^{ab}<0), and antiferromagnetic interspecies coupling (0 < c^{ab} ≤ 2γB and c^{ab} > 2γB). The output is a CSV file of computed (S_a^m, S_b^m, S^m) for each point.

## Reproduction target
Produce a CSV file named ground_states.csv containing the computed ground-state total spin quantum numbers for a comprehensive set of parameter points. The CSV must contain the columns: c_a, c_b, c_ab, B, N_a, N_b, S_a, S_b, S. Each row corresponds to a single parameter point, where c_a, c_b, c_ab are the coupling strengths (floats), B is the magnetic field (float), N_a and N_b are the atom numbers (positive integers), and S_a, S_b, S are the minimizing spin quantum numbers (integers) obtained by your energy minimization. Your parameter grid should cover the key regimes identified in the approach: c^{ab}=0 with a representative range of c^a and c^b; c^{ab}<0 for various c^a and c^b (excluding the unsolved first quadrant c^a>0, c^b>0); 0 < c^{ab} ≤ 2γB; and c^{ab} > 2γB. Use atom numbers that are modest (e.g., N_a=10, N_b=10) and vary B to explore the field dependence. The grid does not need to include points inside regimes that are unsolved in the analytic literature or that require atom numbers exceeding a certain threshold (N > N*); the hidden verifier will similarly avoid those. Your goal is to produce a complete, correctly minimized dataset.

## Assets

- Python interpreter (>=3.8): python3
- NumPy: numpy

## Workflow steps

### Step 1: Energy minimization and ground-state computation
- Role: scored (load-bearing)
- Action: Implement the minimization of the energy E(S_a,S_b,S) = (c^a - c^{ab}) * S_a*(S_a+1)/2 + (c^b - c^{ab}) * S_b*(S_b+1)/2 + c^{ab} * S*(S+1)/2 - gamma * B * S over integer S_a in [0, N_a], S_b in [0, N_b], and integer S satisfying |S_a - S_b| <= S <= S_a + S_b, with the magnetic field favoring S_z=S. For each parameter point given by (c^a, c^b, c^{ab}, B, N_a, N_b), compute the minimizing total spins S_a^m, S_b^m, S^m and write a row to the output CSV. The parameter grid should cover the key regimes: c^{ab}=0, c^{ab}<0, 0<c^{ab}<=2*gamma*B, and c^{ab}>2*gamma*B, with representative N_a and N_b values.
- Output file: `/app/outputs/ground_states.csv`
- Format: csv
- Contract: columns: c_a (float), c_b (float), c_ab (float), B (float), N_a (int), N_b (int), S_a (int), S_b (int), S (int). Each row corresponds to a single parameter point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ground_states.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ground_states.csv
- path: `/app/outputs/ground_states.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ground state total spin quantum numbers for each parameter point. The checker compares S_a, S_b, and S against exact analytic predictions derived from the paper.
- schema:
  - `type`: table
  - `required_columns`: `c_a`, `c_b`, `c_ab`, `B`, `N_a`, `N_b`, `S_a`, `S_b`, `S`
  - `units`: object

Notes: Test points avoid the unsolved first quadrant for c^{ab}<0, and regimes C2/E2 when N <= N*. Only exact integer matches are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ground_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "c_a",
          "c_b",
          "c_ab",
          "B",
          "N_a",
          "N_b",
          "S_a",
          "S_b",
          "S"
        ],
        "units": {}
      },
      "description": "Ground state total spin quantum numbers for each parameter point. The checker compares S_a, S_b, and S against exact analytic predictions derived from the paper."
    }
  ],
  "notes": "Test points avoid the unsolved first quadrant for c^{ab}<0, and regimes C2/E2 when N <= N*. Only exact integer matches are required."
}
```

## How you are scored
A hidden verifier independently checks your ground_states.csv. For each row, it computes the expected integer values of S_a, S_b, and S using analytic ground-state rules that are exact within the tested regimes. Your computed (S_a, S_b, S) are compared to those expected values; all three integers must match exactly. The final reward is 1.0 if every row in the tested subset matches, otherwise it is proportional to the fraction of rows where all three spin numbers are correct. The test points are selected to stay within the well-solved parts of parameter space, so you do not need to handle regimes where the analytic solution is not available. Your task is to make the discrete minimization procedure yield the correct integer ground-state spins; a correct implementation will pass exactly.
