# Hydrogen vacancy formation and migration in ceria interfaces

## Problem background
Solid-state hydrogen storage materials such as MgH2 offer high gravimetric capacity but suffer from slow desorption kinetics, driving the search for effective catalysts. One promising strategy uses symbiotic cerium hydride/oxide phases (CeH2.73/CeO2) to enhance dehydrogenation. A key mechanistic question is whether the interface between the hydride and oxide can spontaneously release hydrogen and whether the oxide provides a facile transport path. Computational investigations can shed light on this by quantifying (i) the energy cost to create hydrogen vacancies in the bulk CeH2.75 and at the CeH2.75/CeO2 interface, and (ii) the energy barriers for hydrogen migration through pure CeO2. This task uses density functional theory to compute those quantities and thereby evaluate the plausibility of an interfacial “hydrogen pump” effect.

## Approach
The work follows a three-stage first-principles protocol entirely within an open-source DFT framework (e.g., Quantum ESPRESSO), using the PBE+U functional, PAW pseudopotentials, and a Hubbard U correction on Ce f-states.

1. **Bulk relaxations:** Optimize the lattice constants and atomic positions of fluorite CeO2 and the closely related fluorite-based CeH2.75 structure (tetrahedral and octahedral hydrogen sites) to obtain equilibrium cells.

2. **Interface construction:** Build a (2×2) coherent CeH2.75(111)/CeO2(111) supercell with O-Ce-H termination, using the relaxed bulk lattice constants. Allow the atomic coordinates to relax while keeping the cell fixed to identify the lowest-energy interfacial arrangement.

3. **Defect energetics and migration barriers:**
   - Using the relaxed bulk and interface supercells, calculate the formation energies of single and double hydrogen vacancies at several distinct sites, comparing the interface region with bulk CeH2.75.
   - In a separate pure CeO2 (2×2×1) supercell, use the climbing-image nudged elastic band (CI-NEB) method to determine the minimum-energy paths and barriers for hydrogen migration between nearest-neighbor hydroxyl sites.

The computed formation energies and migration barriers are collected into a structured JSON file for verification.

## Reproduction target
Produce a JSON file (`dft_results.json`) that contains the following quantities, all in units of eV:
- `interface_single_vacancy_formation_energy`
- `interface_double_vacancy_formation_energy`
- `bulk_single_vacancy_formation_energy`
- `bulk_double_vacancy_formation_energy`
- `migration_barriers_CeO2` (a list of barrier heights for the examined migration hops)

The verification will compare the computed values against hidden reference data derived from the original study. The assessment focuses on whether the interface vacancy formation energies are lower (more favorable) than the corresponding bulk values, and whether the migration barriers in CeO2 are indicative of facile hydrogen transport.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- PAW pseudopotentials for Ce, O, H: https://www.materialscloud.org/discover/sssp
- Initial crystal structures of CeO2 and CeH2.75: https://materialsproject.org/materials/mp-20194

## Workflow steps

### Step 1: Bulk DFT geometry optimization
- Role: process
- Action: Perform DFT+U geometry optimization of bulk CeO2 (fluorite) and CeH2.75 (fluorite-based with tetrahedral and octahedral hydrogen) to obtain equilibrium lattice constants and total energies. Use an open-source DFT code (e.g., Quantum ESPRESSO), PBE+U functional with U_eff on Ce f-states, and appropriate pseudopotentials. Fully relax cell parameters and atomic positions.
- Evidence: `/app/outputs/bulk_relax.log`

### Step 2: Interface model construction and relaxation
- Role: process
- Action: Build a (2×2) coherent CeH2.75(111)/CeO2(111) interface supercell with O-Ce-H termination, using the optimized bulk lattice constants. Relax atomic positions while keeping the cell fixed, and verify the lowest-energy interface configuration.
- Evidence: `/app/outputs/interface_relax.log`

### Step 3: Compute vacancy formation energies and migration barriers
- Role: scored (load-bearing)
- Action: Using the relaxed interface and bulk supercells, compute the formation energies of single and double hydrogen vacancies at different sites in the CeH2.75/CeO2 interface and in bulk CeH2.75. Also compute CI-NEB energy barriers for hydrogen migration between nearest-neighbor hydroxyl sites in pure CeO2. Collect all values in a structured JSON file.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"interface_single_vacancy_formation_energy": "float (eV)", "interface_double_vacancy_formation_energy": "float (eV)", "bulk_single_vacancy_formation_energy": "float (eV)", "bulk_double_vacancy_formation_energy": "float (eV)", "migration_barriers_CeO2": "[float, ...] (eV)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: JSON file containing the computed hydrogen vacancy formation energies at the CeH2.75/CeO2 interface and in bulk CeH2.75, and the hydrogen migration energy barriers in pure CeO2. The checker verifies that at least one interface formation energy is negative and lower than the corresponding bulk value, and that all migration barriers are ≤0.2 eV.
- schema:
  - `type`: object
  - `required`: `interface_single_vacancy_formation_energy`, `interface_double_vacancy_formation_energy`, `bulk_single_vacancy_formation_energy`, `bulk_double_vacancy_formation_energy`, `migration_barriers_CeO2`
  - `properties`:
    - `interface_single_vacancy_formation_energy`:
      - `type`: number
      - `unit`: eV
    - `interface_double_vacancy_formation_energy`:
      - `type`: number
      - `unit`: eV
    - `bulk_single_vacancy_formation_energy`:
      - `type`: number
      - `unit`: eV
    - `bulk_double_vacancy_formation_energy`:
      - `type`: number
      - `unit`: eV
    - `migration_barriers_CeO2`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: eV

Notes: The reproduction target is to demonstrate the spontaneous hydrogen release effect (negative vacancy formation energy at the interface) and nearly barrierless hydrogen migration in CeO2. The hidden checker performs a T0 result-level comparison, scoring formation energies by threshold_or_better (negative and lower than bulk) and migration barriers by threshold_or_better (≤0.2 eV). Tolerances account for differences in DFT code and pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "interface_single_vacancy_formation_energy",
          "interface_double_vacancy_formation_energy",
          "bulk_single_vacancy_formation_energy",
          "bulk_double_vacancy_formation_energy",
          "migration_barriers_CeO2"
        ],
        "properties": {
          "interface_single_vacancy_formation_energy": {
            "type": "number",
            "unit": "eV"
          },
          "interface_double_vacancy_formation_energy": {
            "type": "number",
            "unit": "eV"
          },
          "bulk_single_vacancy_formation_energy": {
            "type": "number",
            "unit": "eV"
          },
          "bulk_double_vacancy_formation_energy": {
            "type": "number",
            "unit": "eV"
          },
          "migration_barriers_CeO2": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "eV"
            }
          }
        }
      },
      "description": "JSON file containing the computed hydrogen vacancy formation energies at the CeH2.75/CeO2 interface and in bulk CeH2.75, and the hydrogen migration energy barriers in pure CeO2. The checker verifies that at least one interface formation energy is negative and lower than the corresponding bulk value, and that all migration barriers are ≤0.2 eV."
    }
  ],
  "notes": "The reproduction target is to demonstrate the spontaneous hydrogen release effect (negative vacancy formation energy at the interface) and nearly barrierless hydrogen migration in CeO2. The hidden checker performs a T0 result-level comparison, scoring formation energies by threshold_or_better (negative and lower than bulk) and migration barriers by threshold_or_better (≤0.2 eV). Tolerances account for differences in DFT code and pseudopotentials."
}
```

## How you are scored
A hidden verifier reads your `dft_results.json` and compares each extracted numeric value to reference quantities (the corresponding paper-reported numbers or derived thresholds). Scoring is performed with a **threshold_or_better** policy: full credit is earned when your computed values meet or exceed the reference performance, and credit degrades only if the result is worse. Specifically:
- For the formation energies, the verifier checks whether at least one interface vacancy formation energy is lower than the corresponding bulk formation energy, and whether the interface energies indicate a thermodynamic driving force for vacancy formation.
- For the migration barriers, all reported barriers are compared against a low cutoff derived from the original work, and credit is awarded based on how many barriers are below that cutoff.

The final reward aggregates these checks with weights concentrated on the main defect-energy and barrier comparisons. Reporting plausible numbers without completing the DFT workflow will not pass the verifier; the computed results must stem from the described three-stage pipeline.
