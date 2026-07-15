# Solvent Effects on γ‑Al2O3 and AlOOH Surfaces: DFT Study of Relaxation, Lewis Acidity, and DME Synthesis in Gas and Liquid Phases

## Problem background
Slurry-bubble reactors for methanol dehydration to dimethyl ether (DME) use a liquid organic medium such as liquid paraffin, but the microscopic influence of this solvent on the catalyst surfaces and on the reaction mechanism is not well understood. This work aims to quantify how liquid paraffin alters the structure, acidity, and reactivity of two alumina-based catalysts: γ‑Al₂O₃ and AlOOH (boehmite). The target is to compute, from first principles, the surface relaxation, charge distribution, adsorption behaviour of reactants, and the activation energies for DME formation on these surfaces in both gas phase and liquid paraffin, thereby revealing the solvent's role.

## Approach
Density functional theory (DFT) calculations with the PW91 exchange-correlation functional are employed. A conductor-like screening model (COSMO) with a dielectric constant of 2.06 is used to simulate liquid paraffin; gas-phase calculations omit the solvent model. Starting from the bulk crystal structures, the (110) surface of γ‑Al₂O₃ and the (100) surface of AlOOH are modelled with four-layer slabs. The top three layers are relaxed in vacuum and then re-optimised in the implicit solvent. From the relaxed slabs, atomic surface displacements (Δz) and Mulliken charges are extracted. Adsorption energies of CH₃OH, H₂O, and DME on the Lewis acid sites (Al atoms) are computed. Finally, complete LST/QST transition-state searches are performed for three proposed DME formation pathways on each surface: (I) two molecularly adsorbed CH₃OH → DME + H₂O; (II) one dissociatively adsorbed CH₃O reacts with a second CH₃OH; (III) two dissociatively adsorbed CH₃O → DME + O. All calculations may be performed with an open-source DFT code that supports PW91 and COSMO (e.g., CP2K).

## Reproduction target
Produce the following scored artifacts from the completed DFT workflow:

- CSV: surface relaxation (Δz, Å) and Mulliken charges (e) for the O1‑O4 and Al1‑Al3 atoms of γ‑Al₂O₃(110) in gas and liquid paraffin.
- CSV: surface relaxation (Δz, Å) and Mulliken charges (e) for the surface Al and O atoms of AlOOH(100) in gas and liquid paraffin.
- CSV: adsorption energies (eV) of CH₃OH, H₂O, and DME on the Al3 site of γ‑Al₂O₃(110) in gas and liquid paraffin.
- CSV: adsorption energies (eV) of CH₃OH, H₂O, and DME on AlOOH(100) in gas and liquid paraffin.
- JSON: activation energies (eV) for the three pathways (I, II, III) on γ‑Al₂O₃(110) in both phases, and the preferred pathway in each phase.
- JSON: activation energies (eV) for the three pathways on AlOOH(100) in both phases, and the preferred pathway in each phase.

Each file must follow the exact column and schema contracts detailed in the workflow steps.

## Assets

- CP2K (or another open‑source DFT code with COSMO support): https://www.cp2k.org/
- Bulk crystal structures of γ‑Al2O3 (non‑spinel) and AlOOH (orthorhombic)

## Workflow steps

### Step 1: Optimize bulk structures of γ‑Al2O3 and AlOOH
- Role: process
- Action: Perform DFT geometry optimization of the bulk unit cells for γ‑Al2O3 (non‑spinel model) and AlOOH (orthorhombic) to obtain accurate lattice parameters and atomic positions.
- Evidence: `/app/outputs/bulk_opt.log`

### Step 2: Build and relax surface slabs in gas phase
- Role: process
- Action: Construct four‑layer slab models for the γ‑Al2O3 (110) and AlOOH (100) surfaces from the optimized bulk structures. Relax the top three layers in vacuum (gas phase) while fixing the bottom layer(s).
- Evidence: `/app/outputs/slabs_gas.xyz`

### Step 3: Re‑optimize surface slabs in liquid paraffin
- Role: process
- Action: Using the gas‑phase relaxed slabs as initial guesses, re‑optimize the same slab geometries with the COSMO implicit solvent model (dielectric constant 2.06) to represent liquid paraffin.
- Evidence: `/app/outputs/slabs_liquid.xyz`

### Step 4: Surface relaxation and Mulliken charges for γ‑Al2O3(110)
- Role: scored
- Action: Extract perpendicular displacements Δz of surface O1‑O4 and Al1‑Al3 atoms relative to bulk positions from the gas‑phase and liquid‑paraffin relaxed slabs. Compute Mulliken charges for those atoms. Write the results to the output CSV.
- Output file: `/app/outputs/step_02_gamma_surface_relaxation.csv`
- Format: csv
- Contract: surface (string), atom_label (string), delta_z_gas (float, Å), Q_gas (float, e), delta_z_liquid (float, Å), Q_liquid (float, e)
- Scoring: scored by hidden verifier

### Step 5: Surface relaxation and Mulliken charges for AlOOH(100)
- Role: scored
- Action: Extract perpendicular displacements Δz of surface Al and O atoms relative to bulk positions from the gas‑phase and liquid‑paraffin relaxed slabs. Compute Mulliken charges. Write the results to the output CSV.
- Output file: `/app/outputs/step_03_boehmite_surface_relaxation.csv`
- Format: csv
- Contract: surface (string), atom_label (string), delta_z_gas (float, Å), Q_gas (float, e), delta_z_liquid (float, Å), Q_liquid (float, e)
- Scoring: scored by hidden verifier

### Step 6: Adsorption energies on γ‑Al2O3(110)
- Role: scored
- Action: Calculate the adsorption energies of CH3OH, H2O, and DME on the Al3 Lewis acid site of the γ‑Al2O3(110) surface in gas phase and in liquid paraffin using the relaxed slab models. Write results.
- Output file: `/app/outputs/step_04_gamma_adsorption_energies.csv`
- Format: csv
- Contract: adsorbate (string), site_type (string), Eads_gas (float, eV), Eads_liquid (float, eV)
- Scoring: scored by hidden verifier

### Step 7: Adsorption energies on AlOOH(100)
- Role: scored
- Action: Calculate the adsorption energies of CH3OH, H2O, and DME on the AlOOH(100) surface in gas phase and in liquid paraffin. Write results.
- Output file: `/app/outputs/step_05_boehmite_adsorption_energies.csv`
- Format: csv
- Contract: adsorbate (string), Eads_gas (float, eV), Eads_liquid (float, eV)
- Scoring: scored by hidden verifier

### Step 8: Reaction profiles for DME synthesis over γ‑Al2O3(110)
- Role: scored (load-bearing)
- Action: Using complete LST/QST transition state search, construct the energy profiles for the three DME formation pathways (I: 2 CH3OH → DME + H2O, II: CH3O + CH3OH → DME + OH, III: 2 CH3O → DME + O) on the γ‑Al2O3(110) surface in gas phase and liquid paraffin. Report activation energies for each path and identify the preferred path in each phase.
- Output file: `/app/outputs/step_06_gamma_reaction_profile.json`
- Format: json
- Contract: {"path_I": {"Ea_gas": float, "Ea_liquid": float}, "path_II": {"Ea_gas": float, "Ea_liquid": float}, "path_III": {"Ea_gas": float, "Ea_liquid": float}, "preferred_path_gas": "string", "preferred_path_liquid": "string"}
- Scoring: scored by hidden verifier

### Step 9: Reaction profiles for DME synthesis over AlOOH(100)
- Role: scored (load-bearing)
- Action: Using complete LST/QST transition state search, construct the energy profiles for the three pathways on the AlOOH(100) surface in gas phase and liquid paraffin. Report activation energies and identify the preferred path in each phase.
- Output file: `/app/outputs/step_07_boehmite_reaction_profile.json`
- Format: json
- Contract: {"path_I": {"Ea_gas": float, "Ea_liquid": float}, "path_II": {"Ea_gas": float, "Ea_liquid": float}, "path_III": {"Ea_gas": float, "Ea_liquid": float}, "preferred_path_gas": "string", "preferred_path_liquid": "string"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_gamma_surface_relaxation.csv`
- `/app/outputs/step_03_boehmite_surface_relaxation.csv`
- `/app/outputs/step_04_gamma_adsorption_energies.csv`
- `/app/outputs/step_05_boehmite_adsorption_energies.csv`
- `/app/outputs/step_06_gamma_reaction_profile.json`
- `/app/outputs/step_07_boehmite_reaction_profile.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_gamma_surface_relaxation.csv
- path: `/app/outputs/step_02_gamma_surface_relaxation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Surface relaxation Δz and Mulliken charges for γ‑Al2O3(110) surface atoms.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `atom_label`, `delta_z_gas`, `Q_gas`, `delta_z_liquid`, `Q_liquid`
  - `units`:
    - `delta_z_gas`: Å
    - `delta_z_liquid`: Å
    - `Q_gas`: e
    - `Q_liquid`: e

### step_03_boehmite_surface_relaxation.csv
- path: `/app/outputs/step_03_boehmite_surface_relaxation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Surface relaxation Δz and Mulliken charges for AlOOH(100) surface atoms.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `atom_label`, `delta_z_gas`, `Q_gas`, `delta_z_liquid`, `Q_liquid`
  - `units`:
    - `delta_z_gas`: Å
    - `delta_z_liquid`: Å
    - `Q_gas`: e
    - `Q_liquid`: e

### step_04_gamma_adsorption_energies.csv
- path: `/app/outputs/step_04_gamma_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Adsorption energies on the Al3 site of γ‑Al2O3(110).
- schema:
  - `type`: table
  - `required_columns`: `adsorbate`, `site_type`, `Eads_gas`, `Eads_liquid`
  - `units`:
    - `Eads_gas`: eV
    - `Eads_liquid`: eV

### step_05_boehmite_adsorption_energies.csv
- path: `/app/outputs/step_05_boehmite_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Adsorption energies on AlOOH(100).
- schema:
  - `type`: table
  - `required_columns`: `adsorbate`, `Eads_gas`, `Eads_liquid`
  - `units`:
    - `Eads_gas`: eV
    - `Eads_liquid`: eV

### step_06_gamma_reaction_profile.json
- path: `/app/outputs/step_06_gamma_reaction_profile.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Activation energies for DME synthesis on γ‑Al2O3(110).
- schema:
  - `type`: object
  - `required`: `path_I`, `path_II`, `path_III`, `preferred_path_gas`, `preferred_path_liquid`
  - `items`:
    - `Ea_gas`: float (eV)
    - `Ea_liquid`: float (eV)
  - `preferred_path_gas`: string
  - `preferred_path_liquid`: string

### step_07_boehmite_reaction_profile.json
- path: `/app/outputs/step_07_boehmite_reaction_profile.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Activation energies for DME synthesis on AlOOH(100).
- schema:
  - `type`: object
  - `required`: `path_I`, `path_II`, `path_III`, `preferred_path_gas`, `preferred_path_liquid`
  - `items`:
    - `Ea_gas`: float (eV)
    - `Ea_liquid`: float (eV)
  - `preferred_path_gas`: string
  - `preferred_path_liquid`: string

Notes: All values are checked against paper‑reported numbers with appropriate tolerances (not disclosed). The checker also verifies that relative trends hold (e.g., adsorption energies less negative in liquid paraffin, preferred pathway assignments consistent with reported mechanism).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_gamma_surface_relaxation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "atom_label",
          "delta_z_gas",
          "Q_gas",
          "delta_z_liquid",
          "Q_liquid"
        ],
        "units": {
          "delta_z_gas": "Å",
          "delta_z_liquid": "Å",
          "Q_gas": "e",
          "Q_liquid": "e"
        }
      },
      "description": "Surface relaxation Δz and Mulliken charges for γ‑Al2O3(110) surface atoms."
    },
    {
      "file": "step_03_boehmite_surface_relaxation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "atom_label",
          "delta_z_gas",
          "Q_gas",
          "delta_z_liquid",
          "Q_liquid"
        ],
        "units": {
          "delta_z_gas": "Å",
          "delta_z_liquid": "Å",
          "Q_gas": "e",
          "Q_liquid": "e"
        }
      },
      "description": "Surface relaxation Δz and Mulliken charges for AlOOH(100) surface atoms."
    },
    {
      "file": "step_04_gamma_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "adsorbate",
          "site_type",
          "Eads_gas",
          "Eads_liquid"
        ],
        "units": {
          "Eads_gas": "eV",
          "Eads_liquid": "eV"
        }
      },
      "description": "Adsorption energies on the Al3 site of γ‑Al2O3(110)."
    },
    {
      "file": "step_05_boehmite_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "adsorbate",
          "Eads_gas",
          "Eads_liquid"
        ],
        "units": {
          "Eads_gas": "eV",
          "Eads_liquid": "eV"
        }
      },
      "description": "Adsorption energies on AlOOH(100)."
    },
    {
      "file": "step_06_gamma_reaction_profile.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "path_I",
          "path_II",
          "path_III",
          "preferred_path_gas",
          "preferred_path_liquid"
        ],
        "items": {
          "Ea_gas": "float (eV)",
          "Ea_liquid": "float (eV)"
        },
        "preferred_path_gas": "string",
        "preferred_path_liquid": "string"
      },
      "description": "Activation energies for DME synthesis on γ‑Al2O3(110)."
    },
    {
      "file": "step_07_boehmite_reaction_profile.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "path_I",
          "path_II",
          "path_III",
          "preferred_path_gas",
          "preferred_path_liquid"
        ],
        "items": {
          "Ea_gas": "float (eV)",
          "Ea_liquid": "float (eV)"
        },
        "preferred_path_gas": "string",
        "preferred_path_liquid": "string"
      },
      "description": "Activation energies for DME synthesis on AlOOH(100)."
    }
  ],
  "notes": "All values are checked against paper‑reported numbers with appropriate tolerances (not disclosed). The checker also verifies that relative trends hold (e.g., adsorption energies less negative in liquid paraffin, preferred pathway assignments consistent with reported mechanism)."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact by comparing your computed quantities to a reference. Appropriate tolerances are used for each physical quantity, and the verifier also checks that relative trends (e.g., sign and magnitude relationships between phases) are correctly reproduced. The individual scores are combined by weight into a final reward between 0 and 1. Simply reporting the paper's published numbers without running the actual computations will not produce a passing score because the verifier checks consistency and magnitude against an independent reference.
