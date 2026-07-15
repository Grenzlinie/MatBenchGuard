# Dipole Moment Calculation for Chlorocyclohexane Isomers using the Morino-Miyagawa Rule

## Problem background
Polyhalocyclohexanes, particularly substituted cyclohexane rings with chlorine atoms, can adopt many spatial arrangements due to the chair conformation of the ring. Determining which configuration a particular isomer possesses is often done by comparing experimentally measured dipole moments with calculated values. A simple vector addition of bond moments is insufficient because induced moments arising from neighbouring bonds affect the total dipole significantly. An empirical computational rule, the Morino-Miyagawa rule, was developed to account for these induced corrections, enabling more accurate predictions of molecular dipole moments for chlorocyclohexanes. This work provides a complete set of computed dipole moments and counts of sterically repulsive (1a,3a) axial chlorine atom pairs for all possible stable and inverted chair isomers of tetrachloro-, hexachloro-, and heptachlorocyclohexanes, forming a reference for assigning configurations from experimental measurements. Your task is to implement the rule and compute these values for the entire series of isomers.

## Approach
The Morino-Miyagawa empirical rule models a molecule as a set of C–Cl bond dipoles (bond moment 1.86 D) and adds induced moment corrections that depend on the geometry of neighbouring bonds. The chair cyclohexane ring has twelve substitution positions: axial (a) positions roughly parallel to the molecular symmetry axis, and equatorial (e) positions oriented at tetrahedral angles. Substitution of hydrogen by chlorine at various combinations of a and e sites yields many isomers for each level of chlorination. The stable chair and its ring-inverted counterpart (where all axial positions become equatorial and vice versa) generally have different energies and steric repulsions, chiefly between chlorine atoms in 1,3-diaxial positions. To reproduce the reported dipole moments, you must enumerate every possible configuration for tetrachlorocyclohexanes, hexachlorocyclohexanes, and heptachlorocyclohexanes, apply the Morino-Miyagawa rule to compute the resultant dipole vector and its magnitude (in Debye), and count the number of (1a,3a) chlorine–chlorine pairs. The method is fully described in the referenced 1950/1954 journal articles; your implementation should follow those descriptions. The complete list of isomers and their computed dipole moments and pair counts provides the reference that is compared with experimental observations to determine molecular configurations.

## Reproduction target
Compute the molecular dipole moment (in Debye) and the count of (1a,3a) axial chlorine atom pairs for every stable and inverted chair configuration of tetrachlorocyclohexanes, hexachlorocyclohexanes, and heptachlorocyclohexanes using the Morino-Miyagawa empirical rule. Output a single CSV file, `dipole_moments_results.csv`, with exactly the columns: `table_type` (a string label: `I` for hexachloro, `II` for heptachloro, `III` for tetrachloro), `form` (either `stable` or `inverted`), `configuration` (the axial/equatorial assignment string, e.g. `1e2e3e4e5e6e`), `dipole_moment_D` (float, in Debye), and `pairs_count` (integer). The CSV must include every isomer configuration that appears in the published tables for these three compound classes, including the inverted forms where applicable. The result is a numerical reference dataset; you do not need to compare with experimental measurements.

## Assets

- Morino, Miyagawa, Oiwa (1950) - Botyu-Kagaku, 15, 181
- Miyagawa (1954) - J. Chem. Soc. Japan, 75, 1061

## Workflow steps

### Step 1: Enumerate chlorocyclohexane configurations
- Role: process
- Action: Enumerate all possible axial (a) and equatorial (e) substitution configurations for tetrachloro-, hexachloro-, and heptachlorocyclohexane chair conformations, generating both stable and inverted forms. For each configuration, produce the assignment string (e.g., '1e2e3e4e5e6e' for hexachloro) and determine the number of (1a,3a) axial chlorine pairs. Save the list of configurations (table_type, form, configuration, pairs_count) to a temporary file.
- Evidence: `/app/outputs/enumerated_configurations.csv`

### Step 2: Compute dipole moments using the Morino-Miyagawa rule
- Role: scored (load-bearing)
- Action: Read the enumerated configurations from the previous step. For each configuration, compute the molecular dipole moment (in Debye) using the Morino-Miyagawa empirical rule as described in the literature (C-Cl bond moment 1.86 D, induced moment corrections). Report both the dipole moment and the (1a,3a) pair count in a final CSV file. The file must cover all isomers appearing in the paper's Tables I (hexachloro), II (heptachloro), and III (tetrachloro), including inverted forms where applicable.
- Output file: `/app/outputs/dipole_moments_results.csv`
- Format: csv
- Contract: table_type: string (I, II, or III), form: string (stable or inverted), configuration: string, dipole_moment_D: float, pairs_count: integer
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dipole_moments_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dipole_moments_results.csv
- path: `/app/outputs/dipole_moments_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with one row per isomer configuration. Columns: table_type (I, II, or III indicating the compound class and paper table), form (stable or inverted), configuration (axial/equatorial assignment string), dipole_moment_D (float, Debye), pairs_count (integer).
- schema:
  - `type`: table
  - `required_columns`: `table_type`, `form`, `configuration`, `dipole_moment_D`, `pairs_count`
  - `units`:
    - `dipole_moment_D`: Debye

Notes: The CSV must include all entries from the paper's Tables I, II, III. The hidden checker compares each row's dipole moment within a tolerance and pairs_count exactly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dipole_moments_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "table_type",
          "form",
          "configuration",
          "dipole_moment_D",
          "pairs_count"
        ],
        "units": {
          "dipole_moment_D": "Debye"
        }
      },
      "description": "CSV file with one row per isomer configuration. Columns: table_type (I, II, or III indicating the compound class and paper table), form (stable or inverted), configuration (axial/equatorial assignment string), dipole_moment_D (float, Debye), pairs_count (integer)."
    }
  ],
  "notes": "The CSV must include all entries from the paper's Tables I, II, III. The hidden checker compares each row's dipole moment within a tolerance and pairs_count exactly."
}
```

## How you are scored
Your sole scored artifact is `/app/outputs/dipole_moments_results.csv`. A hidden verifier will load this file and, for each row, compare your reported `dipole_moment_D` and `pairs_count` to reference values. The dipole moment must fall within a hidden tolerance of the expected value; the pairs count must match exactly. The final score is the fraction of rows that satisfy these checks, weighted by the total number of expected rows. There is no separate score for the intermediate configuration file; it is produced as process evidence. The verifier is independent and uses the exact row identity (table_type, form, configuration) to align comparisons. Because the target values are deterministic derivates of a published empirical rule, they can be verified without needing experimental measurements.
