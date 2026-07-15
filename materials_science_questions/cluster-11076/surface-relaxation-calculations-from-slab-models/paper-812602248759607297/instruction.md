# Computing surface-phonon dispersion of NiAl(110) using lattice dynamics

## Problem background
Surface-phonon dispersion of the ordered alloy NiAl(110) provides key insights into the vibrational properties and surface relaxation of compositionally ordered intermetallic surfaces. Electron energy-loss spectroscopy (EELS) measurements have revealed several surface-phonon branches along the Γ–Y ([100]) and Γ–X ([110]) directions. The surface-termination rippling, where first-layer Ni atoms move inward and Al atoms outward relative to the bulk-terminated positions, strongly influences the phonon frequencies. In this task you will compute the dispersion of the even surface-phonon modes (the modes observable in the EELS experiment) using a surface-adjusted Born–von Kármán lattice-dynamical model. The result is a set of phonon frequencies as a function of reduced wavevector, which can be compared with experimental data to verify the surface-force-constant model.

## Approach
The calculation uses a third-nearest-neighbour central-force Born–von Kármán model applied to a 15-layer NiAl(110) slab. The slab is constructed from the CsCl crystal structure (lattice constant a = 2.887 Å) with the experimentally determined surface rippling: first-layer Ni atoms are displaced inward by 6% and first-layer Al atoms outward by 4.6% (relative to the bulk interlayer spacing).

For each required reduced wavevector ζ along Γ–Y and Γ–X, the dynamical matrix is built using the force constants of the MS (modified surface) model. This model includes bulk third-nearest-neighbour central force constants and specific surface adjustments that account for the rippled relaxation. The eigenvalue problem is solved to obtain phonon eigenfrequencies and eigenvectors. From the full set of slab modes you must identify the *even* modes with respect to the sagittal plane (the plane that coincides with the scattering plane in EELS). These even modes are the surface-localised branches that produce significant intensity in the experiment.

The force constants to be used are given below (the MS model). The notation φ″ is the longitudinal (stretching) central force constant and φ′ is the tangential (bending) component; the subscript indicates the atom pair and the layer environment.

**Bulk central force constants (all interactions up to third-nearest neighbours, identical for the MB and MS models)**

| Pair | Distance (Å) | φ″ (dyn/cm) | φ′ (dyn/cm) |
|----------|----------------|-------------|-------------|
| Ni–Al (1NN) | 2.50 | 31420 | 1150 |
| Al–Al (2NN) | 2.89 | 18380 | 760 |
| Ni–Ni (2NN) | 2.89 | 2180 | –440 |
| Al–Al (3NN) | 4.08 | 4036 | –1484 |
| Ni–Ni (3NN) | 4.08 | 4760 | –620 |

**Surface-force-constant adjustments (MS model)**

These replace or modify the corresponding bulk φ″ and φ′ values for the specified near-surface pairs:

- φ″ between first-layer Al and second-layer Ni: **25136** dyn/cm
- φ″ between first-layer Ni and second-layer Al: **47130** dyn/cm
- φ″ between first-layer Ni and second-layer Ni: **3052** dyn/cm
- φ″ between first-layer Ni and third-layer Ni: **6664** dyn/cm
- Intralayer tangential force constant φ′ between second-nearest-neighbour Ni atoms in the first layer: **2000** dyn/cm (bulk value –440)
- Intralayer tangential force constant φ′ between third-nearest-neighbour Ni atoms in the first layer: **–2000** dyn/cm (bulk value –620)

The slab forces on surface atoms must be balanced; you may use the following surface-balanced φ′ values (all other φ′ values are unchanged from the bulk):

- φ′ between first-layer Al and second-layer Ni: 264 dyn/cm
- φ′ between first-layer Ni and second-layer Ni: 145 dyn/cm
- φ′ between first-layer Al and second-layer Al: 724 dyn/cm

Using these constants, set up the dynamical matrix for each wavevector, diagonalise, and collect the even surface-mode frequencies. The slab has 15 layers (30 atoms per 2D unit cell); convergence of surface-localised modes is sufficient with this thickness.

## Reproduction target
Produce a CSV file, `phonon_dispersion.csv`, containing the even surface-phonon frequencies (in cm⁻¹) computed from the MS force-constant model at a representative set of reduced wavevectors ζ along the Γ–Y ([100]) and Γ–X ([110]) directions.  
Each row must contain:
- `direction`: either `"GY"` (for Γ–Y) or `"GX"` (for Γ–X);
- `reduced_wavevector`: a float between 0 and 1;
- `frequency_cm1`: a positive float – the phonon frequency in cm⁻¹.

Include one row per resolved even-mode branch per wavevector. Cover both directions with enough points to trace the main dispersion branches; for example, at least 5 points in the range ζ = 0.2–1.0 for each direction, and ensure that the lowest acoustic branch and the gap modes are represented. The file will be evaluated against hidden experimental data without reference to any particular figure or table from the source paper.

## Assets

- NiAl crystal structure parameters and atomic masses

## Workflow steps

### Step 1: Build the NiAl(110) slab with surface rippling
- Role: process
- Action: Generate atomic coordinates for a 15-layer NiAl(110) slab in the CsCl structure (lattice constant 2.887 Å). Apply the experimentally determined surface rumpling: first-layer Ni atoms displaced inward by 6%, first-layer Al atoms displaced outward by 4.6%. Save the slab coordinates (species, x, y, z) to slab_coords.csv.
- Evidence: `/app/outputs/slab_coords.csv`

### Step 2: Compute surface-phonon dispersion and output even modes
- Role: scored (load-bearing)
- Action: Using the slab coordinates and the surface-adjusted force constants from the MS model (provided in the task instruction: Table I with explicit φ'' and φ' values), set up the dynamical matrix for a set of reduced wavevectors ζ along the Γ–Y and Γ–X directions. Solve the eigenvalue problem to obtain phonon eigenfrequencies and eigenvectors. For each ζ and direction, identify the even modes (observable in the EELS experiment) and output their frequencies. Write the results to phonon_dispersion.csv.
- Output file: `/app/outputs/phonon_dispersion.csv`
- Format: csv
- Contract: direction (string: GY or GX), reduced_wavevector (float, 0 to 1), frequency_cm1 (float, cm⁻¹). One row per resolved mode per wavevector. Both directions must be covered.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_dispersion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_dispersion.csv
- path: `/app/outputs/phonon_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Agent-computed surface-phonon frequencies. The checker extracts the frequencies, pairs them with hidden experimental points at matching direction and reduced wavevector, computes the RMSE, and awards credit based on a pre-set hidden threshold.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `reduced_wavevector`, `frequency_cm1`
  - `units`:
    - `frequency_cm1`: cm^{-1}
  - `notes`: direction must be either 'GY' or 'GX'; reduced_wavevector in [0,1]; frequency_cm1 positive float.

Notes: The hidden checker uses digitized experimental dispersion data from the source paper to compute an RMSE. The scoring function is monotonic: lower RMSE yields higher reward. The agent must not rely on any particular RMSE threshold as it is unknown to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "reduced_wavevector",
          "frequency_cm1"
        ],
        "units": {
          "frequency_cm1": "cm^{-1}"
        },
        "notes": "direction must be either 'GY' or 'GX'; reduced_wavevector in [0,1]; frequency_cm1 positive float."
      },
      "description": "Agent-computed surface-phonon frequencies. The checker extracts the frequencies, pairs them with hidden experimental points at matching direction and reduced wavevector, computes the RMSE, and awards credit based on a pre-set hidden threshold."
    }
  ],
  "notes": "The hidden checker uses digitized experimental dispersion data from the source paper to compute an RMSE. The scoring function is monotonic: lower RMSE yields higher reward. The agent must not rely on any particular RMSE threshold as it is unknown to the agent."
}
```

## How you are scored
A hidden verifier will read your `phonon_dispersion.csv` and compare the submitted frequencies to a hidden set of reference surface-phonon frequencies derived from experimental measurements. For each reference point (identified by its direction and reduced wavevector), the verifier finds the closest frequency you submitted at that same direction and wavevector, and computes the absolute error. The root-mean-square error (RMSE) across all reference points is then calculated.  
Your reward is determined by the RMSE: a low RMSE yields a high reward, and the reward decays monotonically as the RMSE increases. There is a hidden tolerance for full credit; you do not need to know the exact threshold – just aim for the smallest physically reasonable error by correctly implementing the MS model and the mode filtering.  
The verifier also checks that your CSV contains data for both directions and a reasonable density of ζ values, but the primary score is the RMSE. No reward is given for simply reporting numbers without a valid computation; the trustworthiness of your result is assumed, but the evaluation is based purely on the submitted CSV.
