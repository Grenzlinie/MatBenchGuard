# DFT Investigation of Boron-Promoted CO Hydrogenation Selectivity on Pd(211)

## Problem background
Methanol is a clean fuel that can be produced from syngas (CO+H2). Over palladium catalysts, the hydrogenation of CO can produce both methanol and methane, with methane being the thermodynamically favored byproduct and a major selectivity challenge. The presence of step sites on Pd surfaces is known to be important for bond-breaking reactions, including CO dissociation. Experiments have suggested that doping Pd with light elements like boron can alter catalytic performance. Subsurface boron atoms may modify the electronic structure of Pd, potentially changing the adsorption strength of key reaction intermediates and thereby shifting the selectivity between methanol and methane. This computational study investigates the energetics of CO hydrogenation on both a pristine Pd(211) surface and a boron-modified Pd(211) surface to understand how subsurface boron influences the adsorption and reaction barriers that govern product selectivity.

## Approach
The investigation uses density functional theory (DFT) calculations with plane-wave basis sets and the PBE exchange-correlation functional. Surface models are built as 12-layer 1×4 Pd(211) slabs. A boron-modified slab is constructed by placing boron atoms at subsurface octahedral sites, corresponding to a boron coverage of approximately 0.33 monolayers.

On both surfaces, the adsorption energies of CO, H, CH3OH, H2O, and CH2O are computed. Reaction pathways for methanol formation are evaluated through a sequence of hydrogenation steps: CO+H→CHO, CHO+H→CHOH, CHOH+H→CH2OH, and CH2OH+H→CH3OH. As the main competing path, the hydrogen-assisted C–O bond dissociation step COH→C+OH, which is the rate-determining step for methane formation, is also examined. Transition state searches provide activation energies and reaction energies for these elementary steps.

Finally, the effective barrier for each product is estimated using the two-step model, which takes the highest energy transition state along the preferred pathway relative to the lowest-energy adsorbed state. Comparing the effective barriers on the clean and boron-modified surfaces reveals whether subsurface boron can promote methanol formation over methane.

## Reproduction target
Your task is to produce three CSV files that capture the computed energetics:

1. Adsorption energies of CO, H, CH3OH, H2O, and CH2O on both Pd(211) and Pd(211)-B.
2. Activation energies and reaction energies for the elementary steps CO+H→CHO, CHO+H→CHOH, CHOH+H→CH2OH, CH2OH+H→CH3OH, and COH→C+OH on both surfaces.
3. Effective barriers for methanol and methane formation on each surface, derived from the computed adsorption energies and activation barriers using the two-step model.

Based on these computed quantities, you will determine which surface is selective for methanol formation and which is selective for methane formation. The numerical values you report will be compared against hidden reference data, and the derived selectivity conclusion must follow logically from your submitted effective barriers.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code) or equivalent: https://www.quantum-espresso.org
- Pd and B pseudopotentials (PBE functional): https://www.materialscloud.org/discover/sssp/table/efficiency
- pymatgen (Python Materials Genomics): pymatgen

## Workflow steps

### Step 1: Build Pd(211) and Pd(211)-B slab models
- Role: process
- Action: Construct a 12-layer 1×4 Pd(211) slab from bulk Pd. Create a Pd(211)-B slab by placing 4 boron atoms at subsurface octahedral sites (coverage ~0.33 ML). Perform full geometry relaxation of both slabs.
- Evidence: none

### Step 2: Calculate adsorption energies of key species
- Role: scored
- Action: For each of CO, H, CH3OH, H2O, and CH2O, find the most stable adsorption site on Pd(211) and Pd(211)-B and compute the adsorption energy E_ad = E_total - E_slab - E_gas. Write one row per species per surface.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: surface (string, 'Pd(211)' or 'Pd(211)-B'), species (string, one of CO, H, CH3OH, H2O, CH2O), adsorption_energy_eV (float, eV)
- Scoring: scored by hidden verifier

### Step 3: Calculate reaction barriers for methanol and methane pathways
- Role: scored
- Action: Locate transition states and compute activation energies (Ea) and reaction energies (ΔE) for the elementary steps: CO+H→CHO, CHO+H→CHOH, CHOH+H→CH2OH, CH2OH+H→CH3OH (methanol preferred path) and COH→C+OH (methane rate-determining step). Perform on both Pd(211) and Pd(211)-B. Write one row per reaction per surface.
- Output file: `/app/outputs/reaction_barriers.csv`
- Format: csv
- Contract: surface (string), reaction_step (string describing the reaction, e.g. 'CO+H→CHO'), activation_energy_eV (float, eV), reaction_energy_eV (float, eV)
- Scoring: scored by hidden verifier

### Step 4: Estimate effective barriers and determine selectivity
- Role: scored (load-bearing)
- Action: Using the two-step model, estimate the effective barrier for methanol formation (energy difference between the highest transition state along the preferred path and the lowest adsorption state) and for methane formation (using the COH dissociation step as rate-determining and subsequent hydrogenations) on both surfaces. Report the effective barriers, then deduce which surface is selective for methanol.
- Output file: `/app/outputs/effective_barriers.csv`
- Format: csv
- Contract: surface (string), product (string, 'methanol' or 'methane'), effective_barrier_eV (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/reaction_barriers.csv`
- `/app/outputs/effective_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies of CO, H, CH3OH, H2O, CH2O on Pd(211) and Pd(211)-B. Checker compares values to hidden reference within tolerance and verifies weakening trend.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `species`, `adsorption_energy_eV`
  - `units`:
    - `adsorption_energy_eV`: eV

### reaction_barriers.csv
- path: `/app/outputs/reaction_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Activation energies and reaction energies for the specified elementary steps on both surfaces. Checker compares values to hidden reference within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `reaction_step`, `activation_energy_eV`, `reaction_energy_eV`
  - `units`:
    - `activation_energy_eV`: eV
    - `reaction_energy_eV`: eV

### effective_barriers.csv
- path: `/app/outputs/effective_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective barriers for methanol and methane formation on each surface, derived from the two-step model. Checker compares values to hidden reference and checks selectivity trends.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `product`, `effective_barrier_eV`
  - `units`:
    - `effective_barrier_eV`: eV

Notes: All energies are in eV. The checker also verifies that adsorption energies on Pd(211)-B are higher (less negative) than on Pd(211) for each species. The checker verifies the consistency of effective barriers and the selectivity conclusion with the reference data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "species",
          "adsorption_energy_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "Adsorption energies of CO, H, CH3OH, H2O, CH2O on Pd(211) and Pd(211)-B. Checker compares values to hidden reference within tolerance and verifies weakening trend."
    },
    {
      "file": "reaction_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "reaction_step",
          "activation_energy_eV",
          "reaction_energy_eV"
        ],
        "units": {
          "activation_energy_eV": "eV",
          "reaction_energy_eV": "eV"
        }
      },
      "description": "Activation energies and reaction energies for the specified elementary steps on both surfaces. Checker compares values to hidden reference within tolerance."
    },
    {
      "file": "effective_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "product",
          "effective_barrier_eV"
        ],
        "units": {
          "effective_barrier_eV": "eV"
        }
      },
      "description": "Effective barriers for methanol and methane formation on each surface, derived from the two-step model. Checker compares values to hidden reference and checks selectivity trends."
    }
  ],
  "notes": "All energies are in eV. The checker also verifies that adsorption energies on Pd(211)-B are higher (less negative) than on Pd(211) for each species. The checker verifies the consistency of effective barriers and the selectivity conclusion with the reference data."
}
```

## How you are scored
A hidden automated checker evaluates your submitted artifacts. For each scored output file, the checker compares your reported energies to hidden reference standards using tolerances that account for differences between DFT implementations. The checker also verifies that the adsorption energies on Pd(211)-B are weaker (less negative) than on Pd(211) for every species. The checker verifies that your derived effective barriers and your conclusion about which surface selects for methanol are consistent with the paper's findings. The final reward is monotonic: your score increases as your computed values approach the reference, and as you correctly reproduce the weakening trend and the selectivity pattern.
