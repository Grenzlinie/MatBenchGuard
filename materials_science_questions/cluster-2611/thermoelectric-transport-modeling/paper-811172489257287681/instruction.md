# First-Principles Thermoelectric Figure of Merit for Monolayer ZrSe₂ and HfSe₂

## Problem background
Thermoelectric materials convert heat into electricity; their efficiency is captured by the dimensionless figure of merit ZT = S²σT/(κₑ + κₗ), where S is the Seebeck coefficient, σ electrical conductivity, T temperature, and κₑ (κₗ) the electronic (lattice) thermal conductivity. Two-dimensional monolayer transition‑metal dichalcogenides (TMDCs) have attracted interest for thermoelectrics because phonon transport can be very different from the bulk. Most previous efforts focused on MoS₂‑type monolayers (e.g. MoSe₂, WSe₂) that exhibit high lattice thermal conductivity, limiting their ZT. TMDCs can also adopt the CdI₂‑type crystal structure, and recent work suggests that such monolayers (ZrSe₂, HfSe₂) may possess exceptionally low κₗ due to strong coupling between acoustic and low‑frequency optical phonon modes. The task is to compute both the electronic and phononic transport properties of monolayer ZrSe₂ and HfSe₂ from first principles and to evaluate their thermoelectric figure of merit under different doping conditions and temperatures.

## Approach
The pipeline combines density functional theory (DFT) with Boltzmann transport equations. Electronic structures (band gap, band dispersion, effective masses, deformation potential constants, and the 2D elastic modulus) are obtained with the PBE functional and PAW pseudopotentials. Carrier mobilities and relaxation times are then estimated via deformation potential theory assuming acoustic‑phonon scattering. Phonon transport is treated by constructing second‑order force constants via finite‑displacement supercell calculations (Phonopy) and third‑order force constants up to third nearest neighbours; the phonon Boltzmann transport equation is solved iteratively (ShengBTE) to obtain lattice thermal conductivity κₗ as a function of temperature. Electronic transport coefficients (S, σ/τ, κₑ/τ) across a carrier concentration range (10¹⁸–10²⁰ cm⁻³) are computed from the DFT band structure using BoltzTraP2 under the constant relaxation‑time approximation. Finally, the absolute electrical conductivity σ = (σ/τ)×τ and electronic thermal conductivity κₑ = (κₑ/τ)×τ are formed, and ZT = S²σT/(κₑ+κₗ) is evaluated. This workflow is applied to both monolayer ZrSe₂ and HfSe₂, contrasting n‑type and p‑type doping at 600 K and 800 K.

## Reproduction target
Using the above methodology, compute and report in a structured JSON file:

1. Lattice thermal conductivity κₗ at 300 K for monolayer ZrSe₂ and HfSe₂.
2. Maximum thermoelectric figure of merit ZT for n‑type and p‑type doping at 600 K and at 800 K for both materials.
3. The optimal carrier concentrations (cm⁻³) that yield those ZT maxima at 600 K.
4. Verify the structural relations: n‑type ZT exceeds p‑type ZT for each material at both temperatures, and at 800 K the maximal n‑type ZT of HfSe₂ is larger than that of ZrSe₂.

All values must be produced from the full DFT + Boltzmann transport pipeline; look‑up or reproduction of tabulated numbers from the literature without executing the computations is not the objective.

## Assets

- Quantum ESPRESSO (or GPAW/ABINIT): https://www.quantum-espresso.org/
- PBE PAW pseudopotentials for Zr, Hf, Se (SSSP library): https://www.materialscloud.org/discover/sssp/table
- BoltzTraP2: https://www.boltztrapp.org/
- ShengBTE: https://www.shengbte.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Third-order force constant calculation script (thirdorder.py from ShengBTE): https://www.shengbte.org/

## Workflow steps

### Step 1: DFT structural optimization and electronic structure
- Role: process
- Action: Perform geometry optimization and electronic structure calculation for monolayer ZrSe2 and HfSe2 using PBE functional and PAW pseudopotentials. Obtain optimized lattice constants, band structure, carrier effective masses, deformation potential constants, and 2D elastic modulus.
- Evidence: `/app/outputs/dft_output.tar.gz`

### Step 2: Deformation potential relaxation time estimation
- Role: process
- Action: Using effective masses, deformation potentials, and elastic modulus, compute hole and electron carrier mobilities and relaxation times at 300 K via deformation potential theory under acoustic-phonon scattering assumption.
- Evidence: `/app/outputs/mobility_relaxation.json`

### Step 3: Supercell DFT for interatomic force constants
- Role: process
- Action: Using the optimized unit cell, create supercells and compute second-order interatomic force constants via finite displacements (Phonopy) and third-order force constants up to third nearest neighbors.
- Evidence: none

### Step 4: ShengBTE phonon transport calculation
- Role: process
- Action: Solve phonon Boltzmann transport equation using ShengBTE with the second and third order force constants to obtain lattice thermal conductivity as a function of temperature. Extract κ_l at 300 K.
- Evidence: none

### Step 5: BoltzTraP electronic transport simulation
- Role: process
- Action: Run BoltzTraP with the DFT band structure to obtain Seebeck coefficient S, electrical conductivity scaled by relaxation time σ/τ, and electronic thermal conductivity scaled by relaxation time κ_e/τ as functions of carrier concentration (1e18 to 1e20 cm⁻³) at 600 K and 800 K.
- Evidence: none

### Step 6: Figure of merit evaluation and final reporting
- Role: scored (load-bearing)
- Action: Combine electronic and phononic transport coefficients and relaxation times to compute absolute electrical conductivity σ, electronic thermal conductivity κ_e, and figure of merit ZT. Determine maximum ZT for n-type and p-type doping at 600 K and 800 K for both materials, and the optimal carrier concentrations. Also report lattice thermal conductivity κ_l at 300 K. Write all results to final_results.json.
- Output file: `/app/outputs/final_results.json`
- Format: json
- Contract: type=object; required=['ZrSe2_kappa_l_300K', 'HfSe2_kappa_l_300K', 'ZrSe2_ZT_n_max_600K', 'ZrSe2_ZT_p_max_600K', 'HfSe2_ZT_n_max_600K', 'HfSe2_ZT_p_max_600K', 'n_opt_n_type_600K', 'n_opt_p_type_600K', 'ZrSe2_ZT_n_max_800K', 'ZrSe2_ZT_p_max_800K', 'HfSe2_ZT_n_max_800K', 'HfSe2_ZT_p_max_800K']; properties={'ZrSe2_kappa_l_300K': {'type': 'number', 'unit': 'W/mK'}, 'HfSe2_kappa_l_300K': {'type': 'number', 'unit': 'W/mK'}, 'ZrSe2_ZT_n_max_600K': {'type': 'number', 'unit': 'dimensionless'}, 'ZrSe2_ZT_p_max_600K': {'type': 'number', 'unit': 'dimensionless'}, 'HfSe2_ZT_n_max_600K': {'type': 'number', 'unit': 'dimensionless'}, 'HfSe2_ZT_p_max_600K': {'type': 'number', 'unit': 'dimensionless'}, 'n_opt_n_type_600K': {'type': 'number', 'unit': 'cm^{-3}'}, 'n_opt_p_type_600K': {'type': 'number', 'unit': 'cm^{-3}'}, 'ZrSe2_ZT_n_max_800K': {'type': 'number', 'unit': 'dimensionless'}, 'ZrSe2_ZT_p_max_800K': {'type': 'number', 'unit': 'dimensionless'}, 'HfSe2_ZT_n_max_800K': {'type': 'number', 'unit': 'dimensionless'}, 'HfSe2_ZT_p_max_800K': {'type': 'number', 'unit': 'dimensionless'}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_results.json
- path: `/app/outputs/final_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermoelectric figure of merit and lattice thermal conductivity computed from first-principles for monolayer ZrSe2 and HfSe2.
- schema:
  - `type`: object
  - `required`: `ZrSe2_kappa_l_300K`, `HfSe2_kappa_l_300K`, `ZrSe2_ZT_n_max_600K`, `ZrSe2_ZT_p_max_600K`, `HfSe2_ZT_n_max_600K`, `HfSe2_ZT_p_max_600K`, `n_opt_n_type_600K`, `n_opt_p_type_600K`, `ZrSe2_ZT_n_max_800K`, `ZrSe2_ZT_p_max_800K`, `HfSe2_ZT_n_max_800K`, `HfSe2_ZT_p_max_800K`
  - `properties`:
    - `ZrSe2_kappa_l_300K`:
      - `type`: number
      - `unit`: W/mK
    - `HfSe2_kappa_l_300K`:
      - `type`: number
      - `unit`: W/mK
    - `ZrSe2_ZT_n_max_600K`:
      - `type`: number
      - `unit`: dimensionless
    - `ZrSe2_ZT_p_max_600K`:
      - `type`: number
      - `unit`: dimensionless
    - `HfSe2_ZT_n_max_600K`:
      - `type`: number
      - `unit`: dimensionless
    - `HfSe2_ZT_p_max_600K`:
      - `type`: number
      - `unit`: dimensionless
    - `n_opt_n_type_600K`:
      - `type`: number
      - `unit`: cm^{-3}
    - `n_opt_p_type_600K`:
      - `type`: number
      - `unit`: cm^{-3}
    - `ZrSe2_ZT_n_max_800K`:
      - `type`: number
      - `unit`: dimensionless
    - `ZrSe2_ZT_p_max_800K`:
      - `type`: number
      - `unit`: dimensionless
    - `HfSe2_ZT_n_max_800K`:
      - `type`: number
      - `unit`: dimensionless
    - `HfSe2_ZT_p_max_800K`:
      - `type`: number
      - `unit`: dimensionless

Notes: All values are produced by the complete DFT+Boltzmann transport pipeline and are compared to hidden reference values from the literature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "ZrSe2_kappa_l_300K",
          "HfSe2_kappa_l_300K",
          "ZrSe2_ZT_n_max_600K",
          "ZrSe2_ZT_p_max_600K",
          "HfSe2_ZT_n_max_600K",
          "HfSe2_ZT_p_max_600K",
          "n_opt_n_type_600K",
          "n_opt_p_type_600K",
          "ZrSe2_ZT_n_max_800K",
          "ZrSe2_ZT_p_max_800K",
          "HfSe2_ZT_n_max_800K",
          "HfSe2_ZT_p_max_800K"
        ],
        "properties": {
          "ZrSe2_kappa_l_300K": {
            "type": "number",
            "unit": "W/mK"
          },
          "HfSe2_kappa_l_300K": {
            "type": "number",
            "unit": "W/mK"
          },
          "ZrSe2_ZT_n_max_600K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "ZrSe2_ZT_p_max_600K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "HfSe2_ZT_n_max_600K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "HfSe2_ZT_p_max_600K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "n_opt_n_type_600K": {
            "type": "number",
            "unit": "cm^{-3}"
          },
          "n_opt_p_type_600K": {
            "type": "number",
            "unit": "cm^{-3}"
          },
          "ZrSe2_ZT_n_max_800K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "ZrSe2_ZT_p_max_800K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "HfSe2_ZT_n_max_800K": {
            "type": "number",
            "unit": "dimensionless"
          },
          "HfSe2_ZT_p_max_800K": {
            "type": "number",
            "unit": "dimensionless"
          }
        }
      },
      "description": "Thermoelectric figure of merit and lattice thermal conductivity computed from first-principles for monolayer ZrSe2 and HfSe2."
    }
  ],
  "notes": "All values are produced by the complete DFT+Boltzmann transport pipeline and are compared to hidden reference values from the literature."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently inspects `final_results.json`. Each required field is compared against reference expectations (numerical values with appropriate tolerance for computational reproducibility, and structural relations). The final reward is a weighted combination of the successes on every scored field. Simply writing numbers that match the literature without running the full computational pipeline will not yield a high score; the verifier assumes the values originate from the instructed workflow and cross‑checks them accordingly. No additional human judgement is applied.
