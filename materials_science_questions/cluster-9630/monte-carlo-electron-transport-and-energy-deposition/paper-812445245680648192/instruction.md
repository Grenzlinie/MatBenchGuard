# Compute gamma-ray transition strengths from lifetime and branching data

## Problem background
Understanding the nuclear structure of $^{38}$Ar requires precise electromagnetic transition strengths, which test shell-model predictions. The nucleus exhibits both positive- and negative-parity levels arising from multi-particle, multi-hole excitations. Experimental lifetimes and gamma-ray branching ratios allow the derivation of transition strengths in Weisskopf units. These strengths reveal important collectivity and configuration mixing, guiding the improvement of nuclear models. This task focuses on computing those strengths from provided lifetime and branching-ratio data.

## Approach
Given tables of level lifetimes and branching ratios for $^{38}$Ar, compute for each observed gamma transition the partial radiative width using the relation $\Gamma = \hbar / \tau_{\text{partial}}$, where $\tau_{\text{partial}}$ is the effective lifetime accounting for the branching fraction. Express the strength in Weisskopf units by comparing to the single-particle estimate for the relevant multipolarity (E1, E2, M1, M2). When a mixing ratio is known, decompose the strength into the two respective multipoles; otherwise, assume a pure transition of the lowest allowed multipolarity. Propagate uncertainties from lifetime and branching-ratio uncertainties quadratically. Output the results as a CSV file.

## Reproduction target
Read the provided lifetime and branching-ratio tables. Compute the transition strength in Weisskopf units for every gamma cascade from a bound level whose lifetime is listed, using the branching ratios supplied. Output a CSV table with columns: initial_energy (MeV), final_energy (MeV), J_i_pi, J_f_pi, multipolarity, strength_Wu, uncertainty_Wu. The table must cover all observed transitions, with strengths and uncertainties properly propagated.

## Assets

- Lifetime data for 38Ar
- Branching ratios for 38Ar

## Workflow steps

### Step 1: Compute transition strengths
- Role: scored
- Action: Read the provided lifetime data and branching ratio tables. For each gamma transition, compute the partial radiative width using Gamma = hbar / tau_partial, where tau_partial is the effective lifetime corresponding to the branching fraction. Express the strength in Weisskopf units for each multipolarity (E1, E2, M1, M2) using the known mixing ratio or assuming a pure multipole transition when the mixing ratio is not given. Propagate uncertainties from lifetimes and branching ratios (add quadratically). Output the results as a CSV file.
- Output file: `/app/outputs/transition_strengths.csv`
- Format: csv
- Contract: Columns: initial_energy (MeV, float), final_energy (MeV, float), J_i_pi (string, e.g., '2+'), J_f_pi (string), multipolarity (string, e.g., 'E2', 'M1'), strength_Wu (float, Weisskopf units), uncertainty_Wu (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_strengths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_strengths.csv
- path: `/app/outputs/transition_strengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of experimental transition strengths for gamma-ray decays of bound levels in 38Ar, derived from the provided lifetimes and branching ratios.
- schema:
  - `type`: table
  - `required_columns`: `initial_energy`, `final_energy`, `J_i_pi`, `J_f_pi`, `multipolarity`, `strength_Wu`, `uncertainty_Wu`
  - `columns`:
    - `initial_energy`:
      - `type`: float
      - `unit`: MeV
      - `description`: Excitation energy of the initial level
    - `final_energy`:
      - `type`: float
      - `unit`: MeV
      - `description`: Excitation energy of the final level
    - `J_i_pi`:
      - `type`: string
      - `description`: Spin and parity of the initial level, e.g., '2+'
    - `J_f_pi`:
      - `type`: string
      - `description`: Spin and parity of the final level
    - `multipolarity`:
      - `type`: string
      - `description`: Multipolarity of the transition, e.g., 'E1', 'E2', 'M1', 'M2'. For mixed transitions, the dominant multipolarity is listed, or 'M1+E2' if mixing is significant and ratios are known.
    - `strength_Wu`:
      - `type`: float
      - `unit`: Weisskopf units
      - `description`: Gamma-ray transition strength expressed in Weisskopf units
    - `uncertainty_Wu`:
      - `type`: float
      - `unit`: Weisskopf units
      - `description`: Uncertainty of the transition strength (may be absent or empty for transitions with only an upper/lower limit)

Notes: The checker compares each computed strength (and multipolarity label) against hidden reference values extracted from Table 4 of the paper, using appropriate tolerances. Transitions must be correctly paired by initial/final energies and multipolarity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_strengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "initial_energy",
          "final_energy",
          "J_i_pi",
          "J_f_pi",
          "multipolarity",
          "strength_Wu",
          "uncertainty_Wu"
        ],
        "columns": {
          "initial_energy": {
            "type": "float",
            "unit": "MeV",
            "description": "Excitation energy of the initial level"
          },
          "final_energy": {
            "type": "float",
            "unit": "MeV",
            "description": "Excitation energy of the final level"
          },
          "J_i_pi": {
            "type": "string",
            "description": "Spin and parity of the initial level, e.g., '2+'"
          },
          "J_f_pi": {
            "type": "string",
            "description": "Spin and parity of the final level"
          },
          "multipolarity": {
            "type": "string",
            "description": "Multipolarity of the transition, e.g., 'E1', 'E2', 'M1', 'M2'. For mixed transitions, the dominant multipolarity is listed, or 'M1+E2' if mixing is significant and ratios are known."
          },
          "strength_Wu": {
            "type": "float",
            "unit": "Weisskopf units",
            "description": "Gamma-ray transition strength expressed in Weisskopf units"
          },
          "uncertainty_Wu": {
            "type": "float",
            "unit": "Weisskopf units",
            "description": "Uncertainty of the transition strength (may be absent or empty for transitions with only an upper/lower limit)"
          }
        }
      },
      "description": "Table of experimental transition strengths for gamma-ray decays of bound levels in 38Ar, derived from the provided lifetimes and branching ratios."
    }
  ],
  "notes": "The checker compares each computed strength (and multipolarity label) against hidden reference values extracted from Table 4 of the paper, using appropriate tolerances. Transitions must be correctly paired by initial/final energies and multipolarity."
}
```

## How you are scored
A hidden verifier will compare the transition_strengths.csv you output against the expected strengths derived from the literature. For each transition, the verifier checks that the multipolarity label is correct and that the strength value lies within an allowed tolerance derived from the reference uncertainties. Transitions that do not appear in the expected set or whose strength falls outside the tolerance are counted as incorrect. Your final score is the fraction of transitions that match.
