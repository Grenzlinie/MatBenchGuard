# Skyrmion Nucleation and Thermal Stability in h-BN(AC)/Co(3 ML) Nanodisks

## Problem background
This task concerns micromagnetic simulations of a magnetic nanodisk formed at the interface between hexagonal boron nitride (h‑BN) and cobalt. Specifically, an h‑BN(AC)/Co(3 ML) stack is patterned into a 100 nm diameter disk. Using material parameters derived from first‑principles calculations (exchange stiffness, Dzyaloshinskii–Moriya interaction, perpendicular magnetic anisotropy, saturation magnetization, and damping), the equilibrium magnetic textures are investigated as a function of external magnetic field and temperature. The central question is how the system’s topological charge (skyrmion number) and the number of skyrmions change under these conditions.

## Approach
The equilibrium magnetization is obtained by solving the Landau–Lifshitz–Gilbert equation using the open‑source micromagnetic solver OOMMF. The disk is initialized in a uniform out‑of‑plane ferromagnetic state and then relaxed to its ground state for each of the six conditions listed in the workflow step. From the final magnetization distribution the skyrmion number (topological charge) is computed, and isolated skyrmions are identified and counted. The setup includes the demagnetization field, a uniform out‑of‑plane external field where specified, and thermal fluctuations modeled via a stochastic thermal field for the finite‑temperature runs.

## Reproduction target
Your goal is to produce a single JSON file, `step_01_skyrmion_metrics.json`, that contains an array of condition entries. Each entry must report the label of the simulation condition, the computed `skyrmion_number` (float), and the integer `skyrmion_count`. The six required conditions are listed in the workflow step. The file will be evaluated solely on the accuracy of the numeric values it contains.

## Assets

- OOMMF (Object Oriented MicroMagnetic Framework): https://math.nist.gov/oommf/

## Workflow steps

### Step 1: Micromagnetic simulation and skyrmion metric extraction
- Role: scored (load-bearing)
- Action: Using OOMMF, perform micromagnetic simulations of a 100 nm diameter nanodisk for the h-BN(AC)/Co(3 ML) system. Set the material parameters to A=5 pJ/m, D=2.24 mJ/m², K=8.63×10⁵ J/m³, M_s=1.37×10⁶ A/m, α=0.3. Start from a uniform out-of-plane ferromagnetic state and relax the magnetization to equilibrium for each of the six required conditions: (1) zero external field, 0 K; (2) external field 200 mT, 0 K; (3) external field 250 mT, 0 K; (4) field 200 mT, temperature 100 K; (5) field 200 mT, temperature 150 K; (6) field 200 mT, 0 K, with exchange stiffness A increased to 15 pJ/m. For each condition, compute the skyrmion number (topological charge) and the number of skyrmions present in the relaxed state, and collect the results into a single JSON file.
- Output file: `/app/outputs/step_01_skyrmion_metrics.json`
- Format: json
- Contract: JSON object with a key 'conditions' containing an array of condition entries. Each entry has: 'label' (string), 'skyrmion_number' (float), 'skyrmion_count' (integer). Conditions correspond to the six listed scenarios.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_skyrmion_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_skyrmion_metrics.json
- path: `/app/outputs/step_01_skyrmion_metrics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Skyrmion metrics for each simulation condition. The checker compares skyrmion_number (within ±0.5) and skyrmion_count (exact match) against hidden expected values.
- schema:
  - `type`: object
  - `required`:
    - `conditions`: array of condition objects
  - `items`:
    - `label`: string
    - `skyrmion_number`: float
    - `skyrmion_count`: integer

Notes: The agent must produce the skyrmion number (topological charge) and skyrmion count for all six conditions. The hidden checker uses a tolerance of 0.5 for skyrmion_number and exact match for skyrmion_count.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_skyrmion_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "conditions": "array of condition objects"
        },
        "items": {
          "label": "string",
          "skyrmion_number": "float",
          "skyrmion_count": "integer"
        }
      },
      "description": "Skyrmion metrics for each simulation condition. The checker compares skyrmion_number (within ±0.5) and skyrmion_count (exact match) against hidden expected values."
    }
  ],
  "notes": "The agent must produce the skyrmion number (topological charge) and skyrmion count for all six conditions. The hidden checker uses a tolerance of 0.5 for skyrmion_number and exact match for skyrmion_count."
}
```

## How you are scored
A hidden verifier reads your `step_01_skyrmion_metrics.json` and compares the reported `skyrmion_number` and `skyrmion_count` for each condition against expected values. The comparison uses a tolerance for the skyrmion number and an exact match for the count. The result is a weighted score between 0 and 1, with full credit obtained only when the metrics correctly reflect the true underlying magnetic states. Reporting numbers without performing the actual simulations will not produce a valid result.
