# DFT Defect Formation Energy Calculations in CeO₂

## Problem background
Ceria (CeO₂) is a material widely used in catalysis and energy conversion. Its properties are strongly influenced by point defects—both intrinsic (vacancies, interstitials, electron/hole polarons) and extrinsic (hydrogen impurities, metal dopants such as Y, Cu, Ni). A quantitative understanding of defect formation energies and migration barriers is needed to predict how synthesis conditions (e.g., oxygen partial pressure) control defect populations and govern electronic and ionic transport. This task addresses that challenge by computing the relevant defect energetics from first principles.

## Approach
The computational protocol uses hybrid density‑functional theory (HSE06) within a plane‑wave pseudopotential framework to study defects in CeO₂. First, the bulk fluorite CeO₂ unit cell is relaxed to obtain the equilibrium lattice constant, band gap, and dielectric constants. A 324‑atom supercell is then used to model isolated point defects. Total energies of all relevant elemental and compound reference phases (e.g., Ce, Ce₂O₃, O₂, H₂O, CuO, NiO, Y₂O₃) are computed to derive atomic chemical potentials under two experimentally relevant conditions: condition A (oxidizing) with μ_O = −0.87 eV and condition B (highly reducing) with μ_O = −3.09 eV. For each native and extrinsic defect in multiple charge states, a supercell calculation is performed and the formation energy is expressed as a function of the Fermi level, corrected for finite‑size effects using standard alignment schemes. The intrinsic Fermi level is determined from the charge‑neutrality condition among the native defects. Finally, migration barriers for the electron polaron, oxygen vacancy, and hydrogen interstitial are estimated using DFT+U (U = 5 eV on Ce 4f) and the climbing‑image nudged elastic band (CI‑NEB) method, starting from the relaxed defect structures obtained in the formation‑energy calculations.

## Reproduction target
Compute, using an open‑source DFT code (e.g., Quantum ESPRESSO) with the HSE06 functional, the defect formation energies for native defects (electron polaron η_Ce⁻, oxygen vacancy V_O²⁺, and other native defects) and for hydrogen‑related and metal‑dopant defects (H_i⁺, H_O⁺, Y_Ce⁻, Cu_Ce²⁻, Ni_Ce²⁻, and relevant complexes) in a 324‑atom CeO₂ supercell under the two chemical‑potential conditions A (μ_O = −0.87 eV) and B (μ_O = −3.09 eV). Derive the intrinsic Fermi level from the native‑defect formation energies via charge neutrality, and report the formation energies of the key defects at that Fermi level. Additionally, compute the migration barriers of the electron polaron (η_Ce⁻), oxygen vacancy (V_O²⁺), and hydrogen interstitial (H_i⁺) using DFT+U and the CI‑NEB method. The overarching goal is to determine the stability ordering of the defects and the magnitude of the migration barriers under the specified conditions.

## Assets

- CeO₂ fluorite crystal structure: https://materialsproject.org/materials/mp-20194
- Crystal structures of elemental and compound reference phases: https://materialsproject.org/materials/ (mp-xxxx for Ce, Ce₂O₃, Cu, CuO, Ni, NiO, Y, Y₂O₃)
- SSSP pseudopotentials (PBE/HSE-optimized): https://www.materialscloud.org/discover/sssp/table/pbe
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Bulk CeO₂ reference calculation
- Role: scored
- Action: Perform HSE06 DFT calculations on the CeO₂ fluorite unit cell to obtain the equilibrium lattice constant, band gap, electronic/ionic dielectric constants, and the total energy of a perfect 324‑atom supercell (the reference for defect supercells). Output the key bulk properties.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: {"lattice_constant_A": float, "band_gap_eV": float, "static_dielectric_constant_electronic": float, "static_dielectric_constant_ionic": float, "total_energy_supercell_eV": float}
- Scoring: scored by hidden verifier

### Step 2: Reference phase total energies
- Role: process
- Action: Compute HSE06 total energies of elemental and compound reference phases (Ce, Ce₂O₃, Cu, CuO, Ni, NiO, Y, Y₂O₃) and isolated molecules (O₂, H₂, H₂O). Derive the atomic chemical potentials μ_i for each condition:

- For both conditions A and B: the Ce chemical potential is derived from the host phase CeO₂ (μ_Ce = E(CeO₂) − 2 μ_O).
- Condition A (μ_O = −0.87 eV): H from an isolated H₂O molecule, Y from Y₂O₃, Cu from CuO, Ni from NiO.
- Condition B (μ_O = −3.09 eV): H from an isolated H₂ molecule, Cu from elemental Cu, Ni from elemental Ni; Y still from Y₂O₃.

Output the derived chemical potentials as evidence.
- Evidence: `/app/outputs/chemical_potentials.json`

### Step 3: Native defect formation energies
- Role: scored (load-bearing)
- Action: For each native defect (V_O, O_i, V_Ce, Ce_i, electron polaron η_Ce⁻, hole polaron η_O⁺) in all relevant charge states, perform HSE06 DFT supercell calculations (324 atoms) and compute formation energies E^f as a function of Fermi level from VBM to CBM under conditions A and B, applying finite‑size corrections. Output the formation energy data, including the Fermi‑level values, for each condition.
- Output file: `/app/outputs/native_defect_formation_energies.csv`
- Format: csv
- Contract: Columns: condition (string), defect (string), charge (int), formation_energy_eV (float), fermi_level_eV (float)
- Scoring: scored by hidden verifier

### Step 4: Impurity and dopant formation energies
- Role: scored
- Action: Analogous to step 03, compute formation energies for hydrogen defects (H_i, H_O, and complexes) and metal dopants (Y, Cu, Ni: substitutional, interstitial, and complexes with oxygen vacancies) as a function of Fermi level under conditions A and B. Output the data in the same CSV format.
- Output file: `/app/outputs/impurity_dopant_formation_energies.csv`
- Format: csv
- Contract: Columns: condition (string), defect (string), charge (int), formation_energy_eV (float), fermi_level_eV (float)
- Scoring: scored by hidden verifier

### Step 5: Defect migration barriers
- Role: scored
- Action: Using the DFT+U method (U=5 eV on Ce 4f) and the climbing‑image NEB method, calculate migration barriers for the electron polaron (η_Ce⁻), oxygen vacancy (V_O²⁺), and hydrogen interstitial (H_i⁺). Use the final relaxed structures from the formation energy calculations as initial and final states.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: {"polaron_etaCe_minus_barrier_eV": float, "oxygen_vacancy_VO2plus_barrier_eV": float, "hydrogen_interstitial_Hi_plus_barrier_eV": float, "method": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/native_defect_formation_energies.csv`
- `/app/outputs/impurity_dopant_formation_energies.csv`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed bulk properties of CeO₂ from HSE06 DFT: lattice constant, band gap, electronic and ionic dielectric constants, and total energy of the 324-atom perfect supercell.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: float
    - `band_gap_eV`: float
    - `static_dielectric_constant_electronic`: float
    - `static_dielectric_constant_ionic`: float
    - `total_energy_supercell_eV`: float

### native_defect_formation_energies.csv
- path: `/app/outputs/native_defect_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Formation energy vs. Fermi level for native defects under conditions A and B. The checker will compute the intrinsic Fermi level from charge neutrality and compare the formation energies of key defects at that level to reference values.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `defect`, `charge`, `formation_energy_eV`, `fermi_level_eV`

### impurity_dopant_formation_energies.csv
- path: `/app/outputs/impurity_dopant_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Formation energy vs. Fermi level for hydrogen and metal dopant defects under conditions A and B. The checker will compare the formation energies of specific dopant configurations at the intrinsic Fermi level to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `defect`, `charge`, `formation_energy_eV`, `fermi_level_eV`

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed migration barriers for electron polaron, oxygen vacancy, and hydrogen interstitial using DFT+U/NEB. Values are compared to paper's reported barriers with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `polaron_etaCe_minus_barrier_eV`: float (eV)
    - `oxygen_vacancy_VO2plus_barrier_eV`: float (eV)
    - `hydrogen_interstitial_Hi_plus_barrier_eV`: float (eV)
    - `method`: string

Notes: The intrinsic Fermi level is not an explicit output; it is derived by the checker from the provided formation energy vs. Fermi level data. The agent must perform all DFT calculations using open-source code (e.g., Quantum ESPRESSO) with the HSE06 functional for formation energies and DFT+U (U=5 eV on Ce 4f) for migration barriers. Reference phase energies must be computed to derive the chemical potentials needed in the defect formation energy formula.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "float",
          "band_gap_eV": "float",
          "static_dielectric_constant_electronic": "float",
          "static_dielectric_constant_ionic": "float",
          "total_energy_supercell_eV": "float"
        }
      },
      "description": "Computed bulk properties of CeO₂ from HSE06 DFT: lattice constant, band gap, electronic and ionic dielectric constants, and total energy of the 324-atom perfect supercell."
    },
    {
      "file": "native_defect_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "defect",
          "charge",
          "formation_energy_eV",
          "fermi_level_eV"
        ]
      },
      "description": "Formation energy vs. Fermi level for native defects under conditions A and B. The checker will compute the intrinsic Fermi level from charge neutrality and compare the formation energies of key defects at that level to reference values."
    },
    {
      "file": "impurity_dopant_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "defect",
          "charge",
          "formation_energy_eV",
          "fermi_level_eV"
        ]
      },
      "description": "Formation energy vs. Fermi level for hydrogen and metal dopant defects under conditions A and B. The checker will compare the formation energies of specific dopant configurations at the intrinsic Fermi level to paper-reported values."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "polaron_etaCe_minus_barrier_eV": "float (eV)",
          "oxygen_vacancy_VO2plus_barrier_eV": "float (eV)",
          "hydrogen_interstitial_Hi_plus_barrier_eV": "float (eV)",
          "method": "string"
        }
      },
      "description": "Computed migration barriers for electron polaron, oxygen vacancy, and hydrogen interstitial using DFT+U/NEB. Values are compared to paper's reported barriers with tolerance."
    }
  ],
  "notes": "The intrinsic Fermi level is not an explicit output; it is derived by the checker from the provided formation energy vs. Fermi level data. The agent must perform all DFT calculations using open-source code (e.g., Quantum ESPRESSO) with the HSE06 functional for formation energies and DFT+U (U=5 eV on Ce 4f) for migration barriers. Reference phase energies must be computed to derive the chemical potentials needed in the defect formation energy formula."
}
```

## How you are scored
Your work is evaluated by a hidden automated verifier. It will examine each of the four scored output files (bulk_properties.json, native_defect_formation_energies.csv, impurity_dopant_formation_energies.csv, migration_barriers.json) and check that the computed quantities fall within scientifically reasonable tolerances relative to independently established reference values, and that essential structural trends (e.g., relative defect stability ordering) are correctly reproduced. Each artifact contributes a weight to the final reward, and the overall score is a weighted combination. Simply reporting a number without executing the full DFT workflow is not sufficient; the verifier expects artifact shapes and value ranges consistent with a genuine re‑computation.
