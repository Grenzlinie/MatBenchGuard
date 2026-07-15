# DFT surface properties and adsorption trends of alkaline-earth metal oxides

## Problem background
Alkaline-earth metal oxides (MgO, CaO, SrO, BaO) in the rocksalt structure are model ionic solids. Understanding their surface stability and reactivity is crucial for applications in heterogeneous catalysis, where these materials serve as active components or supports. This work systematically computes bulk properties, surface energies of several low-index facets, and adsorption energies of small probe molecules across the whole series, employing multiple exchange-correlation functionals to map energetic trends and to benchmark the theoretical predictions.

## Approach
The investigation employs density functional theory (DFT) within the plane-wave pseudopotential framework, using the open-source Quantum ESPRESSO code. Six functionals spanning different rungs of DFT are applied: LDA, PBE, RPBE, PBEsol, BEEF-vdW, and the screened hybrid HSE. The computational protocol proceeds in stages: (1) Bulk properties (equilibrium lattice constant, bulk modulus, atomization energy, and HSE band gaps) are obtained from equation-of-state fits of rocksalt unit cells. (2) Symmetric slab models are built for the (100), (110), and the metal- and oxygen-terminated octopolar (111) surfaces; surface energies are extracted via the linearized (Fiorentini–Methfessel) method after relaxing the top layers. (3) Adsorption of CO, NO, CH₄, and H₂O on MgO(100) is studied at appropriate coverage, with adsorption energies defined as the difference between the total energy of the combined system and the sum of the clean slab and the gas-phase molecule. (4) The BEEF-vdW functional is then used to map CO and NO adsorption energies on the (100), (110), and (111)-M octopolar surfaces of all four oxides. (5) Oxygen chemistry is probed by computing atomic oxygen adsorption energies at the metal-oxygen-metal bridge site and neutral oxygen vacancy formation energies on the (100) surface, referencing gas-phase O₂. All computed values are finally aggregated into a structured JSON file.

## Reproduction target
Compute the following quantities for the rocksalt alkaline-earth metal oxides MgO, CaO, SrO, and BaO:
- Bulk lattice constant, bulk modulus, and atomization energy for each oxide with the functionals LDA, PBE, RPBE, PBEsol, BEEF-vdW, and HSE; additionally, HSE band gaps.
- Surface energies per 1×1 area for the (100), (110), M-oct (111), and O-oct (111) surfaces of each oxide with all six functionals.
- Adsorption energies of CO, NO, CH₄, and H₂O on the MgO(100) surface with the same set of functionals.
- Adsorption energies of CO and NO on the (100), (110), and (111)-M-oct surfaces of all four oxides using the BEEF-vdW functional.
- Oxygen adsorption energies at the MOM (metal-oxygen-metal bridge) site and neutral oxygen vacancy formation energies on the (100) surface of each oxide with all six functionals.

All computed values must be written into a single JSON file (`/app/outputs/computed_results.json`) that records, for each oxide/functional combination, the property name, numeric value, and unit. The workflow must also preserve the relative trends of the computed quantities across the oxide series.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org/
- PBE norm-conserving pseudopotentials (Mg, O): https://www.quantum-espresso.org/pseudopotentials/
- GTH pseudopotentials (Ca, Sr, Ba): https://www.quantum-espresso.org/pseudopotentials/
- BEEF-vdW functional: part of Quantum ESPRESSO (libxc implementation)
- HSE screened hybrid functional: part of Quantum ESPRESSO (exx module)

## Workflow steps

### Step 1: Bulk property calculations for AEMO series
- Role: process
- Action: Perform DFT total-energy calculations for bulk rocksalt MgO, CaO, SrO, BaO using functionals LDA, PBE, RPBE, PBEsol, BEEF-vdW, and HSE. For each oxide/functional, compute the equilibrium lattice constant a, bulk modulus M via equation-of-state fitting, and atomization energy (crystal minus isolated atoms). Additionally, compute band gaps from HSE calculations.
- Evidence: `/app/outputs/bulk_results_raw.json`

### Step 2: Surface energy calculations for stoichiometric surfaces
- Role: process
- Action: Build symmetric slab models for (100), (110), M-oct (111), and O-oct (111) surfaces of each oxide. For each functional, compute surface energies per 1x1 area using the linearized method (Fiorentini-Methfessel). Use slabs of appropriate thickness and vacuum; relax top layers.
- Evidence: `/app/outputs/surface_energies_raw.json`

### Step 3: MgO(100) adsorption energies
- Role: process
- Action: For the MgO(100) surface with a 4-layer slab and appropriate cell, compute adsorption energies of CO (on-top Mg), NO (tilted), CH4 (monolayer dipod configuration), and H2O (flat) using all functionals. Relax top layers and molecule, then calculate E_ads = E(slab+molecule) - E(slab) - E(molecule).
- Evidence: `/app/outputs/mgo100_adsorption_raw.json`

### Step 4: CO and NO adsorption energy mapping on AEMO surfaces
- Role: process
- Action: Using the BEEF-vdW functional, compute adsorption energies of CO and NO molecules on the on-top metal site of (100), (110), and (111)-M-oct surfaces for MgO, CaO, SrO, and BaO. Use 4-layer slabs with appropriate cells; relax top layers and adsorbate.
- Evidence: `/app/outputs/co_no_adsorption_raw.json`

### Step 5: Oxygen adsorption and vacancy formation energies
- Role: process
- Action: For the (100) surface of all four oxides, compute oxygen adsorption energies at the MOM (metal-oxygen-metal bridge) site and neutral oxygen vacancy formation energies using all functionals. Use 4-layer slabs with appropriate cells; reference is gas-phase O2.
- Evidence: `/app/outputs/oxygen_chemistry_raw.json`

### Step 6: Compile final computed results
- Role: scored (load-bearing)
- Action: Aggregate all computed quantities from previous steps into a single JSON file 'computed_results.json'. Each entry must contain oxide, functional, property, value, and unit, covering all required bulk, surface, adsorption, and oxygen chemistry properties. Only include properties that were computed in the earlier steps.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: JSON array of objects. Each object has keys: 'oxide' (string: MgO, CaO, SrO, BaO), 'functional' (string: LDA, PBE, RPBE, PBEsol, BEEF-vdW, HSE), 'property' (string, one of lattice_constant_A, bulk_modulus_GPa, atomization_energy_eV, band_gap_eV, surface_energy_100_eV_per_1x1, surface_energy_110_eV_per_1x1, surface_energy_111_Moct_eV_per_1x1, surface_energy_111_Ooct_eV_per_1x1, adsorption_energy_CO_MgO100_eV, adsorption_energy_NO_MgO100_eV, adsorption_energy_CH4_MgO100_eV, adsorption_energy_H2O_MgO100_eV, adsorption_energy_CO_on(100)_eV, adsorption_energy_NO_on(100)_eV, adsorption_energy_CO_on(110)_eV, adsorption_energy_NO_on(110)_eV, adsorption_energy_CO_on(111)_Moct_eV, adsorption_energy_NO_on(111)_Moct_eV, oxygen_adsorption_MOM_on(100)_eV, oxygen_vacancy_formation_on(100)_eV), 'value' (float), 'unit' (string). Include all properties computed for each applicable oxide/functional combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.json
- path: `/app/outputs/computed_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structured JSON file containing all computed DFT properties for bulk, surfaces, adsorption, and oxygen chemistry of AEMO series. The hidden checker compares each entry against reference data from the paper with tolerances and validates monotonic trends.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `oxide`, `functional`, `property`, `value`, `unit`
    - `properties`:
      - `oxide`:
        - `type`: string
        - `enum`: `MgO`, `CaO`, `SrO`, `BaO`
      - `functional`:
        - `type`: string
        - `enum`: `LDA`, `PBE`, `RPBE`, `PBEsol`, `BEEF-vdW`, `HSE`
      - `property`:
        - `type`: string
        - `enum`: `lattice_constant_A`, `bulk_modulus_GPa`, `atomization_energy_eV`, `band_gap_eV`, `surface_energy_100_eV_per_1x1`, `surface_energy_110_eV_per_1x1`, `surface_energy_111_Moct_eV_per_1x1`, `surface_energy_111_Ooct_eV_per_1x1`, `adsorption_energy_CO_MgO100_eV`, `adsorption_energy_NO_MgO100_eV`, `adsorption_energy_CH4_MgO100_eV`, `adsorption_energy_H2O_MgO100_eV`, `adsorption_energy_CO_on(100)_eV`, `adsorption_energy_NO_on(100)_eV`, `adsorption_energy_CO_on(110)_eV`, `adsorption_energy_NO_on(110)_eV`, `adsorption_energy_CO_on(111)_Moct_eV`, `adsorption_energy_NO_on(111)_Moct_eV`, `oxygen_adsorption_MOM_on(100)_eV`, `oxygen_vacancy_formation_on(100)_eV`
      - `value`:
        - `type`: number
      - `unit`:
        - `type`: string

Notes: The checker will reference hidden gold values from the paper for each property. It will apply tolerances appropriate for DFT reproduction (lattice constant ±0.05 Å, bulk modulus ±5 GPa, atomization energy ±0.5 eV, surface energy ±0.05 eV per 1x1, adsorption energy ±0.10 eV, band gap ±0.5 eV) and verify expected monotonic trends across the series.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "oxide",
            "functional",
            "property",
            "value",
            "unit"
          ],
          "properties": {
            "oxide": {
              "type": "string",
              "enum": [
                "MgO",
                "CaO",
                "SrO",
                "BaO"
              ]
            },
            "functional": {
              "type": "string",
              "enum": [
                "LDA",
                "PBE",
                "RPBE",
                "PBEsol",
                "BEEF-vdW",
                "HSE"
              ]
            },
            "property": {
              "type": "string",
              "enum": [
                "lattice_constant_A",
                "bulk_modulus_GPa",
                "atomization_energy_eV",
                "band_gap_eV",
                "surface_energy_100_eV_per_1x1",
                "surface_energy_110_eV_per_1x1",
                "surface_energy_111_Moct_eV_per_1x1",
                "surface_energy_111_Ooct_eV_per_1x1",
                "adsorption_energy_CO_MgO100_eV",
                "adsorption_energy_NO_MgO100_eV",
                "adsorption_energy_CH4_MgO100_eV",
                "adsorption_energy_H2O_MgO100_eV",
                "adsorption_energy_CO_on(100)_eV",
                "adsorption_energy_NO_on(100)_eV",
                "adsorption_energy_CO_on(110)_eV",
                "adsorption_energy_NO_on(110)_eV",
                "adsorption_energy_CO_on(111)_Moct_eV",
                "adsorption_energy_NO_on(111)_Moct_eV",
                "oxygen_adsorption_MOM_on(100)_eV",
                "oxygen_vacancy_formation_on(100)_eV"
              ]
            },
            "value": {
              "type": "number"
            },
            "unit": {
              "type": "string"
            }
          }
        }
      },
      "description": "Structured JSON file containing all computed DFT properties for bulk, surfaces, adsorption, and oxygen chemistry of AEMO series. The hidden checker compares each entry against reference data from the paper with tolerances and validates monotonic trends."
    }
  ],
  "notes": "The checker will reference hidden gold values from the paper for each property. It will apply tolerances appropriate for DFT reproduction (lattice constant ±0.05 Å, bulk modulus ±5 GPa, atomization energy ±0.5 eV, surface energy ±0.05 eV per 1x1, adsorption energy ±0.10 eV, band gap ±0.5 eV) and verify expected monotonic trends across the series."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. The verifier checks the numerical values in `computed_results.json` against reference data (obtained from the source paper) using tolerances appropriate for DFT reproduction, and it validates that certain expected monotonic trends across the AEMO series are present. Meeting or exceeding the reference earns full credit; there is no penalty for producing values that are more accurate than the paper's own. The final reward is a weighted average of the individual stage scores: roughly 50% weight on bulk and surface properties, 30% on the MgO(100) adsorption energies, and 20% on the oxygen chemistry results. Simply reporting numbers without executing the computational pipeline will yield a low or zero score because the verifier expects values that originate from the described DFT protocol.
