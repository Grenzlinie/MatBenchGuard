# Effective Field Theory Magnetization and Hysteresis of Two-Layer Ising Nanographene

## Problem background
This investigation studies the magnetic properties of a two-layer spin-1/2 Ising nanographene system within the effective field theory (EFT) framework. The nanographene structure comprises central and edge graphene atoms arranged in two layers. The magnetic interactions are described by four exchange coupling constants: Jc between nearest-neighbor central atoms, Jint between central and edge atoms, Je between nearest-neighbor edge atoms, and J1 (interlayer coupling) between corresponding atoms on the two layers. Applying the EFT differential operator technique leads to a set of four coupled self-consistent equations for the sublattice magnetizations mc1, mc2, me1, me2, involving the function F(x)=tanh(β(x+H)). By solving these equations numerically over a range of temperatures and external magnetic fields H, one obtains the magnetization behavior and can locate the ferromagnetic–paramagnetic transition temperature Tc as well as hysteresis loops. The objective is to implement this EFT solver and characterize the magnetic response for two distinct exchange parameter sets.

## Approach
The effective field theory (EFT) with the differential operator technique is used to derive the coupled magnetization equations. Each sublattice magnetization is expressed as a product of hyperbolic cosine and sine operators acting on the function F(x)=tanh(β(x+H)), evaluated at x=0, with the coordination numbers determined by the graphene lattice. The agent must implement a numerical solver to self-consistently determine the four magnetizations at each (T,H) point. The approach proceeds as follows: (1) define the two exchange parameter sets (FM and AFM), (2) solve the equations at zero field across a temperature range to obtain magnetization vs. temperature curves for both parameter sets, (3) solve the equations at fixed temperatures T=1,2,3 while sweeping the external field H to obtain hysteresis loops for both parameter sets, (4) from the raw curves, extract physical quantities such as the critical temperature Tc (where total magnetization vanishes), zero-temperature magnetizations, coercive fields (field values where total magnetization crosses zero), and remanence ordering, (5) for the antiferromagnetic case at T=1, compute a fine-field hysteresis curve for the central sublattice alone to resolve any subtle transitions and determine whether a peak effect region (a local maximum in |dM/dH| between two coercive fields) is present.

## Reproduction target
The task is to produce raw numerical data from the EFT solver and to extract key physical quantities that characterize the magnetic phase transitions and hysteresis behavior. Specifically, for the ferromagnetic parameter set (Jc=Jint=Je=J1=1), the target includes: (i) a CSV of magnetization vs. temperature (T, mc1, mc2, me1, me2, MT), (ii) a CSV of hysteresis curves (T=1,2,3; H, all magnetizations), (iii) a JSON file with the extracted critical temperature Tc, zero-temperature sublattice magnetizations, coercive fields at T=1,2,3, and a boolean indicating whether the remanent magnetization of central atoms exceeds that of edge atoms. For the antiferromagnetic parameter set (Jc=Je=J1=1, Jint=-1), the target includes: (i) analogous magnetization vs. temperature CSV, (ii) a hysteresis CSV for all sublattices at T=1,2,3, (iii) a fine-grid hysteresis CSV for the central sublattice at T=1 (H, mc1, mc2), (iv) a JSON file with Tc, zero-temperature magnetizations, the coercive fields of the total hysteresis at T=1 (Hc1, Hc2, Hc3), the coercive fields of the central sublattice at T=1, and a boolean indicating whether a peak effect region (local maximum in |dM/dH| between Hc2 and Hc3) is present. All extracted values must be consistent with the submitted raw CSV data.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define exchange parameter sets
- Role: process
- Action: Define the ferromagnetic (FM) parameter set: Jc=Jint=Je=J1=1, and the antiferromagnetic (AFM) set: Jc=Je=J1=1, Jint=-1. (Units: J=1 energy unit, kB=1).
- Evidence: `/app/outputs/parameters.json`

### Step 2: Compute ferromagnetic magnetization vs temperature
- Role: scored (load-bearing)
- Action: Solve the self-consistent EFT magnetization equations for the ferromagnetic parameter set (all J=1) with zero external field over a temperature range from T=0 to at least 3.0. Use root-finding to determine the four sublattice magnetizations and total magnetization at each temperature. Write the curve as a CSV.
- Output file: `/app/outputs/fm_magnetization_vs_T.csv`
- Format: csv
- Contract: Header: T,mc1,mc2,me1,me2,MT. Columns: T (temperature in J/k_B), mc1, mc2, me1, me2, MT (total magnetization).
- Scoring: scored by hidden verifier

### Step 3: Compute antiferromagnetic magnetization vs temperature
- Role: scored (load-bearing)
- Action: Solve the EFT magnetization equations for the antiferromagnetic parameter set (Jc=Je=J1=1, Jint=-1) with zero external field over a temperature range from T=0 to at least 3.0. Root-find the sublattice magnetizations and total magnetization at each temperature. Write the curve as a CSV.
- Output file: `/app/outputs/afm_magnetization_vs_T.csv`
- Format: csv
- Contract: Header: T,mc1,mc2,me1,me2,MT. Columns: T (temperature in J/k_B), mc1, mc2, me1, me2, MT.
- Scoring: scored by hidden verifier

### Step 4: Compute ferromagnetic hysteresis loops
- Role: scored (load-bearing)
- Action: For the FM parameter set, solve the EFT equations with an external magnetic field H at temperatures T=1, 2, 3. Sweep H over a range that fully saturates the magnetizations (e.g., from -2 to 2). At each field value, record the sublattice magnetizations and total magnetization. Write all data to a CSV.
- Output file: `/app/outputs/fm_hysteresis_curves.csv`
- Format: csv
- Contract: Header: T,H,mc1,mc2,me1,me2,MT. Columns: T (∈ {1,2,3}), H (external field in units of J), mc1, mc2, me1, me2, MT.
- Scoring: scored by hidden verifier

### Step 5: Compute antiferromagnetic hysteresis loops (all sublattices)
- Role: scored (load-bearing)
- Action: For the AFM parameter set, solve the EFT equations with external field H at temperatures T=1, 2, 3, sweeping H over a suitable range. Record all sublattice magnetizations and total magnetization at each field point. Write to a CSV.
- Output file: `/app/outputs/afm_hysteresis_curves.csv`
- Format: csv
- Contract: Header: T,H,mc1,mc2,me1,me2,MT. Columns: T (∈ {1,2,3}), H (external field in J), mc1, mc2, me1, me2, MT.
- Scoring: scored by hidden verifier

### Step 6: Compute AFM central sublattice hysteresis at T=1 (fine grid)
- Role: scored (load-bearing)
- Action: For the AFM parameter set at T=1, solve the EFT equations while sweeping H with a fine grid (e.g., step ≤ 0.005) to resolve the triple hysteresis loop and peak effect region in the central sublattice. Write only H, mc1, mc2 to a CSV.
- Output file: `/app/outputs/afm_hysteresis_central_T1.csv`
- Format: csv
- Contract: Header: H,mc1,mc2. Columns: H (external field in J), mc1, mc2.
- Scoring: scored by hidden verifier

### Step 7: Extract ferromagnetic key values
- Role: scored
- Action: From the FM magnetization and hysteresis data, extract the critical temperature Tc, zero-temperature sublattice magnetizations, coercive fields at T=1,2,3, and whether remanent magnetization of central atoms exceeds that of edge atoms. Write these findings to a JSON file.
- Output file: `/app/outputs/fm_extracted_values.json`
- Format: json
- Contract: JSON object with keys: 'Tc' (float), 'zeroT_magnetizations' (object with mc1,mc2,me1,me2,MT as floats), 'coercive_fields_T1' (float), 'coercive_fields_T2' (float), 'coercive_fields_T3' (float), 'remanence_central_greater_than_edge' (bool).
- Scoring: scored by hidden verifier

### Step 8: Extract antiferromagnetic key values
- Role: scored
- Action: From the AFM magnetization and hysteresis data, extract Tc, zero-temperature magnetizations, coercive fields of total hysteresis at T=1 (Hc1, Hc2, Hc3), coercive fields of central sublattice at T=1, and whether a peak effect region (local maximum in |dM/dH| between Hc2 and Hc3) is present. Write to JSON.
- Output file: `/app/outputs/afm_extracted_values.json`
- Format: json
- Contract: JSON object with keys: 'Tc' (float), 'zeroT_magnetizations' (object with mc1,mc2,me1,me2,MT as floats), 'coercive_fields_total_T1' (object with Hc1,Hc2,Hc3 as floats), 'coercive_fields_central_T1' (object with Hc1,Hc2,Hc3 as floats), 'peak_effect_present_T1' (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fm_magnetization_vs_T.csv`
- `/app/outputs/afm_magnetization_vs_T.csv`
- `/app/outputs/fm_hysteresis_curves.csv`
- `/app/outputs/afm_hysteresis_curves.csv`
- `/app/outputs/afm_hysteresis_central_T1.csv`
- `/app/outputs/fm_extracted_values.json`
- `/app/outputs/afm_extracted_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fm_magnetization_vs_T.csv
- path: `/app/outputs/fm_magnetization_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature scan of magnetizations for FM case; used to derive Tc and zero-T values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `mc1`, `mc2`, `me1`, `me2`, `MT`
  - `units`:
    - `T`: J/k_B
    - `mc1`: spin (dimensionless)
    - `mc2`: spin (dimensionless)
    - `me1`: spin (dimensionless)
    - `me2`: spin (dimensionless)
    - `MT`: spin (dimensionless)

### afm_magnetization_vs_T.csv
- path: `/app/outputs/afm_magnetization_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature scan of magnetizations for AFM case; used to derive Tc and zero-T values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `mc1`, `mc2`, `me1`, `me2`, `MT`
  - `units`:
    - `T`: J/k_B
    - `mc1`: spin (dimensionless)
    - `mc2`: spin (dimensionless)
    - `me1`: spin (dimensionless)
    - `me2`: spin (dimensionless)
    - `MT`: spin (dimensionless)

### fm_hysteresis_curves.csv
- path: `/app/outputs/fm_hysteresis_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Hysteresis loops at T=1,2,3 for FM case; used to extract coercive fields and remanence ordering.
- schema:
  - `type`: table
  - `required_columns`: `T`, `H`, `mc1`, `mc2`, `me1`, `me2`, `MT`
  - `units`:
    - `T`: J/k_B
    - `H`: J
    - `mc1`: spin (dimensionless)
    - `mc2`: spin (dimensionless)
    - `me1`: spin (dimensionless)
    - `me2`: spin (dimensionless)
    - `MT`: spin (dimensionless)

### afm_hysteresis_curves.csv
- path: `/app/outputs/afm_hysteresis_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Hysteresis loops at T=1,2,3 for AFM case (all sublattices); used to extract coercive fields and identify triple hysteresis.
- schema:
  - `type`: table
  - `required_columns`: `T`, `H`, `mc1`, `mc2`, `me1`, `me2`, `MT`
  - `units`:
    - `T`: J/k_B
    - `H`: J
    - `mc1`: spin (dimensionless)
    - `mc2`: spin (dimensionless)
    - `me1`: spin (dimensionless)
    - `me2`: spin (dimensionless)
    - `MT`: spin (dimensionless)

### afm_hysteresis_central_T1.csv
- path: `/app/outputs/afm_hysteresis_central_T1.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Fine-grid hysteresis of central sublattice at T=1 for AFM; used to locate coercive fields and check peak effect region.
- schema:
  - `type`: table
  - `required_columns`: `H`, `mc1`, `mc2`
  - `units`:
    - `H`: J
    - `mc1`: spin (dimensionless)
    - `mc2`: spin (dimensionless)

### fm_extracted_values.json
- path: `/app/outputs/fm_extracted_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted scalar quantities for FM case; the checker compares these to hidden reference values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Tc`: float
    - `zeroT_magnetizations`: object with mc1,mc2,me1,me2,MT as floats
    - `coercive_fields_T1`: float
    - `coercive_fields_T2`: float
    - `coercive_fields_T3`: float
    - `remanence_central_greater_than_edge`: bool

### afm_extracted_values.json
- path: `/app/outputs/afm_extracted_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted scalar quantities for AFM case; the checker compares these to hidden reference values with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Tc`: float
    - `zeroT_magnetizations`: object with mc1,mc2,me1,me2,MT as floats
    - `coercive_fields_total_T1`: object with Hc1,Hc2,Hc3 as floats
    - `coercive_fields_central_T1`: object with Hc1,Hc2,Hc3 as floats
    - `peak_effect_present_T1`: bool

Notes: All numerical values are in units where J is the energy unit and kB=1. The checker recomputes the EFT-derived properties from the raw CSV files to validate consistency and then compares extracted JSON values against paper-reported numbers within tolerances. The agent must implement the self-consistent solver; no pre-trained model or external data required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fm_magnetization_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "mc1",
          "mc2",
          "me1",
          "me2",
          "MT"
        ],
        "units": {
          "T": "J/k_B",
          "mc1": "spin (dimensionless)",
          "mc2": "spin (dimensionless)",
          "me1": "spin (dimensionless)",
          "me2": "spin (dimensionless)",
          "MT": "spin (dimensionless)"
        }
      },
      "description": "Temperature scan of magnetizations for FM case; used to derive Tc and zero-T values."
    },
    {
      "file": "afm_magnetization_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "mc1",
          "mc2",
          "me1",
          "me2",
          "MT"
        ],
        "units": {
          "T": "J/k_B",
          "mc1": "spin (dimensionless)",
          "mc2": "spin (dimensionless)",
          "me1": "spin (dimensionless)",
          "me2": "spin (dimensionless)",
          "MT": "spin (dimensionless)"
        }
      },
      "description": "Temperature scan of magnetizations for AFM case; used to derive Tc and zero-T values."
    },
    {
      "file": "fm_hysteresis_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "H",
          "mc1",
          "mc2",
          "me1",
          "me2",
          "MT"
        ],
        "units": {
          "T": "J/k_B",
          "H": "J",
          "mc1": "spin (dimensionless)",
          "mc2": "spin (dimensionless)",
          "me1": "spin (dimensionless)",
          "me2": "spin (dimensionless)",
          "MT": "spin (dimensionless)"
        }
      },
      "description": "Hysteresis loops at T=1,2,3 for FM case; used to extract coercive fields and remanence ordering."
    },
    {
      "file": "afm_hysteresis_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "H",
          "mc1",
          "mc2",
          "me1",
          "me2",
          "MT"
        ],
        "units": {
          "T": "J/k_B",
          "H": "J",
          "mc1": "spin (dimensionless)",
          "mc2": "spin (dimensionless)",
          "me1": "spin (dimensionless)",
          "me2": "spin (dimensionless)",
          "MT": "spin (dimensionless)"
        }
      },
      "description": "Hysteresis loops at T=1,2,3 for AFM case (all sublattices); used to extract coercive fields and identify triple hysteresis."
    },
    {
      "file": "afm_hysteresis_central_T1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "H",
          "mc1",
          "mc2"
        ],
        "units": {
          "H": "J",
          "mc1": "spin (dimensionless)",
          "mc2": "spin (dimensionless)"
        }
      },
      "description": "Fine-grid hysteresis of central sublattice at T=1 for AFM; used to locate coercive fields and check peak effect region."
    },
    {
      "file": "fm_extracted_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc": "float",
          "zeroT_magnetizations": "object with mc1,mc2,me1,me2,MT as floats",
          "coercive_fields_T1": "float",
          "coercive_fields_T2": "float",
          "coercive_fields_T3": "float",
          "remanence_central_greater_than_edge": "bool"
        }
      },
      "description": "Extracted scalar quantities for FM case; the checker compares these to hidden reference values with tolerance."
    },
    {
      "file": "afm_extracted_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Tc": "float",
          "zeroT_magnetizations": "object with mc1,mc2,me1,me2,MT as floats",
          "coercive_fields_total_T1": "object with Hc1,Hc2,Hc3 as floats",
          "coercive_fields_central_T1": "object with Hc1,Hc2,Hc3 as floats",
          "peak_effect_present_T1": "bool"
        }
      },
      "description": "Extracted scalar quantities for AFM case; the checker compares these to hidden reference values with tolerance."
    }
  ],
  "notes": "All numerical values are in units where J is the energy unit and kB=1. The checker recomputes the EFT-derived properties from the raw CSV files to validate consistency and then compares extracted JSON values against paper-reported numbers within tolerances. The agent must implement the self-consistent solver; no pre-trained model or external data required."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. For the raw CSV files, the verifier may recompute the magnetization curves using an independent EFT implementation and verify that the submitted data conform to expected physical behavior. For the extracted JSON files, consistency with the raw CSV data is checked, and key quantities (Tc, zero-temperature magnetizations, coercive fields) are compared against hidden reference values derived from the paper's original results within appropriate tolerances. Structural checks (e.g., whether the remanence ordering holds, whether a peak effect region appears in the central sublattice at T=1) are also performed. Each scored step contributes a weighted fraction to the final reward, which is a float between 0 and 1. Simply reporting the paper's numbers without physically plausible raw curves will not yield full credit.
