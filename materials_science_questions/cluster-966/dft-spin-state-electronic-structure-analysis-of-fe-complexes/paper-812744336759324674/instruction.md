# Ligand-field spin-orbit diagonalization for Fe3+ zero-field splitting in cubic crystals

## Problem background
The ground-state zero-field splitting of the Fe³⁺ ion (3d⁵) in cubic (octahedral) environments provides key insight into the interplay between ligand-field and spin-orbit interactions. EPR spectra and optical d-d transitions of Fe³⁺ in crystals such as Fe(H₂O)₆³⁺, beryl, and MgO:Fe³⁺ are sensitive to the zero-field splitting parameter 3a, but its computation requires a full diagonalization of the combined ligand-field plus spin-orbit-coupling Hamiltonian. The parameter 3a can be extracted from the ground-state multiplet splitting, and its dependence on the sign of the crystal-field parameter Dq reveals fundamental symmetry properties of the d⁵ configuration.

## Approach
Construct and diagonalize the complete Hamiltonian matrix for the 3d⁵ configuration in octahedral symmetry using standard Racah (B, C) and crystal-field (Dq) parametrizations, augmented by the Trees correction (α) and spin-orbit coupling (ζ). All matrix elements are built from the appropriate basis states of the d⁵ manifold. Diagonalization yields the energy eigenvalues, from which d-d transition energies (differences between the five lowest excited states and the ground state) and the ground-state zero-field splitting 3a are extracted. The computation is repeated for multiple sets of free-ion and crystal-field parameters to cover the three experimental crystals and to test the inequality (3a)_{+Dq} > (3a)_{-Dq} across four representative parameter combinations. The entire implementation relies on open-source numerical libraries (numpy, scipy).

## Reproduction target
Produce two scored JSON artifacts by implementing the full Hamiltonian diagonalization:

1. For the crystals Fe(H₂O)₆³⁺, beryl, and MgO:Fe³⁺, using fixed parameters B=730 cm⁻¹, C=3150 cm⁻¹, α=90 cm⁻¹, ζ=420 cm⁻¹, and Dq=1350, 1400, and 1500 cm⁻¹ respectively, report the five lowest d-d transition energies and the zero-field splitting parameter 10³(3a) (i.e., 3a multiplied by 1000) for each Dq value.

2. For the four parameter sets with both positive and negative Dq:
   - Set 1: B=730, C=3150, α=90, ζ=300, Dq=±1350
   - Set 2: B=730, C=3150, α=90, ζ=420, Dq=±1350
   - Set 3: B=1100, C=4000, α=90, ζ=440, Dq=±2150
   - Set 4: B=1100, C=4000, α=0, ζ=440, Dq=±2150
   report 10³(3a) for the positive-Dq and negative-Dq cases, and verify that for every parameter set the zero-field splitting for positive Dq is strictly larger than for negative Dq.

All energies are in cm⁻¹. The output files must follow the exact JSON schemas specified in the workflow steps and output contract.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Diagonalize the complete ligand-field plus spin-orbit-coupling Hamiltonian for all parameter sets
- Role: process
- Action: Construct the full Hamiltonian matrix for the d5 configuration in octahedral symmetry for the following parameter combinations: (B=730, C=3150, alpha=90, zeta=420, Dq=1350, 1400, 1500); for the signed-Dq sets: (B=730, C=3150, alpha=90, zeta=300, Dq=±1350); (B=730, C=3150, alpha=90, zeta=420, Dq=±1350); (B=1100, C=4000, alpha=90, zeta=440, Dq=±2150); (B=1100, C=4000, alpha=0, zeta=440, Dq=±2150). Diagonalize each matrix and save the full set of eigenvalues (in cm^{-1}) for each case to eigenvalues.json. This file must be readable by downstream scored steps.
- Evidence: `/app/outputs/eigenvalues.json`

### Step 2: Extract d-d transition energies and zero-field splitting for primary crystals
- Role: scored (load-bearing)
- Action: From the eigenvalues for the three primary parameter sets (Dq=1350,1400,1500 with B=730, C=3150, alpha=90, zeta=420), identify the ground-state energy and the five lowest excited-state energies. Compute the d-d transition energies (excited minus ground) in cm^{-1}. Extract the ground-state zero-field splitting parameter 3a (in cm^{-1}) and report it as 10^3(3a) (i.e., the value of 3a multiplied by 1000). Save the results to dd_zfs_results.json. The output must contain the exact keys and structure specified in the output contract.
- Output file: `/app/outputs/dd_zfs_results.json`
- Format: json
- Contract: {"Dq_1350": {"dd_transitions": [number, ...], "zfs_1e3_3a": number}, "Dq_1400": {"dd_transitions": [number, ...], "zfs_1e3_3a": number}, "Dq_1500": {"dd_transitions": [number, ...], "zfs_1e3_3a": number}}
- Scoring: scored by hidden verifier

### Step 3: Compute zero-field splitting for positive and negative Dq to verify sign inequality
- Role: scored
- Action: From the eigenvalues for the four parameter sets with ±Dq (as defined in step_01), extract the ground-state zero-field splitting parameter 3a and report it as 10^3(3a) (3a multiplied by 1000, in cm^{-1}) for each case. Save the results to signed_zfs_results.json. The output must contain the exact keys and structure specified in the output contract.
- Output file: `/app/outputs/signed_zfs_results.json`
- Format: json
- Contract: {"set1": {"Dq_pos": {"param": {"B": number, "C": number, "alpha": number, "zeta": number, "Dq": number}, "zfs": number}, "Dq_neg": {"param": {"B": number, "C": number, "alpha": number, "zeta": number, "Dq": number}, "zfs": number}}, "set2": {...}, "set3": {...}, "set4": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dd_zfs_results.json`
- `/app/outputs/signed_zfs_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dd_zfs_results.json
- path: `/app/outputs/dd_zfs_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed d-d transition energies (five lowest excited-state energies relative to ground, in cm^{-1}) and the zero-field splitting parameter 10^3(3a) (in cm^{-1}) for three representative crystals. The hidden checker compares these values against reference gold values from the literature with appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Dq_1350`: object
    - `Dq_1400`: object
    - `Dq_1500`: object
  - `items`:
    - `Dq_1350`:
      - `type`: object
      - `required`:
        - `dd_transitions`: array of 5 numbers
        - `zfs_1e3_3a`: number
      - `unit`: cm^{-1}
    - `Dq_1400`:
      - `type`: object
      - `required`:
        - `dd_transitions`: array of 5 numbers
        - `zfs_1e3_3a`: number
      - `unit`: cm^{-1}
    - `Dq_1500`:
      - `type`: object
      - `required`:
        - `dd_transitions`: array of 5 numbers
        - `zfs_1e3_3a`: number
      - `unit`: cm^{-1}

### signed_zfs_results.json
- path: `/app/outputs/signed_zfs_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed zero-field splitting parameter 10^3(3a) (in cm^{-1}) for four parameter combinations, each evaluated with both positive and negative Dq. The hidden checker compares these values against reference gold values and verifies that for every set (3a)_{+Dq} > (3a)_{-Dq}.
- schema:
  - `type`: object
  - `required`:
    - `set1`: object
    - `set2`: object
    - `set3`: object
    - `set4`: object
  - `items`:
    - `set1`:
      - `type`: object
      - `required`:
        - `Dq_pos`: object
        - `Dq_neg`: object
      - `Dq_pos`:
        - `type`: object
        - `required`:
          - `param`: object
          - `zfs`: number
        - `param`:
          - `type`: object
          - `required`:
            - `B`: number
            - `C`: number
            - `alpha`: number
            - `zeta`: number
            - `Dq`: number
      - `Dq_neg`: ... same structure
    - `set2`: ...
    - `set3`: ...
    - `set4`: ...

Notes: All reported energies are in cm^{-1}. The d-d transition energies are derived from the five lowest excited states relative to the ground state for each Dq value. The zero-field splitting 3a is extracted from the ground-state multiplet and reported as 10^3(3a). The scored comparison tolerances account for floating-point implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dd_zfs_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Dq_1350": "object",
          "Dq_1400": "object",
          "Dq_1500": "object"
        },
        "items": {
          "Dq_1350": {
            "type": "object",
            "required": {
              "dd_transitions": "array of 5 numbers",
              "zfs_1e3_3a": "number"
            },
            "unit": "cm^{-1}"
          },
          "Dq_1400": {
            "type": "object",
            "required": {
              "dd_transitions": "array of 5 numbers",
              "zfs_1e3_3a": "number"
            },
            "unit": "cm^{-1}"
          },
          "Dq_1500": {
            "type": "object",
            "required": {
              "dd_transitions": "array of 5 numbers",
              "zfs_1e3_3a": "number"
            },
            "unit": "cm^{-1}"
          }
        }
      },
      "description": "Computed d-d transition energies (five lowest excited-state energies relative to ground, in cm^{-1}) and the zero-field splitting parameter 10^3(3a) (in cm^{-1}) for three representative crystals. The hidden checker compares these values against reference gold values from the literature with appropriate tolerance."
    },
    {
      "file": "signed_zfs_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "set1": "object",
          "set2": "object",
          "set3": "object",
          "set4": "object"
        },
        "items": {
          "set1": {
            "type": "object",
            "required": {
              "Dq_pos": "object",
              "Dq_neg": "object"
            },
            "Dq_pos": {
              "type": "object",
              "required": {
                "param": "object",
                "zfs": "number"
              },
              "param": {
                "type": "object",
                "required": {
                  "B": "number",
                  "C": "number",
                  "alpha": "number",
                  "zeta": "number",
                  "Dq": "number"
                }
              }
            },
            "Dq_neg": "... same structure"
          },
          "set2": "...",
          "set3": "...",
          "set4": "..."
        }
      },
      "description": "Computed zero-field splitting parameter 10^3(3a) (in cm^{-1}) for four parameter combinations, each evaluated with both positive and negative Dq. The hidden checker compares these values against reference gold values and verifies that for every set (3a)_{+Dq} > (3a)_{-Dq}."
    }
  ],
  "notes": "All reported energies are in cm^{-1}. The d-d transition energies are derived from the five lowest excited states relative to the ground state for each Dq value. The zero-field splitting 3a is extracted from the ground-state multiplet and reported as 10^3(3a). The scored comparison tolerances account for floating-point implementation differences."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact. The verifier compares the d-d transition energies and 10³(3a) values in `dd_zfs_results.json` to reference gold values with appropriate floating-point tolerances. It also compares the 10³(3a) values in `signed_zfs_results.json` to reference gold and checks that for every set (3a)_{+Dq} > (3a)_{-Dq}. Each scored artifact contributes to the final reward; neither shape-only checks nor reporting paper values without genuine computation will earn full credit. The exact tolerances and reference values are hidden from you.
