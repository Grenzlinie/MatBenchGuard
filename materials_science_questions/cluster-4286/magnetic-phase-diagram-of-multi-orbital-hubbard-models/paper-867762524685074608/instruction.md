# Zero-temperature phase diagram of orbital-selective Mott transitions in the two-orbital Hubbard model

## Problem background
The two-orbital Hubbard model with different bandwidths and Hund coupling exhibits orbital-selective Mott transitions (OSMT). At half-filling, varying the interaction strength can localize one orbital while leaving the other itinerant, before ultimately driving both insulating. Understanding the ground-state phase diagram and the residual entropies of the resulting phases is a key problem in strongly correlated electron systems.

## Approach
The Self-Energy Functional Approach (SFA) maps the interacting lattice problem onto a reference system with two sites per orbital, characterized by variational hybridization parameters V1 and V2. For the half-filled model with semi-circular densities of states of bandwidths W1=2.0 and W2=4.0, and interaction parameters U'=0.5U, J=0.25U (satisfying U = U' + 2J), one evaluates the grand potential Ω(V1,V2) on a grid of V1,V2 values. The physical state corresponds to the stationary point(s) that minimize Ω. By sweeping the intra-orbital interaction U from 2.0 to 4.0 (in steps of 0.1, or finer near potential transitions), one obtains the U-dependence of the stationary hybridizations and the associated entropy per site S/L. This yields the zero-temperature phase diagram.

## Reproduction target
Implement the SFA procedure described above. For each U, compute the stationary values of V1, V2 and the entropy per site S/L. Save these as a CSV file with columns U, V1, V2, S_over_L. Then, using these results, determine the critical interactions at which each hybridization first becomes zero (if such transitions occur) and the residual entropy per site in any phase where one or both hybridizations vanish. Report these extracted quantities in a text file (transition_report.txt).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute zero-temperature SFA phase diagram
- Role: scored (load-bearing)
- Action: Implement the Self-Energy Functional Approach (SFA) with a two-site reference Hamiltonian for the half-filled two-orbital Hubbard model. Use bandwidths W1=2.0, W2=4.0, interaction ratios U'=0.5U, J=0.25U, semi-circular DOS, and enforce half-filling. For U from 2.0 to 4.0 in steps of 0.1 (or finer near transitions), compute the grand potential Ω(V1,V2) on a grid of hybridizations V1,V2, locate the stationary point(s) that minimize Ω, and record the corresponding V1, V2, and the entropy per site S/L. Output results to phase_diagram.csv.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: columns: U (float), V1 (float), V2 (float), S_over_L (float). U ranges from 2.0 to 4.0 in increments of 0.1 (finer scan near transitions allowed).
- Scoring: scored by hidden verifier

### Step 2: Extract critical interactions and residual entropies
- Role: scored
- Action: From the computed phase_diagram.csv, identify the critical interaction U_c1 where V1 first becomes zero (metal→OSM transition) and U_c2 where V2 becomes zero (OSM→MI transition). Determine the residual entropy S/L in the OSM phase (where V1=0, V2>0) and in the MI phase (both zero). Write these four values to a text file.
- Output file: `/app/outputs/transition_report.txt`
- Format: txt
- Contract: Lines: 'U_c1: <float>', 'U_c2: <float>', 'S_OSM: <float>', 'S_MI: <float>'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/transition_report.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Zero-temperature SFA stationary-point results.
- schema:
  - `type`: table
  - `required_columns`: `U`, `V1`, `V2`, `S_over_L`
  - `units`:
    - `U`: energy scale
    - `V1`: same
    - `V2`: same
    - `S_over_L`: dimensionless

### transition_report.txt
- path: `/app/outputs/transition_report.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Extracted zero-temperature critical interactions and residual entropies.
- schema:
  - `type`: text
  - `required`: `U_c1`, `U_c2`, `S_OSM`, `S_MI`

Notes: The checker recomputes critical interactions and entropies from the raw CSV and compares to paper-reported values. Finite‑T and global‑J stages are beyond the minimal core per the approved taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "V1",
          "V2",
          "S_over_L"
        ],
        "units": {
          "U": "energy scale",
          "V1": "same",
          "V2": "same",
          "S_over_L": "dimensionless"
        }
      },
      "description": "Zero-temperature SFA stationary-point results."
    },
    {
      "file": "transition_report.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": [
          "U_c1",
          "U_c2",
          "S_OSM",
          "S_MI"
        ]
      },
      "description": "Extracted zero-temperature critical interactions and residual entropies."
    }
  ],
  "notes": "The checker recomputes critical interactions and entropies from the raw CSV and compares to paper-reported values. Finite‑T and global‑J stages are beyond the minimal core per the approved taskability scope."
}
```

## How you are scored
A hidden verifier will independently score each artifact. For phase_diagram.csv, the verifier will check the file format and that the computed V1, V2, and entropies evolve reasonably. For transition_report.txt, the verifier will compare the reported critical interactions and residual entropies against hidden reference values (derived from the correct SFA solution). The final reward is a weighted combination of these scores; a correct implementation that faithfully executes the SFA will achieve the highest reward. Guessing or copying values from the literature without running the computation will not pass, because the hidden reference may not exactly match any single reported number due to subtle implementation choices.
