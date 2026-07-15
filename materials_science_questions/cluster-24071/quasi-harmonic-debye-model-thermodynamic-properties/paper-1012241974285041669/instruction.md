# Quasi-harmonic Debye model thermodynamic properties and Bayesian model selection for CALPHAD modeling of molten salts

## Problem background
Molten chloride salts are widely used in pyroprocessing for lanthanide separation. Accurate thermodynamic models of multi-component chloride systems are needed to predict phase stability, mixing behaviour, and critical operating conditions. This task addresses the KCl-LaCl₃ binary and the LiCl-KCl-LaCl₃ ternary systems. You will compute thermochemical data for intermediate compounds (K₂LaCl₅ and K₃La₅Cl₁₈) using first-principles density-functional theory (DFT) combined with phonon-based quasiharmonic calculations, and then use those data together with published experimental measurements to build CALPHAD models of the liquid phase. The central challenge is to perform Bayesian model comparison among four candidate liquid models (associate, ionic, and two MQMQA variants) and to identify which model is most supported by the available data, as measured by the marginal likelihood. The final deliverables are the predicted equilibrium volumes, bulk moduli, heat capacities, the marginal likelihoods, and the full set of fitted CALPHAD interaction parameters that, when used with PyCalphad, reproduce phase boundaries, mixing enthalpies, and activity coefficients in agreement with the experimental observations.

## Approach
The workflow has two connected stages:

**1. DFT-based compound thermochemistry.**  
Using an open-source plane-wave DFT code (Quantum ESPRESSO with PBE functional) and the phonon package Phonopy, you will first obtain the relaxed crystal structures of KCl, LaCl₃, K₂LaCl₅, and the lowest-energy configuration of the partially-occupied K₃La₅Cl₁₈ phase. For each compound, compute static total energies at several volumes, fit them to a Birch–Murnaghan equation of state, and extract the zero-temperature equilibrium volume, bulk modulus, and its pressure derivative. Then, via finite-displacement supercell phonon calculations at the equilibrium volume, compute the vibrational free energy and derive temperature-dependent thermodynamic properties (heat capacity, entropy, relative enthalpy) under the quasiharmonic approximation. The predicted heat capacities at 500 K for the two ternary compounds are a required output.

**2. CALPHAD modeling and Bayesian model selection.**  
Compile an input dataset from published experimental phase-equilibrium points, mixing enthalpies, and activity-coefficient measurements for KCl-LaCl₃ and LiCl-KCl-LaCl₃, together with the DFT-derived compound data and standard end-member Gibbs energies. Define four liquid models within the PyCalphad/ESPEI framework: an associate model, a two-sublattice ionic model, and two MQMQA models that differ only in their coordination-number sets. For each model, estimate the interaction parameters with Markov Chain Monte Carlo (MCMC) and record the log marginal likelihood. Use the Bayes factor to compare the models and select the most favourable one. Finally, fix the binary parameters of the best model and fit ternary interaction parameters for the LiCl-KCl-LaCl₃ liquid against the ternary experimental data. The output is the full set of optimized CALPHAD parameters for all four binary models and the ternary extension.

## Reproduction target
Produce the following four scored artifacts by executing the complete computational workflow:

- **dft_static_properties.json** – The equilibrium volume V₀ (Å³/atom), bulk modulus B₀ (GPa), and pressure derivative B′ for KCl, LaCl₃, K₂LaCl₅, and K₃La₅Cl₁₈ at 0 K, obtained from DFT energy-volume data and Birch–Murnaghan EOS fitting.
- **dft_heat_capacity_500K.json** – The isobaric heat capacity Cₚ (J mol⁻¹ K⁻¹) at T = 500 K for K₂LaCl₅ and K₃La₅Cl₁₈, extracted from the phonon-based quasiharmonic calculations.
- **marginal_likelihoods.json** – The natural logarithm of the marginal likelihood for each of the four KCl-LaCl₃ liquid models: Associate‑M1, Ionic‑M2, MQMQA‑M3, and MQMQA‑M4. These values quantify how well each model describes the data and enable Bayes-factor model comparisons.
- **calphad_model_parameters.json** – The optimized interaction parameters for the same four binary liquid models, plus for the MQMQA‑M3 model the ternary interaction parameters for LiCl‑KCl‑LaCl₃. The parameters must be in J mol⁻¹ or J mol⁻¹ K⁻¹ and, when used with PyCalphad, should produce phase diagrams, mixing enthalpies, and activity coefficients consistent with the experimental reference data.

Write all files to `/app/outputs` following the exact JSON schemas described in the Workflow steps and Output contract sections.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://pypi.org/project/phonopy/
- ATAT: https://www.brown.edu/Engineering/Labs/avdw/atat/
- ESPEI: https://pypi.org/project/espei/
- PyCalphad: https://pypi.org/project/pycalphad/
- Crystal structures: Use ICSD, Materials Project or literature (e.g., ICSD codes).
- Experimental thermochemical and phase equilibrium data
- SGTE and JANAF thermochemical tables

## Workflow steps

### Step 1: Configurational search and structure optimization
- Role: process
- Action: Use ATAT to enumerate symmetry-inequivalent configurations for the K3La5Cl18 proto-cell and perform DFT relaxations to identify the lowest-energy structure. Also obtain relaxed unit cells for KCl, LaCl3, K2LaCl5.
- Evidence: `/app/outputs/01_structure_results.log`

### Step 2: DFT static energy-volume calculations
- Role: process
- Action: For each compound, compute total energies at a series of volumes around the equilibrium volume using Quantum ESPRESSO (PBE). Save the E(V) data points.
- Evidence: `/app/outputs/02_energies.csv`

### Step 3: Phonon supercell calculations
- Role: process
- Action: Using the relaxed structures, perform finite-displacement phonon calculations with Phonopy and Quantum ESPRESSO at the equilibrium volume (or a set of volumes) to obtain phonon frequencies for each compound.
- Evidence: `/app/outputs/03_phonon_dos.json`

### Step 4: Birch-Murnaghan EOS fitting and equilibrium properties
- Role: scored
- Action: Fit the E(V) data to a four-parameter Birch-Murnaghan equation of state and extract the equilibrium volume V0 (ang^3/atom), bulk modulus B0 (GPa), and its pressure derivative B' for each compound. Output the results as dft_static_properties.json.
- Output file: `/app/outputs/dft_static_properties.json`
- Format: json
- Contract: JSON object with keys: KCl, LaCl3, K2LaCl5, K3La5Cl18. Each value is an object with fields: V0_ang3_per_atom (float), B0_GPa (float), B_prime (float).
- Scoring: scored by hidden verifier

### Step 5: Quasiharmonic thermodynamic property calculations
- Role: process
- Action: From the phonon frequencies at the equilibrium volume, compute the vibrational Helmholtz free energy and derive temperature-dependent heat capacity Cp, entropy S, and relative enthalpy H-H300 for each compound over a temperature range (e.g., 0–1200 K). Save the full (T, Cp) arrays for later use.
- Evidence: `/app/outputs/05_qha_thermo.csv`

### Step 6: Heat capacity at 500 K
- Role: scored
- Action: Extract the heat capacity at 500 K for K2LaCl5 and K3La5Cl18 from the computed thermodynamic data and write to dft_heat_capacity_500K.json.
- Output file: `/app/outputs/dft_heat_capacity_500K.json`
- Format: json
- Contract: JSON object with keys: K2LaCl5 (float, Cp in J/mol-K), K3La5Cl18 (float, Cp in J/mol-K).
- Scoring: scored by hidden verifier

### Step 7: Compile CALPHAD input dataset
- Role: process
- Action: Collect experimental phase equilibrium data (liquidus, eutectic temperatures, invariant compositions) for KCl-LaCl3 from Seifert et al. (1985) and Song and Zheng (1995); mixing enthalpy data from Papatheodorou and Ostvold (1974); activity coefficients of LaCl3 in LiCl-KCl from Bagri and Simpson (2016) and Samin et al. (2016); mixing enthalpies in ternary from Goncharov et al. (2024). Combine with the DFT thermodynamic data for compounds (Cp(T), formation enthalpies, etc.) and binary endmember data from SGTE/JANAF. Prepare the dataset in ESPEI-compatible format.
- Evidence: `/app/outputs/07_calphad_dataset.json`

### Step 8: MCMC parameter estimation for KCl-LaCl3 liquid models
- Role: process
- Action: For each of the four liquid models (Associate-M1, Ionic-M2, MQMQA-M3, MQMQA-M4), run ESPEI MCMC optimization using the compiled dataset. Collect posterior parameter chains and marginal likelihood estimates.
- Evidence: `/app/outputs/08_mcmc_chains`

### Step 9: Marginal likelihood and Bayes factor reporting
- Role: scored
- Action: Extract the ln(marginal_likelihood) for each model from the MCMC outputs and write them to marginal_likelihoods.json.
- Output file: `/app/outputs/marginal_likelihoods.json`
- Format: json
- Contract: JSON object with keys: Associate_M1 (number), Ionic_M2 (number), MQMQA_M3 (number), MQMQA_M4 (number); each value is the natural logarithm of the marginal likelihood.
- Scoring: scored by hidden verifier

### Step 10: Ternary MQMQA parameter fitting
- Role: process
- Action: Fix the binary parameters of the best model (MQMQA-M3) and run MCMC to estimate the ternary interaction parameters for the LiCl-KCl-LaCl3 liquid using ternary experimental data (phase boundaries, activity coefficients, mixing enthalpy).
- Evidence: `/app/outputs/10_ternary_mcmc.log`

### Step 11: CALPHAD model parameters
- Role: scored (load-bearing)
- Action: Collect the optimized interaction parameters for all four binary models and the ternary model, and write them following the schema in calphad_model_parameters.json.
- Output file: `/app/outputs/calphad_model_parameters.json`
- Format: json
- Contract: JSON object containing liquid model parameters for KCl-LaCl3 and LiCl-KCl-LaCl3. It must include, for each model (Associate-M1, Ionic-M2, MQMQA-M3, MQMQA-M4), the interaction parameters as given in the paper; for MQMQA-M3 also the ternary parameters. Numeric values in J/mol or J/mol-K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_static_properties.json`
- `/app/outputs/dft_heat_capacity_500K.json`
- `/app/outputs/marginal_likelihoods.json`
- `/app/outputs/calphad_model_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_static_properties.json
- path: `/app/outputs/dft_static_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium volumes, bulk moduli, and pressure derivatives for the four compounds at 0 K from DFT+EOS fitting. Scored by exact match within tolerances to the paper-reported values.
- schema:
  - `type`: object
  - `required`:
    - `KCl`:
      - `V0_ang3_per_atom`: float
      - `B0_GPa`: float
      - `B_prime`: float
    - `LaCl3`:
      - `V0_ang3_per_atom`: float
      - `B0_GPa`: float
      - `B_prime`: float
    - `K2LaCl5`:
      - `V0_ang3_per_atom`: float
      - `B0_GPa`: float
      - `B_prime`: float
    - `K3La5Cl18`:
      - `V0_ang3_per_atom`: float
      - `B0_GPa`: float
      - `B_prime`: float

### dft_heat_capacity_500K.json
- path: `/app/outputs/dft_heat_capacity_500K.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Heat capacity at 500 K for the two ternary compounds computed from DFT+phonon QHA. Scored by exact match within tolerances to paper-reported values.
- schema:
  - `type`: object
  - `required`:
    - `K2LaCl5`: float (J/mol-K)
    - `K3La5Cl18`: float (J/mol-K)

### marginal_likelihoods.json
- path: `/app/outputs/marginal_likelihoods.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Estimated log marginal likelihoods for the four liquid models. Scored by exact match within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `Associate_M1`: number (log marginal likelihood)
    - `Ionic_M2`: number
    - `MQMQA_M3`: number
    - `MQMQA_M4`: number

### calphad_model_parameters.json
- path: `/app/outputs/calphad_model_parameters.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted interaction parameters for the binary and ternary liquid models. The checker will recompute phase diagrams, activity coefficients, and mixing enthalpies using these parameters and compare them to experimental reference values.
- schema:
  - `type`: object
  - `required`:
    - `Associate_M1`:
      - `L0`:
        - `A`: number (J/mol)
        - `B`: number (J/mol-K)
      - `L1`:
        - `A`: number
        - `B`: number
    - `Ionic_M2`:
      - `L0`:
        - `A`: number
        - `B`: number
      - `L1`:
        - `A`: number
        - `B`: number
    - `MQMQA_M3`:
      - `delta_g_ex`:
        - `A`: number
        - `B`: number
      - `chi_KLaCl2`: number
      - `chi_LaKCl2`: number
      - `ternary`:
        - `Delta_g_101`: number
        - `Delta_g_001`:
          - `A`: number
          - `B`: number
    - `MQMQA_M4`:
      - `delta_g_ex`:
        - `A`: number
        - `B`: number
      - `chi_KLaCl2`: number
      - `chi_LaKCl2`: number

Notes: All scored artifacts must be written under /app/outputs. Tolerances and exact gold values are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_static_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "KCl": {
            "V0_ang3_per_atom": "float",
            "B0_GPa": "float",
            "B_prime": "float"
          },
          "LaCl3": {
            "V0_ang3_per_atom": "float",
            "B0_GPa": "float",
            "B_prime": "float"
          },
          "K2LaCl5": {
            "V0_ang3_per_atom": "float",
            "B0_GPa": "float",
            "B_prime": "float"
          },
          "K3La5Cl18": {
            "V0_ang3_per_atom": "float",
            "B0_GPa": "float",
            "B_prime": "float"
          }
        }
      },
      "description": "Equilibrium volumes, bulk moduli, and pressure derivatives for the four compounds at 0 K from DFT+EOS fitting. Scored by exact match within tolerances to the paper-reported values."
    },
    {
      "file": "dft_heat_capacity_500K.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "K2LaCl5": "float (J/mol-K)",
          "K3La5Cl18": "float (J/mol-K)"
        }
      },
      "description": "Heat capacity at 500 K for the two ternary compounds computed from DFT+phonon QHA. Scored by exact match within tolerances to paper-reported values."
    },
    {
      "file": "marginal_likelihoods.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Associate_M1": "number (log marginal likelihood)",
          "Ionic_M2": "number",
          "MQMQA_M3": "number",
          "MQMQA_M4": "number"
        }
      },
      "description": "Estimated log marginal likelihoods for the four liquid models. Scored by exact match within tolerances."
    },
    {
      "file": "calphad_model_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "Associate_M1": {
            "L0": {
              "A": "number (J/mol)",
              "B": "number (J/mol-K)"
            },
            "L1": {
              "A": "number",
              "B": "number"
            }
          },
          "Ionic_M2": {
            "L0": {
              "A": "number",
              "B": "number"
            },
            "L1": {
              "A": "number",
              "B": "number"
            }
          },
          "MQMQA_M3": {
            "delta_g_ex": {
              "A": "number",
              "B": "number"
            },
            "chi_KLaCl2": "number",
            "chi_LaKCl2": "number",
            "ternary": {
              "Delta_g_101": "number",
              "Delta_g_001": {
                "A": "number",
                "B": "number"
              }
            }
          },
          "MQMQA_M4": {
            "delta_g_ex": {
              "A": "number",
              "B": "number"
            },
            "chi_KLaCl2": "number",
            "chi_LaKCl2": "number"
          }
        }
      },
      "description": "Fitted interaction parameters for the binary and ternary liquid models. The checker will recompute phase diagrams, activity coefficients, and mixing enthalpies using these parameters and compare them to experimental reference values."
    }
  ],
  "notes": "All scored artifacts must be written under /app/outputs. Tolerances and exact gold values are hidden."
}
```

## How you are scored
An automated hidden verifier will evaluate your submission. It independently checks each scored artifact:

- For **dft_static_properties.json** and **dft_heat_capacity_500K.json** it compares your computed values to hidden reference values derived from the paper’s reported DFT results.
- For **marginal_likelihoods.json** it compares your reported log marginal likelihoods to hidden reference values; the relative ordering of the four models is also checked.
- For **calphad_model_parameters.json** it recomputes phase boundaries, mixing enthalpies, and activity coefficients from your submitted parameters using PyCalphad and compares those derived quantities to hidden experimental benchmarks.

Each artifact contributes a weighted portion of the total reward (between 0 and 1). The verifier only sees the files you place in `/app/outputs`. Simply reporting numbers from the literature is not sufficient; you must produce them through the prescribed computational workflow.
