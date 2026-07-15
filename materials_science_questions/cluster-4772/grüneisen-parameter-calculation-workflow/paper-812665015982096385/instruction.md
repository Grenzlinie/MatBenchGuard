# Mode Grüneisen Parameter and Anharmonicity Calculation for Barite and Celestine

## Problem background
Barite (BaSO₄) and celestine (SrSO₄) are isostructural sulfate minerals with widespread industrial and geological importance. Their crystal structures contain SO₄ tetrahedra and metal–oxygen polyhedra (M–O₁₂, where M = Ba²⁺ or Sr²⁺) whose vibrational dynamics control thermal expansion and stability. The Grüneisen parameter quantifies the sensitivity of a phonon frequency to volume change — the isobaric mode Grüneisen parameter γ_iP measures the effect of temperature-driven expansion, while the isothermal mode Grüneisen parameter γ_iT measures the effect of pressure. The intrinsic anharmonicity parameter a_i captures the non‑harmonic contributions to the frequency shift that remain after the pure volume effect is removed. Understanding how these quantities differ between M–O lattice vibrations and internal SO₄ vibrations can reveal which structural units are most responsive to external conditions. This task requires you to compute the full set of γ_iP, γ_iT, and a_i for all observed Raman modes of barite and celestine, and then evaluate whether the M–O₁₂ modes exhibit a systematically different behavior from the SO₄ modes.

## Approach
You will use temperature‑dependent Raman shift data, provided as polynomial fits ω_i(T) = x_i + y_i T + z_i T² for each Raman mode (see Asset list for the coefficients). To compute the isobaric Grüneisen parameter γ_iP, you need the molar volume as a function of temperature V(T) to construct ln(ν) vs ln(V) curves; obtain the volumetric thermal expansion data from the literature reference (Ye et al. 2019) and integrate to get V(T). Determine γ_iP from the slope of ln(ν) vs ln(V) in the high‑temperature region. For the isothermal Grüneisen parameter γ_iT, use the definition γ_iT = (K₀/ν_i)(dν_i/dP)_T, where K₀ is the ambient‑pressure bulk modulus and dν_i/dP is the mode pressure derivative; both are available from the referenced high‑pressure studies (Lee et al. 2003 for barite, Girard et al. 2019 for celestine). The intrinsic anharmonicity a_i is obtained from the slope of δ ln ν_i versus T, where δ ln ν_i is the difference between the observed frequency shift and the shift expected from the pure volume contribution. Process all modes for both minerals, write the results to grueneisen_results.json, then separate the modes into M–O₁₂ lattice and SO₄ internal groups according to their vibrational assignment (modes below ~250 cm⁻¹ are M–O₁₂, higher wavenumber modes are SO₄ internal) and decide whether the M–O group shows higher average values of γ_iP, γ_iT, and |a_i|. Output your True/False verdict in trend_check.txt.

## Reproduction target
Your target is to produce a complete table of γ_iP, γ_iT, and a_i for every Raman mode of barite and celestine, using the given polynomial frequency fits and the public literature data for thermal expansion, bulk moduli, and pressure derivatives. Then, assess the systematic difference between the M–O₁₂ lattice mode group and the SO₄ internal mode group: for each mineral, determine whether the M–O₁₂ modes exhibit consistently higher values of γ_iP, γ_iT, and |a_i| compared to the SO₄ modes. The answer must be expressed as two simple True/False statements, one for barite and one for celestine.

## Assets

- Barite high-pressure Raman data (Lee et al. 2003): 10.1088/0953-8984/15/24/103
- Celestine high-pressure Raman data (Girard et al. 2019): 10.1088/1361-648X/aaf2a2
- Barite and celestine thermoelastic data (Ye et al. 2019): 10.1007/s00269-019-01032-8
- Polynomial fit coefficients ω_i(T) = x_i + y_i T + z_i T² (Tables 3 and 4 of the paper)

## Workflow steps

### Step 1: Collect and prepare literature reference data
- Role: process
- Action: Retrieve volumetric thermal expansion data for barite and celestine from Ye et al. 2019, bulk modulus K0 and pressure derivatives dν/dP from Lee et al. 2003 (barite) and Girard et al. 2019 (celestine). Convert the thermal expansion data into a volume–temperature function V(T) and prepare arrays of temperatures spanning 25–600 °C for calculation. No scored output.
- Evidence: none

### Step 2: Compute Grüneisen and anharmonicity parameters
- Role: scored (load-bearing)
- Action: For each Raman mode of barite and celestine, using the provided polynomial fits ω_i(T) (Tables 3 and 4), the prepared V(T) relation, bulk modulus K0, and pressure derivatives dν/dP: (1) compute the isobaric mode Grüneisen parameter γ_iP from the slope of ln(ν) vs ln(V) in the high‑temperature region; (2) compute the isothermal mode Grüneisen parameter γ_iT = (K0/ν_i) (dν_i/dP)_T; (3) compute the intrinsic anharmonicity parameter a_i from the slope of δ ln ν_i versus T. Output all computed values in the structured JSON file 'grueneisen_results.json'.
- Output file: `/app/outputs/grueneisen_results.json`
- Format: json
- Contract: JSON object with top-level keys 'barite' and 'celestine', each containing an array of mode objects. Each mode object has keys: 'wavenumber(cm)' (number), 'gamma_iP' (number or null), 'gamma_iT' (number or null), 'a_i(x10^5_K^-1)' (number or null). The wavenumber is the ambient frequency of that mode.
- Scoring: scored by hidden verifier

### Step 3: Assess systematic trend between M–O and SO₄ mode groups
- Role: scored
- Action: Load 'grueneisen_results.json' and, for each mineral, separate modes into M–O₁₂ lattice vibrations and SO₄ internal modes based on the assignment given in the instruction. For each material, determine whether the M–O group exhibits higher average (or consistently higher) γ_iP, γ_iT, and absolute a_i values than the SO₄ group, and output a simple True/False answer. Write exactly two lines to 'trend_check.txt' as specified.
- Output file: `/app/outputs/trend_check.txt`
- Format: txt
- Contract: Plain text file with exactly two lines: 'Barite trend: M-O higher than SO4 (True/False)' and 'Celestine trend: M-O higher than SO4 (True/False)'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/grueneisen_results.json`
- `/app/outputs/trend_check.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### grueneisen_results.json
- path: `/app/outputs/grueneisen_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Full computed Grüneisen and anharmonicity parameters for all reported Raman modes of barite and celestine. The hidden checker compares every non-null value to the paper's Table 5 gold using an appropriate tolerance, and also uses this artifact to recompute the trend.
- schema:
  - `type`: object
  - `required`:
    - `barite`: array of mode objects
    - `celestine`: array of mode objects
  - `properties`:
    - `barite`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `wavenumber(cm)`, `gamma_iP`, `gamma_iT`, `a_i(x10^5_K^-1)`
        - `properties`:
          - `wavenumber(cm)`:
            - `type`: number
          - `gamma_iP`:
            - `type`: `number`, `null`
          - `gamma_iT`:
            - `type`: `number`, `null`
          - `a_i(x10^5_K^-1)`:
            - `type`: `number`, `null`
    - `celestine`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `wavenumber(cm)`, `gamma_iP`, `gamma_iT`, `a_i(x10^5_K^-1)`
        - `properties`:
          - `wavenumber(cm)`:
            - `type`: number
          - `gamma_iP`:
            - `type`: `number`, `null`
          - `gamma_iT`:
            - `type`: `number`, `null`
          - `a_i(x10^5_K^-1)`:
            - `type`: `number`, `null`

### trend_check.txt
- path: `/app/outputs/trend_check.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Simple True/False verdict on whether M–O₁₂ lattice modes show systematically higher γ_iP, γ_iT, and |a_i| than SO₄ internal modes for each mineral. The hidden checker recomputes the trend from 'grueneisen_results.json' and compares the agent's answer to the expected truth.
- schema:
  - `type`: text
  - `lines`: 2
  - `format_description`: Exactly two lines: 'Barite trend: M-O higher than SO4 (True/False)' and 'Celestine trend: M-O higher than SO4 (True/False)'.

Notes: The isobaric Grüneisen parameter requires high‑temperature slope determination; any reasonable numerical method is acceptable as long as the final values fall within the checker's tolerance. For modes where the paper reported two γ_iP values (e.g., 0.02/2.92), the checker will accept either within tolerance. The trend check must be consistent with the agent's own computed values; the checker will verify the trend from the submitted JSON.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "grueneisen_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "barite": "array of mode objects",
          "celestine": "array of mode objects"
        },
        "properties": {
          "barite": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "wavenumber(cm)",
                "gamma_iP",
                "gamma_iT",
                "a_i(x10^5_K^-1)"
              ],
              "properties": {
                "wavenumber(cm)": {
                  "type": "number"
                },
                "gamma_iP": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "gamma_iT": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "a_i(x10^5_K^-1)": {
                  "type": [
                    "number",
                    "null"
                  ]
                }
              }
            }
          },
          "celestine": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "wavenumber(cm)",
                "gamma_iP",
                "gamma_iT",
                "a_i(x10^5_K^-1)"
              ],
              "properties": {
                "wavenumber(cm)": {
                  "type": "number"
                },
                "gamma_iP": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "gamma_iT": {
                  "type": [
                    "number",
                    "null"
                  ]
                },
                "a_i(x10^5_K^-1)": {
                  "type": [
                    "number",
                    "null"
                  ]
                }
              }
            }
          }
        }
      },
      "description": "Full computed Grüneisen and anharmonicity parameters for all reported Raman modes of barite and celestine. The hidden checker compares every non-null value to the paper's Table 5 gold using an appropriate tolerance, and also uses this artifact to recompute the trend."
    },
    {
      "file": "trend_check.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "lines": 2,
        "format_description": "Exactly two lines: 'Barite trend: M-O higher than SO4 (True/False)' and 'Celestine trend: M-O higher than SO4 (True/False)'."
      },
      "description": "Simple True/False verdict on whether M–O₁₂ lattice modes show systematically higher γ_iP, γ_iT, and |a_i| than SO₄ internal modes for each mineral. The hidden checker recomputes the trend from 'grueneisen_results.json' and compares the agent's answer to the expected truth."
    }
  ],
  "notes": "The isobaric Grüneisen parameter requires high‑temperature slope determination; any reasonable numerical method is acceptable as long as the final values fall within the checker's tolerance. For modes where the paper reported two γ_iP values (e.g., 0.02/2.92), the checker will accept either within tolerance. The trend check must be consistent with the agent's own computed values; the checker will verify the trend from the submitted JSON."
}
```

## How you are scored
The hidden verifier independently checks both of your output files. For grueneisen_results.json, each computed parameter is compared to an expected reference using a tolerance that allows for legitimate differences arising from numerical method choices (e.g., derivative approximation, thermal expansion interpolation). For trend_check.txt, the verifier inspects your own computed values from the JSON and confirms that the True/False verdict is consistent with the data. The overall reward is a weighted combination: 70% of the score is determined by the numerical accuracy of grueneisen_results.json, and 30% by the correctness of trend_check.txt. Simply reporting the expected trend or copying numbers from a literature source is not sufficient – you must perform the computation and produce self‑consistent results.
