# Detecting structural crossover in supercritical water across the Frenkel line

## Problem background
Water at supercritical pressures was long assumed to exhibit only smooth, gradual changes in its properties. Recently, a dynamical crossover called the Frenkel line (FL) was introduced, dividing the supercritical state into two regimes: one where molecules retain solid-like oscillatory motion between diffusive jumps, and a higher-temperature regime where motion becomes purely diffusive. This raises the question: does a structural crossover accompany the dynamical transition at the FL? In other words, at pressures up to several tens of kbar, do the oxygen-oxygen pair distribution functions (PDFs) undergo a marked change in their peak features at the FL temperature? Answering this question will deepen understanding of water's phase diagram far beyond the critical point.

## Approach
The investigation is carried out using classical molecular dynamics (MD) simulations with the TIP4P/2005 water potential, a rigid water model known for its accuracy at high pressure and temperature. For each of five supercritical pressures (0.5, 1.0, 2.5, 5.0, and 10.0 kbar), simulations of a large system (32768 water molecules) are run at several temperatures that bracket the expected Frenkel line. Short NPT equilibration is followed by NVE production, from which the oxygen-oxygen pair distribution function g(r) is computed. The g(r) profiles are then analyzed to extract the positions and heights of the first, second, third, and (where it emerges) a new second peak. At lower pressures (0.5–2.5 kbar) the structural crossover, if present, is detected by the emergence of a new second peak that becomes more prominent than the original second peak. At higher pressures (5.0 and 10.0 kbar) the crossover is identified by tracking the position of the third peak and finding the temperature at which its radial position reaches a minimum. This method yields a crossover temperature for each pressure, which can be compared with the known dynamical FL temperatures.

## Reproduction target
Run the full MD simulation pipeline as specified and produce a single JSON file `crossover_results.json`. This file must contain, for every simulated state point, the pressure, temperature, and the extracted PDF peak positions and heights. It must also contain a summary that, for each pressure, reports the determined structural crossover temperature and the method used (either "new_peak_prominent" or "third_peak_minimum"). The output schema is given in the output contract. Reaching the correct crossover temperature with the specified method at each pressure is the primary goal.

## Assets

- TIP4P/2005 water force field parameters: 10.1063/1.2121685
- MD simulation package (LAMMPS or DL_POLY): https://www.lammps.org

## Workflow steps

### Step 1: Run TIP4P/2005 MD simulations
- Role: process
- Action: For each of the five pressures (0.5, 1.0, 2.5, 5.0, 10.0 kbar), run MD simulations of 32768 water molecules using the TIP4P/2005 potential. At each pressure, choose at least five temperatures spanning 300–1000 K to bracket the Frenkel line. Perform 30 ps NPT equilibration followed by 170 ps NVE production for each state point. Save the trajectory files.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute O-O pair distribution functions
- Role: process
- Action: From the NVE production trajectories, compute the oxygen-oxygen pair distribution function g(r) at each state point using a bin width no larger than 0.01 Å and up to a distance of at least 10 Å. Save g(r) profiles.
- Evidence: `/app/outputs/pdf_computation.log`

### Step 3: Extract peak features and determine structural crossover
- Role: scored (load-bearing)
- Action: For each (P,T) state point, extract from g(r) the first, second, third, and, where discernible, the new second peak positions (Å) and the first peak height (g_max-1). Then, for each pressure, determine the structural crossover temperature: for 0.5, 1.0, 2.5 kbar, identify the temperature at which the new second peak becomes more prominent than the original second peak; for 5.0 and 10.0 kbar, find the temperature at which the third peak position is minimal. Write all per-state-point peak data and a crossover summary to crossover_results.json.
- Output file: `/app/outputs/crossover_results.json`
- Format: json
- Contract: {"state_points": [{"pressure_kbar": number, "temperature_K": number, "peaks": [{"peak_id": "first|second|third|new_second", "position_A": number, "height": number}]}], "crossover_summary": [{"pressure_kbar": number, "crossover_temperature_K": number, "crossover_method": "new_peak_prominent|third_peak_minimum"}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/crossover_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### crossover_results.json
- path: `/app/outputs/crossover_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: All per-state-point PDF peak positions/heights and per-pressure crossover temperature and method.
- schema:
  - `type`: object
  - `required`: `state_points`, `crossover_summary`
  - `state_points`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `pressure_kbar`, `temperature_K`, `peaks`
      - `properties`:
        - `pressure_kbar`:
          - `type`: number
        - `temperature_K`:
          - `type`: number
        - `peaks`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `peak_id`, `position_A`, `height`
            - `properties`:
              - `peak_id`:
                - `type`: string
                - `enum`: `first`, `second`, `third`, `new_second`
              - `position_A`:
                - `type`: number
              - `height`:
                - `type`: number
  - `crossover_summary`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `pressure_kbar`, `crossover_temperature_K`, `crossover_method`
      - `properties`:
        - `pressure_kbar`:
          - `type`: number
        - `crossover_temperature_K`:
          - `type`: number
        - `crossover_method`:
          - `type`: string
          - `enum`: `new_peak_prominent`, `third_peak_minimum`

Notes: The agent must run the full MD simulation pipeline; no pre-computed data is provided. The checker will compare the reported crossover temperatures to the expected Frenkel line values (hidden) and verify self-consistency with the peak data, scoring on a threshold-or-better basis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "crossover_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "state_points",
          "crossover_summary"
        ],
        "state_points": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "pressure_kbar",
              "temperature_K",
              "peaks"
            ],
            "properties": {
              "pressure_kbar": {
                "type": "number"
              },
              "temperature_K": {
                "type": "number"
              },
              "peaks": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "peak_id",
                    "position_A",
                    "height"
                  ],
                  "properties": {
                    "peak_id": {
                      "type": "string",
                      "enum": [
                        "first",
                        "second",
                        "third",
                        "new_second"
                      ]
                    },
                    "position_A": {
                      "type": "number"
                    },
                    "height": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          }
        },
        "crossover_summary": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "pressure_kbar",
              "crossover_temperature_K",
              "crossover_method"
            ],
            "properties": {
              "pressure_kbar": {
                "type": "number"
              },
              "crossover_temperature_K": {
                "type": "number"
              },
              "crossover_method": {
                "type": "string",
                "enum": [
                  "new_peak_prominent",
                  "third_peak_minimum"
                ]
              }
            }
          }
        }
      },
      "description": "All per-state-point PDF peak positions/heights and per-pressure crossover temperature and method."
    }
  ],
  "notes": "The agent must run the full MD simulation pipeline; no pre-computed data is provided. The checker will compare the reported crossover temperatures to the expected Frenkel line values (hidden) and verify self-consistency with the peak data, scoring on a threshold-or-better basis."
}
```

## How you are scored
A hidden verifier automatically inspects your `crossover_results.json`. First, it performs a self-consistency check: it recomputes the crossover temperature from your own submitted peak data using the same rule you were asked to apply, and verifies that it matches your reported crossover summary. Then it compares your crossover temperatures to a set of hidden reference FL temperatures, using a tolerance that accounts for expected run-to-run variation. You receive full credit when your result is within tolerance of the reference; credit degrades as the deviation grows. The verifier also checks that the correct crossover method was used for each pressure. To succeed, you must faithfully execute the entire MD workflow and apply the peak analysis rules correctly.
