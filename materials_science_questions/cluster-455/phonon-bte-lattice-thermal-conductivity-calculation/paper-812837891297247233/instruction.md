# Strain-driven odd-even phonon transport in carbon chain junctions

## Problem background
Monatomic carbon chains (CCs) bridging graphene nanoribbon (GNR) electrodes form ideal all-carbon nanoscale junctions where one-dimensional sp carbon meets two-dimensional sp2 graphene. A long-standing question in phonon transport is how the number of carbon atoms in the chain—and the resulting even–odd structural motif (polyyne-like vs. cumulene-like)—affects heat conduction under mechanical strain. Tensile strain modifies the vibrational spectra of both the chain and the GNR, potentially leading to an anomalously different response for even- versus odd-numbered chains. Understanding this strain-dependent ballistic phonon transport is critical for designing thermal interconnects and sensors based on these hybrid interfaces. The present task investigates the lattice thermal conductance and phonon transmission across representative GNR-CC-GNR junctions to reveal the odd-even effect under strain.

## Approach
The computational strategy combines ab initio density-functional theory (DFT) and the atomistic Green’s function (AGF) formalism for phonons. First, atomic models of the junctions (4zGNR-8C-4zGNR and 4zGNR-7C-4zGNR) are built using the known equilibrium lattice constants of the 4-zigzag-chain GNR and the bond lengths of the chains. Geometries are optimized with SIESTA using the LDA functional and a double-zeta-plus-polarization (DZP) basis set with norm-conserving pseudopotentials. Two conditions are prepared for each chain length: (a) the unstrained junction and (b) a strained junction where the electrode GNRs are stretched by approximately 0.8 Å. After relaxation, harmonic force constants (dynamical matrices) are obtained via the small-displacement method as implemented in Phonopy, using SIESTA as the force calculator. From these dynamical matrices, the phonon transmission function T_ph(ω) and the lattice thermal conductance K_ph(T) are computed using the AGF method. The AGF transport code must implement the standard retarded Green’s function partitioning, the electrode surface Green’s functions, and the broadening matrices to calculate the transmission (trace formula) and eventually integrate over frequency to obtain K_ph. No ready-made AGF solver is provided; it must be implemented from the published transport equations.

## Reproduction target
Compute the lattice thermal conductance K_ph at T = 300 K for the four junction configurations: 4zGNR-8C-4zGNR (unstrained and strained) and 4zGNR-7C-4zGNR (unstrained and strained). Report the results in nW/K in Kph_results.csv. The strain-induced relative change must differ between the even- and odd-numbered cases. Additionally, compute the phonon transmission spectrum T_ph(ω) for the 4zGNR-8C-4zGNR junction under both strain conditions across the frequency range 0–2000 cm⁻¹, with sufficient resolution to capture the spectral features near 1490 cm⁻¹. The transmission data are to be written to transmission_spectra.csv. The combined outputs must allow one to assess the odd–even ballistic phonon transport effect.

## Assets

- SIESTA: https://departments.icmab.es/leem/siesta/
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: Build GNR-CC-GNR junction models
- Role: process
- Action: Construct atomic structures for the 4zGNR-8C-4zGNR and 4zGNR-7C-4zGNR junctions using known equilibrium lattice constants and bond lengths. Create initial configurations for unstrained and strained conditions.
- Evidence: `/app/outputs/junction_structures`

### Step 2: DFT geometry optimization
- Role: process
- Action: Using SIESTA (LDA, DZP basis, norm-conserving pseudopotentials), optimize geometries of each junction under two conditions: unstrained and strained by stretching electrode GNRs by approximately 0.8 Å. Keep electrode C atoms fixed beyond a transition region.
- Evidence: `/app/outputs/optimized_geometries`

### Step 3: Phonon dynamical matrix calculation
- Role: process
- Action: For each optimized geometry, compute dynamical matrices using Phonopy (small-displacement method) with SIESTA as the force calculator. Use a suitable supercell and displacement amplitude.
- Evidence: `/app/outputs/dynamical_matrices`

### Step 4: Compute lattice thermal conductance
- Role: scored (load-bearing)
- Action: From the dynamical matrices, compute the phonon transmission function T_ph(ω) and lattice thermal conductance K_ph(T) using the atomistic Green's function method. Extract K_ph at T=300 K for all four configurations and write the results to /app/outputs/Kph_results.csv. Report Kph in nW/K.
- Output file: `/app/outputs/Kph_results.csv`
- Format: csv
- Contract: Columns: system (str: '4zGNR-8C-4zGNR_unstrained', '4zGNR-8C-4zGNR_strained', '4zGNR-7C-4zGNR_unstrained', '4zGNR-7C-4zGNR_strained'), T (float: temperature in K, i.e., 300.0), Kph (float: thermal conductance in nW/K).
- Scoring: scored by hidden verifier

### Step 5: Extract transmission spectrum for even-numbered junction
- Role: scored
- Action: For the 4zGNR-8C-4zGNR junction, extract the computed T_ph(ω) for both unstrained and strained conditions over the frequency range 0–2000 cm⁻¹ and write to /app/outputs/transmission_spectra.csv. Use a frequency grid fine enough to resolve the peak near 1490 cm⁻¹.
- Output file: `/app/outputs/transmission_spectra.csv`
- Format: csv
- Contract: Columns: system (str: '4zGNR-8C-4zGNR_unstrained' or '4zGNR-8C-4zGNR_strained'), frequency (float: wavenumber in cm⁻¹), transmission (float: dimensionless T_ph(ω)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Kph_results.csv`
- `/app/outputs/transmission_spectra.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Kph_results.csv
- path: `/app/outputs/Kph_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Thermal conductance values that must demonstrate the odd-even strain effect: relative increase >5% for 8C and decrease >5% for 7C.
- schema:
  - `type`: table
  - `required_columns`: `system`, `T`, `Kph`
  - `units`:
    - `T`: K
    - `Kph`: nW/K

### transmission_spectra.csv
- path: `/app/outputs/transmission_spectra.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon transmission that must show a peak near 1490 cm⁻¹ enhanced under strain for the 8C junction.
- schema:
  - `type`: table
  - `required_columns`: `system`, `frequency`, `transmission`
  - `units`:
    - `frequency`: cm^-1
    - `transmission`: dimensionless

Notes: The checker verifies the strain-dependent trend in K_ph (increase for even-numbered CC, decrease for odd-numbered CC) with a minimum relative difference, and confirms that the transmission peak around 1490 cm⁻¹ is enhanced under strain for the 8C junction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Kph_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "T",
          "Kph"
        ],
        "units": {
          "T": "K",
          "Kph": "nW/K"
        }
      },
      "description": "Thermal conductance values that must demonstrate the odd-even strain effect: relative increase >5% for 8C and decrease >5% for 7C."
    },
    {
      "file": "transmission_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "frequency",
          "transmission"
        ],
        "units": {
          "frequency": "cm^-1",
          "transmission": "dimensionless"
        }
      },
      "description": "Phonon transmission that must show a peak near 1490 cm⁻¹ enhanced under strain for the 8C junction."
    }
  ],
  "notes": "The checker verifies the strain-dependent trend in K_ph (increase for even-numbered CC, decrease for odd-numbered CC) with a minimum relative difference, and confirms that the transmission peak around 1490 cm⁻¹ is enhanced under strain for the 8C junction."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the two CSV files. The verifier checks the strain-dependent relative changes in K_ph for the 8C and 7C junctions against a hidden trend (sign of the change) and a required quantitative variation. It also inspects the transmission spectra for the 8C junction and verifies whether the transmission in the frequency window 1480–1500 cm⁻¹ is enhanced under strain by a required minimum margin. Both numerical tolerances and trend checks account for the inherent spread of LDA-based calculations. The final reward is a weighted sum of the per-artifact scores, with larger weight assigned to the thermal conductance trend and the transmission peak enhancement.
