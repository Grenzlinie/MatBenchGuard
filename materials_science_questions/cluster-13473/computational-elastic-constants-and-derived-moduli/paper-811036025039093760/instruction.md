# Si(111) Step Stiffness from MD Capillary Fluctuations in Al-Si Alloys

## Problem background
In the solidification of binary alloys, faceted solid-liquid interfaces play a critical role in dendritic growth and microstructural evolution. The step stiffness (γ+γ″), which quantifies the free energy cost of a step on a faceted interface, determines step fluctuations and influences growth kinetics. Understanding how step stiffness depends on liquid composition, temperature, and step orientation is essential for predicting solidification morphology. Molecular dynamics simulations combined with capillary fluctuation analysis provide a direct computational route to measure step stiffness for model alloy systems. This task reproduces the computation of step stiffness for Si(111) steps in contact with Al-Si liquids of two different compositions using an angular embedded atom method (AEAM) interatomic potential.

## Approach
The reproduction workflow is a two-stage process: first, equilibrium molecular dynamics (MD) simulations are performed to generate solid-liquid interface configurations containing a pair of active steps; second, capillary fluctuation analysis is applied to the MD trajectories to extract step stiffness values.

MD simulations are set up with a non-orthogonal periodic cell containing a pure Si solid in contact with an Al-Si liquid of the target composition, oriented to expose (111) interfaces with steps along the desired direction. The simulation uses the AEAM potential for Al-Si and is run in the NPxzAT ensemble to maintain zero stress in the step plane while allowing the box dimension normal to the interface to adjust. Production runs collect snapshots of atom positions at regular intervals.

From the snapshots, atoms are classified as solid-like or liquid-like using a local order parameter based on the symmetry of second-nearest neighbors characteristic of the diamond cubic structure. The step height profile on each interface is extracted through a multi-step post-processing routine: the simulation domain is discretized into small domains, each domain is assigned a solid/liquid label based on the average order parameter of its atoms, and defects (liquid puddles in the solid and solid islands in the liquid) are removed by relabeling algorithms that enforce continuity of the solid and liquid phases. A column-wise interface detection then yields single-valued step height profiles.

For each snapshot, the step profile is Fourier transformed, and the time-averaged squared amplitude ⟨|A(k_n)|²⟩ is computed as a function of wave number k_n. According to the capillary-fluctuation relation for a rough step, ⟨|A(k_n)|²⟩ should scale as 1/k_n² with a prefactor involving the step length, temperature, and step stiffness. A linear fit to ⟨|A(k_n)|²⟩ versus 1/k_n² yields the step stiffness (γ+γ″) and its 95% confidence interval for each simulated condition.

## Reproduction target
Compute step stiffness (γ+γ″) and its 95% confidence interval for four distinct conditions:
- Liquid composition Al–87.4 at.% Si at 1570 K, step orientation [1̅10]
- Liquid composition Al–87.4 at.% Si at 1570 K, step orientation [11̅2]
- Liquid composition Al–59.4 at.% Si at 1230 K, step orientation [1̅10]
- Liquid composition Al–59.4 at.% Si at 1230 K, step orientation [11̅2]
Each condition must be simulated independently using MD with the AEAM potential, and the step stiffness must be extracted entirely from the generated trajectories via capillary fluctuation analysis. Report the four stiffness values with their uncertainties in the output file `step_stiffness_results.json`.

## Assets

- AEAM Al-Si interatomic potential (Saidi et al. 2014): 10.1088/0965-0393/22/5/055010
- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://www.lammps.org

## Workflow steps

### Step 1: Prepare systems and run equilibrium MD simulations
- Role: process
- Action: For the four conditions (two liquid compositions: Al-87.4at.%Si at 1570 K and Al-59.4at.%Si at 1230 K; two step orientations: [1̅10] and [11̅2]), construct initial configurations of a Si(111) solid in contact with Al-Si liquid including two steps, using a non‑orthogonal periodic cell. Equilibrate and run production MD in the NPxzAT ensemble with the AEAM potential, collecting 200 snapshots every 50 ps. Produce trajectory files for all systems.
- Evidence: `/app/outputs/trajectory_files`

### Step 2: Capillary fluctuation analysis and stiffness fitting
- Role: scored (load-bearing)
- Action: From the MD trajectories, classify atoms as solid‑like or liquid‑like using the Buta order parameter ψ(i). Apply grid‑based defect removal (discretization into domains of size 0.8a along and 0.5a perpendicular to the step, relabeling to eliminate liquid puddles and solid islands, and column‑wise interface detection) to extract single‑valued step height profiles for each snapshot. Fourier transform each profile to obtain amplitudes A(k_n), compute time‑averaged squared amplitudes ⟨|A(k_n)|²⟩, and fit the capillary‑fluctuation relation ⟨|A(k_n)|²⟩ = k_B T / (l_step (γ+γ″) k_n²) to derive the step stiffness (γ+γ″) and its 95% confidence interval for each condition. Write the results to step_stiffness_results.json.
- Output file: `/app/outputs/step_stiffness_results.json`
- Format: json
- Contract: JSON array of objects, each with fields: composition (string), temperature_K (number), orientation (string), stiffness_J_per_m (number), stiffness_uncertainty_J_per_m (number)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_stiffness_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_stiffness_results.json
- path: `/app/outputs/step_stiffness_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed step stiffness values for the four conditions (two compositions × two orientations) with uncertainties.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `composition`, `temperature_K`, `orientation`, `stiffness_J_per_m`, `stiffness_uncertainty_J_per_m`
    - `properties`:
      - `composition`:
        - `type`: string
      - `temperature_K`:
        - `type`: number
      - `orientation`:
        - `type`: string
      - `stiffness_J_per_m`:
        - `type`: number
      - `stiffness_uncertainty_J_per_m`:
        - `type`: number

Notes: The agent must compute stiffness values from its own MD runs; no pre‑computed trajectory or stiffness is provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_stiffness_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "composition",
            "temperature_K",
            "orientation",
            "stiffness_J_per_m",
            "stiffness_uncertainty_J_per_m"
          ],
          "properties": {
            "composition": {
              "type": "string"
            },
            "temperature_K": {
              "type": "number"
            },
            "orientation": {
              "type": "string"
            },
            "stiffness_J_per_m": {
              "type": "number"
            },
            "stiffness_uncertainty_J_per_m": {
              "type": "number"
            }
          }
        }
      },
      "description": "Computed step stiffness values for the four conditions (two compositions × two orientations) with uncertainties."
    }
  ],
  "notes": "The agent must compute stiffness values from its own MD runs; no pre‑computed trajectory or stiffness is provided."
}
```

## How you are scored
A hidden verifier reads your `step_stiffness_results.json` and compares each of the four reported stiffness values to a hidden reference that corresponds to the correct result for the given potential and protocol. The total reward is the average of the per-condition scores (each condition carries equal weight). To earn full credit, a computed stiffness must be consistent with the hidden reference within an appropriate tolerance; the verifier may also verify that reasonable uncertainty estimates are provided. The verifier judges the numerical values produced by your workflow, not whether they match a particular published number. Simply copying numbers from external sources will not pass because the verifier expects values that could only come from running the MD simulations and the full capillary fluctuation analysis as described.
