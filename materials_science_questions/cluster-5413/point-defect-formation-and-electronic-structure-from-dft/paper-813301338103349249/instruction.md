# Pd surface segregation and oxygen vacancy energetics in LaFeO3: DFT study

## Problem background
Palladium-containing perovskite oxides such as LaFe1-xPdxO3 are used as intelligent automotive catalysts because palladium can reversibly segregate to the surface as metallic nanoparticles under reducing conditions and dissolve back into the oxide lattice under oxidizing conditions, suppressing particle growth. The segregation behavior is expected to depend on the surface termination (LaO vs. FeO2) and on the presence of oxygen vacancies near the surface. Understanding the relative segregation tendency of Pd at these two terminations, and how oxygen vacancies modify it, is essential for rational catalyst design.

## Approach
The task uses spin-polarized density functional theory (DFT) calculations with the PBE exchange-correlation functional, as implemented in Quantum ESPRESSO. Ultrasoft pseudopotentials from the SSSP Efficiency library describe the ion-electron interaction. The LaFeO3 crystal is modeled in the orthorhombic GdFeO3-type structure with G-type antiferromagnetic order. Slab models are constructed for both LaO- and FeO2-terminated (001) surfaces, each containing five FeO2 layers and ~11 Å of vacuum; the bottom two layers are fixed. A single Fe atom is replaced by Pd at the 1st and 3rd FeO2 layers below the surface. The solution energy of Pd is defined as the total energy difference between the Pd-substituted slab and the pristine slab, corrected by bulk Fe and Pd reference energies. The relative segregation energy is the difference in solution energy between the surface (1st layer) and the bulk-like (3rd layer) positions. Oxygen vacancies are introduced by removing one oxygen atom; all nonequivalent oxygen sites are tested to find the most stable vacancy. The vacancy formation energy is calculated relative to half the energy of an isolated O2 molecule. The workflow produces two scored CSV files: one with relative segregation energies for the four Pd/surface configurations (LaO/FeO2, with/without vacancy), and one with the most stable oxygen vacancy formation energy for each termination when Pd sits at the surface.

## Reproduction target
Compute and report:

1. The relative segregation energy (solution energy at the 1st FeO2 layer minus solution energy at the 3rd FeO2 layer) for Pd in LaFeO3(001) slabs, for the following four cases:
   - LaO termination, no oxygen vacancy
   - LaO termination, with an oxygen vacancy at its most stable site
   - FeO2 termination, no oxygen vacancy
   - FeO2 termination, with an oxygen vacancy at its most stable site

2. The formation energy of the most stable oxygen vacancy near the Pd atom located at the surface (1st FeO2 layer) for the LaO-terminated slab and for the FeO2-terminated slab.

All energies are reported in eV. The results are written to the output files `step_03_segregation_energies.csv` and `step_04_vo_formation_energies.csv` as specified in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency pseudopotentials for La, Fe, Pd, O: https://www.materialscloud.org/discover/sssp/table/efficiency
- LaFeO3 orthorhombic crystal structure (Pbnm, GdFeO3-type): Standard crystallographic data; agent constructs unit cell from published lattice constants.
- Bulk bcc Fe crystal structure: Standard bcc Fe; agent generates coordinates.
- Bulk fcc Pd crystal structure: Standard fcc Pd; agent generates coordinates.
- O2 molecule geometry: Isolated O2 dimer; agent constructs from standard bond length.

## Workflow steps

### Step 1: Bulk LaFeO3 relaxation
- Role: process
- Action: Using Quantum ESPRESSO (PBE functional, spin-polarized, G-type AFM order), relax the orthorhombic LaFeO3 unit cell (Pbnm, GdFeO3-type) to obtain optimized lattice constants.
- Evidence: `/app/outputs/step_01_bulk_relax.log`

### Step 2: Reference total energies (Fe, Pd, O2)
- Role: process
- Action: Compute total energies of bulk bcc Fe, bulk fcc Pd, and an isolated O2 molecule using the same DFT settings (PBE, spin-polarized). These energies are required for the solution and vacancy formation energy formulas.
- Evidence: `/app/outputs/step_02_reference_energies.log`

### Step 3: Slab model construction
- Role: process
- Action: Build atomistic slab models for LaO- and FeO2-terminated LaFeO3(001) surfaces using the relaxed bulk lattice constants. Each slab contains 5 FeO2 layers, ~11 Å vacuum, and the bottom two layers fixed. Set up initial coordinates for subsequent relaxations.
- Evidence: `/app/outputs/step_03_slab_models.json`

### Step 4: Relaxation of Pd-substituted slabs (no vacancy)
- Role: process
- Action: For each of the two terminations (LaO, FeO2), substitute one Fe atom with Pd at the 1st and 3rd FeO2 layers (counting from the surface). Perform geometry relaxation of these slabs, keeping the bottom two layers fixed. Store total energies.
- Evidence: `/app/outputs/step_04_no_vo_relax_energies.json`

### Step 5: Relaxation with oxygen vacancy and identification of most stable site
- Role: process
- Action: For each Pd configuration (termination/layer), test all nonequivalent oxygen sites for the oxygen vacancy. For each candidate, relax the slab and compute the formation energy (reference: half O2). Identify the most stable (lowest formation energy) vacancy site for each configuration. Store the total energies and formation energies of the most stable configurations.
- Evidence: `/app/outputs/step_05_vo_relax_energies.json`

### Step 6: Compute segregation energies
- Role: scored (load-bearing)
- Action: Using the total energies from the relaxations and the reference energies, calculate the solution energy of Pd via the standard substitution-solution formula and the segregation energy as the difference between solution energies at the 1st and 3rd FeO2 layers. Compute the relative segregation energy (E_sol(1st) - E_sol(3rd)) for each of the four configurations: LaO without Vo, LaO with Vo, FeO2 without Vo, FeO2 with Vo. Write the results to step_03_segregation_energies.csv.
- Output file: `/app/outputs/step_03_segregation_energies.csv`
- Format: csv
- Contract: columns: termination (string, 'LaO' or 'FeO2'), vo_present (string, 'true'/'false'), relative_energy (float, eV). Four rows.
- Scoring: scored by hidden verifier

### Step 7: Compute oxygen vacancy formation energies
- Role: scored (load-bearing)
- Action: Using the most stable configuration energies from the vacancy relaxations and the O2 reference energy, calculate the formation energy of the oxygen vacancy for each termination when Pd is at the surface (the most stable Vo site for the Pd-surface case). Write the formation energies to step_04_vo_formation_energies.csv.
- Output file: `/app/outputs/step_04_vo_formation_energies.csv`
- Format: csv
- Contract: columns: termination (string, 'LaO' or 'FeO2'), formation_energy (float, eV), notes (string, optional description). Two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_segregation_energies.csv`
- `/app/outputs/step_04_vo_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_segregation_energies.csv
- path: `/app/outputs/step_03_segregation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative segregation energies (E_sol(1st) - E_sol(3rd)) for the four Pd/surface configurations: LaO without Vo, LaO with Vo, FeO2 without Vo, FeO2 with Vo.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `vo_present`, `relative_energy`
  - `units`:
    - `relative_energy`: eV

### step_04_vo_formation_energies.csv
- path: `/app/outputs/step_04_vo_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Oxygen vacancy formation energies for the most stable Vo site near the Pd-substituted surface of each termination.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `formation_energy`, `notes`
  - `units`:
    - `formation_energy`: eV

Notes: The checker will compare the reported values to hidden paper-reported Quantum ESPRESSO results with an absolute tolerance and verify the expected trend ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_segregation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "vo_present",
          "relative_energy"
        ],
        "units": {
          "relative_energy": "eV"
        }
      },
      "description": "Relative segregation energies (E_sol(1st) - E_sol(3rd)) for the four Pd/surface configurations: LaO without Vo, LaO with Vo, FeO2 without Vo, FeO2 with Vo."
    },
    {
      "file": "step_04_vo_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "formation_energy",
          "notes"
        ],
        "units": {
          "formation_energy": "eV"
        }
      },
      "description": "Oxygen vacancy formation energies for the most stable Vo site near the Pd-substituted surface of each termination."
    }
  ],
  "notes": "The checker will compare the reported values to hidden paper-reported Quantum ESPRESSO results with an absolute tolerance and verify the expected trend ordering."
}
```

## How you are scored
A hidden verifier program independently inspects the two output CSV files and extracts the reported relative segregation energies and oxygen vacancy formation energies. It compares each value against reference results derived from the paper's Quantum ESPRESSO calculations, using predefined tolerances. It also checks that the relative segregation energies across the four configurations obey a specific required ordering. The final reward (a float between 0 and 1) is a weighted combination of the scores from the segregation energies and the vacancy formation energies. To receive full credit, your computed values must be within the allowed tolerances and the trend must match the expected ordering. The verifier does not check any intermediate evidence files; you must output the required CSV files exactly as specified.
