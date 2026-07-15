# DFT-calculated OER energetics for MIL-59 MOF variants

## Problem background
The oxygen evolution reaction (OER) is a kinetically sluggish process central to water electrolysis and metal-air batteries, demanding efficient catalysts. Metal-organic frameworks (MOFs) built from high-valent metal clusters, such as MIL-59, offer a platform to tune catalytic activity through coordination environment modification. This task computationally evaluates the OER energetics of MIL-59 variants with Fe, Ni, and FeNi active sites using density functional theory (DFT). By computing the Gibbs free-energy landscape of the four canonical OER steps and identifying rate-determining barriers, we can quantitatively connect coordination changes to catalytic performance.

## Approach
The computational approach begins with constructing tri‑nuclear molecular cluster models of MIL-59(Fe), MIL-59(Ni), and MIL-59(FeNi) from the public crystal structure of MIL-59(V). Charge‑neutralizing modifications are introduced: an –OH group on one Fe for MIL-59(Fe), protonation of two -COO- groups for MIL-59(Ni), and one Fe³⁺ → Ni²⁺ substitution to achieve Fe:Ni=2:1 for MIL-59(FeNi). All structures are optimized with DFT using the B3LYP functional, the Lanl2DZ pseudopotential for transition metals, and the 6-31G(d,p) basis set for other atoms. Vibrational frequency analysis confirms stationary points and provides zero‑point corrections and Gibbs free energies. From these energies, the free‑energy changes ΔG for the four elementary OER steps (H₂O → *OH, *OH → *O, *O → *OOH, *OOH → O₂) are computed for four active‑site cases: MIL‑59(Fe)@Fe, MIL‑59(Ni)@Ni, MIL‑59(FeNi)@Fe, and MIL‑59(FeNi)@Ni. Standard thermodynamic relations (O₂(g) + 2H₂(g) = 2H₂O(l) + 4×1.23 eV, ½H₂(g) = H⁺ + e⁻) are used to reference free energies. The rate‑determining step (largest ΔG) is identified for each system. As an additional electronic‑structure probe, Mulliken charges on the active Fe atom in the *OOH intermediate are computed for MIL‑59(Fe) and MIL‑59(FeNi) to obtain the charge difference Δq.

## Reproduction target
Compute the Gibbs free‑energy changes (ΔG, in eV) for the four OER elementary steps on MIL-59(Fe)@Fe, MIL-59(Ni)@Ni, MIL-59(FeNi)@Fe, and MIL-59(FeNi)@Ni using DFT. Identify the rate‑determining step barrier for each system. Compute the Mulliken charge difference (Δq, in |e|) on the active Fe atom in the *OOH intermediate between MIL‑59(Fe) and MIL‑59(FeNi). All results must be written to the file `/app/outputs/dft_oer_energies.json` following the output contract.

## Assets

- MIL-59(V) crystal structure (Barthelet et al., 2002): 10.1039/B202498J
- Open-source DFT code (e.g., NWChem): https://github.com/nwchemgit/nwchem
- Standard thermodynamic references for OER free-energy calculations

## Workflow steps

### Step 1: Construct molecular cluster models
- Role: process
- Action: Build tri-nuclear cluster models of MIL-59(Fe), MIL-59(Ni), and MIL-59(FeNi) based on the crystal structure of MIL-59(V). Apply charge-neutralizing modifications: replace outer anion with an -OH group on one Fe for MIL-59(Fe); protonate two -COO- groups for MIL-59(Ni); substitute one Fe3+ by Ni2+ to obtain Fe:Ni=2:1 for MIL-59(FeNi). Save the molecular models.
- Evidence: `/app/outputs/mil59_models.zip`

### Step 2: DFT geometry optimization and vibrational analysis
- Role: process
- Action: Using an open-source DFT code (e.g., NWChem), optimize the structures of all molecular cluster models with the B3LYP functional, Lanl2DZ pseudopotential for transition metals, and 6-31G(d,p) basis set for other atoms. Perform vibrational frequency analysis to confirm no imaginary frequencies and obtain Gibbs free energies and zero-point energies.
- Evidence: `/app/outputs/dft_calculation_logs.zip`

### Step 3: Compute OER energetics, rate-determining steps, and Mulliken charges
- Role: scored (load-bearing)
- Action: From the DFT energies and standard thermodynamic relations, compute Gibbs free-energy changes (ΔG in eV) for the four OER elementary steps on each system: MIL-59(Fe)@Fe, MIL-59(Ni)@Ni, MIL-59(FeNi)@Fe, MIL-59(FeNi)@Ni. Identify the rate-determining step (largest ΔG) and extract its barrier. Compute Mulliken charges on the active Fe atom in the *OOH intermediate for MIL-59(Fe) and MIL-59(FeNi) and the difference Δq. Write all results to dft_oer_energies.json.
- Output file: `/app/outputs/dft_oer_energies.json`
- Format: json
- Contract: A JSON object with keys: 'systems' (object with system identifiers as keys and arrays of four ΔG floats in eV), 'rate_determining_step_barriers' (object with the same identifiers and RDS barrier float in eV), and 'mulliken_charge_difference_fe_ooH' (float in |e|).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_oer_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_oer_energies.json
- path: `/app/outputs/dft_oer_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The agent's self-reported OER free-energy changes, rate-determining barriers, and Mulliken charge difference from DFT calculations.
- schema:
  - `type`: object
  - `required`: `systems`, `rate_determining_step_barriers`, `mulliken_charge_difference_fe_ooH`
  - `properties`:
    - `systems`:
      - `type`: object
      - `description`: keys: 'MIL-59(Fe)@Fe', 'MIL-59(Ni)@Ni', 'MIL-59(FeNi)@Fe', 'MIL-59(FeNi)@Ni'; each value an array of four floats in eV
    - `rate_determining_step_barriers`:
      - `type`: object
      - `description`: keys: same system identifiers; each value a float in eV
    - `mulliken_charge_difference_fe_ooH`:
      - `type`: number
      - `description`: difference in units of |e|

Notes: The hidden checker compares each reported ΔG array and RDS barrier to paper gold values with tolerance ±0.10 eV, the Mulliken charge difference with tolerance ±0.005 |e|, and verifies the ordering barrier(MIL-59(FeNi)@Fe) < barrier(MIL-59(Fe)@Fe) < barrier(MIL-59(Ni)@Ni).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_oer_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "systems",
          "rate_determining_step_barriers",
          "mulliken_charge_difference_fe_ooH"
        ],
        "properties": {
          "systems": {
            "type": "object",
            "description": "keys: 'MIL-59(Fe)@Fe', 'MIL-59(Ni)@Ni', 'MIL-59(FeNi)@Fe', 'MIL-59(FeNi)@Ni'; each value an array of four floats in eV"
          },
          "rate_determining_step_barriers": {
            "type": "object",
            "description": "keys: same system identifiers; each value a float in eV"
          },
          "mulliken_charge_difference_fe_ooH": {
            "type": "number",
            "description": "difference in units of |e|"
          }
        }
      },
      "description": "The agent's self-reported OER free-energy changes, rate-determining barriers, and Mulliken charge difference from DFT calculations."
    }
  ],
  "notes": "The hidden checker compares each reported ΔG array and RDS barrier to paper gold values with tolerance ±0.10 eV, the Mulliken charge difference with tolerance ±0.005 |e|, and verifies the ordering barrier(MIL-59(FeNi)@Fe) < barrier(MIL-59(Fe)@Fe) < barrier(MIL-59(Ni)@Ni)."
}
```

## How you are scored
A hidden verifier independently scores your submission by comparing the computed ΔG arrays and rate‑determining‑step barriers against reference values, checking the ordering of the barriers across systems, and evaluating the Mulliken charge difference. Each scored component is assigned a weight; the final reward is the weighted sum. Accurate reproduction of the described DFT procedure and faithful reporting of the results within the required tolerances are necessary to achieve a high score.
