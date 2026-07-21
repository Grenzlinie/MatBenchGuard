# ZT Enhancement of ZnO Nanowires via Phase Transformation

## Problem background
Thermoelectric materials convert heat into electricity, and their efficiency is captured by the dimensionless figure of merit ZT = S²σT/κ. ZnO nanowires are promising thermoelectrics because of their high Seebeck coefficient and stability, but their high thermal conductivity limits performance. Recent work suggests that a phase transformation from the conventional wurtzite (W) phase to a hexagonal (H) phase, triggered by tensile loading, significantly alters electronic and phonon transport. This task investigates whether the H-phase can yield a higher ZT than the W-phase for a [0001]-oriented ZnO nanowire (wire D), and how the relative thermoelectric performance changes with temperature.

## Approach
The workflow proceeds in three stages. First, density functional theory (DFT) with the PBE GGA functional is used to relax the atomic geometry of ZnO nanowire D in both W and H phases and to compute their electronic band structures. From the band structures the electron effective mass and density of states are extracted.

Second, a one‑dimensional Boltzmann transport equation (BTE) model is built. The electron relaxation time is calibrated against a published experimental conductivity data point (σ = 384.6 (Ω·cm)⁻¹ at n = 8.8×10¹⁹ cm⁻³, T = 300 K), and its carrier‑concentration dependence is taken from an empirical mobility–concentration relation for ZnO thin films. Under the rigid‑band approximation, the model yields the electrical conductivity, Seebeck coefficient, and electronic thermal conductivity for both phases as functions of carrier concentration at 300 K, and later as functions of temperature at the optimal doping levels.

Finally, the total thermal conductivity is assembled using literature phonon thermal conductivities (κ_ph = 10.1 W/m·K for H‑phase, 8.3 W/m·K for W‑phase), and ZT is computed. The key output is the ratio ZT_H / ZT_W over the temperature range 200–1000 K.

## Reproduction target
Produce two scored CSV artifacts under /app/outputs:

1. **electronic_transport.csv** – electronic transport properties (σ, S, κ_e, power factor) for both W and H phases as a function of carrier concentration at 300 K.

2. **temperature_dependence_ZT.csv** – ZT and the ratio ZT_H / ZT_W for the H‑phase at n = 6.5×10¹⁸ cm⁻³ and the W‑phase at n = 7.1×10¹⁸ cm⁻³, sampled at temperatures from 200 K to 1000 K (e.g., 100 K steps).

The verifier will cross‑check internal consistency between these two files and then evaluate the temperature‑dependent ZT ratio: the ratio values at selected benchmark temperatures and the qualitative shape of the ratio‑vs‑temperature curve. The objective is to reproduce the relative thermoelectric performance of the two phases as a function of temperature.

## Assets

- Open-source DFT code (Quantum ESPRESSO, CP2K, or equivalent): https://www.quantum-espresso.org/
- Experimental conductivity data point from Noriega et al.: 10.1063/1.3425883
- Empirical mobility–carrier concentration relation for ZnO thin films (Ellmer & Mietus): 10.1016/j.tsf.2007.09.037
- Phonon thermal conductivity values from Kulkarni & Zhou: 10.1088/0957-4484/18/43/435706

## Workflow steps

### Step 1: DFT geometry optimization of ZnO nanowire D
- Role: process
- Action: Using an open-source DFT code (Quantum ESPRESSO or equivalent, PBE GGA functional, 1×1×16 k-point mesh), relax the atomic positions and supercell lengths of [0001]-oriented ZnO nanowire D in both wurtzite (W) and hexagonal (H) phases. Use the supercell approach with sufficient vacuum in the transverse directions. Target the reported diameters (approx. 1.4 nm for W, 1.75 nm for H) and optimized supercell lengths.
- Evidence: `/app/outputs/geometry_opt.log`

### Step 2: DFT band structure and effective mass calculation
- Role: process
- Action: From the optimized structures, compute the electronic band structure along kz, density of states, and extract the electron effective mass at the Γ point from the curvature of the lowest conduction band. Use the same DFT settings. Output the band energies and density of states in a format suitable for the subsequent transport code.
- Evidence: `/app/outputs/band_data.log`

### Step 3: 1D BTE transport simulation at T=300 K vs carrier concentration
- Role: scored (load-bearing)
- Action: Implement the 1D Boltzmann transport equation using the effective masses and density of states from step 2. Calibrate the electron relaxation time: first fit τ₀ from the experimental data point σ=384.6 (Ω·cm)⁻¹ at n=8.8×10¹⁹ cm⁻³, T=300 K. Then scale τ with carrier concentration using the empirical mobility–concentration relation from Ellmer & Mietus. Under the rigid-band approximation, shift the chemical potential to simulate doping and compute the electrical conductivity σ (in S/m), Seebeck coefficient S (in µV/K), electronic thermal conductivity κ_e (in W/m·K), and power factor P = S²σ (in µW/m·K²) for both H and W phases as functions of electron carrier concentration n from 1×10¹⁸ to 1×10²⁰ cm⁻³ at T=300 K. Save the results to electronic_transport.csv.
- Output file: `/app/outputs/electronic_transport.csv`
- Format: csv
- Contract: CSV with columns: n_cm3, sigma_H_Sm, sigma_W_Sm, S_H_uVK, S_W_uVK, kappa_e_H_WmK, kappa_e_W_WmK, P_H_uWmK2, P_W_uWmK2
- Scoring: scored by hidden verifier

### Step 4: Temperature-dependent transport coefficients at fixed doping
- Role: process
- Action: Using the same transport model, compute the electronic transport coefficients (σ, S, κ_e) for H-phase at n = 6.5×10¹⁸ cm⁻³ and for W-phase at n = 7.1×10¹⁸ cm⁻³, for temperatures from 200 K to 1000 K (e.g., at 100 K intervals). Save raw results as a JSON file for provenance.
- Evidence: `/app/outputs/transport_vs_T.json`

### Step 5: ZT calculation and relative ZT ratio
- Role: scored (load-bearing)
- Action: For each temperature from 200 K to 1000 K, compute the figure of merit ZT = S²σ T / (κ_e + κ_ph) using the temperature-dependent transport coefficients from step 4 and the constant phonon thermal conductivities κ_ph = 10.1 W/m·K (H-phase) and 8.3 W/m·K (W-phase) from Kulkarni & Zhou. Calculate the ratio ZT_H / ZT_W. Write the data to temperature_dependence_ZT.csv.
- Output file: `/app/outputs/temperature_dependence_ZT.csv`
- Format: csv
- Contract: CSV with columns: T_K, ZT_H, ZT_W, ratio_ZT_HW
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_transport.csv`
- `/app/outputs/temperature_dependence_ZT.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_transport.csv
- path: `/app/outputs/electronic_transport.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Electronic transport properties vs carrier concentration at 300 K for both phases. The checker will recompute ZT from these values and cross-check consistency with the T=300 K row of temperature_dependence_ZT.csv.
- schema:
  - `type`: table
  - `required_columns`: `n_cm3`, `sigma_H_Sm`, `sigma_W_Sm`, `S_H_uVK`, `S_W_uVK`, `kappa_e_H_WmK`, `kappa_e_W_WmK`, `P_H_uWmK2`, `P_W_uWmK2`

### temperature_dependence_ZT.csv
- path: `/app/outputs/temperature_dependence_ZT.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: ZT values and ratio for H and W phases as a function of temperature at optimal doping. The checker will compare the ratio_ZT_HW values at T=300 K and T=1000 K against hidden reference values, and verify the qualitative temperature trend.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `ZT_H`, `ZT_W`, `ratio_ZT_HW`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_transport.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_cm3",
          "sigma_H_Sm",
          "sigma_W_Sm",
          "S_H_uVK",
          "S_W_uVK",
          "kappa_e_H_WmK",
          "kappa_e_W_WmK",
          "P_H_uWmK2",
          "P_W_uWmK2"
        ]
      },
      "description": "Electronic transport properties vs carrier concentration at 300 K for both phases. The checker will recompute ZT from these values and cross-check consistency with the T=300 K row of temperature_dependence_ZT.csv."
    },
    {
      "file": "temperature_dependence_ZT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "ZT_H",
          "ZT_W",
          "ratio_ZT_HW"
        ]
      },
      "description": "ZT values and ratio for H and W phases as a function of temperature at optimal doping. The checker will compare the ratio_ZT_HW values at T=300 K and T=1000 K against hidden reference values, and verify the qualitative temperature trend."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted CSV files and scores each stage independently. For `electronic_transport.csv` it recomputes ZT from the reported transport coefficients and checks consistency with the 300 K row of `temperature_dependence_ZT.csv`. For `temperature_dependence_ZT.csv` it inspects the ZT ratio at specific temperatures and examines the qualitative shape of the ratio‑vs‑temperature curve, and the checker will verify against a hidden reference trend. The final reward is a weighted combination of these stage scores, with the largest weight on the ZT ratio at key temperatures. Reporting numbers that do not originate from the computational pipeline described in the workflow will not receive full credit.
