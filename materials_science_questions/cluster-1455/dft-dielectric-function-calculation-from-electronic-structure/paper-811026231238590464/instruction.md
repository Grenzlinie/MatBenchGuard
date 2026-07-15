# Phonon, Born effective charge, and dielectric tensor calculation for ZnSnP2

## Problem background
The ternary semiconductor ZnSnP2 crystallizes in the chalcopyrite structure and is a promising candidate for thin-film photovoltaics due to its direct band gap and high theoretical efficiency. Understanding its lattice-dynamical and dielectric properties—lattice constants, Born effective charges, zone-center phonon frequencies, and dielectric tensors—is essential for interpreting vibrational spectra and optimizing device performance. First-principles density-functional theory (DFT) and density-functional perturbation theory (DFPT) provide a direct route to compute these quantities from the fundamental crystal structure and pseudopotentials, without adjustable parameters. This task aims to reproduce such first-principles calculations and obtain the key structural, dielectric, and vibrational parameters of ZnSnP2.

## Approach
The calculations are performed with the open-source ABINIT package using the plane-wave pseudopotential method. The exchange-correlation functional is treated at the local-density approximation (LDA) level, and the electron-ion interaction is described by norm-conserving Troullier-Martins pseudopotentials for Zn, Sn, and P. The approach consists of two stages: (1) Structural optimization: the ground-state geometry is found by relaxing the lattice constants and internal coordinates until forces are sufficiently small. This yields the equilibrium tetragonal lattice parameters a and c, and the anion displacement parameter u. (2) Linear-response calculation: starting from the optimized structure, DFPT is used to compute the Born effective charge tensors for each atom, the high-frequency dielectric tensor, and the dynamical matrices on a q-point grid. From these, zone-center phonon frequencies are obtained, and for infrared-active modes the LO-TO splitting is extracted. The static dielectric tensor is then derived from the Lyddane-Sachs-Teller relation using the high-frequency tensor and the LO/TO frequencies.

## Reproduction target
Compute the relaxed lattice constants a, c, and internal parameter u of ZnSnP2 by performing a full DFT structural optimization with ABINIT, and write them to `/app/outputs/optimized_structure.json`. Then, using the optimized structure, compute the Born effective charge tensors for the Zn, Sn, and P atoms, the complete set of zone-center phonon frequencies (with mode symmetry labels and LO/TO frequencies where applicable), and the perpendicular and parallel components of the high-frequency and static dielectric tensors. Collect all results in `/app/outputs/results.json`. The output JSON files must follow the schemas described in the workflow steps and the output contract.

## Assets

- ABINIT: https://www.abinit.org/
- Troullier-Martins LDA pseudopotentials for Zn, Sn, and P: https://www.abinit.org/downloads/psp-tm

## Workflow steps

### Step 1: Structure optimization
- Role: scored
- Action: Perform DFT structural optimization of ZnSnP2 using ABINIT with norm-conserving LDA pseudopotentials. Start from the chalcopyrite structure with approximate experimental lattice parameters and relax all degrees of freedom until forces converge (e.g., below 5e-5 Ha/Bohr). Output the optimized lattice constants a, c, and internal parameter u.
- Output file: `/app/outputs/optimized_structure.json`
- Format: json
- Contract: {"type": "object", "properties": {"a": {"type": "number"}, "c": {"type": "number"}, "u": {"type": "number"}}, "required": ["a", "c", "u"]}
- Scoring: scored by hidden verifier

### Step 2: Phonon and dielectric properties calculation
- Role: scored (load-bearing)
- Action: Using the optimized structure, perform DFPT calculations with ABINIT. Compute Born effective charge tensors for each atom, the high-frequency dielectric tensor, dynamical matrices on a q-point grid, and derive zone-center phonon frequencies (with LO/TO splittings for polar modes) and static dielectric constants via the Lyddane-Sachs-Teller relation. Collect all computed quantities into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": ["born_effective_charges", "phonon_frequencies", "dielectric_tensors"], "properties": {"born_effective_charges": {"type": "object", "description": "Born effective charge tensors for Zn, Sn, P"}, "phonon_frequencies": {"type": "array", "items": {"type": "object", "properties": {"mode_label": {"type": "string"}, "symmetries": {"type": "array", "items": {"type": "string"}}, "activity": {"type": "string"}, "frequencies": {"type": "object", "properties": {"lo": {"type": "number"}, "to": {"type": "number"}}, "required": ["lo", "to"]}}, "required": ["mode_label", "frequencies"]}}, "dielectric_tensors": {"type": "object", "properties": {"epsilon_inf_perp": {"type": "number"}, "epsilon_inf_par": {"type": "number"}, "epsilon0_perp": {"type": "number"}, "epsilon0_par": {"type": "number"}}, "required": ["epsilon_inf_perp", "epsilon_inf_par", "epsilon0_perp", "epsilon0_par"]}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structure.json`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structure.json
- path: `/app/outputs/optimized_structure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice constants a (Å), c (Å), and internal parameter u.
- schema:
  - `type`: object
  - `required`: `a`, `c`, `u`
  - `properties`:
    - `a`:
      - `type`: number
    - `c`:
      - `type`: number
    - `u`:
      - `type`: number

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed Born effective charges, zone-center phonon frequencies (with LO/TO splittings for IR-active modes), and static/high-frequency dielectric constants.
- schema:
  - `type`: object
  - `required`: `born_effective_charges`, `phonon_frequencies`, `dielectric_tensors`
  - `properties`:
    - `born_effective_charges`:
      - `type`: object
      - `description`: Born effective charge tensors for Zn, Sn, and P; each tensor is a 3x3 matrix or a dictionary of its components.
    - `phonon_frequencies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `mode_label`:
            - `type`: string
          - `symmetries`:
            - `type`: array
            - `items`:
              - `type`: string
          - `activity`:
            - `type`: string
          - `frequencies`:
            - `type`: object
            - `properties`:
              - `lo`:
                - `type`: number
              - `to`:
                - `type`: number
            - `required`: `lo`, `to`
        - `required`: `mode_label`, `frequencies`
    - `dielectric_tensors`:
      - `type`: object
      - `properties`:
        - `epsilon_inf_perp`:
          - `type`: number
        - `epsilon_inf_par`:
          - `type`: number
        - `epsilon0_perp`:
          - `type`: number
        - `epsilon0_par`:
          - `type`: number
      - `required`: `epsilon_inf_perp`, `epsilon_inf_par`, `epsilon0_perp`, `epsilon0_par`

Notes: The agent must write both JSON files to /app/outputs. The hidden checker will compare the submitted numerical values to the paper's reported values with appropriate tolerances. Partial credit is awarded proportionally to the fraction of fields that pass within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "a",
          "c",
          "u"
        ],
        "properties": {
          "a": {
            "type": "number"
          },
          "c": {
            "type": "number"
          },
          "u": {
            "type": "number"
          }
        }
      },
      "description": "Relaxed lattice constants a (Å), c (Å), and internal parameter u."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "born_effective_charges",
          "phonon_frequencies",
          "dielectric_tensors"
        ],
        "properties": {
          "born_effective_charges": {
            "type": "object",
            "description": "Born effective charge tensors for Zn, Sn, and P; each tensor is a 3x3 matrix or a dictionary of its components."
          },
          "phonon_frequencies": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "mode_label": {
                  "type": "string"
                },
                "symmetries": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "activity": {
                  "type": "string"
                },
                "frequencies": {
                  "type": "object",
                  "properties": {
                    "lo": {
                      "type": "number"
                    },
                    "to": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "lo",
                    "to"
                  ]
                }
              },
              "required": [
                "mode_label",
                "frequencies"
              ]
            }
          },
          "dielectric_tensors": {
            "type": "object",
            "properties": {
              "epsilon_inf_perp": {
                "type": "number"
              },
              "epsilon_inf_par": {
                "type": "number"
              },
              "epsilon0_perp": {
                "type": "number"
              },
              "epsilon0_par": {
                "type": "number"
              }
            },
            "required": [
              "epsilon_inf_perp",
              "epsilon_inf_par",
              "epsilon0_perp",
              "epsilon0_par"
            ]
          }
        }
      },
      "description": "Computed Born effective charges, zone-center phonon frequencies (with LO/TO splittings for IR-active modes), and static/high-frequency dielectric constants."
    }
  ],
  "notes": "The agent must write both JSON files to /app/outputs. The hidden checker will compare the submitted numerical values to the paper's reported values with appropriate tolerances. Partial credit is awarded proportionally to the fraction of fields that pass within tolerance."
}
```

## How you are scored
A hidden verifier will read the two output files you produce and compare the numerical values to reference values. Each field is checked independently, with tolerances that account for typical numerical noise and methodological variations. The final score is a weighted sum of the fraction of fields that pass the tolerance check: structural parameters, Born effective charge components, phonon frequencies, and dielectric constants. To earn full credit you must run the full DFT and DFPT workflow; reporting approximate numbers without genuine computation will fail.
