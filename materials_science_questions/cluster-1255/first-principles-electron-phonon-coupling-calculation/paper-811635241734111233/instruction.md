# First-principles calculation of lattice constants, electron-phonon coupling, and XRD of high-pressure PtH

## Problem background
High-pressure experiments on silane (SiH4) reported a superconducting transition with an unusual pressure dependence, but the underlying crystal structure remained elusive. It has been suggested that the measured signal may originate from a platinum hydride phase formed by reaction with the platinum electrodes, rather than from silane itself. Among proposed candidate phases, a hexagonal P6₃/mmc (NiAs-type) PtH structure has been identified as a plausible candidate at pressures around 110–160 GPa. This task addresses the key open question: can first-principles calculations for this PtH phase reproduce the experimentally observed lattice constants, superconducting properties, and X-ray diffraction pattern, thereby providing a consistent explanation for the experimental data?

## Approach
First-principles calculations are performed using density functional theory (DFT) within the generalized gradient approximation (GGA). The plane-wave pseudopotential method as implemented in Quantum ESPRESSO is used for all steps. The hexagonal P6₃/mmc unit cell is constructed with Pt atoms occupying Wyckoff position 2c (1/3, 2/3, 1/4) and H atoms at 2a (0,0,0). Geometry optimizations are carried out at fixed hydrostatic pressures of 113, 130, and 160 GPa, relaxing both atomic positions and lattice parameters to obtain equilibrium lattice constants a and c.

Phonon dispersion and density of states are computed via density functional perturbation theory (DFPT) using the relaxed structures. Electron-phonon coupling matrix elements are evaluated on a sufficiently fine grid of q-points and the Eliashberg function α²F(ω) is constructed. From these data, the electron-phonon coupling strength λ and the logarithmic average phonon frequency ω_log are extracted. The superconducting transition temperature Tc is estimated using the Allen-Dynes modified McMillan formula,

Tc = (ω_log / 1.2) exp{ -1.04(1+λ) / [λ - μ*(1+0.62λ)] },

with a Coulomb pseudopotential μ* = 0.1 (a typical representative value).

Finally, the powder X-ray diffraction pattern is simulated for the structure relaxed at 113 GPa using a wavelength of 0.3344 Å. Standard crystallographic methods (e.g., via pymatgen) are used to compute 2θ positions and relative intensities.

## Reproduction target
Produce the following scored artifacts:

- `/app/outputs/lattice_constants.json`: containing the optimized hexagonal lattice constants a and c (in Å) at each pressure: 113, 130, and 160 GPa.

- `/app/outputs/epc_properties.json`: containing the electron-phonon coupling strength λ (dimensionless), the logarithmic average phonon frequency ω_log (in K), and the superconducting transition temperature Tc (in K) at each of the three pressures, computed with μ* = 0.1.

- `/app/outputs/xrd_pattern.csv`: a simulated powder XRD pattern (wavelength 0.3344 Å) for the relaxed structure at 113 GPa, with columns `two_theta` (degrees) and `intensity` (arbitrary units).

The verifier will separately check each artifact against hidden reference values and also verify that Tc decreases monotonically from 113 to 160 GPa.

## Assets

- Quantum ESPRESSO (DFT/DFPT code): https://www.quantum-espresso.org/
- Pseudopotentials for Pt and H (ultrasoft, GGA-PBE or PW91): https://www.materialscloud.org/discover/sssp/
- Python XRD simulation package (pymatgen or diffpy): pymatgen

## Workflow steps

### Step 1: Build initial PtH structure
- Role: process
- Action: Construct the hexagonal P6₃/mmc PtH unit cell with Pt at Wyckoff 2c (fractional coordinates 0.333, 0.667, 0.25) and H at 2a (0.0, 0.0, 0.0). Use sensible initial lattice parameters (e.g., a=2.70 Å, c=4.53 Å) as a starting point for optimization.
- Evidence: `/app/outputs/initial_structure.cif`

### Step 2: Geometry optimization and lattice constants
- Role: scored
- Action: Perform DFT geometry optimization at fixed pressures of 113, 130, and 160 GPa. For each pressure, relax atomic positions and cell parameters. Extract the optimized hexagonal lattice constants a and c in Å.
- Output file: `/app/outputs/lattice_constants.json`
- Format: json
- Contract: JSON object with string keys '113', '130', '160' (GPa). Each value is an object with numeric fields 'a' and 'c' in Å. Example structure: {"113": {"a": <a_value>, "c": <c_value>}, ...}
- Scoring: scored by hidden verifier

### Step 3: Phonon and electron-phonon coupling calculation
- Role: process
- Action: Using the relaxed structures from step02, compute phonon dispersion, dynamical matrices, and electron-phonon coupling matrix elements via DFPT at pressures 113, 130, and 160 GPa. Output intermediate data (e.g., λ, α²F(ω), ω_log) for post-processing.
- Evidence: `/app/outputs/epc_intermediate.json`

### Step 4: Extract EPC parameters and Tc
- Role: scored (load-bearing)
- Action: From the electron-phonon coupling data, extract the coupling strength λ and the logarithmic average phonon frequency ω_log (in Kelvin) at each pressure. Compute the superconducting transition temperature Tc using the Allen-Dynes modified McMillan formula with a Coulomb pseudopotential μ* = 0.1.
- Output file: `/app/outputs/epc_properties.json`
- Format: json
- Contract: JSON object with string keys '113', '130', '160'. Each value is an object with numeric fields: 'lambda' (dimensionless), 'omega_log_K' (in K), 'Tc_K' (in K). Example structure: {"113": {"lambda": <value>, "omega_log_K": <value>, "Tc_K": <value>}, ...}
- Scoring: scored by hidden verifier

### Step 5: Simulate powder XRD pattern
- Role: scored
- Action: Using the structure relaxed at 113 GPa from step02, simulate the powder X-ray diffraction pattern with a wavelength of 0.3344 Å. Output the 2θ positions (in degrees) and relative intensities.
- Output file: `/app/outputs/xrd_pattern.csv`
- Format: csv
- Contract: CSV with two columns: 'two_theta' (float, in degrees) and 'intensity' (float, relative units). Wavelength = 0.3344 Å. Includes peaks from the relaxed structure.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.json`
- `/app/outputs/epc_properties.json`
- `/app/outputs/xrd_pattern.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.json
- path: `/app/outputs/lattice_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT-optimized hexagonal lattice constants of P6₃/mmc PtH at 113, 130, and 160 GPa. Compared to hidden reference values with a small absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `113`:
      - `a`: float_Å
      - `c`: float_Å
    - `130`:
      - `a`: float_Å
      - `c`: float_Å
    - `160`:
      - `a`: float_Å
      - `c`: float_Å

### epc_properties.json
- path: `/app/outputs/epc_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electron-phonon coupling strength λ, logarithmic average phonon frequency ω_log, and superconducting transition temperature Tc at three pressures. Hidden checker compares to paper-reported values and verifies Tc monotonicity.
- schema:
  - `type`: object
  - `required`:
    - `113`:
      - `lambda`: float_dimensionless
      - `omega_log_K`: float_K
      - `Tc_K`: float_K
    - `130`:
      - `lambda`: float_dimensionless
      - `omega_log_K`: float_K
      - `Tc_K`: float_K
    - `160`:
      - `lambda`: float_dimensionless
      - `omega_log_K`: float_K
      - `Tc_K`: float_K

### xrd_pattern.csv
- path: `/app/outputs/xrd_pattern.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated powder XRD pattern at 113 GPa, wavelength 0.3344 Å. The hidden checker validates peak positions and relative intensities against a reference.
- schema:
  - `type`: table
  - `required_columns`: `two_theta`, `intensity`
  - `units`:
    - `two_theta`: degrees
    - `intensity`: arbitrary_units

Notes: All scored outputs are re-derived from first-principles calculations. The hidden checker uses paper-reported values and simulated patterns as reference, with tolerances appropriate for the change in DFT code (VASP to Quantum ESPRESSO) and pseudopotential.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "113": {
            "a": "float_Å",
            "c": "float_Å"
          },
          "130": {
            "a": "float_Å",
            "c": "float_Å"
          },
          "160": {
            "a": "float_Å",
            "c": "float_Å"
          }
        }
      },
      "description": "DFT-optimized hexagonal lattice constants of P6₃/mmc PtH at 113, 130, and 160 GPa. Compared to hidden reference values with a small absolute tolerance."
    },
    {
      "file": "epc_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "113": {
            "lambda": "float_dimensionless",
            "omega_log_K": "float_K",
            "Tc_K": "float_K"
          },
          "130": {
            "lambda": "float_dimensionless",
            "omega_log_K": "float_K",
            "Tc_K": "float_K"
          },
          "160": {
            "lambda": "float_dimensionless",
            "omega_log_K": "float_K",
            "Tc_K": "float_K"
          }
        }
      },
      "description": "Electron-phonon coupling strength λ, logarithmic average phonon frequency ω_log, and superconducting transition temperature Tc at three pressures. Hidden checker compares to paper-reported values and verifies Tc monotonicity."
    },
    {
      "file": "xrd_pattern.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "two_theta",
          "intensity"
        ],
        "units": {
          "two_theta": "degrees",
          "intensity": "arbitrary_units"
        }
      },
      "description": "Simulated powder XRD pattern at 113 GPa, wavelength 0.3344 Å. The hidden checker validates peak positions and relative intensities against a reference."
    }
  ],
  "notes": "All scored outputs are re-derived from first-principles calculations. The hidden checker uses paper-reported values and simulated patterns as reference, with tolerances appropriate for the change in DFT code (VASP to Quantum ESPRESSO) and pseudopotential."
}
```

## How you are scored
The hidden verifier independently scores each output file. For `lattice_constants.json`, it compares the reported a and c values at each pressure to a reference with an appropriate tolerance (accounting for differences in DFT code and pseudopotential). For `epc_properties.json`, it compares λ, ω_log, and Tc to reference values and additionally verifies that Tc decreases as pressure increases. For `xrd_pattern.csv`, it matches peak positions (2θ) and relative intensity profiles against a reference pattern via cross-correlation. The scores from all artifacts are combined into a final reward between 0 and 1. Simply reporting published numbers without executing the DFT/DFPT workflow will not pass the checks.
