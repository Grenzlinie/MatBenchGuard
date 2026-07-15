# Classical Nucleation Theory Critical Size Calculation

## Problem background
Understanding ice nucleation in the atmosphere depends on knowing the critical size of water clusters that form on nucleating substrates. This task investigates the critical cluster size for a water monolayer developing on a model silver iodide (AgI) basal surface—a system used to study the early stages of heterogeneous ice formation. The central challenge is to compute the Helmholtz free energy differences of adsorbed water clusters of various sizes, which govern the steady‑state nucleation rate. The goal is to determine, for a fixed temperature and saturation condition, at what cluster size the monolayer becomes stable and begins to grow rapidly. The calculation requires a statistical‑mechanical treatment of the adsorbed clusters, coupled with accurate interatomic potentials, and ultimately provides the critical nucleus size and the corresponding nucleation rate.

## Approach
The method combines a Monte Carlo free energy technique with a statistical mechanical formalism for non‑interacting ideal cluster gases on a rigid substrate.

The core computational step is a Metropolis Monte Carlo thermodynamic integration using the Squire‑Hoover method. For each cluster size n (n=1,2,3,4,6,24 water molecules), simulations are run with a scaled interaction potential whose scaling parameter λ is varied gradually. Integrating the ensemble‑averaged energy difference ⟨ΔU⟩ as a function of λ yields the configurational integral difference, expressed as C(n) = –Δw⁽s⁾(n)/(kT), where Δw⁽s⁾(n) is the Helmholtz free energy difference for adding one molecule to a cluster of size n‑1 on the substrate. The water molecules are treated as rigid; water‑water interactions follow the Stillinger‑Rahman central force potential, and water‑substrate interactions follow the Hale‑Kiefer H₂O–AgI potential.

With the C(n) values, the statistical mechanical framework relates the areal concentrations of adsorbed clusters to the monomer concentration in the vapor. The critical cluster size n* is defined as the size where the free energy profile satisfies Δw⁽s⁾(n*) ≈ ln(S) (with S=1 at saturation). The steady‑state nucleation rate J is then obtained from a sum over cluster concentrations and a kinetic prefactor that depends on the monomer surface diffusion rate. The task focuses on producing the C(n) values; the downstream derivation of n* and J from those C(n) is checked by the hidden verifier.

## Reproduction target
Compute the six configurational integral differences C(n) for water monolayer clusters of sizes n = 1, 2, 3, 4, 6, and 24 on a rigid model AgI basal substrate at 265 K and water saturation (S=1). Write the results as a JSON object in `/app/outputs/results.json` with the key `"C_values"` mapping each cluster size (as a string key) to its floating‑point C(n). The verifier will use these values to derive the critical cluster size and nucleation rate and assess whether they are physically correct.

## Assets

- Stillinger-Rahman central force potential for water: 10.1063/1.435946
- H2O-AgI interaction potential: 10.1063/1.439380
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Monte Carlo Free Energy Calculation
- Role: process
- Action: Run Metropolis Monte Carlo simulations using the Squire-Hoover thermodynamic integration technique to compute configurational integral differences C(n) = -\Delta w^s(n)/(kT) for water monolayer clusters of sizes n=1,2,3,4,6,24 adsorbed on a rigid AgI basal substrate at 265 K. Use the Stillinger-Rahman central force potential for water-water interactions and the Hale-Kiefer H₂O–AgI interaction potential. The computational technique should follow the thermodynamic integration method described by Squire and Hoover (J. Chem. Phys. 50, 701, 1969), where the potential is scaled by a parameter \lambda and the free energy difference is obtained by integrating <\Delta U> as a function of \lambda.
- Evidence: `/app/outputs/mc_simulation.log`

### Step 2: Output C values
- Role: scored (load-bearing)
- Action: Compute the C(n) values for n=1,2,3,4,6,24 from the Monte Carlo thermodynamic integration results. Write a JSON object containing a key "C_values" with sub-keys "1", "2", "3", "4", "6", "24" mapping to the corresponding C(n) floats.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"C_values": {"1": float, "2": float, "3": float, "4": float, "6": float, "24": float}}
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
- target_policy: metric_recompute
- description: Helmholtz free energy difference parameters C(n) = -Δw^s(n)/(kT) for adsorbed water clusters of size 1 through 24 on a model AgI basal substrate at 265 K. The checker will use these values to recompute the critical cluster size n* and steady-state nucleation rate J using hidden reference parameters, and verify that n* matches the expected integer and that J is within a factor-of-5 threshold.
- schema:
  - `type`: object
  - `required`: `C_values`
  - `properties`:
    - `C_values`:
      - `type`: object
      - `required`: `1`, `2`, `3`, `4`, `6`, `24`
      - `properties`:
        - `1`:
          - `type`: number
        - `2`:
          - `type`: number
        - `3`:
          - `type`: number
        - `4`:
          - `type`: number
        - `6`:
          - `type`: number
        - `24`:
          - `type`: number

Notes: Only the C(n) values are scored; the checker recomputes n* and J from them. The agent must run the Monte Carlo simulation to obtain accurate C(n) values; providing exact paper-reported values without genuine computation will fail the checker's recomputation of n* and J because the derived critical size and nucleation rate are sensitive to the precise free energy differences.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "C_values"
        ],
        "properties": {
          "C_values": {
            "type": "object",
            "required": [
              "1",
              "2",
              "3",
              "4",
              "6",
              "24"
            ],
            "properties": {
              "1": {
                "type": "number"
              },
              "2": {
                "type": "number"
              },
              "3": {
                "type": "number"
              },
              "4": {
                "type": "number"
              },
              "6": {
                "type": "number"
              },
              "24": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Helmholtz free energy difference parameters C(n) = -Δw^s(n)/(kT) for adsorbed water clusters of size 1 through 24 on a model AgI basal substrate at 265 K. The checker will use these values to recompute the critical cluster size n* and steady-state nucleation rate J using hidden reference parameters, and verify that n* matches the expected integer and that J is within a factor-of-5 threshold."
    }
  ],
  "notes": "Only the C(n) values are scored; the checker recomputes n* and J from them. The agent must run the Monte Carlo simulation to obtain accurate C(n) values; providing exact paper-reported values without genuine computation will fail the checker's recomputation of n* and J because the derived critical size and nucleation rate are sensitive to the precise free energy differences."
}
```

## How you are scored
A hidden verifier evaluates the submitted `results.json` by reading the C(n) values. It recomputes the critical cluster size n* and the steady‑state nucleation rate J from those C(n), employing a set of hidden reference physical constants (vapor monomer concentration, constraining geometry factors, diffusion parameters, etc.) that you are not given. The verifier compares the derived n* and J to the paper’s target answers. A correct result is one whose C(n) values, when plugged into the statistical mechanical formalism with the hidden constants, reproduce n* and J within the verifier’s allowed tolerances. Simply reporting a memorized number is not sufficient; you must have genuinely run the Monte Carlo thermodynamic integration to obtain C(n) values that are consistent with the correct physics. The individual check on the derived quantities is combined into a single reward in the [0,1] range.
