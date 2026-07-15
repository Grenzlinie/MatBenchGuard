# Ab initio melting curve and phonon dispersion of sodium

## Problem background
Sodium exhibits an unusual melting curve under high pressure: the melting temperature rises to a maximum in the body-centred cubic (BCC) phase and then drops sharply in the face-centred cubic (FCC) phase. The shape is believed to be driven by softening of transverse phonon modes with compression, but the role of anharmonic (phonon–phonon) interactions remains an open question. First-principles Born–Oppenheimer molecular dynamics (BOMD) can fully include such anharmonic effects and provides a direct route to compute melting points and phonon frequencies at finite temperature. This task uses BOMD simulations to reproduce the melting behaviour and phonon dispersion of sodium at high pressures, allowing a comparison with reference quasi-harmonic results.

## Approach
The core idea is to perform BOMD simulations using the open‑source Quantum ESPRESSO DFT code, which replaces the proprietary CPMD code used in the original study. With a norm‑conserving LDA pseudopotential for sodium, you will simulate BCC and FCC supercells at a range of pressures and temperatures under NVT conditions. From the ionic trajectories you detect melting by the onset of linear growth in the mean‑square displacement (MSD) and optionally confirm it with the Raveché–Mountain–Streett (RMS) criterion based on the pair correlation function. Additionally, you compute the one‑phonon dynamic structure factor S(q,ω) from selected trajectories and extract phonon frequencies as peak positions. The obtained melting points and phonon frequencies will be compared against reference quasi‑harmonic DFT calculations.

## Reproduction target
Using BOMD, determine the melting temperatures of sodium at a minimum of three pressures that span both BCC and FCC phases (for example, a low‑pressure point, a point near the BCC melting maximum, and a high‑pressure FCC point). Report each melting temperature with an estimated accuracy (typically ±50–100 K). In addition, compute the phonon frequencies for the BCC phase at 64.5 GPa and for the FCC phase at 67 GPa and 99.5 GPa. Extract longitudinal and transverse mode frequencies at selected q‑points along the Γ–H direction (BCC) and Γ–K direction (FCC). Save all results as JSON files following the specified schemas.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Troullier–Martins LDA pseudopotential for Na: SSSP efficiency library or PseudoDojo

## Workflow steps

### Step 1: BOMD simulations for melting detection
- Role: process
- Action: Run Born–Oppenheimer molecular dynamics (BOMD) simulations using Quantum ESPRESSO for BCC (4×4×4, 128 atoms) and FCC (3×3×3, 108 atoms) sodium at a range of pressures and temperatures. Use a norm-conserving LDA pseudopotential for Na, plane-wave cutoff 20 Ry, Gamma‑point Brillouin‑zone integration, time step 3.6 fs (BCC) / 2.4 fs (FCC), NVT ensemble with a chain of four Nosé–Hoover thermostats. Generate ionic trajectories (positions vs time) for subsequent melting analysis.
- Evidence: none

### Step 2: Melting temperature determination
- Role: scored (load-bearing)
- Action: From the melting simulation trajectories, compute the mean‑square displacement ⟨u²(t)⟩ and optionally the pair correlation function g(r). Detect melting by the onset of linear diffusion (MSD criterion) and optionally confirm with the RMS criterion. Determine melting temperature intervals (accuracy ±50–100 K) for the following pressures: 27.5 GPa, 64.5 GPa, and 99.5 GPa. Report the results in melting_points.json.
- Output file: `/app/outputs/melting_points.json`
- Format: json
- Contract: object with pressure (number, GPa) as keys; each value is an object with keys 'melting_temperature_K' (number) and 'error_K' (number). Example: {"64.5": {"melting_temperature_K": 850, "error_K": 50}}
- Scoring: scored by hidden verifier

### Step 3: BOMD simulations for dynamic structure factor
- Role: process
- Action: Run additional BOMD simulations for BCC (4×4×4, 128 atoms) at p=64.5 GPa, T=400 K and T=700 K; and for FCC (4×4×4, 256 atoms) at p=67 GPa, T=500 K and p=99.5 GPa, T=250 K. Use the same DFT parameters and pseudopotential as in the melting simulations. Generate ionic trajectories for dynamic structure factor calculation.
- Evidence: none

### Step 4: Phonon frequency extraction from dynamic structure factor
- Role: scored (load-bearing)
- Action: From the DCF simulation trajectories, compute the one‑phonon dynamic structure factor S(q,ω). Identify phonon frequencies as peak positions for selected q‑points along high‑symmetry directions: [100] (Γ–H) for BCC, with q‑points (0.25,0,0), (0.5,0,0), (0.75,0,0), (1,0,0); [110] (Γ–K) for FCC, with q‑points (0.25,0.25,0), (0.5,0.5,0), (0.75,0.75,0), (1,1,0). Extract frequencies for longitudinal and transverse modes. Report the frequencies in phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: array of objects; each object has keys: 'pressure_GPa' (number), 'phase' (string, one of 'bcc','fcc'), 'q_point' (list of 3 numbers in units of reciprocal lattice vectors), 'mode' (string, one of 'longitudinal','transverse'), 'frequency_cm1' (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/melting_points.json`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### melting_points.json
- path: `/app/outputs/melting_points.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mapping pressure (GPa) to melting temperature (K) with error estimate. Checked against paper-reported melting points within tolerance.
- schema:
  - `type`: object
  - `additionalProperties`:
    - `type`: object
    - `properties`:
      - `melting_temperature_K`:
        - `type`: number
      - `error_K`:
        - `type`: number
    - `required`: `melting_temperature_K`, `error_K`

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies at selected (pressure, q-point) points from dynamic structure factor. Checked against quasi‑harmonic frequencies from the paper within tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `pressure_GPa`:
        - `type`: number
      - `phase`:
        - `type`: string
        - `enum`: `bcc`, `fcc`
      - `q_point`:
        - `type`: array
        - `items`:
          - `type`: number
        - `minItems`: 3
        - `maxItems`: 3
      - `mode`:
        - `type`: string
        - `enum`: `longitudinal`, `transverse`
      - `frequency_cm1`:
        - `type`: number
    - `required`: `pressure_GPa`, `phase`, `q_point`, `mode`, `frequency_cm1`

Notes: The agent must re‑run all BOMD simulations; no pre‑computed trajectories are provided. The checker compares the reported melting temperatures and phonon frequencies against the paper's hidden gold using tolerances derived from simulation precision.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "melting_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "additionalProperties": {
          "type": "object",
          "properties": {
            "melting_temperature_K": {
              "type": "number"
            },
            "error_K": {
              "type": "number"
            }
          },
          "required": [
            "melting_temperature_K",
            "error_K"
          ]
        }
      },
      "description": "Mapping pressure (GPa) to melting temperature (K) with error estimate. Checked against paper-reported melting points within tolerance."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "pressure_GPa": {
              "type": "number"
            },
            "phase": {
              "type": "string",
              "enum": [
                "bcc",
                "fcc"
              ]
            },
            "q_point": {
              "type": "array",
              "items": {
                "type": "number"
              },
              "minItems": 3,
              "maxItems": 3
            },
            "mode": {
              "type": "string",
              "enum": [
                "longitudinal",
                "transverse"
              ]
            },
            "frequency_cm1": {
              "type": "number"
            }
          },
          "required": [
            "pressure_GPa",
            "phase",
            "q_point",
            "mode",
            "frequency_cm1"
          ]
        }
      },
      "description": "Phonon frequencies at selected (pressure, q-point) points from dynamic structure factor. Checked against quasi‑harmonic frequencies from the paper within tolerance."
    }
  ],
  "notes": "The agent must re‑run all BOMD simulations; no pre‑computed trajectories are provided. The checker compares the reported melting temperatures and phonon frequencies against the paper's hidden gold using tolerances derived from simulation precision."
}
```

## How you are scored
Each output file is evaluated independently by a hidden verifier. Your reported melting temperatures in `melting_points.json` are compared against reference values from the original study; your phonon frequencies in `phonon_frequencies.json` are compared against reference quasi‑harmonic phonon frequencies. The closer your numbers are to the reference (within acceptable tolerances), the higher your score; meeting the reference earns full credit. Simply reporting numbers without executing the required BOMD simulations is insufficient, because the verifier expects results that reflect actual molecular dynamics runs.
