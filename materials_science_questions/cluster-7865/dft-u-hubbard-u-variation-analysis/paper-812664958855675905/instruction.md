# First-Principles Study of Oxygen Adsorption on BaO-Terminated Perovskite Surface

## Problem background
GdBaCo2O5.5 (GBCO) is a double perovskite cathode material for intermediate-temperature solid oxide fuel cells (IT-SOFCs). Understanding its electronic structure and oxygen surface interaction is essential for improving the oxygen reduction reaction (ORR) kinetics. Key properties include the magnetic ground state, bulk electronic properties, oxygen vacancy formation energies in different layers, and the energetics and charge transfer during O2 adsorption on the BaO-terminated (001) surface. First-principles density functional theory with on-site Coulomb repulsion (DFT+U) is a reliable method to compute these quantities.

## Approach
The work uses spin-polarized DFT+U (with a Hubbard U applied to Co d-orbitals) to investigate the material. The computational workflow includes: (i) screening magnetic configurations (ferromagnetic and antiferromagnetic variants) to identify the ground state; (ii) optimizing the bulk crystal structure and extracting lattice constants, Co magnetic moments, Bader charges, and the electronic band gap; (iii) calculating oxygen vacancy formation energies for the distinct oxygen sites by comparing total energies of perfect and defective supercells; (iv) constructing BaO-terminated (001) slab models for the perfect surface and one with a surface oxygen vacancy; (v) placing an O2 molecule at three high-symmetry adsorption sites (Ba-top, bridge, oxygen-top) on each surface, relaxing, and computing adsorption energies, Bader charge transfers, and O–O bond lengths. All calculations are performed with an open-source DFT code using PAW pseudopotentials.

## Reproduction target
Your task is to reproduce the key computed properties of GBCO using the above protocol. Specifically, you must (1) determine the most stable magnetic configuration; (2) compute and output the optimized bulk lattice constants, the magnetic moments and Bader charges for Co ions, and the GGA+U band gap; (3) compute the oxygen vacancy formation energies for the five distinct oxygen sites (O1–O5); (4) relax slab models for the perfect and defective surfaces; and (5) compute the O2 adsorption energies, Bader charges on the adsorbate and surface ions, and O–O bond lengths for the three adsorption sites on each surface, plus the Oa–vacancy distance on the defective surface. All results must be written to the specified output files (bulk_properties.json, vacancy_formation_energies.csv, perfect_adsorption_properties.csv, defective_adsorption_properties.csv) under /app/outputs. The assessment will compare your computed values against reference standards derived from the underlying study.

## Assets

- GdBaCo2O5.5 crystal structure (orthorhombic, Pmmm): https://doi.org/10.17188/1262675
- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/
- PAW pseudopotentials for Gd, Ba, Co, O: https://www.materialscloud.org/discover/sssp/table/efficiency
- Bader charge analysis tool: https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Magnetic ground state screening
- Role: process
- Action: Perform spin-polarized DFT+U total energy calculations for the four magnetic configurations (FM, A-AFM, C-AFM, G-AFM) of the bulk GBCO unit cell to confirm that G-AFM is the most stable. Record total energies for each configuration.
- Evidence: `/app/outputs/magnetic_energies.json`

### Step 2: Bulk geometry optimization and electronic structure
- Role: scored
- Action: Using the G-AFM magnetic ordering, optimize the lattice parameters of the orthorhombic bulk GBCO unit cell and compute Co magnetic moments, Bader charges, and the band gap (from GGA+U electronic structure). Output all results in bulk_properties.json.
- Output file: `/app/outputs/bulk_properties.json`
- Format: json
- Contract: {"lattice_constants": {"a": float, "b": float, "c": float, "volume": float}, "co_magnetic_moments": [{"label": "Co1_octa", "moment_muB": float}, {"label": "Co2_octa", "moment_muB": float}, {"label": "Co1_pyr", "moment_muB": float}, {"label": "Co2_pyr", "moment_muB": float}], "co_bader_charges": [{"label": "Co1_octa", "charge_e": float}, {"label": "Co2_octa", "charge_e": float}, {"label": "Co1_pyr", "charge_e": float}, {"label": "Co2_pyr", "charge_e": float}], "band_gap_GGA+U": float}
- Scoring: scored by hidden verifier

### Step 3: O2 molecule reference optimization
- Role: process
- Action: Optimize an isolated O2 molecule in a large supercell (e.g., 8×8×8 Å³) using spin-polarized DFT to obtain its total energy and equilibrium bond length. Record the total energy and bond length.
- Evidence: `/app/outputs/o2_reference.json`

### Step 4: Oxygen vacancy formation energies
- Role: scored
- Action: For each distinct oxygen site in the bulk supercell (O1...O5), remove one oxygen atom to create a vacancy, relax the defective supercell, and compute the formation energy using E_f = E(def) + 0.5*E(O2) – E(perf). Output all formation energies in vacancy_formation_energies.csv.
- Output file: `/app/outputs/vacancy_formation_energies.csv`
- Format: csv
- Contract: CSV with columns: site (string, e.g., O1, O2, O3, O4, O5), formation_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 5: Perfect BaO-terminated (001) slab relaxation
- Role: process
- Action: Construct a 6-plane BaO-terminated (001) slab with a P(1×2) supercell from the relaxed bulk structure, and perform a full geometry relaxation to obtain the clean perfect surface energy and structure.
- Evidence: `/app/outputs/perfect_slab_relaxed.pdb`

### Step 6: O2 adsorption on perfect GBCO (001) surface
- Role: scored (load-bearing)
- Action: Place an O2 molecule at 0.25 ML coverage on the relaxed perfect slab at three adsorption sites (Ba, Bridge, O). For each, relax the geometry and compute the adsorption energy (E_ads = E(slab+O2) – E(slab) – E(O2)), Bader charges on the two O atoms and selected surface ions (Ba*, O*, sub-surface Co), and the O–O bond length. Output all results in perfect_adsorption_properties.csv.
- Output file: `/app/outputs/perfect_adsorption_properties.csv`
- Format: csv
- Contract: CSV with columns: adsorption_site (Ba, Bridge, O), E_ads_eV, charge_Oa_e, charge_Ob_e, charge_Ba_star_e, charge_O_star_e, charge_Co_e, Oa_Ob_bond_length_A. Each row corresponds to one site.
- Scoring: scored by hidden verifier

### Step 7: Defective BaO-terminated (001) slab relaxation
- Role: process
- Action: Create a defective surface model by removing a surface oxygen atom from the perfect slab (creating a 12.5% defect concentration), and fully relax the slab.
- Evidence: `/app/outputs/defective_slab_relaxed.pdb`

### Step 8: O2 adsorption on defective GBCO (001) surface
- Role: scored (load-bearing)
- Action: Place an O2 molecule at 0.25 ML coverage on the relaxed defective slab at the same three adsorption sites (Ba, Bridge, O). For each, relax and compute the adsorption energy, Bader charges on Oa/Ob, Ba*, O*, Co, the O–O bond length, and the Oa–vacancy distance. Output all results in defective_adsorption_properties.csv.
- Output file: `/app/outputs/defective_adsorption_properties.csv`
- Format: csv
- Contract: CSV with columns: adsorption_site (Ba, Bridge, O), E_ads_eV, charge_Oa_e, charge_Ob_e, charge_Ba_star_e, charge_O_star_e, charge_Co_e, Oa_Ob_bond_length_A, Oa_vacancy_distance_A.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_properties.json`
- `/app/outputs/vacancy_formation_energies.csv`
- `/app/outputs/perfect_adsorption_properties.csv`
- `/app/outputs/defective_adsorption_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_properties.json
- path: `/app/outputs/bulk_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bulk lattice constants, Co magnetic moments, Bader charges, and band gap reproduced by the agent using G-AFM spin-polarized DFT+U.
- schema:
  - `type`: object
  - `required`: `lattice_constants`, `co_magnetic_moments`, `co_bader_charges`, `band_gap_GGA+U`
  - `properties`:
    - `lattice_constants`:
      - `a`: float (Å)
      - `b`: float (Å)
      - `c`: float (Å)
      - `volume`: float (Å³)
    - `co_magnetic_moments`: array of objects with label (string) and moment_muB (float)
    - `co_bader_charges`: array of objects with label (string) and charge_e (float)
    - `band_gap_GGA+U`: float (eV) or null

### vacancy_formation_energies.csv
- path: `/app/outputs/vacancy_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Oxygen vacancy formation energies for distinct oxygen sites in the bulk supercell, computed using E_f = E(def) + 0.5*E(O2) – E(perf).
- schema:
  - `type`: table
  - `required_columns`: `site`, `formation_energy_eV`
  - `column_types`:
    - `site`: string
    - `formation_energy_eV`: float

### perfect_adsorption_properties.csv
- path: `/app/outputs/perfect_adsorption_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies, Bader charges, and O–O bond lengths for O2 adsorbed at three sites on the perfect BaO-terminated (001) surface.
- schema:
  - `type`: table
  - `required_columns`: `adsorption_site`, `E_ads_eV`, `charge_Oa_e`, `charge_Ob_e`, `charge_Ba_star_e`, `charge_O_star_e`, `charge_Co_e`, `Oa_Ob_bond_length_A`
  - `column_types`:
    - `adsorption_site`: Ba, Bridge, or O
    - `E_ads_eV`: float
    - `charge_Oa_e`: float
    - `charge_Ob_e`: float
    - `charge_Ba_star_e`: float
    - `charge_O_star_e`: float
    - `charge_Co_e`: float
    - `Oa_Ob_bond_length_A`: float

### defective_adsorption_properties.csv
- path: `/app/outputs/defective_adsorption_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies, Bader charges, O–O bond lengths, and Oa–vacancy distance for O2 adsorbed at three sites on the defective BaO-terminated (001) surface with a surface oxygen vacancy.
- schema:
  - `type`: table
  - `required_columns`: `adsorption_site`, `E_ads_eV`, `charge_Oa_e`, `charge_Ob_e`, `charge_Ba_star_e`, `charge_O_star_e`, `charge_Co_e`, `Oa_Ob_bond_length_A`, `Oa_vacancy_distance_A`
  - `column_types`:
    - `adsorption_site`: Ba, Bridge, or O
    - `E_ads_eV`: float
    - `charge_Oa_e`: float
    - `charge_Ob_e`: float
    - `charge_Ba_star_e`: float
    - `charge_O_star_e`: float
    - `charge_Co_e`: float
    - `Oa_Ob_bond_length_A`: float
    - `Oa_vacancy_distance_A`: float

Notes: All scored artifacts will be compared to hidden paper-reported reference values with appropriate tolerances (T0 result-level comparison). The ordering of adsorption energies (Bridge most negative) and vacancy formation energies (O5 lowest) will be verified to ensure correct trends are reproduced. Load-bearing steps 06 and 08 force execution of the intermediate slab relaxation stages.

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
        "required": [
          "lattice_constants",
          "co_magnetic_moments",
          "co_bader_charges",
          "band_gap_GGA+U"
        ],
        "properties": {
          "lattice_constants": {
            "a": "float (Å)",
            "b": "float (Å)",
            "c": "float (Å)",
            "volume": "float (Å³)"
          },
          "co_magnetic_moments": "array of objects with label (string) and moment_muB (float)",
          "co_bader_charges": "array of objects with label (string) and charge_e (float)",
          "band_gap_GGA+U": "float (eV) or null"
        }
      },
      "description": "Bulk lattice constants, Co magnetic moments, Bader charges, and band gap reproduced by the agent using G-AFM spin-polarized DFT+U."
    },
    {
      "file": "vacancy_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "formation_energy_eV"
        ],
        "column_types": {
          "site": "string",
          "formation_energy_eV": "float"
        }
      },
      "description": "Oxygen vacancy formation energies for distinct oxygen sites in the bulk supercell, computed using E_f = E(def) + 0.5*E(O2) – E(perf)."
    },
    {
      "file": "perfect_adsorption_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "adsorption_site",
          "E_ads_eV",
          "charge_Oa_e",
          "charge_Ob_e",
          "charge_Ba_star_e",
          "charge_O_star_e",
          "charge_Co_e",
          "Oa_Ob_bond_length_A"
        ],
        "column_types": {
          "adsorption_site": "Ba, Bridge, or O",
          "E_ads_eV": "float",
          "charge_Oa_e": "float",
          "charge_Ob_e": "float",
          "charge_Ba_star_e": "float",
          "charge_O_star_e": "float",
          "charge_Co_e": "float",
          "Oa_Ob_bond_length_A": "float"
        }
      },
      "description": "Adsorption energies, Bader charges, and O–O bond lengths for O2 adsorbed at three sites on the perfect BaO-terminated (001) surface."
    },
    {
      "file": "defective_adsorption_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "adsorption_site",
          "E_ads_eV",
          "charge_Oa_e",
          "charge_Ob_e",
          "charge_Ba_star_e",
          "charge_O_star_e",
          "charge_Co_e",
          "Oa_Ob_bond_length_A",
          "Oa_vacancy_distance_A"
        ],
        "column_types": {
          "adsorption_site": "Ba, Bridge, or O",
          "E_ads_eV": "float",
          "charge_Oa_e": "float",
          "charge_Ob_e": "float",
          "charge_Ba_star_e": "float",
          "charge_O_star_e": "float",
          "charge_Co_e": "float",
          "Oa_Ob_bond_length_A": "float",
          "Oa_vacancy_distance_A": "float"
        }
      },
      "description": "Adsorption energies, Bader charges, O–O bond lengths, and Oa–vacancy distance for O2 adsorbed at three sites on the defective BaO-terminated (001) surface with a surface oxygen vacancy."
    }
  ],
  "notes": "All scored artifacts will be compared to hidden paper-reported reference values with appropriate tolerances (T0 result-level comparison). The ordering of adsorption energies (Bridge most negative) and vacancy formation energies (O5 lowest) will be verified to ensure correct trends are reproduced. Load-bearing steps 06 and 08 force execution of the intermediate slab relaxation stages."
}
```

## How you are scored
A hidden verifier inspects each scored artifact independently. It checks the lattice constants, magnetic moments, Bader charges, band gap, vacancy formation energies, and the adsorption properties (energies, charges, bond lengths). For each artifact, a stage-level score is computed based on how close your values are to the expected results (using tolerances appropriate for DFT+U calculations with an open-source code). The final reward is a weighted average of these stage scores, with the adsorption-property tables carrying the highest weight. You must perform the actual DFT calculations to obtain values; reporting numbers without evidence of the underlying workflow will not earn credit.
