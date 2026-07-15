# LDA+U+SO Electronic Structure of Actinides under Compression

## Problem background
Transuranium metals (Np, Pu, Am, Cm) possess an intricate electronic structure because Coulomb correlations, Hund exchange, and spin-orbit coupling are all of comparable strength. Applying pressure compresses the lattice, which can drive gradual delocalization of 5f electrons and broaden the corresponding bands. Understanding how the 5f electrons respond to volume contraction—whether the coupling scheme is of jj, LS, or intermediate type, and how the magnetic moments and spectral features evolve—is essential for predicting the behavior of actinide materials under extreme conditions. This task aims to reproduce the computational investigation of these effects using static mean-field LDA+U+SO calculations.

## Approach
The central method is the LDA+U+SO (local density approximation with Hubbard U correction and spin-orbit coupling) approach, which incorporates strong Coulomb repulsion, Hund exchange, and spin-orbit interaction in a general nondiagonal form. For each of the four metals (bcc Np, fcc Pu, fcc Am, fcc Cm), self-consistent electronic structure calculations are performed at a series of unit-cell volumes, corresponding to relative compression ratios V/V₀ = 1.0, 0.95, 0.90, 0.85, 0.80. The computational setup uses a fixed Hubbard parameter U = 4 eV and the metal-specific Hund exchange values derived from constrained LDA. From the self-consistent solutions, the following quantities are extracted: (1) at ambient volume (V/V₀ = 1.0), spin, orbital, and total magnetic moments, effective moment, the seven largest eigenvalues of the 5f occupation matrix, and the largest off-diagonal elements in both the {mσ} and {jmⱼ} bases; (2) at every volume, the partial densities of states projected onto the j = 5/2 and j = 7/2 channels to determine subband bandwidths (full width at half maximum) and the total magnetic moment. The results are used to assess which coupling scheme (jj, LS, or intermediate) prevails for each element and to quantify the band-broadening trend with compression.

## Reproduction target
Produce two structured output files that together capture the electronic-structure response to volume compression. (a) material_properties_ambient.json: for each metal (Np, Pu, Am, Cm) at the ambient volume V/V₀ = 1.0, report the spin moment S, orbital moment L, total moment J, effective magnetic moment μ_eff, the seven largest occupation eigenvalues, and the maximum off-diagonal elements OD_LS and OD_jmj. (b) bandwidth_vs_volume.csv: for each metal and each relative volume V/V₀ in {1.0, 0.95, 0.90, 0.85, 0.80}, report the bandwidth (FWHM) of the j = 5/2 subband, the bandwidth of the j = 7/2 subband, and the total magnetic moment. The primary scientific aim is to demonstrate a monotonic increase of the 5f subband bandwidths as the volume decreases (band broadening under pressure).

## Assets

- Quantum ESPRESSO (plane-wave pseudopotential DFT code with SOC+U) or equivalent open-source DFT code: https://www.quantum-espresso.org
- Cubic lattice parameters for bcc Np, fcc Pu, Am, Cm

## Workflow steps

### Step 1: LDA+U+SO self-consistent calculations for all metals and volumes
- Role: process
- Action: For each metal (bcc Np, fcc Pu, fcc Am, fcc Cm) at each relative volume V/V0 in {1.0, 0.95, 0.90, 0.85, 0.80}, perform self-consistent LDA+U+SO calculations with U=4 eV, the appropriate J_H (Np,Pu: 0.48 eV; Am: 0.49 eV; Cm: 0.52 eV), and full spin-orbit coupling. Use the cubic lattice parameters from the bundled resource. This step produces converged electron densities, Kohn-Sham orbitals, and occupation matrices needed for all downstream analyses.
- Evidence: none

### Step 2: Extract ambient-pressure occupation matrix and magnetic moments
- Role: scored (load-bearing)
- Action: From the converged LDA+U+SO results at V/V0=1.0 for each metal, compute spin moment S, orbital moment L, total moment J, effective magnetic moment mu_eff, the seven largest eigenvalues of the occupation matrix, and the maximum off-diagonal elements OD_LS and OD_jmj in the {mσ} and {jmj} bases. Write the results to material_properties_ambient.json.
- Output file: `/app/outputs/material_properties_ambient.json`
- Format: json
- Contract: JSON object with keys 'Np', 'Pu', 'Am', 'Cm'. Each value is an object with numeric fields: 'S' (μB), 'L' (μB), 'J' (μB), 'mu_eff' (μB), 'occupation_eigenvalues' (array of 7 floats), 'OD_LS' (float), 'OD_jmj' (float).
- Scoring: scored by hidden verifier

### Step 3: Extract bandwidths and magnetic moments at all volumes
- Role: scored (load-bearing)
- Action: For each metal and each volume ratio, compute the partial densities of states projected onto the j=5/2 and j=7/2 channels. Determine the full width at half maximum (FWHM) of each subband as the bandwidth. Also extract the total magnetic moment. Output the results as a CSV file bandwidth_vs_volume.csv with columns: material, volume_ratio, j5_2_bandwidth (eV), j7_2_bandwidth (eV), total_magnetic_moment (μB).
- Output file: `/app/outputs/bandwidth_vs_volume.csv`
- Format: csv
- Contract: CSV with columns: material (str), volume_ratio (float), j5_2_bandwidth (float, eV), j7_2_bandwidth (float, eV), total_magnetic_moment (float, μB). One row per material per volume ratio.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/material_properties_ambient.json`
- `/app/outputs/bandwidth_vs_volume.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### material_properties_ambient.json
- path: `/app/outputs/material_properties_ambient.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic moments, occupation matrix eigenvalues, and off-diagonal elements at ambient pressure for all four metals, compared to hidden reference values from the paper.
- schema:
  - `type`: object
  - `required`:
    - `Np`: object with fields S, L, J, mu_eff (float, μB), occupation_eigenvalues (array of 7 floats), OD_LS (float), OD_jmj (float)
    - `Pu`: object with same fields
    - `Am`: object with same fields
    - `Cm`: object with same fields
  - `items`: object

### bandwidth_vs_volume.csv
- path: `/app/outputs/bandwidth_vs_volume.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Bandwidths and magnetic moments at all volumes, verified for monotonic bandwidth increase with compression and specific Pu j=5/2 bandwidth increment.
- schema:
  - `type`: table
  - `required_columns`: `material`, `volume_ratio`, `j5_2_bandwidth`, `j7_2_bandwidth`, `total_magnetic_moment`
  - `units`:
    - `j5_2_bandwidth`: eV
    - `j7_2_bandwidth`: eV
    - `total_magnetic_moment`: μB

Notes: None

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "material_properties_ambient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Np": "object with fields S, L, J, mu_eff (float, μB), occupation_eigenvalues (array of 7 floats), OD_LS (float), OD_jmj (float)",
          "Pu": "object with same fields",
          "Am": "object with same fields",
          "Cm": "object with same fields"
        },
        "items": {}
      },
      "description": "Magnetic moments, occupation matrix eigenvalues, and off-diagonal elements at ambient pressure for all four metals, compared to hidden reference values from the paper."
    },
    {
      "file": "bandwidth_vs_volume.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "volume_ratio",
          "j5_2_bandwidth",
          "j7_2_bandwidth",
          "total_magnetic_moment"
        ],
        "units": {
          "j5_2_bandwidth": "eV",
          "j7_2_bandwidth": "eV",
          "total_magnetic_moment": "μB"
        }
      },
      "description": "Bandwidths and magnetic moments at all volumes, verified for monotonic bandwidth increase with compression and specific Pu j=5/2 bandwidth increment."
    }
  ],
  "notes": "None"
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that is not accessible to you. The verifier first checks that both output files exist and conform to the specified JSON schema and CSV column structure. Then it assigns scores to each artifact independently: (1) For material_properties_ambient.json, the verifier compares your reported magnetic moments, eigenvalues, and off-diagonal elements against expected values for this computational method. (2) For bandwidth_vs_volume.csv, the verifier verifies that for every metal the j=5/2 and j=7/2 bandwidths are monotonic non-decreasing as the relative volume decreases, and verifies other quantitative consistency properties. The two artifacts are weighted equally, and the overall reward is a value between 0.0 (no correct information) and 1.0 (all requirements met). Simply reporting numbers that look plausible is not sufficient; the numbers must follow from a genuine execution of the LDA+U+SO workflow as described.
