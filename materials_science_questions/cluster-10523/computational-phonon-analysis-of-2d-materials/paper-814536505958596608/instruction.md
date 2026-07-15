# Linear chain model of interlayer vibrations in few-layer MoTe₂

## Problem background
Few-layer transition metal dichalcogenides (TMDs) such as MoTe₂ exhibit low-energy interlayer vibrational modes—shear (in-plane rigid layer displacements) and breathing (out-of-plane rigid layer displacements)—whose frequencies evolve with the number of layers. This thickness dependence arises from the interlayer force constants and can be described by a linear chain model in which each layer is treated as a rigid unit interacting with its nearest neighbours. The experimental frequencies of these modes in bilayer crystals directly determine the in-plane shear force constant K_x and the out-of-plane compression force constant K_z, which then predict the mode energies for any layer count. This task reproduces that analysis: from the measured bilayer shear (19.2 cm⁻¹) and breathing (27.8 cm⁻¹) frequencies and the known atomic masses per unit area, compute the interlayer force constants and the complete set of Raman-active shear and breathing mode frequencies for layer counts N = 2 through 7 and the bulk limit.

## Approach
The computation employs the linear chain model with nearest-neighbour interactions. Each MoTe₂ triple layer (Te–Mo–Te) is modelled as a single effective mass point with a reduced mass per unit area μ, obtained from the published atomic masses per area (m_Te = 2×10⁶ kg/m², m_Mo = 1.5×10⁶ kg/m²). The interlayer restoring forces are parametrised by a shear force constant K_x and a breathing force constant K_z (both in N/m³). For N layers, the allowed phonon branches are indexed by α = 2,3,…,N, and the frequency of branch α is given by

ω_{i,α} = √[ (K_i / (2 μ π² c²)) (1 – cos((α−1)π/N)) ]

where i = x (shear) or z (breathing). The bilayer (N=2) frequencies directly fix K_x and K_z, since the Raman-active branches are α=2 for both modes. Once K_x and K_z are known, the same formula yields the frequencies for any N. The Raman-active shear branches are the highest-energy branch α=N and, for N ≥ 4, the next branch α=N−2. The Raman-active breathing branches are the even-α branches (α = 2,4,6,…) up to N. The bulk limit is approximated by N=100.

## Reproduction target
Use the provided bilayer experimental frequencies (shear 19.2 cm⁻¹, breathing 27.8 cm⁻¹) and the given mass per area values to compute:
1. The interlayer force constants K_x (shear) and K_z (breathing) in N/m³.
2. For each layer count N in {2, 3, 4, 5, 6, 7, 100}:
   – the Raman-active shear mode frequencies (branches α=N and, when N≥4, α=N−2), and
   – the Raman-active breathing mode frequencies (branches α=2,4,6,… up to N).

Output all results in a single JSON file, model_results.json, following the schema described below. The computation must be carried out programmatically; the agent is free to choose the implementation language and libraries.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Linear chain model calculation of interlayer force constants and thickness-dependent mode frequencies
- Role: scored (load-bearing)
- Action: Implement the linear chain model for rigid interlayer shear and breathing modes. Using the reported bilayer shear (19.2 cm⁻¹) and breathing (27.8 cm⁻¹) frequencies, and the published mass per unit area for Te (2×10⁶ kg/m²) and Mo (1.5×10⁶ kg/m²), compute the interlayer force constants K_x and K_z. Then for layer counts N from 2 to 7, and for the bulk limit N=100, compute the Raman-active shear mode frequencies (highest branch α=N and next branch α=N-2 for N≥4) and breathing mode frequencies (even branches α=2,4,6,… for α≤N). Output the force constants and all mode frequencies.
- Output file: `/app/outputs/model_results.json`
- Format: json
- Contract: {"K_x": number, "K_z": number, "modes": [{"N": integer, "mode_type": "shear"|"breathing", "branch": string, "frequency_cm-1": number}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_results.json
- path: `/app/outputs/model_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON file containing the computed interlayer force constants (K_x, K_z) and a list of all calculated Raman-active shear and breathing mode frequencies for layer counts 2 through 7 and bulk (N=100). The verifier will recompute K_x and K_z from the bilayer input constants, recompute the frequency table from the agent's K_x/K_z, and compare the frequencies against the paper's experimentally measured frequencies.
- schema:
  - `type`: object
  - `required`:
    - `K_x`: number (N/m³)
    - `K_z`: number (N/m³)
    - `modes`: array
  - `items`:
    - `modes`:
      - `type`: object
      - `required`:
        - `N`: integer
        - `mode_type`: string (shear or breathing)
        - `branch`: string (e.g. "α=N", "α=N-2", "α=2", ...)
        - `frequency_cm-1`: number

Notes: The task uses a pure analytical model; no external datasets are required. The solving agent must implement the model and produce the structured artifact. All input constants are provided in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "K_x": "number (N/m³)",
          "K_z": "number (N/m³)",
          "modes": "array"
        },
        "items": {
          "modes": {
            "type": "object",
            "required": {
              "N": "integer",
              "mode_type": "string (shear or breathing)",
              "branch": "string (e.g. \"α=N\", \"α=N-2\", \"α=2\", ...)",
              "frequency_cm-1": "number"
            }
          }
        }
      },
      "description": "JSON file containing the computed interlayer force constants (K_x, K_z) and a list of all calculated Raman-active shear and breathing mode frequencies for layer counts 2 through 7 and bulk (N=100). The verifier will recompute K_x and K_z from the bilayer input constants, recompute the frequency table from the agent's K_x/K_z, and compare the frequencies against the paper's experimentally measured frequencies."
    }
  ],
  "notes": "The task uses a pure analytical model; no external datasets are required. The solving agent must implement the model and produce the structured artifact. All input constants are provided in the instruction."
}
```

## How you are scored
A hidden verifier independently checks your submission. It recomputes K_x and K_z from the input bilayer frequencies using the same analytical formula, and compares them to your reported values with a strict relative tolerance. It then recomputes, from your K_x and K_z, the full set of mode frequencies and compares them to your reported frequencies. Finally, your computed frequencies are compared against experimentally measured frequencies available to the verifier. The reward is a weighted combination of these comparisons; reporting correct values without performing the computation will not give full credit, because the verifier tests consistency across the force constants and the entire frequency table. The exact tolerances and weights are hidden.
