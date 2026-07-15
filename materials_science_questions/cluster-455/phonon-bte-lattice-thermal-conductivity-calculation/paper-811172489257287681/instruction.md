# Lattice thermal conductivity and thermoelectric figure of merit of monolayer ZrSe2 and HfSe2 from first-principles

## Problem background
Monolayer transition-metal dichalcogenides (TMDCs) are a well-known class of two-dimensional materials. While MoS₂-type TMDCs have been extensively studied for thermoelectrics, the CdI₂-type monolayers MX₂ (M = Zr, Hf; X = S, Se, Te) remain largely unexplored. This task computes the thermoelectric properties — electronic transport, lattice thermal conductivity, and the thermoelectric figure of merit ZT — of monolayer ZrSe₂ and HfSe₂ from first principles. The goal is to quantify how their lattice dynamics and electronic structure control their thermoelectric performance, and to compare n‑type vs p‑type doping and the two materials.

## Approach
Using density functional theory (DFT) with the PBE functional, we optimize the monolayer crystal structures and compute electronic band structures. We extract effective masses, elastic moduli, and deformation potentials to estimate acoustic-phonon-limited carrier mobilities and relaxation times. Electronic transport coefficients — Seebeck coefficient, electrical conductivity, and electronic thermal conductivity — are obtained as functions of temperature (400–1000 K) and carrier concentration via Boltzmann transport theory. Lattice thermal conductivity is computed by solving the phonon Boltzmann transport equation using harmonic and anharmonic force constants obtained from DFT supercell calculations. We then combine the electronic and lattice contributions to obtain the thermoelectric figure of merit ZT over a range of carrier concentrations and temperatures, and extract the optimal ZT for each doping type and material. Finally, we compare the two doping types and the two materials to assess relative performance trends.

## Reproduction target
Compute and report:
1. The lattice thermal conductivity (κ_l) at 300 K for monolayer ZrSe₂ and HfSe₂.
2. The optimal thermoelectric figure of merit (ZT) and the corresponding carrier concentration for n‑type and p‑type doping at 600 K and 1000 K for both materials.
3. From the optimal ZT results at 1000 K, determine whether n‑type ZT is greater than p‑type ZT for both materials, and whether HfSe₂ n‑type ZT is greater than ZrSe₂ n‑type ZT.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table
- BoltzTraP2: https://github.com/eamfitz/boltztrp2
- ShengBTE: https://www.shengbte.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Python with scientific libraries: python

## Workflow steps

### Step 1: DFT structural optimization of monolayer ZrSe2 and HfSe2
- Role: process
- Action: Perform density functional theory (PBE) structural optimization of monolayer ZrSe2 and HfSe2 in the CdI2-type structure, obtaining equilibrium lattice constants and atomic positions.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: DFT electronic structure and deformation potential parameters
- Role: process
- Action: Using the optimized structures, compute band structures, effective masses along Γ-M and M-K directions, the two-dimensional elastic modulus C2D, and deformation potential constants E_l for electrons and holes via DFT calculations with applied uniaxial strain.
- Evidence: `/app/outputs/deformation_potential_params.json`

### Step 3: Estimate carrier mobility and relaxation time
- Role: process
- Action: Using the effective masses, elastic modulus C2D, and deformation potential constants, compute the acoustic-phonon-limited carrier mobility μ and relaxation time τ at room temperature for electrons and holes via deformation potential theory.
- Evidence: `/app/outputs/mobility_relaxation_time.csv`

### Step 4: BoltzTraP electronic transport calculation
- Role: process
- Action: Perform a DFT calculation on a dense k-mesh to obtain eigenvalues, then run BoltzTraP to compute the Seebeck coefficient S, electrical conductivity over relaxation time σ/τ, and electronic thermal conductivity over relaxation time κ_e/τ as functions of temperature (400, 600, 800, 1000 K) and carrier concentration.
- Evidence: `/app/outputs/boltztrp_output.npz`

### Step 5: Phonon BTE lattice thermal conductivity calculation
- Role: process
- Action: Using optimized structures, create 5×5×1 supercells, compute second-order harmonic force constants with Phonopy and third-order anharmonic force constants with finite-difference DFT up to third nearest neighbors, then run ShengBTE to obtain lattice thermal conductivity κ_l as a function of temperature (300–1000 K).
- Evidence: `/app/outputs/kappa_l_vs_T.csv`

### Step 6: Report lattice thermal conductivity at 300 K
- Role: scored (load-bearing)
- Action: Extract the lattice thermal conductivity at 300 K for monolayer ZrSe2 and HfSe2 from the ShengBTE output and write a CSV file with columns: Material, Temperature_K, kappa_l_WmK.
- Output file: `/app/outputs/step_02_lattice_thermal_conductivity.csv`
- Format: csv
- Contract: Material (string, one of: ZrSe2, HfSe2), Temperature_K (integer, constant 300), kappa_l_WmK (float, in W/mK)
- Scoring: scored by hidden verifier

### Step 7: Compute thermoelectric figure of merit ZT and optimal values
- Role: scored (load-bearing)
- Action: For each material and doping type (n-type, p-type), combine the Seebeck coefficient, electrical conductivity (after scaling by τ), electronic thermal conductivity, and lattice thermal conductivity to compute ZT as a function of temperature (400, 600, 800, 1000 K) and carrier concentration. Extract the optimal ZT and the corresponding optimal carrier concentration at 600 K and 1000 K, and write a CSV file with columns: Material, DopingType, Temperature_K, Optimal_ZT, Optimal_carrier_concentration_cm3.
- Output file: `/app/outputs/step_03_ZT_optimal_values.csv`
- Format: csv
- Contract: Material (string), DopingType (string, 'p-type' or 'n-type'), Temperature_K (integer, 600 or 1000), Optimal_ZT (float), Optimal_carrier_concentration_cm3 (float, in cm⁻³)
- Scoring: scored by hidden verifier

### Step 8: Trend comparison
- Role: scored
- Action: Based on the optimal ZT values at 1000 K, write a text file containing two lines: the first line is 'True' if n-type optimal ZT is greater than p-type optimal ZT for both materials, else 'False'; the second line is 'True' if HfSe2 n-type optimal ZT at 1000 K is greater than ZrSe2 n-type optimal ZT at 1000 K, else 'False'.
- Output file: `/app/outputs/step_04_trend_comparison.txt`
- Format: txt
- Contract: Two lines, each either 'True' or 'False'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_lattice_thermal_conductivity.csv`
- `/app/outputs/step_03_ZT_optimal_values.csv`
- `/app/outputs/step_04_trend_comparison.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_lattice_thermal_conductivity.csv
- path: `/app/outputs/step_02_lattice_thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal conductivity at 300 K for monolayer ZrSe2 and HfSe2.
- schema:
  - `type`: table
  - `required_columns`: `Material`, `Temperature_K`, `kappa_l_WmK`
  - `units`:
    - `kappa_l_WmK`: W/mK

### step_03_ZT_optimal_values.csv
- path: `/app/outputs/step_03_ZT_optimal_values.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Optimal thermoelectric figure of merit ZT and corresponding carrier concentration for n-type and p-type doping at 600 K and 1000 K.
- schema:
  - `type`: table
  - `required_columns`: `Material`, `DopingType`, `Temperature_K`, `Optimal_ZT`, `Optimal_carrier_concentration_cm3`
  - `units`:
    - `Optimal_carrier_concentration_cm3`: cm⁻³

### step_04_trend_comparison.txt
- path: `/app/outputs/step_04_trend_comparison.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Boolean trends derived from the computed ZT: n-type vs p-type superiority and HfSe2 vs ZrSe2 for n-type doping.
- schema:
  - `type`: text
  - `lines`: `n-type ZT > p-type ZT at 1000 K for both materials`, `HfSe2 ZT > ZrSe2 ZT at 1000 K for n-type`

Notes: All quantities are computed from the first-principles pipeline. The lattice thermal conductivity is compared to the paper-reported value within tolerance; the optimal ZT is compared on a threshold-or-better basis where meeting or exceeding the reference earns full credit; the trend file is checked structurally for correctness of the two logical assertions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_lattice_thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Material",
          "Temperature_K",
          "kappa_l_WmK"
        ],
        "units": {
          "kappa_l_WmK": "W/mK"
        }
      },
      "description": "Lattice thermal conductivity at 300 K for monolayer ZrSe2 and HfSe2."
    },
    {
      "file": "step_03_ZT_optimal_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Material",
          "DopingType",
          "Temperature_K",
          "Optimal_ZT",
          "Optimal_carrier_concentration_cm3"
        ],
        "units": {
          "Optimal_carrier_concentration_cm3": "cm⁻³"
        }
      },
      "description": "Optimal thermoelectric figure of merit ZT and corresponding carrier concentration for n-type and p-type doping at 600 K and 1000 K."
    },
    {
      "file": "step_04_trend_comparison.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "lines": [
          "n-type ZT > p-type ZT at 1000 K for both materials",
          "HfSe2 ZT > ZrSe2 ZT at 1000 K for n-type"
        ]
      },
      "description": "Boolean trends derived from the computed ZT: n-type vs p-type superiority and HfSe2 vs ZrSe2 for n-type doping."
    }
  ],
  "notes": "All quantities are computed from the first-principles pipeline. The lattice thermal conductivity is compared to the paper-reported value within tolerance; the optimal ZT is compared on a threshold-or-better basis where meeting or exceeding the reference earns full credit; the trend file is checked structurally for correctness of the two logical assertions."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that independently checks each of the three scored artifacts: the lattice thermal conductivity CSV, the optimal ZT CSV, and the trend‑comparison text file. For each artifact the verifier compares your reported values against expected scientific results according to the output contract. The scores from the three artifacts are combined into a final reward between 0 and 1. Simply reporting a number is not enough — the workflow must genuinely execute the pipeline and produce the artifacts.
