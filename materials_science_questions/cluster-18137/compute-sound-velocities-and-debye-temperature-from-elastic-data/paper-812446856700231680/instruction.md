# Compute Effective Debye Temperature from Phase-Weighted Mixing Rule for Mixed Alkali Halide

## Problem background
Mixed alkali halide crystals such as KBr-KI can exhibit compositional fluctuations at the nanoscale, yet their low-temperature thermal properties may remain crystalline. Determining whether such fluctuations induce glass-like thermal behaviour requires a consistent description of the material's Debye temperature. One approach treats the material as a mixture of discrete crystalline phases characterised by distinct compositions and volume fractions. The effective Debye temperature of the aggregate then emerges from a weighted combination of the phase properties. This task focuses on computing that effective Debye temperature for a polycrystalline KBr₀.₅₃I₀.₄₇ sample, given publicly known end‑member lattice constants, molar masses, and Debye temperatures, together with the phase composition data. The computed result provides a theoretical reference that can be compared with measured specific-heat data.

## Approach
The material is modeled as three coexisting crystalline phases with known KBr fractions and volume fractions. For each phase, the lattice constant is obtained from Vegard's law (linear interpolation between the pure KBr and KI constants). The mass density follows from the lattice constant and the rocksalt crystal structure (four formula units per conventional cell). The Debye temperature of a phase is estimated by an inverse‑square mixing rule that interpolates between the known pure‑material Debye temperatures weighted by the KBr fraction. Finally, the low‑temperature Debye specific heat per unit volume (proportional to ρ/θD³) is computed for each phase, and a volume‑fraction‑weighted average of these heat capacities yields an effective Debye temperature for the entire aggregate. This three‑stage calculation (lattice constants and densities → phase Debye temperatures → weighted effective Debye temperature) captures the essential physics while relying only on public input constants.

## Reproduction target
Reproduce the effective Debye temperature of a polycrystalline KBr₀.₅₃I₀.₄₇ sample by performing the following calculation: (1) using the pure KBr and KI lattice constants and Vegard's law, compute the lattice constant and density for each of the three phases identified by Nair & Walker (KBr₀.₂₆I₀.₇₄, KBr₀.₅I₀.₅, KBr₀.₈₇I₀.₁₃); (2) apply the inverse‑square mixing rule to obtain the Debye temperature of each phase from the pure end‑member Debye temperatures (θD,KBr = 172 K, θD,KI = 132 K); (3) compute the low‑temperature Debye heat capacity per unit volume for each phase, weight by the published volume fractions (43%, 24%, 33%), and extract the effective Debye temperature of the aggregate. Report every intermediate quantity and the final effective Debye temperature in the JSON file `computed_values.json` with the required schema.

## Assets

- Lattice constants of KBr and KI (NaCl structure)
- Pure-material Debye temperatures (θD,KBr=172 K, θD,KI=132 K): https://doi.org/10.1103/PhysRev.161.877
- Phase compositions and volume fractions from Nair: https://doi.org/10.1103/PhysRevB.5.4101
- Molar masses of KBr and KI

## Workflow steps

### Step 1: Compute phase lattice constants and densities
- Role: process
- Action: Using the pure KBr (6.600 Å) and KI (7.066 Å) lattice constants, apply Vegard's law linear interpolation to compute the lattice constants for the three phases: KBr0.26I0.74, KBr0.5I0.5, KBr0.87I0.13. Then compute the mass density for each phase from the lattice constant and the molar mass (rocksalt structure, 4 formula units per cell).
- Evidence: none

### Step 2: Compute phase-specific Debye temperatures
- Role: process
- Action: For each phase, apply the inverse-square mixing rule: 1/θD² = x/θD_KBr² + (1-x)/θD_KI², where θD_KBr=172 K, θD_KI=132 K, and x is the KBr fraction in the phase. Compute θD for each of the three phases.
- Evidence: none

### Step 3: Compute effective Debye temperature and write results
- Role: scored (load-bearing)
- Action: Combine the phase densities (from step_01), phase Debye temperatures (from step_02), and the volume fractions (43%, 24%, 33%) to compute the low-temperature Debye specific heat per unit volume for each phase (C_V ∝ ρ / θD³). Perform a volume-fraction weighted average of the heat capacities, and from that weighted average extract an effective Debye temperature for the polycrystalline aggregate. Output all computed quantities (phase compositions, volume fractions, lattice constants, densities, phase Debye temperatures, effective Debye temperature) as a JSON file 'computed_values.json'.
- Output file: `/app/outputs/computed_values.json`
- Format: json
- Contract: JSON object with keys: 'phase_compositions' (list of three floats, KBr fraction for each phase), 'volume_fractions' (list of three floats), 'phase_lattice_constants_A' (list of three floats in Å), 'phase_densities_g_per_cc' (list of three floats), 'phase_theta_D_K' (list of three floats), 'theta_D_effective_K' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_values.json
- path: `/app/outputs/computed_values.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Contains all computed intermediate quantities and the final effective Debye temperature; the checker recomputes theta_D_effective_K from the reported phase densities and Debye temperatures and compares it against the paper's reference value, after first verifying internal consistency of the intermediates.
- schema:
  - `type`: object
  - `required`: `phase_compositions`, `volume_fractions`, `phase_lattice_constants_A`, `phase_densities_g_per_cc`, `phase_theta_D_K`, `theta_D_effective_K`
  - `properties`:
    - `phase_compositions`:
      - `type`: array
      - `items`:
        - `type`: number
    - `volume_fractions`:
      - `type`: array
      - `items`:
        - `type`: number
    - `phase_lattice_constants_A`:
      - `type`: array
      - `items`:
        - `type`: number
    - `phase_densities_g_per_cc`:
      - `type`: array
      - `items`:
        - `type`: number
    - `phase_theta_D_K`:
      - `type`: array
      - `items`:
        - `type`: number
    - `theta_D_effective_K`:
      - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "phase_compositions",
          "volume_fractions",
          "phase_lattice_constants_A",
          "phase_densities_g_per_cc",
          "phase_theta_D_K",
          "theta_D_effective_K"
        ],
        "properties": {
          "phase_compositions": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "volume_fractions": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "phase_lattice_constants_A": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "phase_densities_g_per_cc": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "phase_theta_D_K": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "theta_D_effective_K": {
            "type": "number"
          }
        }
      },
      "description": "Contains all computed intermediate quantities and the final effective Debye temperature; the checker recomputes theta_D_effective_K from the reported phase densities and Debye temperatures and compares it against the paper's reference value, after first verifying internal consistency of the intermediates."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently recompute all intermediate quantities from the same public inputs (lattice constants, molar masses, pure Debye temperatures, phase compositions, and volume fractions) using the identical formulas. It checks that the lattice constants, densities, and phase Debye temperatures you report are internally consistent with the recomputed values. Then, using YOUR reported phase densities and Debye temperatures, the verifier recomputes the effective Debye temperature via the heat‑capacity weighting formula and compares it to a hidden reference value. The total reward is 1.0 only if both the internal consistency and the final effective Debye temperature pass the verification; otherwise the reward is reduced or zero. Reporting a plausible number without a correct, self‑consistent calculation does not suffice.
