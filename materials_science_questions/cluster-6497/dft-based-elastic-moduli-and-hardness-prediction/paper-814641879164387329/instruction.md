# Validate 2NN MEAM potentials for Co-W and Al-W binary systems

## Problem background
Co-Al-W-based superalloys are of great interest for high-temperature applications, and their microstructure evolution is strongly influenced by interfacial properties between the γ-Co matrix and γ'-Co₃(Al,W) precipitates. Large-scale atomistic simulations of these interfaces require accurate interatomic potentials for the constituent binary systems. The 2NN modified embedded-atom method (MEAM) provides a common formalism capable of describing a wide range of elements and alloys simultaneously. This task validates published 2NN MEAM potential parameters for the Co-W and Al-W binary systems by computing fundamental physical properties of several intermetallic phases that appear in these systems.

## Approach
The 2NN MEAM total energy of a system is expressed as a sum of an embedding energy that depends on a background electron density and a pairwise interaction term, with a many-body screening function that includes interactions up to second-nearest neighbors. The pure-element potentials for Co (HCP), Al (FCC), and W (BCC) are fully specified by the parameters in Table 1. For the binary systems, the cross pair interaction is derived from a reference structure (L1₂ Co₃W for Co-W, and B1 AlW for Al-W) using its universal equation of state, which depends on cohesive energy, equilibrium nearest-neighbor distance, bulk modulus, and a model parameter. Additional screening parameters (C_min, C_max) and the relative electron density scaling factor (ρ₀ ratio) control alloy behavior. All necessary binary parameter values for Co-W and Al-W are given in Table 2. The validation approach consists of: constructing simulation cells for each target intermetallic phase, performing static energy minimization with cell relaxation to obtain equilibrium lattice constants and total energies, computing the reference energies of the pure elements in their ground-state structures, calculating formation enthalpies from the energy differences, and for Al₁₂W applying small strains and extracting stress components to determine the elastic constants C₁₁, C₁₂, C₄₄ and the bulk modulus.

## Reproduction target
Implement the 2NN MEAM potential using the provided pure-element (Table 1) and binary (Table 2) parameters, then perform static relaxations and energy calculations to determine: 1. equilibrium lattice parameters (a, c for hexagonal phases, a for cubic, a, b, c for monoclinic) for DO19 Co₃W, L1₂ Co₃W, Al₁₂W (cI26), Al₅W (hP12), and Al₄W (mC30); 2. formation enthalpies (kJ/(g·atom)) of each phase relative to the pure elements in their reference states (HCP Co, FCC Al, BCC W); 3. for Al₁₂W, the elastic constants C₁₁, C₁₂, C₄₄ and the bulk modulus B. Compile all results into the JSON file according to the output contract.

## Assets

- LAMMPS molecular dynamics package: https://lammps.sandia.gov/
- Pure-element and binary MEAM potential parameters

## Workflow steps

### Step 1: Prepare MEAM potential input files
- Role: process
- Action: Using the pure-element MEAM parameters (Table 1) and the binary parameters for Co-W and Al-W (Table 2) provided in the instruction, construct the MEAM potential files required by LAMMPS (or an equivalent MEAM implementation). This includes setting up the pair_coeff, mass, and potential file(s) for the two binary systems.
- Evidence: none

### Step 2: Run static relaxation for all target phases and reference elements
- Role: process
- Action: For each target phase: DO19 Co3W (P63/mmc), L12 Co3W (Pm-3m), Al12W (cI26), Al5W (hP12), Al4W (mC30), create a simulation cell with experimental starting lattice parameters, perform energy minimization allowing cell relaxation to obtain equilibrium lattice constants, total energies, and final atomic positions. Also compute the total energy of the pure elements (HCP Co, FCC Al, BCC W) using the same potentials.
- Evidence: none

### Step 3: Compute validation properties and write final scored JSON
- Role: scored (load-bearing)
- Action: From the relaxed data: (1) record equilibrium lattice parameters a, b, c (in Angstrom) for each phase; (2) calculate formation enthalpy (kJ/(g·atom)) as Hf = Etotal_compound − Σ(xi * Eref_i), where xi is atomic fraction and Eref_i is the energy per atom of element i in its pure reference state; (3) for Al12W, compute elastic constants C11, C12, C44 and bulk modulus B (GPa) using a strain-stress method. Compile all results into a single JSON file.
- Output file: `/app/outputs/calculated_properties.json`
- Format: json
- Contract: JSON object with keys: Co3W_DO19 (a, c, Hf), Co3W_L12 (a, Hf), Al12W (a, Hf, C11, C12, C44, B), Al5W (a, c, Hf), Al4W (a, b, c, Hf). All lengths in Angstrom, energies in kJ/(g·atom), elastic constants in GPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_properties.json
- path: `/app/outputs/calculated_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computationally validated physical properties of Co-W and Al-W intermetallic phases using the provided 2NN MEAM potentials.
- schema:
  - `type`: object
  - `required`: `Co3W_DO19`, `Co3W_L12`, `Al12W`, `Al5W`, `Al4W`
  - `properties`:
    - `Co3W_DO19`:
      - `type`: object
      - `required`: `a`, `c`, `Hf`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Angstrom
        - `c`:
          - `type`: number
          - `unit`: Angstrom
        - `Hf`:
          - `type`: number
          - `unit`: kJ/(g·atom)
    - `Co3W_L12`:
      - `type`: object
      - `required`: `a`, `Hf`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Angstrom
        - `Hf`:
          - `type`: number
          - `unit`: kJ/(g·atom)
    - `Al12W`:
      - `type`: object
      - `required`: `a`, `Hf`, `C11`, `C12`, `C44`, `B`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Angstrom
        - `Hf`:
          - `type`: number
          - `unit`: kJ/(g·atom)
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `B`:
          - `type`: number
          - `unit`: GPa
    - `Al5W`:
      - `type`: object
      - `required`: `a`, `c`, `Hf`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Angstrom
        - `c`:
          - `type`: number
          - `unit`: Angstrom
        - `Hf`:
          - `type`: number
          - `unit`: kJ/(g·atom)
    - `Al4W`:
      - `type`: object
      - `required`: `a`, `b`, `c`, `Hf`
      - `properties`:
        - `a`:
          - `type`: number
          - `unit`: Angstrom
        - `b`:
          - `type`: number
          - `unit`: Angstrom
        - `c`:
          - `type`: number
          - `unit`: Angstrom
        - `Hf`:
          - `type`: number
          - `unit`: kJ/(g·atom)

Notes: All values must be computed using the provided MEAM potentials. The checker compares each numeric field to the paper-reported MEAM values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Co3W_DO19",
          "Co3W_L12",
          "Al12W",
          "Al5W",
          "Al4W"
        ],
        "properties": {
          "Co3W_DO19": {
            "type": "object",
            "required": [
              "a",
              "c",
              "Hf"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Angstrom"
              },
              "c": {
                "type": "number",
                "unit": "Angstrom"
              },
              "Hf": {
                "type": "number",
                "unit": "kJ/(g·atom)"
              }
            }
          },
          "Co3W_L12": {
            "type": "object",
            "required": [
              "a",
              "Hf"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Angstrom"
              },
              "Hf": {
                "type": "number",
                "unit": "kJ/(g·atom)"
              }
            }
          },
          "Al12W": {
            "type": "object",
            "required": [
              "a",
              "Hf",
              "C11",
              "C12",
              "C44",
              "B"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Angstrom"
              },
              "Hf": {
                "type": "number",
                "unit": "kJ/(g·atom)"
              },
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "B": {
                "type": "number",
                "unit": "GPa"
              }
            }
          },
          "Al5W": {
            "type": "object",
            "required": [
              "a",
              "c",
              "Hf"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Angstrom"
              },
              "c": {
                "type": "number",
                "unit": "Angstrom"
              },
              "Hf": {
                "type": "number",
                "unit": "kJ/(g·atom)"
              }
            }
          },
          "Al4W": {
            "type": "object",
            "required": [
              "a",
              "b",
              "c",
              "Hf"
            ],
            "properties": {
              "a": {
                "type": "number",
                "unit": "Angstrom"
              },
              "b": {
                "type": "number",
                "unit": "Angstrom"
              },
              "c": {
                "type": "number",
                "unit": "Angstrom"
              },
              "Hf": {
                "type": "number",
                "unit": "kJ/(g·atom)"
              }
            }
          }
        }
      },
      "description": "Computationally validated physical properties of Co-W and Al-W intermetallic phases using the provided 2NN MEAM potentials."
    }
  ],
  "notes": "All values must be computed using the provided MEAM potentials. The checker compares each numeric field to the paper-reported MEAM values with appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each numeric field in your output JSON against a hidden reference derived from the paper's reported MEAM values. The verifier applies appropriate tolerances (absorbing expected numerical spread from independent implementations) and assigns a fraction of the total reward for each field that meets tolerance. The final score is the fraction of all required fields that are within tolerance. A correct reproduction requires executing the full workflow; simply reporting the paper's numbers without genuine computation will generally not satisfy the tolerances. You must produce exactly the file `/app/outputs/calculated_properties.json` as specified in the output contract.
