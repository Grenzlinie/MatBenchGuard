# DFT formation and adsorption energies for ε-MnO₂ with Mn vacancies and Li⁺

## Problem background
Epsilon-MnO₂ (ε-MnO₂) with the akhtenskite structure is a promising catalyst for ozone decomposition. Oxygen vacancies on the catalyst surface are believed to be the active sites for ozone adsorption and decomposition. Introducing manganese (Mn) vacancies and alkali ions such as Li⁺ into the ε-MnO₂ lattice has been proposed to tune the formation energy of these oxygen vacancies and to alter the adsorption strengths of O₃, H₂O, and O₂ molecules. Quantifying these effects via first-principles calculations can provide insight into the catalytic mechanism. This task aims to reproduce the DFT‑computed oxygen vacancy formation energies and molecular adsorption energies for ε-MnO₂ systems with different defect and dopant configurations.

## Approach
Use density functional theory (DFT) calculations with an open‑source code such as Quantum ESPRESSO and standard pseudopotentials. Construct periodic supercells of ε‑MnO₂: both bulk models and surface slabs. Create models with and without a Mn vacancy, and for surface models incorporate varying numbers of Li⁺ ions placed near the Mn vacancy site. For each model, compute the total energy of the pristine structure and of the structure with an oxygen vacancy, then derive the oxygen vacancy formation energy. To compute adsorption energies, calculate total energies of isolated gas‑phase O₃, H₂O, and O₂ molecules, and of surface slabs with these molecules adsorbed on oxygen vacancy sites. The adsorption energy is the difference between the energy of the slab+molecule system and the sum of the clean slab energy and the isolated molecule energy. The workflow covers systems with a perfect surface, a surface with an oxygen vacancy only, a surface with both oxygen and Mn vacancies, and a surface with both vacancies plus a moderate number of Li⁺ ions.

## Reproduction target
Generate two CSV files. `formation_energies.csv` must contain oxygen vacancy formation energies (in eV) for bulk perfect, bulk with Mn vacancy, surface perfect, surface with Mn vacancy, and surface with Mn vacancy at several Li⁺ numbers (e.g., 0 to 6). `adsorption_energies.csv` must contain adsorption energies (in eV) for O₃, H₂O, and O₂ on the following surface types: perfect, surface with an oxygen vacancy only (V_O_only), surface with both oxygen and Mn vacancies (V_O + V_Mn), and surface with both vacancies plus Li⁺ (V_O + V_Mn + Li). The reported energies should be physically reasonable: formation energies positive and adsorption energies negative (exothermic). The specific numerical values will be evaluated for internal consistency across the different configurations.

## Assets

- ε-MnO₂ crystal structure (akhtenskite)
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Construct ε-MnO₂ structural models
- Role: process
- Action: Build bulk and surface supercells of ε-MnO₂ (akhtenskite structure, lattice parameters a=2.828 Å, c=4.465 Å). Create perfect cells and cells containing a Mn vacancy. For surface models, construct slabs and incorporate varying numbers of Li⁺ ions placed near Mn vacancy sites.
- Evidence: none

### Step 2: Compute oxygen vacancy formation energies
- Role: scored (load-bearing)
- Action: Using DFT (Quantum ESPRESSO), compute total energies of the perfect and defective structures and of structures with an oxygen vacancy. Calculate oxygen vacancy formation energies for: bulk perfect, bulk with Mn vacancy, surface perfect, surface with Mn vacancy, and surface with Mn vacancy at a range of Li⁺ numbers (e.g., 0 to 6). Output to formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: Columns: system (string, e.g. bulk_perfect, bulk_Mn_vac, surf_perfect, surf_Mn_vac, surf_Mn_vac_Li0, ...), Li_number (integer, optional, present for Li-containing systems), E_form_eV (float, unit: eV).
- Scoring: scored by hidden verifier

### Step 3: Compute adsorption energies of O₃, H₂O, O₂ on ε-MnO₂ surfaces
- Role: scored
- Action: Using DFT, compute total energies of gas-phase O₃, H₂O, O₂ molecules and of surface slabs with these molecules adsorbed on oxygen vacancy sites. Configurations: (a) perfect surface, (b) surface with an oxygen vacancy (V_O) only, (c) surface with V_O and a Mn vacancy (V_Mn), (d) surface with V_O, V_Mn and a moderate number of Li⁺ ions. Calculate adsorption energies and output to adsorption_energies.csv.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Columns: surface_type (string, e.g. perfect, V_O_only, V_O+V_Mn, V_O+V_Mn+Li), adsorbate (string: O3, H2O, O2), E_ads_eV (float, unit: eV), Li_number (integer, optional, included for Li-containing configurations).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/adsorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The checker verifies that the formation energies exhibit internally consistent and physically plausible behavior across the different configurations.
- schema:
  - `type`: table
  - `required_columns`: `system`, `E_form_eV`
  - `optional_columns`: `Li_number`
  - `units`:
    - `E_form_eV`: eV

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The checker verifies that the adsorption energies exhibit internally consistent and physically plausible behavior across the different configurations.
- schema:
  - `type`: table
  - `required_columns`: `surface_type`, `adsorbate`, `E_ads_eV`
  - `optional_columns`: `Li_number`
  - `units`:
    - `E_ads_eV`: eV

Notes: Absolute formation/adsorption energies may differ from the original paper due to use of a different DFT code (Quantum ESPRESSO vs. VASP) and pseudopotentials; only the relative trends are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "E_form_eV"
        ],
        "optional_columns": [
          "Li_number"
        ],
        "units": {
          "E_form_eV": "eV"
        }
      },
      "description": "The checker verifies that the formation energies exhibit internally consistent and physically plausible behavior across the different configurations."
    },
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface_type",
          "adsorbate",
          "E_ads_eV"
        ],
        "optional_columns": [
          "Li_number"
        ],
        "units": {
          "E_ads_eV": "eV"
        }
      },
      "description": "The checker verifies that the adsorption energies exhibit internally consistent and physically plausible behavior across the different configurations."
    }
  ],
  "notes": "Absolute formation/adsorption energies may differ from the original paper due to use of a different DFT code (Quantum ESPRESSO vs. VASP) and pseudopotentials; only the relative trends are scored."
}
```

## How you are scored
A hidden verification script reads your two CSV files and evaluates them against expected structural trends. It does not require agreement with any single absolute reference value, because different DFT settings (pseudopotentials, functionals) can shift absolute energies. Instead, it checks that (i) sign conventions are obeyed (formation energies positive; adsorption energies negative), and (ii) the energies vary in a systematic, physically plausible manner as the defect and dopant concentrations change. The checker combines scores from several such checks into a single reward between 0 and 1, with the largest weight on the formation energy trends. Reporting numbers is not enough; the verifier will independently examine the numbers you provide.
