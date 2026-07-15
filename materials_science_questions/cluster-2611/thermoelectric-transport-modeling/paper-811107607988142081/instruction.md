# Ab initio thermoelectric transport modeling of SnO2

## Problem background
Thermoelectric materials, which directly convert heat into electricity, require a delicate balance of high electrical conductivity, large Seebeck coefficient, and low thermal conductivity. Oxide semiconductors like SnO₂ are attractive because they are stable, non‑toxic, and low‑cost. Predicting their thermoelectric performance from first principles lets researchers identify optimal doping levels and operating temperatures without exhaustive trial experiments. This task reproduces a first‑principles study that computes the structural, electronic, and thermoelectric transport properties of rutile SnO₂, providing insight into its potential as a high‑temperature thermoelectric.

## Approach
The workflow combines density functional theory (DFT) with semiclassical Boltzmann transport to predict the figure of merit. The crystal structure of rutile SnO₂ (space group 136) is relaxed using the generalized gradient approximation (GGA) within a full‑potential linearized augmented plane‑wave (FP‑LAPW) framework. Using the relaxed geometry, the electronic band structure is computed with the more accurate Tran–Blaha modified Becke–Johnson (TB‑mBJ) potential, which corrects the well‑known band‑gap underestimation of standard GGA. The resulting Kohn‑Sham eigenvalues are fed into a Boltzmann transport solver under the constant relaxation time approximation. This yields reduced transport coefficients—Seebeck coefficient S, electrical conductivity over relaxation time σ/τ, electronic thermal conductivity over relaxation time κₑ/τ, and power factor σS²/τ—as functions of chemical potential (i.e., doping level) at the three temperatures 600 K, 900 K, and 1200 K. The unknown relaxation time τ is estimated by matching the computed S and σ/τ at 900 K to experimentally measured values for a specific ceramic SnO₂ sample (Seebeck –175 μV/K, conductivity 353 (Ω·m)⁻¹ at a doping concentration of 3.95×10¹⁹ cm⁻³, as given in the task assets). Once τ is known, absolute electrical conductivity, power factor, and the electronic figure of merit ZTₑ are obtained. This approach allows the agent to compute the thermoelectric response of both n‑type and p‑type doping without relying on any pre‑computed transport data.

## Reproduction target
The objective is to compute and report the following quantities by executing the DFT and transport workflow described in the steps below:

- The equilibrium lattice constants a and c (in nm) of rutile SnO₂ obtained from GGA relaxation.
- The direct band gap (in eV) at the Γ point computed with the TB‑mBJ functional.
- For the temperature 600 K: the peak Seebeck coefficient (μV/K) for n‑type and p‑type doping.
- For the temperature 900 K: the optimal n‑type and p‑type doping parameters, each comprising the chemical potential shift (eV), carrier concentration (cm⁻³), Seebeck coefficient (μV/K), absolute electrical conductivity ((Ω·m)⁻¹), power factor (W m⁻¹ K⁻²), and electronic figure of merit ZTₑ (dimensionless).
- The estimated carrier relaxation time τ (in seconds) obtained from the calibration procedure.

These results must be written as three JSON files—lattice_constants.json, band_gap.json, and transport_summary.json—conforming to the output contracts below. The hidden verifier will compare your reported numbers to reference values derived from the original publication.

## Assets

- Initial rutile SnO2 crystal structure
- Elk FP-LAPW DFT code: https://elk.sourceforge.net/
- BoltzTraP2: https://github.com/sponce24/BoltzTraP2
- Experimental transport data for SnO2 (Tsubota et al. 2014): 10.1007/s11664-014-3359-2

## Workflow steps

### Step 1: DFT structural relaxation of rutile SnO2 with GGA
- Role: process
- Action: Perform FP-LAPW DFT structural optimization of rutile SnO2 using the GGA functional, starting from the experimental crystal structure (space group 136, a=b=0.4737 nm, c=0.3142 nm, u=0.306), to find the equilibrium lattice constants a and c.
- Evidence: `/app/outputs/relaxation_output.log`

### Step 2: Extract relaxed lattice constants
- Role: scored
- Action: From the optimized structure, read and output the relaxed lattice constants a and c (in nm).
- Output file: `/app/outputs/lattice_constants.json`
- Format: json
- Contract: {"a_nm": float, "c_nm": float}
- Scoring: scored by hidden verifier

### Step 3: Electronic structure calculation with TB-mBJ
- Role: process
- Action: Using the relaxed structure, compute the electronic band structure of SnO2 with the TB-mBJ exchange-correlation functional along a high-symmetry path, obtaining the Kohn-Sham eigenvalues and the band gap.
- Evidence: `/app/outputs/band_structure.dat`

### Step 4: Compute band gap
- Role: scored
- Action: Extract the direct band gap (eV) from the band structure at the Γ-point.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {"band_gap_eV": float}
- Scoring: scored by hidden verifier

### Step 5: Boltzmann transport calculation
- Role: process
- Action: Use the band structure as input to BoltzTraP2 to compute the transport distribution and reduced transport coefficients (Seebeck S, electrical conductivity σ/τ, electronic thermal conductivity κ_e/τ, power factor σS²/τ) as functions of chemical potential at temperatures 600 K, 900 K, and 1200 K, under the constant relaxation time approximation.
- Evidence: `/app/outputs/BoltzTraP2_output.traced_r8`

### Step 6: Estimate relaxation time and compute absolute transport properties
- Role: scored (load-bearing)
- Action: Using the reduced transport coefficients from step 5 and the experimental calibration data (Seebeck coefficient S = -175 µV/K, electrical conductivity σ = 353 (Ωm)⁻¹ at T = 900 K), estimate the carrier relaxation time τ by matching computed S and σ/τ at a doping concentration of n = 3.95×10¹⁹ cm⁻³. Then compute absolute electrical conductivity, power factor, and electronic figure of merit ZT_e as functions of doping and temperature. Extract the Seebeck peak values at 600 K for both n-type and p-type, and the optimal n-type and p-type parameters at 900 K (chemical potential shift, carrier concentration, Seebeck, conductivity, power factor, ZT_e). Output all in a structured JSON.
- Output file: `/app/outputs/transport_summary.json`
- Format: json
- Contract: {"relaxation_time_s": float, "n_type_600K": {"Seebeck_peak_uVK": float}, "p_type_600K": {"Seebeck_peak_uVK": float}, "900K": {"n_type": {"chem_pot_eV": float, "carrier_conc_cm3": float, "Seebeck_uVK": float, "sigma_Ohmm": float, "power_factor_WmK2": float, "ZT_e": float}, "p_type": {"chem_pot_eV": float, "carrier_conc_cm3": float, "Seebeck_uVK": float, "sigma_Ohmm": float, "power_factor_WmK2": float, "ZT_e": float}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.json`
- `/app/outputs/band_gap.json`
- `/app/outputs/transport_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.json
- path: `/app/outputs/lattice_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Relaxed lattice constants of rutile SnO2 from DFT-GGA structural optimization.
- schema:
  - `type`: object
  - `required`: `a_nm`, `c_nm`
  - `properties`:
    - `a_nm`:
      - `type`: number
      - `unit`: nm
    - `c_nm`:
      - `type`: number
      - `unit`: nm

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Direct band gap of SnO2 at the Γ-point from TB-mBJ electronic structure calculation.
- schema:
  - `type`: object
  - `required`: `band_gap_eV`
  - `properties`:
    - `band_gap_eV`:
      - `type`: number
      - `unit`: eV

### transport_summary.json
- path: `/app/outputs/transport_summary.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Thermoelectric transport properties of SnO2: relaxation time, Seebeck peaks at 600 K, and optimal n-type/p-type parameters at 900 K.
- schema:
  - `type`: object
  - `required`: `relaxation_time_s`, `n_type_600K`, `p_type_600K`, `900K`
  - `properties`:
    - `relaxation_time_s`:
      - `type`: number
      - `unit`: s
    - `n_type_600K`:
      - `type`: object
      - `required`: `Seebeck_peak_uVK`
      - `properties`:
        - `Seebeck_peak_uVK`:
          - `type`: number
          - `unit`: μV/K
    - `p_type_600K`:
      - `type`: object
      - `required`: `Seebeck_peak_uVK`
      - `properties`:
        - `Seebeck_peak_uVK`:
          - `type`: number
          - `unit`: μV/K
    - `900K`:
      - `type`: object
      - `required`: `n_type`, `p_type`
      - `properties`:
        - `n_type`:
          - `type`: object
          - `required`: `chem_pot_eV`, `carrier_conc_cm3`, `Seebeck_uVK`, `sigma_Ohmm`, `power_factor_WmK2`, `ZT_e`
          - `properties`:
            - `chem_pot_eV`:
              - `type`: number
              - `unit`: eV
            - `carrier_conc_cm3`:
              - `type`: number
              - `unit`: cm^{-3}
            - `Seebeck_uVK`:
              - `type`: number
              - `unit`: μV/K
            - `sigma_Ohmm`:
              - `type`: number
              - `unit`: (Ωm)^{-1}
            - `power_factor_WmK2`:
              - `type`: number
              - `unit`: W/mK^{2}
            - `ZT_e`:
              - `type`: number
        - `p_type`:
          - `type`: object
          - `required`: `chem_pot_eV`, `carrier_conc_cm3`, `Seebeck_uVK`, `sigma_Ohmm`, `power_factor_WmK2`, `ZT_e`
          - `properties`:
            - `chem_pot_eV`:
              - `type`: number
              - `unit`: eV
            - `carrier_conc_cm3`:
              - `type`: number
              - `unit`: cm^{-3}
            - `Seebeck_uVK`:
              - `type`: number
              - `unit`: μV/K
            - `sigma_Ohmm`:
              - `type`: number
              - `unit`: (Ωm)^{-1}
            - `power_factor_WmK2`:
              - `type`: number
              - `unit`: W/mK^{2}
            - `ZT_e`:
              - `type`: number

Notes: The agent must run all computational stages; no pre-computed results are provided. The experimental calibration data from Tsubota et al. are provided in the task instruction. Only electronic transport quantities are computed; lattice thermal conductivity is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a_nm",
          "c_nm"
        ],
        "properties": {
          "a_nm": {
            "type": "number",
            "unit": "nm"
          },
          "c_nm": {
            "type": "number",
            "unit": "nm"
          }
        }
      },
      "description": "Relaxed lattice constants of rutile SnO2 from DFT-GGA structural optimization."
    },
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_eV"
        ],
        "properties": {
          "band_gap_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Direct band gap of SnO2 at the Γ-point from TB-mBJ electronic structure calculation."
    },
    {
      "file": "transport_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "relaxation_time_s",
          "n_type_600K",
          "p_type_600K",
          "900K"
        ],
        "properties": {
          "relaxation_time_s": {
            "type": "number",
            "unit": "s"
          },
          "n_type_600K": {
            "type": "object",
            "required": [
              "Seebeck_peak_uVK"
            ],
            "properties": {
              "Seebeck_peak_uVK": {
                "type": "number",
                "unit": "μV/K"
              }
            }
          },
          "p_type_600K": {
            "type": "object",
            "required": [
              "Seebeck_peak_uVK"
            ],
            "properties": {
              "Seebeck_peak_uVK": {
                "type": "number",
                "unit": "μV/K"
              }
            }
          },
          "900K": {
            "type": "object",
            "required": [
              "n_type",
              "p_type"
            ],
            "properties": {
              "n_type": {
                "type": "object",
                "required": [
                  "chem_pot_eV",
                  "carrier_conc_cm3",
                  "Seebeck_uVK",
                  "sigma_Ohmm",
                  "power_factor_WmK2",
                  "ZT_e"
                ],
                "properties": {
                  "chem_pot_eV": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "carrier_conc_cm3": {
                    "type": "number",
                    "unit": "cm^{-3}"
                  },
                  "Seebeck_uVK": {
                    "type": "number",
                    "unit": "μV/K"
                  },
                  "sigma_Ohmm": {
                    "type": "number",
                    "unit": "(Ωm)^{-1}"
                  },
                  "power_factor_WmK2": {
                    "type": "number",
                    "unit": "W/mK^{2}"
                  },
                  "ZT_e": {
                    "type": "number"
                  }
                }
              },
              "p_type": {
                "type": "object",
                "required": [
                  "chem_pot_eV",
                  "carrier_conc_cm3",
                  "Seebeck_uVK",
                  "sigma_Ohmm",
                  "power_factor_WmK2",
                  "ZT_e"
                ],
                "properties": {
                  "chem_pot_eV": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "carrier_conc_cm3": {
                    "type": "number",
                    "unit": "cm^{-3}"
                  },
                  "Seebeck_uVK": {
                    "type": "number",
                    "unit": "μV/K"
                  },
                  "sigma_Ohmm": {
                    "type": "number",
                    "unit": "(Ωm)^{-1}"
                  },
                  "power_factor_WmK2": {
                    "type": "number",
                    "unit": "W/mK^{2}"
                  },
                  "ZT_e": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Thermoelectric transport properties of SnO2: relaxation time, Seebeck peaks at 600 K, and optimal n-type/p-type parameters at 900 K."
    }
  ],
  "notes": "The agent must run all computational stages; no pre-computed results are provided. The experimental calibration data from Tsubota et al. are provided in the task instruction. Only electronic transport quantities are computed; lattice thermal conductivity is not required."
}
```

## How you are scored
The verifier is a hidden checker that independently inspects each of the three scored output files. Each artifact carries a fixed weight: the lattice constants constitute 10 % of the total score, the band gap 10 %, and the transport summary 80 %. For each quantity, the checker compares your reported value against a hidden gold standard using domain‑appropriate tolerances (absolute tolerances for lattice constants and band gap, relative tolerances for transport coefficients). The final reward is the weighted average of per‑artifact scores, each a number between 0 and 1. Reaching the gold within tolerance earns full credit for that artifact; performance degrades gracefully as the deviation grows. Simply copying the paper’s numbers will not satisfy the verifier because the checker expects values that result from actually running the computational pipeline described in the workflow steps. You must execute the DFT and Boltzmann transport calculations to produce the required artifacts.
