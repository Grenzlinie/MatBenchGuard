# Group-theoretical classification of Cr³⁺ pair electronic states and optical selection rules

## Problem background
The optical spectra of Cr³⁺ pairs in ruby (first and second nearest neighbour) are well resolved and offer a probe for exchange interactions between 3d ions. To analyze these spectra, knowledge of the symmetry properties of the electronic pair states is required. The pair states can be derived from the known single‑ion electronic states by applying group‑theoretical induction, taking into account the site symmetries of the ions in the crystal.

## Approach
This task implements the group‑theoretical induction method to classify the orbital states of Cr³⁺ pairs. Starting from the octahedral single‑ion states (⁴A₂g, ²E_g, ²T₁g, ²T₂g), we first reduce them to the appropriate site symmetries (C₃ᵥ for 1.n.n. pairs, C₂ᵥ for 2.n.n. pairs) using standard correlation tables. Then, for each pair type, we construct the product basis of two‑ion states, apply the induction formulas to obtain the characters of the pair representation under the full pair symmetry group (D₃ₕ for 1.n.n., D₂ₕ for 2.n.n.), and decompose these characters into irreducible representations. After classifying the orbital states and their allowed total spin values, we use the group multiplication tables together with the dipole operator representations to determine the symmetry‑allowed electric dipole transitions and their polarizations. All steps rely on publicly available character tables and can be implemented with open‑source group‑theory libraries such as SymPy.

## Reproduction target
The goal is to produce four tables: (1) the orbital state decompositions for 1.n.n. pairs, including the single‑ion reduction in C₃ᵥ and the resulting D₃ₕ irreps with allowed total spin; (2) the electric dipole selection rules for 1.n.n. pairs, listing initial and final irreps, polarization, and whether the transition is allowed; (3) the orbital state decompositions for 2.n.n. pairs; (4) the electric dipole selection rules for 2.n.n. pairs. All irreducible representations are to be given in the notation of Koster et al. (e.g., A₁′, A₂″, E′, etc., for D₃ₕ; A_g, B₁u, etc., for D₂ₕ). The tables must be written as CSV files with columns as specified in the workflow steps. The computation is deterministic; therefore the correctness of each table is assessed by exact string match against the group‑theoretically derived reference.

## Assets

- SymPy: sympy
- Character tables for O_h, C₃ᵥ, D₃ₕ, C₂ᵥ, D₂ₕ

## Workflow steps

### Step 1: Single‑ion state reduction to site symmetries
- Role: process
- Action: Determine the irreducible representations of the Cr³⁺ single‑ion states (⁴A₂g, ²E_g, ²T₁g, ²T₂g) in the site symmetries C₃ᵥ (for 1.n.n. pairs) and C₂ᵥ (for 2.n.n. pairs) using standard correlation tables. Record the mappings as a JSON file.
- Evidence: `/app/outputs/single_ion_reduction.json`

### Step 2: Orbital states for 1.n.n. pairs
- Role: scored (load-bearing)
- Action: Using the C₃ᵥ representations from Step 1 and the induction formulas for D₃ₕ, compute the irreducible representations for all pair configurations given in the paper (Table 2). Write the results to table_1nn_orbital_states.csv.
- Output file: `/app/outputs/table_1nn_orbital_states.csv`
- Format: csv
- Contract: Columns: configuration (string), c3v_reduction (string), d3h_representation (string), allowed_spin (string). One row per configuration.
- Scoring: scored by hidden verifier

### Step 3: Selection rules for 1.n.n. pairs
- Role: scored
- Action: From the orbital states of 1.n.n. pairs and the dipole operator representations in D₃ₕ, determine the allowed electric dipole transitions and their polarizations as given in the paper (Table 3). Write table_1nn_selection_rules.csv.
- Output file: `/app/outputs/table_1nn_selection_rules.csv`
- Format: csv
- Contract: Columns: initial_repr (string), final_repr (string), polarization (string), allowed (bool). One row per initial-final pair.
- Scoring: scored by hidden verifier

### Step 4: Orbital states for 2.n.n. pairs
- Role: scored (load-bearing)
- Action: Using the C₂ᵥ representations from Step 1 and the induction formulas for D₂ₕ, compute the irreducible representations for all pair configurations given in the paper (Table 6). Write table_2nn_orbital_states.csv.
- Output file: `/app/outputs/table_2nn_orbital_states.csv`
- Format: csv
- Contract: Columns: configuration (string), c2v_reduction (string), d2h_representation (string), allowed_spin (string). One row per configuration.
- Scoring: scored by hidden verifier

### Step 5: Selection rules for 2.n.n. pairs
- Role: scored
- Action: From the orbital states of 2.n.n. pairs and the dipole operator representations in D₂ₕ, determine the allowed electric dipole transitions and their polarizations as given in the paper (Table 7). Write table_2nn_selection_rules.csv.
- Output file: `/app/outputs/table_2nn_selection_rules.csv`
- Format: csv
- Contract: Columns: initial_repr (string), final_repr (string), polarization (string), allowed (bool). One row per initial-final pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_1nn_orbital_states.csv`
- `/app/outputs/table_1nn_selection_rules.csv`
- `/app/outputs/table_2nn_orbital_states.csv`
- `/app/outputs/table_2nn_selection_rules.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_1nn_orbital_states.csv
- path: `/app/outputs/table_1nn_orbital_states.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Orbital state decompositions for first nearest neighbour Cr³⁺ pairs. The irreducible representation strings and configuration names must exactly match the paper.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `c3v_reduction`, `d3h_representation`, `allowed_spin`

### table_1nn_selection_rules.csv
- path: `/app/outputs/table_1nn_selection_rules.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electric dipole selection rules for 1.n.n. pairs. The allowed boolean and representation strings must exactly match the paper.
- schema:
  - `type`: table
  - `required_columns`: `initial_repr`, `final_repr`, `polarization`, `allowed`

### table_2nn_orbital_states.csv
- path: `/app/outputs/table_2nn_orbital_states.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Orbital state decompositions for second nearest neighbour Cr³⁺ pairs.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `c2v_reduction`, `d2h_representation`, `allowed_spin`

### table_2nn_selection_rules.csv
- path: `/app/outputs/table_2nn_selection_rules.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electric dipole selection rules for 2.n.n. pairs.
- schema:
  - `type`: table
  - `required_columns`: `initial_repr`, `final_repr`, `polarization`, `allowed`

Notes: All outputs are deterministic group-theoretical tables. The checker compares each row/entry exactly against the paper’s published tables. Spin-orbit coupling and symmetry reductions are excluded per taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_1nn_orbital_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "c3v_reduction",
          "d3h_representation",
          "allowed_spin"
        ]
      },
      "description": "Orbital state decompositions for first nearest neighbour Cr³⁺ pairs. The irreducible representation strings and configuration names must exactly match the paper."
    },
    {
      "file": "table_1nn_selection_rules.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "initial_repr",
          "final_repr",
          "polarization",
          "allowed"
        ]
      },
      "description": "Electric dipole selection rules for 1.n.n. pairs. The allowed boolean and representation strings must exactly match the paper."
    },
    {
      "file": "table_2nn_orbital_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "c2v_reduction",
          "d2h_representation",
          "allowed_spin"
        ]
      },
      "description": "Orbital state decompositions for second nearest neighbour Cr³⁺ pairs."
    },
    {
      "file": "table_2nn_selection_rules.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "initial_repr",
          "final_repr",
          "polarization",
          "allowed"
        ]
      },
      "description": "Electric dipole selection rules for 2.n.n. pairs."
    }
  ],
  "notes": "All outputs are deterministic group-theoretical tables. The checker compares each row/entry exactly against the paper’s published tables. Spin-orbit coupling and symmetry reductions are excluded per taskability scope."
}
```

## How you are scored
A hidden verifier independently scores each of the four scored output files. For each table, the verifier compares your submitted rows against a hidden reference (derived from the paper’s published results) using exact match: every irreducible representation string must be identical, and every boolean selection rule entry must match. Partial credit is assigned per row; the total score is a weighted sum across the four tables, with the orbital state tables carrying the highest weight. There is no tolerance for approximate answers—group‑theoretical results are exact. The verifier does not grant credit for merely reporting plausible numbers; it checks whether the submitted tables are consistent with the group‑theoretic induction method applied to the specified single‑ion states. You must therefore compute each table from first principles; guessing or fabricating values will result in a low score.
