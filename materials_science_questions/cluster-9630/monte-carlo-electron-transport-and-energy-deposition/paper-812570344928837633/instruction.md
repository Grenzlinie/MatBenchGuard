# Electron Swarm Monte Carlo Simulation for Reid Model Validation

## Problem background
The electron transport properties of a gas under an electric field can be studied theoretically using simplified model cross-sections. The Reid gas model is a widely used benchmark for electron swarm simulation codes. It defines a constant elastic cross-section and a linear excitation cross-section that activates above a threshold. By simulating a large ensemble of electrons (a swarm) moving through this model gas under a constant electric field, one obtains swarm parameters such as the mean electron energy, the bulk drift velocity, and the transverse diffusion coefficient. These quantities characterise how the electron distribution evolves and drifts in the field, and they serve as a validation target for Monte Carlo electron transport algorithms.

## Approach
You will implement a null-collision Monte Carlo simulation for the Reid gas model. The elastic cross-section is a constant \(\sigma_{\text{el}} = 1.0\times10^{-20}\,\text{m}^2\). The excitation cross-section is \(\sigma_{\text{exc}} = 1.0\times10^{-20}\times(\varepsilon - 0.2)\,\text{m}^2\) for electron energies \(\varepsilon \ge 0.2\) eV, and zero otherwise. The simulation follows many electrons moving under a constant electric field in the z-direction. The null-collision technique uses a maximum collision frequency to sample the free-flight time, and at each collision a real process (elastic, excitation) or a null event is selected. The electron positions and velocities are updated accordingly. For each of three reduced electric field values (\(E/N = 1, 10, 20\) Td), you run the simulation until a steady state is reached (the median energy fluctuates by less than about 10% over several time windows). From the steady-state swarm statistics you compute the mean electron energy, the bulk drift velocity (from the centre-of-mass displacement over time), and the transverse diffusion coefficient (from the variance of the transverse positions).

## Reproduction target
Produce the electron swarm parameters (mean energy, bulk drift velocity, and transverse diffusion coefficient) for the Reid gas model at the three reduced electric fields \(E/N = 1, 10, 20\) Td. Report the results in a JSON file conforming to the output contract. The values you obtain will be automatically compared against a hidden reference to judge the correctness of your Monte Carlo implementation. The task is to produce physically accurate numbers, not merely to output a correctly formatted file.

## Assets
No external datasets, pre-trained models, or proprietary tools are required. The cross-sections and problem setup are fully specified in the instructions above. You will only need standard numerical and scientific Python libraries (e.g., numpy, scipy); you may install any needed packages yourself. There is no external data file to download.

## Workflow steps

### Step 1: Monte Carlo swarm simulation for Reid model
- Role: scored (load-bearing)
- Action: Implement an electron null-collision Monte Carlo simulation for the Reid gas model (constant elastic cross-section σ_el = 1.0×10⁻²⁰ m², linear excitation cross-section σ_exc = 1.0×10⁻²⁰×(ε−0.2) m² for ε ≥ 0.2 eV, zero otherwise). Simulate an electron swarm at rest under a constant electric field along z for reduced electric fields E/N = 1, 10, and 20 Td. Run each simulation until steady state (median energy fluctuation <10% over several cycles). Compute the mean electron energy (eV), bulk drift velocity (1e6 cm/s) using center-of-mass displacement, and transverse diffusion coefficient (1e5 cm²/s) from the swarm statistics. Output these three parameters for each field to step_01_swarm_results.json as a JSON array of three objects.
- Output file: `/app/outputs/step_01_swarm_results.json`
- Format: json
- Contract: A JSON array of exactly 3 objects, each with keys: reduced_field (number, Td), mean_energy (number, eV), drift_velocity (number, 1e6 cm/s), diffusion_coefficient (number, 1e5 cm²/s). Example structure: [{"reduced_field": 1, "mean_energy": 0.101, "drift_velocity": 1.28, "diffusion_coefficient": 0.978}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_swarm_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_swarm_results.json
- path: `/app/outputs/step_01_swarm_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electron swarm parameters for the Reid model at E/N = 1, 10, 20 Td. The array must contain exactly three objects, one per reduced field. Checker compares each numeric value to the hidden gold from SCENA Table 1 within hidden absolute tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `reduced_field`, `mean_energy`, `drift_velocity`, `diffusion_coefficient`
    - `properties`:
      - `reduced_field`:
        - `type`: number
        - `units`: Td
      - `mean_energy`:
        - `type`: number
        - `units`: eV
      - `drift_velocity`:
        - `type`: number
        - `units`: 1e6 cm/s
      - `diffusion_coefficient`:
        - `type`: number
        - `units`: 1e5 cm2/s
  - `minItems`: 3
  - `maxItems`: 3

Notes: Only the three specified reduced electric fields (1, 10, 20 Td) are required. The agent must use the exact units stated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_swarm_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "reduced_field",
            "mean_energy",
            "drift_velocity",
            "diffusion_coefficient"
          ],
          "properties": {
            "reduced_field": {
              "type": "number",
              "units": "Td"
            },
            "mean_energy": {
              "type": "number",
              "units": "eV"
            },
            "drift_velocity": {
              "type": "number",
              "units": "1e6 cm/s"
            },
            "diffusion_coefficient": {
              "type": "number",
              "units": "1e5 cm2/s"
            }
          }
        },
        "minItems": 3,
        "maxItems": 3
      },
      "description": "Electron swarm parameters for the Reid model at E/N = 1, 10, 20 Td. The array must contain exactly three objects, one per reduced field. Checker compares each numeric value to the hidden gold from SCENA Table 1 within hidden absolute tolerances."
    }
  ],
  "notes": "Only the three specified reduced electric fields (1, 10, 20 Td) are required. The agent must use the exact units stated."
}
```

## How you are scored
A hidden automated verifier will read your output file and compare each reported swarm parameter to a reference value. Your score is based on how closely your simulation results match the expected physical values. Simply producing a syntactically correct JSON file is not sufficient; the computed numbers must be accurate. The verifier combines the individual comparisons into a single reward between 0 and 1.

Important: the reference values are secret and you must not attempt to retrieve them from any source other than your own simulation. The problem is designed so that an honest, correctly implemented Monte Carlo procedure will yield results that pass the verification.
