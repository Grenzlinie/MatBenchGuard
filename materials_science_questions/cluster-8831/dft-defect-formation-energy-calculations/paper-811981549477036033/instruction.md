# DFT reaction energies for water absorption and defect formation in forsterite, MgO, and α-quartz

## Problem background
This task reproduces a computational study of water incorporation in forsterite (Mg2SiO4), the magnesium end‑member of olivine, a common rock‑forming mineral. Water is known to influence the physical properties of mantle minerals, including forsterite. Understanding the energetics of water incorporation — as interstitial H2O molecules or as protons replacing cation defects — provides insight into water storage and transport in the Earth’s mantle. The study uses density functional theory (DFT) to compute reaction energies for water uptake in perfect forsterite, MgO (periclase), and α‑quartz (SiO2), and for defect formation where MgO or SiO2 units are replaced by water molecules.

## Approach
The reproduction employs first‑principles DFT within the generalized‑gradient approximation (GGA) and plane‑wave basis sets with pseudopotentials to describe core electrons. The calculations are performed using an open‑source plane‑wave DFT code. The workflow consists of several stages:

1. Relax perfect crystals of forsterite (orthorhombic), MgO (rock‑salt), and α‑quartz (hexagonal) to obtain their lowest‑energy configurations and total energies.
2. Compute the total energy of an isolated gas‑phase water molecule.
3. Create supercells of each host material, introduce an interstitial water molecule, and relax the structure to obtain the energy of the water‑absorbed system.
4. Model substitutional defects: remove an MgO or SiO2 unit from the crystal lattice and incorporate water molecules (two for each removed SiO2, one for each removed MgO) to maintain charge neutrality, then relax the defect supercell and compute its total energy. The MgO replacements are performed at the two distinct octahedral sites M1 and M2 in forsterite, and in pure MgO.
5. From the set of total energies, calculate reaction energies for each incorporation process using stoichiometric reaction equations defined by the paper’s methodology. The resulting reaction energies are reported in kJ/mol.

## Reproduction target
The objective is to produce a single JSON file, `/app/outputs/reaction_energies.json`, containing all DFT total energies (eV) used in the calculations and the eight reaction energies (kJ/mol). Specifically, the required reaction energies are:

- Water absorption in perfect forsterite
- Water absorption in perfect MgO
- Water absorption in perfect α‑quartz
- Replacement of an SiO2 unit by two water molecules in forsterite
- Replacement of an SiO2 unit by two water molecules in α‑quartz
- Replacement of an MgO unit by one water molecule at the M1 site in forsterite
- Replacement of an MgO unit by one water molecule at the M2 site in forsterite
- Replacement of an MgO unit by one water molecule in MgO

All total energies must be computed from DFT relaxations using the GGA functional and publicly available crystal structures. The reaction energies must be derived from these total energies and be reported in the JSON file along with the total energies. No pre‑computed values may be used.

## Assets

- Forsterite (Mg2SiO4) crystal structure: https://materialsproject.org/materials/mp-289
- MgO (periclase) crystal structure: https://materialsproject.org/materials/mp-1265
- α-quartz (SiO2) crystal structure: https://materialsproject.org/materials/mp-6930
- Open-source plane-wave DFT code: https://www.quantum-espresso.org/
- Standard PAW pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax perfect forsterite crystal
- Role: process
- Action: Use an open-source DFT code with GGA functional and PAW pseudopotentials to relax the perfect Mg2SiO4 (forsterite) crystal (orthorhombic, Pbnm). Record the relaxed total energy.
- Evidence: `/app/outputs/forsterite_energy.txt`

### Step 2: Relax perfect MgO crystal
- Role: process
- Action: Relax the perfect face-centered cubic MgO crystal and record its total energy.
- Evidence: `/app/outputs/MgO_energy.txt`

### Step 3: Relax perfect α-quartz crystal
- Role: process
- Action: Relax the perfect hexagonal α-quartz (SiO2) crystal and record its total energy.
- Evidence: `/app/outputs/quartz_energy.txt`

### Step 4: Calculate isolated H2O molecule
- Role: process
- Action: Compute the total energy of an isolated H2O molecule placed in a large vacuum cell to represent the gaseous state. Use the same DFT settings.
- Evidence: `/app/outputs/H2O_energy.txt`

### Step 5: Water absorption in perfect forsterite
- Role: process
- Action: Build a supercell of forsterite, insert one interstitial H2O molecule, relax the structure, and obtain the total energy of the forsterite+H2O system.
- Evidence: `/app/outputs/forsterite_H2O_energy.txt`

### Step 6: Water absorption in perfect MgO
- Role: process
- Action: Insert one interstitial H2O molecule into a perfect MgO supercell, relax, and obtain the total energy.
- Evidence: `/app/outputs/MgO_H2O_energy.txt`

### Step 7: Water absorption in perfect α-quartz
- Role: process
- Action: Insert one interstitial H2O molecule into a perfect α-quartz supercell, relax, and obtain the total energy.
- Evidence: `/app/outputs/quartz_H2O_energy.txt`

### Step 8: SiO2 replacement defect in forsterite
- Role: process
- Action: Create a forsterite supercell, remove one SiO2 unit, replace it with four protons (i.e., two H2O molecules), relax the defect structure, and record the total energy.
- Evidence: `/app/outputs/forsterite_Si_vac_energy.txt`

### Step 9: SiO2 replacement defect in α-quartz
- Role: process
- Action: Create an α-quartz supercell, remove one SiO2 unit, replace it with four protons (two H2O molecules), relax, and record the total energy.
- Evidence: `/app/outputs/quartz_Si_vac_energy.txt`

### Step 10: MgO replacement defect at M1 site in forsterite
- Role: process
- Action: Create a forsterite supercell, remove one MgO unit from the M1 octahedral site, insert one H2O molecule, relax, and record the total energy.
- Evidence: `/app/outputs/forsterite_Mg_vac_M1_energy.txt`

### Step 11: MgO replacement defect at M2 site in forsterite
- Role: process
- Action: Create a forsterite supercell, remove one MgO unit from the M2 octahedral site, insert one H2O molecule, relax, and record the total energy.
- Evidence: `/app/outputs/forsterite_Mg_vac_M2_energy.txt`

### Step 12: MgO replacement defect in MgO
- Role: process
- Action: Create an MgO supercell, replace one MgO unit by one H2O molecule, relax, and record the total energy.
- Evidence: `/app/outputs/MgO_vac_energy.txt`

### Step 13: Compute and report all reaction energies
- Role: scored (load-bearing)
- Action: Using the total energies obtained in the previous steps, calculate the eight reaction energies (in kJ/mol) according to the paper's stoichiometric reaction definitions: (1) water absorption in perfect forsterite, (2) in perfect MgO, (3) in perfect α-quartz; (4) SiO2 replacement by two water molecules in forsterite, (5) in α-quartz; (6) MgO replacement by one water molecule at M1 site in forsterite, (7) at M2 site in forsterite, (8) in MgO. Output all total energies (eV) and the computed reaction energies (kJ/mol) in a single JSON file.
- Output file: `/app/outputs/reaction_energies.json`
- Format: json
- Contract: {"total_energies": {"forsterite": <eV>, "MgO": <eV>, "alpha_quartz": <eV>, "H2O_isolated": <eV>, "forsterite_H2O_absorbed": <eV>, "MgO_H2O_absorbed": <eV>, "alpha_quartz_H2O_absorbed": <eV>, "forsterite_Si_vacancy": <eV>, "alpha_quartz_Si_vacancy": <eV>, "forsterite_Mg_vacancy_M1": <eV>, "forsterite_Mg_vacancy_M2": <eV>, "MgO_vacancy": <eV>}, "reaction_energies": {"water_absorption_forsterite": <kJ_per_mol>, "water_absorption_MgO": <kJ_per_mol>, "water_absorption_alpha_quartz": <kJ_per_mol>, "SiO2_replacement_forsterite": <kJ_per_mol>, "SiO2_replacement_alpha_quartz": <kJ_per_mol>, "MgO_replacement_M1_forsterite": <kJ_per_mol>, "MgO_replacement_M2_forsterite": <kJ_per_mol>, "MgO_replacement_MgO": <kJ_per_mol>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reaction_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_energies.json
- path: `/app/outputs/reaction_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON file containing all DFT total energies (eV) and the eight reaction energies (kJ/mol) computed from them. The hidden checker recomputes the reaction energies from the provided total energies and compares to the paper's reference values.
- schema:
  - `type`: object
  - `required`:
    - `total_energies`: object
    - `reaction_energies`: object
  - `items`:
    - `total_energies`:
      - `forsterite`: float (eV)
      - `MgO`: float (eV)
      - `alpha_quartz`: float (eV)
      - `H2O_isolated`: float (eV)
      - `forsterite_H2O_absorbed`: float (eV)
      - `MgO_H2O_absorbed`: float (eV)
      - `alpha_quartz_H2O_absorbed`: float (eV)
      - `forsterite_Si_vacancy`: float (eV)
      - `alpha_quartz_Si_vacancy`: float (eV)
      - `forsterite_Mg_vacancy_M1`: float (eV)
      - `forsterite_Mg_vacancy_M2`: float (eV)
      - `MgO_vacancy`: float (eV)
    - `reaction_energies`:
      - `water_absorption_forsterite`: float (kJ/mol)
      - `water_absorption_MgO`: float (kJ/mol)
      - `water_absorption_alpha_quartz`: float (kJ/mol)
      - `SiO2_replacement_forsterite`: float (kJ/mol)
      - `SiO2_replacement_alpha_quartz`: float (kJ/mol)
      - `MgO_replacement_M1_forsterite`: float (kJ/mol)
      - `MgO_replacement_M2_forsterite`: float (kJ/mol)
      - `MgO_replacement_MgO`: float (kJ/mol)

Notes: Total energies must be in eV; reaction energies in kJ/mol. The checker recomputes each reaction energy from the provided total energies using the paper's stoichiometric equations and compares the recomputed values against hidden gold tolerances and sign checks. Reward is the fraction of reaction energies within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "total_energies": "object",
          "reaction_energies": "object"
        },
        "items": {
          "total_energies": {
            "forsterite": "float (eV)",
            "MgO": "float (eV)",
            "alpha_quartz": "float (eV)",
            "H2O_isolated": "float (eV)",
            "forsterite_H2O_absorbed": "float (eV)",
            "MgO_H2O_absorbed": "float (eV)",
            "alpha_quartz_H2O_absorbed": "float (eV)",
            "forsterite_Si_vacancy": "float (eV)",
            "alpha_quartz_Si_vacancy": "float (eV)",
            "forsterite_Mg_vacancy_M1": "float (eV)",
            "forsterite_Mg_vacancy_M2": "float (eV)",
            "MgO_vacancy": "float (eV)"
          },
          "reaction_energies": {
            "water_absorption_forsterite": "float (kJ/mol)",
            "water_absorption_MgO": "float (kJ/mol)",
            "water_absorption_alpha_quartz": "float (kJ/mol)",
            "SiO2_replacement_forsterite": "float (kJ/mol)",
            "SiO2_replacement_alpha_quartz": "float (kJ/mol)",
            "MgO_replacement_M1_forsterite": "float (kJ/mol)",
            "MgO_replacement_M2_forsterite": "float (kJ/mol)",
            "MgO_replacement_MgO": "float (kJ/mol)"
          }
        }
      },
      "description": "JSON file containing all DFT total energies (eV) and the eight reaction energies (kJ/mol) computed from them. The hidden checker recomputes the reaction energies from the provided total energies and compares to the paper's reference values."
    }
  ],
  "notes": "Total energies must be in eV; reaction energies in kJ/mol. The checker recomputes each reaction energy from the provided total energies using the paper's stoichiometric equations and compares the recomputed values against hidden gold tolerances and sign checks. Reward is the fraction of reaction energies within tolerance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier in several stages:

1. The verifier reads your `reaction_energies.json` and checks that it contains all required total energy entries and all eight reaction energy entries, in the correct format.
2. Using the total energies you provided, the verifier recomputes each reaction energy according to the same stoichiometric definitions used by the study.
3. The recomputed reaction energies are compared to hidden reference values (derived from the original paper’s results). Each reaction energy that falls within a hidden tolerance earns a fraction of the total reward.
4. The final reward is the sum of scores across all reaction energies, yielding a value between 0 and 1. A higher reward corresponds to better agreement between your computed reaction energies and the expected reference values.
5. The verifier also checks that you have not simply copied the reference numbers: if your submitted total energies are inconsistent with your claimed reaction energies, or if no total energies are provided, you will receive a low score.

Accurate DFT calculations and correct stoichiometric derivation are essential to obtain a high score.
