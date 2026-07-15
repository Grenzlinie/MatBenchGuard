# First-principles superconducting critical temperature and electron-phonon coupling constants for NbC under pressure

## Problem background
Transition-metal carbides such as NbC have long been studied as potential superconductors because the light carbon atoms give rise to high-frequency vibrational modes that can strongly couple to electrons. The superconducting critical temperature Tc in these materials is determined by the electron-phonon interaction, which can be separated into contributions from acoustic and optical phonon branches. Applying hydrostatic pressure compresses the crystal lattice, stiffening the phonon modes and altering the electronic density of states at the Fermi level, both of which influence Tc. It is an open question whether pressure increases or decreases Tc in NbC and how the coupling to acoustic versus optical modes evolves. This task computes the electron-phonon coupling constants and Tc from first principles for NbC at ambient pressure and under two levels of compression, providing quantitative insight into the pressure dependence of superconductivity in this compound.

## Approach
The calculations are performed using plane-wave density functional theory (DFT) and density functional perturbation theory (DFPT) within the adiabatic approximation. The system is NbC in the rock-salt (NaCl) crystal structure. Electronic structure, phonon dispersion, and electron-phonon matrix elements are computed at the experimental equilibrium volume V0 and at two compressed volumes, 0.85 V0 and 0.70 V0, corresponding to approximately 15 % and 30 % reduction in volume. The isotropically averaged Eliashberg spectral function α²F(ω) is obtained via Wannier-function interpolation. The total electron-phonon coupling constant λ is integrated from α²F(ω) as λ = 2 ∫ (dω/ω) α²F(ω). Separate integrations over the acoustic (0–14 THz) and optical (>14 THz) frequency ranges yield λ_ac and λ_op. The superconducting critical temperature Tc is then determined by solving the isotropic Eliashberg equations on the real frequency axis, using a chosen Coulomb pseudopotential μ* (e.g., 0.15). This procedure is repeated for each volume to obtain Tc as a function of compression. All calculations can be carried out with open-source electronic-structure codes such as Quantum ESPRESSO and EPW.

## Reproduction target
The goal is to produce a single JSON file containing the computed electron-phonon coupling constants and the critical temperature for the three volumes. Specifically:
- Compute λ_ac (coupling to acoustic phonons, integrated from 0 to 14 THz) and λ_op (coupling to optical phonons, integrated from >14 THz) at ambient pressure using the Eliashberg function obtained from the DFT+DFPT calculation at V0.
- Compute the isotropic Eliashberg Tc at equilibrium volume V0, at 15 % compression (0.85 V0), and at 30 % compression (0.70 V0).
- Write the results to `/app/outputs/reproduced_results.json` with exactly the structure described in the output contract: a JSON object containing the keys `lambda_ac`, `lambda_op`, and `Tc_values` (a list of three objects, each with `volume` ("V0", "0.85V0", "0.70V0") and `Tc` (in Kelvin)).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- EPW (Electron-Phonon using Wannier functions): https://epw-code.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: First-principles calculation of electronic structure, phonons, and Eliashberg function
- Role: process
- Action: Perform DFT and DFPT calculations for NbC in NaCl structure at the experimental equilibrium volume V0 and at compressed volumes 0.85V0 and 0.70V0 using Quantum ESPRESSO and EPW. Compute the electronic density of states, phonon dispersion, and the isotropically averaged Eliashberg spectral function α²F(ω) for each volume.
- Evidence: `/app/outputs/el_ph_output.log`

### Step 2: Coupling constants and Tc trend
- Role: scored (load-bearing)
- Action: From the computed α²F(ω) at V0, integrate λ = 2 ∫ (dω/ω) α²F(ω) over [0,14] THz to obtain λ_ac and over (14, ∞) THz to obtain λ_op. For each volume, solve the isotropic Eliashberg equation with a chosen Coulomb pseudopotential μ* (e.g., 0.15) to obtain Tc. Write a JSON object with keys lambda_ac, lambda_op, and Tc_values to /app/outputs/reproduced_results.json.
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: {"lambda_ac": 0.0, "lambda_op": 0.0, "Tc_values": [{"volume": "V0", "Tc": 0.0}, {"volume": "0.85V0", "Tc": 0.0}, {"volume": "0.70V0", "Tc": 0.0}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the computed electron-phonon coupling constants for acoustic and optical modes at ambient pressure, and the critical temperature Tc as a function of volume (V0, 0.85V0, 0.70V0). The Tc values will be checked for physically correct ordering.
- schema:
  - `type`: object
  - `required`: `lambda_ac`, `lambda_op`, `Tc_values`
  - `properties`:
    - `lambda_ac`:
      - `type`: number
      - `unit`: dimensionless
    - `lambda_op`:
      - `type`: number
      - `unit`: dimensionless
    - `Tc_values`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `volume`:
            - `type`: string
            - `enum`: `V0`, `0.85V0`, `0.70V0`
          - `Tc`:
            - `type`: number
            - `unit`: K
        - `required`: `volume`, `Tc`
      - `minItems`: 3
      - `maxItems`: 3

Notes: The agent may use any reasonable Coulomb pseudopotential μ* (e.g., 0.13–0.17). The scoring checks the closeness of λ values to paper-reported references and the physical ordering of Tc with compression.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "lambda_ac",
          "lambda_op",
          "Tc_values"
        ],
        "properties": {
          "lambda_ac": {
            "type": "number",
            "unit": "dimensionless"
          },
          "lambda_op": {
            "type": "number",
            "unit": "dimensionless"
          },
          "Tc_values": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "volume": {
                  "type": "string",
                  "enum": [
                    "V0",
                    "0.85V0",
                    "0.70V0"
                  ]
                },
                "Tc": {
                  "type": "number",
                  "unit": "K"
                }
              },
              "required": [
                "volume",
                "Tc"
              ]
            },
            "minItems": 3,
            "maxItems": 3
          }
        }
      },
      "description": "Contains the computed electron-phonon coupling constants for acoustic and optical modes at ambient pressure, and the critical temperature Tc as a function of volume (V0, 0.85V0, 0.70V0). The Tc values will be checked for physically correct ordering."
    }
  ],
  "notes": "The agent may use any reasonable Coulomb pseudopotential μ* (e.g., 0.13–0.17). The scoring checks the closeness of λ values to paper-reported references and the physical ordering of Tc with compression."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the `/app/outputs/reproduced_results.json` file. The verifier computes two independent scores:
- **Reference comparison**: the values of `lambda_ac` and `lambda_op` are compared to benchmark reference values (with an allowed tolerance). Meeting the reference within tolerance earns full credit.
- **Trend check**: the three `Tc` values are checked for strict monotonic ordering (all values must be positive and obey a required ordering). Fulfilling the correct trend earns full credit.
The final reward is a weighted combination of these two checks. The verifier does not inspect the intermediate log files; only the structured JSON output is scored. Reporting numbers without having performed the required first-principles calculations will not produce the correct trend and will not pass the check.
