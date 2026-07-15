# EAM Phonon Dispersion and Surface Force Constants for Cu and Ag

## Problem background
Understanding the vibrational properties of metal surfaces is crucial for surface-related phenomena like catalysis and growth. The (111) surfaces of copper and silver are prototypical systems where experimental measurements (e.g., helium atom scattering, electron-energy-loss spectroscopy) have revealed surface phonon modes with frequencies that differ from the bulk. The embedded-atom method (EAM) provides a many-body description of metallic bonding that can predict surface phonon dispersion and force-constant modifications without fitting to surface data. This task sets out to compute the bulk phonon frequencies at high-symmetry points, the Rayleigh-wave (S1) frequency at the M point for the (111) surfaces, and the nearest-neighbour intralayer force-constant xx-component for both Cu and Ag, enabling a direct comparison with available experimental reference.

## Approach
The calculation is built on the embedded-atom method (EAM). The total energy is expressed as a sum of an embedding energy (which depends on the local electron density) and a short-ranged pair repulsion. The electron density at each atom is approximated by a linear superposition of atomic electron densities of neighbouring atoms. The interatomic force-constant tensors are obtained from the second derivatives of this total energy, yielding contributions from an environment-dependent effective pair potential and from many-body terms that involve the gradients of the electron density. The dynamical matrix for any wavevector is then constructed from these force constants; its eigenvalues give the squared phonon frequencies, and its eigenvectors give the polarizations.

To obtain bulk phonon frequencies, build a primitive fcc unit cell with the experimental lattice constant for Cu and for Ag. Evaluate the force constants using the EAM potential functions from Foiles et al. (1986). At each of the high-symmetry points Gamma, X, L, and K, form the dynamical matrix, diagonalise it, and record the three phonon frequencies.

For the (111) surface, construct a 63-layer slab with a vacuum gap and relax the atomic positions by energy minimisation using the same EAM potentials, thereby obtaining the equilibrium surface structure. Compute the slab dynamical matrix along the Gamma-M direction. Identify the Rayleigh wave (the S1 mode, which is primarily the first-layer transverse vibration) and report its frequency at the M point.

To extract the intralayer force constant, evaluate the force-constant tensor for the nearest-neighbour in-plane atom pair (atoms 1 and 2 in the (111) surface geometry) for both the bulk fcc crystal and the relaxed surface slab. The coordinate system aligns x with [\overline{1}10], y with [11\overline{2}], and z with [111]. From the K12 tensor, report the xx component, which is the dominant in-plane radial force constant. The EAM potential files are publicly available from the NIST Interatomic Potentials Repository or in LAMMPS distributions.

## Reproduction target
Produce three quantitative outputs:
1. **Bulk phonon frequencies at high-symmetry points**: For Cu and Ag, the phonon frequencies (in THz) at Gamma, X, L, and K. Each point has three branches. The result must be a CSV with exactly 24 rows (4 q-points × 3 branches × 2 materials).
2. **Surface Rayleigh wave (S1) frequency at the M point**: For Cu(111) and Ag(111) surfaces, the frequency (in THz) of the Rayleigh wave at the M point along the Gamma-M direction. One row per material.
3. **Intralayer force constant xx component**: For Cu and Ag, the xx component of the nearest-neighbour intralayer force-constant tensor K12, expressed in eV/Å², for the bulk fcc configuration and for the relaxed (111) surface configuration. Four rows in total.

All calculations must employ the EAM potential parameters from Foiles et al. (1986). The outputs must adhere exactly to the CSV schemas detailed in the workflow steps.

## Assets

- EAM potential files for Cu and Ag (Foiles, Baskes, Daw, 1986): https://www.ctcms.nist.gov/potentials/
- LAMMPS molecular dynamics package: https://lammps.sandia.gov
- Phonopy software: phonopy

## Workflow steps

### Step 1: Obtain EAM potential parameters
- Role: process
- Action: Retrieve the EAM potential parameter files for Cu and Ag (Foiles et al. 1986) from the NIST Interatomic Potentials Repository or the LAMMPS distribution.
- Evidence: `/app/outputs/potential_files.log`

### Step 2: Bulk phonon frequencies at high-symmetry points
- Role: scored
- Action: For each material (Cu, Ag), build a primitive fcc unit cell, compute force-constant tensors from the EAM total energy (using the embedding function, pair potential, and electron density via the linear superposition approximation), construct the dynamical matrix at Gamma, X, L, K points, diagonalize, and extract the three phonon frequencies. Output the frequencies at these points.
- Output file: `/app/outputs/bulk_phonon_frequencies.csv`
- Format: csv
- Contract: CSV with columns material (Cu|Ag), q_point (Gamma|X|L|K), branch_index (integer 1..3), frequency_THz (float). 24 rows total.
- Scoring: scored by hidden verifier

### Step 3: Relaxation of 63-layer (111) slabs
- Role: process
- Action: Build a 63-layer (111) slab for Cu and Ag with vacuum, and relax the atomic positions by energy minimization using the EAM potential.
- Evidence: `/app/outputs/slab_relaxation.xyz`

### Step 4: Surface Rayleigh wave frequency at M point
- Role: scored (load-bearing)
- Action: For each relaxed slab, compute the slab dynamical matrix and phonon dispersion along Gamma-M. Identify the Rayleigh wave (S1 mode, primarily first-layer transverse) and report its frequency at the M point.
- Output file: `/app/outputs/surface_rayleigh_frequency.csv`
- Format: csv
- Contract: CSV with columns material (Cu|Ag), q_point (M), symmetry_direction (GammaM), frequency_THz (float). One row per material.
- Scoring: scored by hidden verifier

### Step 5: Intralayer force constant K12_xx
- Role: scored (load-bearing)
- Action: Using the force-constant tensors evaluated from the EAM for bulk fcc and the relaxed surface slab, compute the nearest-neighbor intralayer force-constant tensor K12 for the atom pair 1-2 (in-plane nearest neighbor in the (111) surface geometry) and extract the xx component. Output the xx component values for bulk and relaxed surface configurations.
- Output file: `/app/outputs/force_constant_K12_xx.csv`
- Format: csv
- Contract: CSV with columns material (Cu|Ag), configuration (bulk|relaxed_surface), atom_pair (12), component (xx), value_eV_per_Ang2 (float). 4 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_phonon_frequencies.csv`
- `/app/outputs/surface_rayleigh_frequency.csv`
- `/app/outputs/force_constant_K12_xx.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_phonon_frequencies.csv
- path: `/app/outputs/bulk_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bulk phonon frequencies at Gamma, X, L, K for fcc Cu and Ag.
- schema:
  - `type`: table
  - `required_columns`: `material`, `q_point`, `branch_index`, `frequency_THz`
  - `units`:
    - `frequency_THz`: THz

### surface_rayleigh_frequency.csv
- path: `/app/outputs/surface_rayleigh_frequency.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Rayleigh wave (S1) frequency at M point along Gamma-M for Cu(111) and Ag(111).
- schema:
  - `type`: table
  - `required_columns`: `material`, `q_point`, `symmetry_direction`, `frequency_THz`
  - `units`:
    - `frequency_THz`: THz

### force_constant_K12_xx.csv
- path: `/app/outputs/force_constant_K12_xx.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: xx component of nearest-neighbor intralayer force constant for bulk and relaxed surface Cu and Ag.
- schema:
  - `type`: table
  - `required_columns`: `material`, `configuration`, `atom_pair`, `component`, `value_eV_per_Ang2`
  - `units`:
    - `value_eV_per_Ang2`: eV/Å²

Notes: The scored outputs are compared to paper-reported reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "q_point",
          "branch_index",
          "frequency_THz"
        ],
        "units": {
          "frequency_THz": "THz"
        }
      },
      "description": "Bulk phonon frequencies at Gamma, X, L, K for fcc Cu and Ag."
    },
    {
      "file": "surface_rayleigh_frequency.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "q_point",
          "symmetry_direction",
          "frequency_THz"
        ],
        "units": {
          "frequency_THz": "THz"
        }
      },
      "description": "Rayleigh wave (S1) frequency at M point along Gamma-M for Cu(111) and Ag(111)."
    },
    {
      "file": "force_constant_K12_xx.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "configuration",
          "atom_pair",
          "component",
          "value_eV_per_Ang2"
        ],
        "units": {
          "value_eV_per_Ang2": "eV/Å²"
        }
      },
      "description": "xx component of nearest-neighbor intralayer force constant for bulk and relaxed surface Cu and Ag."
    }
  ],
  "notes": "The scored outputs are compared to paper-reported reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates your three scored output files. For each output, the verifier compares your reported values to independently established reference values (derived from published experimental observations) using predetermined tolerances. The score for a given output is the fraction of data rows that fall within the required tolerance. The three per-output scores are then averaged with equal weight (1/3 each) to produce the final total reward, a number between 0 and 1. The verifier does not rely on you stating any particular previously reported number; it directly checks the CSV files you write. You should therefore compute the quantities faithfully from the EAM potentials and report your best numerical results.
