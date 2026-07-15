# Ferroelectric Multistability of SnS and GeSe Monolayers via DFT

## Problem background
Group-IV monochalcogenide monolayers, such as SnS and GeSe, have a puckered orthorhombic structure that can exist in multiple orientation states. These materials have been proposed as candidate platforms for non-volatile ferroelectric memories because their puckering direction may be switched by external stimuli. The monolayers can adopt a polar Pnma-like phase and a higher-symmetry, non-polar Cmcm-like phase. Two quantities are central to evaluating their ferroelectric functionality: the energetic barrier between these phases (activation energy for puckering reorientation) and the magnitude of the spontaneous polarization in the ground-state polar phase. This task reproduces these two quantities from first-principles density functional theory (DFT).

## Approach
The reproduction uses plane-wave DFT as implemented in the QUANTUM ESPRESSO package with the PBE exchange-correlation functional and Troullier-Martins pseudopotentials. For each of the two materials, SnS and GeSe, two monolayer structures are built: the polar Pnma-ML phase (distorted) and the centrosymmetric Cmcm-ML phase (undistorted). The workflow consists of three conceptual stages:

1. **Structure construction:** Generate the initial atomic models for both phases using the fractional coordinates described below.
2. **Relaxation and energy evaluation:** Relax the geometries of all four structures, obtain their ground-state total energies, and compute the activation energy as the energy difference between the Cmcm-ML and Pnma-ML phases for each material.
3. **Polarization calculation:** From the relaxed Pnma-ML structures, compute the spontaneous polarization relative to the centrosymmetric Cmcm-ML reference using the modern theory of polarization (Berry phase) within QUANTUM ESPRESSO.

The resulting numbers characterise the ferroelectric double-well energy landscape and the spontaneous electric dipole of each monolayer.

## Reproduction target
Produce two JSON files under `/app/outputs`:

- `activation_energies.json` must contain the activation energies for puckering reorientation of SnS and GeSe, in meV. The structure is an object with keys `"SnS"` and `"GeSe"`, each mapping to a floating-point number.
- `polarization_values.json` must contain the spontaneous polarization magnitudes of SnS and GeSe, in C/m², relative to the centrosymmetric reference. The structure is an object with keys `"SnS"` and `"GeSe"`, each mapping to an object `{"P": <float>}`.

All values must be derived from the DFT calculations described in the workflow, and the units must match the contract exactly. The task is complete when both files are correctly written to the specified paths with the required structure.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Troullier-Martins PBE pseudopotentials for Sn, S, Ge, Se: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Crystal structure preparation
- Role: process
- Action: Generate the initial atomic structures for Pnma-ML and Cmcm-ML phases of SnS and GeSe using the fractional coordinates: Pnma-ML ±(M:0.25±δ, 0.25, 0.05; X:0.25, 0.25, -0.05) with δ=0.06 (SnS), δ=0.08 (GeSe); Cmcm-ML with δ=0. Prepare the input files for Quantum ESPRESSO.
- Evidence: none

### Step 2: DFT Relaxation and Activation Energy Calculation
- Role: scored (load-bearing)
- Action: Run Quantum ESPRESSO to relax the Pnma-ML and Cmcm-ML structures of SnS and GeSe using PBE functional, Troullier-Martins pseudopotentials, plane-wave cutoff 70 Ry, charge density cutoff 280 Ry, and Monkhorst-Pack k-point grid 10×10×1. From the relaxed total energies, compute the activation energy for puckering reorientation as the energy difference between the Cmcm-ML and Pnma-ML phases for each material. Output the activation energies in meV as a JSON file.
- Output file: `/app/outputs/activation_energies.json`
- Format: json
- Contract: {"SnS": <float, unit meV>, "GeSe": <float, unit meV>}
- Scoring: scored by hidden verifier

### Step 3: Spontaneous Polarization via Berry Phase
- Role: scored (load-bearing)
- Action: Using the relaxed Pnma-ML structures from the previous step, perform a Berry-phase polarization calculation within Quantum ESPRESSO (modern theory of polarization) to obtain the spontaneous polarization relative to the centrosymmetric Cmcm-ML reference. Use the same computational parameters. Output the polarization in C/m² as a JSON file.
- Output file: `/app/outputs/polarization_values.json`
- Format: json
- Contract: {"SnS": {"P": <float, unit C/m^2>}, "GeSe": {"P": <float, unit C/m^2>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.json`
- `/app/outputs/polarization_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.json
- path: `/app/outputs/activation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Activation energies for puckering reorientation of SnS and GeSe monolayers, in meV.
- schema:
  - `type`: object
  - `required`:
    - `SnS`: float; unit meV
    - `GeSe`: float; unit meV

### polarization_values.json
- path: `/app/outputs/polarization_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Spontaneous polarization of SnS and GeSe monolayers relative to the centrosymmetric phase, in C/m².
- schema:
  - `type`: object
  - `required`:
    - `SnS`: object with key "P" (float, unit C/m^2)
    - `GeSe`: object with key "P" (float, unit C/m^2)

Notes: Scoring compares computed values to the paper's reported ones within prescribed tolerances. Exact_match policy with appropriate absolute tolerance is applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "SnS": "float; unit meV",
          "GeSe": "float; unit meV"
        }
      },
      "description": "Activation energies for puckering reorientation of SnS and GeSe monolayers, in meV."
    },
    {
      "file": "polarization_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "SnS": "object with key \"P\" (float, unit C/m^2)",
          "GeSe": "object with key \"P\" (float, unit C/m^2)"
        }
      },
      "description": "Spontaneous polarization of SnS and GeSe monolayers relative to the centrosymmetric phase, in C/m²."
    }
  ],
  "notes": "Scoring compares computed values to the paper's reported ones within prescribed tolerances. Exact_match policy with appropriate absolute tolerance is applied."
}
```

## How you are scored
A hidden verifier independently checks each output file. For `activation_energies.json`, the verifier compares the submitted activation energies to a hidden reference using an appropriate comparison that accounts for run‑to‑run spread. For `polarization_values.json`, the verifier compares the submitted polarization values to a hidden reference in the same way. Meeting or exceeding the agreement threshold earns full credit for that artifact. The final reward is a weighted sum of the per‑artifact scores. Simply guessing or reporting plausible numbers without correct DFT results will not achieve full credit; the reward reflects genuine computational agreement with the expected reference.
