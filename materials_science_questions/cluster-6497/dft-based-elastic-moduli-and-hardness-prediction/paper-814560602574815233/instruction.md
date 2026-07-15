# Bulk modulus and compressibility classification of calcite-structure carbonates

## Problem background
The compressibility of isostructural crystals is often modeled by an empirical inverse linear relationship between the isothermal bulk modulus (K0) and the ambient unit-cell volume (V0). For many oxide and silicate families this relationship works well, but systematic departures have been reported, particularly when cations with different valence electron characters replace one another. The calcite-structure carbonates (space group R-3c) provide a clean test bed: they form for divalent cations ranging from Mg²⁺ (small, alkaline earth) to Cd²⁺ (large, 4d transition metal), and seven end-member compositions have been measured at room temperature under compression. The central question in this task is whether the bulk modulus and axial/volume compressibilities of MgCO3, CaCO3, NiCO3, CoCO3, MnCO3, ZnCO3 and CdCO3 collapse onto a single trend with cell volume, or whether they separate into groups related to the outer-electron configuration of the metal ions.

## Approach
The analysis follows a standard high-pressure crystallography workflow. The provided data file (pv_data.csv) reports the hexagonal lattice parameters a, c and unit-cell volume V at each applied pressure for every carbonate. Because the experiments cover a limited pressure range (roughly 0–8 GPa), the pressure derivative of the bulk modulus, K0′, is fixed at 4 in a second-order Birch–Murnaghan equation-of-state (BM2). For each carbonate the reference volume V0 is taken as the volume at the lowest measured pressure. A least-squares fit of the BM2 equation to the pressure–volume points yields the isothermal bulk modulus K0 and an estimate of the fitting uncertainty.

Mean linear compressibilities are obtained by a simpler linear regression: the ratios a/a₀, c/c₀ and V/V₀ are computed using the ambient (zero-pressure) lattice constants, and each is fitted against pressure with a zero-intercept constraint (ratio = 1 at P = 0). The slopes give the a-axis, c-axis and volume compressibilities (b_a, b_c, b_V).

Finally, the seven carbonates are classified into three subsets according to the valence electron character of the cation: alkaline earth (Mg, Ca – s² outer electrons), 3d transition metal (Ni, Co, Mn, Zn) and 4d transition metal (Cd). No numerical thresholds are needed; the classification is based solely on cation identity.

## Reproduction target
Using the pressure–volume data in pv_data.csv, produce three JSON artifact files under /app/outputs/:

1. bulk_moduli.json – for each carbonate report the carbonate name, the fitted K0 (GPa) and the fitting uncertainty K0_err (GPa).
2. axial_compressibilities.json – for each carbonate report the carbonate name and the mean linear compressibilities b_a, b_c, b_V (units of 10⁻³ GPa⁻¹).
3. subset_classification.json – list the carbonate names assigned to each of the three subsets: alkaline_earth, 3d_transition_metal, 4d_transition_metal.

Exact output schemas are given in the workflow steps below. All quantities must be derived from the provided P–V data; no external database look-ups or pre-computed values may be substituted.

## Assets

- P-V data of calcite-structure carbonates (Table 1): pv_data.csv

## Workflow steps

### Step 1: Fit Birch-Murnaghan EOS and extract bulk moduli
- Role: scored
- Action: For each carbonate, use its pressure–volume data from the provided CSV to fit a second-order Birch–Murnaghan equation of state (fixing K0'=4 and using the volume at the lowest pressure as the reference V0). Extract the isothermal bulk modulus K0 and its fitting uncertainty. Output the results as a JSON file.
- Output file: `/app/outputs/bulk_moduli.json`
- Format: json
- Contract: {"carbonates": [{"carbonate": string, "K0_GPa": float, "K0_err": float}]}
- Scoring: scored by hidden verifier

### Step 2: Compute mean axial and volume compressibilities
- Role: scored
- Action: For each carbonate, compute the ratios a/a0, c/c0, V/V0 using the provided ambient (zero-pressure) lattice parameters. Perform a linear least-squares fit of each ratio vs. pressure (forcing intercept=1 at P=0). Extract the mean linear compressibilities b_a (a-axis), b_c (c-axis) and b_V (volume). Output the results as a JSON file.
- Output file: `/app/outputs/axial_compressibilities.json`
- Format: json
- Contract: {"carbonates": [{"carbonate": string, "ba": float, "bc": float, "bV": float}]}
- Scoring: scored by hidden verifier

### Step 3: Classify carbonates by valence electron type
- Role: scored
- Action: Based on the known valence electron configuration of the cations, assign each carbonate to one of three subsets: alkaline earth (Mg, Ca), 3d transition metal (Ni, Co, Mn, Zn), or 4d transition metal (Cd). Output the classification as a JSON file.
- Output file: `/app/outputs/subset_classification.json`
- Format: json
- Contract: {"alkaline_earth": [string], "3d_transition_metal": [string], "4d_transition_metal": [string]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_moduli.json`
- `/app/outputs/axial_compressibilities.json`
- `/app/outputs/subset_classification.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_moduli.json
- path: `/app/outputs/bulk_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Room-temperature bulk modulus K0 and fitting uncertainty for each carbonate, obtained from a second-order Birch-Murnaghan EOS fit with K0'=4.
- schema:
  - `type`: object
  - `required`:
    - `carbonates`: array of objects, each with keys: carbonate (string), K0_GPa (number, GPa), K0_err (number, GPa)

### axial_compressibilities.json
- path: `/app/outputs/axial_compressibilities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mean linear compressibilities b_a, b_c, and b_V derived from linear fits of normalized axes and volume versus pressure.
- schema:
  - `type`: object
  - `required`:
    - `carbonates`: array of objects, each with keys: carbonate (string), ba (number, 1e-3 GPa⁻¹), bc (number, 1e-3 GPa⁻¹), bV (number, 1e-3 GPa⁻¹)

### subset_classification.json
- path: `/app/outputs/subset_classification.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Classification of carbonates into three subsets based on the cation's valence electron character (alkaline earth s², 3d transition metal, 4d transition metal).
- schema:
  - `type`: object
  - `required`:
    - `alkaline_earth`: array of carbonate name strings
    - `3d_transition_metal`: array of carbonate name strings
    - `4d_transition_metal`: array of carbonate name strings

Notes: FeCO3 is mentioned in the paper but is not included in the provided P–V data; classification includes only the carbonates for which data is supplied. The classification is based solely on cation type, not on numerical trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "carbonates": "array of objects, each with keys: carbonate (string), K0_GPa (number, GPa), K0_err (number, GPa)"
        }
      },
      "description": "Room-temperature bulk modulus K0 and fitting uncertainty for each carbonate, obtained from a second-order Birch-Murnaghan EOS fit with K0'=4."
    },
    {
      "file": "axial_compressibilities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "carbonates": "array of objects, each with keys: carbonate (string), ba (number, 1e-3 GPa⁻¹), bc (number, 1e-3 GPa⁻¹), bV (number, 1e-3 GPa⁻¹)"
        }
      },
      "description": "Mean linear compressibilities b_a, b_c, and b_V derived from linear fits of normalized axes and volume versus pressure."
    },
    {
      "file": "subset_classification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alkaline_earth": "array of carbonate name strings",
          "3d_transition_metal": "array of carbonate name strings",
          "4d_transition_metal": "array of carbonate name strings"
        }
      },
      "description": "Classification of carbonates into three subsets based on the cation's valence electron character (alkaline earth s², 3d transition metal, 4d transition metal)."
    }
  ],
  "notes": "FeCO3 is mentioned in the paper but is not included in the provided P–V data; classification includes only the carbonates for which data is supplied. The classification is based solely on cation type, not on numerical trends."
}
```

## How you are scored
A hidden verifier runs after you submit your outputs. It reads each of the three JSON files and independently checks the values against the expected results, using tolerances appropriate for the computational choices (BM2 fit with K0′=4, linear-regression slope with fixed intercept). The three artifacts are combined by weight; reporting a number that happens to be correct without actually carrying out the required analysis will not pass because the verifier compares the values derived from the data. Producing the files with the correct structure is necessary but not sufficient – the contents must be the result of performing the described computations on the given CSV.
