# DFT Investigation of ORR on FeN3-Graphene: Reproduce Adsorption Energies, Barriers, and Free Energy Diagram

## Problem background
Developing non-precious metal catalysts for the oxygen reduction reaction (ORR) is critical for fuel cell commercialization. Fe/N/C catalysts with FeNx active centres have shown promise, but the optimal structure and detailed mechanism remain debated. Knowing which Fe coordination number drives efficient four-electron ORR is essential for rational design. This task investigates a three-coordinated FeN3 centre embedded in a graphene layer (FeN3-G) by computing the detailed thermodynamics and kinetics of the ORR on this model catalyst. The goal is to determine whether this specific active site can catalyse the full reduction of O2 to water through a complete free-energy assessment and barrier analysis.

## Approach
The system is modelled with periodic DFT using the GGA-PBE functional. A 5x5 graphene supercell is constructed, one C replaced by Fe, and the three nearest-neighbour C atoms replaced by N, forming the FeN3-G slab. A vacuum layer of at least 15 Å is added in the z-direction to avoid spurious interactions. Adsorption energies of the five key ORR intermediates (O2, OOH, O, OH, H2O) are obtained from relaxed total energies of the bare slab, the isolated species, and the adsorbed systems. Transition states for the seven elementary steps (O2 dissociation, O2 hydrogenation to OOH, OOH hydrogenation to O+H2O/2OH and direct dissociation to O+OH, O hydrogenation to OH, and OH hydrogenation to H2O) are located and activation barriers computed. Vibrational frequency calculations provide zero-point energies and entropies at 300 K. Finally, free-energy diagrams are constructed at U = 0 V, pH = 0, T = 300 K using the computational hydrogen electrode (CHE) model, referencing ½H2(g) as the proton-electron pair, H2O at 0.035 bar equilibrium, and O2 referenced through the O2 + 2H2 → 2H2O reaction (ΔG = −4.92 eV).

## Reproduction target
Compute the adsorption energies (Eads in eV) of O2, OOH, O, OH, and H2O on the Fe site of FeN3-G. Compute the activation barriers (Ea in eV) for the seven elementary steps listed above. Compute the Gibbs free energy changes (ΔG in eV) for the four reduction steps: O2(ads) → OOH(ads), OOH(ads) → O(ads) + H2O(l), O(ads) → OH(ads), and OH(ads) → H2O(l), all at zero external potential. Results must be saved as three CSV files: `step_01_adsorption_energies.csv` (columns: species, Eads_ev), `step_02_activation_barriers.csv` (columns: reaction, Ea_ev), and `step_03_free_energy_diagram.csv` (columns: step, dG_ev), placed under `/app/outputs`.

## Assets

- Open-source periodic DFT code with GGA-PBE (e.g., Quantum ESPRESSO, CP2K): Quantum ESPRESSO, CP2K (or equivalent)
- GGA-PBE pseudopotentials (e.g., from SSSP library or analogous): Standard pseudopotential libraries (e.g., SSSP, PseudoDojo, DCACP)

## Workflow steps

### Step 1: Construct FeN3-G supercell model
- Role: process
- Action: Build the initial periodic structure: a 5x5 graphene supercell, substitute one C with Fe, and substitute the three nearest-neighbour C atoms with N. Add a vacuum slab of at least 15 Å in the z-direction.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: DFT geometry optimization of clean FeN3-G
- Role: process
- Action: Perform full geometry relaxation of the FeN3-G slab using DFT with GGA-PBE, with an appropriate k-point mesh and basis/pseudopotential set. Converge forces to a tight threshold.
- Evidence: `/app/outputs/clean_slab_energy.txt`

### Step 3: DFT optimization of isolated ORR species
- Role: process
- Action: Optimize the geometries of gas-phase O2, OOH, O, OH, H2O2, and H2O in a large vacuum box using the same DFT settings as the slab. Compute the total energy of each isolated molecule.
- Evidence: `/app/outputs/isolated_energies.json`

### Step 4: Compute adsorption energies of ORR intermediates
- Role: scored
- Action: For each intermediate (O2, OOH, O, OH, H2O), construct the adsorbed system on the Fe site of the clean slab, relax the geometry, compute the total energy, and calculate Eads = E(total) − E(slab) − E(isolated). Report the results in a CSV.
- Output file: `/app/outputs/step_01_adsorption_energies.csv`
- Format: csv
- Contract: species (string), Eads_ev (float, eV)
- Scoring: scored by hidden verifier

### Step 5: Transition state searches and activation barriers
- Role: scored
- Action: For each elementary step: O2 dissociation, O2 hydrogenation to OOH, OOH hydrogenation to O+H2O, OOH hydrogenation to 2OH, OOH direct dissociation to O+OH, O hydrogenation to OH, and OH hydrogenation to H2O, locate the transition state and compute the activation energy Ea = E(TS) − E(initial state). Output a CSV with the reaction name and Ea (eV).
- Output file: `/app/outputs/step_02_activation_barriers.csv`
- Format: csv
- Contract: reaction (string), Ea_ev (float, eV)
- Scoring: scored by hidden verifier

### Step 6: Vibrational frequency analysis for free energy corrections
- Role: process
- Action: Perform harmonic vibrational frequency calculations for each adsorbed species (and gas-phase reference molecules) to obtain zero-point energies (ZPE) and entropies at 300 K, using the same DFT settings.
- Evidence: `/app/outputs/freq_data.json`

### Step 7: Free energy diagram via CHE model
- Role: scored (load-bearing)
- Action: Combine the DFT total energies, ZPE and entropy corrections, and standard CHE references (½H2(g) as H+ + e−, H2O gas at 0.035 bar, O2 from O2 + 2H2 → 2H2O with ΔG = −4.92 eV). Compute the Gibbs free energy change ΔG for each reduction step at U = 0 V, pH = 0, T = 300 K: 1. O2(ads) + H+ + e− → OOH(ads), 2. OOH(ads) + H+ + e− → O(ads) + H2O(l), 3. O(ads) + H+ + e− → OH(ads), 4. OH(ads) + H+ + e− → H2O(l). Output a CSV with step label and ΔG (eV).
- Output file: `/app/outputs/step_03_free_energy_diagram.csv`
- Format: csv
- Contract: step (string), dG_ev (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_adsorption_energies.csv`
- `/app/outputs/step_02_activation_barriers.csv`
- `/app/outputs/step_03_free_energy_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_adsorption_energies.csv
- path: `/app/outputs/step_01_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies of O2, OOH, O, OH, H2O on FeN3-G. The CSV must contain a header row and exactly 5 data rows.
- schema:
  - `type`: table
  - `required_columns`: `species`, `Eads_ev`
  - `units`:
    - `Eads_ev`: eV

### step_02_activation_barriers.csv
- path: `/app/outputs/step_02_activation_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Activation barriers for seven elementary ORR steps. The CSV must contain a header row and at least 7 rows covering O2_dissoc, O2_to_OOH, OOH_to_O_H2O, OOH_to_2OH, OOH_to_O_OH, O_to_OH, OH_to_H2O.
- schema:
  - `type`: table
  - `required_columns`: `reaction`, `Ea_ev`
  - `units`:
    - `Ea_ev`: eV

### step_03_free_energy_diagram.csv
- path: `/app/outputs/step_03_free_energy_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Gibbs free energy changes for the four reduction steps at U=0 V, pH=0, T=300 K. The CSV must contain a header row and exactly 4 data rows corresponding to the steps O2->OOH, OOH->O+H2O, O->OH, OH->H2O.
- schema:
  - `type`: table
  - `required_columns`: `step`, `dG_ev`
  - `units`:
    - `dG_ev`: eV

Notes: All energies are in eV. The reference comparison is to the paper's reported values (e.g., Table I and text) with method-dependent tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "Eads_ev"
        ],
        "units": {
          "Eads_ev": "eV"
        }
      },
      "description": "Adsorption energies of O2, OOH, O, OH, H2O on FeN3-G. The CSV must contain a header row and exactly 5 data rows."
    },
    {
      "file": "step_02_activation_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction",
          "Ea_ev"
        ],
        "units": {
          "Ea_ev": "eV"
        }
      },
      "description": "Activation barriers for seven elementary ORR steps. The CSV must contain a header row and at least 7 rows covering O2_dissoc, O2_to_OOH, OOH_to_O_H2O, OOH_to_2OH, OOH_to_O_OH, O_to_OH, OH_to_H2O."
    },
    {
      "file": "step_03_free_energy_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "dG_ev"
        ],
        "units": {
          "dG_ev": "eV"
        }
      },
      "description": "Gibbs free energy changes for the four reduction steps at U=0 V, pH=0, T=300 K. The CSV must contain a header row and exactly 4 data rows corresponding to the steps O2->OOH, OOH->O+H2O, O->OH, OH->H2O."
    }
  ],
  "notes": "All energies are in eV. The reference comparison is to the paper's reported values (e.g., Table I and text) with method-dependent tolerances."
}
```

## How you are scored
Your submission is scored by a hidden verifier that inspects the three output CSV files. Each file is compared against reference values derived from the computational study: adsorption energies, activation barriers, and free-energy steps are evaluated separately. The verifier checks that the computed numbers follow the expected physical trends and are within method-appropriate tolerances, with the free-energy diagram carrying the highest weight. You do not need to match any pre-announced target; simply run the protocol faithfully and report your results. The final reward is a weighted sum of the per-artifact scores.
