# Spin Wave Polarization Manipulation via Synthetic Antiferromagnet Sublayer Engineering

## Problem background
Spin waves are collective magnetic excitations that can propagate without Joule heating and carry information. In synthetic antiferromagnets (SyAFs) – bilayer structures with two antiferromagnetically coupled magnetic sublayers – the two sublayers are spatially separated. A key feature is that circular spin-wave polarization is partially locked to the sublayer: right-circular spin waves preferentially reside in the upper sublayer, left-circular in the lower sublayer. By engineering the sublayers, one can manipulate spin-wave polarization. Removing a sublayer creates a monolayer region that supports only one circular polarization – a circular polarizer. Capping with an additional layer creates a trilayer region that lifts the degeneracy between the two circular modes, acting as a circular retarder (wave-plate). This task explores these devices by computing their transmission and phase characteristics from first principles, without relying on the original paper's reported numbers.

## Approach
The magnetization dynamics in a synthetic antiferromagnet are described by two coupled Landau‑Lifshitz‑Gilbert (LLG) equations. Linearizing about the antiferromagnetic ground state yields a set of linear equations governing the right‑ and left‑circular components in each sublayer. The task implements a numerical solver for these linearized equations, employing the material parameters given in the literature: easy‑axis anisotropy K = 8.57 GHz, intra‑layer exchange A = 7.25 × 10⁻⁶ Hz·m², interlayer antiferromagnetic coupling J = 4.25 GHz, and gyromagnetic ratio γ = 2.21 × 10⁵ Hz/(A/m). The solver can be based on a Green function method, transfer matrices, or a finite‑difference approach; it must compute complex transmission amplitudes and phase shifts for spin waves propagating through layered SyAF structures. Two structures are studied: (1) a 2/1/2 polarizer – a bilayer SyAF with a 200 nm long central region where the upper sublayer is removed, leaving a monolayer with magnetization pointing upward (¬1 structure). The solver computes the transmission probabilities T_L and T_R for incident left‑ and right‑circular spin waves at frequency ω/(2π) = 6.5 GHz. (2) a 2/3/2 retarder – a bilayer SyAF with a 200 nm long central region where a third ferromagnetic layer is capped on top; its magnetization is pinned antiparallel to the upper sublayer (magnetization downward), producing an effective field γH₂ = +J on the upper sublayer. For an injected linearly polarized spin wave (equal left/right components) at 6.5 GHz, the solver extracts the accumulated relative phase delay δφ_LR between the left‑ and right‑circular components after the central region.

## Reproduction target
Compute the following quantities using your solver and write them to the specified output files:

- `polarizer_results.json`: transmission probabilities T_L and T_R for a 2/1/2 structure at 6.5 GHz.
- `retarder_results.json`: relative phase delay δφ_LR (in radians) through a 2/3/2 structure at 6.5 GHz with central length 200 nm.

The computed values should be physically consistent: a working polarizer strongly transmits one circular polarization and strongly blocks the other; a retarder introduces a non‑zero relative phase shift while transmitting both polarizations. The hidden verifier will compare your results against reference values derived from an independent implementation and the physics of the devices, using appropriate tolerances.

## Assets
This task uses no external datasets, pre‑trained models, or proprietary software. The required solver is implemented from scratch using only the material parameters and equations described above.

Recommended Python packages:
- `numpy` (for matrix operations)
- `scipy` (for linear algebra and numerical routines)

No specialized magnetic simulation software is needed.

## Workflow steps

### Step 1: Implement spin wave solver for synthetic antiferromagnet
- Role: process
- Action: Implement a numerical solver for spin waves in synthetic antiferromagnets, based on the linearized coupled equations of motion for the two sublayer transverse variables. The solver must compute transmission amplitudes and relative phase shifts for left- and right-circular spin waves propagating through layered structures, using the following material parameters: easy-axis anisotropy K = 8.57 GHz, intra-layer exchange A = 7.25e-6 Hz·m², interlayer antiferromagnetic coupling J = 4.25 GHz, gyromagnetic ratio γ = 2.21e5 Hz/(A/m). The solver can employ a Green function, transfer matrix, or finite-difference approach.
- Evidence: `/app/outputs/solver_script.py`

### Step 2: Compute polarizer transmission probabilities
- Role: scored (load-bearing)
- Action: Using the solver, simulate a 2/1/2 polarizer structure: a bilayer synthetic antiferromagnet with a 200 nm long central monolayer region where the upper sublayer is removed (i.e., a ¬1 monolayer with magnetization pointing upward). Inject left- and right-circular spin waves at frequency ω/(2π) = 6.5 GHz and compute the transmission probabilities T_L and T_R. Write the results to polarizer_results.json.
- Output file: `/app/outputs/polarizer_results.json`
- Format: json
- Contract: {"T_R": <float>, "T_L": <float>, "frequency_GHz": <float>}
- Scoring: scored by hidden verifier

### Step 3: Compute retarder relative phase delay
- Role: scored (load-bearing)
- Action: Using the solver, simulate a 2/3/2 retarder structure: a bilayer synthetic antiferromagnet with a 200 nm long central trilayer region where a third ferromagnetic layer is capped on top, with magnetization pinned antiparallel to the upper sublayer (magnetization downward, giving an effective field γH₂ = +J). Inject a linearly polarized spin wave (equal left/right circular components) at frequency ω/(2π) = 6.5 GHz and extract the accumulated relative phase delay δφ_LR between the left- and right-circular components after the central region. Write the results to retarder_results.json.
- Output file: `/app/outputs/retarder_results.json`
- Format: json
- Contract: {"delta_phi_LR": <float (radians)>, "frequency_GHz": <float>, "length_nm": <int>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/polarizer_results.json`
- `/app/outputs/retarder_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### polarizer_results.json
- path: `/app/outputs/polarizer_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Transmission probabilities for left- and right-circular spin waves through the 2/1/2 polarizer at 6.5 GHz. The scoring checks that T_L is large (≥0.95) and T_R is small (≤0.05), consistent with the paper's claim of near-perfect circular polarization filtering.
- schema:
  - `type`: object
  - `required`:
    - `T_R`: float
    - `T_L`: float
    - `frequency_GHz`: float
  - `units`:
    - `T_R`: dimensionless (probability)
    - `T_L`: dimensionless (probability)
    - `frequency_GHz`: GHz

### retarder_results.json
- path: `/app/outputs/retarder_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Accumulated relative phase delay between left- and right-circular spin wave components through the 2/3/2 retarder at 6.5 GHz. The scoring compares the reported δφ_LR value to the paper's reported phase delay within a tight tolerance.
- schema:
  - `type`: object
  - `required`:
    - `delta_phi_LR`: float
    - `frequency_GHz`: float
    - `length_nm`: int
  - `units`:
    - `delta_phi_LR`: radians
    - `frequency_GHz`: GHz
    - `length_nm`: nm

Notes: The solver must be implemented from scratch; no external code or pre-trained model is provided. All material parameters are given in the paper and included in the step actions. The capping layer magnetization direction for the retarder must follow the 2/‾3/2 configuration (pinned downward).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "polarizer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "T_R": "float",
          "T_L": "float",
          "frequency_GHz": "float"
        },
        "units": {
          "T_R": "dimensionless (probability)",
          "T_L": "dimensionless (probability)",
          "frequency_GHz": "GHz"
        }
      },
      "description": "Transmission probabilities for left- and right-circular spin waves through the 2/1/2 polarizer at 6.5 GHz. The scoring checks that T_L is large (≥0.95) and T_R is small (≤0.05), consistent with the paper's claim of near-perfect circular polarization filtering."
    },
    {
      "file": "retarder_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_phi_LR": "float",
          "frequency_GHz": "float",
          "length_nm": "int"
        },
        "units": {
          "delta_phi_LR": "radians",
          "frequency_GHz": "GHz",
          "length_nm": "nm"
        }
      },
      "description": "Accumulated relative phase delay between left- and right-circular spin wave components through the 2/3/2 retarder at 6.5 GHz. The scoring compares the reported δφ_LR value to the paper's reported phase delay within a tight tolerance."
    }
  ],
  "notes": "The solver must be implemented from scratch; no external code or pre-trained model is provided. All material parameters are given in the paper and included in the step actions. The capping layer magnetization direction for the retarder must follow the 2/‾3/2 configuration (pinned downward)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the artifact files you produce under `/app/outputs`.

- **Polarizer stage** (`polarizer_results.json`): the verifier checks T_L and T_R using a threshold‑or‑better policy. Full credit is awarded if T_L meets a high threshold and T_R does not exceed a low threshold; credit degrades gracefully as the values deviate from the expected performance of a good polarizer.
- **Retarder stage** (`retarder_results.json`): the verifier compares your reported δφ_LR to a hidden reference value using an exact‑match policy with a tight tolerance.

The two scored stages carry equal weight (50% each). The verifier also confirms that all required fields are present and correctly formatted. Simply reporting numbers known from the literature is not sufficient; you must demonstrate a working solver and produce results that realistically match the device physics.
