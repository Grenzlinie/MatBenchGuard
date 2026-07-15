# DFT Defect Formation and NEB Migration Barrier Analysis for Lithium Amide Decomposition Activation Energies

## Problem background
Lithium amide (LiNH2) is a promising candidate for solid-state hydrogen storage, but the atomic-scale mechanisms controlling its decomposition into lithium imide (Li2NH) and ammonia (NH3) are not fully established. First-principles density functional theory (DFT) combined with nudged elastic band (NEB) calculations can probe the role of native point defects in this process. The goal of this task is to compute two proposed activation energies that correspond to distinct defect-mediated decomposition mechanisms, thereby providing a quantitative foundation for understanding the rate-limiting steps.

## Approach
We use an open-source DFT code (e.g., Quantum ESPRESSO) with standard solid-state pseudopotentials to model the LiNH2 and Li2NH crystal structures. The workflow begins with bulk geometry relaxations to obtain formation enthalpies, from which atomic chemical potentials are derived under hydrogen-desorption conditions (corresponding to equilibrium between LiNH2 and Li2NH). Using a supercell of LiNH2, we compute the formation energies of the key hydrogen defects — the positively charged hydrogen interstitial (H_i^+), the negatively charged hydrogen vacancy (V_H^-), and the (H_i^+, V_H^-) Frenkel pair — and determine the energy cost to separate the bound pair. NEB calculations then yield the migration barriers of H_i^+ and V_H^-. These quantities are combined to obtain two activation energies: Mechanism 1 (bulk Frenkel mechanism) = formation energy of H_i^+ + separation cost + migration barrier of H_i^+; Mechanism 2 (surface-mediated mechanism) = formation energy of V_H^- + migration barrier of V_H^-. The final output contains both energies.

## Reproduction target
Compute the two activation energies for LiNH2 decomposition and write them as a JSON object with keys Ea_mech1 and Ea_mech2 (both in eV) to `/app/outputs/activation_energies.json`. Your reproduction will be evaluated against a hidden reference; in addition, a required structural relationship between Ea_mech1 and Ea_mech2 will be verified.

## Assets

- Quantum ESPRESSO (open-source DFT package) or alternative (e.g., CP2K): https://www.quantum-espresso.org/
- Standard solid-state pseudopotentials (e.g., SSSP precision library): https://www.materialscloud.org/discover/sssp
- Crystal structures of LiNH2 (tetragonal I-4) and Li2NH (orthorhombic Pbca)

## Workflow steps

### Step 1: Bulk DFT and chemical potential derivation
- Role: process
- Action: Perform DFT geometry relaxation for LiNH2 (tetragonal I-4) and Li2NH (orthorhombic Pbca) to obtain formation enthalpies. Derive atomic chemical potentials for hydrogen desorption conditions (μ_H = -0.49 eV) using the formation enthalpies and equilibrium between LiNH2 and Li2NH.
- Evidence: `/app/outputs/bulk_results.json`

### Step 2: Hydrogen defect formation energies
- Role: process
- Action: Using the derived chemical potentials and a supercell of LiNH2, compute formation energies of hydrogen interstitial (H_i^+), hydrogen vacancy (V_H^-), and the (H_i^+,V_H^-) Frenkel pair. Determine the equilibrium Fermi level from charge neutrality between Li_i^+ and V_Li^-.
- Evidence: `/app/outputs/defect_formation_energies.json`

### Step 3: NEB migration barrier calculations
- Role: process
- Action: Compute migration barriers of H_i^+ and V_H^- in LiNH2 using the climbing-image nudged elastic band (NEB) method on the same supercell.
- Evidence: `/app/outputs/migration_barriers.json`

### Step 4: Activation energy analysis
- Role: scored (load-bearing)
- Action: From the formation energies and migration barriers, compute the separation cost (energy to separate H_i^+ and V_H^- in the Frenkel pair). Compute Ea_mech1 = E_f(H_i^+) + separation_cost + E_m(H_i^+), and Ea_mech2 = E_f(V_H^-) + E_m(V_H^-). Write the two activation energies to activation_energies.json.
- Output file: `/app/outputs/activation_energies.json`
- Format: json
- Contract: {"Ea_mech1": float, "Ea_mech2": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.json
- path: `/app/outputs/activation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Activation energies (in eV) for the two LiNH2 decomposition mechanisms: bulk Frenkel mechanism (Ea_mech1) and surface-mediated mechanism (Ea_mech2).
- schema:
  - `type`: object
  - `required`:
    - `Ea_mech1`: number
    - `Ea_mech2`: number
  - `items`: object
  - `units`:
    - `Ea_mech1`: eV
    - `Ea_mech2`: eV

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
          "Ea_mech1": "number",
          "Ea_mech2": "number"
        },
        "items": {},
        "units": {
          "Ea_mech1": "eV",
          "Ea_mech2": "eV"
        }
      },
      "description": "Activation energies (in eV) for the two LiNH2 decomposition mechanisms: bulk Frenkel mechanism (Ea_mech1) and surface-mediated mechanism (Ea_mech2)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads only the files you write under `/app/outputs`. The primary scored artifact is `activation_energies.json`. The verifier checks that the reported activation energies are numerically accurate (within a tolerance that accounts for the spread expected from different DFT implementations) and that a necessary relationship between Ea_mech1 and Ea_mech2 holds. The intermediate process artifacts (bulk_results.json, defect_formation_energies.json, migration_barriers.json) may also be inspected to confirm that the underlying calculations were performed, but the bulk of the reward is determined by the final activation energies. No paper-reported values are provided; your results will be compared to a hidden standard.
