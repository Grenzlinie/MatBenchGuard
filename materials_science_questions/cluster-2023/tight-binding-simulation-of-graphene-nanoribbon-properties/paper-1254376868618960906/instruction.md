# DFT Calculation of Band Gap and Raman Spectrum for a Gulf-Edged Chiral Graphene Nanoribbon

## Problem background
Graphene nanoribbons (GNRs) are narrow strips of graphene whose electronic and vibrational properties are tunable by edge topology and width. Chiral GNRs mix armchair and zigzag segments, opening new degrees of freedom for property design. A recent on‑surface synthesis study realized a gulf‑edged chiral GNR, denoted (4,2,7)-chGNR, featuring a unique edge structure. Density functional theory (DFT) simulations complemented the experimental characterization by predicting the electronic band structure and Raman‑active vibrational modes. This task reproduces those computational predictions: the Kohn‑Sham band gap of the (4,2,7)-chGNR and its simulated non‑resonant Raman spectrum in the high‑frequency region.

## Approach
The reproduction follows a compute‑driven protocol. First, construct the periodic atomic model of the (4,2,7)-chGNR from the known chiral vector (n=4, m=2), width w=7, and the benzenoid ring modifications that create the gulf edge. Then, perform a periodic Kohn‑Sham DFT calculation using the PBE exchange–correlation functional and appropriate pseudopotentials to obtain the electronic eigenvalues and band structure. Determine the Kohn‑Sham band gap from the resulting eigenvalues. Next, compute the vibrational frequencies and Raman activities via finite‑displacement (phonons) and finite‑field (Raman) approaches. Finally, convolve the Raman activities with Lorentzian broadening to produce a peak list of the Raman spectrum in the 1100–1700 cm⁻¹ range, reporting wavenumber and normalized intensity.

## Reproduction target
Produce two scored artifacts:
* `electronic_properties.json` – contains the Kohn‑Sham band gap of the (4,2,7)-chGNR in eV.
* `raman_spectrum.json` – lists the dominant Raman peaks (wavenumber in cm⁻¹ and normalized intensity in [0,1]) in the high‑frequency region (1100–1700 cm⁻¹).
Both quantities must be derived from the DFT calculations performed in the workflow steps. The goal is to compute these values independently; simply matching or reporting the paper's published numbers is not the objective.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE precision pseudopotential library: https://www.materialscloud.org/discover/sssp/table/precision
- aiida-vibroscopy plugin: aiida-vibroscopy

## Workflow steps

### Step 1: Generate atomic structure of (4,2,7)-chGNR
- Role: process
- Action: Construct the periodic unit cell and atomic coordinates of the gulf-edged (4,2,7)-chGNR from its chiral vector (n=4, m=2), width w=7, and the benzenoid ring modifications that create the gulf edge. Produce a CIF file containing the relaxed lattice parameters and positions.
- Evidence: `/app/outputs/atomic_structure.cif`

### Step 2: Run DFT electronic structure calculation
- Role: process
- Action: Using the generated atomic structure, perform a periodic Kohn-Sham DFT calculation with the PBE functional and appropriate plane-wave cutoffs and k-point grid to obtain the electronic eigenvalues, band structure, and density of states. This verifies the closed-shell ground state and provides the raw eigenvalues needed for the band gap.
- Evidence: `/app/outputs/dft_band_structure.log`

### Step 3: Run DFT phonon and Raman calculation
- Role: process
- Action: Using the same DFT settings, compute the vibrational frequencies and Raman activities via finite-displacement (phonons) and finite-field (Raman) approaches. This yields the raw vibrational data for the Raman spectrum.
- Evidence: `/app/outputs/phonon_raman.log`

### Step 4: Extract Kohn-Sham band gap
- Role: scored (load-bearing)
- Action: From the DFT electronic structure output, determine the Kohn-Sham band gap (the energy difference between the highest occupied and lowest unoccupied eigenvalues) and write it to electronic_properties.json.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: JSON object with key 'band_gap_eV' (float) containing the Kohn-Sham band gap in eV.
- Scoring: scored by hidden verifier

### Step 5: Generate simulated Raman spectrum
- Role: scored
- Action: Convolve the Raman activities from step 03 with Lorentzian broadening to produce a non-resonant Raman spectrum. Generate a peak list for all modes in the high-frequency region (1100-1700 cm⁻¹), reporting wavenumber (cm⁻¹) and normalized intensity (normalised to the maximum intensity in this region). Write the peak list to raman_spectrum.json.
- Output file: `/app/outputs/raman_spectrum.json`
- Format: json
- Contract: JSON object with key 'peaks', an array of objects each containing 'wavenumber_cm-1' (float) and 'normalized_intensity' (float in [0,1]).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.json`
- `/app/outputs/raman_spectrum.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Kohn-Sham band gap of the (4,2,7)-chGNR. Compared to the reference DFT value within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: number

### raman_spectrum.json
- path: `/app/outputs/raman_spectrum.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Simulated Raman peak list (1100-1700 cm⁻¹). Matched against reference DFT peaks using a wavenumber tolerance.
- schema:
  - `type`: object
  - `required`:
    - `peaks`: array of objects with wavenumber_cm-1 (number) and normalized_intensity (number in [0,1])

Notes: The hidden checker compares the band gap to the paper's DFT value and the Raman peaks to the paper's simulated peak list, applying wavenumber tolerance for peak matching. Reward depends on correctness of gap and fraction of matched major peaks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "number"
        }
      },
      "description": "Kohn-Sham band gap of the (4,2,7)-chGNR. Compared to the reference DFT value within a tolerance."
    },
    {
      "file": "raman_spectrum.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "peaks": "array of objects with wavenumber_cm-1 (number) and normalized_intensity (number in [0,1])"
        }
      },
      "description": "Simulated Raman peak list (1100-1700 cm⁻¹). Matched against reference DFT peaks using a wavenumber tolerance."
    }
  ],
  "notes": "The hidden checker compares the band gap to the paper's DFT value and the Raman peaks to the paper's simulated peak list, applying wavenumber tolerance for peak matching. Reward depends on correctness of gap and fraction of matched major peaks."
}
```

## How you are scored
A hidden verifier inspects your `electronic_properties.json` and `raman_spectrum.json`. It compares your reported band gap to a hidden reference DFT value using a predetermined tolerance. Your Raman peak list is matched against a hidden reference peak list using a wavenumber tolerance; the fraction of major peaks that match contributes to the score. The final reward is a weighted combination of band‑gap correctness and Raman peak matching. Because the verifier checks the actual computed results, it is essential to execute the DFT workflow properly — a fabricated value that happens to be close will not mask structural inconsistencies in the spectrum.
