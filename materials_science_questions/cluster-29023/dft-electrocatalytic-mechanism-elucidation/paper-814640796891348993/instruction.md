# DFT Study of Water Adsorption and OER on Spinel Oxide (100) Surface

## Problem background
Electrocatalytic water splitting is a key technology for renewable hydrogen production, and the oxygen evolution reaction (OER) is often the efficiency-limiting half-reaction. Spinel Co3O4 is a promising OER catalyst, but its overpotential remains too high for practical applications. Anion doping—specifically substituting surface oxygen with fluorine—has been proposed as a strategy to enhance catalytic activity by altering adsorption energetics and reaction pathways on the surface. This task investigates the effect of fluorine doping on water adsorption modes (associative vs. dissociative) and on the OER theoretical overpotential at different cobalt sites on the Co3O4(100) surface using first‑principles density functional theory (DFT) with a Hubbard‑U correction.

## Approach
The computational approach is based on spin‑polarised DFT calculations with the PBE functional and a Hubbard‑U correction (Ueff = 3 eV) to describe the localised Co 3d states. The Co3O4(100) surface is modelled by a symmetric seven‑layer slab with a Co0.5 termination. Fluorine doping is introduced by substituting one three‑fold coordinated surface oxygen (O3c) with a fluorine atom, yielding a 12.5 % doping concentration.

Water adsorption energies are computed by placing a single H2O molecule on various surface cobalt sites and evaluating the total energies of the combined system, the clean slab, and the gas‑phase molecule. The oxygen evolution reaction is described by the four‑electron, four‑step mechanism (H2O → *OH → *O → *OOH → O2). The Gibbs free‑energy changes for each step are constructed using the computational standard hydrogen electrode (SHE) approach, with zero‑point energy and entropy corrections derived from vibrational frequencies of the adsorbates and gas‑phase molecules. The theoretical overpotential η is defined as the maximum free‑energy step divided by e minus the equilibrium potential (1.23 V). All DFT calculations are performed with the open‑source Quantum ESPRESSO package using appropriate pseudopotentials.

## Reproduction target
Using plane‑wave DFT with the PBE functional and a Hubbard‑U correction (Ueff = 3 eV), compute:

1. **Water adsorption energies** (ΔEads) and the **adsorption mode** (associative or dissociative) on the Co3O4(100) surface for the pure (undoped) Co2cT site, the fluorine‑doped Co2cT site, and the fluorine‑doped Co5cO site.

2. The **theoretical OER overpotential** (η) for the pure and fluorine‑doped surfaces at the Co2cT and Co5cO sites, using the four‑step mechanism and the computational standard hydrogen electrode approach (pH = 0, T = 298 K).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Co3O4 crystal structure

## Workflow steps

### Step 1: Bulk Co3O4 optimization
- Role: process
- Action: Optimize the bulk spinel Co3O4 crystal structure using DFT+U with U_eff=3 eV and the PBE functional. Verify consistency with experimental lattice constant and Co-O bond distances.
- Evidence: `/app/outputs/bulk_optimization.log`

### Step 2: Co3O4(100) slab construction
- Role: process
- Action: Build a symmetric seven-layer Co0.5-terminated (100) slab. Relax all atomic positions.
- Evidence: `/app/outputs/slab_relax.log`

### Step 3: Fluorine-doped slab
- Role: process
- Action: Substitute one three-fold surface oxygen (O3c) by a fluorine atom in the relaxed slab to create a 12.5% F-doped surface. Relax the slab again.
- Evidence: `/app/outputs/f_doped_slab.log`

### Step 4: Gas-phase reference energies
- Role: process
- Action: Compute total energies of an isolated H2O molecule and an isolated H2 molecule in a large simulation box using the same DFT settings.
- Evidence: `/app/outputs/gas_phase_energies.json`

### Step 5: Water adsorption calculations
- Role: scored
- Action: Place a water molecule on the pure Co2cT site, the F-doped Co2cT site, and the F-doped Co5cO site. Explore multiple initial geometries to find the most stable adsorption configuration for each. Compute the adsorption energy ΔE_ads = E(slab+H2O) − [E(slab) + E(H2O)], record the shortest Co–O bond distance, and determine the adsorption mode (dissociative or associative).
- Output file: `/app/outputs/step_05_adsorption_energies.json`
- Format: json
- Contract: [{"condition": "pure|F-doped", "site": "Co2cT|Co5cO", "adsorption_energy_eV": float, "bond_distance_A": float, "mode": "dissociative|associative"}]
- Scoring: scored by hidden verifier

### Step 6: OER intermediates
- Role: process
- Action: Place O*, OH*, and OOH* species on the four sites (pure Co2cT, pure Co5cO, F-doped Co2cT, F-doped Co5cO) and relax. Obtain total energies for each combination.
- Evidence: `/app/outputs/intermediate_binding_energies.json`

### Step 7: OER overpotential
- Role: scored (load-bearing)
- Action: From the binding energies of O*, OH*, OOH* and gas-phase references, construct the four-step OER free-energy diagram using the standard hydrogen electrode approach (pH=0, T=298 K). Include zero-point energy and entropy corrections. Compute the theoretical overpotential for each site/condition.
- Output file: `/app/outputs/step_07_overpotential.json`
- Format: json
- Contract: [{"condition": "pure|F-doped", "site": "Co2cT|Co5cO", "overpotential_V": float, "potential_determining_step": "string"}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_05_adsorption_energies.json`
- `/app/outputs/step_07_overpotential.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_05_adsorption_energies.json
- path: `/app/outputs/step_05_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Water adsorption energies, bond distances, and adsorption modes on pure and F-doped Co3O4(100) surfaces at Co2cT and Co5cO sites.
- schema:
  - `type`: array
  - `items`:
    - `condition`: string
    - `site`: string
    - `adsorption_energy_eV`: number
    - `bond_distance_A`: number
    - `mode`: string

### step_07_overpotential.json
- path: `/app/outputs/step_07_overpotential.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Theoretical OER overpotentials for pure and F-doped surfaces at Co2cT and Co5cO sites, together with the potential-determining step.
- schema:
  - `type`: array
  - `items`:
    - `condition`: string
    - `site`: string
    - `overpotential_V`: number
    - `potential_determining_step`: string

Notes: Bader charge analysis is excluded from scoring. The adsorption energies and overpotentials are compared to the paper's reported values with appropriate tolerances; the relative trend (F-doped overpotential lower) is also checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_05_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "condition": "string",
          "site": "string",
          "adsorption_energy_eV": "number",
          "bond_distance_A": "number",
          "mode": "string"
        }
      },
      "description": "Water adsorption energies, bond distances, and adsorption modes on pure and F-doped Co3O4(100) surfaces at Co2cT and Co5cO sites."
    },
    {
      "file": "step_07_overpotential.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "condition": "string",
          "site": "string",
          "overpotential_V": "number",
          "potential_determining_step": "string"
        }
      },
      "description": "Theoretical OER overpotentials for pure and F-doped surfaces at Co2cT and Co5cO sites, together with the potential-determining step."
    }
  ],
  "notes": "Bader charge analysis is excluded from scoring. The adsorption energies and overpotentials are compared to the paper's reported values with appropriate tolerances; the relative trend (F-doped overpotential lower) is also checked."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the output files you produce. For each scored artifact, the verifier compares your reported adsorption energies, adsorption modes, and overpotentials to a hidden reference within appropriate tolerances, and checks that the mode assignments are physically consistent. The final reward is a weighted combination of the scores for the adsorption energy file and the overpotential file. Simply reporting arbitrary numbers is not sufficient; the verifier expects values that could only result from a proper computational workflow. The relative trend between the pure and fluorine‑doped conditions carries the largest weight.
