# Phonon dispersion and vibrational density of states of a simple cubic lattice from elastic constants

## Problem background
The metal Polonium is the only element that forms a simple cubic lattice. Experimental study of its lattice dynamics is lacking. This work computes the bulk and surface vibrational properties of α-Po using a force-constant model, deriving nearest- and next-nearest-neighbor force constants from published ab initio elastic constants, then calculating phonon dispersions, surface phonons and resonances, and local vibrational density of states.

## Approach
The approach starts from given bulk elastic constants c11 and c12 and the simple cubic crystal structure. Using constitutive equations based on the Fuchs method for a simple cubic lattice, the central pair force constants between nearest and next-nearest-neighbor atoms are derived. With these force constants and the lattice constant, the bulk dynamical matrix is constructed and diagonalized for wavevectors along high-symmetry directions to obtain phonon dispersion branches. For the unreconstructed (001) surface, the matching method accounts for evanescent modes, and diagonalizing an enlarged dynamical matrix yields Rayleigh surface phonons and surface resonances. The Green's function formalism is then used to compute the local vibrational density of states for a bulk site and a surface site.

## Reproduction target
Given the elastic constants c11 = 113 GPa and c12 = 28 GPa from the referenced ab initio calculation, the lattice constant a = 3.36 Å, the atomic mass M = 3.49×10⁻²⁵ kg, and the characteristic frequency ω0 = 10.45×10¹² rad/s, implement the described workflow to (1) derive the nearest-neighbor force constant k1 and next-nearest-neighbor force constant k2; (2) compute the bulk phonon dispersion branches along [100], [110], and [111] as dimensionless frequency Ω versus normalized wavevector; (3) compute Rayleigh phonons and surface resonances along [010] on the unreconstructed (001) surface; and (4) compute the local vibrational density of states for a bulk site and for a site in the topmost atomic layer of the (001) surface. Submit the computed force constants, bulk dispersion, surface dispersion, and VDOS spectra in the specified output files.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Derive force constants
- Role: scored
- Action: Derive nearest-neighbor force constant k1 (N/m) and next-nearest-neighbor force constant k2 (N/m) from given elastic constants c11=113 GPa, c12=28 GPa, lattice constant a=3.36 Å, and atomic mass M=3.49e-25 kg using the Fuchs constitutive equations for a simple cubic lattice. Save the results.
- Output file: `/app/outputs/force_constants.json`
- Format: json
- Contract: {"k1": "float (N/m)", "k2": "float (N/m)"}
- Scoring: scored by hidden verifier

### Step 2: Compute bulk phonon dispersion
- Role: scored (load-bearing)
- Action: Construct the bulk dynamical matrix from the derived force constants, atomic mass, and lattice constant, and diagonalize it for wavevectors along high-symmetry directions [100], [110], and [111]. Output the dimensionless frequency Omega (omega / omega0, with omega0=10.45e12 rad/s) as a function of normalized wavevector for each phonon branch.
- Output file: `/app/outputs/bulk_dispersion.csv`
- Format: csv
- Contract: Columns: direction (string, one of [100],[110],[111]), q_norm (float, reduced wavevector 0 to 1), branch (int, 1/2/3), Omega (float, dimensionless frequency)
- Scoring: scored by hidden verifier

### Step 3: Compute surface phonons and resonances
- Role: scored
- Action: Using the matching method for the unreconstructed (001) surface, set up the enlarged dynamical matrix including evanescent modes and diagonalize it along the [010] direction. Extract Rayleigh phonon and surface resonance frequencies (Omega) as functions of reduced wavevector along [010].
- Output file: `/app/outputs/surface_dispersion.csv`
- Format: csv
- Contract: Columns: q_010 (float, reduced wavevector along [010]), Omega (float, dimensionless frequency), mode_type (string, 'Rayleigh' or 'resonance')
- Scoring: scored by hidden verifier

### Step 4: Compute vibrational density of states
- Role: scored
- Action: Using the Green's function formalism and the dynamical matrix, compute the local vibrational density of states (VDOS) for a bulk site and for a site in the topmost atomic layer of the (001) surface. Output the VDOS spectra as functions of Omega.
- Output file: `/app/outputs/vdos.csv`
- Format: csv
- Contract: Columns: Omega (float, dimensionless frequency), bulk_VDOS (float, arbitrary units), surface_VDOS (float, arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_constants.json`
- `/app/outputs/bulk_dispersion.csv`
- `/app/outputs/surface_dispersion.csv`
- `/app/outputs/vdos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_constants.json
- path: `/app/outputs/force_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Derived force constants k1 and k2. The values will be compared against the expected results with a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `k1`: float
    - `k2`: float

### bulk_dispersion.csv
- path: `/app/outputs/bulk_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Bulk phonon dispersion. The checker will recompute eigenvalues at hidden symmetry points from the submitted force constants and compare Omega values within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `q_norm`, `branch`, `Omega`
  - `columns`:
    - `direction`: string
    - `q_norm`: float
    - `branch`: int
    - `Omega`: float

### surface_dispersion.csv
- path: `/app/outputs/surface_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface phonon and resonance dispersion. The checker will validate Rayleigh mode frequencies lie below projected bulk bands and compare resonance positions within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `q_010`, `Omega`, `mode_type`
  - `columns`:
    - `q_010`: float
    - `Omega`: float
    - `mode_type`: string

### vdos.csv
- path: `/app/outputs/vdos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Local VDOS spectra. The checker will verify the overall shape (e.g., high-frequency Einstein mode at surface), peak locations, and that the spectra integrate to unit area.
- schema:
  - `type`: table
  - `required_columns`: `Omega`, `bulk_VDOS`, `surface_VDOS`
  - `columns`:
    - `Omega`: float
    - `bulk_VDOS`: float
    - `surface_VDOS`: float

Notes: All physical constants and input elastic constants are provided in the instruction. The agent must reimplement the Fuchs method and the matching procedure; no pre-computed intermediates are supplied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "k1": "float",
          "k2": "float"
        }
      },
      "description": "Derived force constants k1 and k2. The values will be compared against the expected results with a tolerance."
    },
    {
      "file": "bulk_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "q_norm",
          "branch",
          "Omega"
        ],
        "columns": {
          "direction": "string",
          "q_norm": "float",
          "branch": "int",
          "Omega": "float"
        }
      },
      "description": "Bulk phonon dispersion. The checker will recompute eigenvalues at hidden symmetry points from the submitted force constants and compare Omega values within a tolerance."
    },
    {
      "file": "surface_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_010",
          "Omega",
          "mode_type"
        ],
        "columns": {
          "q_010": "float",
          "Omega": "float",
          "mode_type": "string"
        }
      },
      "description": "Surface phonon and resonance dispersion. The checker will validate Rayleigh mode frequencies lie below projected bulk bands and compare resonance positions within tolerance."
    },
    {
      "file": "vdos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Omega",
          "bulk_VDOS",
          "surface_VDOS"
        ],
        "columns": {
          "Omega": "float",
          "bulk_VDOS": "float",
          "surface_VDOS": "float"
        }
      },
      "description": "Local VDOS spectra. The checker will verify the overall shape (e.g., high-frequency Einstein mode at surface), peak locations, and that the spectra integrate to unit area."
    }
  ],
  "notes": "All physical constants and input elastic constants are provided in the instruction. The agent must reimplement the Fuchs method and the matching procedure; no pre-computed intermediates are supplied."
}
```

## How you are scored
A hidden verifier independently checks each output artifact. For the force constants (Step 1), the verifier re-derives k1 and k2 and compares them within a tolerance. For the bulk dispersion (Step 2), eigenvalues at hidden symmetry points are recomputed from your submitted force constants and compared to your dispersion data. For the surface dispersion (Step 3), the verifier confirms that Rayleigh mode frequencies lie below the projected bulk bands and that resonance positions match within tolerance. For the VDOS (Step 4), the verifier checks overall shape features and verifies that the spectra integrate to unit area. Each stage contributes a fraction of the total reward, and the verifier combines them into a final score. Reporting numbers that match the paper is not enough; the verifier re-derives from your raw data.
