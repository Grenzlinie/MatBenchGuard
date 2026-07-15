# Plane-Wave DFT Band Gap Calculation for Eight Molecular Crystals

## Problem background
Organic molecular crystals are promising materials for organic electronics because of their well-defined periodic packing and absence of grain boundaries. The synthesis of 3-(4-aryl-1,2,3-triazol-1-yl)coumarins (ATCs) via a one-step multicomponent reaction yields crystalline solids whose solid-state electronic properties can be assessed by plane-wave DFT. This task probes the semiconducting character of eight such ATC crystal structures by computing their fundamental electronic band gaps.

## Approach
The approach uses periodic plane-wave density functional theory to calculate the valence-conduction band gap for each crystal. Starting from experimental crystal structures (CIF files), a geometry optimization is performed with the PBE exchange-correlation functional including Grimme D3 dispersion correction. The relaxed geometries are then used in a single-point calculation with the screened hybrid functional HSE06, which provides a band structure. From the band structure, the minimum energy difference between the valence band maximum and conduction band minimum is extracted. The entire workflow is carried out with an open-source plane-wave DFT code such as Quantum ESPRESSO or CP2K, using norm-conserving pseudopotentials. The band gaps for the eight ATCs are compared with one another to reveal the trend in semiconducting behaviour across this family of molecular crystals.

## Reproduction target
Produce a CSV file (`band_gaps.csv`) containing the HSE06 valence-conduction band gap (in eV) for each of the eight ATC crystal structures: 5a, 5b, 5c, 5f, 5h, 5j, 5k, and 5l. The band gap is defined as the smallest energy separation between the valence and conduction bands obtained from the HSE06 single-point calculation on the PBE+D3-optimized crystal geometry. The file must have columns `compound` (string) and `band_gap_eV` (float).

## Assets

- CCDC crystal structure CIFs for compounds 5a,5b,5c,5f,5h,5j,5k,5l: https://www.ccdc.cam.ac.uk/structures
- Quantum ESPRESSO (or CP2K): https://www.quantum-espresso.org
- Norm-conserving PBE pseudopotentials: https://pseudopotentials.quantum-espresso.org/upf_files/

## Workflow steps

### Step 1: Geometry optimization of ATC crystal structures
- Role: process
- Action: For each of the eight ATC crystal structures (compounds 5a, 5b, 5c, 5f, 5h, 5j, 5k, 5l), perform a plane-wave DFT variable-cell geometry optimization using the PBE exchange-correlation functional with Grimme D3 dispersion correction, norm-conserving pseudopotentials, and an open-source DFT code (e.g., Quantum ESPRESSO or CP2K). The optimized structures are required for the subsequent HSE06 band structure calculations.
- Evidence: none

### Step 2: HSE06 single-point and band gap extraction
- Role: scored (load-bearing)
- Action: For each optimized structure from the geometry optimization step, perform a single-point DFT calculation with the HSE06 hybrid functional using the same pseudopotentials and cutoff, compute the band structure along high-symmetry k-point paths in the Brillouin zone, extract the valence-conduction band gap (minimum energy difference between valence and conduction bands), and write the results to band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: columns: compound (string, one of 5a,5b,5c,5f,5h,5j,5k,5l), band_gap_eV (float, in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed valence-conduction band gaps for the eight ATC crystal structures, extracted from HSE06 single-point calculations on optimized geometries.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `band_gap_eV`
  - `units`:
    - `band_gap_eV`: eV

Notes: The checker will compare each band_gap_eV value to a hidden reference derived from the source paper's Figure 7. Ordering consistency among compounds is also assessed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "band_gap_eV"
        ],
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Computed valence-conduction band gaps for the eight ATC crystal structures, extracted from HSE06 single-point calculations on optimized geometries."
    }
  ],
  "notes": "The checker will compare each band_gap_eV value to a hidden reference derived from the source paper's Figure 7. Ordering consistency among compounds is also assessed."
}
```

## How you are scored
Your submission is scored by a hidden verifier that checks the CSV file produced in Step 2. The verifier compares each computed band gap to a reference derived from the literature and checks whether the relative ordering of the band gaps across the eight compounds is preserved. The reward is the weighted combination of these two assessments. Simply reporting a value does not guarantee credit; the verifier independently evaluates the physical consistency and trend of your computed results.
