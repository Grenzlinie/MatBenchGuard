# LMTO-ASA cohesive properties of early actinide metals and oxides

## Problem background
Uranium dioxide ($\mathrm{UO}_2$) is the standard fuel for pressurized water reactors, and accurate knowledge of its cohesive properties—equilibrium lattice constants, bulk moduli, cohesive energies—is crucial for predicting in-reactor behaviour. The formation energy of oxygen vacancies, a key point defect, directly influences fuel stoichiometry and transport properties. Ab-initio electronic structure methods offer a predictive pathway to obtain these quantities. This task reproduces a linear muffin-tin orbital (LMTO) study in the atomic-sphere approximation (ASA) that computes the cohesive properties of $\mathrm{UO}_2$, $\mathrm{ThO}_2$, and the early actinide metals thorium, protoactinium, and uranium, as well as the formation energy of an oxygen vacancy in $\mathrm{UO}_2$.

## Approach
The LMTO-ASA method is a density-functional theory (DFT) band-structure technique that uses the atomic-sphere approximation and muffin-tin potentials. Two exchange-correlation functionals are applied: the local-density approximation (LDA) of von Barth–Hedin and the Langreth–Mehl gradient corrections (GC). For the metals (Th, Pa, U), total energies are computed as a function of volume for the fcc, bct, α‑U, and bcc crystal structures. Each energy–volume curve is fitted to an equation of state (e.g., Birch–Murnaghan) to extract the equilibrium atomic volume $V$, cohesive energy $E_\mathrm{coh}$, and bulk modulus $B$. For the oxides $\mathrm{UO}_2$ and $\mathrm{ThO}_2$, total energies are determined as a function of lattice parameter in the fluorite structure, with empty spheres placed at the octahedral sites to improve the ASA description. In $\mathrm{UO}_2$, uranium 5f orbitals are treated as valence states; in $\mathrm{ThO}_2$, 5f states are excluded from the valence. For the oxygen vacancy, a centro‑symmetric supercell containing 4 U, 7 O, and 4 empty spheres (O/U = 1.75) is constructed, and the vacancy formation energy is obtained from a total-energy difference. All computed properties are reported for both LDA and GC functionals where applicable.

## Reproduction target
Compute the following properties and write them to JSON files with the given schemas:

- For Th, Pa, and U metals (each in the fcc, bct, α‑U, and bcc phases) using LDA and GC: equilibrium atomic volume $V$ (Å³), cohesive energy $E_\mathrm{coh}$ (eV), and bulk modulus $B$ (GPa). Report values for both functionals for each element.
- For $\mathrm{UO}_2$ using LDA and GC: equilibrium lattice parameter $a_0$ (Å), bulk modulus $B$ (GPa), and cohesive energy $E_\mathrm{coh}$ (Ryd).
- For $\mathrm{ThO}_2$ using LDA and GC: equilibrium lattice parameter $a_0$ (Å), bulk modulus $B$ (GPa), and cohesive energy $E_\mathrm{coh}$ (Ryd).
- For an oxygen vacancy in $\mathrm{UO}_2$ (supercell with O/U = 1.75): formation energy (eV) using LDA.

## Assets

- LMTO-ASA electronic-structure code
- Crystal structure data for the metals and oxides

## Workflow steps

### Step 1: LMTO-ASA total-energy calculations for Th, Pa, U metals
- Role: scored (load-bearing)
- Action: Perform LMTO-ASA total-energy calculations for thorium, protoactinium, and uranium metals in the fcc, bct, α‑U, and bcc crystal structures using LDA (von Barth–Hedin) and Langreth–Mehl GC exchange-correlation functionals. For each element, compute total energy as a function of volume; fit each energy‑volume curve to an equation of state to extract the equilibrium atomic volume V, cohesive energy E_coh, and bulk modulus B. Report all extracted properties for both LDA and GC.
- Output file: `/app/outputs/metals_properties.json`
- Format: json
- Contract: Object with keys 'Th', 'Pa', 'U'; each value is an object with keys 'LDA' and 'GC'; each of those is an object with numeric keys 'V', 'Ecoh', 'B'.
- Scoring: scored by hidden verifier

### Step 2: LMTO-ASA total-energy calculations for UO2
- Role: scored
- Action: Perform LMTO-ASA total-energy calculations for uranium dioxide in the fluorite structure (including empty spheres). Use LDA and GC functionals. Compute total energy as a function of lattice parameter; extract equilibrium lattice parameter a0, bulk modulus B, and cohesive energy E_coh for both LDA and GC.
- Output file: `/app/outputs/uo2_properties.json`
- Format: json
- Contract: Object with keys 'LDA' and 'GC'; each value is an object with numeric keys 'a0', 'B', 'Ecoh'.
- Scoring: scored by hidden verifier

### Step 3: LMTO-ASA total-energy calculations for ThO2
- Role: scored
- Action: Perform LMTO-ASA total-energy calculations for thorium dioxide in the fluorite structure (5f states excluded from the valence). Use LDA and GC functionals. Compute total energy as a function of lattice parameter; extract equilibrium lattice parameter a0, bulk modulus B, and cohesive energy E_coh for both LDA and GC.
- Output file: `/app/outputs/tho2_properties.json`
- Format: json
- Contract: Object with keys 'LDA' and 'GC'; each value is an object with numeric keys 'a0', 'B', 'Ecoh'.
- Scoring: scored by hidden verifier

### Step 4: Oxygen vacancy formation energy in UO2
- Role: scored (load-bearing)
- Action: Build a centro‑symmetric supercell of UO2 with 4 U, 7 O atoms and 4 empty spheres (O/U = 1.75). Perform an LMTO-ASA total‑energy calculation with LDA. Compute the formation energy of an oxygen vacancy by taking the appropriate total‑energy difference. Report the result in eV.
- Output file: `/app/outputs/vacancy_formation_energy.json`
- Format: json
- Contract: Object with a single numeric key 'formation_energy'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/metals_properties.json`
- `/app/outputs/uo2_properties.json`
- `/app/outputs/tho2_properties.json`
- `/app/outputs/vacancy_formation_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### metals_properties.json
- path: `/app/outputs/metals_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium atomic volume V (Å³), cohesive energy E_coh (eV), and bulk modulus B (GPa) for Th, Pa, and U metals, computed with LDA and GC functionals.
- schema:
  - `type`: object
  - `required`:
    - `Th`: object
    - `Pa`: object
    - `U`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `Th.LDA.V`: Å³
    - `Th.LDA.Ecoh`: eV
    - `Th.LDA.B`: GPa
    - `Th.GC.V`: Å³
    - `Th.GC.Ecoh`: eV
    - `Th.GC.B`: GPa
    - `Pa.LDA.V`: Å³
    - `Pa.LDA.Ecoh`: eV
    - `Pa.LDA.B`: GPa
    - `Pa.GC.V`: Å³
    - `Pa.GC.Ecoh`: eV
    - `Pa.GC.B`: GPa
    - `U.LDA.V`: Å³
    - `U.LDA.Ecoh`: eV
    - `U.LDA.B`: GPa
    - `U.GC.V`: Å³
    - `U.GC.Ecoh`: eV
    - `U.GC.B`: GPa

### uo2_properties.json
- path: `/app/outputs/uo2_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice parameter a0 (Å), bulk modulus B (GPa), and cohesive energy E_coh (Ryd) for UO2, computed with LDA and GC functionals.
- schema:
  - `type`: object
  - `required`:
    - `LDA`: object
    - `GC`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `LDA.a0`: Å
    - `LDA.B`: GPa
    - `LDA.Ecoh`: Ryd
    - `GC.a0`: Å
    - `GC.B`: GPa
    - `GC.Ecoh`: Ryd

### tho2_properties.json
- path: `/app/outputs/tho2_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Lattice parameter a0 (Å), bulk modulus B (GPa), and cohesive energy E_coh (Ryd) for ThO2, computed with LDA and GC functionals.
- schema:
  - `type`: object
  - `required`:
    - `LDA`: object
    - `GC`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `LDA.a0`: Å
    - `LDA.B`: GPa
    - `LDA.Ecoh`: Ryd
    - `GC.a0`: Å
    - `GC.B`: GPa
    - `GC.Ecoh`: Ryd

### vacancy_formation_energy.json
- path: `/app/outputs/vacancy_formation_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Oxygen vacancy formation energy (eV) in a UO2 supercell with O/U = 1.75.
- schema:
  - `type`: object
  - `required`:
    - `formation_energy`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `formation_energy`: eV

Notes: All computed properties are physical quantities whose 'better' is undefined, scored by exact_match with hidden tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "metals_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Th": "object",
          "Pa": "object",
          "U": "object"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "Th.LDA.V": "Å³",
          "Th.LDA.Ecoh": "eV",
          "Th.LDA.B": "GPa",
          "Th.GC.V": "Å³",
          "Th.GC.Ecoh": "eV",
          "Th.GC.B": "GPa",
          "Pa.LDA.V": "Å³",
          "Pa.LDA.Ecoh": "eV",
          "Pa.LDA.B": "GPa",
          "Pa.GC.V": "Å³",
          "Pa.GC.Ecoh": "eV",
          "Pa.GC.B": "GPa",
          "U.LDA.V": "Å³",
          "U.LDA.Ecoh": "eV",
          "U.LDA.B": "GPa",
          "U.GC.V": "Å³",
          "U.GC.Ecoh": "eV",
          "U.GC.B": "GPa"
        }
      },
      "description": "Equilibrium atomic volume V (Å³), cohesive energy E_coh (eV), and bulk modulus B (GPa) for Th, Pa, and U metals, computed with LDA and GC functionals."
    },
    {
      "file": "uo2_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA": "object",
          "GC": "object"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "LDA.a0": "Å",
          "LDA.B": "GPa",
          "LDA.Ecoh": "Ryd",
          "GC.a0": "Å",
          "GC.B": "GPa",
          "GC.Ecoh": "Ryd"
        }
      },
      "description": "Lattice parameter a0 (Å), bulk modulus B (GPa), and cohesive energy E_coh (Ryd) for UO2, computed with LDA and GC functionals."
    },
    {
      "file": "tho2_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA": "object",
          "GC": "object"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "LDA.a0": "Å",
          "LDA.B": "GPa",
          "LDA.Ecoh": "Ryd",
          "GC.a0": "Å",
          "GC.B": "GPa",
          "GC.Ecoh": "Ryd"
        }
      },
      "description": "Lattice parameter a0 (Å), bulk modulus B (GPa), and cohesive energy E_coh (Ryd) for ThO2, computed with LDA and GC functionals."
    },
    {
      "file": "vacancy_formation_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "formation_energy": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "formation_energy": "eV"
        }
      },
      "description": "Oxygen vacancy formation energy (eV) in a UO2 supercell with O/U = 1.75."
    }
  ],
  "notes": "All computed properties are physical quantities whose 'better' is undefined, scored by exact_match with hidden tolerances."
}
```

## How you are scored
A hidden verifier independently reads each output file, extracts the reported numeric quantities, and compares them to hidden reference values. For each quantity, the absolute relative deviation from the reference is computed. Full credit is awarded when the deviation is within a prescribed tolerance, and the score decreases as the deviation grows beyond that tolerance. The reward is monotonic: smaller deviations always yield higher scores. The final overall reward is a weighted combination of the scores from all four output files, with the metals properties and vacancy formation energy carrying the highest weight. You must genuinely run the LMTO-ASA calculations; simply reporting numbers, even correct ones, is not sufficient without the corresponding evidence in the output files.
