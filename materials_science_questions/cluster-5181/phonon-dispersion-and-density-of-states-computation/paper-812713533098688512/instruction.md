# Phonon dispersion, density of states, and Debye temperature for fcc copper using the interstitial electron model

## Problem background
Traditional atomistic models for metals often rely on simple pair potentials, which fail to capture anisotropic electron density distributions and suffer from the compressibility paradox—the compressibility from the long-wave limit conflicts with that from homogeneous deformation. The embedded-atom method (EAM) partially accounts for inhomogeneous electron density but still assumes isotropic distributions, leading to incorrect Cauchy relations in hcp metals. To incorporate anisotropic many-body electron effects, the interstitial electron model (IEM) treats the valence electrons as classical particles placed at the tetrahedral interstitial sites of the crystal lattice, using pairwise interactions for ion-ion, ion-electron, and electron-electron pairs. When applied to fcc metals in the fluorite structure with nearest-neighbor interactions and zero electron mass (Born–Oppenheimer approximation), the IEM yields an effective ion dynamical matrix from which phonon properties can be computed. This task evaluates the IEM for fcc copper (Cu) by computing its phonon dispersion relations, phonon density of states, and Debye temperature—quantities that probe the quality of the interatomic interactions.

## Approach
The IEM defines six independent force constants (α, γ, μ, λ, δ, ρ) that parameterize the nearest-neighbor ion-ion, ion-electron, and electron-electron interactions in the fluorite configuration. These force constants are determined by solving a system of equations that links them to experimentally measured quantities: the lattice constant, the three cubic elastic constants C11, C12, C44, and the longitudinal and transverse zone-boundary phonon frequencies at the X point. The system includes the equilibrium condition (zero stress) and the long-wavelength expressions for the elastic constants. Once the force constants are obtained, the full dynamical matrix for the composite ion-electron system is constructed, and the electron degrees of freedom are eliminated (using the zero-mass limit) to yield a 3×3 effective ion dynamical matrix D_total(q). Diagonalizing D_total(q) along a dense high-symmetry path Γ–X–W–L–Γ gives the phonon dispersion. Diagonalizing it on a uniform mesh within the Brillouin zone and histogramming the frequencies produces the phonon density of states. The Debye temperature is then extracted from the low-frequency behavior of the density of states (or from the lattice heat capacity) at three temperatures: 0 K, 100 K, and 300 K.

## Reproduction target
Compute, for fcc Cu using the IEM with nearest-neighbor interactions and zero electron mass, the following quantities:
- Phonon dispersion curves: for q-points along the path Γ (0,0,0) → X (0.5,0,0) → W (0.5,0.25,0) → L (0.5,0.5,0.5) → Γ, use at least 50 q-points per segment and output the three branch frequencies (in THz) together with the q-point coordinates.
- Phonon density of states: from a uniform q-mesh covering the Brillouin zone with at least 10⁶ q-points, histogram the frequencies into bins of width ≤ 0.1 THz and output the histogram (frequency vs. normalized DOS counts).
- Debye temperature: at T = 0 K, 100 K, and 300 K, output the temperature and the corresponding Debye temperature in Kelvin.

Use the experimental input data for Cu: lattice constant a = 3.6150 Å, elastic constants C11 = 16.84×10¹¹ dyn/cm², C12 = 12.14×10¹¹ dyn/cm², C44 = 7.54×10¹¹ dyn/cm², longitudinal X-point frequency ω_X^L = 7.19 THz, transverse ω_X^T = 5.08 THz, and atomic mass M = 63.54 amu. Convert to a consistent unit system.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare experimental input data
- Role: process
- Action: Define the experimental reference data for fcc Cu: lattice constant a=3.6150 Å, elastic constants C11=16.84e11 dyn/cm², C12=12.14e11 dyn/cm², C44=7.54e11 dyn/cm², longitudinal zone-boundary frequency ω_X^L=7.19 THz, transverse ω_X^T=5.08 THz, and atomic mass M=63.54 amu. Convert all quantities to a consistent unit system (e.g., SI or dyn/cm²/Å/THz).
- Evidence: none

### Step 2: Solve for IEM force constants
- Role: process
- Action: Derive the six independent force constants α, γ, μ, λ, δ, ρ for the fluorite structure by solving the system formed by the equilibrium condition (zero stress), the relations for elastic constants C11, C12, C44, and the expressions for the zone-boundary frequencies ω_X^L and ω_X^T. This involves solving a cubic equation for ρ and selecting the real solution set that yields real phonon frequencies.
- Evidence: none

### Step 3: Compute phonon dispersion curves
- Role: scored (load-bearing)
- Action: Construct the dynamical matrix for the composite ion-electron system in the fluorite configuration with zero electron mass. Eliminate the electron degrees of freedom to obtain the 3×3 ion dynamical matrix D_total(q). Diagonalize D_total(q) for a dense set of q-points along the high-symmetry path Γ (0,0,0) → X (0.5,0,0) → W (0.5,0.25,0) → L (0.5,0.5,0.5) → Γ, using at least 50 q-points per segment. Write the q-point coordinates, branch indices (0–2), and frequencies (in THz) to the output file.
- Output file: `/app/outputs/phonon_dispersion.csv`
- Format: csv
- Contract: qpoint_x (float, fractional), qpoint_y (float, fractional), qpoint_z (float, fractional), branch_index (int 0..2), frequency (float, THz)
- Scoring: scored by hidden verifier

### Step 4: Compute phonon density of states
- Role: scored
- Action: Using the same fitted force constants and dynamical matrix, diagonalize D_total(q) on a uniform q-mesh covering the Brillouin zone with at least 10^6 q-points total. Histogram the resulting frequencies into bins of width ≤ 0.1 THz to obtain the phonon density of states. Write the histogram (frequency, DOS value) to the output file.
- Output file: `/app/outputs/phonon_dos.csv`
- Format: csv
- Contract: frequency (float, THz), dos_value (float, normalized counts)
- Scoring: scored by hidden verifier

### Step 5: Compute Debye temperature
- Role: scored
- Action: From the phonon density of states, calculate the lattice heat capacity C_V(T) and determine the Debye temperature Θ_D at temperatures 0 K, 100 K, and 300 K, either by fitting to the Debye model or by solving the standard relation. Write the temperature and corresponding Debye temperature to the output file.
- Output file: `/app/outputs/debye_temperature.csv`
- Format: csv
- Contract: temperature_K (float), debye_temperature_K (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_dispersion.csv`
- `/app/outputs/phonon_dos.csv`
- `/app/outputs/debye_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_dispersion.csv
- path: `/app/outputs/phonon_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon dispersion relation along the high-symmetry path Γ–X–W–L–Γ, with each row giving the q-point coordinates, branch index (0–2), and phonon frequency in THz.
- schema:
  - `type`: table
  - `required_columns`: `qpoint_x`, `qpoint_y`, `qpoint_z`, `branch_index`, `frequency`
  - `units`:
    - `qpoint_x`: fractional
    - `qpoint_y`: fractional
    - `qpoint_z`: fractional
    - `frequency`: THz

### phonon_dos.csv
- path: `/app/outputs/phonon_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon density of states histogram, giving the frequency bin center and the normalized DOS count.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `dos_value`
  - `units`:
    - `frequency`: THz
    - `dos_value`: arbitrary normalized units

### debye_temperature.csv
- path: `/app/outputs/debye_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Debye temperature of fcc Cu calculated at 0 K, 100 K, and 300 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `debye_temperature_K`
  - `units`:
    - `temperature_K`: K
    - `debye_temperature_K`: K

Notes: The checker will compare phonon frequencies at high-symmetry points to hidden experimental reference values, verify the DOS cutoff and non-constant shape, and compare the Debye temperature at 0 K to a hidden gold value. Weights are 50% dispersion, 20% DOS, 30% Debye temperature. All comparisons use tolerance-based monotonic scoring: full credit for meeting or exceeding the reference, degrading gracefully as the result deviates.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "qpoint_x",
          "qpoint_y",
          "qpoint_z",
          "branch_index",
          "frequency"
        ],
        "units": {
          "qpoint_x": "fractional",
          "qpoint_y": "fractional",
          "qpoint_z": "fractional",
          "frequency": "THz"
        }
      },
      "description": "Phonon dispersion relation along the high-symmetry path Γ–X–W–L–Γ, with each row giving the q-point coordinates, branch index (0–2), and phonon frequency in THz."
    },
    {
      "file": "phonon_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "dos_value"
        ],
        "units": {
          "frequency": "THz",
          "dos_value": "arbitrary normalized units"
        }
      },
      "description": "Phonon density of states histogram, giving the frequency bin center and the normalized DOS count."
    },
    {
      "file": "debye_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "debye_temperature_K"
        ],
        "units": {
          "temperature_K": "K",
          "debye_temperature_K": "K"
        }
      },
      "description": "Debye temperature of fcc Cu calculated at 0 K, 100 K, and 300 K."
    }
  ],
  "notes": "The checker will compare phonon frequencies at high-symmetry points to hidden experimental reference values, verify the DOS cutoff and non-constant shape, and compare the Debye temperature at 0 K to a hidden gold value. Weights are 50% dispersion, 20% DOS, 30% Debye temperature. All comparisons use tolerance-based monotonic scoring: full credit for meeting or exceeding the reference, degrading gracefully as the result deviates."
}
```

## How you are scored
A hidden verifier will independently assess each of the three scored artifacts:
- Phonon dispersion (weight 50%): the verifier locates the q-points nearest to the high-symmetry points X, W, and L and compares the three branch frequencies at each point against hidden experimental reference values. Credit is awarded based on how closely your computed frequencies match the references; better agreement earns higher credit.
- Phonon density of states (weight 20%): the verifier checks that the density of states has a non-zero bin at the highest frequency within an expected cutoff range and that the distribution is not flat (demonstrating a proper computation). A DOS that meets these structural criteria receives full weight.
- Debye temperature (weight 30%): the verifier compares your Debye temperature at 0 K against a hidden reference value derived from the paper. Closer agreement yields higher credit.

Your final reward is the weighted sum of these three scores (range 0–1). You must write the computed results to the specified output files; the verifier does not reconstruct the full pipeline but evaluates your submitted artifacts against these criteria.
