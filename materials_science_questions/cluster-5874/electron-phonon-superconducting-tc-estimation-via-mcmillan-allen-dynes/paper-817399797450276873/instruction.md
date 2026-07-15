# Electron-Phonon Coupling and Isotope Effect in Lanthanum Hydride under Pressure

## Problem background
Recently, room-temperature superconductivity was observed in the fcc phase of LaH10 under megabar pressures, and isotope effect measurements point to phonon-mediated pairing. This task aims to compute the electron-phonon coupling constant (λ), superconducting critical temperature (Tc), and isotope coefficient (α) from first principles, in order to assess whether conventional electron-phonon coupling can account for the high superconducting transition temperature.

## Approach
The approach combines density functional theory (DFT) and Eliashberg theory. First, the crystal structure of fcc LaH10 (space group Fm-3m) is relaxed at three target pressures (250, 300, and 350 GPa) using DFT with ultrasoft pseudopotentials and the PBE exchange-correlation functional. Next, density functional perturbation theory (DFPT) is employed to compute phonon spectra and the Eliashberg spectral function α²F(ω) at each pressure. For LaD10, the same electronic structure applies but the phonon frequencies are shifted because of the heavier deuterium mass. The total electron-phonon coupling constant λ is obtained by integrating α²F(ω). Using the spectral functions for both isotopes, the isotropic Eliashberg equations on the imaginary-frequency axis are solved with a Coulomb pseudopotential μ∗ = 0.2 to determine Tc for LaH10 and LaD10 at each pressure. Finally, the isotope coefficient α is derived from the Tc values and the masses of hydrogen and deuterium via the standard logarithmic mass relation.

## Reproduction target
Produce three scored artifacts:
1. The total electron-phonon coupling constant λ for fcc LaH10 (identical for LaD10) at 250, 300, and 350 GPa, written to a JSON file.
2. The superconducting critical temperatures Tc (in Kelvin) for LaH10 and LaD10 at the same three pressures, computed with μ∗ = 0.2, written to a JSON file.
3. The isotope coefficient α at each pressure and its average, derived from the Tc values and the masses of H and D, written to a JSON file.
All artifacts must be placed under /app/outputs according to the workflow steps below.

## Assets

- QUANTUM ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft pseudopotentials for La, H, D: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization of fcc LaH10
- Role: process
- Action: Relax atomic positions and cell vectors of fcc LaH10 (space group Fm-3m) at 250, 300, and 350 GPa using DFT with ultrasoft pseudopotentials and the PBE exchange-correlation functional. Ensure convergence of total energy and pressure.
- Evidence: `/app/outputs/geom_opt_summary.txt`

### Step 2: DFPT calculation of phonons and Eliashberg function
- Role: process
- Action: Perform density functional perturbation theory (DFPT) on the relaxed structures at each pressure to obtain phonon dispersions, phonon linewidths, and the Eliashberg spectral function α²F(ω).
- Evidence: `/app/outputs/dfpt_data.tar.gz`

### Step 3: Total EPC constant λ
- Role: scored (load-bearing)
- Action: From the computed Eliashberg spectral function, integrate to obtain the total electron‑phonon coupling constant λ for fcc LaH10 (identical for LaD10) at 250, 300, and 350 GPa. Write the values to JSON.
- Output file: `/app/outputs/step_03_epc_lambda.json`
- Format: json
- Contract: JSON object with keys '250_GPa', '300_GPa', '350_GPa' (float values).
- Scoring: scored by hidden verifier

### Step 4: Superconducting critical temperature Tc
- Role: scored
- Action: Using the Eliashberg spectral function α²F(ω) for LaH10 and LaD10 (different phonon frequencies due to isotope mass), solve the isotropic Eliashberg equations on the imaginary‑frequency axis with Coulomb pseudopotential μ* = 0.2 to obtain Tc for each isotope at each pressure. Write the Tc values to JSON.
- Output file: `/app/outputs/step_04_tc_values.json`
- Format: json
- Contract: JSON object with keys 'LaH10' and 'LaD10', each containing an object with keys '250_GPa', '300_GPa', '350_GPa' (float Tc in Kelvin).
- Scoring: scored by hidden verifier

### Step 5: Isotope effect coefficient α
- Role: scored
- Action: From the Tc values of LaH10 and LaD10, compute the isotope coefficient α at each pressure and the average α using the standard logarithmic mass relation. Write the results to JSON.
- Output file: `/app/outputs/step_05_isotope_coefficient.json`
- Format: json
- Contract: JSON object with keys 'alpha' (average), 'alpha_250', 'alpha_300', 'alpha_350' (float values).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_epc_lambda.json`
- `/app/outputs/step_04_tc_values.json`
- `/app/outputs/step_05_isotope_coefficient.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_epc_lambda.json
- path: `/app/outputs/step_03_epc_lambda.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electron‑phonon coupling constant λ for fcc LaH10 (identical for LaD10).
- schema:
  - `type`: object
  - `required`: `250_GPa`, `300_GPa`, `350_GPa`
  - `properties`:
    - `250_GPa`:
      - `type`: number
    - `300_GPa`:
      - `type`: number
    - `350_GPa`:
      - `type`: number

### step_04_tc_values.json
- path: `/app/outputs/step_04_tc_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Superconducting critical temperature Tc (K) for LaH10 and LaD10 with μ*=0.2.
- schema:
  - `type`: object
  - `required`: `LaH10`, `LaD10`
  - `properties`:
    - `LaH10`:
      - `type`: object
      - `required`: `250_GPa`, `300_GPa`, `350_GPa`
      - `properties`:
        - `250_GPa`:
          - `type`: number
        - `300_GPa`:
          - `type`: number
        - `350_GPa`:
          - `type`: number
    - `LaD10`:
      - `type`: object
      - `required`: `250_GPa`, `300_GPa`, `350_GPa`
      - `properties`:
        - `250_GPa`:
          - `type`: number
        - `300_GPa`:
          - `type`: number
        - `350_GPa`:
          - `type`: number

### step_05_isotope_coefficient.json
- path: `/app/outputs/step_05_isotope_coefficient.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Isotope effect coefficient α.
- schema:
  - `type`: object
  - `required`: `alpha`, `alpha_250`, `alpha_300`, `alpha_350`
  - `properties`:
    - `alpha`:
      - `type`: number
    - `alpha_250`:
      - `type`: number
    - `alpha_300`:
      - `type`: number
    - `alpha_350`:
      - `type`: number

Notes: All quantities refer to fcc LaH10 and LaD10 at 250, 300, and 350 GPa. Tc is computed with Coulomb pseudopotential μ* = 0.2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_epc_lambda.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "250_GPa",
          "300_GPa",
          "350_GPa"
        ],
        "properties": {
          "250_GPa": {
            "type": "number"
          },
          "300_GPa": {
            "type": "number"
          },
          "350_GPa": {
            "type": "number"
          }
        }
      },
      "description": "Electron‑phonon coupling constant λ for fcc LaH10 (identical for LaD10)."
    },
    {
      "file": "step_04_tc_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "LaH10",
          "LaD10"
        ],
        "properties": {
          "LaH10": {
            "type": "object",
            "required": [
              "250_GPa",
              "300_GPa",
              "350_GPa"
            ],
            "properties": {
              "250_GPa": {
                "type": "number"
              },
              "300_GPa": {
                "type": "number"
              },
              "350_GPa": {
                "type": "number"
              }
            }
          },
          "LaD10": {
            "type": "object",
            "required": [
              "250_GPa",
              "300_GPa",
              "350_GPa"
            ],
            "properties": {
              "250_GPa": {
                "type": "number"
              },
              "300_GPa": {
                "type": "number"
              },
              "350_GPa": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Superconducting critical temperature Tc (K) for LaH10 and LaD10 with μ*=0.2."
    },
    {
      "file": "step_05_isotope_coefficient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "alpha",
          "alpha_250",
          "alpha_300",
          "alpha_350"
        ],
        "properties": {
          "alpha": {
            "type": "number"
          },
          "alpha_250": {
            "type": "number"
          },
          "alpha_300": {
            "type": "number"
          },
          "alpha_350": {
            "type": "number"
          }
        }
      },
      "description": "Isotope effect coefficient α."
    }
  ],
  "notes": "All quantities refer to fcc LaH10 and LaD10 at 250, 300, and 350 GPa. Tc is computed with Coulomb pseudopotential μ* = 0.2."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact by comparing the reported numerical values against paper-reported reference results using appropriate tolerances. The three artifacts are weighted and combined to produce a final reward between 0 and 1. Simply reporting plausible numbers is not sufficient; the required computation must be executed as described in the workflow steps to produce the correct results.
