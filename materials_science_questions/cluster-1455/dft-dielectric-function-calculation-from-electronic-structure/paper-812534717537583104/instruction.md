# DFT electronic structure and optical properties of OsP2 marcasite

## Problem background
OsP₂ in the orthorhombic marcasite structure is a narrow-gap semiconductor with potential applications in thermoelectrics and infrared optics. A thorough theoretical characterization of its electronic, optical, and dielectric properties is lacking. This work investigates these properties using density functional theory (DFT) within the full-potential linearized augmented plane wave (FP‑LAPW) method. By comparing several exchange‑correlation functionals — GGA, LDA, GGA‑mBJ, and LDA‑mBJ — and incorporating spin‑orbit coupling (SOC), the study determines the fundamental bandgap, its transition type, and the material’s refractive index in the infrared region.

## Approach
Perform all‑electron FP‑LAPW calculations using an open‑source code (e.g., Elk). First, relax the marcasite OsP₂ structure with the LDA functional to obtain a stable ground‑state geometry. Using that geometry, run self‑consistent field and band‑structure calculations for four different exchange‑correlation functionals: GGA, LDA, GGA‑mBJ, and LDA‑mBJ, extracting the bandgap energy and transition character (direct or indirect) for each. Also compute the band structure with LDA‑mBJ including spin‑orbit coupling. From the LDA‑mBJ (no SOC) self‑consistent charge density, calculate the complex dielectric function via momentum matrix elements and a Kramers‑Kronig transformation, and derive the frequency‑dependent refractive index. The approach systematically compares the four functionals and the effect of spin‑orbit coupling on the electronic structure.

## Reproduction target
Using an open‑source FP‑LAPW code (e.g., Elk), perform DFT calculations on OsP₂ in the orthorhombic marcasite structure: (1) relax the crystal structure with LDA; (2) compute bandgaps and transition type with GGA, LDA, GGA‑mBJ, and LDA‑mBJ (no SOC); (3) compute the bandgap with LDA‑mBJ + SOC; (4) from the LDA‑mBJ (no SOC) run, evaluate the refractive index at 1000 cm⁻¹. Collect all results in a JSON file following the output schema below. The objective is to obtain the bandgap energies, the indirect transition direction, and the infrared refractive index from first principles.

## Assets

- Marcasite OsP2 experimental crystal structure
- Elk FP-LAPW code: https://elk.sourceforge.io/

## Workflow steps

### Step 1: Structure optimization
- Role: process
- Action: Relax the marcasite OsP₂ structure using the LDA functional within the FP-LAPW method. Optimize lattice parameters and atomic positions to obtain a stable ground-state geometry.
- Evidence: `/app/outputs/optimization.log`

### Step 2: Band structure with GGA, LDA, GGA-mBJ, LDA-mBJ
- Role: process
- Action: Using the optimized structure, run self-consistent and band structure calculations for each of the four exchange-correlation functionals: GGA, LDA, GGA-mBJ, LDA-mBJ. Extract the bandgap energies and transition character.
- Evidence: `/app/outputs/bandgaps_process.log`

### Step 3: SOC band structure
- Role: process
- Action: Perform a band structure calculation using the LDA-mBJ functional with spin-orbit coupling included. Extract the fundamental bandgap.
- Evidence: `/app/outputs/soc_process.log`

### Step 4: Optical properties
- Role: process
- Action: From the self-consistent LDA-mBJ (without SOC) calculation, compute the complex dielectric function via momentum matrix elements and Kramers-Kronig transformation. Derive the refractive index n(ω).
- Evidence: `/app/outputs/optical_process.log`

### Step 5: Aggregate results
- Role: scored
- Action: Collect the bandgap values for GGA, LDA, GGA-mBJ, LDA-mBJ (without SOC), the LDA-mBJ+SOC bandgap, the transition direction, and the refractive index at 1000 cm⁻¹. Write a JSON file conforming to the output schema.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"bandgap_GGA": float, "bandgap_LDA": float, "bandgap_GGA_mBJ": float, "bandgap_LDA_mBJ": float, "bandgap_LDA_mBJ_SOC": float, "refractive_index_1000cm": float, "transition_type": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed bandgap energies (eV) for each functional, SOC bandgap, refractive index at 1000 cm⁻¹, and the transition type (e.g., direct or indirect, including direction if indirect). Scoring compares to paper-reported gold tolerances.
- schema:
  - `type`: object
  - `required`: `bandgap_GGA`, `bandgap_LDA`, `bandgap_GGA_mBJ`, `bandgap_LDA_mBJ`, `bandgap_LDA_mBJ_SOC`, `refractive_index_1000cm`, `transition_type`
  - `properties`:
    - `bandgap_GGA`:
      - `type`: number
      - `units`: eV
    - `bandgap_LDA`:
      - `type`: number
      - `units`: eV
    - `bandgap_GGA_mBJ`:
      - `type`: number
      - `units`: eV
    - `bandgap_LDA_mBJ`:
      - `type`: number
      - `units`: eV
    - `bandgap_LDA_mBJ_SOC`:
      - `type`: number
      - `units`: eV
    - `refractive_index_1000cm`:
      - `type`: number
      - `units`: dimensionless
    - `transition_type`:
      - `type`: string

Notes: All bandgap values in eV. Refractive index is dimensionless. Transition type should be a descriptive string (e.g., direct, indirect with direction).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "bandgap_GGA",
          "bandgap_LDA",
          "bandgap_GGA_mBJ",
          "bandgap_LDA_mBJ",
          "bandgap_LDA_mBJ_SOC",
          "refractive_index_1000cm",
          "transition_type"
        ],
        "properties": {
          "bandgap_GGA": {
            "type": "number",
            "units": "eV"
          },
          "bandgap_LDA": {
            "type": "number",
            "units": "eV"
          },
          "bandgap_GGA_mBJ": {
            "type": "number",
            "units": "eV"
          },
          "bandgap_LDA_mBJ": {
            "type": "number",
            "units": "eV"
          },
          "bandgap_LDA_mBJ_SOC": {
            "type": "number",
            "units": "eV"
          },
          "refractive_index_1000cm": {
            "type": "number",
            "units": "dimensionless"
          },
          "transition_type": {
            "type": "string"
          }
        }
      },
      "description": "Computed bandgap energies (eV) for each functional, SOC bandgap, refractive index at 1000 cm⁻¹, and the transition type (e.g., direct or indirect, including direction if indirect). Scoring compares to paper-reported gold tolerances."
    }
  ],
  "notes": "All bandgap values in eV. Refractive index is dimensionless. Transition type should be a descriptive string (e.g., direct, indirect with direction)."
}
```

## How you are scored
A hidden verifier reads your `results.json` and scores each quantity against a hidden reference derived from the paper. The scoring weights are: LDA‑mBJ bandgap (30%), relative ordering of the four non‑SOC bandgaps (20%), SOC‑induced bandgap reduction (20%), and refractive index at 1000 cm⁻¹ (30%). Each component uses a `threshold_or_better` policy: meeting or exceeding the reference within a tolerance gives full credit, and reward decreases as the reported quantity deviates further from the target. The verifier does not disclose the reference values or tolerances.
