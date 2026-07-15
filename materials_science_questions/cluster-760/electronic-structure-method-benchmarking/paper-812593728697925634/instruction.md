# Ab Initio Thermochemistry of Substituted Methyl Radicals

## Problem background
The stability and structure of carbon‑centered organic radicals are strongly influenced by substituent effects and protonation. Understanding how protonation alters radical properties is key to predicting reaction intermediates in organic and bioorganic chemistry. This task involves a computational study of a set of substituted methyl radicals (•CH₂X) and their protonated forms (•CH₂XH⁺), along with their closed‑shell analogues (CH₃X and CH₃XH⁺). The substituents X span a range of π‑donor and π‑acceptor groups: NH₂, OH, OCH₃, PH₂, SH, F, Cl, Br, CN, CHO, and NO₂. The challenge is to quantify the effects of protonation on bond lengths, radical stability, proton affinity, and thermochemistry using high‑level ab initio theory.

## Approach
The reproduction uses the G2 composite protocol. Structures and harmonic vibrational frequencies are computed at the MP2(full)/6‑31G(d) and HF/6‑31G(d) levels, respectively. Zero‑point energies are scaled by 0.8929. Single‑point energies are obtained at the QCISD(T)/6‑311+G(3df,2p) level, and the G2 total energy is formed by adding a standard higher‑level correction and the scaled ZPE. Radical stabilization energies are derived from isodesmic reactions comparing substituted radicals with methane and the methyl radical. Proton affinities are computed from the enthalpy differences between protonated and unprotonated species. Heats of formation are obtained via the atomization method, combining G2 total energies with known experimental atomic heats of formation and thermal corrections. All computations should be carried out with an open‑source quantum chemistry package such as Psi4.

## Reproduction target
For all 44 species (CH₃X, CH₃XH⁺, •CH₂X, •CH₂XH⁺; X as listed above), report:

- Equilibrium C–X bond lengths (Å) from MP2(full)/6‑31G(d) geometries.
- Radical stabilization energies (kJ mol⁻¹) at 298 K for •CH₂X and •CH₂XH⁺.
- Proton affinities (kJ mol⁻¹) at 298 K for CH₃X and •CH₂X.
- Heats of formation (kJ mol⁻¹) at 298 K for all 44 species.

These must be written to the specified CSV files (bond_lengths.csv, rse.csv, pa.csv, heats_of_formation.csv) following the column schemas defined in the workflow steps.

## Assets

- Psi4 quantum chemistry package: psi4
- Basis sets 6-31G(d) and 6-311+G(3df,2p)
- Experimental atomic heats of formation

## Workflow steps

### Step 1: Geometry optimization and frequency calculation
- Role: process
- Action: For each of the 44 species (CH3X, CH3XH+, •CH2X, •CH2XH+ with X = NH2, OH, OCH3, PH2, SH, F, Cl, Br, CN, CHO, NO2), perform a full geometry optimization at the MP2(full)/6-31G(d) level and a harmonic vibrational frequency calculation at the HF/6-31G(d) level. Save the optimized Cartesian coordinates in an XYZ file and the scaled (factor 0.8929) zero-point vibrational energies in a CSV file.
- Evidence: `/app/outputs/optimized_geometries.xyz,zpe.csv`

### Step 2: Extract C–X bond lengths
- Role: scored
- Action: For each species, extract the equilibrium C–X bond length (in Å) from the optimized geometry. Write the results to bond_lengths.csv.
- Output file: `/app/outputs/bond_lengths.csv`
- Format: csv
- Contract: X (substituent identifier), species (one of CH3X, CH3XH+, dotCH2X, dotCH2XH+), r_CX_angstrom (float in Å).
- Scoring: scored by hidden verifier

### Step 3: G2 total energy calculation
- Role: process
- Action: Using the optimized geometries and scaled ZPEs, compute G2 total energies at 0 K and 298 K for all species following the published G2 recipe: QCISD(T)/6-311+G(3df,2p) single-point, add the standard higher-level correction (HLC) and ZPE. Save the energies in g2_total_energies.csv.
- Evidence: `/app/outputs/g2_total_energies.csv`

### Step 4: Radical stabilization energies
- Role: scored (load-bearing)
- Action: Calculate radical stabilization energies (RSEs) at 298 K from the G2 total energies using the isodesmic reaction •CH2X + CH4 → CH3X + •CH3 (and the analogous reaction for protonated forms). Write the results to rse.csv.
- Output file: `/app/outputs/rse.csv`
- Format: csv
- Contract: X (substituent identifier), state (one of dotCH2X, dotCH2XH+), RSE_kJmol (float at 298 K).
- Scoring: scored by hidden verifier

### Step 5: Proton affinities
- Role: scored
- Action: Calculate proton affinities (PA) at 298 K from the G2 total energies of CH3X, •CH2X, and the corresponding protonated species. Write the results to pa.csv.
- Output file: `/app/outputs/pa.csv`
- Format: csv
- Contract: X (substituent identifier), species (one of CH3X, dotCH2X), PA_kJmol (float at 298 K).
- Scoring: scored by hidden verifier

### Step 6: Heats of formation
- Role: scored
- Action: Calculate heats of formation ΔfH°₂₉₈ for all 44 species using the atomization method: combine G2 total energies with experimental atomic heats of formation and thermal corrections. Write the results to heats_of_formation.csv.
- Output file: `/app/outputs/heats_of_formation.csv`
- Format: csv
- Contract: X (substituent identifier), species (one of CH3X, CH3XH+, dotCH2X, dotCH2XH+), HOF_kJmol (float at 298 K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bond_lengths.csv`
- `/app/outputs/rse.csv`
- `/app/outputs/pa.csv`
- `/app/outputs/heats_of_formation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bond_lengths.csv
- path: `/app/outputs/bond_lengths.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium C–X bond lengths for all 44 species computed at MP2(full)/6-31G(d) level.
- schema:
  - `type`: table
  - `required_columns`: `X`, `species`, `r_CX_angstrom`
  - `units`:
    - `r_CX_angstrom`: Å

### rse.csv
- path: `/app/outputs/rse.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Radical stabilization energies at 298 K derived from G2 total energies.
- schema:
  - `type`: table
  - `required_columns`: `X`, `state`, `RSE_kJmol`
  - `units`:
    - `RSE_kJmol`: kJ mol⁻¹

### pa.csv
- path: `/app/outputs/pa.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Proton affinities at 298 K derived from G2 total energies.
- schema:
  - `type`: table
  - `required_columns`: `X`, `species`, `PA_kJmol`
  - `units`:
    - `PA_kJmol`: kJ mol⁻¹

### heats_of_formation.csv
- path: `/app/outputs/heats_of_formation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Heats of formation at 298 K computed via the atomization method using G2 total energies and experimental atomic heats of formation.
- schema:
  - `type`: table
  - `required_columns`: `X`, `species`, `HOF_kJmol`
  - `units`:
    - `HOF_kJmol`: kJ mol⁻¹

Notes: All outputs are compared to hidden paper-reported values with appropriate tolerances. The bond lengths, RSEs, PAs, and heats of formation must be internally consistent with the underlying G2 energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bond_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "X",
          "species",
          "r_CX_angstrom"
        ],
        "units": {
          "r_CX_angstrom": "Å"
        }
      },
      "description": "Equilibrium C–X bond lengths for all 44 species computed at MP2(full)/6-31G(d) level."
    },
    {
      "file": "rse.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "X",
          "state",
          "RSE_kJmol"
        ],
        "units": {
          "RSE_kJmol": "kJ mol⁻¹"
        }
      },
      "description": "Radical stabilization energies at 298 K derived from G2 total energies."
    },
    {
      "file": "pa.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "X",
          "species",
          "PA_kJmol"
        ],
        "units": {
          "PA_kJmol": "kJ mol⁻¹"
        }
      },
      "description": "Proton affinities at 298 K derived from G2 total energies."
    },
    {
      "file": "heats_of_formation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "X",
          "species",
          "HOF_kJmol"
        ],
        "units": {
          "HOF_kJmol": "kJ mol⁻¹"
        }
      },
      "description": "Heats of formation at 298 K computed via the atomization method using G2 total energies and experimental atomic heats of formation."
    }
  ],
  "notes": "All outputs are compared to hidden paper-reported values with appropriate tolerances. The bond lengths, RSEs, PAs, and heats of formation must be internally consistent with the underlying G2 energies."
}
```

## How you are scored
The hidden verifier will assign a weighted score across all four scored artifacts. For each file, the verifier compares your computed values against hidden reference results, using tolerances that reflect the expected spread from different implementations of the G2 protocol. The verifier also checks internal consistency: e.g., relationships between bond lengths in corresponding closed‑shell and radical species, and consistency of thermochemical cycles (RSE, PA, and heats of formation should be derivable from the same underlying total energies). The final reward is the weighted sum of the stage scores. Simply reporting the paper’s published numbers is not a valid solution; you must genuinely perform the ab initio calculations.
