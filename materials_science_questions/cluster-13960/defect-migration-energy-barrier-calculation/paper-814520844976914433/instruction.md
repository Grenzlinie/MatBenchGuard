# Mg migration barrier in cubic Ti2S4 spinel

## Problem background
The sluggish mobility of divalent Mg²⁺ ions in solid hosts has been a major bottleneck in the development of rechargeable Mg batteries. Soft anion lattices, such as sulfides, are thought to mitigate this issue by weakening the electrostatic interaction between the mobile cation and the framework. The cubic thiospinel Ti₂S₄ is one such candidate. Its structural simplicity and theoretical studies have highlighted the role of Mg diffusion kinetics in determining cathode performance. A key quantity that governs the Mg diffusion rate is the migration energy barrier for a single Mg²⁺ ion hopping between adjacent sites. First-principles nudged elastic band (NEB) calculations provide a reliable route to compute this barrier, allowing direct comparison with experimental activation energies extracted from electrochemical measurements. This task focuses on computing the Mg migration barrier in cubic Ti₂S₄ for two limiting Mg concentrations — the dilute limit and the concentrated limit — via standard DFT‑NEB methods.

## Approach
The computational approach relies on density functional theory (DFT) within the PBE generalized gradient approximation, coupled with the climbing-image nudged elastic band (CI‑NEB) method to locate the minimum-energy path for Mg diffusion. The crystal structure of cubic Ti₂S₄ adopts the spinel structure (space group Fd‑3m), with known lattice parameters for the two different Mg loadings. For the dilute limit, one Mg atom is placed in an octahedral site of an 8‑formula‑unit supercell; for the concentrated limit, the supercell is filled with Mg atoms (e.g., 7 per supercell) to approach full occupancy. The diffusion mechanism considered is the tri‑vacancy pathway, where a Mg ion hops from an octahedral site through a face-sharing tetrahedral intermediate to a neighboring vacant octahedral site. The agent must first construct the supercells, relax the endpoint configurations, interpolate a chain of intermediate images, and then perform CI‑NEB to converge the saddle point. The migration barrier is the energy difference between the saddle point and the initial minimum, expressed in meV. Any standard open‑source DFT package that supports the PBE functional and NEB (Quantum ESPRESSO, GPAW, etc.) may be used; the computed barriers for the two concentration limits constitute the primary output.

## Reproduction target
The task objective is to produce a JSON file, step_01_barrier.json, containing two fields: "dilute_barrier_meV" and "concentrated_barrier_meV". Each is a floating-point number giving the computed Mg migration barrier in meV for the corresponding Mg concentration limit. The barriers must be obtained from proper CI‑NEB calculations on the specified supercells, and the reported values must reflect the energy at the saddle point relative to the initial energy minimum. No additional statistical analysis or comparison with experimental data is required; the two barrier numbers are the sole scored outputs.

## Assets

- Cubic Ti2S4 crystal structure
- Open-source DFT package with NEB support

## Workflow steps

### Step 1: Compute Mg migration barrier
- Role: scored (load-bearing)
- Action: Perform first-principles NEB calculations to obtain the minimum-energy migration barrier for Mg²⁺ diffusion in cubic Ti₂S₄ via the tri-vacancy mechanism. Build an 8-formula-unit supercell with one Mg atom for the dilute limit, and with 7 Mg atoms for the concentrated limit. Relax the end-point images (octahedral site occupancy for the Mg ion), set up a diffusion path through the face-sharing octahedral–tetrahedral–octahedral pathway, and run climbing-image NEB. Extract the energy difference between the saddle point and the minimum in meV.
- Output file: `/app/outputs/step_01_barrier.json`
- Format: json
- Contract: {"dilute_barrier_meV": <float>, "concentrated_barrier_meV": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_barrier.json
- path: `/app/outputs/step_01_barrier.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Migration energy barriers for Mg diffusion in cubic Ti2S4, computed for the dilute (1 Mg per 8-formula-unit supercell) and concentrated (7 Mg per supercell) limits.
- schema:
  - `type`: object
  - `required`: `dilute_barrier_meV`, `concentrated_barrier_meV`
  - `properties`:
    - `dilute_barrier_meV`:
      - `type`: number
      - `unit`: meV
    - `concentrated_barrier_meV`:
      - `type`: number
      - `unit`: meV

Notes: The checker compares the agent's reported barriers to a hidden reference derived from the paper's first-principles NEB results with a tolerance that accounts for code-to-code variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "dilute_barrier_meV",
          "concentrated_barrier_meV"
        ],
        "properties": {
          "dilute_barrier_meV": {
            "type": "number",
            "unit": "meV"
          },
          "concentrated_barrier_meV": {
            "type": "number",
            "unit": "meV"
          }
        }
      },
      "description": "Migration energy barriers for Mg diffusion in cubic Ti2S4, computed for the dilute (1 Mg per 8-formula-unit supercell) and concentrated (7 Mg per supercell) limits."
    }
  ],
  "notes": "The checker compares the agent's reported barriers to a hidden reference derived from the paper's first-principles NEB results with a tolerance that accounts for code-to-code variation."
}
```

## How you are scored
Your submission will be checked by a hidden verifier that reads the file step_01_barrier.json and compares your reported barriers to the expected values from a trusted reference computation. The verifier applies a predefined tolerance that accounts for the typical spread introduced by using different DFT codes, pseudopotentials, and numerical settings, while still requiring physically meaningful agreement. Both the dilute and concentrated barriers must fall within tolerance to receive full credit. The final reward is a single number between 0 and 1, reflecting how accurately you reproduced the migration barriers. No further instructions will be given regarding the reference values or the tolerance; simply performing the NEB calculations with standard care should yield a result that passes the check.
