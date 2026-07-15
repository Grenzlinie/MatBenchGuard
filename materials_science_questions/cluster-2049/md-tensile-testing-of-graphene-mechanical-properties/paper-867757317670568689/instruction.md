# MD tensile testing of monolayer InSe mechanical properties and Griffith deviation analysis

## Problem background
Monolayer indium selenide (InSe) is a two-dimensional van‑der‑Waals semiconductor with promising electronic and optoelectronic applications.  Understanding how its mechanical properties and fracture strength are affected by nanoscale pre‑cracks is essential for device reliability.  This task uses molecular dynamics to simulate tensile loading of pristine and pre‑cracked InSe sheets, producing quantitative comparisons between the atomistic fracture response and the classical Griffith brittle‑fracture prediction.  The aim is to compute the surface energy, the pristine elastic and failure properties, and the fracture stress for a series of crack lengths and temperatures, thereby evaluating the applicability of continuum fracture mechanics at the nanoscale.

## Approach
All simulations employ molecular dynamics with the Stillinger–Weber interatomic potential parameterised for monolayer InSe (Jiang & Zhou, 2017).  A pristine 30 nm × 30 nm sheet is constructed and subjected to energy minimisation, followed by short NPT and NVT equilibrations.  Uniaxial tension is applied at a constant strain rate, and virial stress is recorded as a function of engineering strain.  From the stress–strain curves, Young’s modulus (slope in the linear elastic regime), ultimate tensile stress (peak), and fracture strain are extracted.  Pre‑cracked structures containing central nano‑cracks of five half‑lengths (≈ 2.5–5.4 nm) oriented along both armchair and zigzag directions are created by atom removal.  The surface (edge) energy is obtained from the energy difference between slabs with periodic and free‑edge boundary conditions.  For each pre‑cracked sheet at 300 K, the MD fracture stress and Young’s modulus are recorded, and the corresponding Griffith fracture stress is calculated using the formula σ_f = √(2γY/(π a₀)), where γ is the surface energy and Y is the orientation‑averaged Young’s modulus.  Finally, the temperature dependence (1 K to 600 K) of fracture stress, strain, elastic modulus, and toughness is investigated for a fixed half‑crack length of 4.1 nm in both loading directions.

## Reproduction target
The goal is to produce the following scored artifacts under `/app/outputs`:

1. `surface_energy.json` – the surface (edge) energy of monolayer InSe in N/m, computed from energy‑minimised slabs with different boundary conditions.
2. `pristine_validation.csv` – Young’s modulus, ultimate tensile stress, and fracture strain for pristine sheets under armchair and zigzag tension at 1 K and 300 K.
3. `fracture_data.csv` – for each crack half‑length ( 2.5, 3.3, 4.1, 4.8, 5.4 nm) and both orientations at 300 K: the MD‑derived Young’s modulus, the MD fracture stress, and the Griffith fracture stress computed from the measured surface energy and orientation‑averaged Young’s modulus.
4. `temperature_dependence.csv` – fracture stress, fracture strain, elastic modulus, and toughness of a pre‑cracked sheet with a half‑crack length of 4.1 nm under armchair and zigzag loading at temperatures from 1 K to 600 K in 100 K steps.

All MD simulations should follow the same equilibration and tensile‑loading protocol (strain rate 10⁹ s⁻¹, time step 1 fs, periodic boundary conditions in the planar directions).  The output files must conform exactly to the column/field specifications listed in the workflow steps.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/
- Atomsk structure manipulation tool: https://atomsk.univ-lille.fr/
- Stillinger–Weber potential parameters for monolayer InSe: 10.5772/intechopen.71929
- OVITO visualization and analysis software: https://www.ovito.org/

## Workflow steps

### Step 1: Generate pristine monolayer InSe structure
- Role: process
- Action: Using lattice constant 4.09 Å, In–Se bond 2.69 Å, In–In bond 2.82 Å, effective thickness 8.32 Å, construct a 30 nm × 30 nm SLInSe sheet with ≈25000 atoms. Output a LAMMPS data file for the pristine structure.
- Evidence: `/app/outputs/pristine.data`

### Step 2: Create pre‑cracked structures
- Role: process
- Action: From the pristine structure, use Atomsk (or OVITO) to delete atoms and create central nano‑cracks of half‑lengths a0 = 2.5, 3.3, 4.1, 4.8, 5.4 nm in both armchair and zigzag orientations. Also create a sheet with a0 = 4.1 nm for the temperature study. Ensure a0 / ω0 < 0.1 (ω0 is half the sheet length).
- Evidence: `/app/outputs/crack_structures`

### Step 3: Compute surface (edge) energy
- Role: scored
- Action: Using LAMMPS with the SW potential, run energy minimization on (a) a fully periodic slab and (b) a slab with free edges in one planar direction. Compute the surface energy γ = (E_nonperiodic − E_periodic) / (2 × edge_length). Output the result in N/m.
- Output file: `/app/outputs/surface_energy.json`
- Format: json
- Contract: JSON object with keys: gamma_value (float), units (string), method (string).
- Scoring: scored by hidden verifier

### Step 4: Pristine sheet mechanical property validation
- Role: scored
- Action: Run uniaxial tensile MD simulations (strain rate 10⁹ s⁻¹) on the pristine sheet in armchair and zigzag directions at 1 K and 300 K. From the stress–strain curves extract Young’s modulus (slope in linear regime), ultimate tensile stress (peak), and fracture strain (strain at peak). Compile the results into CSV.
- Output file: `/app/outputs/pristine_validation.csv`
- Format: csv
- Contract: Columns: temp_K, direction, Young_modulus_Nm, UTS_Nm, fracture_strain_pct. Rows: 1K_armchair, 1K_zigzag, 300K_armchair, 300K_zigzag.
- Scoring: scored by hidden verifier

### Step 5: Pre‑cracked fracture data and Griffith comparison
- Role: scored (load-bearing)
- Action: Run tensile MD simulations on each pre‑cracked sheet (all crack lengths, both orientations) at 300 K. Extract fracture stress (peak stress) and Young’s modulus for each. Compute the Griffith fracture stress σ_f = sqrt(2γY/(π a0)) using the surface energy γ and the orientation‑averaged Young’s modulus Y. Write the combined results to CSV.
- Output file: `/app/outputs/fracture_data.csv`
- Format: csv
- Contract: Columns: a0_nm, orientation, Young_modulus_MD_Nm, fracture_stress_MD_Nm, fracture_stress_Griffith_Nm. Rows for every combination of a0 and orientation.
- Scoring: scored by hidden verifier

### Step 6: Temperature dependence for a fixed crack length
- Role: scored
- Action: Run tensile MD simulations on the pre‑cracked sheet with a0 = 4.1 nm at temperatures 1 K, 100 K, 200 K, 300 K, 400 K, 500 K, 600 K, in both armchair and zigzag directions. For each simulation extract fracture stress, fracture strain, elastic modulus (Young’s modulus), and toughness (area under curve). Compile into CSV.
- Output file: `/app/outputs/temperature_dependence.csv`
- Format: csv
- Contract: Columns: temp_K, orientation, fracture_stress_Nm, fracture_strain_pct, elastic_modulus_Nm, toughness_Nm. Rows for each temperature and orientation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energy.json`
- `/app/outputs/pristine_validation.csv`
- `/app/outputs/fracture_data.csv`
- `/app/outputs/temperature_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energy.json
- path: `/app/outputs/surface_energy.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Surface (edge) energy of monolayer InSe computed from MD energy differences.
- schema:
  - `type`: object
  - `required`:
    - `gamma_value`: number
    - `units`: string
    - `method`: string

### pristine_validation.csv
- path: `/app/outputs/pristine_validation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Pristine mechanical properties (Young’s modulus, UTS, fracture strain) for validation.
- schema:
  - `type`: table
  - `required_columns`: `temp_K`, `direction`, `Young_modulus_Nm`, `UTS_Nm`, `fracture_strain_pct`

### fracture_data.csv
- path: `/app/outputs/fracture_data.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: MD fracture stresses and Griffith predictions for crack‑length series at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `a0_nm`, `orientation`, `Young_modulus_MD_Nm`, `fracture_stress_MD_Nm`, `fracture_stress_Griffith_Nm`

### temperature_dependence.csv
- path: `/app/outputs/temperature_dependence.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Temperature‑dependent mechanical properties of a pre‑cracked SLInSe sheet.
- schema:
  - `type`: table
  - `required_columns`: `temp_K`, `orientation`, `fracture_stress_Nm`, `fracture_strain_pct`, `elastic_modulus_Nm`, `toughness_Nm`

Notes: Scoring uses tolerance‑based comparison against hidden paper‑reported values, plus trend consistency check (monotonic decrease of fracture stress with crack length, systematic deviation from Griffith prediction).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma_value": "number",
          "units": "string",
          "method": "string"
        }
      },
      "description": "Surface (edge) energy of monolayer InSe computed from MD energy differences."
    },
    {
      "file": "pristine_validation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temp_K",
          "direction",
          "Young_modulus_Nm",
          "UTS_Nm",
          "fracture_strain_pct"
        ]
      },
      "description": "Pristine mechanical properties (Young’s modulus, UTS, fracture strain) for validation."
    },
    {
      "file": "fracture_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0_nm",
          "orientation",
          "Young_modulus_MD_Nm",
          "fracture_stress_MD_Nm",
          "fracture_stress_Griffith_Nm"
        ]
      },
      "description": "MD fracture stresses and Griffith predictions for crack‑length series at 300 K."
    },
    {
      "file": "temperature_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temp_K",
          "orientation",
          "fracture_stress_Nm",
          "fracture_strain_pct",
          "elastic_modulus_Nm",
          "toughness_Nm"
        ]
      },
      "description": "Temperature‑dependent mechanical properties of a pre‑cracked SLInSe sheet."
    }
  ],
  "notes": "Scoring uses tolerance‑based comparison against hidden paper‑reported values, plus trend consistency check (monotonic decrease of fracture stress with crack length, systematic deviation from Griffith prediction)."
}
```

## How you are scored
A hidden verifier independently inspects each scored artifact after you finish.  It checks the computed values (surface energy, elastic moduli, fracture stresses, etc.) against reference expectations and validates structural requirements such as consistent relationships between quantities.  Each artifact contributes a weight to the final reward, which is a single number between 0 and 1.  Only the outputs written to `/app/outputs` are evaluated; the exact checking rules, reference values, and tolerances are kept secret to ensure the task must be solved by performing the requested MD simulations, not by guessing or reverse‑engineering the answers.
