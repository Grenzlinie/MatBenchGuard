# First-principles mechanical properties and stability analysis of hafnium oxide compounds

## Problem background
Hafnium oxide (HfO₂) and its suboxides are attractive candidates for hard coatings and high‑k dielectrics, yet the relationship between pressure‑induced stoichiometry, crystal structure, and mechanical properties remains an open computational question. Several novel Hf‑O phases have been predicted to become stable under pressure, and some are hypothesised to exhibit semimetallic electronic behaviour with low carrier densities. This task investigates whether these phases are dynamically stable at ambient pressure and what bulk modulus, shear modulus, Young’s modulus, Vickers hardness, and (for one candidate) electron and hole carrier densities they yield.

## Approach
The reproduction follows a first‑principles workflow based on density‑functional theory (DFT) within the PBE‑GGA approximation and the projector‑augmented wave (PAW) method. For each of the five target crystal structures, a geometry optimization is first performed to obtain the equilibrium lattice parameters and atomic positions. The dynamical stability of the relaxed structures is then examined by computing the phonon dispersion via the finite‑displacement method. Elastic constants are derived from the relaxed cells (e.g., by density‑functional perturbation theory or the stress–strain method) and are used to obtain the bulk modulus, shear modulus, and Young’s modulus through the Voigt–Reuss–Hill average; Vickers hardness is estimated from these elastic data using Chen’s empirical model. For one selected phase, a non‑self‑consistent band‑structure calculation is carried out along the high‑symmetry path Γ–M–K–Γ–A–L–H–A, and the resulting band energies are used to identify semimetallic character and to extract electron and hole carrier densities. All calculations are performed with the open‑source packages Quantum ESPRESSO (DFT engine) and Phonopy (phonon post‑processing).

## Reproduction target
Given the crystal structures (lattice parameters and atomic coordinates) of the five Hf‑O compounds **P‑62m‑HfO**, **Pnnm‑Hf₂O**, **Imm2‑Hf₅O₂**, **P‑31m‑Hf₂O**, and **P‑42m‑Hf₂O₃**, you must execute the DFT + phonon + elastic + band‑structure pipeline described above. Your main deliverables are:

1. **`mechanical_properties.json`** – a JSON array where each object contains:
   - `phase` (string)
   - `bulk_modulus_GPa` (float)
   - `shear_modulus_GPa` (float)
   - `young_modulus_GPa` (float)
   - `hardness_GPa` (float)
   - `phonon_stable` (boolean, `true` if no imaginary frequencies exist)
   For the phase **P‑62m‑HfO** the object must additionally contain:
   - `carrier_density_electrons_cm3` (float)
   - `carrier_density_holes_cm3` (float)

2. **`band_structure_P62m_HfO.dat`** – a plain‑text file with three whitespace‑separated columns: k‑point index (integer), band index (integer), and energy in eV relative to the Fermi level (set to 0 eV). The k‑points must follow the Γ–M–K–Γ–A–L–H–A path.

All results must be generated from your own calculations; simply copying numbers from a reference is not acceptable.

## Assets

- PAW pseudopotentials for Hf and O (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Quantum ESPRESSO: https://www.quantum-espresso.org
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: DFT Geometry Optimization of Hf-O Compounds
- Role: process
- Action: Perform DFT geometry optimization for the five Hf-O phases (P-62m-HfO, Pnnm-Hf2O, Imm2-Hf5O2, P-31m-Hf2O, P-42m-Hf2O3) using the provided initial crystal structures and PAW pseudopotentials from SSSP. Relax until forces are below an appropriate threshold. Document the relaxation in geo_opt.log.
- Evidence: `/app/outputs/geo_opt.log`

### Step 2: Phonon Stability Calculation
- Role: process
- Action: Using the relaxed structures from step 1, perform finite-displacement phonon calculations with Phonopy and DFT to compute phonon dispersion for each phase. Record the calculation in phonon.log.
- Evidence: `/app/outputs/phonon.log`

### Step 3: Elastic Constants Calculation
- Role: process
- Action: Compute the elastic stiffness tensor for each relaxed phase using density functional perturbation theory (DFPT) or the stress-strain method. Document the calculation in elastic.log.
- Evidence: `/app/outputs/elastic.log`

### Step 4: Electronic Band Structure Calculation for P-62m-HfO
- Role: process
- Action: Perform a non-self-consistent DFT calculation for P-62m-HfO along the high-symmetry path to obtain band energies. Document the calculation in band_calc.log.
- Evidence: `/app/outputs/band_calc.log`

### Step 5: Mechanical Properties and Stability Report
- Role: scored (load-bearing)
- Action: Using the elastic constants from step 3, compute bulk modulus (B), shear modulus (G), Young's modulus (E) via Voigt-Reuss-Hill scheme, and Vickers hardness (Hv) via Chen's model. Record phonon stability (absence of imaginary frequencies) from step 2. For P-62m-HfO, extract electron and hole carrier densities from the band structure obtained in step 4. Output all results as a JSON file: mechanical_properties.json.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: JSON array of objects, each with fields: phase (string), bulk_modulus_GPa (float), shear_modulus_GPa (float), young_modulus_GPa (float), hardness_GPa (float), phonon_stable (bool). For phase P-62m-HfO additionally: carrier_density_electrons_cm3 (float), carrier_density_holes_cm3 (float).
- Scoring: scored by hidden verifier

### Step 6: Semimetallic Band Structure File for P-62m-HfO
- Role: scored (load-bearing)
- Action: Write the band energies for P-62m-HfO to a text file: band_structure_P62m_HfO.dat, with columns: kpoint_index (integer), band_index (integer), energy (eV) relative to the Fermi level.
- Output file: `/app/outputs/band_structure_P62m_HfO.dat`
- Format: txt
- Contract: Text file with three columns separated by whitespace: kpoint_index (integer), band_index (integer), energy (float, eV). The Fermi energy is set to zero.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mechanical_properties.json`
- `/app/outputs/band_structure_P62m_HfO.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mechanical properties, phonon stability, and carrier densities for the five target Hf-O phases. The hidden checker compares these values against the paper's reported numbers with appropriate tolerances and cross-checks the hardness via Chen's model.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `phase`, `bulk_modulus_GPa`, `shear_modulus_GPa`, `young_modulus_GPa`, `hardness_GPa`, `phonon_stable`
    - `properties`:
      - `phase`:
        - `type`: string
      - `bulk_modulus_GPa`:
        - `type`: number
      - `shear_modulus_GPa`:
        - `type`: number
      - `young_modulus_GPa`:
        - `type`: number
      - `hardness_GPa`:
        - `type`: number
      - `phonon_stable`:
        - `type`: boolean
    - `additionalProperties`: True
  - `minItems`: 5

### band_structure_P62m_HfO.dat
- path: `/app/outputs/band_structure_P62m_HfO.dat`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Band energies for P-62m-HfO. The checker audits structural properties: existence of electron and hole pockets (bands crossing the Fermi level) indicating semimetallic character.
- schema:
  - `type`: text
  - `required_columns`: `kpoint_index`, `band_index`, `energy`

Notes: The solver must use open-source codes (Quantum ESPRESSO, Phonopy) and provided crystal structures. The checker does not require an external test set; gold values are derived from the paper's reported results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "phase",
            "bulk_modulus_GPa",
            "shear_modulus_GPa",
            "young_modulus_GPa",
            "hardness_GPa",
            "phonon_stable"
          ],
          "properties": {
            "phase": {
              "type": "string"
            },
            "bulk_modulus_GPa": {
              "type": "number"
            },
            "shear_modulus_GPa": {
              "type": "number"
            },
            "young_modulus_GPa": {
              "type": "number"
            },
            "hardness_GPa": {
              "type": "number"
            },
            "phonon_stable": {
              "type": "boolean"
            }
          },
          "additionalProperties": true
        },
        "minItems": 5
      },
      "description": "Mechanical properties, phonon stability, and carrier densities for the five target Hf-O phases. The hidden checker compares these values against the paper's reported numbers with appropriate tolerances and cross-checks the hardness via Chen's model."
    },
    {
      "file": "band_structure_P62m_HfO.dat",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required_columns": [
          "kpoint_index",
          "band_index",
          "energy"
        ]
      },
      "description": "Band energies for P-62m-HfO. The checker audits structural properties: existence of electron and hole pockets (bands crossing the Fermi level) indicating semimetallic character."
    }
  ],
  "notes": "The solver must use open-source codes (Quantum ESPRESSO, Phonopy) and provided crystal structures. The checker does not require an external test set; gold values are derived from the paper's reported results."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact and combines the stage scores (weighted) into a final reward between 0 and 1.

The mechanical properties JSON is checked for physical plausibility, self‑consistency, and agreement with reference values from the original study using tolerances that account for differences in DFT codes, pseudopotentials, and convergence settings. Phonon stability must be correctly identified for each phase. For the semimetallic candidate, the carrier densities are examined for consistency with the band‑structure evidence.

The band‑structure file is audited for structural evidence of semimetallic character – in particular, the presence of electron and hole pockets (bands crossing the Fermi level) at distinct high‑symmetry points. Simply listing expected values without executing the required computations will not pass. Adhere strictly to the declared output formats; files that deviate from the specification may receive reduced or zero credit.
