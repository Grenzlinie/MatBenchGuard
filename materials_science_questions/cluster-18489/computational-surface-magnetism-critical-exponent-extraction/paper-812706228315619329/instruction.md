# Magnetization properties of ABO3 perovskite nanoparticle via Effective Field Theory

## Problem background
The ABO3 perovskite-type nanoparticle is a three-sublattice magnetic system (A atoms on the edges, B atom at the centre, and O atoms on the surfaces) that can exhibit ferromagnetic, edge-antiferromagnetic, and surface-antiferromagnetic order depending on the signs of the nearest-neighbour exchange interactions. Computing the temperature and field dependence of the sublattice and total magnetisations reveals how edge and surface antiferromagnetism modify the collective magnetic behaviour, potentially leading to lowered critical temperatures, compensation, and complex hysteresis. This task requires implementing the Effective Field Theory (EFT) and solving the self-consistent magnetisation equations to obtain the M–T and M–H curves, then extracting the critical temperatures, compensation temperature, and coercive fields as quantitative measures of the magnetic response.

## Approach
The ABO3 perovskite nanoparticle is modelled as a spin-1/2 Ising system on a fixed lattice with three sublattices (A, B, O) and five nearest-neighbour exchange interactions: j_AA, j_AO, j_AB, j_OO, j_OB. The magnetisations m_A, m_B, m_O are obtained from the self-consistent EFT equations that follow from the Kaneyoshi differential-operator technique. These equations involve hyperbolic functions and the spin-1/2 function F_1/2(x) = ½ tanh[β(x+h)/2] (β = 1/T in reduced units, h is the external field). The total magnetisation is M_total = (8 m_A + m_B + 6 m_O)/15. Three exchange-coupling regimes are studied: ferromagnetic (FM, all j=+1), edge antiferromagnetic (EAFM, j_AA=−1, others +1), and surface antiferromagnetic (SAFM, j_AO=−1, others +1). The equations must be solved numerically (e.g. iterative root-finding) over a grid of reduced temperatures (0 ≤ T ≤ 4) at zero field to produce M–T curves, and over a complete field loop (e.g. −5 ≤ H ≤ 5) at fixed temperatures T=1,2,3,4 to produce hysteresis M–H curves. From these raw data the critical temperature Tc, the compensation temperature T_comp (if a second zero crossing appears), and the coercive field(s) Hc are derived.

## Reproduction target
Produce magnetisation-vs-temperature (M–T) curves at zero external field and magnetisation-vs-applied-field (M–H) hysteresis loops for the ABO3 perovskite nanoparticle in the three exchange regimes: FM (all j=+1), EAFM (j_AA=−1, others +1), and SAFM (j_AO=−1, others +1). From the M–T curves, extract the critical temperature Tc for each regime and, for the SAFM case, the compensation temperature T_comp if a second zero crossing exists. From the M–H curves at T=1,2,3,4 for each regime, extract the coercive field Hc (or all distinct coercive fields when multiple sign crossings are present). Output the raw data (mt_data.csv, mh_data.csv) and a summary (summary.json) containing these extracted quantities.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute magnetization vs temperature (M-T curves)
- Role: scored (load-bearing)
- Action: Implement the three-sublattice EFT self-consistency equations for the ABO3 perovskite nanoparticle. Solve them for three exchange-coupling regimes (ferromagnetic FM, edge antiferromagnetic EAFM, surface antiferromagnetic SAFM) at zero external field (H=0) over a reduced temperature grid from 0 to approximately 4, and record the sublattice magnetizations m_A, m_B, m_O and total magnetization M_total for each temperature and case.
- Output file: `/app/outputs/mt_data.csv`
- Format: csv
- Contract: CSV with columns: T (float), case (string: FM, EAFM, SAFM), m_A (float), m_B (float), m_O (float), M_total (float). At least 500 rows per case spanning T from 0 to 4.
- Scoring: scored by hidden verifier

### Step 2: Compute magnetization vs applied field (M-H hysteresis loops)
- Role: scored (load-bearing)
- Action: Solve the EFT equations for the three regimes at fixed temperatures T=1,2,3,4 while sweeping the reduced external field H over a complete hysteresis loop (e.g., from +5 to -5 and back). Record sublattice and total magnetizations at each field point.
- Output file: `/app/outputs/mh_data.csv`
- Format: csv
- Contract: CSV with columns: T (float), case (string: FM, EAFM, SAFM), H (float), m_A (float), m_B (float), m_O (float), M_total (float). H covers a full loop; at least 2000 points per (T, case).
- Scoring: scored by hidden verifier

### Step 3: Extract critical temperatures, compensation temperature, and coercive fields
- Role: scored
- Action: From the computed magnetization curves, extract and report the following derived quantities: critical temperature Tc for each regime, compensation temperature T_comp for the SAFM regime (if a second zero crossing exists), and coercive fields Hc for each temperature and regime (fields where M_total=0 in the hysteresis loops, recording all distinct coercive points). Write the extracted values to summary.json.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: JSON object with keys: Tc_FM (number), Tc_EAFM (number), Tc_SAFM (number), T_comp_SAFM (number or null), Hc_values (array of objects each with T: number, case: string, Hc: number or array of numbers for multiple coercive fields).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mt_data.csv`
- `/app/outputs/mh_data.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mt_data.csv
- path: `/app/outputs/mt_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: M‑T data for FM, EAFM, SAFM regimes. The checker will extract Tc and T_comp from the M_total column.
- schema:
  - `type`: table
  - `required_columns`: `T`, `case`, `m_A`, `m_B`, `m_O`, `M_total`
  - `units`:
    - `T`: reduced temperature
    - `m_A`: magnetisation
    - `m_B`: magnetisation
    - `m_O`: magnetisation
    - `M_total`: total magnetisation

### mh_data.csv
- path: `/app/outputs/mh_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Hysteresis M‑H data for FM, EAFM, SAFM regimes at T=1,2,3,4. The checker will extract coercive fields from the M_total column.
- schema:
  - `type`: table
  - `required_columns`: `T`, `case`, `H`, `m_A`, `m_B`, `m_O`, `M_total`
  - `units`:
    - `T`: reduced temperature
    - `H`: reduced external field
    - `m_A`: magnetisation
    - `m_B`: magnetisation
    - `m_O`: magnetisation
    - `M_total`: total magnetisation

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent's extracted quantities. Cross‑checked for consistency with the recomputed values from mt_data.csv and mh_data.csv.
- schema:
  - `type`: object
  - `required`:
    - `Tc_FM`: number
    - `Tc_EAFM`: number
    - `Tc_SAFM`: number
    - `T_comp_SAFM`: number|null
    - `Hc_values`: array of objects each with T: number, case: string, Hc: number or array of numbers

Notes: All scored artifacts must be written under /app/outputs. The checker recomputes critical quantities from the raw CSV files, not from the summary.json directly; the summary.json is validated against those recomputed values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mt_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "case",
          "m_A",
          "m_B",
          "m_O",
          "M_total"
        ],
        "units": {
          "T": "reduced temperature",
          "m_A": "magnetisation",
          "m_B": "magnetisation",
          "m_O": "magnetisation",
          "M_total": "total magnetisation"
        }
      },
      "description": "M‑T data for FM, EAFM, SAFM regimes. The checker will extract Tc and T_comp from the M_total column."
    },
    {
      "file": "mh_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "case",
          "H",
          "m_A",
          "m_B",
          "m_O",
          "M_total"
        ],
        "units": {
          "T": "reduced temperature",
          "H": "reduced external field",
          "m_A": "magnetisation",
          "m_B": "magnetisation",
          "m_O": "magnetisation",
          "M_total": "total magnetisation"
        }
      },
      "description": "Hysteresis M‑H data for FM, EAFM, SAFM regimes at T=1,2,3,4. The checker will extract coercive fields from the M_total column."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Tc_FM": "number",
          "Tc_EAFM": "number",
          "Tc_SAFM": "number",
          "T_comp_SAFM": "number|null",
          "Hc_values": "array of objects each with T: number, case: string, Hc: number or array of numbers"
        }
      },
      "description": "Agent's extracted quantities. Cross‑checked for consistency with the recomputed values from mt_data.csv and mh_data.csv."
    }
  ],
  "notes": "All scored artifacts must be written under /app/outputs. The checker recomputes critical quantities from the raw CSV files, not from the summary.json directly; the summary.json is validated against those recomputed values."
}
```

## How you are scored
A hidden verifier will read your submitted mt_data.csv and mh_data.csv. It will independently recompute Tc and T_comp from the M_total column in mt_data.csv, and coercive fields from the full hysteresis loop in mh_data.csv. These recomputed values are compared against hidden reference quantities (derived from the paper’s reported results) with appropriate tolerances. The verifier also cross-checks your summary.json against the recomputed values to ensure consistency. The scoring is monotonic: for directional metrics, meeting or exceeding the reference earns full credit, and the reward decreases only as the result gets worse. The final score is a weighted combination across all quantities; simply reporting numbers without producing the raw curves will not pass.
