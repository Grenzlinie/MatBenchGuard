# DFT-based Optical Property Reproduction for BaSe1-xTex Alloys

## Problem background
Optoelectronic devices rely on wide-band-gap semiconductors with tunable optical properties, and BaSe₁₋ₓTeₓ alloys are candidate materials in this family. Their optical response — including absorption onset, refractive index, and plasmon features — determines suitability for applications like laser diodes and light-emitting diodes. Predicting these properties across the composition range requires accurate first-principles electronic structure calculations. This task reproduces the key optical quantities that govern device performance, providing a computational benchmark for the alloy system.

## Approach
The optical properties are derived from the frequency-dependent complex dielectric function ε(ω) = ε₁(ω) + iε₂(ω). The workflow uses density functional theory (DFT) with the GGA+mBJ exchange-correlation functional, which captures band gaps more accurately than standard GGA. First, the equilibrium lattice constants are obtained for each composition via total-energy optimization with the GGA-PBEsol functional. Second, using the optimized structures, a self-consistent electronic structure calculation is performed with GGA+mBJ to obtain the ground-state charge density and wavefunctions. Third, the imaginary part ε₂(ω) is computed directly from the momentum matrix elements on a fine k-point grid in the range 0–35 eV. The real part ε₁(ω) is then obtained from ε₂(ω) through the Kramers–Kronig relation. From these dielectric functions, the optical absorption onset (the energy where ε₂ first rises above zero), the static refractive index n₀ = √ε₁(0), and the energy-loss function L(ω) = ε₂/(ε₁²+ε₂²) are derived; the main plasmon peak above 10 eV is identified as the maximum of L(ω). The calculations are carried out with the open-source Quantum ESPRESSO code to ensure full reproducibility, as the procedure is the experiment.

## Reproduction target
Produce the following quantities for the five alloy compositions BaSe₁₋ₓTeₓ with x = 0, 0.25, 0.5, 0.75, 1:
1. Equilibrium lattice constant a₀ (Å) from GGA-PBEsol structural optimization, stored in lattice_constants.csv.
2. Optical absorption onset energy (eV) extracted from ε₂(ω) as the first photon energy where ε₂ exceeds a small positive threshold, stored in absorption_onsets.csv.
3. Static refractive index n₀ = √ε₁(0), computed via Kramers–Kronig transformation of ε₂(ω), stored in static_refractive_index.csv.
4. Main plasmon peak energy (eV) above 10 eV from the energy-loss function L(ω) = ε₂/(ε₁²+ε₂²), stored in plasmon_peak_energies.csv.
All outputs are CSV tables with columns for composition index x and the corresponding value. The raw ε₂(ω) arrays used to derive these values must be saved in an HDF5 archive (dielectric_data.h5) to enable a recomputation-based verification.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- libxc: libxc
- Pseudopotentials (Ba, Se, Te): https://www.quantum-espresso.org/pseudopotentials/
- Python libraries (ase, numpy, scipy, h5py): ase, numpy, scipy, h5py

## Workflow steps

### Step 1: Structural optimization and lattice constants
- Role: scored
- Action: For each composition x = 0, 0.25, 0.5, 0.75, 1, set up the cubic NaCl-type (Fm-3m) 8-atom unit cell. Perform DFT total-energy vs. volume optimization using the GGA-PBEsol functional and fit the Birch-Murnaghan equation of state to obtain the equilibrium lattice constant a0. Store the results in lattice_constants.csv.
- Output file: `/app/outputs/lattice_constants.csv`
- Format: csv
- Contract: columns: x, a0_angstrom
- Scoring: scored by hidden verifier

### Step 2: Electronic structure SCF with GGA+mBJ
- Role: process
- Action: Using the optimized structures from step_01 and the GGA+mBJ functional, perform self-consistent field (SCF) calculations to obtain converged charge densities and wavefunctions for all compositions. This provides the ground-state electronic structure for subsequent optical calculations.
- Evidence: `/app/outputs/scf.log`

### Step 3: Compute raw optical dielectric function
- Role: process
- Action: On the SCF results from step_02, perform a non-self-consistent field calculation with a dense k-point mesh using GGA+mBJ to compute the momentum matrix elements and the imaginary part of the dielectric function ε₂(ω) for photon energies 0–35 eV. Save the complete ε₂(ω) arrays for each composition in a single HDF5 archive (dielectric_data.h5).
- Evidence: `/app/outputs/dielectric_data.h5`

### Step 4: Extract optical absorption onsets
- Role: scored
- Action: From the ε₂(ω) arrays in dielectric_data.h5, determine the absorption onset energy for each composition as the first photon energy where ε₂ exceeds a small positive threshold. Write the onsets to absorption_onsets.csv.
- Output file: `/app/outputs/absorption_onsets.csv`
- Format: csv
- Contract: columns: x, onset_eV
- Scoring: scored by hidden verifier

### Step 5: Compute static refractive index
- Role: scored
- Action: Using the ε₂(ω) data, compute ε₁(ω) via the Kramers–Kronig relation, extract the zero-frequency limit ε₁(0), and calculate the static refractive index n₀ = sqrt(ε₁(0)) for each composition. Output the values to static_refractive_index.csv.
- Output file: `/app/outputs/static_refractive_index.csv`
- Format: csv
- Contract: columns: x, n0
- Scoring: scored by hidden verifier

### Step 6: Compute plasmon peak energies
- Role: scored (load-bearing)
- Action: From ε₁(ω) and ε₂(ω) for each composition, compute the energy-loss function L(ω) = ε₂/(ε₁²+ε₂²). Identify the main plasmon peak as the energy above 10 eV where L(ω) reaches its maximum. Write the peak energies to plasmon_peak_energies.csv.
- Output file: `/app/outputs/plasmon_peak_energies.csv`
- Format: csv
- Contract: columns: x, plasmon_peak_eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.csv`
- `/app/outputs/absorption_onsets.csv`
- `/app/outputs/static_refractive_index.csv`
- `/app/outputs/plasmon_peak_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.csv
- path: `/app/outputs/lattice_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constant from GGA-PBEsol optimization for each composition.
- schema:
  - `type`: table
  - `required_columns`: `x`, `a0_angstrom`
  - `units`:
    - `x`: dimensionless
    - `a0_angstrom`: angstrom

### absorption_onsets.csv
- path: `/app/outputs/absorption_onsets.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Optical absorption onset energy extracted from ε₂(ω) for each composition.
- schema:
  - `type`: table
  - `required_columns`: `x`, `onset_eV`
  - `units`:
    - `x`: dimensionless
    - `onset_eV`: eV

### static_refractive_index.csv
- path: `/app/outputs/static_refractive_index.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Static refractive index n₀ = sqrt(ε₁(0)) for each composition.
- schema:
  - `type`: table
  - `required_columns`: `x`, `n0`
  - `units`:
    - `x`: dimensionless
    - `n0`: dimensionless

### plasmon_peak_energies.csv
- path: `/app/outputs/plasmon_peak_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Main plasmon peak energy from energy-loss function L(ω) for each composition.
- schema:
  - `type`: table
  - `required_columns`: `x`, `plasmon_peak_eV`
  - `units`:
    - `x`: dimensionless
    - `plasmon_peak_eV`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "a0_angstrom"
        ],
        "units": {
          "x": "dimensionless",
          "a0_angstrom": "angstrom"
        }
      },
      "description": "Equilibrium lattice constant from GGA-PBEsol optimization for each composition."
    },
    {
      "file": "absorption_onsets.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "onset_eV"
        ],
        "units": {
          "x": "dimensionless",
          "onset_eV": "eV"
        }
      },
      "description": "Optical absorption onset energy extracted from ε₂(ω) for each composition."
    },
    {
      "file": "static_refractive_index.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "n0"
        ],
        "units": {
          "x": "dimensionless",
          "n0": "dimensionless"
        }
      },
      "description": "Static refractive index n₀ = sqrt(ε₁(0)) for each composition."
    },
    {
      "file": "plasmon_peak_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "plasmon_peak_eV"
        ],
        "units": {
          "x": "dimensionless",
          "plasmon_peak_eV": "eV"
        }
      },
      "description": "Main plasmon peak energy from energy-loss function L(ω) for each composition."
    }
  ],
  "notes": ""
}
```

## How you are scored
Each scored artifact is independently checked by a hidden verifier. The verifier reads your raw dielectric data archive (dielectric_data.h5) and recomputes the absorption onsets, static refractive indices, and plasmon peak energies using the same definitions; it then compares the recomputed values to the quantities in your submitted CSV files. The lattice constants are compared directly against a reference result. The verification stages are weighted, and the overall reward is a number between 0 and 1 that reflects the consistency and accuracy of your computed optical properties. Reporting values that match the expected physical trends without genuine execution of the DFT workflow is not sufficient—the verifier's recomputation from your raw data ensures that the submitted quantities are derived from a real dielectric function calculation.
