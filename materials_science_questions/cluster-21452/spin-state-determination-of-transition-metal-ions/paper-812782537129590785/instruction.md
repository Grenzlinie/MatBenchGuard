# CASPT2 Binding Energies and Spin State Assignment for Co–Ammonia Cation Complexes

## Problem background
The reaction of Co⁺ with ammonia produces several products: CoNH₃⁺, HCoNH₂⁺, CoNH₂⁺ + H, and CoH⁺ + NH₂. The branching ratios depend on the relative stability of the intermediates. In particular, the ground spin state and the accurate binding energy of the CoNH₂⁺ product are critical for understanding the reaction mechanism and the absence of H₂ elimination. This work uses multireference ab initio methods to compute these binding energies and to assign the ground state of CoNH₂⁺. Your task is to reproduce these computational results: calculate the zero-point corrected dissociation energies (D₀) for CoNH₃⁺, CoNH₂⁺ (in both quartet and doublet spin states), and CoH⁺, and determine which spin state of CoNH₂⁺ is more stable.

## Approach
Use the CASPT2 multireference technique with CASSCF reference functions to calculate electronic energies. Perform geometry optimizations for the relevant species at the CASSCF level with a minimal active space (AS1) that includes the metal 3d, 4s, and key ligand orbitals. Then carry out single-point CASPT2 energy calculations with a larger active space (AS2) that includes double-shell 3d′ orbitals to capture relaxation effects. Apply zero-point vibrational corrections, basis set superposition error (BSSE) corrections using the counterpoise method, and relativistic mass‑velocity/Darwin corrections. Assemble the final D₀ binding energies for the complexes and compute the energy difference between the quartet and doublet states of CoNH₂⁺ to assign the ground spin state. All calculations use ANO‑RCC basis sets.

## Reproduction target
Produce a JSON file `binding_energies.json` containing the D₀ binding energies (in kcal/mol) for CoNH₃⁺, CoNH₂⁺ (quartet and doublet), and CoH⁺, plus the spin gap of CoNH₂⁺ (defined as quartet D₀ minus doublet D₀). Based on the computed spin gap, determine which spin state of CoNH₂⁺ is the ground state.

## Assets

- ORCA quantum chemistry package (or equivalent CASPT2‑capable software): https://orcaforum.kofo.mpg.de/
- ANO‑RCC basis sets for Co, N, H: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Geometry optimization of reactants, products, and fragments
- Role: process
- Action: Perform CASSCF geometry optimizations for CoNH₃⁺, CoNH₂⁺ (doublet and quartet), CoH⁺, and the Co⁺ atom; perform MP2 geometry optimizations for NH₃, NH₂, and H₂ fragments. Use ANO‑type basis sets and active spaces that include the metal 3d, 4s, and key ligand orbitals, consistent with a minimal active space (AS1) description.
- Evidence: `/app/outputs/step_1_geom_opt.log`

### Step 2: CASPT2/AS2 single‑point energy calculations
- Role: process
- Action: Perform CASPT2 single‑point calculations on all optimized geometries using a larger active space (AS2) that includes the double‑shell 3d′ orbitals. Obtain raw total electronic energies for all species (complexes, fragments, and Co⁺ atom).
- Evidence: `/app/outputs/step_2_caspt2_energies.log`

### Step 3: Calculate zero‑point vibrational energy corrections
- Role: process
- Action: Compute numerical harmonic vibrational frequencies for all stationary points to obtain ZPE corrections.
- Evidence: `/app/outputs/step_3_zpe.log`

### Step 4: Evaluate BSSE and relativistic corrections
- Role: process
- Action: Estimate basis set superposition error using the counterpoise method and compute mass‑velocity/Darwin relativistic corrections for the binding energies.
- Evidence: `/app/outputs/step_4_corrections.log`

### Step 5: Assemble final binding energies and spin gap
- Role: scored (load-bearing)
- Action: Combine the CASPT2/AS2 energies with ZPE, BSSE, and relativistic corrections to obtain D₀ binding energies. Write a JSON file containing the D₀ values for CoNH₃⁺, CoNH₂⁺ (quartet and doublet), CoH⁺, and the spin gap (quartet D₀ minus doublet D₀).
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: {'CoNH3_D0': <number>, 'CoNH2_quartet_D0': <number>, 'CoNH2_doublet_D0': <number>, 'CoH_D0': <number>, 'CoNH2_spin_gap': <number>} (all in kcal/mol; spin_gap = quartet_D0 - doublet_D0, expected to be negative if quartet is lower)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zero‑point corrected binding energies D₀ (kcal/mol) for CoNH₃⁺, CoNH₂⁺ (quartet and doublet), CoH⁺, and the energy difference between the quartet and doublet states of CoNH₂⁺ (spin gap = quartet_D0 minus doublet_D0). The hidden checker compares each quantity against hidden paper‑reported reference values using appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `CoNH3_D0`: number
    - `CoNH2_quartet_D0`: number
    - `CoNH2_doublet_D0`: number
    - `CoH_D0`: number
    - `CoNH2_spin_gap`: number
  - `units`:
    - `CoNH3_D0`: kcal/mol
    - `CoNH2_quartet_D0`: kcal/mol
    - `CoNH2_doublet_D0`: kcal/mol
    - `CoH_D0`: kcal/mol
    - `CoNH2_spin_gap`: kcal/mol

Notes: The hidden checker validates that each reported D₀ is close to the paper's gold value within a tolerance that accounts for methodological differences; the spin gap must be negative with a sufficient magnitude to establish the quartet ground state.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "CoNH3_D0": "number",
          "CoNH2_quartet_D0": "number",
          "CoNH2_doublet_D0": "number",
          "CoH_D0": "number",
          "CoNH2_spin_gap": "number"
        },
        "units": {
          "CoNH3_D0": "kcal/mol",
          "CoNH2_quartet_D0": "kcal/mol",
          "CoNH2_doublet_D0": "kcal/mol",
          "CoH_D0": "kcal/mol",
          "CoNH2_spin_gap": "kcal/mol"
        }
      },
      "description": "Zero‑point corrected binding energies D₀ (kcal/mol) for CoNH₃⁺, CoNH₂⁺ (quartet and doublet), CoH⁺, and the energy difference between the quartet and doublet states of CoNH₂⁺ (spin gap = quartet_D0 minus doublet_D0). The hidden checker compares each quantity against hidden paper‑reported reference values using appropriate tolerances."
    }
  ],
  "notes": "The hidden checker validates that each reported D₀ is close to the paper's gold value within a tolerance that accounts for methodological differences; the spin gap must be negative with a sufficient magnitude to establish the quartet ground state."
}
```

## How you are scored
A hidden verifier will read your `binding_energies.json` and compare each reported D₀ value to a hidden reference based on the original paper's results. For each binding energy, you receive credit proportional to how close your value is to the reference, within a tolerance. For the spin gap, the sign must match the true ground‑state assignment (i.e., the sign that indicates which spin state is more stable). The final score is a weighted combination of all components. Note that simply copying the paper's numbers is insufficient; you must execute the computational workflow to produce these results.
