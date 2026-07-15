# Group-theoretical vibrational mode decomposition for crystalline solids

## Problem background
The vibrational modes of a crystal are determined by its unit-cell arrangement and space-group symmetry. Factor-group analysis uses group theory to decompose the 3N-dimensional space of atomic displacements into irreducible representations of the crystal's point group. Each irreducible representation carries a selection rule: Raman active, infrared active (with a specific polarization direction), inactive, or silent. Because this classification follows from symmetry alone, it provides a rigorous prediction of the number and type of bands expected in a vibrational spectrum, independent of detailed bonding models.

## Approach
For a given crystal structure, the factor-group analysis proceeds in three stages. First, obtain the space group and the Wyckoff positions of the atoms (the number of atoms remaining invariant under each symmetry operation). Second, construct the reducible representation of the 3N translational vector: for each symmetry class, the character is χ_ρ = ω_ρ × (±1 + 2 cos θ), where ω_ρ is the number of atoms that do not move under that operation, the sign is positive for proper rotations and negative for improper rotations, and θ is the rotation angle. Third, reduce this representation using the orthogonality theorem and the character table of the factor group to obtain the number of modes of each irreducible representation. Finally, determine the activity (Raman / infrared / inactive) from the transformation properties of each irreducible representation and, for infrared-active modes, note the polarization direction (e.g., E||c or E⊥c) when applicable. The analysis is applied to a set of well-known crystal structure types: the three TiO₂ polymorphs (rutile, anatase, brookite), two Ga₂O₃ polymorphs (corundum-type α-Ga₂O₃ and monoclinic β-Ga₂O₃), two ZrO₂ polymorphs (fluorite-type cubic and baddeleyite-type monoclinic), ordered rocksalt Li₃NbO₄, ilmenite-type MnTiO₃, ordered spinel LiAl₅O₈, and trirutile-type ZnSb₂O₆ and MgSb₂O₆. The required crystal structure data (space groups and atomic coordinates) are publicly available from crystallographic databases or the original structure papers; character tables can be taken from standard group-theory references or generated from group generators.

## Reproduction target
Compute the factor-group decomposition of the zone-centre vibrational modes for the following 12 crystal structure entries exactly as labelled: `rutile`, `anatase`, `brookite`, `corundum_alpha_Ga2O3`, `beta_Ga2O3`, `cubic_ZrO2`, `monoclinic_ZrO2`, `Li3NbO4`, `ilmenite_MnTiO3`, `ordered_LiAl5O8`, `trirutile_ZnSb2O6`, `trirutile_MgSb2O6`. For each structure, produce a decomposition string that lists the number of modes in each irreducible representation with its activity: Raman active (R), infrared active (IR) with polarisation direction (e.g., E||c or E⊥c) when known, or inactive (−). The string must follow the style (example for rutile) `"A1g(R) + A2g(-) + B1g(R) + B2g(R) + Eg(R) + A2u(IR, E||c) + 2B1u(-) + 3Eu(IR, E⊥c)"`. Also output the Hermann-Mauguin space group symbol (e.g., `"P42/mnm"`) for each structure. Write the complete results to `/app/outputs/factor_group_decompositions.json` as a JSON object whose keys are the structure identifiers above, each value an object with required fields `"decomposition"` (string) and `"space_group"` (string).

## Assets

- Crystallographic structure data for rutile, anatase, brookite TiO2; alpha- and beta-Ga2O3; cubic and monoclinic ZrO2; Li3NbO4; MnTiO3 ilmenite; ordered LiAl5O8; trirutile ZnSb2O6 and MgSb2O6
- Character tables for point groups D4h, D2h, D3d, C2h, T, Oh, O, S6, and related groups

## Workflow steps

### Step 1: Factor-group analysis of lattice vibrations
- Role: scored (load-bearing)
- Action: For each of the crystal structures listed in the output schema, obtain the space group and atomic positions from public crystallographic databases or the cited literature. Construct the reducible representation from the 3N-dimensional translation vector using characters χ_ρ = ω_ρ (±1 + 2 cos θ), then reduce it with the orthogonality theorem to obtain the number of modes in each irreducible representation. Classify each mode as Raman active (R), infrared active (IR) with polarization directions (e.g., E||c), inactive (-), or silent. Output the full decomposition string using the same notation as the paper (e.g., 'A1g(R) + A2g(-) + B1g(R) + B2g(R) + Eg(R) + A2u(IR, E||c) + 2B1u(-) + 3Eu(IR, E⊥c)'). Record the space group for each structure.
- Output file: `/app/outputs/factor_group_decompositions.json`
- Format: json
- Contract: JSON object with top-level keys: 'rutile', 'anatase', 'brookite', 'corundum_alpha_Ga2O3', 'beta_Ga2O3', 'cubic_ZrO2', 'monoclinic_ZrO2', 'Li3NbO4', 'ilmenite_MnTiO3', 'ordered_LiAl5O8', 'trirutile_ZnSb2O6', 'trirutile_MgSb2O6'. Each value is an object with required fields: 'decomposition' (string, e.g., 'A1g(R) + A2g(-) + B1g(R) + B2g(R) + Eg(R) + A2u(IR, E||c) + 2B1u(-) + 3Eu(IR, E⊥c)') and 'space_group' (string, e.g., 'P42/mnm').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/factor_group_decompositions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### factor_group_decompositions.json
- path: `/app/outputs/factor_group_decompositions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Factor-group decomposition of vibrational modes for the listed crystal structures, with IR/Raman activity labels and space group.
- schema:
  - `type`: object
  - `required_keys`: `rutile`, `anatase`, `brookite`, `corundum_alpha_Ga2O3`, `beta_Ga2O3`, `cubic_ZrO2`, `monoclinic_ZrO2`, `Li3NbO4`, `ilmenite_MnTiO3`, `ordered_LiAl5O8`, `trirutile_ZnSb2O6`, `trirutile_MgSb2O6`
  - `value_schema`:
    - `type`: object
    - `required_fields`: `decomposition`, `space_group`
    - `decomposition`: string
    - `space_group`: string

Notes: The checker normalizes whitespace and ordering of terms in the decomposition strings before comparing them to the paper-reported reference. Exact match after normalization is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "factor_group_decompositions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "rutile",
          "anatase",
          "brookite",
          "corundum_alpha_Ga2O3",
          "beta_Ga2O3",
          "cubic_ZrO2",
          "monoclinic_ZrO2",
          "Li3NbO4",
          "ilmenite_MnTiO3",
          "ordered_LiAl5O8",
          "trirutile_ZnSb2O6",
          "trirutile_MgSb2O6"
        ],
        "value_schema": {
          "type": "object",
          "required_fields": [
            "decomposition",
            "space_group"
          ],
          "decomposition": "string",
          "space_group": "string"
        }
      },
      "description": "Factor-group decomposition of vibrational modes for the listed crystal structures, with IR/Raman activity labels and space group."
    }
  ],
  "notes": "The checker normalizes whitespace and ordering of terms in the decomposition strings before comparing them to the paper-reported reference. Exact match after normalization is required."
}
```

## How you are scored
A hidden verifier reads your `factor_group_decompositions.json`. It normalises the whitespace and the ordering of terms within each decomposition string (so that e.g., `A1g + A2g` is equivalent to `A2g + A1g`), then compares each string to the unique correct decomposition for that structure. Every structure that matches exactly after normalisation earns full credit; a mismatch earns no credit for that structure. All structures carry equal weight, and the total reward is the fraction of structures that match. There is no partial credit for an individual string — the decomposition is an exact consequence of the space group and atomic positions, so any deviation is wrong.
