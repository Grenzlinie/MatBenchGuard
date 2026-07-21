# Potential Energy Profile for H₂S Decomposition on ZnO(10-10) Surface

## Problem background
Hydrogen sulfide (H₂S) must be removed from syngas and natural gas to meet environmental regulations and protect downstream catalysts. Zinc oxide (ZnO) is a highly effective desulfurizer, but the molecular-level details of its sulfurization mechanism – how H₂S adsorbs, dissociates, and ultimately forms H₂, H₂O, and surface sulfur – are not fully resolved. Understanding the reaction pathways on the stable nonpolar ZnO(10–10) surface is essential for optimizing desulfurization performance. This task uses density functional theory (DFT) to map the potential energy landscape of H₂S decomposition, comparing competing routes that produce either H₂ or H₂O, and determines which pathway is both kinetically and thermodynamically preferred.

## Approach
The study employs periodic DFT with a GGA functional (PW91 or an equivalent, e.g., PBE) to model the ZnO(10–10) surface as a six-layer slab in a p(2×2) supercell separated by a 1 nm vacuum. The bottom two layers are kept fixed. The approach proceeds in three stages:
1. Validate the computational setup by optimizing bulk ZnO and a free H₂S molecule, checking that calculated lattice parameters and bond lengths agree with experiment. Confirm slab convergence.
2. Determine the most stable adsorption geometries of all intermediates: molecular and dissociative H₂S, SH, S, and H atoms, as well as their coadsorption configurations (SH+H and S+2H). The most stable configuration of each species serves as the reactant or intermediate for the reaction network.
3. Starting from these intermediates, locate the transition states (TS1–TS6) and final products (P1, P2, P3) for the three decomposition pathways using LST/QST or nudged elastic band (NEB) methods. Compute the total energy of every stationary point and then tabulate the relative energies (kJ mol⁻¹) with respect to the initial H₂S adsorption state.

The resulting potential energy profile allows a direct comparison of the H₂‑forming and H₂O‑forming routes.

## Reproduction target
Using the slab model and DFT method described above, compute the relative energies (in kJ mol⁻¹) of ALL stationary states along the three H₂S decomposition pathways on ZnO(10–10). The states are: H₂S(a), TS1, SH+H(a), TS2, S+2H(b), TS3, P1, TS4, S+2H(c), TS5, P2, TS6, and P3. All energies must be referenced to the initial H₂S(a) adsorption configuration (set to 0). The produced file must also allow a comparison that identifies which overall reaction pathway is the most kinetically and thermodynamically favorable – i.e., which route has the lowest effective barrier and the most exothermic overall reaction – without presupposing the answer.

## Assets

- Open-source periodic DFT code (Quantum ESPRESSO or equivalent): https://www.quantum-espresso.org
- Pseudopotentials for Zn, O, H, S: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Method validation and slab model setup
- Role: process
- Action: Validate the DFT computational setup (functional, pseudopotentials, cutoffs, k‑point sampling) by optimizing bulk ZnO and gas‑phase H₂S, verifying agreement with experimental lattice parameters and bond lengths/angles. Construct a 6‑layer p(2×2) ZnO(10‑10) slab with a 1 nm vacuum gap and confirm model convergence to within acceptable energy differences.
- Evidence: `/app/outputs/validation_log.txt`

### Step 2: Geometry optimization of adsorption intermediates and coadsorption structures
- Role: process
- Action: On the 6‑layer p(2×2) ZnO(10‑10) slab (bottom two layers fixed), optimize the geometries and compute total energies of single adsorbates H₂S(a), SH (three binding modes), S (three modes), H (two sites), and their coadsorption configurations SH+H(a, b) and S+2H(a, b, c). Identify the most stable configuration for each species as the intermediates for the reaction pathway.
- Evidence: `/app/outputs/adsorption_energies.csv`

### Step 3: Transition state search and potential energy profile
- Role: scored (load-bearing)
- Action: Starting from the optimized intermediate structures, locate the transition states TS1–TS6 and the final products P1, P2, P3 using LST/QST or NEB methods at the same DFT level. Compute the total energy of each stationary state, then calculate the relative energy (kJ mol⁻¹) of every state with respect to the H₂S(a) adsorption state (set to 0). Write the results to reaction_energies.json.
- Output file: `/app/outputs/reaction_energies.json`
- Format: json
- Contract: JSON object with keys H2S_a, TS1, SH_H_a, TS2, S_2H_b, TS3, P1, TS4, S_2H_c, TS5, P2, TS6, P3. Each value is an object with field 'relative_energy_kJmol' (float). Energies in kJ mol⁻¹, relative to H₂S(a) set to 0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reaction_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_energies.json
- path: `/app/outputs/reaction_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative energies of all stationary states along the three H₂S decomposition pathways on ZnO(10-10). H₂S(a) must be 0; all others in kJ mol⁻¹.
- schema:
  - `type`: object
  - `required_keys`: `H2S_a`, `TS1`, `SH_H_a`, `TS2`, `S_2H_b`, `TS3`, `P1`, `TS4`, `S_2H_c`, `TS5`, `P2`, `TS6`, `P3`
  - `value_schema`:
    - `type`: object
    - `required`: `relative_energy_kJmol`
    - `properties`:
      - `relative_energy_kJmol`:
        - `type`: number

Notes: The checker compares each state's relative energy to the paper-reported reference value within a tolerance and also verifies activation energy trends (e.g., TS3 > 300 kJ/mol, TS4 approx. 220 kJ/mol, TS6 < 100 kJ/mol, P3 most negative).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "H2S_a",
          "TS1",
          "SH_H_a",
          "TS2",
          "S_2H_b",
          "TS3",
          "P1",
          "TS4",
          "S_2H_c",
          "TS5",
          "P2",
          "TS6",
          "P3"
        ],
        "value_schema": {
          "type": "object",
          "required": [
            "relative_energy_kJmol"
          ],
          "properties": {
            "relative_energy_kJmol": {
              "type": "number"
            }
          }
        }
      },
      "description": "Relative energies of all stationary states along the three H₂S decomposition pathways on ZnO(10-10). H₂S(a) must be 0; all others in kJ mol⁻¹."
    }
  ],
  "notes": "The checker compares each state's relative energy to the paper-reported reference value within a tolerance and also verifies activation energy trends (e.g., TS3 > 300 kJ/mol, TS4 approx. 220 kJ/mol, TS6 < 100 kJ/mol, P3 most negative)."
}
```

## How you are scored
A hidden verifier reads your `reaction_energies.json` after execution. It compares each state’s relative energy to a reference set of values (derived from an independent DFT study of the same system) using an appropriate tolerance. The verifier also checks that the energetic ordering and trends among pathways are physically consistent: for example, it verifies that certain elementary steps have activation barriers above a large threshold (making them unfavorable), that the rate‑limiting step for the preferred pathway has a moderate barrier, and that one of the final products is clearly the most exothermic. The final score combines the accuracy of the state‑by‑state relative energies (weight 60%) with the correctness of the key activation‑energy and exothermicity trends (weight 40%). Reporting numbers that are plausible but not obtained by the required workflow will not satisfy the hidden checks on trends and specific barrier thresholds.
