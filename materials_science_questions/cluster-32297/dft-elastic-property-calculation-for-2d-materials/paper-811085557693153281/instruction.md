# DFT calculation of electronic band gaps and static refractive indices for MgF2 bulk and monolayers

## Problem background
Two-dimensional MgF₂ monolayers in 1H (hexagonal) and 1T (tetragonal) phases, together with the parent bulk tetragonal structure, have been predicted to be wide-band-gap insulators with low refractive indices. Such properties make them attractive for anti-reflection coatings and opto-electronic applications. This task aims to reproduce the key electronic and optical properties of these materials by first-principles computation: the electronic band gaps, the nature (direct/indirect) of those gaps, and the static (frequency-zero) refractive index for each monolayer phase under two orthogonal polarizations of the incident electric field.

## Approach
The workflow follows the standard density functional theory (DFT) approach for crystalline systems. Using the plane-wave pseudopotential method within the generalized gradient approximation (GGA-PBE functional), you will first relax the atomic positions and lattice parameters of bulk tetragonal MgF₂ and of the 1H and 1T monolayer structures. For the monolayers, a sufficiently large vacuum spacing (at least 15 Å) must be included in the out-of-plane direction to eliminate spurious interactions between periodic images. From the optimized structures, the electronic band structure along standard high-symmetry paths is computed, from which the band gap energy and whether the gap is direct (i.e., valence and conduction band edges both at the Γ point) are determined. For the two monolayer phases only, the frequency-dependent complex dielectric function is then calculated using the random-phase approximation (RPA) for both in-plane (E || X) and out-of-plane (E ⊥ Z) polarizations. The static refractive index n(ω=0) is extracted from the long-wavelength limit of the dielectric function.

## Reproduction target
Your goal is to compute and report the following quantities for bulk MgF₂ and for the 1H and 1T monolayer phases:
- Electronic band gap (in eV) for each system.
- Whether each band gap is direct (true if both valence band maximum and conduction band minimum lie at the Γ point, false otherwise).
- Static refractive index n(ω=0) for the 1H and 1T monolayers under parallel (in-plane) and perpendicular (out-of-plane) electric field polarizations (dimensionless).

All values must be written to a JSON file named `/app/outputs/results.json` with exactly the following fields:
- `bulk_bandgap` (number, eV)
- `1H_bandgap` (number, eV)
- `1T_bandgap` (number, eV)
- `bulk_direct` (boolean)
- `1H_direct` (boolean)
- `1T_direct` (boolean)
- `1H_n_parallel` (number)
- `1H_n_perpendicular` (number)
- `1T_n_parallel` (number)
- `1T_n_perpendicular` (number)

The JSON schema is also given in the output contract section.

## Assets

- Quantum ESPRESSO (or any plane-wave pseudopotential DFT code with PBE and optical property calculation): https://www.quantum-espresso.org/
- PBE pseudopotentials for Mg and F (SSSP efficiency library or equivalent): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization of bulk, 1H, and 1T MgF2
- Role: process
- Action: Perform DFT geometry optimization for bulk tetragonal MgF2 and for 1H and 1T monolayer MgF2 using plane-wave pseudopotential method with GGA-PBE functional. Relax atomic positions and lattice parameters. For monolayers, include sufficient vacuum (≥15 Å) in the out-of-plane direction to avoid spurious interlayer interactions.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Electronic band structure calculation
- Role: process
- Action: Using the optimized structures from step_01, compute the electronic band structure along high-symmetry paths in the first Brillouin zone for bulk, 1H, and 1T MgF2 with the same DFT settings. Identify the valence band maximum (VBM) and conduction band minimum (CBM) at the Γ point and record the band gap energy and whether the gap is direct.
- Evidence: `/app/outputs/band_structure_data.txt`

### Step 3: Optical dielectric function calculation
- Role: process
- Action: Compute the frequency-dependent complex dielectric function for 1H and 1T monolayers under parallel (E||X) and perpendicular (E⊥Z) electric field polarizations using the random-phase approximation (RPA). Extract the static refractive index n(ω=0) from the long-wavelength limit of the dielectric function.
- Evidence: `/app/outputs/optical_calculations.log`

### Step 4: Assemble and report scored quantities
- Role: scored (load-bearing)
- Action: Extract the band gap energies (eV) and direct/indirect flags for bulk tetragonal MgF2, 1H monolayer, and 1T monolayer from the band structure data. Extract the static refractive indices for 1H and 1T monolayers under parallel and perpendicular polarizations from the optical calculations. Write all values to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Fields: bulk_bandgap (float, eV), 1H_bandgap (float, eV), 1T_bandgap (float, eV), bulk_direct (bool), 1H_direct (bool), 1T_direct (bool), 1H_n_parallel (float), 1H_n_perpendicular (float), 1T_n_parallel (float), 1T_n_perpendicular (float).
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
- target_policy: reference_match
- description: Aggregated reproduction metrics: electronic band gaps and static refractive indices for bulk and monolayer MgF₂ phases. The hidden checker compares each numeric field to the corresponding paper-reported value within a tolerance.
- schema:
  - `type`: object
  - `required`: `bulk_bandgap`, `1H_bandgap`, `1T_bandgap`, `bulk_direct`, `1H_direct`, `1T_direct`, `1H_n_parallel`, `1H_n_perpendicular`, `1T_n_parallel`, `1T_n_perpendicular`
  - `properties`:
    - `bulk_bandgap`:
      - `type`: number
      - `units`: eV
    - `1H_bandgap`:
      - `type`: number
      - `units`: eV
    - `1T_bandgap`:
      - `type`: number
      - `units`: eV
    - `bulk_direct`:
      - `type`: boolean
    - `1H_direct`:
      - `type`: boolean
    - `1T_direct`:
      - `type`: boolean
    - `1H_n_parallel`:
      - `type`: number
      - `units`: dimensionless
    - `1H_n_perpendicular`:
      - `type`: number
      - `units`: dimensionless
    - `1T_n_parallel`:
      - `type`: number
      - `units`: dimensionless
    - `1T_n_perpendicular`:
      - `type`: number
      - `units`: dimensionless

Notes: The agent must compute all properties using DFT and ensure the output JSON conforms to the schema. No gold values or tolerances are disclosed.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "bulk_bandgap",
          "1H_bandgap",
          "1T_bandgap",
          "bulk_direct",
          "1H_direct",
          "1T_direct",
          "1H_n_parallel",
          "1H_n_perpendicular",
          "1T_n_parallel",
          "1T_n_perpendicular"
        ],
        "properties": {
          "bulk_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "1H_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "1T_bandgap": {
            "type": "number",
            "units": "eV"
          },
          "bulk_direct": {
            "type": "boolean"
          },
          "1H_direct": {
            "type": "boolean"
          },
          "1T_direct": {
            "type": "boolean"
          },
          "1H_n_parallel": {
            "type": "number",
            "units": "dimensionless"
          },
          "1H_n_perpendicular": {
            "type": "number",
            "units": "dimensionless"
          },
          "1T_n_parallel": {
            "type": "number",
            "units": "dimensionless"
          },
          "1T_n_perpendicular": {
            "type": "number",
            "units": "dimensionless"
          }
        }
      },
      "description": "Aggregated reproduction metrics: electronic band gaps and static refractive indices for bulk and monolayer MgF₂ phases. The hidden checker compares each numeric field to the corresponding paper-reported value within a tolerance."
    }
  ],
  "notes": "The agent must compute all properties using DFT and ensure the output JSON conforms to the schema. No gold values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier inspects your `/app/outputs/results.json`. It compares each numeric field against a reference value that is known to the verifier but not to you. The comparison uses appropriate tolerances that account for the expected variation among different DFT implementations, pseudopotentials, and convergence settings, while still requiring that the underlying physics is correctly captured. For the boolean (direct/indirect) fields the verifier checks that they match the expected value. Each field is scored equally; the partial scores are summed to give a total reward between 0 and 1. Simply reporting numbers that happen to match is insufficient—you must genuinely run the DFT computations to arrive at your result.
