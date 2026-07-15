# DFT+U Surface Free Energy and Gap State Calculation for Rutile TiO2(110) Reconstructions

## Problem background
Rutile TiO₂(110) is a model transition-metal oxide surface important in catalysis, photovoltaics, and gas sensing. Upon thermal reduction, the surface undergoes a (1 × 2) reconstruction whose atomic structure has been debated between two leading models: the Onishi (Ti₂O₃ added-row) and the Park (Ti₂O) models. Standard DFT fails to describe the experimentally observed gap states from excess electrons. This work uses DFT+U to obtain physically reasonable electronic structures and to compare the thermodynamic stability of the two reconstruction candidates by computing their surface free energies.

## Approach
Use an open-source DFT code (Quantum ESPRESSO or equivalent) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and a Hubbard U correction of U = 5 eV applied to the Ti 3d electrons, following the Dudarev approach. Perform spin-polarized calculations.

- Compute the total energy of the bulk rutile TiO₂ unit cell (Ti₄O₈) to obtain a bulk reference energy.
- Compute the DFT total energy of an isolated oxygen atom and derive the oxygen chemical potential E^O by subtracting half the experimental O₂ binding energy (5.26 eV) from the DFT O atom energy.
- Build symmetric 10-Ti-layer (Ti₄₀O₈₀) slab models for the stoichiometric (1×1) surface and the two (1×2)-reconstructed surfaces: Onishi (Ti₄₀O₇₈, Ti₂O₃ added-row) and Park (Ti₄₀O₇₄, Ti₂O added-row). Relax the geometry for each slab and obtain the total energy.
- Compute surface free energy σ for each surface according to σ = (1/(2A))(E_slab − n E_bulk + m E^O), where A is the (1×2) surface unit cell area, n = 40 for all models, m = 0 (stoichiometric), 2 (Onishi), 6 (Park).
- For the Onishi and Park relaxed slabs, compute the density of states (DOS) and identify the conduction band minimum (CBM) and the highest occupied defect state below the CBM. Report the energy difference (gap state position) in eV.

## Reproduction target
Produce three scored output files:
1. `bulk_energy_and_oxygen_ref.json` – contains the bulk energy per Ti₄O₈ (eV) and the oxygen chemical potential (eV).
2. `surface_energies.csv` – surface free energies (J/m²) for the three surface models: 'stoichiometric', 'Onishi', 'Park'.
3. `gap_state_positions.csv` – gap state energy below the CBM (eV) for the two reconstructed models: 'Onishi' and 'Park'.

All files must be placed under `/app/outputs`. Follow the exact format, column names, and schema described in the Workflow steps and Output contract.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- GBRV pseudopotentials for Ti and O (PBE): http://www.physics.rutgers.edu/gbrv/
- Rutile TiO2 crystal structure: ICSD 9162 or equivalent
- Experimental O2 binding energy (5.26 eV)

## Workflow steps

### Step 1: Reference energies (bulk and oxygen chemical potential)
- Role: scored
- Action: Compute the total energy of the bulk rutile TiO2 Ti4O8 unit cell using PBE+U (U=5 eV). Compute the DFT total energy of an isolated O atom. Derive the oxygen atom chemical potential E^O = (DFT O atom energy) - (experimental O2 binding energy)/2, using the experimental O2 binding energy of 5.26 eV. Save both the bulk energy per Ti4O8 unit and the derived oxygen chemical potential.
- Output file: `/app/outputs/bulk_energy_and_oxygen_ref.json`
- Format: json
- Contract: Object with keys: bulk_energy_per_unit (number, eV), O_chem_potential (number, eV)
- Scoring: scored by hidden verifier

### Step 2: Slab DFT calculations for three surface models
- Role: process
- Action: Construct symmetric 10-Ti-layer (Ti40O80) slab models for the stoichiometric, Onishi (Ti2O3 added-row, Ti40O78), and Park (Ti2O, Ti40O74) (1x2)-reconstructed TiO2(110) surfaces. Perform spin-polarized PBE+U geometry optimization and total energy calculations (U=5 eV) for each slab. Save the relaxed total energies for downstream analysis.
- Evidence: `/app/outputs/slab_total_energies.json`

### Step 3: Surface free energy calculation
- Role: scored (load-bearing)
- Action: Using the slab total energies from step 2, the bulk energy and O chemical potential from step 1, and the surface unit cell area, compute the surface free energies via the formula sigma = (1/(2A)) (E_slab - n E_bulk + m E^O). n=40, m=0 for stoichiometric, m=2 for Onishi, m=6 for Park. Report the three surface energies.
- Output file: `/app/outputs/surface_energies.csv`
- Format: csv
- Contract: Two columns: surface (string), sigma_Jperm2 (float)
- Scoring: scored by hidden verifier

### Step 4: Gap state position extraction
- Role: scored (load-bearing)
- Action: From the relaxed Onishi and Park slabs (step 2), compute the density of states (DOS). Identify the conduction band minimum (CBM) and the energy of the highest occupied defect state below the CBM. Report the magnitude of the gap state energy (positive value, eV) for each model.
- Output file: `/app/outputs/gap_state_positions.csv`
- Format: csv
- Contract: Two columns: surface (string), gap_state_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_energy_and_oxygen_ref.json`
- `/app/outputs/surface_energies.csv`
- `/app/outputs/gap_state_positions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_energy_and_oxygen_ref.json
- path: `/app/outputs/bulk_energy_and_oxygen_ref.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored reference energies that feed into the surface energy formula. The bulk energy per Ti4O8 unit and the oxygen chemical potential are checked against the paper's reference values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `bulk_energy_per_unit`: number (eV)
    - `O_chem_potential`: number (eV)

### surface_energies.csv
- path: `/app/outputs/surface_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed surface free energies for the stoichiometric, Onishi, and Park (1x2)-reconstructed TiO2(110) surfaces. Values are checked against the paper's reported surface energies with tolerance and ordering.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `sigma_Jperm2`
  - `units`:
    - `sigma_Jperm2`: J/m^2

### gap_state_positions.csv
- path: `/app/outputs/gap_state_positions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Gap state positions (energy below the conduction band minimum) for the Onishi and Park models. Compared to the paper's reported values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `gap_state_eV`
  - `units`:
    - `gap_state_eV`: eV below CBM

Notes: All scored artifacts are produced from a fully computational pipeline using open-source DFT code and public pseudopotentials. The checker compares the agent's computed values to hidden reference values with appropriate tolerances that account for code/pseudopotential differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_energy_and_oxygen_ref.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_energy_per_unit": "number (eV)",
          "O_chem_potential": "number (eV)"
        }
      },
      "description": "Scored reference energies that feed into the surface energy formula. The bulk energy per Ti4O8 unit and the oxygen chemical potential are checked against the paper's reference values with tolerance."
    },
    {
      "file": "surface_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "sigma_Jperm2"
        ],
        "units": {
          "sigma_Jperm2": "J/m^2"
        }
      },
      "description": "Computed surface free energies for the stoichiometric, Onishi, and Park (1x2)-reconstructed TiO2(110) surfaces. Values are checked against the paper's reported surface energies with tolerance and ordering."
    },
    {
      "file": "gap_state_positions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "gap_state_eV"
        ],
        "units": {
          "gap_state_eV": "eV below CBM"
        }
      },
      "description": "Gap state positions (energy below the conduction band minimum) for the Onishi and Park models. Compared to the paper's reported values with tolerance."
    }
  ],
  "notes": "All scored artifacts are produced from a fully computational pipeline using open-source DFT code and public pseudopotentials. The checker compares the agent's computed values to hidden reference values with appropriate tolerances that account for code/pseudopotential differences."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares the values in your output files to hidden reference values. The verifier first checks that each output file exists and has the correct structure (JSON keys, CSV columns). For the bulk energy and oxygen chemical potential, a tolerance is applied to account for systematic differences between DFT codes and pseudopotentials. For surface energies, the verifier checks both the numerical values (within a tolerance) and the relative ordering among the three surfaces. For gap state positions, the numerical values are compared against reference values within a tolerance. Each scored stage contributes a portion of the final reward; the total reward ranges from 0 (no match) to 1 (full agreement). You must genuinely execute the computational pipeline to produce these quantities; simply reporting the paper's published numbers is not sufficient.
