# Thermodynamic Phase Diagram of a Non-Isovalent Alloy via Cluster-Variation Method

## Problem background
The (GaAs)1−xGe2x alloy is a non‑isovalent semiconductor solid solution where the two interpenetrating fcc sublattices can be occupied either equally by Ga and As (pseudo‑diamond) or preferentially by one species (pseudo‑zinc blende, ZB). A ZB↔D order–disorder transition is observed experimentally at finite compositions, but its origin remains controversial. A three‑dimensional bulk thermodynamic model based on the cluster‑variation method (CVM) has been proposed to describe this transition, using effective interactions derived from first‑principles superlattice calculations. The central question is whether such a bulk equilibrium thermodynamic description can reproduce the observed critical composition in the relevant temperature range when realistic interaction energies are used. In this task you will implement the CVM pair‑approximation model for this alloy and compute the resulting phase diagram, focusing on the percolation limit and tricritical points that encapsulate the essential physics.

## Approach
The model treats the (GaAs)1-xGe2x alloy as a three‑species zinc‑blende/diamond lattice with Ga, As, and Ge atoms, subject to the constraints: fixed overall Ge composition, no ordering of Ge on the two sublattices, and no Ga–Ga or As–As bonds (ΔZv = ±2 bonds). The excess enthalpy includes an effective pairwise Ising‑like term (N_D + N_A) J(q), where J(q) depends on the charge‑transfer parameter q and the average bond‑energy δ, plus inter‑bond Madelung contributions from first-, second-, and third‑neighbor bond pairs, parameterized by K^(1), K^(2), K^(3). The configurational entropy is expressed in the CVM pair approximation using nearest‑neighbor pair probabilities, with longer‑range pair probabilities related to the nearest‑neighbor ones via a superposition (mean‑field) approximation. The free energy ΔF = ΔH − T S is minimized numerically with respect to the independent correlation functions for a dense grid of compositions x and temperatures T, for both the uncompensated (q = 0) and fully compensated (q = 1/4) cases. From the minimized free energy you identify the order‑disorder transition line (ZB↔D), extract the percolation limit as x at infinite temperature, and locate the tricritical point (x_tc, T_tc) where the transition changes from second‑ to first‑order.

## Reproduction target
Using the given energy parameters (δ = 0.162 eV, J(q=0) = 0.162 eV, J(q=1/4) = 0.109 eV, K^(1) = 0.035 eV, K^(2) = 0.020 eV, K^(3) = 0.017 eV) and the constraints listed in the Approach, compute the equilibrium phase diagram of the (GaAs)1-xGe2x alloy. Determine the following quantities:

- The percolation limit x_c (the critical composition at infinite temperature).
- The tricritical point (x_tc, T_tc) for the uncompensated case (q = 0).
- The tricritical point (x_tc, T_tc) for the compensated case (q = 1/4).

Write these numerical results to cvm_phase_diagram_results.json according to the schema described in the Workflow steps. The values must be derived from your numerical minimization; simply guessing or reporting the paper’s published numbers is not sufficient.

## Assets
No external datasets, model weights, or supplementary files are required. All needed physical parameters and the description of the CVM pair approximation, the superposition relations, and the free‑energy expression are fully contained in this instruction. Use standard scientific computing libraries (e.g., NumPy, SciPy) for minimization and linear algebra. Install any necessary Python packages via pip before running the computation.

## Workflow steps

### Step 1: CVM Phase Diagram Computation
- Role: scored (load-bearing)
- Action: Implement the cluster-variation method (CVM) in the pair approximation for the (GaAs)₁₋ₓGe₂ₓ alloy system using the provided energy parameters δ=0.162 eV, J(q=0)=0.162 eV, J(q=1/4)=0.109 eV, K^(1)=0.035 eV, K^(2)=0.020 eV, K^(3)=0.017 eV. Apply constraints: fixed Ge composition x, no Ge sublattice ordering, no Ga–Ga or As–As bonds. Express the free energy in terms of nearest-neighbor pair probabilities and use the superposition approximation for inter-bond Madelung interactions beyond nearest neighbor. Minimize the free energy numerically over a dense grid of temperatures T and compositions x to locate the order-disorder ZB↔D transition line. Extract the percolation limit (critical composition at infinite T) and the tricritical points (x_tc, T_tc) for both the uncompensated (q=0) and compensated (q=1/4) cases. Write the results to cvm_phase_diagram_results.json.
- Output file: `/app/outputs/cvm_phase_diagram_results.json`
- Format: json
- Contract: {"percolation_limit": float, "tricritical_q0": {"x": float, "T_K": float}, "tricritical_q025": {"x": float, "T_K": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cvm_phase_diagram_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cvm_phase_diagram_results.json
- path: `/app/outputs/cvm_phase_diagram_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed percolation limit and tricritical points for the (GaAs)1-xGe2x alloy in both uncompensated and compensated cases.
- schema:
  - `type`: object
  - `required`:
    - `percolation_limit`: number
    - `tricritical_q0`:
      - `x`: number
      - `T_K`: number
    - `tricritical_q025`:
      - `x`: number
      - `T_K`: number

Notes: Energy parameters and interaction terms are provided as known constants in the instruction; the agent must reimplement the CVM pair approximation and free-energy minimization from scratch. Tolerance ranges and gold values are only used in the hidden checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cvm_phase_diagram_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "percolation_limit": "number",
          "tricritical_q0": {
            "x": "number",
            "T_K": "number"
          },
          "tricritical_q025": {
            "x": "number",
            "T_K": "number"
          }
        }
      },
      "description": "Computed percolation limit and tricritical points for the (GaAs)1-xGe2x alloy in both uncompensated and compensated cases."
    }
  ],
  "notes": "Energy parameters and interaction terms are provided as known constants in the instruction; the agent must reimplement the CVM pair approximation and free-energy minimization from scratch. Tolerance ranges and gold values are only used in the hidden checker."
}
```

## How you are scored
A hidden verifier will read your cvm_phase_diagram_results.json and compare each reported value (percolation_limit, tricritical_q0.x, tricritical_q0.T_K, tricritical_q025.x, tricritical_q025.T_K) against the correct values derived from the paper’s results. The comparison uses appropriate tolerances that account for legitimate differences in numerical implementation and minimization details. Partial credit is awarded for each correct quantity; the final reward is a weighted combination. The verifier does not execute your code—it simply checks the output file. Therefore, the numbers you produce must genuinely come from implementing the CVM model described in the Approach and Workflow steps.
