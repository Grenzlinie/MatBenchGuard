# First-principles study of stress-dependent mechanical stability and electronic properties of a 2D silicon carbide monolayer

## Problem background
Two-dimensional silicon carbide (2D-SiC) is a planar honeycomb monolayer analogous to graphene, composed of alternating Si and C atoms. It possesses a direct electronic band gap, making it a promising candidate for nanoelectronic and optoelectronic applications. Applying in-plane stress is an effective way to tune its mechanical and electronic properties, but the quantitative limits of mechanical stability, the ultimate tensile strength, and the strain-induced modifications of the electronic band gap have not been fully established. This work uses first-principles density functional theory (DFT) to systematically compute these properties under uniaxial (zigzag and armchair) and biaxial loading, characterizing the anisotropic stress-dependent mechanical response and the conditions under which the material becomes mechanically unstable or undergoes a semiconductor-to-metal transition.

## Approach
The approach employs Kohn-Sham density functional theory with a generalized gradient approximation (PBE) exchange-correlation functional. The 2D-SiC monolayer is modeled in a periodic supercell with an out-of-plane vacuum layer to isolate the sheet. Starting from the relaxed hexagonal lattice, a series of in-plane Lagrangian strain values is applied for uniaxial (zigzag, armchair) and biaxial deformation. Self-consistent DFT calculations are performed at each strain to obtain total energies, stress tensors, Kohn-Sham eigenvalues, and charge densities. From the stress-strain data, second-order elastic constants are extracted; the Born-Huang mechanical stability criteria are then applied to identify the critical stresses at which stability is lost. Stress-strain curves are constructed to determine the ultimate tensile strength. The electronic band gap is computed from the Kohn-Sham eigenvalues at equilibrium and at selected stress levels to track any direct-to-indirect transitions or metallization. Finally, Bader charge analysis is performed on the charge density to quantify the ionic character of the material.

## Reproduction target
Using first-principles DFT calculations on a 2D-SiC monolayer, produce the following: (i) the ambient in-plane second-order elastic constants C11 and C12 (in N/m); (ii) for uniaxial zigzag, uniaxial armchair, and biaxial loading, the critical stress values (N/m) where mechanical stability is lost according to the Born-Huang criteria — the compressive stability limit, the tensile stability limit, and the compressive failure stress where C12 ≥ C11; (iii) the ultimate tensile strength (maximum tensile stress, N/m) for each loading direction; (iv) the electronic band gap (eV) at zero stress and at representative stress points that include the compressive failure stress, the tensile stability boundary, and a high tensile stress where the band gap becomes zero, for each loading geometry; (v) from Bader charge analysis on the undeformed cell, the atom type (C or Si) that carries the maximum charge density, and its value (e/Å³).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Si and C: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Structure preparation
- Role: process
- Action: Generate the initial SiC unit cell (hexagonal cell for biaxial, orthorhombic non-primitive cell for uniaxial) using the literature lattice constant of 3.10 Å and planar atomic positions.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: DFT relaxation of undeformed cell
- Role: process
- Action: Perform a full relaxation (cell and atomic positions) for the hexagonal unit cell and the orthorhombic cell using Quantum ESPRESSO (PBE functional, appropriate pseudopotentials, sufficient k-point grid and energy cutoff for convergence). Ensure the relaxed lattice constant matches the literature value and obtain the equilibrium total energy.
- Evidence: `/app/outputs/relaxation_summary.json`

### Step 3: DFT calculations over uniaxial and equi-biaxial strain grids
- Role: process
- Action: For the uniaxial zigzag, uniaxial armchair, and equi-biaxial loading cases, run Quantum ESPRESSO self-consistent calculations at Lagrangian strain values from -0.2 to 0.3 in increments of 0.02. For each strain, compute total energy, stress tensor, Kohn-Sham eigenvalues, and charge density. Use computational settings comparable to the paper (PBE functional, appropriate k-mesh and cutoff).
- Evidence: `/app/outputs/strain_grid_summary.json`

### Step 4: DFT calculations for unequal biaxial strain grid
- Role: process
- Action: For the orthorhombic cell, run Quantum ESPRESSO calculations on a grid of independent strains ε_x and ε_y from -0.1 to 0.1 with 0.02 increments. Collect total energies and stress tensors for each (ε_x, ε_y) combination.
- Evidence: `/app/outputs/unequal_biaxial_grid_summary.json`

### Step 5: Extract ambient second-order elastic constants
- Role: scored
- Action: From the DFT stress-strain data of the undeformed (strain=0) configuration, compute the ambient in-plane second-order elastic constants C11 and C12 (in N/m) for the hexagonal cell. Output the values to ambient_elastic_constants.txt.
- Output file: `/app/outputs/ambient_elastic_constants.txt`
- Format: txt
- Contract: Two floating-point numbers in N/m, one per line (first line C11, second line C12).
- Scoring: scored by hidden verifier

### Step 6: Determine mechanical stability thresholds
- Role: scored (load-bearing)
- Action: Using the strain-dependent second-order elastic constants extracted from the uniaxial/equi-biaxial data, apply the Born-Huang stability criteria (C11 > C12, C11² - C11*C12 > 0) for each stress state. Identify for each loading type (zigzag, armchair, biaxial) the compressive stress at which stability is lost, the tensile stress at which stability is lost, and the compressive failure stress where C12 ≥ C11. Output the results to mechanical_stability_thresholds.csv.
- Output file: `/app/outputs/mechanical_stability_thresholds.csv`
- Format: csv
- Contract: Columns: loading_type (zigzag, armchair, biaxial), compressive_stability_limit_Nm (float), tensile_stability_limit_Nm (float), compressive_failure_stress_Nm (float).
- Scoring: scored by hidden verifier

### Step 7: Compute ultimate tensile strength
- Role: scored
- Action: From the full stress-strain data, construct stress-strain curves for uniaxial zigzag, uniaxial armchair, and biaxial loading. Identify the maximum tensile stress (UTS) for each case. Write the values to ultimate_tensile_strength.csv.
- Output file: `/app/outputs/ultimate_tensile_strength.csv`
- Format: csv
- Contract: Columns: loading_type (zigzag, armchair, biaxial), UTS_Nm (float).
- Scoring: scored by hidden verifier

### Step 8: Compute band gap as function of stress
- Role: scored
- Action: From the Kohn-Sham eigenvalues obtained at equilibrium and at selected stress points (at the compressive failure stress for each geometry, at the tensile stability boundary for armchair and biaxial, and at a tensile stress near the semiconductor-to-metal transition), determine the electronic band gap (in eV). Record the values in band_gap_vs_stress.csv.
- Output file: `/app/outputs/band_gap_vs_stress.csv`
- Format: csv
- Contract: Columns: loading_type (zigzag, armchair, biaxial), stress_Nm (float), band_gap_eV (float). Include data at equilibrium (stress=0), at the failure compressive stress, and at the tensile stability boundary for each direction, and at a high tensile stress where band gap becomes zero.
- Scoring: scored by hidden verifier

### Step 9: Charge density analysis
- Role: scored
- Action: Perform Bader charge analysis on the charge density of the undeformed cell and, optionally, on the maximally strained configurations. Locate the atom with the maximum charge density and record its identity and value. Output the results to charge_analysis.json.
- Output file: `/app/outputs/charge_analysis.json`
- Format: json
- Contract: Keys: 'max_charge_density_atom' (string, 'C' or 'Si'), 'max_charge_density_value' (float, units e/Å³).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ambient_elastic_constants.txt`
- `/app/outputs/mechanical_stability_thresholds.csv`
- `/app/outputs/ultimate_tensile_strength.csv`
- `/app/outputs/band_gap_vs_stress.csv`
- `/app/outputs/charge_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ambient_elastic_constants.txt
- path: `/app/outputs/ambient_elastic_constants.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Two floating-point numbers in N/m, one per line: first line C11, second line C12.
- schema:
  - `type`: text
  - `columns`:
  - `fields`:

### mechanical_stability_thresholds.csv
- path: `/app/outputs/mechanical_stability_thresholds.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Critical stress values (N/m) where mechanical stability criteria fail. Each row corresponds to one loading geometry.
- schema:
  - `type`: table
  - `columns`: `loading_type`, `compressive_stability_limit_Nm`, `tensile_stability_limit_Nm`, `compressive_failure_stress_Nm`
  - `fields`:
    - `loading_type`: string
    - `compressive_stability_limit_Nm`: float
    - `tensile_stability_limit_Nm`: float
    - `compressive_failure_stress_Nm`: float

### ultimate_tensile_strength.csv
- path: `/app/outputs/ultimate_tensile_strength.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ultimate tensile strength (N/m) for each loading direction.
- schema:
  - `type`: table
  - `columns`: `loading_type`, `UTS_Nm`
  - `fields`:
    - `loading_type`: string
    - `UTS_Nm`: float

### band_gap_vs_stress.csv
- path: `/app/outputs/band_gap_vs_stress.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electronic band gap (eV) at selected stress levels for each loading geometry.
- schema:
  - `type`: table
  - `columns`: `loading_type`, `stress_Nm`, `band_gap_eV`
  - `fields`:
    - `loading_type`: string
    - `stress_Nm`: float
    - `band_gap_eV`: float

### charge_analysis.json
- path: `/app/outputs/charge_analysis.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Bader charge analysis result: the atom with highest charge density and its value.
- schema:
  - `type`: object
  - `required`: `max_charge_density_atom`, `max_charge_density_value`
  - `items`:
    - `max_charge_density_atom`: string
    - `max_charge_density_value`: float (e/Å³)

Notes: All output files are scored against reference values/tolerances derived from the published results. The checker expects valid formatting and quantities in the specified units.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ambient_elastic_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "columns": [],
        "fields": []
      },
      "description": "Two floating-point numbers in N/m, one per line: first line C11, second line C12."
    },
    {
      "file": "mechanical_stability_thresholds.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "columns": [
          "loading_type",
          "compressive_stability_limit_Nm",
          "tensile_stability_limit_Nm",
          "compressive_failure_stress_Nm"
        ],
        "fields": {
          "loading_type": "string",
          "compressive_stability_limit_Nm": "float",
          "tensile_stability_limit_Nm": "float",
          "compressive_failure_stress_Nm": "float"
        }
      },
      "description": "Critical stress values (N/m) where mechanical stability criteria fail. Each row corresponds to one loading geometry."
    },
    {
      "file": "ultimate_tensile_strength.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "columns": [
          "loading_type",
          "UTS_Nm"
        ],
        "fields": {
          "loading_type": "string",
          "UTS_Nm": "float"
        }
      },
      "description": "Ultimate tensile strength (N/m) for each loading direction."
    },
    {
      "file": "band_gap_vs_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "columns": [
          "loading_type",
          "stress_Nm",
          "band_gap_eV"
        ],
        "fields": {
          "loading_type": "string",
          "stress_Nm": "float",
          "band_gap_eV": "float"
        }
      },
      "description": "Electronic band gap (eV) at selected stress levels for each loading geometry."
    },
    {
      "file": "charge_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "max_charge_density_atom",
          "max_charge_density_value"
        ],
        "items": {
          "max_charge_density_atom": "string",
          "max_charge_density_value": "float (e/Å³)"
        }
      },
      "description": "Bader charge analysis result: the atom with highest charge density and its value."
    }
  ],
  "notes": "All output files are scored against reference values/tolerances derived from the published results. The checker expects valid formatting and quantities in the specified units."
}
```

## How you are scored
Each scored artifact listed in the Output contract is evaluated independently by a hidden verifier. The verifier compares your submitted quantities to reference values derived from the paper's reported results, using pre-defined tolerances and/or directional checks. Elastic constants, stability thresholds, and tensile strengths are compared to expected values with tolerances that account for implementation differences; band gaps are checked for correct trends (e.g., decreasing with tensile stress, vanishing at metallization) and approximate values; the charge analysis is checked for the correct atom and a density above a threshold. The per-artifact scores are combined by weight into a final reward between 0 and 1. Executing the full workflow and producing the required files is essential; simply reporting published numbers is not sufficient and may not yield a valid score.
