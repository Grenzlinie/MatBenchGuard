# Pressure-induced Changes in Band Gaps and Optical Spectra of Rocksalt InN

## Problem background
Indium nitride (InN) is a narrow-gap semiconductor promising for long-wavelength optoelectronics. At high pressure, wurtzite InN transforms to a rocksalt phase. Understanding how pressure affects the electronic band structure and optical properties of rocksalt InN is important for tuning its optoelectronic performance. This task investigates the pressure dependence of band gaps and optical spectra in rocksalt InN using first-principles density functional theory (DFT).

## Approach
The approach employs density functional theory with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation. Calculations are performed for the rocksalt phase of InN at three pressures: 0, 20, and 40 GPa. First, the unit cell is relaxed at each pressure to obtain equilibrium lattice constants and atomic positions. Then, electronic band structures and density of states are computed to extract direct and indirect band gaps at the Γ, L, and X high-symmetry points. Finally, the imaginary part of the dielectric function and the absorption coefficient are derived from the electronic structure. The trends in band gaps and optical spectral peak positions with pressure are examined.

## Reproduction target
Produce the electronic band gaps of rocksalt InN at pressures 0, 20, and 40 GPa (direct at Γ, L, X and indirect L→Γ) and the optical spectra (imaginary dielectric function ε2 and absorption coefficient α) on a uniform energy grid up to 40 eV at the same pressures. The results must be saved to `band_gaps.csv` and `optical_properties.json` following the format specified in the output contract; these artifacts will be independently evaluated against hidden reference criteria.

## Assets

- Quantum ESPRESSO DFT package: https://www.quantum-espresso.org/
- In pseudopotential (GGA-PBE): https://pseudopotentials.quantum-espresso.org/
- N pseudopotential (GGA-PBE): https://pseudopotentials.quantum-espresso.org/
- Rocksalt InN crystal structure

## Workflow steps

### Step 1: Geometry optimization of rocksalt InN under pressure
- Role: process
- Action: Perform variable-cell relaxation of the rocksalt InN unit cell at pressures 0, 20, and 40 GPa using density functional theory with the PBE exchange-correlation functional. Use a plane-wave basis set and pseudopotentials for In and N. Save the optimized lattice constants and atomic positions for each pressure.
- Evidence: `/app/outputs/optimized_structures.txt`

### Step 2: Electronic structure calculation and band gap extraction
- Role: scored (load-bearing)
- Action: For each optimized structure at 0, 20, and 40 GPa, compute the electronic band structure and extract the direct and indirect band gaps: Γ→Γ, L→L, X→X, and indirect L→Γ. Report the band gap values in eV.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with columns: pressure (float), Eg_gamma_gamma (float, eV), Eg_L_L (float, eV), Eg_X_X (float, eV), Eg_L_Gamma (float, eV). Rows for pressures 0, 20, 40.
- Scoring: scored by hidden verifier

### Step 3: Optical property calculation: dielectric function and absorption
- Role: scored
- Action: Using the electronic structure results, compute the imaginary part of the dielectric function ε2(ω) and the absorption coefficient α(ω) for each pressure (0, 20, 40 GPa) on a uniform energy grid from 0 to 40 eV. Save the spectra.
- Output file: `/app/outputs/optical_properties.json`
- Format: json
- Contract: JSON object with top-level keys '0', '20', '40'. Each value is an object with keys 'energy' (list of float, eV), 'epsilon2' (list of float, arbitrary units), 'absorption' (list of float, cm^-1). Arrays equal length within each pressure.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/optical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Direct and indirect band gaps of rocksalt InN at pressures 0, 20, and 40 GPa. The checker recomputes the pressure coefficient dEg/dP at Γ from a linear fit and compares individual gaps to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `Eg_gamma_gamma`, `Eg_L_L`, `Eg_X_X`, `Eg_L_Gamma`
  - `units`:
    - `pressure`: GPa
    - `Eg_gamma_gamma`: eV
    - `Eg_L_L`: eV
    - `Eg_X_X`: eV
    - `Eg_L_Gamma`: eV

### optical_properties.json
- path: `/app/outputs/optical_properties.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Imaginary part of dielectric function ε2(ω) and absorption coefficient α(ω) at 0, 20, 40 GPa. The checker verifies that the first major peak in ε2 and the absorption edge shift monotonically to higher energy with increasing pressure.
- schema:
  - `type`: object
  - `required`:
    - `0`:
      - `energy`: list of float (eV)
      - `epsilon2`: list of float
      - `absorption`: list of float (cm^-1)
    - `20`:
      - `energy`: list of float (eV)
      - `epsilon2`: list of float
      - `absorption`: list of float (cm^-1)
    - `40`:
      - `energy`: list of float (eV)
      - `epsilon2`: list of float
      - `absorption`: list of float (cm^-1)

Notes: All DFT calculations should use the PBE functional with plane-wave basis and pseudopotentials. The optical spectra may show overall intensity differences due to broadening conventions; only the peak shift trends are scored.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "Eg_gamma_gamma",
          "Eg_L_L",
          "Eg_X_X",
          "Eg_L_Gamma"
        ],
        "units": {
          "pressure": "GPa",
          "Eg_gamma_gamma": "eV",
          "Eg_L_L": "eV",
          "Eg_X_X": "eV",
          "Eg_L_Gamma": "eV"
        }
      },
      "description": "Direct and indirect band gaps of rocksalt InN at pressures 0, 20, and 40 GPa. The checker recomputes the pressure coefficient dEg/dP at Γ from a linear fit and compares individual gaps to paper-reported values."
    },
    {
      "file": "optical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "0": {
            "energy": "list of float (eV)",
            "epsilon2": "list of float",
            "absorption": "list of float (cm^-1)"
          },
          "20": {
            "energy": "list of float (eV)",
            "epsilon2": "list of float",
            "absorption": "list of float (cm^-1)"
          },
          "40": {
            "energy": "list of float (eV)",
            "epsilon2": "list of float",
            "absorption": "list of float (cm^-1)"
          }
        }
      },
      "description": "Imaginary part of dielectric function ε2(ω) and absorption coefficient α(ω) at 0, 20, 40 GPa. The checker verifies that the first major peak in ε2 and the absorption edge shift monotonically to higher energy with increasing pressure."
    }
  ],
  "notes": "All DFT calculations should use the PBE functional with plane-wave basis and pseudopotentials. The optical spectra may show overall intensity differences due to broadening conventions; only the peak shift trends are scored."
}
```

## How you are scored
A hidden verifier independently scores each stage's artifact. For the band gaps (`band_gaps.csv`), the verifier recomputes the pressure coefficient of the Γ–Γ gap from a linear fit and compares individual gaps to reference values, using tolerances that account for typical DFT toolchain spread. For the optical spectra (`optical_properties.json`), the verifier checks that the first major peak in ε2 and the absorption edge shift monotonically to higher energy as pressure increases, reflecting the underlying physics. Each stage contributes to the final weighted reward; reporting plausible numbers without a faithful execution of the required workflow steps is unlikely to pass.
