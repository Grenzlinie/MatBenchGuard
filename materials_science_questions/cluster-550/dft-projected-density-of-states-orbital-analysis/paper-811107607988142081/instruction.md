# DFT and Boltzmann transport study of SnO2 thermoelectric properties

## Problem background
Thermoelectric materials directly convert heat into electricity. Tin dioxide (SnO2) in the rutile structure is an oxide semiconductor of interest for high-temperature thermoelectric applications because it is non-toxic, abundant, and thermally stable. However, a quantitative first-principles assessment of its electronic transport coefficients is required to understand its potential. This task is to compute the electronic structure and semi-classical transport coefficients of rutile SnO2 using density functional theory (DFT) and Boltzmann transport equations, and to evaluate its thermoelectric performance through key quantities such as the Seebeck coefficient, power factor, and electronic figure of merit.

## Approach
First, the ground-state crystal structure of rutile SnO2 is relaxed using the generalized gradient approximation (GGA) for exchange-correlation. Then, the Tran–Blaha modified Becke–Johnson (TB-mBJ) meta‑GGA functional is employed to compute an accurate electronic band structure and density of states. Using this band structure, the Seebeck coefficient S(μ,T) and the reduced transport coefficients σ/τ and κe/τ are obtained within the semi-classical Boltzmann transport framework under the rigid band approximation, for a range of chemical potentials (doping levels) and temperatures. Finally, the absolute electrical conductivity and power factor are derived by calibrating the relaxation time against an experimental data point (Seebeck coefficient and electrical conductivity at 900 K) from a published ceramic SnO2 study, assuming an electron–phonon scaling τ(T,n) ∝ T⁻¹ n⁻¹⁄³.

## Reproduction target
Produce the relaxed lattice constants a and c (in nm) of rutile SnO2 from GGA structural optimization. Compute the fundamental band gap (in eV) using the TB-mBJ functional. Then, after calibrating the relaxation time, determine the maximum Seebeck coefficient for both p‑type and n‑type doping (in μV/K, positive and negative, respectively), the maximum power factor for both n‑type and p‑type doping (in W/m·K²), and the electronic figure of merit ZT_e at the optimal doping level. Report these quantities in the specified JSON output files.

## Assets

- exciting (open-source FP-LAPW DFT with TB-mBJ functional): http://exciting-code.org/
- BoltzTraP2 (Boltzmann transport properties solver): https://www.boltztrapp2.org/
- Tsubota et al. experimental Seebeck and conductivity data: 10.1007/s11664-014-3281-9
- Rutile SnO2 experimental crystal structure

## Workflow steps

### Step 1: DFT structural optimization
- Role: scored
- Action: Perform FP-LAPW DFT structural optimization of rutile SnO2 using the GGA functional. Calculate total energy as a function of reduced unit-cell volume and the c/a ratio, then fit to locate the minimum-energy geometry. Output the relaxed lattice constants a and c in nm.
- Output file: `/app/outputs/relaxed_lattice.json`
- Format: json
- Contract: JSON object with keys "a_nm" (float) and "c_nm" (float).
- Scoring: scored by hidden verifier

### Step 2: Electronic structure calculation
- Role: scored
- Action: Using the relaxed structure from step 1, compute the electronic band structure and density of states with the TB-mBJ exchange-correlation functional. Determine the fundamental band gap as the energy difference between the valence band maximum and the conduction band minimum.
- Output file: `/app/outputs/electronic_results.json`
- Format: json
- Contract: JSON object with key "band_gap_eV" (float).
- Scoring: scored by hidden verifier

### Step 3: Boltzmann transport and relaxation time calibration
- Role: process
- Action: Use BoltzTraP2 (rigid band approximation) with the band structure from step 2 to compute the Seebeck coefficient S(μ,T), reduced electrical conductivity σ/τ, and reduced electronic thermal conductivity κe/τ as functions of chemical potential and temperature (e.g., 600, 900, 1200 K). Then retrieve the experimental Seebeck coefficient and electrical conductivity at 900 K from Tsubota et al. (2014). Calibrate the relaxation time by assuming an electron-phonon dependence τ(T,n) = C·T⁻¹·n⁻¹/³; fit C by matching the computed S and σ/τ to the experimental data point. Store the reduced transport data and the fitted relaxation-time model for the next step.
- Evidence: `/app/outputs/relaxation_time_model.json`

### Step 4: Absolute transport coefficients and figure of merit
- Role: scored (load-bearing)
- Action: Combine the reduced transport coefficients from step 3 with the calibrated relaxation-time model to obtain absolute electrical conductivity σ(μ,T), power factor PF = σS², and electronic figure of merit ZT_e = σS²T/κe. From the computed data, extract: (a) the maximum Seebeck coefficient for p-type and n-type doping (obtained before calibration); (b) the maximum power factor for n-type and p-type doping; (c) the electronic figure of merit at the optimal doping. Report these values in the output file.
- Output file: `/app/outputs/transport_results.json`
- Format: json
- Contract: JSON object with keys: "Seebeck_p_type_muV_per_K" (float, positive), "Seebeck_n_type_muV_per_K" (float, negative), "PF_n_type_W_per_mK2" (float), "PF_p_type_W_per_mK2" (float), "ZT_electronic" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_lattice.json`
- `/app/outputs/electronic_results.json`
- `/app/outputs/transport_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_lattice.json
- path: `/app/outputs/relaxed_lattice.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice constants a and c from GGA structural optimization.
- schema:
  - `type`: object
  - `required`:
    - `a_nm`: float (nm)
    - `c_nm`: float (nm)

### electronic_results.json
- path: `/app/outputs/electronic_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap computed with TB-mBJ functional.
- schema:
  - `type`: object
  - `required`:
    - `band_gap_eV`: float (eV)

### transport_results.json
- path: `/app/outputs/transport_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final thermoelectric quantities extracted from the calibrated transport data: peak Seebeck coefficients, maximum power factors, and electronic figure of merit.
- schema:
  - `type`: object
  - `required`:
    - `Seebeck_p_type_muV_per_K`: float (positive)
    - `Seebeck_n_type_muV_per_K`: float (negative)
    - `PF_n_type_W_per_mK2`: float
    - `PF_p_type_W_per_mK2`: float
    - `ZT_electronic`: float

Notes: All scored artifacts are compared against hidden reference values derived from the paper, using tolerances appropriate for code/functional differences. The relaxation-time calibration step (process) must be executed by the agent to obtain the model required for step 4.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_lattice.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "a_nm": "float (nm)",
          "c_nm": "float (nm)"
        }
      },
      "description": "Relaxed lattice constants a and c from GGA structural optimization."
    },
    {
      "file": "electronic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "band_gap_eV": "float (eV)"
        }
      },
      "description": "Band gap computed with TB-mBJ functional."
    },
    {
      "file": "transport_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Seebeck_p_type_muV_per_K": "float (positive)",
          "Seebeck_n_type_muV_per_K": "float (negative)",
          "PF_n_type_W_per_mK2": "float",
          "PF_p_type_W_per_mK2": "float",
          "ZT_electronic": "float"
        }
      },
      "description": "Final thermoelectric quantities extracted from the calibrated transport data: peak Seebeck coefficients, maximum power factors, and electronic figure of merit."
    }
  ],
  "notes": "All scored artifacts are compared against hidden reference values derived from the paper, using tolerances appropriate for code/functional differences. The relaxation-time calibration step (process) must be executed by the agent to obtain the model required for step 4."
}
```

## How you are scored
Your submission is evaluated by an automated checker. It reads the three scored artifacts (`relaxed_lattice.json`, `electronic_results.json`, and `transport_results.json`) and compares your reported values against hidden reference criteria, with tolerances that account for legitimate differences between open‑source and proprietary codes and for reasonable discretisation choices. Each stage contributes a weighted share to the final reward. Simply reporting numbers that happen to match the paper’s values is not enough; the checker verifies that the outputs are consistent with a properly executed computational pipeline.
