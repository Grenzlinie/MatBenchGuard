# DFT Adsorption Energy and Bader Charge Analysis on High-Entropy Perovskite (110) Surfaces

## Problem background
High‑entropy perovskite oxides, such as La(Ni0.2Mn0.2Cu0.2Fe0.2Co0.2)O3-δ (HE‑LMO), can be synthesized with abundant oxygen vacancies and nanoscale dimensions. These materials have been investigated as catalysts for CO oxidation. Density functional theory (DFT) calculations are used to probe how oxygen vacancies and reduced transition metal sites on the (110) surface influence the adsorption and activation of CO molecules. This task reproduces the key DFT‑derived quantities that underlie the proposed catalytic mechanism.

## Approach
Two slab models of the HE‑LMO (110) surface are constructed: a defective “Redox” slab with three surface oxygen vacancies adjacent to Co, Cu, and Ni atoms, and a stoichiometric “Bulk” slab without vacancies. Spin‑polarized DFT geometry optimizations are performed for both clean slabs and for an isolated CO molecule. CO is then placed atop a Co atom on each slab, and the adsorbate+slab system is relaxed. The adsorption energy is computed as E_ads = E(CO+slab) – E(slab) – E(CO). The C–O bond length in the adsorbed CO and the Bader charges on the Co atom before and after CO adsorption are extracted for both slabs. The gas‑phase CO bond length is obtained from the isolated molecule calculation. The comparison between the Redox and Bulk slabs reveals how the introduced oxygen vacancies affect the binding and geometry of CO.

## Reproduction target
Using an open‑source DFT code (e.g., Quantum ESPRESSO) and standard pseudopotentials, perform the slab construction, geometry optimizations, CO adsorption, and Bader charge analysis described in the Approach. Compute the following quantities and write them to a JSON file (`adsorption_results.json`):
- For the defective (Redox) slab with CO adsorbed: adsorption energy (eV), C–O bond length (Å), Bader charge on Co before adsorption (e), and Bader charge on Co after adsorption (e).
- For the stoichiometric (Bulk) slab with CO adsorbed: the same four quantities.
- The gas‑phase CO bond length (Å).
Additionally, export the optimized atomic coordinates of each CO‑adsorbed slab as separate XYZ files (`Redox_slab_with_CO.xyz` and `Bulk_slab_with_CO.xyz`).

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/
- Standard solid-state pseudopotentials (SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table
- LaMnO3 bulk crystal structure (Material Project or ICSD): https://www.materialsproject.org/materials/mp-19317
- Bader charge analysis code (Henkelman group): https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Build HE-LMO (110) slab models
- Role: process
- Action: Construct bulk HE-LMO (La(Ni0.2Mn0.2Cu0.2Fe0.2Co0.2)O3) unit cell from LaMnO3 perovskite (ICSD or MP). Cut a (110) surface slab with vacuum. For the Redox slab, remove three oxygen atoms adjacent to Co, Cu, and Ni. For the Bulk slab, keep stoichiometric. Generate DFT input files for both slabs.
- Evidence: none

### Step 2: DFT geometry optimization of clean slabs
- Role: process
- Action: Perform spin-polarized DFT geometry relaxation on both the Redox and Bulk HE-LMO (110) slabs using Quantum ESPRESSO (or equivalent) with appropriate pseudopotentials, until forces converge.
- Evidence: none

### Step 3: Optimize gas-phase CO molecule
- Role: process
- Action: Place a CO molecule in a large cell and perform DFT geometry relaxation to obtain the isolated CO bond length and total energy as reference for adsorption calculations.
- Evidence: none

### Step 4: CO adsorption and Bader analysis
- Role: scored (load-bearing)
- Action: For each slab (Redox and Bulk), place CO atop the relaxed Co atom, perform DFT geometry optimization, then compute: adsorption energy E_ads = E(CO+slab) - E(slab) - E(CO), C-O bond length in the adsorbed CO, and Bader charges of the Co atom on the clean slab and on the CO-adsorbed slab. Additionally, output the gas-phase CO bond length.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: {
  "Redox_HE_LMO": { "adsorption_energy_eV": float, "C_O_bond_length_Ang": float, "Bader_charge_Co_before_e": float, "Bader_charge_Co_after_e": float },
  "Bulk_HE_LMO": { "adsorption_energy_eV": float, "C_O_bond_length_Ang": float, "Bader_charge_Co_before_e": float, "Bader_charge_Co_after_e": float },
  "gas_phase_CO_bond_length_Ang": float
}
- Scoring: scored by hidden verifier

### Step 5: Export Redox slab with CO geometry
- Role: scored
- Action: Extract the final optimized atomic positions of the Redox-HE-LMO (110) slab with CO adsorbed and write to an XYZ file.
- Output file: `/app/outputs/Redox_slab_with_CO.xyz`
- Format: txt
- Contract: XYZ format: first line atom count, second line comment, then lines with element symbol x y z.
- Scoring: scored by hidden verifier

### Step 6: Export Bulk slab with CO geometry
- Role: scored
- Action: Extract the final optimized atomic positions of the Bulk-HE-LMO (110) slab with CO adsorbed and write to an XYZ file.
- Output file: `/app/outputs/Bulk_slab_with_CO.xyz`
- Format: txt
- Contract: XYZ format: first line atom count, second line comment, then lines with element symbol x y z.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.json`
- `/app/outputs/Redox_slab_with_CO.xyz`
- `/app/outputs/Bulk_slab_with_CO.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Main scored artifact containing adsorption energies (eV), C-O bond lengths (Å), and Bader charges (e) for the Redox and Bulk HE-LMO surfaces, plus the gas-phase CO bond length.
- schema:
  - `type`: object
  - `required`: `Redox_HE_LMO`, `Bulk_HE_LMO`, `gas_phase_CO_bond_length_Ang`
  - `properties`:
    - `Redox_HE_LMO`:
      - `type`: object
      - `required`: `adsorption_energy_eV`, `C_O_bond_length_Ang`, `Bader_charge_Co_before_e`, `Bader_charge_Co_after_e`
    - `Bulk_HE_LMO`:
      - `type`: object
      - `required`: `adsorption_energy_eV`, `C_O_bond_length_Ang`, `Bader_charge_Co_before_e`, `Bader_charge_Co_after_e`
    - `gas_phase_CO_bond_length_Ang`:
      - `type`: number

### Redox_slab_with_CO.xyz
- path: `/app/outputs/Redox_slab_with_CO.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: XYZ file of the optimized Redox-HE-LMO slab with adsorbed CO; checked for correct atom counts and elements and internal consistency with adsorption_results.json.
- schema:
  - `type`: text
  - `format`: XYZ
  - `fields`: `atom_count`, `comment_line`, `atom_symbol`, `x`, `y`, `z`

### Bulk_slab_with_CO.xyz
- path: `/app/outputs/Bulk_slab_with_CO.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: XYZ file of the optimized Bulk-HE-LMO slab with adsorbed CO; checked for correct atom counts and elements and internal consistency with adsorption_results.json.
- schema:
  - `type`: text
  - `format`: XYZ
  - `fields`: `atom_count`, `comment_line`, `atom_symbol`, `x`, `y`, `z`

Notes: The checker will compare numerical values in adsorption_results.json to the paper's reference values with appropriate tolerances (adsorption energy ±0.1 eV, bond length ±0.01 Å, Bader charge ±0.05 e). The two XYZ files are audited for existence, reasonable atom counts, and consistency with the JSON. Missing or clearly invalid XYZ files apply a penalty.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Redox_HE_LMO",
          "Bulk_HE_LMO",
          "gas_phase_CO_bond_length_Ang"
        ],
        "properties": {
          "Redox_HE_LMO": {
            "type": "object",
            "required": [
              "adsorption_energy_eV",
              "C_O_bond_length_Ang",
              "Bader_charge_Co_before_e",
              "Bader_charge_Co_after_e"
            ]
          },
          "Bulk_HE_LMO": {
            "type": "object",
            "required": [
              "adsorption_energy_eV",
              "C_O_bond_length_Ang",
              "Bader_charge_Co_before_e",
              "Bader_charge_Co_after_e"
            ]
          },
          "gas_phase_CO_bond_length_Ang": {
            "type": "number"
          }
        }
      },
      "description": "Main scored artifact containing adsorption energies (eV), C-O bond lengths (Å), and Bader charges (e) for the Redox and Bulk HE-LMO surfaces, plus the gas-phase CO bond length."
    },
    {
      "file": "Redox_slab_with_CO.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "format": "XYZ",
        "fields": [
          "atom_count",
          "comment_line",
          "atom_symbol",
          "x",
          "y",
          "z"
        ]
      },
      "description": "XYZ file of the optimized Redox-HE-LMO slab with adsorbed CO; checked for correct atom counts and elements and internal consistency with adsorption_results.json."
    },
    {
      "file": "Bulk_slab_with_CO.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "format": "XYZ",
        "fields": [
          "atom_count",
          "comment_line",
          "atom_symbol",
          "x",
          "y",
          "z"
        ]
      },
      "description": "XYZ file of the optimized Bulk-HE-LMO slab with adsorbed CO; checked for correct atom counts and elements and internal consistency with adsorption_results.json."
    }
  ],
  "notes": "The checker will compare numerical values in adsorption_results.json to the paper's reference values with appropriate tolerances (adsorption energy ±0.1 eV, bond length ±0.01 Å, Bader charge ±0.05 e). The two XYZ files are audited for existence, reasonable atom counts, and consistency with the JSON. Missing or clearly invalid XYZ files apply a penalty."
}
```

## How you are scored
A hidden verifier independently evaluates the uploaded artifacts. The primary score comes from comparing the numerical values in `adsorption_results.json` to reference values (the paper’s reported results) using appropriate tolerances. The verifier also checks that `Redox_slab_with_CO.xyz` and `Bulk_slab_with_CO.xyz` exist, contain plausible atom counts and elements consistent with the HE‑LMO composition, and that the C–O bond lengths match those in the JSON file. The final score is a weighted combination of these checks. Reporting numbers that differ from the reference or producing invalid XYZ files will reduce the score. The specific tolerances and weights are hidden; you must compute the quantities by faithfully executing the described DFT workflow.
