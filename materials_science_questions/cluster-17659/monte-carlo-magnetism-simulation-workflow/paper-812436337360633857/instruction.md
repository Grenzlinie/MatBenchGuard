# Critical Inverse Temperatures of SU(N)/Z_N Gauge Theories via Monte Carlo Simulation

## Problem background
Lattice gauge theories provide a non-perturbative framework for studying the confinement mechanism in quantum chromodynamics and other gauge theories. Wilson's formulation expresses the partition function as an integral over link variables in the fundamental representation, with an action that depends on the trace of plaquette matrices. Removing the center of the gauge group by using the adjoint representation yields the SU(N)/Z_N models. While early expectations held that non-abelian gauge theories might not possess phase transitions separating high- and low-temperature regimes, later studies observed first-order transitions for certain groups. The nature of the transition in the adjoint SU(N) models for N=3 to 6 remains an open question. Determining whether a phase transition occurs for these groups—and, if it does, pinpointing the critical inverse temperature β_c where the ordered and disordered phases coexist—is essential for understanding the role of the group center in gauge theory dynamics.

## Approach
The core method is a Monte Carlo simulation of the lattice gauge theory in four Euclidean dimensions using the Metropolis algorithm. The system is defined on a hypercubical lattice of size 4^4 with periodic boundary conditions. Each link is an element of SU(N). The action is modified to use the adjoint representation: for each plaquette, the adjoint action is given by S_□ = 1 - (1/(N^2 - 1)) Tr_A U_□. The adjoint trace Tr_A U can be computed from the fundamental trace using the identity Tr_A U = |Tr_F U|^2 - 1, which holds for any SU(N) group. The simulation proceeds by proposing link updates and accepting or rejecting them according to the Metropolis criterion weighted by exp(-β ΔS).

The investigation proceeds in two stages. First, the hysteresis loop is mapped by performing simulations from completely ordered (all links = identity) and completely disordered (random SU(N) matrices) initial configurations over a range of inverse temperatures β. This yields an approximate location of the transition region. Second, mixed initial conditions are employed: half of the lattice links are randomized, while the other half (those with time coordinate less than half the lattice size) are frozen to the identity. This configuration provides a seed for both phases. Simulations at several β values near the suspected transition are run, and the evolution of the average plaquette action is monitored. At the critical temperature, the two phases coexist and the average action exhibits a meandering drift without settling into a unique value. The β_c is estimated as the value where this coexistence occurs, with uncertainty derived from the range of β over which coexistence is observed.

The entire implementation relies solely on standard numerical libraries (NumPy) and does not require any external data or pretrained models.

## Reproduction target
For each gauge group SU(N)/Z_N with N = 3, 4, 5, 6, implement the full Monte Carlo simulation as described. From the mixed-initial-condition runs, determine the critical inverse temperature β_c and an estimate of its uncertainty. The results must be recorded in the file critical_betas.json with exactly the keys "N3", "N4", "N5", "N6", each mapping to an object containing the numeric fields "beta_c" and "uncertainty". The goal is to produce β_c values that fall within the physically correct coexistence region as determined by the underlying theory and simulation methodology.

## Assets

- NumPy: https://pypi.org/project/numpy/

## Workflow steps

### Step 1: Ordered/Disordered Start Simulations
- Role: process
- Action: Implement a Monte Carlo simulation of SU(N)/Z_N gauge theory for N=3,4,5,6 on a 4^4 lattice using the Metropolis algorithm with the adjoint action (Tr_A U = |Tr_F U|^2 - 1). Run simulations from ordered and disordered initial configurations over a range of inverse temperatures β to identify the hysteresis region, producing evidence of the approximate transition location.
- Evidence: `/app/outputs/ordered_disordered_log.txt`

### Step 2: Extract Critical Inverse Temperatures from Mixed-Start Runs
- Role: scored (load-bearing)
- Action: For each N=3,4,5,6, using the hysteresis region identified in step 1, perform Monte Carlo simulations with mixed initial conditions (half-random, half-ordered) at several β values near the transition. Monitor the evolution of the average plaquette action. Determine β_c as the value where the two phases coexist, evidenced by a meandering drift without rapid relaxation to a unique value. Estimate the uncertainty from the range of β over which coexistence persists. Write the results to critical_betas.json.
- Output file: `/app/outputs/critical_betas.json`
- Format: json
- Contract: A JSON object with keys "N3", "N4", "N5", "N6". Each value is an object with numeric fields "beta_c" and "uncertainty".
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_betas.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_betas.json
- path: `/app/outputs/critical_betas.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical inverse temperature and uncertainty for each gauge group.
- schema:
  - `type`: object
  - `required`: `N3`, `N4`, `N5`, `N6`
  - `properties`:
    - `N3`:
      - `type`: object
      - `required`: `beta_c`, `uncertainty`
    - `N4`:
      - `type`: object
      - `required`: `beta_c`, `uncertainty`
    - `N5`:
      - `type`: object
      - `required`: `beta_c`, `uncertainty`
    - `N6`:
      - `type`: object
      - `required`: `beta_c`, `uncertainty`

Notes: The critical temperatures are extracted from the mixed-phase Monte Carlo simulations. The hidden checker will compare the reported values to the expected paper results using absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_betas.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "N3",
          "N4",
          "N5",
          "N6"
        ],
        "properties": {
          "N3": {
            "type": "object",
            "required": [
              "beta_c",
              "uncertainty"
            ]
          },
          "N4": {
            "type": "object",
            "required": [
              "beta_c",
              "uncertainty"
            ]
          },
          "N5": {
            "type": "object",
            "required": [
              "beta_c",
              "uncertainty"
            ]
          },
          "N6": {
            "type": "object",
            "required": [
              "beta_c",
              "uncertainty"
            ]
          }
        }
      },
      "description": "Critical inverse temperature and uncertainty for each gauge group."
    }
  ],
  "notes": "The critical temperatures are extracted from the mixed-phase Monte Carlo simulations. The hidden checker will compare the reported values to the expected paper results using absolute tolerances."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently inspects the output artifacts. The process-step logs are checked for existence, but only the scored artifact critical_betas.json contributes to the reward. The verifier reads the JSON file and compares each reported β_c and its uncertainty against hidden reference gold values (the correct critical temperatures for these models). The comparisons use absolute tolerances that account for inherent Monte Carlo run-to-run variation and implementation differences; the verifier also ensures that the reported uncertainties are non-zero and physically plausible. The final reward is a weighted combination of the per-group checks, with equal weight per group. You do not need to match any exact numbers stated in a paper—your task is to perform the simulation honestly and reproduce the physical transition temperatures to within the accepted uncertainty of the method.
