# Vibrational properties of isolated AlAs monolayers in GaAs: effects of disorder via virtual crystal Raman spectroscopy

## Problem background
In GaAs/AlAs superlattices, the precise chemical sharpness of the interfaces critically affects electronic properties, but quantifying the degree of cationic intermixing is experimentally challenging. Raman spectroscopy of AlAs-like longitudinal optical (LO) phonons is sensitive to the local cation composition, opening the possibility to distinguish ideal, abrupt interfaces from configurations with intermixed cation planes. This task asks you to compute the Raman spectra for a prototypical short-period superlattice, (GaAs)₅(AlAs)₁, both in the ideal structure and in a cationically intermixed variant, and to characterize the AlAs-like LO peak positions. The aim is to determine whether the intermixed structure leaves a measurable signature in the phonon spectrum that could serve as a diagnostic for interface disorder.

## Approach
The theoretical method relies on the observation that Ga and Al are chemically similar, so the interatomic force constants of GaAs, AlAs, and their alloys are, to a very good approximation, independent of composition. This enables a two-stage procedure:

1. **Virtual crystal force constants.** A single set of real-space interatomic force constants is computed for a periodic virtual crystal whose cation pseudopotential is the arithmetic average of the Ga and Al pseudopotentials. This calculation is carried out with density-functional linear-response theory (DFPT), which yields the dynamical matrices on a grid of wavevectors, the Born effective charges, and the static dielectric constant. After subtracting the long-range Coulomb (non-analytic) part, the dynamical matrices are Fourier-transformed to obtain harmonic force constants in real space.

2. **Mass approximation for arbitrary supercells.** For any target structure—ideal or intermixed—the dynamical matrix is constructed from these force constants and the actual masses of Ga, Al, and As on each site. Diagonalizing the matrix gives phonon frequencies and displacement eigenvectors. Disorder is simulated by generating multiple random realizations of the intermixed cation distribution and averaging the resulting Raman spectra over approximately ten realizations. Raman intensities in the backscattering z(xy)z geometry are computed from the eigenvectors using a bond-polarizability or equivalent selection-rule model that respects the zinc-blende symmetry.

## Reproduction target
Produce the following three files under /app/outputs:

- **ideal_raman.csv**: Raman spectrum (frequency in cm⁻¹ and intensity in arbitrary units) of the ideal (GaAs)₅(AlAs)₁ superlattice in the z(xy)z backscattering configuration.
- **intermixed_raman.csv**: Disorder-averaged Raman spectrum of the intermixed configuration (GaAs)₄(Al₀.₇₈Ga₀.₂₂As)₁(Al₀.₂₂Ga₀.₇₈As)₁, averaged over ~10 random realizations of the cation arrangement, same backscattering configuration and units.
- **peak_positions.json**: A JSON object containing the extracted AlAs-like LO peak positions. Scan the frequency range 350–410 cm⁻¹ in each spectrum and report the highest peak as the main peak; for the intermixed spectrum, also identify the most prominent additional peak at lower frequency than the main peak (if one exists). The JSON must have keys `ideal_main_peak` (float, cm⁻¹), `intermixed_main_peak` (float, cm⁻¹), and `intermixed_secondary_peak` (float or null if no secondary peak is found).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Ga, Al, As: https://www.materialscloud.org/discover/sssp/table
- Virtual crystal pseudopotential construction
- Python 3 with NumPy, SciPy: numpy scipy

## Workflow steps

### Step 1: Compute real-space interatomic force constants of virtual crystal
- Role: process
- Action: Run density-functional linear-response calculation (DFPT) for the virtual crystal (zinc-blende structure with cation pseudopotential equal to the arithmetic average of Ga and Al pseudopotentials) to obtain dynamical matrices D(q) on a q-point grid, Born effective charges, and the static dielectric constant. Subtract the non-analytic long-wavelength Coulomb contribution from D(q) using the ab-initio effective charges and dielectric constant. Fourier-transform the corrected D(q) to real-space interatomic force constants Φ(R). Save Φ as a NumPy file.
- Evidence: `/app/outputs/force_constants.npy`

### Step 2: Compute phonon modes for ideal superlattice
- Role: process
- Action: Construct the supercell for the ideal (GaAs)5(AlAs)1 superlattice (18-atom tetragonal 2D unit cell). Assemble the mass-scaled dynamical matrix using the real-space force constants from step_01 and the physical masses of Ga, Al, As on each site. Diagonalize the dynamical matrix to obtain phonon frequencies and displacement eigenvectors.
- Evidence: `/app/outputs/ideal_modes.csv`

### Step 3: Calculate Raman spectrum for ideal superlattice
- Role: scored
- Action: Using the phonon eigenvectors from step_02, compute the Raman intensity for the z(xy)z backscattering configuration on the (001) face employing a bond-polarizability or equivalent Raman selection rule model. Output a CSV of frequency (cm⁻¹) versus intensity (arbitrary units).
- Output file: `/app/outputs/ideal_raman.csv`
- Format: csv
- Contract: Two columns: ‘frequency’ (float, cm⁻¹) and ‘intensity’ (float, arbitrary units). At least 200 frequency points covering the range ~0–500 cm⁻¹.
- Scoring: scored by hidden verifier

### Step 4: Generate phonon modes for intermixed superlattice (disorder averaging)
- Role: process
- Action: Construct approximately 10 independent random realizations of the intermixed (GaAs)4(Al0.78Ga0.22As)1(Al0.22Ga0.78As)1 superlattice using the same 18-atom tetragonal unit cell. For each realization, assign cation sites randomly according to the target concentrations, build the mass-scaled dynamical matrix using the force constants from step_01, diagonalize, and collect all frequencies and eigenvectors. Save the per-realization mode data.
- Evidence: `/app/outputs/intermixed_modes_collection.npz`

### Step 5: Calculate averaged Raman spectrum for intermixed superlattice
- Role: scored (load-bearing)
- Action: For each disorder realization from step_04, compute the Raman intensity using the same configuration and method as step_03. Average the spectra point-wise over all realizations. Output the averaged spectrum as a CSV.
- Output file: `/app/outputs/intermixed_raman.csv`
- Format: csv
- Contract: Same as ideal_raman.csv: columns ‘frequency’ (cm⁻¹) and ‘intensity’ (a.u.).
- Scoring: scored by hidden verifier

### Step 6: Extract AlAs-like LO peak positions
- Role: scored
- Action: From ideal_raman.csv, locate the highest peak in the AlAs-like frequency range (350–410 cm⁻¹) as the ideal main peak. From intermixed_raman.csv, locate the highest peak in the same range as the intermixed main peak, and also identify the most prominent additional peak on the lower-frequency side of the main peak (if any) as the secondary peak. Write the results to peak_positions.json.
- Output file: `/app/outputs/peak_positions.json`
- Format: json
- Contract: JSON object with keys: ‘ideal_main_peak’ (float, cm⁻¹), ‘intermixed_main_peak’ (float, cm⁻¹), ‘intermixed_secondary_peak’ (float or null if not found).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ideal_raman.csv`
- `/app/outputs/intermixed_raman.csv`
- `/app/outputs/peak_positions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ideal_raman.csv
- path: `/app/outputs/ideal_raman.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raman spectrum of the ideal superlattice. Checked for correct two-column format and non-empty content.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `intensity`

### intermixed_raman.csv
- path: `/app/outputs/intermixed_raman.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Disorder-averaged Raman spectrum of the intermixed superlattice. Checked for format and non-empty content.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `intensity`

### peak_positions.json
- path: `/app/outputs/peak_positions.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Extracted AlAs-like LO peak positions. The checker validates that the ideal main peak is positive, the intermixed main peak is downshifted relative to the ideal, and that a secondary lower-frequency peak appears in the intermixed spectrum.
- schema:
  - `type`: object
  - `required`:
    - `ideal_main_peak`: number (cm⁻¹)
    - `intermixed_main_peak`: number (cm⁻¹)
    - `intermixed_secondary_peak`: number or null

Notes: Scoring is structural: the key reward comes from verifying the relative frequency shift between ideal and intermixed main peaks (trend) and the presence of a secondary peak. The CSV files contribute minor format/completeness checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ideal_raman.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "intensity"
        ]
      },
      "description": "Raman spectrum of the ideal superlattice. Checked for correct two-column format and non-empty content."
    },
    {
      "file": "intermixed_raman.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "intensity"
        ]
      },
      "description": "Disorder-averaged Raman spectrum of the intermixed superlattice. Checked for format and non-empty content."
    },
    {
      "file": "peak_positions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "ideal_main_peak": "number (cm⁻¹)",
          "intermixed_main_peak": "number (cm⁻¹)",
          "intermixed_secondary_peak": "number or null"
        }
      },
      "description": "Extracted AlAs-like LO peak positions. The checker validates that the ideal main peak is positive, the intermixed main peak is downshifted relative to the ideal, and that a secondary lower-frequency peak appears in the intermixed spectrum."
    }
  ],
  "notes": "Scoring is structural: the key reward comes from verifying the relative frequency shift between ideal and intermixed main peaks (trend) and the presence of a secondary peak. The CSV files contribute minor format/completeness checks."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact. The CSV files are checked for correct two-column format (frequency, intensity) and non-empty content. The primary reward comes from the peak positions reported in `peak_positions.json`: the verifier extracts the values and evaluates the relationship between the ideal and intermixed peaks. The overall reward is a weighted sum of these individual scores. Simply reporting the expected numbers is not sufficient; the verifier expects the positions to be derived from the spectra that you compute.
