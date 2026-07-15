# Phagraphene thermal and mechanical properties via molecular dynamics

## Problem background
Phagraphene is a recently predicted planar carbon allotrope built from a 5‑6‑7 ring pattern, with electronic properties that may be more favorable than graphene for thermoelectric devices. Its room‑temperature thermal conductivity and mechanical properties are currently unexplored. Determining these properties is essential to assess its potential in carbon‑based device applications.

## Approach
The thermal transport and mechanical response are investigated via classical molecular dynamics simulations powered by the optimized Tersoff empirical potential (Lindsay–Broido) for carbon. After constructing the phagraphene unit cell and verifying its dynamical stability via phonon dispersion calculations, non‑equilibrium molecular dynamics (NEMD) is performed on samples of increasing length to obtain size‑dependent thermal conductivity along the two principal in‑plane directions (armchair and zigzag). The intrinsic thermal conductivity and effective phonon mean free path are extracted by fitting the data to the classical scaling relation that connects apparent conductivity to system size. Mechanical behavior is studied through uniaxial tensile simulations at constant strain rate; a cutoff‑modified potential (cutoff increased to 0.2 nm) is used to avoid unphysical hardening. The elastic modulus is determined from the initial linear region of the stress‑strain curve and the tensile strength from the peak stress. A parallel validation on pristine graphene confirms that the modified potential reproduces known mechanical benchmarks.

## Reproduction target
Carry out the described simulation pipeline to obtain the intrinsic thermal conductivity (κ, in W/m‑K) and effective phonon mean free path (Λ_eff, in nm) along both armchair and zigzag directions of phagraphene, as well as the elastic modulus (in GPa) and tensile strength (in GPa) along both directions. Write the thermal properties to `/app/outputs/thermal_properties.json` and the mechanical properties to `/app/outputs/mechanical_properties.json`.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- GULP lattice dynamics code: https://gulp.curtin.edu.au/
- Optimized Tersoff potential for carbon (Lindsay–Broido): 10.1103/PhysRevB.81.205441

## Workflow steps

### Step 1: Build phagraphene unit cell and verify dynamical stability
- Role: process
- Action: Construct the 20-atom rectangular unit cell of phagraphene as described in the paper, and perform a phonon dispersion calculation using GULP with the optimized Tersoff potential. Confirm that no imaginary (negative) frequencies appear along the high‑symmetry path Γ-X-Z-Y-Γ.
- Evidence: `/app/outputs/phonon_dispersion.txt`

### Step 2: NEMD simulations for size‑dependent thermal conductivity
- Role: process
- Action: Using LAMMPS, run non‑equilibrium molecular dynamics simulations for phagraphene samples of varying lengths (e.g., 5‑10 different lengths) along both armchair and zigzag directions at 300 K with the optimized Tersoff potential. Record the apparent thermal conductivity vs. length for each direction.
- Evidence: `/app/outputs/kappa_vs_length.json`

### Step 3: Fit intrinsic thermal conductivity and effective MFP
- Role: scored (load-bearing)
- Action: Fit the length‑dependent thermal conductivity data to the classical scaling relation 1/κ(L) = 1/κ · (1 + Λ_eff/L) to extract the intrinsic thermal conductivity κ and effective phonon mean free path Λ_eff for both armchair and zigzag directions. Write the results to /app/outputs/thermal_properties.json.
- Output file: `/app/outputs/thermal_properties.json`
- Format: json
- Contract: type=object; required=['kappa_armchair', 'kappa_zigzag', 'Lambda_armchair', 'Lambda_zigzag']; properties={'kappa_armchair': {'type': 'number', 'unit': 'W/m-K'}, 'kappa_zigzag': {'type': 'number', 'unit': 'W/m-K'}, 'Lambda_armchair': {'type': 'number', 'unit': 'nm'}, 'Lambda_zigzag': {'type': 'number', 'unit': 'nm'}}
- Scoring: scored by hidden verifier

### Step 4: Validate mechanics potential on pristine graphene
- Role: process
- Action: Run a uniaxial tensile simulation of pristine graphene at 300 K using the cutoff‑modified Tersoff potential (cutoff increased to 0.2 nm) and a strain rate of 1e8/s. Obtain the stress‑strain curve to confirm the potential reproduces known elastic modulus and tensile strength of graphene.
- Evidence: `/app/outputs/graphene_stress_strain.csv`

### Step 5: Uniaxial tensile simulations of phagraphene
- Role: process
- Action: Run uniaxial tensile simulations of phagraphene sheets along armchair and zigzag directions under identical conditions (cutoff‑modified Tersoff, 300 K, strain rate 1e8/s, zero‑stress condition transverse to loading). Record the engineering stress‑strain curves for both directions.
- Evidence: `/app/outputs/phagraphene_stress_strain_armchair.csv,phagraphene_stress_strain_zigzag.csv`

### Step 6: Extract mechanical properties
- Role: scored (load-bearing)
- Action: From the stress‑strain curves, determine the elastic modulus (initial linear slope) and the ultimate tensile strength (peak stress) for both armchair and zigzag directions. Write the results to /app/outputs/mechanical_properties.json.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: type=object; required=['modulus_armchair', 'modulus_zigzag', 'strength_armchair', 'strength_zigzag']; properties={'modulus_armchair': {'type': 'number', 'unit': 'GPa'}, 'modulus_zigzag': {'type': 'number', 'unit': 'GPa'}, 'strength_armchair': {'type': 'number', 'unit': 'GPa'}, 'strength_zigzag': {'type': 'number', 'unit': 'GPa'}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_properties.json`
- `/app/outputs/mechanical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_properties.json
- path: `/app/outputs/thermal_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Intrinsic thermal conductivity and effective phonon mean free path of phagraphene at 300 K along armchair and zigzag directions.
- schema:
  - `type`: object
  - `required`: `kappa_armchair`, `kappa_zigzag`, `Lambda_armchair`, `Lambda_zigzag`
  - `properties`:
    - `kappa_armchair`:
      - `type`: number
      - `unit`: W/m-K
    - `kappa_zigzag`:
      - `type`: number
      - `unit`: W/m-K
    - `Lambda_armchair`:
      - `type`: number
      - `unit`: nm
    - `Lambda_zigzag`:
      - `type`: number
      - `unit`: nm

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Elastic modulus and tensile strength of phagraphene at 300 K along armchair and zigzag directions.
- schema:
  - `type`: object
  - `required`: `modulus_armchair`, `modulus_zigzag`, `strength_armchair`, `strength_zigzag`
  - `properties`:
    - `modulus_armchair`:
      - `type`: number
      - `unit`: GPa
    - `modulus_zigzag`:
      - `type`: number
      - `unit`: GPa
    - `strength_armchair`:
      - `type`: number
      - `unit`: GPa
    - `strength_zigzag`:
      - `type`: number
      - `unit`: GPa

Notes: Thermal conductivity and mechanical properties are extracted from NEMD and tensile MD simulations, respectively. The checker compares the reported values to the paper-reported gold with appropriate tolerances and trend verification (κ_zigzag > κ_armchair, modulus_armchair > modulus_zigzag).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "kappa_armchair",
          "kappa_zigzag",
          "Lambda_armchair",
          "Lambda_zigzag"
        ],
        "properties": {
          "kappa_armchair": {
            "type": "number",
            "unit": "W/m-K"
          },
          "kappa_zigzag": {
            "type": "number",
            "unit": "W/m-K"
          },
          "Lambda_armchair": {
            "type": "number",
            "unit": "nm"
          },
          "Lambda_zigzag": {
            "type": "number",
            "unit": "nm"
          }
        }
      },
      "description": "Intrinsic thermal conductivity and effective phonon mean free path of phagraphene at 300 K along armchair and zigzag directions."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "modulus_armchair",
          "modulus_zigzag",
          "strength_armchair",
          "strength_zigzag"
        ],
        "properties": {
          "modulus_armchair": {
            "type": "number",
            "unit": "GPa"
          },
          "modulus_zigzag": {
            "type": "number",
            "unit": "GPa"
          },
          "strength_armchair": {
            "type": "number",
            "unit": "GPa"
          },
          "strength_zigzag": {
            "type": "number",
            "unit": "GPa"
          }
        }
      },
      "description": "Elastic modulus and tensile strength of phagraphene at 300 K along armchair and zigzag directions."
    }
  ],
  "notes": "Thermal conductivity and mechanical properties are extracted from NEMD and tensile MD simulations, respectively. The checker compares the reported values to the paper-reported gold with appropriate tolerances and trend verification (κ_zigzag > κ_armchair, modulus_armchair > modulus_zigzag)."
}
```

## How you are scored
A hidden verifier evaluates each output artifact independently. It checks that every reported property value lies within acceptable uncertainty of a reference (obtained from the original computational study) and that any qualitative anisotropy — the relative ordering of properties between armchair and zigzag directions — matches the expected pattern. The final reward is a weighted combination of the scores from the two artifact files. Merely reporting plausible numbers cannot substitute for correctly executing the required simulations and analysis; the verifier's tolerances reflect the spread expected from an honest re‑implementation, so only a correctly run workflow will pass.
