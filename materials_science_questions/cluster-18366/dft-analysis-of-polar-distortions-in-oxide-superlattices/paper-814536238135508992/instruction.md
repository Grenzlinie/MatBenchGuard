# Three-band optical-phonon superconductivity model for n-type SrTiO₃

## Problem background
Superconductivity in n-type SrTiO₃ (strontium titanate) appears at carrier densities as low as 5.5 × 10¹⁷ cm⁻³, where the Fermi energy is only ~1 meV — far smaller than the frequencies of longitudinal optical (LO) phonons. In this strongly nonadiabatic regime the usual BCS phonon pairing picture must be re‑examined. A proposed mechanism involves electron pairing mediated by LO polar phonons. The conduction band of SrTiO₃ is split into three subbands that fill successively with increasing doping. A theoretical model built on this mechanism predicts that the superconducting transition temperature T_C should depend on carrier concentration n_s in a non‑monotonic way, potentially exhibiting distinct features tied to the filling of each subband. The goal of this task is to implement that model and compute how T_C varies with doping.

## Approach
The model treats each of the three conduction bands as parabolic with effective masses m₁ = 1.8 mₑ, m₂ = 3.5 mₑ, m₃ = 6 mₑ. Electrons are added to the system, increasing the total carrier concentration n_s; the chemical potential moves up and bands fill sequentially. The critical concentrations for the onset of the second and third bands are n_c₁ = 1.2 × 10¹⁸ cm⁻³ and n_c₂ = 2.5 × 10¹⁹ cm⁻³.

The pairing interaction between electrons is described by a screened LO‑phonon‑mediated vertex. In the nonadiabatic limit (phonon frequency ≫ E_F) the vertex simplifies, and after incorporating screening by both the high‑frequency dielectric constant and the mobile carriers (in the Thomas–Fermi approximation), each band i acquires a dimensionless coupling constant λ_i that depends on the Fermi momenta of all occupied bands. The transition temperature for band i is given by a BCS‑like expression
    T_C,i = const × E_F,i × exp(−1 / λ_i) ,
up to a numerical factor of order unity. The prefactor “const” and the effective optical Bohr radius a_B (which enters through the screening) are not known a priori; they must be determined by a calibration step.

Calibration: the model’s first‑band T_C has a maximum at a characteristic value of the dimensionless parameter x = π p_F a_B / ħ. By requiring that this maximum matches the experimental value of T_C ≈ 0.2 K observed at n_s ≈ 2 × 10¹⁸ cm⁻³, one can solve for a_B and const. With the calibrated parameters in hand, the model can then predict T_C,i(n_s) for all three bands over the full doping range.

The task is to implement the λ_i formulas, perform the calibration, and compute the T_C curves and their maxima.

## Reproduction target
(1) A CSV file `tc_vs_ns.csv` containing T_C values for the three bands as functions of carrier concentration n_s. The file should cover a range that includes regions below n_c₁, around both critical concentrations, and up to high doping beyond n_c₂, with enough points to resolve the shapes of the curves. (2) A CSV file `maxima.csv` that lists, for each band, the maximum T_C and the concentration n_s at which it occurs. The computation should faithfully implement the analytical model described in the instructions; the output should reflect the correct non‑monotonic behaviour and the location of the maxima.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Model calibration
- Role: process
- Action: Using the known physical parameters (effective masses m1=1.8m_e, m2=3.5m_e, m3=6m_e; critical concentrations n_c1=1.2e18 cm^{-3}, n_c2=2.5e19 cm^{-3}) and the experimental first-band T_C maximum (~0.2 K at n_s≈2e18 cm^{-3}), calibrate the effective optical Bohr radius a_B and the constant prefactor const by matching the theoretical first-band maximum to the experimental data. Write the calibrated values to a JSON file.
- Evidence: `/app/outputs/calibration.json`

### Step 2: Compute T_C vs carrier concentration
- Role: scored (load-bearing)
- Action: Using the calibrated a_B and const, compute for each of the three conduction bands the coupling constants λ_i and the transition temperatures T_C_i as functions of carrier concentration n_s. Cover a range of n_s from below n_c1 to above n_c2, including the regions of the T_C maxima. Output a CSV file with columns: n_s (cm^{-3}), T_C_1 (K), T_C_2 (K), T_C_3 (K).
- Output file: `/app/outputs/tc_vs_ns.csv`
- Format: csv
- Contract: CSV with header: n_s,T_C_1,T_C_2,T_C_3. n_s in cm^{-3}, T_C_i in K. Missing (unoccupied) bands may be 0.
- Scoring: scored by hidden verifier

### Step 3: Compute T_C maxima
- Role: scored
- Action: From the computed T_C vs n_s data, determine for each band the maximum value of T_C and the corresponding concentration n_s. Output a CSV file with columns band (integer 1,2,3), n_s_max (cm^{-3}), T_C_max (K).
- Output file: `/app/outputs/maxima.csv`
- Format: csv
- Contract: CSV with header: band,n_s_max,T_C_max. band is integer 1,2,3; three rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_vs_ns.csv`
- `/app/outputs/maxima.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_vs_ns.csv
- path: `/app/outputs/tc_vs_ns.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file with T_C values for the three bands as functions of carrier concentration n_s.
- schema:
  - `type`: table
  - `required_columns`: `n_s`, `T_C_1`, `T_C_2`, `T_C_3`
  - `units`:
    - `n_s`: cm^{-3}
    - `T_C_1`: K
    - `T_C_2`: K
    - `T_C_3`: K

### maxima.csv
- path: `/app/outputs/maxima.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file with the maximum T_C and corresponding concentration for each band.
- schema:
  - `type`: table
  - `required_columns`: `band`, `n_s_max`, `T_C_max`
  - `units`:
    - `n_s_max`: cm^{-3}
    - `T_C_max`: K

Notes: The model uses only analytical formulas; no numerical simulation or external datasets are required. The agent must implement the multi-band coupling constants and the T_C expression as described in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_vs_ns.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_s",
          "T_C_1",
          "T_C_2",
          "T_C_3"
        ],
        "units": {
          "n_s": "cm^{-3}",
          "T_C_1": "K",
          "T_C_2": "K",
          "T_C_3": "K"
        }
      },
      "description": "CSV file with T_C values for the three bands as functions of carrier concentration n_s."
    },
    {
      "file": "maxima.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "band",
          "n_s_max",
          "T_C_max"
        ],
        "units": {
          "n_s_max": "cm^{-3}",
          "T_C_max": "K"
        }
      },
      "description": "CSV file with the maximum T_C and corresponding concentration for each band."
    }
  ],
  "notes": "The model uses only analytical formulas; no numerical simulation or external datasets are required. The agent must implement the multi-band coupling constants and the T_C expression as described in the instruction."
}
```

## How you are scored
A hidden verifier will evaluate your submissions. It will independently implement the same analytical model with the same physical parameters (masses, critical concentrations, dielectric constant) and the correctly calibrated a_B and const. For `tc_vs_ns.csv`, the verifier will recompute T_C values at a set of hidden concentration points and compare your reported T_C values to the recomputed ones; your score for this stage reflects the accuracy of your T_C curves. For `maxima.csv`, the verifier will check that the reported maxima positions and values are consistent with the analytic model’s true maxima within a tolerance. The final reward is a weighted combination: 60 % from the `tc_vs_ns.csv` accuracy and 40 % from the `maxima.csv` correctness. Simply copying published numbers without performing the correct calibration and computation will not produce a good match and will be penalised.
