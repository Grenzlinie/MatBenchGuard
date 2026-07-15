# First-Principles Thermodynamic and Elastic Properties of Anti-Fluorite Rb2Te

## Problem background
Rubidium telluride (Rb₂Te) is an alkali-metal chalcogenide with potential applications in photodetection. Its anti-fluorite phase properties under pressure have not been well characterized, and there is a need for reliable first‑principles predictions of its structural, elastic and thermodynamic behaviour. This task asks you to compute these properties from first principles using a standard density‑functional theory (DFT) workflow and a quasi‑harmonic Debye model.

## Approach
You will use a DFT code with the generalized gradient approximation (GGA‑PBE) to calculate total energies of the Rb₂Te anti‑fluorite unit cell at a range of volumes. From the energy‑volume data you will determine the equilibrium lattice constant and bulk modulus via the Murnaghan equation of state. The three independent elastic constants (C₁₁, C₁₂, C₄₄) will be obtained by applying volume‑conserving strains and fitting the resulting energy changes (Mehl method). With the zero‑pressure elastic constants, you will then implement the quasi‑harmonic Debye model to obtain temperature‑ and pressure‑dependent thermodynamic quantities: lattice parameter, bulk modulus, heat capacities at constant volume and pressure, thermal expansion coefficient, and Debye temperature, on a grid spanning 0–1200 K and 0–60 GPa. Finally, you will also compute the elastic constants at a set of hydrostatic pressures (0, 20, 40, 60 GPa) to determine their pressure dependence.

## Reproduction target
Produce a final results file containing the following quantities: the ground‑state lattice constant a₀ (Å), bulk modulus B₀ (GPa) and its pressure derivative B₀′, the three independent elastic constants C₁₁, C₁₂, C₄₄ at zero pressure, the derived polycrystalline moduli (shear modulus G, Young’s modulus E, Poisson ratio ν, Zener anisotropy A, and B/G ratio), the heat capacities C_V and C_P (J mol⁻¹ K⁻¹), thermal expansion coefficient α (K⁻¹), and Debye temperature Θ_D (K) at 300 K and 0 GPa, and the pressure‑dependent elastic constants at 0, 20, 40 and 60 GPa. All quantities must be obtained solely from the DFT and Debye‑model calculations described in the workflow steps, using no external experimental data.

## Assets

- Quantum ESPRESSO (open-source DFT): https://www.quantum-espresso.org/
- Elk FP-LAPW code: https://elk.sourceforge.net/
- SSSP or PseudoDojo pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- GIBBS code: https://github.com/mailsonak/GIBBS
- Anti-fluorite Rb2Te crystal structure

## Workflow steps

### Step 1: DFT total-energy vs. volume calculations
- Role: process
- Action: Perform DFT total-energy calculations on the anti-fluorite Rb2Te unit cell (space group Fm-3m) at a range of unit-cell volumes around equilibrium using an open-source DFT code (e.g., Quantum ESPRESSO with GGA-PBE pseudopotentials, or Elk). Converge with respect to k-points and plane-wave cutoff. Save the volume (in cubic Angstroms) and total energy (in eV) pairs to a CSV file.
- Evidence: `/app/outputs/e_v.csv`

### Step 2: Elastic constants at zero pressure
- Role: process
- Action: Compute the three independent elastic constants C11, C12, C44 for anti-fluorite Rb2Te at equilibrium volume using the energy approach under volume-conserving strains (the Mehl method). Use the same DFT settings as in step 1. Save the constants in JSON format.
- Evidence: `/app/outputs/elastic_zero.json`

### Step 3: Pressure-dependent elastic constants
- Role: process
- Action: For each target hydrostatic pressure (0, 20, 40, 60 GPa), perform DFT calculations with the pressure applied and compute C11, C12, C44 using the Mehl method. Save the results as an array of objects with keys pressure_GPa, C11, C12, C44.
- Evidence: `/app/outputs/elastic_pressure.json`

### Step 4: Quasi-harmonic Debye model thermodynamic calculations
- Role: process
- Action: Implement the quasi-harmonic Debye model (e.g., using the GIBBS code or custom Python implementation of the Debye model formulas) using the E(V) data from step 1 and the Poisson ratio derived from step 2. Compute the lattice parameter, bulk modulus, heat capacities at constant volume and pressure, thermal expansion coefficient, and Debye temperature on a grid of temperatures (0–1200 K) and pressures (0, 20, 40, 60 GPa). Save the output grid to a CSV file.
- Evidence: `/app/outputs/debye_output.csv`

### Step 5: Compile final summary results
- Role: scored (load-bearing)
- Action: From the intermediate files of previous steps: fit the Murnaghan equation of state to e_v.csv to obtain equilibrium lattice constant a0, bulk modulus B0, and B0'; from elastic_zero.json extract C11, C12, C44 and compute shear modulus G, Young's modulus E, Poisson ratio ν, Zener anisotropy A, and B/G ratio using standard Voigt-Reuss-Hill formulas; from debye_output.csv extract the values at T=300 K, P=0 GPa for Cv, Cp, α, and Debye temperature; and include the pressure-dependent elastic constants from elastic_pressure.json. Write all these quantities to results.json as specified.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"a0_angstrom": number, "B0_GPa": number, "B0_prime": number, "C11_GPa": number, "C12_GPa": number, "C44_GPa": number, "G_GPa": number, "E_GPa": number, "nu": number, "A": number, "B_over_G": number, "Cv_300K_JmolK": number, "Cp_300K_JmolK": number, "alpha_300K_K-1": number, "Debye_T_300K_K": number, "pressure_elastic": [{"pressure_GPa": number, "C11": number, "C12": number, "C44": number}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Aggregated final results: zero-pressure equilibrium lattice constant, bulk modulus, elastic constants, derived polycrystalline moduli, key thermodynamic quantities at 300 K and 0 GPa, and pressure-dependent elastic constants. The checker recomputes these from the raw intermediate artifacts.
- schema:
  - `type`: object
  - `required`: `a0_angstrom`, `B0_GPa`, `B0_prime`, `C11_GPa`, `C12_GPa`, `C44_GPa`, `G_GPa`, `E_GPa`, `nu`, `A`, `B_over_G`, `Cv_300K_JmolK`, `Cp_300K_JmolK`, `alpha_300K_K-1`, `Debye_T_300K_K`, `pressure_elastic`
  - `properties`:
    - `a0_angstrom`:
      - `type`: number
    - `B0_GPa`:
      - `type`: number
    - `B0_prime`:
      - `type`: number
    - `C11_GPa`:
      - `type`: number
    - `C12_GPa`:
      - `type`: number
    - `C44_GPa`:
      - `type`: number
    - `G_GPa`:
      - `type`: number
    - `E_GPa`:
      - `type`: number
    - `nu`:
      - `type`: number
    - `A`:
      - `type`: number
    - `B_over_G`:
      - `type`: number
    - `Cv_300K_JmolK`:
      - `type`: number
    - `Cp_300K_JmolK`:
      - `type`: number
    - `alpha_300K_K-1`:
      - `type`: number
    - `Debye_T_300K_K`:
      - `type`: number
    - `pressure_elastic`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `pressure_GPa`, `C11`, `C12`, `C44`
        - `properties`:
          - `pressure_GPa`:
            - `type`: number
          - `C11`:
            - `type`: number
          - `C12`:
            - `type`: number
          - `C44`:
            - `type`: number

Notes: The hidden checker reads the agent's raw intermediate files (e_v.csv, elastic_zero.json, elastic_pressure.json, debye_output.csv) and recomputes all quantities. It then compares each to the paper's reported values with tolerances that account for method-dependent spread (e.g., different DFT implementations). The agent must produce all intermediate files, but only results.json is directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "a0_angstrom",
          "B0_GPa",
          "B0_prime",
          "C11_GPa",
          "C12_GPa",
          "C44_GPa",
          "G_GPa",
          "E_GPa",
          "nu",
          "A",
          "B_over_G",
          "Cv_300K_JmolK",
          "Cp_300K_JmolK",
          "alpha_300K_K-1",
          "Debye_T_300K_K",
          "pressure_elastic"
        ],
        "properties": {
          "a0_angstrom": {
            "type": "number"
          },
          "B0_GPa": {
            "type": "number"
          },
          "B0_prime": {
            "type": "number"
          },
          "C11_GPa": {
            "type": "number"
          },
          "C12_GPa": {
            "type": "number"
          },
          "C44_GPa": {
            "type": "number"
          },
          "G_GPa": {
            "type": "number"
          },
          "E_GPa": {
            "type": "number"
          },
          "nu": {
            "type": "number"
          },
          "A": {
            "type": "number"
          },
          "B_over_G": {
            "type": "number"
          },
          "Cv_300K_JmolK": {
            "type": "number"
          },
          "Cp_300K_JmolK": {
            "type": "number"
          },
          "alpha_300K_K-1": {
            "type": "number"
          },
          "Debye_T_300K_K": {
            "type": "number"
          },
          "pressure_elastic": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "pressure_GPa",
                "C11",
                "C12",
                "C44"
              ],
              "properties": {
                "pressure_GPa": {
                  "type": "number"
                },
                "C11": {
                  "type": "number"
                },
                "C12": {
                  "type": "number"
                },
                "C44": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Aggregated final results: zero-pressure equilibrium lattice constant, bulk modulus, elastic constants, derived polycrystalline moduli, key thermodynamic quantities at 300 K and 0 GPa, and pressure-dependent elastic constants. The checker recomputes these from the raw intermediate artifacts."
    }
  ],
  "notes": "The hidden checker reads the agent's raw intermediate files (e_v.csv, elastic_zero.json, elastic_pressure.json, debye_output.csv) and recomputes all quantities. It then compares each to the paper's reported values with tolerances that account for method-dependent spread (e.g., different DFT implementations). The agent must produce all intermediate files, but only results.json is directly scored."
}
```

## How you are scored
A hidden verifier reads your raw intermediate artifacts (e_v.csv, elastic_zero.json, elastic_pressure.json, debye_output.csv) and independently recomputes every quantity that appears in results.json. It compares each recomputed value against a hidden reference that is consistent with a correct execution of the prescribed workflow. The verifier then computes a weighted average of the per‑quantity scores to produce a final reward between 0 and 1. Simply reporting numbers without producing the underlying raw artifacts, or skipping any workflow step, will result in a zero or very low reward.
