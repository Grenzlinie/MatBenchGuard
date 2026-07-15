# Γ-point H_g phonon frequencies in alkali-doped fullerides A₃C₆₀

## Problem background
Alkali-doped fullerides $A_3$C$_{60}$ (A = K, Rb, Cs) are superconductors whose pairing mechanism has been debated. Reliable first-principles phonon frequencies, especially the strongly coupled intramolecular $H_g$ modes at the Γ point, are essential input for understanding electron‑phonon coupling and superconductivity. The task is to compute these Γ‑point $H_g$ phonon frequencies using density-functional perturbation theory (DFPT) within the local density approximation (LDA).

## Approach
We use first-principles plane‑wave pseudopotential calculations with Quantum ESPRESSO. For each compound we first optimize the crystal structure (lattice constants and atomic positions) under the required pressure conditions using LDA pseudopotentials. From the relaxed structure we then perform a DFPT phonon calculation at the Γ point. The phonon spectrum yields eight fivefold‑degenerate intramolecular $H_g$‑derived modes; for each degenerate branch we compute the average frequency. The whole procedure is carried out for the three compounds individually.

## Reproduction target
Calculate the Γ‑point $H_g$ phonon frequencies (in cm⁻¹) for fcc K$_3$C$_{60}$, Rb$_3$C$_{60}$, and Cs$_3$C$_{60}$ (the latter under a pressure of 7 kbar). The result must be written to `/app/outputs/phonon_frequencies.json` as a JSON object with top‑level keys `K3C60`, `Rb3C60`, `Cs3C60`. Each value is an object mapping the mode labels `Hg1` through `Hg8` to the corresponding numeric frequency.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- C pseudopotential (LDA)
- K pseudopotential (LDA)
- Rb pseudopotential (LDA)
- Cs pseudopotential (LDA)
- Crystal structures of fcc A3C60

## Workflow steps

### Step 1: Structural relaxation of A₃C₆₀
- Role: process
- Action: For each compound (K3C60, Rb3C60, Cs3C60), perform DFT structural relaxation using the LDA pseudopotentials. Optimize lattice constants and atomic positions. For Cs3C60, relax under a pressure of 7 kbar. Produce relaxed structures for the subsequent phonon calculation.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 2: Γ-point phonon frequency calculation
- Role: scored (load-bearing)
- Action: Using the relaxed structures, run a density functional perturbation theory (DFPT) phonon calculation at the Γ point with Quantum ESPRESSO. Identify the eight fivefold-degenerate H_g-derived modes (Hg1–Hg8) for each compound. Compute the average frequency (cm⁻¹) of each degenerate branch and output the results.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object with top-level keys 'K3C60', 'Rb3C60', 'Cs3C60'. Each value is an object with keys 'Hg1' through 'Hg8' whose values are numeric frequencies (cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Γ-point H_g phonon frequencies for the three alkali-doped fullerides. Frequencies are compared against hidden reference values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `K3C60`: object
    - `Rb3C60`: object
    - `Cs3C60`: object
  - `items`:
    - `Hg1`: number
    - `Hg2`: number
    - `Hg3`: number
    - `Hg4`: number
    - `Hg5`: number
    - `Hg6`: number
    - `Hg7`: number
    - `Hg8`: number
  - `units`:
    - `frequency`: cm⁻¹

Notes: Temporarily removed the superconducting_tc.json output to resolve missing solve block; the Tc calculation will be re-added in a subsequent step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "K3C60": "object",
          "Rb3C60": "object",
          "Cs3C60": "object"
        },
        "items": {
          "Hg1": "number",
          "Hg2": "number",
          "Hg3": "number",
          "Hg4": "number",
          "Hg5": "number",
          "Hg6": "number",
          "Hg7": "number",
          "Hg8": "number"
        },
        "units": {
          "frequency": "cm⁻¹"
        }
      },
      "description": "Γ-point H_g phonon frequencies for the three alkali-doped fullerides. Frequencies are compared against hidden reference values with tolerance."
    }
  ],
  "notes": "Temporarily removed the superconducting_tc.json output to resolve missing solve block; the Tc calculation will be re-added in a subsequent step."
}
```

## How you are scored
A hidden verifier will compare each reported frequency against a reference value with an absolute tolerance. It will also check that the three compounds yield nearly the same frequency for each $H_g$ mode (small alkali‑metal dependence). The final reward is the fraction of the 24 individual frequencies (3 compounds × 8 modes) that satisfy both the per‑mode tolerance and the inter‑compound consistency requirement. Only the numerical values in `/app/outputs/phonon_frequencies.json` are considered; the verifier does not inspect intermediate files. There is no need to match any particular code version or achieve exact equality — correctness is judged solely by the computed frequencies.
