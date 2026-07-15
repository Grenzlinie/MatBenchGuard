# Compute Optical Absorption Band Energies of M++X-- Crystals

## Problem background
M++X-- type ionic crystals (oxides, sulfides, selenides, tellurides) exhibit characteristic optical absorption bands whose energies carry information about the crystal's electronic structure. A theoretical framework based on lattice wavefunction and energy cycle methods can compute the first (hν₁) and second (hν₂) absorption band energies by combining Madelung electrostatic effects with corrections for polarization, sharing resonance, and homopolar (van der Waals) contributions. This task implements that framework for a representative set of crystals and computes the expected absorption energies.

## Approach
The energy-level model treats the crystal as an ionic lattice with point charges at lattice sites. The Madelung energy VM = 2Ae²/r₀ sets the electrostatic reference, where A is the Madelung constant, e the electron charge, and r₀ the nearest-neighbor distance. For crystals of the rocksalt (cubic) structure, the first absorption energy hν₁ is obtained from an energy cycle that incorporates the bare electrostatic term 2(2A‑1)e²/r₀, the second ionization energy I₂ of the metal, the second electron affinity E₂ of the nonmetal, and corrections for polarization (ω₁), sharing (Ω₁), and homopolar (ΔU₁) energies. The second absorption energy hν₂ uses a similar cycle with polarization ω₂ and homopolar ΔU₂. For zincblende and wurtzite structures, the polarization contributions are modified (ω₁ is set to zero and ω₂ is halved relative to the rocksalt expression) to account for increased covalency. Using ionic polarizabilities α_M++ and α_X--, the homopolar corrections ΔU/U ratios, and the estimated photoelectric work functions χ, the procedure first compiles all intermediate quantities (r₀, VM, ω₁, ω₂, Ω₁, ΔU₁, ΔU₂) and then applies the corresponding energy formulas to compute hν₁ and hν₂ for each crystal.

## Reproduction target
For the crystals listed below, compute the first absorption band energy hν₁ and second absorption band energy hν₂ (both in eV) using the theoretical framework described above. The required input parameters (lattice constants, Madelung constants, ionic polarizabilities, ionization energies, electron affinities, homopolar corrections, and estimated work functions) are provided in the appended tables. The crystals are: MgO, CaO, SrO, BaO, CdO, CaS, SrS, BaS (all rocksalt); ZnS (zincblende); CdS (wurtzite). Produce a CSV file `absorption_energies.csv` containing one row per crystal, with columns `crystal`, `hν1_eV`, `hν2_eV`.

## Assets

- numpy: numpy

## Formulas

Define the electron‑squared constant (in eV·Å) as
`e2 = 14.3996`.

For a crystal with nearest‑neighbour distance `r0` (in Å) and Madelung constant `A`,
the Madelung energy and the bare electrostatic term are

```
VM   = 2 * A * e2 / r0
U_el = 2 * (2*A - 1) * e2 / r0
```

The polarization correction `ω₁` and `ω₂` and the sharing correction `Ω₁`
are computed from the sum of ionic polarizabilities
`α_sum = α_M ++ α_X` (in 10⁻²⁴ cm³) according to the structure type.

**Rocksalt (cubic) structure:**

```
ω₁ = -2.027 * e2 * α_sum / r0^4
ω₂ = -7.00  * e2 * α_sum / (2 * r0^4)
Ω₁ = -0.4189 * e2 / r0
```

**Zincblende / wurtzite structures:**

```
ω₁ = 0
ω₂ = -3.50  * e2 * α_sum / (2 * r0^4)
Ω₁ = -0.4189 * e2 / r0   (unchanged)
```

The first absorption band energy `hν₁` and second absorption band energy `hν₂`
(in eV) are obtained from the energy‑cycle relations:

```
hν₁ = U_el + E₂ - I₂ + ω₁ + Ω₁ + ΔU₁
hν₂ = VM   + E₂ - χ  + ω₂ + ΔU₂
```

where
- `I₂` is the second ionization energy of the metal (eV),
- `E₂` is the second electron affinity of the non‑metal (eV; negative value means energy released),
- `ΔU₁` and `ΔU₂` are homopolar (van der Waals) corrections (eV) given below,
- `χ` is the estimated photoelectric work function (eV) also given below.

## Input parameters

The table lists all parameters needed for the ten crystals.
All numerical values are taken from the original publication
and are given in the same units as used in the formulas.

| Crystal | Structure  | r0 (Å)   | A     | α_M | α_X  | I₂ (eV) | E₂ (eV) | ΔU₁ (eV) | ΔU₂ (eV) | χ (eV) |
|---------|------------|----------|-------|-----|------|---------|---------|-----------|-----------|--------|
| MgO     | rocksalt   | 2.1015   |1.7476 |0.10 |2.25  |14.96    | -8.5    | 0.0       | 0.0       | 0.5    |
| CaO     | rocksalt   | 2.4053   |1.7476 |0.54 |2.25  |11.82    | -8.5    | 0.0       | 0.0       | 0.5    |
| SrO     | rocksalt   | 2.58     |1.7476 |1.0  |2.25  |10.98    | -8.5    | 0.0       | 0.0       | 0.5    |
| BaO     | rocksalt   | 2.75     |1.7476 |2.08 |2.25  |9.96     | -8.5    | 0.0       | 0.0       | 0.5    |
| CdO     | rocksalt   | 2.3415   |1.7476 |0.54 |2.25  |16.84    | -8.5    | 1.55      | 1.09      | 3.5    |
| CaS     | rocksalt   | 2.84     |1.7476 |0.54 |6.00  |11.82    | -8.0    | 0.0       | 0.0       | 1.2    |
| SrS     | rocksalt   | 2.935    |1.7476 |1.0  |6.00  |10.98    | -8.0    | 0.0       | 0.0       | 1.2    |
| BaS     | rocksalt   | 3.175    |1.7476 |2.08 |6.00  |9.96     | -8.0    | 0.0       | 0.0       | 1.2    |
| ZnS     | zincblende | 2.3513   |1.6381 |0.17 |6.00  |17.89    | -8.0    | 1.11      | 0.81      | 1.5    |
| CdS     | wurtzite   | 2.5352   |1.63   |0.54 |6.00  |16.84    | -8.0    | 1.07      | 0.77      | 0.5    |

## Workflow steps

### Step 1: Compile parameters
- Role: process
- Action: Using the provided crystallographic data and ion parameters (lattice constants, Madelung constants, polarizabilities, ionization energies, electron affinities, homopolar corrections, and estimated work functions) for the set of crystals, compute the nearest-neighbor distance r0, the Madelung energy VM, and the electrostatic term 2(2A-1)e²/r0 for each crystal. Classify each crystal as rocksalt (cubic) or zincblende/wurtzite based on the given structure type.
- Evidence: none

### Step 2: Compute absorption energies and output CSV
- Role: scored (load-bearing)
- Action: For each crystal, using the derived intermediate quantities and the provided formulas for polarization, sharing, and homopolar energies (standard formulas for rocksalt, modified for zincblende/wurtzite), compute the first absorption band energy hν1 and second absorption band energy hν2, and write them to a CSV file.
- Output file: `/app/outputs/absorption_energies.csv`
- Format: csv
- Contract: CSV with columns: crystal (string), hν1_eV (float, eV), hν2_eV (float, eV). One row per crystal.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_energies.csv
- path: `/app/outputs/absorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed first and second absorption band energies for the specified crystals.
- schema:
  - `columns`: `crystal`, `hν1_eV`, `hν2_eV`
  - `dtypes`: `string`, `float`, `float`

Notes: Verification recomputes hν₁ and hν₂ using the same formulas and parameters, comparing against the output CSV with a tolerance of ±0.2 eV per value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "crystal",
          "hν1_eV",
          "hν2_eV"
        ],
        "dtypes": [
          "string",
          "float",
          "float"
        ]
      },
      "description": "Computed first and second absorption band energies for the specified crystals."
    }
  ],
  "notes": "Verification recomputes hν₁ and hν₂ using the same formulas and parameters, comparing against the output CSV with a tolerance of ±0.2 eV per value."
}
```

## How you are scored
A hidden verifier independently computes the expected hν₁ and hν₂ for each crystal using the same formulas and input parameters you are given. It reads your `absorption_energies.csv` and compares your computed values against the expected ones. A crystal is considered correct if both energies fall within a predetermined tolerance of the expected values. Your reward is the fraction of crystals (with both energies correct) out of the total number of crystals. No partial credit per energy; both must match within tolerance for a crystal to count. The verifier's tolerance is chosen to accommodate numerical differences from implementation choices while still requiring faithful computation. The exact tolerance and expected values are hidden.
