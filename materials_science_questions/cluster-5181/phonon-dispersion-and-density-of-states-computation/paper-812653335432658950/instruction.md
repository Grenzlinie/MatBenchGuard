# Phonon dispersion and density of states computation for Au/Ni superlattices

## Problem background
Metallic superlattices composed of alternating Au and Ni layers with a [111] texture have been observed to exhibit an anomalous enhancement of elastic moduli – the supermodulus effect – at short modulation wavelengths. Understanding this effect requires atomistic modeling of the interface structure and the calculation of vibrational local densities of states (LDOS), which can reveal changes in phonon behavior near the interface.

## Approach
You will construct atomistic models of FCC(111)-textured Au/Ni superlattices with layer periodicities ranging from 1/1 to 9/9. Interatomic interactions will be described by Morse pair potentials whose parameters are derived from reference bulk properties of Au and Ni (lattice constant, compressibility, vacancy formation energy) and combined for cross-interactions using standard combination rules. After relaxing the structures via molecular dynamics, you will compute the [111] Young's modulus by applying small uniaxial strains and fitting the potential energy as a function of squared strain. For the (3/3) structure you will compute vibrational LDOS for atoms at and away from the Au-Ni interface using the recursion method applied to the dynamical matrix derived from the Morse force constants.

## Reproduction target
Produce a CSV file with the computed [111] Young's modulus for each of the five modulation wavelengths (layer sequences 1/1, 3/3, 5/5, 7/7, 9/9). Separately, produce a CSV file containing the vibrational LDOS spectra for an Au atom at the interface, an Ni atom at the interface, an Au atom in the interior of an Au layer, and an Ni atom in the interior of an Ni layer in the relaxed (3/3) structure. The LDOS data must span frequencies from 0 to at least 10^13 Hz.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/
- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/

## Workflow steps

### Step 1: Collect reference properties
- Role: process
- Action: Obtain the bulk reference properties for pure Au and Ni: lattice constant a0 (Å), 0 K compressibility K (10^-12 cm²/dyn), and vacancy formation energy Efv (eV) from standard literature.
- Evidence: `/app/outputs/reference_properties.json`

### Step 2: Fit Morse potential parameters for Au-Au and Ni-Ni
- Role: process
- Action: From the reference properties, determine the three Morse potential parameters D, alpha, r0 for Au-Au and Ni-Ni interactions such that the potential reproduces a0, K, and Efv.
- Evidence: `/app/outputs/morse_parameters.json`

### Step 3: Derive Au-Ni cross-interaction parameters
- Role: process
- Action: Compute the Au-Ni Morse parameters using the combination rules D_AuNi = sqrt(D_Au * D_Ni), α_AuNi = 0.5*(α_Au + α_Ni), r0_AuNi = sqrt(α_Au * α_Ni) + ln(2)/α_AuNi.
- Evidence: `/app/outputs/morse_parameters.json`

### Step 4: Build superlattice models
- Role: process
- Action: Generate initial atomic coordinates for five FCC(111)-textured Au/Ni superlattices with layer periodicities 1/1, 3/3, 5/5, 7/7, 9/9 in cylindrical cells of radius ~20 Å containing ~2000 atoms, with periodic boundary conditions applied along the stacking [111] direction.
- Evidence: `/app/outputs/initial_structures.extxyz`

### Step 5: Relax structures by molecular dynamics
- Role: process
- Action: Relax all five superlattice models using molecular dynamics under the full Morse potential set (Au-Au, Ni-Ni, Au-Ni) to obtain equilibrium atomic positions and interplanar spacings.
- Evidence: `/app/outputs/relaxed_structures.extxyz`

### Step 6: Compute Young's modulus
- Role: scored (load-bearing)
- Action: For each relaxed superlattice, apply a series of small uniaxial strains ε along [111], recompute the potential energy W, and extract Young's modulus Y[111] from the quadratic fit W = 0.5 Y[111] ε². Create a CSV with modulation wavelength and corresponding Y[111] for all five layer sequences.
- Output file: `/app/outputs/youngs_modulus_per_lambda.csv`
- Format: csv
- Contract: Columns: modulation_wavelength (Å), Y111 (10^12 dyn/cm^2). One row per layer sequence (1/1, 3/3, 5/5, 7/7, 9/9).
- Scoring: scored by hidden verifier

### Step 7: Compute vibrational LDOS
- Role: scored
- Action: Using the relaxed (3/3) structure and the Morse potential force constants, apply the recursion method (at least 10 recursion levels) to compute the vibrational local density of states (LDOS) for an Au atom at the interface, an Ni atom at the interface, and the corresponding interior atoms. Write a CSV with frequency and LDOS for all four sites.
- Output file: `/app/outputs/ldos_data.csv`
- Format: csv
- Contract: Columns: frequency (Hz), LDOS_Au_interface, LDOS_Ni_interface, LDOS_Au_interior, LDOS_Ni_interior. Rows cover the frequency range from 0 to at least 10^13 Hz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/youngs_modulus_per_lambda.csv`
- `/app/outputs/ldos_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### youngs_modulus_per_lambda.csv
- path: `/app/outputs/youngs_modulus_per_lambda.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Young's modulus Y[111] as a function of modulation wavelength for Au/Ni superlattices.
- schema:
  - `type`: table
  - `required_columns`: `modulation_wavelength`, `Y111`
  - `units`:
    - `modulation_wavelength`: Angstrom
    - `Y111`: 10^12 dyn/cm^2

### ldos_data.csv
- path: `/app/outputs/ldos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Vibrational local density of states for interface and interior atoms in the Au/Ni (3/3) superlattice.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `LDOS_Au_interface`, `LDOS_Ni_interface`, `LDOS_Au_interior`, `LDOS_Ni_interior`
  - `units`:
    - `frequency`: Hz

Notes: The agent must produce both scored artifacts by executing the full pipeline. Young's modulus values are compared to reference values digitized from the paper's Figure 2 within a hidden absolute tolerance; at least four of five must be within tolerance and the overall trend must be monotonically decreasing with wavelength. For LDOS, the frequency of the maximum LDOS for interface atoms must lie within a hidden range and the interface peak must exceed the interior peak by a minimum ratio.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "youngs_modulus_per_lambda.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "modulation_wavelength",
          "Y111"
        ],
        "units": {
          "modulation_wavelength": "Angstrom",
          "Y111": "10^12 dyn/cm^2"
        }
      },
      "description": "Young's modulus Y[111] as a function of modulation wavelength for Au/Ni superlattices."
    },
    {
      "file": "ldos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "LDOS_Au_interface",
          "LDOS_Ni_interface",
          "LDOS_Au_interior",
          "LDOS_Ni_interior"
        ],
        "units": {
          "frequency": "Hz"
        }
      },
      "description": "Vibrational local density of states for interface and interior atoms in the Au/Ni (3/3) superlattice."
    }
  ],
  "notes": "The agent must produce both scored artifacts by executing the full pipeline. Young's modulus values are compared to reference values digitized from the paper's Figure 2 within a hidden absolute tolerance; at least four of five must be within tolerance and the overall trend must be monotonically decreasing with wavelength. For LDOS, the frequency of the maximum LDOS for interface atoms must lie within a hidden range and the interface peak must exceed the interior peak by a minimum ratio."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores each required output file. The verifier compares your computed Young's modulus values per wavelength and the LDOS peak positions and relative enhancements against reference results, without revealing the exact tolerances. Each artifact contributes a specific weight to the total score, and you must produce both artifacts to receive a non-zero reward. Simply reporting the paper's numbers is not sufficient; the artifacts must be generated by executing the described workflow.
