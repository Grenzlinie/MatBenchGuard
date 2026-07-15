# CBS-extrapolated thermochemical energies for third-row G2 test set

## Problem background
Accurate thermochemical data—atomization energies, ionization energies, electron affinities, and proton affinities—for small molecules containing third‑row (Ga–Kr) atoms are vital for benchmarking electronic structure methods and for use in reaction databases. The G2 third‑row test suite provides a set of 40 experimental reference values (19 atomization energies, 15 ionization energies, 4 electron affinities, and 2 proton affinities) that form a challenging benchmark. This study investigates the performance of two widely used electronic structure approaches: the coupled‑cluster CCSD(T) method and the B3LYP density functional, each combined with the augmented correlation‑consistent basis sets aug‑cc‑pVnZ (n = Q, 5). By extrapolating the computed properties to the complete basis set (CBS) / Kohn–Sham limit and comparing them with the experimental references, the goal is to assess the accuracy of each method for this set of third‑row molecules.

## Approach
For every molecule in the G2 third‑row test set, geometries are optimized and harmonic vibrational frequencies are computed at the CCSD(T)/aug‑cc‑pVnZ and B3LYP/aug‑cc‑pVnZ levels (n = Q, 5). CCSD(T) calculations employ the frozen‑core approximation. Using the optimized structures, total energies of all neutral, cationic, anionic, and protonated species are obtained at the same levels. Zero‑point energy corrections (derived from the frequencies) and spin–orbit corrections (obtained from standard literature compilations) are applied, and the four thermochemical properties—atomization energy (AE), ionization energy (IE), electron affinity (EA), and proton affinity (PA)—are derived at each basis set level. For each property and each method, the two‑point extrapolation formula

P(∞) = [P(5)×5³ − P(4)×4³]/(5³ − 4³)

is applied to the Q‑ and 5‑zeta results to obtain the CBS (CCSD(T)) or KS (B3LYP) limit. The extrapolated values for all 40 test cases are then compared with the experimental reference values. The comparison is summarized by computing the per‑property and total mean absolute deviation (MAD), with IE, EA, and PA MADs converted to kcal/mol using 1 eV = 23.0605 kcal/mol.

## Reproduction target
Produce the CBS‑limit extrapolated energies for CCSD(T) and the KS‑limit extrapolated energies for B3LYP for all 40 thermochemical data points of the G2 third‑row test set. Write the per‑molecule extrapolated values into the structured CSV files specified in the workflow steps. Then compute the per‑property mean absolute deviation (AE, IE, EA, PA) and the total mean absolute deviation across all 40 energies for each method, after converting IE, EA, and PA MADs to kcal/mol (1 eV = 23.0605 kcal/mol). Report the summary as JSON. The correctness of the extrapolated energies and the resulting MADs is the concrete objective.

## Assets

- aug-cc-pVQZ basis set for elements H, B, C, N, O, F, Na, Al, Si, P, S, Cl, Ga, Ge, As, Se, Br, Kr: https://www.basissetexchange.org
- aug-cc-pV5Z basis set for elements H, B, C, N, O, F, Na, Al, Si, P, S, Cl, Ga, Ge, As, Se, Br, Kr: https://www.basissetexchange.org
- G2 third-row test set molecules
- Open-source quantum chemistry software
- Experimental reference values for G2 third-row test set
- Spin-orbit corrections for third-row atoms and molecules: 10.1002/(SICI)1097-461X(1997)61:6<943::AID-QUA2>3.0.CO;2-T

## Workflow steps

### Step 1: Geometry optimization and frequency calculation
- Role: process
- Action: For every molecule in the G2 third-row test set, perform geometry optimization and harmonic frequency calculation at the CCSD(T) and B3LYP levels using the aug-cc-pVQZ and aug-cc-pV5Z basis sets. Apply the frozen-core approximation for CCSD(T). Retain optimized structures and zero-point energy corrections for each level of theory.
- Evidence: `/app/outputs/geometry_and_zpe_log.txt`

### Step 2: Raw energy calculation and property derivation
- Role: process
- Action: Using the optimized geometries from step01, compute total energies of all molecules, atoms, and relevant cations/anions at the same levels of theory. Derive atomization energies (kcal/mol), ionization energies (eV), electron affinities (eV), and proton affinities (eV) for all 40 test cases, applying zero-point energy corrections and spin-orbit corrections as described in the paper. Retain the raw property values at each basis set level for later extrapolation.
- Evidence: `/app/outputs/raw_energies_log.txt`

### Step 3: CCSD(T) CBS limit extrapolation
- Role: scored (load-bearing)
- Action: For each of the 40 energies (atomization, ionization, electron affinity, proton affinity) computed with CCSD(T)/aug-cc-pVQZ and aug-cc-pV5Z, apply the two-point CBS extrapolation formula P(∞) = [P(5)×5³ − P(4)×4³] / (5³ − 4³). Write every extrapolated value to extrapolated_values_ccsd.csv.
- Output file: `/app/outputs/extrapolated_values_ccsd.csv`
- Format: csv
- Contract: CSV with columns: molecule (string), property (string, one of AE/IE/EA/PA), extrapolated_value (float), method (string='CCSD(T)'). One row per molecule per property. All 40 energies (19 AE, 15 IE, 4 EA, 2 PA) must be present.
- Scoring: scored by hidden verifier

### Step 4: B3LYP KS limit extrapolation
- Role: scored (load-bearing)
- Action: For each of the 40 energies computed with B3LYP/aug-cc-pVQZ and aug-cc-pV5Z, apply the same two-point KS extrapolation formula. Write every extrapolated value to extrapolated_values_b3lyp.csv.
- Output file: `/app/outputs/extrapolated_values_b3lyp.csv`
- Format: csv
- Contract: CSV with columns: molecule (string), property (string, one of AE/IE/EA/PA), extrapolated_value (float), method (string='B3LYP'). One row per molecule per property. All 40 energies must be present.
- Scoring: scored by hidden verifier

### Step 5: Error analysis and metrics summary
- Role: scored
- Action: Compute the per-property mean absolute deviation (MAD) for atomization energies, ionization energies, electron affinities, and proton affinities against the experimental reference values for both methods. Convert IE, EA, PA MADs to kcal/mol using 1 eV = 23.0605 kcal/mol. Compute the total MAD across all 40 energies for each method. Write a summary JSON file metrics_summary.json containing method, per_property_mad list with property name and mad_kcal_mol, and total_mad_kcal_mol.
- Output file: `/app/outputs/metrics_summary.json`
- Format: json
- Contract: JSON object with keys: 'method' (string), 'per_property_mad' (array of objects with property (string, AE/IE/EA/PA) and mad_kcal_mol (float)), 'total_mad_kcal_mol' (float). Separate entries for CCSD(T) and B3LYP.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/extrapolated_values_ccsd.csv`
- `/app/outputs/extrapolated_values_b3lyp.csv`
- `/app/outputs/metrics_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### extrapolated_values_ccsd.csv
- path: `/app/outputs/extrapolated_values_ccsd.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-molecule CBS-limit extrapolated energies for CCSD(T). The checker recomputes per-property and total MAD against hidden experimental references.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `molecule`, `property`, `extrapolated_value`, `method`
  - `units`:
    - `extrapolated_value`: kcal/mol for AE, eV for IE/EA/PA

### extrapolated_values_b3lyp.csv
- path: `/app/outputs/extrapolated_values_b3lyp.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Per-molecule KS-limit extrapolated energies for B3LYP. The checker recomputes per-property and total MAD against hidden experimental references.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `molecule`, `property`, `extrapolated_value`, `method`
  - `units`:
    - `extrapolated_value`: kcal/mol for AE, eV for IE/EA/PA

### metrics_summary.json
- path: `/app/outputs/metrics_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent's reported per-property and total MAD. The checker verifies that these values are consistent with the recomputed MAD from the CSV files.
- schema:
  - `type`: object
  - `required`:
    - `method`: string
    - `total_mad_kcal_mol`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `total_mad_kcal_mol`: kcal/mol
    - `per_property_mad[].mad_kcal_mol`: kcal/mol

Notes: The primary scoring is based on the recomputed total MAD from the extrapolated values CSVs. The summary JSON is a consistency check. All experimental references and spin-orbit corrections are public; the agent must obtain them from the cited literature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "extrapolated_values_ccsd.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "molecule",
          "property",
          "extrapolated_value",
          "method"
        ],
        "units": {
          "extrapolated_value": "kcal/mol for AE, eV for IE/EA/PA"
        }
      },
      "description": "Per-molecule CBS-limit extrapolated energies for CCSD(T). The checker recomputes per-property and total MAD against hidden experimental references."
    },
    {
      "file": "extrapolated_values_b3lyp.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "molecule",
          "property",
          "extrapolated_value",
          "method"
        ],
        "units": {
          "extrapolated_value": "kcal/mol for AE, eV for IE/EA/PA"
        }
      },
      "description": "Per-molecule KS-limit extrapolated energies for B3LYP. The checker recomputes per-property and total MAD against hidden experimental references."
    },
    {
      "file": "metrics_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "method": "string",
          "total_mad_kcal_mol": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "total_mad_kcal_mol": "kcal/mol",
          "per_property_mad[].mad_kcal_mol": "kcal/mol"
        }
      },
      "description": "Agent's reported per-property and total MAD. The checker verifies that these values are consistent with the recomputed MAD from the CSV files."
    }
  ],
  "notes": "The primary scoring is based on the recomputed total MAD from the extrapolated values CSVs. The summary JSON is a consistency check. All experimental references and spin-orbit corrections are public; the agent must obtain them from the cited literature."
}
```

## How you are scored
A hidden verifier reads your submitted `extrapolated_values_ccsd.csv`, `extrapolated_values_b3lyp.csv`, and `metrics_summary.json`. It recomputes the per‑property and total MAD from the CSV files against hidden experimental reference values. For each method, your computed total MAD is compared to a hidden gold threshold derived from the paper’s reported best result. If your total MAD meets or beats (≤) the threshold, you earn full credit for that method’s scored artifact; if the MAD is larger, the score decreases according to a pre‑defined schedule. The per‑property MADs and the consistency of the summary JSON are also checked, but the total MAD carries the most weight. The final reward is a weighted combination of the scores from all scored artifacts.
