# Bond-valence analysis of dopant occupancy and threshold concentrations in lithium niobate

## Problem background
Lithium niobate (LiNbO₃) is a multifunctional crystal whose electronic, optical and dielectric properties can be tuned by introducing various dopant cations. A crucial and yet incompletely settled question is where each dopant sits in the crystal lattice: does it replace a Li⁺ ion or a Nb⁵⁺ ion? The bond‑valence model (BVM) provides a quantitative way to assess local bonding strains and the overall structural stability of doped crystals. By computing bond‑valence discrepancies and the Global Instability Index (GII), one can predict dopant occupancies and the threshold concentrations at which a dopant changes its site preference.

## Approach
The method rests on the bond‑valence formula that relates a bond length to its bond valence, with a universal constant B = 0.37. For each dopant ion we compute the sum of bond valences when the ion is placed hypothetically at a Li⁺ site (with known Li–O bond lengths of 2.260 Å and 2.052 Å) and at a Nb⁵⁺ site (Nb–O bond lengths 2.126 Å and 1.878 Å). The absolute difference dᵢ = |Vᵢ – Σ sᵢⱼ| between the ion’s normal valence Vᵢ and the computed bond‑valence sum is a measure of local strain; the ion preferentially occupies the site with the smaller dᵢ. The overall structural instability of the doped crystal is quantified by the GII, which aggregates the squared discrepancies over all atoms, including charge‑compensating Li vacancies (each vacancy is treated as having a discrepancy of 1 v.u.). A critical GII value is calibrated from the known experimental threshold of ZnO (5.3 mol %) using the Li‑vacancy compensation model. For other dopants, the threshold concentration (in mol %) is computed as the doping level at which the GII of the doped LN equals that critical GII, assuming charge compensation by (z–1) Li vacancies per substitution, where z is the nominal valence of the dopant. The required bond‑valence d₀ parameters for each cation‑oxygen pair are obtained from I.D. Brown’s public database.

## Reproduction target
Produce two scored CSV files:

1. A table of bond‑valence discrepancies and predicted site occupancies for 19 dopant ions (Mg²⁺, Zn²⁺, Mn²⁺, Sc³⁺, In³⁺, Pr³⁺, Nd³⁺, Eu³⁺, Ho³⁺, Er³⁺, Yb³⁺, Al³⁺, Cr³⁺, Fe³⁺, Ni³⁺, Ti⁴⁺, Hf⁴⁺, Ta⁵⁺, W⁶⁺). Columns: ion, d_i_Li (v.u.), d_i_Nb (v.u.), occupancy_predicted (one of 'Li', 'Nb', or 'borderline').

2. A table of threshold concentrations for a 13‑ion subset (Mg, Zn, Sc, In, Mn, Al, Cr, Fe, Ni, Ti, Hf, Er, Yb). Columns: ion, threshold_concentration_mol_percent (mol %).

## Assets

- Bond-valence parameters (d0 values) for cation-oxygen pairs from I.D. Brown's database: https://www.iucr.org/__data/assets/file/0012/129046/bondvalparams-2021.cif

## Workflow steps

### Step 1: Retrieve bond-valence parameters
- Role: process
- Action: Fetch the bond-valence parameter CIF file from the IUCr database and extract the d0 characteristic distance for each cation-oxygen pair needed for the dopants (Mg, Zn, Mn, Sc, In, Pr, Nd, Eu, Ho, Er, Yb, Al, Cr, Fe, Ni, Ti, Hf, Ta, W), Li, and Nb.
- Evidence: `/app/outputs/d0_parameters.csv`

### Step 2: Compute bond-valence discrepancy and dopant occupancy
- Role: scored
- Action: Using the bond-valence formula s_ij = exp((d0 - d_ij)/0.37) and the LN bond lengths (Li site: three bonds of 2.260 Å and three of 2.052 Å; Nb site: three bonds of 2.126 Å and three of 1.878 Å), compute d_i_Li and d_i_Nb for each dopant: Mg2+, Zn2+, Mn2+, Sc3+, In3+, Pr3+, Nd3+, Eu3+, Ho3+, Er3+, Yb3+, Al3+, Cr3+, Fe3+, Ni3+, Ti4+, Hf4+, Ta5+, W6+. Compute d_i = |V_i - sum(s_ij)|. Assign occupancy: Li if d_i_Li < d_i_Nb else Nb (borderline if equal). Output CSV with columns ion, d_i_Li, d_i_Nb, occupancy_predicted.
- Output file: `/app/outputs/dopant_di_occupancy.csv`
- Format: csv
- Contract: CSV with columns: ion (string), d_i_Li (float, units v.u.), d_i_Nb (float, units v.u.), occupancy_predicted (string, one of 'Li', 'Nb', 'borderline').
- Scoring: scored by hidden verifier

### Step 3: Calibrate critical GII from ZnO experimental threshold
- Role: process
- Action: Using the d_i for Zn on the Li site from step 1 (d_Zn_Li) and the known experimental threshold concentration of ZnO (5.3 mol %), compute the critical GII value by applying the Li-vacancy model (one Li vacancy per substitution, d_V_Li = 1 v.u.) and the GII formula including oxygen contributions. This yields the reference GII that triggers a site change.
- Evidence: `/app/outputs/critical_gii.txt`

### Step 4: Compute threshold concentrations
- Role: scored (load-bearing)
- Action: For each dopant in {Mg, Zn, Sc, In, Mn, Al, Cr, Fe, Ni, Ti, Hf, Er, Yb}, compute the molar concentration x (mol %) at which the GII of the doped LN equals the critical GII from step 2. Assume charge compensation by (z-1) Li vacancies per substitution (where z is the nominal valence of the dopant). Use the same GII construction (dopant, vacancies, oxygen) to solve for x. Output threshold_table.csv with columns ion and threshold_concentration_mol_percent.
- Output file: `/app/outputs/threshold_table.csv`
- Format: csv
- Contract: CSV with columns: ion (string), threshold_concentration_mol_percent (float, units mol %).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dopant_di_occupancy.csv`
- `/app/outputs/threshold_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dopant_di_occupancy.csv
- path: `/app/outputs/dopant_di_occupancy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Bond-valence discrepancies and predicted site occupancies for 19 dopants. The checker recomputes d_i values from the same public inputs and compares with the agent's values (tolerance 0.001 v.u.), and cross-checks the occupancy assignment.
- schema:
  - `type`: table
  - `required_columns`: `ion`, `d_i_Li`, `d_i_Nb`, `occupancy_predicted`
  - `units`:
    - `d_i_Li`: v.u.
    - `d_i_Nb`: v.u.

### threshold_table.csv
- path: `/app/outputs/threshold_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Threshold concentrations for dopants. The checker recomputes thresholds from the agent's d_i values (from step 1) and the hidden critical GII, then compares with the paper’s reported values (absolute tolerance 0.05 mol %).
- schema:
  - `type`: table
  - `required_columns`: `ion`, `threshold_concentration_mol_percent`
  - `units`:
    - `threshold_concentration_mol_percent`: mol %

Notes: The LN bond lengths (Li: 2.260 Å and 2.052 Å; Nb: 2.126 Å and 1.878 Å) and the B=0.37 constant are fixed. The bond-valence parameter database provides d0 values. The ZnO experimental threshold (5.3 mol %) is used for calibration.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dopant_di_occupancy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "ion",
          "d_i_Li",
          "d_i_Nb",
          "occupancy_predicted"
        ],
        "units": {
          "d_i_Li": "v.u.",
          "d_i_Nb": "v.u."
        }
      },
      "description": "Bond-valence discrepancies and predicted site occupancies for 19 dopants. The checker recomputes d_i values from the same public inputs and compares with the agent's values (tolerance 0.001 v.u.), and cross-checks the occupancy assignment."
    },
    {
      "file": "threshold_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ion",
          "threshold_concentration_mol_percent"
        ],
        "units": {
          "threshold_concentration_mol_percent": "mol %"
        }
      },
      "description": "Threshold concentrations for dopants. The checker recomputes thresholds from the agent's d_i values (from step 1) and the hidden critical GII, then compares with the paper’s reported values (absolute tolerance 0.05 mol %)."
    }
  ],
  "notes": "The LN bond lengths (Li: 2.260 Å and 2.052 Å; Nb: 2.126 Å and 1.878 Å) and the B=0.37 constant are fixed. The bond-valence parameter database provides d0 values. The ZnO experimental threshold (5.3 mol %) is used for calibration."
}
```

## How you are scored
An automated verifier reads your CSV files and scores them against hidden reference values. For the occupancy file it recomputes dᵢ values from the same public bond‑valence parameters and LN bond lengths, and cross‑checks your occupancy assignments. For the threshold file it recomputes threshold concentrations from your dᵢ values (taken from your occupancy file) and compares them to the expected thresholds. The final reward is a weighted combination of the scores on these two artifacts.
