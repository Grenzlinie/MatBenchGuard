# DFT Energy Barriers and Reaction Energies for Propene Cyclization in ZSM-5

## Problem background
The methanol-to-olefins (MTO) process on acid zeolites relies on hydrocarbon pool species formed from small olefins. Understanding how cyclic hydrocarbon precursors are built from ethene and propene inside the ZSM-5 (MFI) catalyst is central to controlling catalyst activity and lifetime. The proposed low-energy cyclization route starts from propene adsorption, forms a framework-bound n-propoxide, undergoes stepwise dimerization with a second propene to a 2-hexyl carbenium ion, and ends with rapid ring closure to methylcyclopentane. Accurate modeling requires inclusion of the zeolite framework environment and long-range van der Waals dispersion corrections, as omitted dispersion can alter barriers and reaction energies substantially. Your task is to compute the electronic energy barriers and reaction energies for three key elementary steps along this pathway using a first-principles ONIOM/DFT-D protocol.

## Approach
A finite 46T cluster is cut from the MFI crystallographic structure around the T12 Brønsted acid site at the channel intersection; terminal hydrogen atoms are constrained to prevent unphysical deformation. Geometries of all stationary points (reactants, products, transition states) are optimized using a two-layer ONIOM scheme with high level B3LYP/6-31+g(d) and low level MNDO. Harmonic frequency analysis confirms minima and transition states. Single-point energies are then refined at a higher low-level theory: ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d)). Finally, the Grimme DFT-D empirical dispersion correction is added to obtain dispersion-corrected electronic energies. From these, electronic activation barriers (ΔE‡) and reaction energies (ΔEr) are extracted for the three specific reactions: n-propoxide formation (A2), stepwise propene dimerization to 2-hexyl carbenium ion (A5), and cyclization to methylcyclopentane (B1).

## Reproduction target
Compute the electronic energy barriers (ΔE‡) and reaction energies (ΔEr) for reactions A2, A5, and B1 using the ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d))‑D//ONIOM(B3LYP/6-31+g(d):MNDO) protocol on a 46T MFI cluster. Report all six dispersion‑corrected values (in kJ/mol) in a single JSON file at `/app/outputs/energies.json` with keys A2_E_barrier, A2_E_reaction, A5_E_barrier, A5_E_reaction, B1_E_barrier, B1_E_reaction.

## Assets

- IZA-SC MFI zeolite crystal structure: https://www.iza-structure.org/databases/
- ORCA or equivalent quantum chemistry package with ONIOM and Grimme DFT-D: https://orcaforum.kofo.mpg.de/
- 6-31+G(d) basis set: built-in

## Workflow steps

### Step 1: Cluster model construction
- Role: process
- Action: Cut a 46T finite cluster from the MFI crystallographic structure around the T12 Brønsted acid site, terminate with hydrogen atoms, and apply constraints to peripheral hydrogens to prevent unphysical deformation.
- Evidence: none

### Step 2: Geometry optimization and transition state search
- Role: process
- Action: Optimize geometries for all reactants, products, and transition states of reactions A2 (n-propoxide formation), A5 (stepwise propene dimerization to 2-hexyl carbenium ion), and B1 (cyclization to methylcyclopentane) using ONIOM(B3LYP/6-31+g(d):MNDO) on the 46T cluster. Perform harmonic frequency analysis to confirm minima (no imaginary frequencies) and transition states (exactly one imaginary frequency).
- Evidence: none

### Step 3: Single-point energy refinement
- Role: process
- Action: At each optimized geometry, compute single-point electronic energies using the higher-level ONIOM(B3LYP/6-31+g(d):HF/6-31+g(d)) method.
- Evidence: none

### Step 4: DFT-D dispersion correction
- Role: process
- Action: Add the Grimme DFT-D empirical dispersion correction to the single-point energies from step s2. This yields the final dispersion-corrected electronic energies for all stationary points.
- Evidence: none

### Step 5: Extract barriers and reaction energies
- Role: scored (load-bearing)
- Action: From the dispersion-corrected energies, calculate the electronic activation barrier ΔE‡ and reaction energy ΔEr for each elementary step (A2, A5, B1). Write all six values (in kJ/mol) to energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: JSON object with six keys: A2_E_barrier, A2_E_reaction, A5_E_barrier, A5_E_reaction, B1_E_barrier, B1_E_reaction. Values are floats in kJ/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dispersion-corrected (DFT-D) electronic energy barriers, reaction energies, and transition-state-theory rate constants at 673 K for the three key cyclization steps in H‑ZSM-5, computed with the ONIOM(B3LYP/6‑31+g(d):HF/6‑31+g(d))‑D//ONIOM(B3LYP/6‑31+g(d):MNDO) protocol.
- schema:
  - `type`: object
  - `required`: `A2_E_barrier`, `A2_E_reaction`, `A5_E_barrier`, `A5_E_reaction`, `B1_E_barrier`, `B1_E_reaction`, `A2_k_forward`, `A2_k_backward`, `A5_k_forward`, `A5_k_backward`, `B1_k_forward`, `B1_k_backward`
  - `units`:
    - `A2_E_barrier`: kJ/mol
    - `A2_E_reaction`: kJ/mol
    - `A5_E_barrier`: kJ/mol
    - `A5_E_reaction`: kJ/mol
    - `B1_E_barrier`: kJ/mol
    - `B1_E_reaction`: kJ/mol
    - `A2_k_forward`: s⁻¹
    - `A2_k_backward`: s⁻¹
    - `A5_k_forward`: s⁻¹
    - `A5_k_backward`: s⁻¹
    - `B1_k_forward`: s⁻¹
    - `B1_k_backward`: s⁻¹

Notes: Only the electronic barriers, reaction energies, and rate constants for reactions A2, A5, and B1 are scored. The checker compares each value against the paper’s reference values with a hidden tolerance; no tolerance or gold values are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "A2_E_barrier",
          "A2_E_reaction",
          "A5_E_barrier",
          "A5_E_reaction",
          "B1_E_barrier",
          "B1_E_reaction",
          "A2_k_forward",
          "A2_k_backward",
          "A5_k_forward",
          "A5_k_backward",
          "B1_k_forward",
          "B1_k_backward"
        ],
        "units": {
          "A2_E_barrier": "kJ/mol",
          "A2_E_reaction": "kJ/mol",
          "A5_E_barrier": "kJ/mol",
          "A5_E_reaction": "kJ/mol",
          "B1_E_barrier": "kJ/mol",
          "B1_E_reaction": "kJ/mol",
          "A2_k_forward": "s⁻¹",
          "A2_k_backward": "s⁻¹",
          "A5_k_forward": "s⁻¹",
          "A5_k_backward": "s⁻¹",
          "B1_k_forward": "s⁻¹",
          "B1_k_backward": "s⁻¹"
        }
      },
      "description": "Dispersion-corrected (DFT-D) electronic energy barriers, reaction energies, and transition-state-theory rate constants at 673 K for the three key cyclization steps in H‑ZSM-5, computed with the ONIOM(B3LYP/6‑31+g(d):HF/6‑31+g(d))‑D//ONIOM(B3LYP/6‑31+g(d):MNDO) protocol."
    }
  ],
  "notes": "Only the electronic barriers, reaction energies, and rate constants for reactions A2, A5, and B1 are scored. The checker compares each value against the paper’s reference values with a hidden tolerance; no tolerance or gold values are disclosed."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/energies.json` and compares each of the six values against a hidden reference derived from the original study. Each value is scored independently: if the computed value falls within a tolerance band around the reference it earns full credit for that quantity; larger deviations receive progressively lower credit. The final reward is the average score across all six quantities. The tolerance is chosen to absorb legitimate spread from toolchain and implementation differences. Reporting the reference numbers without running the workflow will not pass—the checker rewards genuine computation, not guesswork.
