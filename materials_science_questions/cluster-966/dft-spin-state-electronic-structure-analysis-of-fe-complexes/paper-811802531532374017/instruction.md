# DFT electronic structure analysis of dinitrosyl iron complexes

## Problem background
The electronic structure of dinitrosyl iron complexes (DNICs) has been debated. The present work uses density functional theory (DFT) to resolve the ground-state spin, electronic configuration, and bonding in the {Fe(NO)2}^9 and {Fe(NO)2}^10 cores. The aim is to compute key properties—optimized geometries, Mössbauer parameters, NO stretching frequencies, spin distributions, and orbital overlaps—and to determine the nature of the metal–ligand coupling from the Kohn–Sham molecular orbitals.

## Approach
Spin-unrestricted DFT calculations are performed with the TPSSh functional and a triple-zeta basis set (e.g., def2-TZVP). For both species, 1 ({Fe(NO)2}^9) and 2 ({Fe(NO)2}^10), the molecular geometries are first fully optimized. From the converged structures, harmonic vibrational frequencies are computed to confirm stationary points and extract the NO stretching frequencies, and Mössbauer isomer shifts and quadrupole splittings are predicted. The Kohn–Sham orbital structure is then analyzed: Mulliken (or Löwdin) spin populations are obtained for the iron center and each NO ligand; the spatial overlap integrals for the strongly spin-coupled Fe–NO orbital pairs are averaged; and the occupation numbers of the spin-up and spin-down manifolds are used to count the singly occupied Fe-3d and NO-π* based molecular orbitals. These quantities allow the assignment of the effective spin state of the metal and the ligands.

## Reproduction target
Starting from the published crystal structures of complexes 1 and 2 (see Assets), perform the DFT workflow described above and compile the following results into a single file: `/app/outputs/computed_results.json`. The file must contain, for each species, the optimized bond lengths (Fe–N(nacnac), Fe–N(NO), N–O) in Å, the Mössbauer isomer shift δ (in mm/s) and quadrupole splitting |ΔEQ| (in mm/s), the symmetric and asymmetric NO stretching frequencies (in cm⁻¹), the Fe spin population and the two NO spin populations, the average spatial overlap integral S for the four spin-coupled Fe–NO orbital pairs, the number of singly occupied Fe-3d based MOs in the spin-up manifold, the number of singly occupied NO-π* based MOs in the spin-down manifold, and the deduced Fe spin-state description (e.g., "HS Fe(III) S=5/2").

## Assets

- Crystal structures of {Fe(NO)2}9 (1) and {Fe(NO)2}10 (2): 10.1021/ja902031q
- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- def2-TZVP basis set: bundled with ORCA or downloadable from Basis Set Exchange (https://www.basissetexchange.org/)

## Workflow steps

### Step 1: Prepare input structures
- Role: process
- Action: Obtain the crystal structures of complexes 1 and 2 from the literature (DOI: 10.1021/ja902031q) and create geometry input files suitable for DFT optimization in the chosen quantum chemistry code.
- Evidence: none

### Step 2: TPSSh DFT geometry optimization and property calculation
- Role: process
- Action: For both species 1 and 2, perform spin-unrestricted DFT geometry optimization using the TPSSh functional and a triple-zeta basis set (e.g., def2-TZVP). After optimization, compute harmonic vibrational frequencies to verify stationary points and obtain NO stretching frequencies, and run a single-point Mössbauer parameter calculation with the same functional and basis. Retain the converged Kohn–Sham orbitals and overlap matrix for subsequent analysis.
- Evidence: none

### Step 3: Extract computed properties and electronic structure quantities
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract and organize the following into a single structured JSON file: optimized bond lengths (Fe–N(nacnac), Fe–N(NO), N–O) for each complex; Mössbauer isomer shift δ and quadrupole splitting |ΔEQ|; symmetric and asymmetric NO stretching frequencies; Mulliken (or Löwdin) spin populations on Fe and on each NO; the average spatial overlap integral S for the four strongly spin-coupled Fe–NO orbital pairs; number of singly occupied Fe-3d based molecular orbitals in the spin-up manifold; number of singly occupied NO-π* based molecular orbitals in the spin-down manifold; and the deduced Fe and ligand spin-state assignments.
- Output file: `/app/outputs/computed_results.json`
- Format: json
- Contract: {
  "species1": {
    "Fe_N_nacnac": [float, float],
    "Fe_N_NO": [float, float],
    "N_O": [float, float],
    "delta_mm_per_s": float,
    "DeltaEQ_mm_per_s": float,
    "v_NO_sym_cm-1": float,
    "v_NO_asym_cm-1": float,
    "Fe_spin_population": float,
    "NO_spin_populations": [float, float],
    "orbital_overlap_S": float,
    "Fe_S_values": ["string"],
    "num_singly_occupied_Fe_d_orbitals": int,
    "num_singly_occupied_NO_pi_orbitals": int
  },
  "species2": {
    "Fe_N_nacnac": [float, float],
    "Fe_N_NO": [float, float],
    "N_O": [float, float],
    "delta_mm_per_s": float,
    "DeltaEQ_mm_per_s": float,
    "v_NO_sym_cm-1": float,
    "v_NO_asym_cm-1": float,
    "Fe_spin_population": float,
    "NO_spin_populations": [float, float],
    "orbital_overlap_S": float,
    "Fe_S_values": ["string"],
    "num_singly_occupied_Fe_d_orbitals": int,
    "num_singly_occupied_NO_pi_orbitals": int
  }
}
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
- description: Structured JSON containing all key numerical results and electronic structure interpretation for both {Fe(NO)2}9 (1) and {Fe(NO)2}10 (2) complexes. Each field is checked against the hidden reference values derived from the paper's reported data with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `species1`, `species2`
  - `properties`:
    - `species1`:
      - `type`: object
      - `required`: `Fe_N_nacnac`, `Fe_N_NO`, `N_O`, `delta_mm_per_s`, `DeltaEQ_mm_per_s`, `v_NO_sym_cm-1`, `v_NO_asym_cm-1`, `Fe_spin_population`, `NO_spin_populations`, `orbital_overlap_S`, `Fe_S_values`, `num_singly_occupied_Fe_d_orbitals`, `num_singly_occupied_NO_pi_orbitals`
      - `properties`:
        - `Fe_N_nacnac`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `Fe_N_NO`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `N_O`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `delta_mm_per_s`:
          - `type`: number
        - `DeltaEQ_mm_per_s`:
          - `type`: number
        - `v_NO_sym_cm-1`:
          - `type`: number
        - `v_NO_asym_cm-1`:
          - `type`: number
        - `Fe_spin_population`:
          - `type`: number
        - `NO_spin_populations`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `orbital_overlap_S`:
          - `type`: number
        - `Fe_S_values`:
          - `type`: array
          - `items`:
            - `type`: string
          - `minItems`: 1
        - `num_singly_occupied_Fe_d_orbitals`:
          - `type`: integer
        - `num_singly_occupied_NO_pi_orbitals`:
          - `type`: integer
    - `species2`:
      - `type`: object
      - `required`: `Fe_N_nacnac`, `Fe_N_NO`, `N_O`, `delta_mm_per_s`, `DeltaEQ_mm_per_s`, `v_NO_sym_cm-1`, `v_NO_asym_cm-1`, `Fe_spin_population`, `NO_spin_populations`, `orbital_overlap_S`, `Fe_S_values`, `num_singly_occupied_Fe_d_orbitals`, `num_singly_occupied_NO_pi_orbitals`
      - `properties`:
        - `Fe_N_nacnac`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `Fe_N_NO`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `N_O`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `delta_mm_per_s`:
          - `type`: number
        - `DeltaEQ_mm_per_s`:
          - `type`: number
        - `v_NO_sym_cm-1`:
          - `type`: number
        - `v_NO_asym_cm-1`:
          - `type`: number
        - `Fe_spin_population`:
          - `type`: number
        - `NO_spin_populations`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 2
          - `maxItems`: 2
        - `orbital_overlap_S`:
          - `type`: number
        - `Fe_S_values`:
          - `type`: array
          - `items`:
            - `type`: string
          - `minItems`: 1
        - `num_singly_occupied_Fe_d_orbitals`:
          - `type`: integer
        - `num_singly_occupied_NO_pi_orbitals`:
          - `type`: integer

Notes: The output file must contain all fields exactly as specified in the schema. Bond lengths are in Å, isomer shift and quadrupole splitting in mm/s, frequencies in cm^-1. Spin populations are Mulliken or Löwdin populations. Overlap S is the average over the four spin-coupled orbital pairs. Fe_S_values is an array of strings describing the Fe spin state (e.g., "HS Fe(III) S=5/2").

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
        "type": "object",
        "required": [
          "species1",
          "species2"
        ],
        "properties": {
          "species1": {
            "type": "object",
            "required": [
              "Fe_N_nacnac",
              "Fe_N_NO",
              "N_O",
              "delta_mm_per_s",
              "DeltaEQ_mm_per_s",
              "v_NO_sym_cm-1",
              "v_NO_asym_cm-1",
              "Fe_spin_population",
              "NO_spin_populations",
              "orbital_overlap_S",
              "Fe_S_values",
              "num_singly_occupied_Fe_d_orbitals",
              "num_singly_occupied_NO_pi_orbitals"
            ],
            "properties": {
              "Fe_N_nacnac": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "Fe_N_NO": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "N_O": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "delta_mm_per_s": {
                "type": "number"
              },
              "DeltaEQ_mm_per_s": {
                "type": "number"
              },
              "v_NO_sym_cm-1": {
                "type": "number"
              },
              "v_NO_asym_cm-1": {
                "type": "number"
              },
              "Fe_spin_population": {
                "type": "number"
              },
              "NO_spin_populations": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "orbital_overlap_S": {
                "type": "number"
              },
              "Fe_S_values": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "minItems": 1
              },
              "num_singly_occupied_Fe_d_orbitals": {
                "type": "integer"
              },
              "num_singly_occupied_NO_pi_orbitals": {
                "type": "integer"
              }
            }
          },
          "species2": {
            "type": "object",
            "required": [
              "Fe_N_nacnac",
              "Fe_N_NO",
              "N_O",
              "delta_mm_per_s",
              "DeltaEQ_mm_per_s",
              "v_NO_sym_cm-1",
              "v_NO_asym_cm-1",
              "Fe_spin_population",
              "NO_spin_populations",
              "orbital_overlap_S",
              "Fe_S_values",
              "num_singly_occupied_Fe_d_orbitals",
              "num_singly_occupied_NO_pi_orbitals"
            ],
            "properties": {
              "Fe_N_nacnac": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "Fe_N_NO": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "N_O": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "delta_mm_per_s": {
                "type": "number"
              },
              "DeltaEQ_mm_per_s": {
                "type": "number"
              },
              "v_NO_sym_cm-1": {
                "type": "number"
              },
              "v_NO_asym_cm-1": {
                "type": "number"
              },
              "Fe_spin_population": {
                "type": "number"
              },
              "NO_spin_populations": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 2,
                "maxItems": 2
              },
              "orbital_overlap_S": {
                "type": "number"
              },
              "Fe_S_values": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "minItems": 1
              },
              "num_singly_occupied_Fe_d_orbitals": {
                "type": "integer"
              },
              "num_singly_occupied_NO_pi_orbitals": {
                "type": "integer"
              }
            }
          }
        }
      },
      "description": "Structured JSON containing all key numerical results and electronic structure interpretation for both {Fe(NO)2}9 (1) and {Fe(NO)2}10 (2) complexes. Each field is checked against the hidden reference values derived from the paper's reported data with appropriate tolerances."
    }
  ],
  "notes": "The output file must contain all fields exactly as specified in the schema. Bond lengths are in Å, isomer shift and quadrupole splitting in mm/s, frequencies in cm^-1. Spin populations are Mulliken or Löwdin populations. Overlap S is the average over the four spin-coupled orbital pairs. Fe_S_values is an array of strings describing the Fe spin state (e.g., \"HS Fe(III) S=5/2\")."
}
```

## How you are scored
A hidden verifier checks the submitted `computed_results.json` against reference data for each field. Numerical quantities (bond lengths, Mössbauer parameters, frequencies, spin populations, and overlap integrals) are compared to expected values with tolerances that account for reasonable method and implementation variations. The spin-state strings and orbital counts are validated against the reported spin populations and occupations. The final reward is a weighted combination of the scores for each field; reporting the literature values without having run the DFT calculations is not sufficient to pass.
