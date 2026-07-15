# Structural, elastic, thermal expansion, and thermal conductivity properties of hexagonal and orthorhombic perovskites using interatomic potential simulations

## Problem background
Hexagonal P6₃cm perovskites A³⁺B³⁺O₃ are candidate materials for thermal barrier coatings. Their mechanical and thermal properties—elastic constants, thermal expansion, and thermal conductivity—are of interest, particularly how anisotropy and magnitude change with composition and between hexagonal and orthorhombic polymorphs. This computational task systematically computes these properties for a representative set of compositions using interatomic potential simulations.

## Approach
The workflow uses atomic‑level simulations with a classical Buckingham potential (parameters from Levy et al.) to describe short‑range interactions, plus Coulombic electrostatics. Lattice‑statics calculations with GULP relax the crystal structures and extract the six independent elastic constants for each hexagonal composition. For hexagonal systems only, quasi‑harmonic phonon calculations within GULP yield directional thermal expansion coefficients α₁₁ and α₃₃. Anharmonic lattice thermal conductivity is computed for all compositions (hexagonal and orthorhombic) by solving the Boltzmann transport equation with the PhonTS code, using force constants from the GULP phonon calculations. The final step assembles all data into a single JSON artifact.

## Reproduction target
For the following systems, compute relaxed lattice parameters a, c, primitive‑cell volume V, elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, C₆₆ (hexagonal only), thermal expansion coefficients α₁₁ and α₃₃ (hexagonal only), and lattice thermal conductivity components k₁₁ and k₃₃ (all systems).

Hexagonal AFeO₃: A = Sc, In, Lu, Yb, Er, Ho, Y, Dy
Hexagonal HoBO₃: B = Fe, Sc, In, Ga, Cr, Al
Orthorhombic AFeO₃: A = Ce, Sm, Gd, Dy
Orthorhombic HoBO₃: B = Al, Cr, Ga

Assemble the output as a JSON file containing an array of system objects with fields: composition, structure_type, a, c, V, elastic constants (nullable), thermal expansion coefficients (nullable), and thermal conductivity components. The hidden verifier will compute various ratios and inter‑phase comparisons using these data.

## Assets

- Buckingham potential parameters for A³⁺B³⁺O₃ perovskites (Levy et al., 2004): 10.1080/14786430412331279724
- General Utility Lattice Program (GULP): https://www.ivec.org/gulp/
- Phonon Transport Simulator (PhonTS): https://github.com/Philpot-Group/PhonTS
- Shannon ionic radii

## Workflow steps

### Step 1: GULP lattice-statics and elastic constants
- Role: process
- Action: Prepare GULP input files for all required compositions (hexagonal AFeO₃ with A = Sc, In, Lu, Yb, Er, Ho, Y, Dy and HoBO₃ with B = Fe, Sc, In, Ga, Cr, Al; orthorhombic AFeO₃ with A = Ce, Sm, Gd, Dy and HoBO₃ with B = Al, Cr, Ga) using the Buckingham potential parameters from Levy et al. Run GULP lattice-statics to obtain relaxed lattice parameters a (Å), c (Å), unit-cell volume V (Å³), and the six independent elastic constants C11, C12, C13, C33, C44, C66 (GPa) for each system. Retain all results for later assembly.
- Evidence: `/app/outputs/gulp_lattice_statics.log`

### Step 2: Quasi-harmonic thermal expansion for hexagonal perovskites
- Role: process
- Action: Using the relaxed hexagonal structures from step 01, run GULP quasi-harmonic phonon calculations to compute linear thermal expansion coefficients α11 and α33 (in 10⁻⁶ K⁻¹) for each hexagonal composition only. Store the results.
- Evidence: `/app/outputs/thermal_expansion.log`

### Step 3: BTE thermal conductivity via PhonTS
- Role: process
- Action: Using the GULP-derived structures and force constants from steps 01 and 02, run PhonTS for all compositions (hexagonal and orthorhombic) to compute anisotropic lattice thermal conductivity components k11 and k33 (W/m·K). Retain the results.
- Evidence: `/app/outputs/phonts_output.log`

### Step 4: Assemble final property table
- Role: scored (load-bearing)
- Action: Compile the computed structural, elastic, thermal expansion, and thermal conductivity data for all required systems into a single JSON file named perovskite_properties.json. The file must contain exactly the set of systems listed in step 01, with fields: composition, structure_type (hexagonal/orthorhombic), a (Å), c (Å), V (Å³), C11, C12, C13, C33, C44, C66 (all in GPa), alpha11, alpha33 (1e-6/K), k11, k33 (W/m·K). For orthorhombic systems, elastic constants and thermal expansion coefficients may be omitted or set to null if not computed (thermal conductivity must be present).
- Output file: `/app/outputs/perovskite_properties.json`
- Format: json
- Contract: {"systems": [{"composition": "string", "structure_type": "hexagonal|orthorhombic", "a": float, "c": float, "V": float, "C11": float|null, "C12": float|null, "C13": float|null, "C33": float|null, "C44": float|null, "C66": float|null, "alpha11": float|null, "alpha33": float|null, "k11": float, "k33": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/perovskite_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### perovskite_properties.json
- path: `/app/outputs/perovskite_properties.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: JSON containing an array of perovskite composition entries with their computed structural, elastic, thermal expansion, and thermal transport properties.
- schema:
  - `type`: object
  - `properties`:
    - `systems`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `composition`:
            - `type`: string
          - `structure_type`:
            - `type`: string
            - `enum`: `hexagonal`, `orthorhombic`
          - `a`:
            - `type`: number
          - `c`:
            - `type`: number
          - `V`:
            - `type`: number
          - `C11`:
            - `type`: number
            - `nullable`: True
          - `C12`:
            - `type`: number
            - `nullable`: True
          - `C13`:
            - `type`: number
            - `nullable`: True
          - `C33`:
            - `type`: number
            - `nullable`: True
          - `C44`:
            - `type`: number
            - `nullable`: True
          - `C66`:
            - `type`: number
            - `nullable`: True
          - `alpha11`:
            - `type`: number
            - `nullable`: True
          - `alpha33`:
            - `type`: number
            - `nullable`: True
          - `k11`:
            - `type`: number
          - `k33`:
            - `type`: number
        - `required`: `composition`, `structure_type`, `a`, `c`, `V`, `k11`, `k33`
  - `required`: `systems`

Notes: Elastic constants and thermal expansion coefficients are required only for hexagonal entries; for orthorhombic entries they may be null. Thermal conductivity components must be present for all entries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "perovskite_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "systems": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "composition": {
                  "type": "string"
                },
                "structure_type": {
                  "type": "string",
                  "enum": [
                    "hexagonal",
                    "orthorhombic"
                  ]
                },
                "a": {
                  "type": "number"
                },
                "c": {
                  "type": "number"
                },
                "V": {
                  "type": "number"
                },
                "C11": {
                  "type": "number",
                  "nullable": true
                },
                "C12": {
                  "type": "number",
                  "nullable": true
                },
                "C13": {
                  "type": "number",
                  "nullable": true
                },
                "C33": {
                  "type": "number",
                  "nullable": true
                },
                "C44": {
                  "type": "number",
                  "nullable": true
                },
                "C66": {
                  "type": "number",
                  "nullable": true
                },
                "alpha11": {
                  "type": "number",
                  "nullable": true
                },
                "alpha33": {
                  "type": "number",
                  "nullable": true
                },
                "k11": {
                  "type": "number"
                },
                "k33": {
                  "type": "number"
                }
              },
              "required": [
                "composition",
                "structure_type",
                "a",
                "c",
                "V",
                "k11",
                "k33"
              ]
            }
          }
        },
        "required": [
          "systems"
        ]
      },
      "description": "JSON containing an array of perovskite composition entries with their computed structural, elastic, thermal expansion, and thermal transport properties."
    }
  ],
  "notes": "Elastic constants and thermal expansion coefficients are required only for hexagonal entries; for orthorhombic entries they may be null. Thermal conductivity components must be present for all entries."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the JSON file and computes ratios/cross‑comparisons (e.g., C₁₁/C₃₃, α₁₁/α₃₃, k₁₁/k₃₃, hexagonal vs. orthorhombic thermal conductivity) and compares them against hidden reference thresholds. Each stage carries a weight, and the final reward is the weighted sum. Reporting paper‑derived numbers is not sufficient; the data must result from running the actual simulations. The verifier’s thresholds are unknown to you.
