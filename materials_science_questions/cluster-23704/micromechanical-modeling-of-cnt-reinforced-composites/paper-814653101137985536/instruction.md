# Interphase Parameter Estimation in CNT-Reinforced Polymer Nanocomposites

## Problem background
Conventional micromechanics models for short-fiber composites often underpredict the tensile strength of polymer/CNT nanocomposites. A leading hypothesis is that a distinct interphase layer forms between the polymer matrix and the CNT, whose properties differ from both bulk constituents and contribute significantly to the load transfer. Extending the Kelly–Tyson theory to account for this interphase provides a quantitative way to estimate the interphase thickness (t), the interfacial shear strength (τ), the interphase strength (σ_i), and the critical CNT length (L_c) from experimental tensile strength measurements. The present task requires implementing such a model and using it to derive these interfacial parameters for a series of polymer/CNT systems from published data.

## Approach
The modeling approach combines two micromechanics frameworks. First, the Kelly–Tyson equation for short-fiber reinforced composites is modified by introducing an interphase layer of thickness t and, assuming that CNTs are shorter than the critical length, yields a formula for the composite tensile strength σ_c in terms of the volume fraction φ_f, CNT aspect ratio α = L/d, matrix strength σ_m, orientation factor η_o = 1/5 (random 3D orientation), and the interfacial shear strength τ. Second, the Pukanszky model relates a filler–matrix interaction parameter B to the relative tensile strength σ_c/σ_m and φ_f, and B itself can be expressed in terms of α, η_o, τ, and σ_m under the dilute limit. By equating the two expressions, one obtains a direct relation between B, t, and the experimental data, which allows determining t by fitting the model to the measured σ_c vs φ_f curves. Once t and B are known, τ follows from B, σ_m, α, and η_o; the interphase strength σ_i can be deduced from B, the matrix strength, and the geometry of the interphase; and the critical length L_c (the minimum CNT length needed to transfer enough shear stress to break the CNT) is obtained from the CNT strength (σ_f = 37 GPa), τ, and geometrical factors. The entire pipeline is applied to five different polymer/CNT nanocomposite samples, each characterized by its own d, L, σ_m, and experimental σ_c(φ_f) data.

## Reproduction target
Using the experimental tensile strength data from the five literature sources listed in the Assets section, and the corresponding CNT diameter, length, and matrix strength provided in those sources, carry out the following for each sample:
1. Compute the Pukanszky B parameter from the strength data and φ_f via the relation derived from the Pukanszky model.
2. Fit the interphase thickness t by minimizing the deviation between the tensile strength predicted by the interphase-extended Kelly–Tyson equation (which depends on B) and the experimental data.
3. Calculate the interfacial shear strength τ (in MPa), the interphase strength σ_i (in MPa), and the critical CNT length L_c (in µm) using the equations that link these quantities to B, t, the matrix strength, and the CNT geometry.
Assemble the results for all five samples in the order they appear in the data into a CSV file with the exact columns: sample_no, t_nm, B, tau_MPa, sigma_i_MPa, Lc_um.

## Assets

- Prashantha et al., 2009 – PP/MWCNT tensile data: 10.1016/j.compscitech.2009.04.007
- Safadi et al., 2002 – PS/MWCNT tensile data: 10.1002/app.10480
- Jeong & Kessler, 2008 – PDCPD/f-MWCNT tensile data: 10.1021/cm800441n
- Rong et al., 2010 – PEEK/f-MWCNT tensile data: 10.1016/j.compscitech.2009.07.015
- Montazeri et al., 2010 – Epoxy/f-MWCNT tensile data: 10.1016/j.matdes.2010.04.018

## Workflow steps

### Step 1: Collect experimental tensile strength data and input parameters
- Role: process
- Action: Obtain the five cited papers and extract for each of the five samples: CNT diameter d, CNT length L, matrix tensile strength σ_m, and the experimental composite tensile strength σ_c as a function of CNT volume fraction φ_f. Save the extracted data in a machine‑readable file (e.g., JSON) for use by subsequent steps.
- Evidence: `/app/outputs/extracted_data.json`

### Step 2: Compute Pukanszky B parameter and fit interphase thickness t
- Role: process
- Action: Using the extracted experimental data, for each sample compute the Pukanszky B parameter using the formula B = ln(σ_c/σ_m * (1+2.5 φ_f)/(1-φ_f)) / φ_f. Then fit the interphase thickness t by numerically minimizing the squared error between the experimental σ_c values and the model prediction σ_c = σ_m * [ (B-2.04)*(1+2t/d)*φ_f + 1 - (1+2t/d)^2*φ_f ], where d is CNT diameter. Save the resulting t (nm) and B values together with optimization logs.
- Evidence: `/app/outputs/fitting_results.json`

### Step 3: Calculate interfacial shear strength, interphase strength, and critical length
- Role: scored (load-bearing)
- Action: From the fitted t and B, calculate interfacial shear strength τ = σ_m (B - 2.04) / (η_o α), where α = L/d, interphase strength σ_i = σ_m * exp( B / (1 + 2t/d) ), and critical length L_c = (η_o σ_f L) / (2 σ_m (B - 2.04)), with CNT strength σ_f = 37 GPa and orientation factor η_o = 1/5. Ensure units: t in nm, σ_m and τ in MPa, σ_i in MPa, L_c in µm. Compile the results for all five samples (sample_no, t_nm, B, tau_MPa, sigma_i_MPa, Lc_um) into a single CSV file.
- Output file: `/app/outputs/computed_table.csv`
- Format: csv
- Contract: CSV with header: sample_no, t_nm, B, tau_MPa, sigma_i_MPa, Lc_um. One data row per sample (1–5), all values numeric.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_table.csv
- path: `/app/outputs/computed_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of computed interphase thickness, Pukanszky B parameter, interfacial shear strength, interphase strength, and critical CNT length for five polymer/CNT nanocomposite samples. Values are compared against hidden reference results with appropriate per-parameter tolerances.
- schema:
  - `type`: table
  - `required_columns`: `sample_no`, `t_nm`, `B`, `tau_MPa`, `sigma_i_MPa`, `Lc_um`
  - `units`:
    - `t_nm`: nm
    - `tau_MPa`: MPa
    - `sigma_i_MPa`: MPa
    - `Lc_um`: µm

Notes: The scored file must contain exactly five rows corresponding to the five samples (PP/MWCNT, PS/MWCNT, PDCPD/f-MWCNT, PEEK/f-MWCNT, Epoxy/f-MWCNT) in the order given by the extracted experimental data. All columns are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample_no",
          "t_nm",
          "B",
          "tau_MPa",
          "sigma_i_MPa",
          "Lc_um"
        ],
        "units": {
          "t_nm": "nm",
          "tau_MPa": "MPa",
          "sigma_i_MPa": "MPa",
          "Lc_um": "µm"
        }
      },
      "description": "Table of computed interphase thickness, Pukanszky B parameter, interfacial shear strength, interphase strength, and critical CNT length for five polymer/CNT nanocomposite samples. Values are compared against hidden reference results with appropriate per-parameter tolerances."
    }
  ],
  "notes": "The scored file must contain exactly five rows corresponding to the five samples (PP/MWCNT, PS/MWCNT, PDCPD/f-MWCNT, PEEK/f-MWCNT, Epoxy/f-MWCNT) in the order given by the extracted experimental data. All columns are required."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that reads the file `computed_table.csv`. For each sample, the verifier compares your reported values of t_nm, B, tau_MPa, sigma_i_MPa, and Lc_um against independently obtained reference values using parameter-specific tolerances. The tolerance ranges are chosen to account for numerical differences arising from the fitting procedure and implementation details. Each individual value that falls within its tolerance earns partial credit; the final score is the fraction of all values (6 per sample × 5 samples = 30 total) that meet the tolerance. The exact reference numbers and tolerances are not provided. The verifier then writes a normalized reward between 0 and 1 to `/logs/verifier/reward.txt`. You are not required to reproduce exact numbers from any publication, but the values should result from correctly implementing the described methodology.
