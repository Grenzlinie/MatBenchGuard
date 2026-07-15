# MD comparison of nanoindentation and uniaxial tensile strength of graphene

## Problem background
Graphene's mechanical strength is typically measured by nanoindentation because uniaxial tensile testing on 2D materials is challenging. However, the failure process under indentation (a concentrated biaxial stress) may differ fundamentally from uniaxial tension (a uniform stress), and the strength values inferred from the two loading modes may not agree. Understanding how the failure mechanisms differ and how strength estimates are affected is important for interpreting experimental grain-boundary strength measurements and for reliable device design. This task investigates this question by comparing strengths and failure behaviors for both pristine graphene and a bicrystalline graphene sheet containing a symmetric tilt grain boundary.

## Approach
The investigation uses molecular dynamics (MD) simulations with the AIREBO interatomic potential to model the carbon‑carbon interactions. Two loading modes are compared: (1) nanoindentation with a clamped circular boundary, where a rigid spherical indenter is advanced at constant speed and the tip force is recorded; (2) uniaxial tension along the armchair direction (or perpendicular to the grain boundary for bicrystal), where the sample is stretched at a constant rate and the stress–strain response is recorded. For indentation, the failure force is converted to a strength estimate using a stress–force calibration derived from the stress field of pristine graphene. For tension, the strength is taken directly from the peak stress. The workflow constructs two atomic models: a pristine graphene sheet of about 50 nm × 50 nm with clamped circular boundaries, and a bicrystalline sheet of the same size containing a symmetric tilt grain boundary of 5.7° misorientation (5‑7 defects spaced ∼40 Å). Identical simulation conditions (temperature, loading rate, potential cutoff) are used for all runs to allow a fair comparison of the strengths and failure metrics.

## Reproduction target
The objective is to compute and report the following metrics: the strength of pristine graphene estimated from nanoindentation (GPa) and from uniaxial tension (GPa); the strength of the bicrystalline sheet with a 5.7° grain boundary estimated from nanoindentation (GPa) and from uniaxial tension (GPa); and, for the bicrystalline nanoindentation, the indenter deflection at first crack nucleation (nm) and at final catastrophic failure (nm). All six values must be written to a JSON file with the exact keys: pristine_strength_nanoindentation_GPa, pristine_strength_tension_GPa, gb_strength_nanoindentation_GPa, gb_strength_tension_GPa, gb_nucleation_deflection_nm, gb_failure_deflection_nm.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/download.html
- AIREBO potential

## Workflow steps

### Step 1: Construct atomic models
- Role: process
- Action: Generate LAMMPS data files for a pristine graphene sheet (≈50 nm × 50 nm) with clamped circular boundary conditions and for a bicrystalline graphene sheet containing a symmetric tilt grain boundary with misorientation 5.7° (5-7 defect spacing ≈40 Å).
- Evidence: none

### Step 2: Run nanoindentation on pristine graphene
- Role: process
- Action: Perform molecular dynamics nanoindentation on pristine graphene using LAMMPS with AIREBO potential (cutoff 1.92 Å), rigid spherical indenter (R=50 Å, K=10 eV/Å³), indenter speed 0.02 Å/ps, NVT ensemble at 300 K. Record the force-deflection curve.
- Evidence: `/app/outputs/pristine_nano_force_deflection.csv`

### Step 3: Run uniaxial tension on pristine graphene
- Role: process
- Action: Perform molecular dynamics uniaxial tensile loading of pristine graphene (armchair direction) with the same potential and conditions. Record the stress–strain curve.
- Evidence: `/app/outputs/pristine_tension_stress_strain.csv`

### Step 4: Run nanoindentation on bicrystalline graphene (5.7° GB)
- Role: process
- Action: Perform nanoindentation on the bicrystalline graphene sheet with indenter centered on the grain boundary line. Use identical indenter and simulation settings as the pristine case. Record the force–deflection curve.
- Evidence: `/app/outputs/gb_nano_force_deflection.csv`

### Step 5: Run uniaxial tension on bicrystalline graphene (5.7° GB)
- Role: process
- Action: Perform uniaxial tensile loading of the bicrystalline graphene sheet with loading direction perpendicular to the grain boundary. Use the same potential and ensemble as the pristine case. Record the stress–strain curve.
- Evidence: `/app/outputs/gb_tension_stress_strain.csv`

### Step 6: Compute strength metrics and failure deflections
- Role: scored (load-bearing)
- Action: Analyze simulation outputs: derive the stress–force relationship from pristine nanoindentation data; compute (i) pristine strength from nanoindentation and from tension, (ii) GB strength from nanoindentation and from tension; determine the indentation deflection at first crack nucleation and at catastrophic failure for GB nanoindentation. Report all quantities in a JSON file.
- Output file: `/app/outputs/step_06_results.json`
- Format: json
- Contract: {"type": "object", "properties": {"pristine_strength_nanoindentation_GPa": {"type": "number", "unit": "GPa"}, "pristine_strength_tension_GPa": {"type": "number", "unit": "GPa"}, "gb_strength_nanoindentation_GPa": {"type": "number", "unit": "GPa"}, "gb_strength_tension_GPa": {"type": "number", "unit": "GPa"}, "gb_nucleation_deflection_nm": {"type": "number", "unit": "nm"}, "gb_failure_deflection_nm": {"type": "number", "unit": "nm"}}, "required": ["pristine_strength_nanoindentation_GPa", "pristine_strength_tension_GPa", "gb_strength_nanoindentation_GPa", "gb_strength_tension_GPa", "gb_nucleation_deflection_nm", "gb_failure_deflection_nm"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_06_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_06_results.json
- path: `/app/outputs/step_06_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated strength estimates and critical deflections that demonstrate the difference between nanoindentation and uniaxial tension for pristine and grain-boundary graphene.
- schema:
  - `type`: object
  - `properties`:
    - `pristine_strength_nanoindentation_GPa`:
      - `type`: number
      - `unit`: GPa
    - `pristine_strength_tension_GPa`:
      - `type`: number
      - `unit`: GPa
    - `gb_strength_nanoindentation_GPa`:
      - `type`: number
      - `unit`: GPa
    - `gb_strength_tension_GPa`:
      - `type`: number
      - `unit`: GPa
    - `gb_nucleation_deflection_nm`:
      - `type`: number
      - `unit`: nm
    - `gb_failure_deflection_nm`:
      - `type`: number
      - `unit`: nm
  - `required`: `pristine_strength_nanoindentation_GPa`, `pristine_strength_tension_GPa`, `gb_strength_nanoindentation_GPa`, `gb_strength_tension_GPa`, `gb_nucleation_deflection_nm`, `gb_failure_deflection_nm`

Notes: The checker compares the reported values against hidden reference values (paper-reported results) with tolerances and enforces structural relations (gb_failure_deflection > gb_nucleation_deflection, pristine nano strength < pristine tensile strength).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_06_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "pristine_strength_nanoindentation_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "pristine_strength_tension_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "gb_strength_nanoindentation_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "gb_strength_tension_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "gb_nucleation_deflection_nm": {
            "type": "number",
            "unit": "nm"
          },
          "gb_failure_deflection_nm": {
            "type": "number",
            "unit": "nm"
          }
        },
        "required": [
          "pristine_strength_nanoindentation_GPa",
          "pristine_strength_tension_GPa",
          "gb_strength_nanoindentation_GPa",
          "gb_strength_tension_GPa",
          "gb_nucleation_deflection_nm",
          "gb_failure_deflection_nm"
        ]
      },
      "description": "Aggregated strength estimates and critical deflections that demonstrate the difference between nanoindentation and uniaxial tension for pristine and grain-boundary graphene."
    }
  ],
  "notes": "The checker compares the reported values against hidden reference values (paper-reported results) with tolerances and enforces structural relations (gb_failure_deflection > gb_nucleation_deflection, pristine nano strength < pristine tensile strength)."
}
```

## How you are scored
A hidden verifier reads your submitted step_06_results.json and compares each field to reference values obtained from independent calculations under the same conditions. The verifier also applies structural consistency checks on the reported values. The reward is a weighted combination: each strength value receives credit proportional to how close it is to the reference within an allowed tolerance, structural checks enforce mandatory relations, and the final reward is a single number between 0 and 1. Reporting the paper's numbers alone is not sufficient; the workflow must execute the molecular dynamics simulations and compute the strengths from the simulation outputs.
