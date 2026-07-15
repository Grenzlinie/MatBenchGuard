# Xenon/Krypton Separation Prediction in MFM Metal-Organic Frameworks using GCMC and Geometric Analysis

## Problem background
The MFM family of copper paddlewheel-based, isoreticular metal-organic frameworks (MFM-126, 127, 128, 136, 137, 138) has already shown promising performance for gas separations such as CO₂/CH₄ and CO₂/N₂. Expanding their application to xenon/krypton (Xe/Kr) separation is attractive because separating these two noble gases is critical in industrial air processing and in the revalorisation of fission products from nuclear fuel reprocessing. This study uses computational methods to predict the structural and adsorption properties of these MOFs for Xe/Kr mixtures, aiming to quantify their potential as selective adsorbents. Your task is to reproduce the geometric pore characterisation, the Xe/Kr selectivity under several industrially relevant conditions, and the thermodynamic binding metrics (heats of adsorption and Henry constants) for all six MFM frameworks.

## Approach
The computational approach consists of two main stages: (1) geometric pore analysis using the Zeo++ software, and (2) molecular simulations using the RASPA package. All work is performed on the crystal structures of the six MFM MOFs provided as public CIF files (see Assets).

**Geometric analysis (Zeo++):** Zeo++ builds a Voronoi network of the framework and samples it with spherical probes. You will compute pore limiting diameter (PLD), largest cavity diameter (LCD), total geometric surface area (using a probe radius corresponding to N₂ kinetic diameter, 3.64 Å), accessible volume with a zero-radius probe, and helium void fraction. These descriptors quantify the pore architecture relevant for gas adsorption.

**Molecular simulations (RASPA):** Grand Canonical Monte Carlo (GCMC) simulations are used to obtain Xe and Kr adsorption isotherms. Simulations are run for both single-component gases and binary mixtures (50/50 and 20/80 Xe/Kr) at two temperatures (273 K and 298 K) over a pressure range of 0.01–10 bar. Framework atoms are described with Lennard-Jones parameters from Dreiding force field, except for copper which uses Universal Force Field (UFF) parameters. Guest species are modelled with published parameters: Hirschfelder et al. for Xe and Talu–Myers for Kr. From the binary mixture uptake data, Xe/Kr selectivity is computed via the formula S = (q_Xe * y_Kr) / (q_Kr * y_Xe) at the specific pressures 0.01 bar and 10 bar.

Additionally, Widom insertion simulations (100,000 cycles) at 298 K provide infinite dilution heats of adsorption (Qst) for Xe and Kr, and Henry constants K_H for both gases. Henry selectivity is obtained as K_H_Xe / K_H_Kr.

## Reproduction target
Your goal is to compute the following three sets of quantities and write them to the specified JSON files under `/app/outputs`.

1. **Structural properties** (in `structural_properties.json`): For each of the six MOFs (MFM-126, MFM-127, MFM-128, MFM-136, MFM-137, MFM-138), report pore limiting diameter (Å), largest cavity diameter (Å), the ratio LCD/PLD, total geometric surface area (m²/g), probe-occupiable volume with zero-radius probe (cm³/g), and helium void fraction.

2. **Xe/Kr selectivity** (in `selectivity_summary.json`): Report the computed Xe/Kr selectivity for eight specific conditions, each identified by a key: 50/50 mixture at 273 K, 0.01 bar; 50/50 mixture at 273 K, 10 bar; 50/50 mixture at 298 K, 0.01 bar; 50/50 mixture at 298 K, 10 bar; 20/80 mixture at 273 K, 0.01 bar; 20/80 mixture at 273 K, 10 bar; 20/80 mixture at 298 K, 0.01 bar; 20/80 mixture at 298 K, 10 bar. For each key, provide an object mapping each MOF name to its selectivity value.

3. **Thermodynamic properties** (in `thermodynamic_properties.json`): Provide infinite dilution heats of adsorption (Qst) for Xe and Kr (kJ/mol) at 298 K, Henry constants K_H for Xe and Kr (units mol·kg⁻¹·Pa⁻¹ ×10⁻⁵) at 298 K, and Henry selectivity (K_H_Xe / K_H_Kr). Each of these five quantities is an object mapping MOF name to the computed value.

## Assets

- Zeo++: https://github.com/hpcmin-ucsd/ZeoPP
- RASPA: https://github.com/numat/RASPA2
- MFM crystal structures: 10.1039/C8SC04097J

## Workflow steps

### Step 1: Zeo++ geometric pore characterization
- Role: scored
- Action: Run Zeo++ on each of the six MFM frameworks (MFM-126,127,128,136,137,138) using appropriate probe radii: N₂ kinetic diameter (3.64 Å) for surface area, zero radius for accessible volume, and helium radius for void fraction. Compute pore limiting diameter (PLD), largest cavity diameter (LCD), total geometric surface area (sum of accessible and non-accessible), probe-occupiable volume (zero-radius probe), and helium void fraction. Write the results to structural_properties.json.
- Output file: `/app/outputs/structural_properties.json`
- Format: json
- Contract: Array of 6 JSON objects, each with keys: 'mof' (string, MOF name), 'pld' (float, pore limiting diameter in Angstrom), 'lcd' (float, largest cavity diameter in Angstrom), 'lcd_pl' (float, LCD/PLD ratio), 'total_sa' (float, total geometric surface area in m²/g), 'volume' (float, probe-occupiable volume with zero-radius probe in cm³/g), 'void_fraction' (float, helium void fraction).
- Scoring: scored by hidden verifier

### Step 2: GCMC selectivity computation
- Role: scored (load-bearing)
- Action: Using RASPA, perform Grand Canonical Monte Carlo simulations for Xe and Kr single-component isotherms and for 50/50 and 20/80 binary mixture isotherms at 273 K and 298 K, over pressures from 0.01 bar to 10 bar. Use Dreiding+UFF force field for framework atoms (UFF for Cu) and published guest parameters (Hirschfelder for Xe, Talu–Myers for Kr). From the binary mixture uptake data, compute Xe/Kr selectivity at 0.01 bar and 10 bar for each combination of temperature and gas mixture. Output the resulting selectivities as selectivity_summary.json.
- Output file: `/app/outputs/selectivity_summary.json`
- Format: json
- Contract: JSON object with exactly 8 keys: 'S_50_50_273_0.01', 'S_50_50_273_10', 'S_50_50_298_0.01', 'S_50_50_298_10', 'S_20_80_273_0.01', 'S_20_80_273_10', 'S_20_80_298_0.01', 'S_20_80_298_10'. Each key maps to an object whose keys are MOF names (e.g. 'MFM-126') and values are the computed Xe/Kr selectivity (float).
- Scoring: scored by hidden verifier

### Step 3: Widom insertion for heats and Henry constants
- Role: scored (load-bearing)
- Action: Perform Widom insertion simulations (100,000 cycles) at 298 K in RASPA for each MOF to obtain infinite dilution heats of adsorption (Qst) for Xe and Kr, and Henry constants K_H for both gases. Compute Henry selectivity as K_H_Xe / K_H_Kr. Write the results to thermodynamic_properties.json.
- Output file: `/app/outputs/thermodynamic_properties.json`
- Format: json
- Contract: JSON object with keys: 'Qst_Xe' (object mapping MOF name to float, kJ/mol), 'Qst_Kr' (object mapping MOF name to float, kJ/mol), 'K_H_Xe' (object mapping MOF name to float, units mol·kg⁻¹·Pa⁻¹ ×10⁻⁵), 'K_H_Kr' (object mapping MOF name to float, same units), 'Henry_selectivity' (object mapping MOF name to float, K_H_Xe / K_H_Kr).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.json`
- `/app/outputs/selectivity_summary.json`
- `/app/outputs/thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.json
- path: `/app/outputs/structural_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Geometric pore properties (PLD, LCD, surface area, volume, void fraction) for the six MFM MOFs, compared against paper-reported values with tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `mof`, `pld`, `lcd`, `lcd_pl`, `total_sa`, `volume`, `void_fraction`
    - `properties`:
      - `mof`:
        - `type`: string
      - `pld`:
        - `type`: number
        - `unit`: Angstrom
      - `lcd`:
        - `type`: number
        - `unit`: Angstrom
      - `lcd_pl`:
        - `type`: number
      - `total_sa`:
        - `type`: number
        - `unit`: m^2/g
      - `volume`:
        - `type`: number
        - `unit`: cm^3/g
      - `void_fraction`:
        - `type`: number

### selectivity_summary.json
- path: `/app/outputs/selectivity_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Xe/Kr selectivity at 0.01 bar and 10 bar for all six MOFs, eight condition keys, compared to paper-reported values with tolerances. MFM-138 is expected to show the highest selectivity under most conditions (trend check).
- schema:
  - `type`: object
  - `required`: `S_50_50_273_0.01`, `S_50_50_273_10`, `S_50_50_298_0.01`, `S_50_50_298_10`, `S_20_80_273_0.01`, `S_20_80_273_10`, `S_20_80_298_0.01`, `S_20_80_298_10`
  - `properties`:
    - `S_50_50_273_0.01`:
      - `type`: object
      - `description`: MOF name -> Xe/Kr selectivity for 50/50 mixture at 273 K, 0.01 bar
    - `S_50_50_273_10`:
      - `type`: object
      - `description`: MOF name -> selectivity for 50/50 mixture, 273 K, 10 bar
    - `S_50_50_298_0.01`:
      - `type`: object
      - `description`: MOF name -> selectivity for 50/50 mixture, 298 K, 0.01 bar
    - `S_50_50_298_10`:
      - `type`: object
      - `description`: MOF name -> selectivity for 50/50 mixture, 298 K, 10 bar
    - `S_20_80_273_0.01`:
      - `type`: object
      - `description`: MOF name -> selectivity for 20/80 mixture, 273 K, 0.01 bar
    - `S_20_80_273_10`:
      - `type`: object
      - `description`: MOF name -> selectivity for 20/80 mixture, 273 K, 10 bar
    - `S_20_80_298_0.01`:
      - `type`: object
      - `description`: MOF name -> selectivity for 20/80 mixture, 298 K, 0.01 bar
    - `S_20_80_298_10`:
      - `type`: object
      - `description`: MOF name -> selectivity for 20/80 mixture, 298 K, 10 bar

### thermodynamic_properties.json
- path: `/app/outputs/thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Heats of adsorption (Qst) and Henry constants for Xe and Kr at infinite dilution, 298 K, compared to paper Tables 2-3 with tolerances.
- schema:
  - `type`: object
  - `required`: `Qst_Xe`, `Qst_Kr`, `K_H_Xe`, `K_H_Kr`, `Henry_selectivity`
  - `properties`:
    - `Qst_Xe`:
      - `type`: object
      - `description`: MOF name -> infinite dilution heat of adsorption for Xe, kJ/mol
    - `Qst_Kr`:
      - `type`: object
      - `description`: MOF name -> infinite dilution heat of adsorption for Kr, kJ/mol
    - `K_H_Xe`:
      - `type`: object
      - `description`: MOF name -> Henry constant for Xe, units mol·kg⁻¹·Pa⁻¹ ×10⁻⁵
    - `K_H_Kr`:
      - `type`: object
      - `description`: MOF name -> Henry constant for Kr, same units
    - `Henry_selectivity`:
      - `type`: object
      - `description`: MOF name -> Henry selectivity (K_H_Xe / K_H_Kr)

Notes: All three scored outputs are compared against paper-reported reference values using relative and absolute tolerances. No recomputation by the verifier; the checker directly compares the agent-reported numbers to the hidden gold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "mof",
            "pld",
            "lcd",
            "lcd_pl",
            "total_sa",
            "volume",
            "void_fraction"
          ],
          "properties": {
            "mof": {
              "type": "string"
            },
            "pld": {
              "type": "number",
              "unit": "Angstrom"
            },
            "lcd": {
              "type": "number",
              "unit": "Angstrom"
            },
            "lcd_pl": {
              "type": "number"
            },
            "total_sa": {
              "type": "number",
              "unit": "m^2/g"
            },
            "volume": {
              "type": "number",
              "unit": "cm^3/g"
            },
            "void_fraction": {
              "type": "number"
            }
          }
        }
      },
      "description": "Geometric pore properties (PLD, LCD, surface area, volume, void fraction) for the six MFM MOFs, compared against paper-reported values with tolerances."
    },
    {
      "file": "selectivity_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "S_50_50_273_0.01",
          "S_50_50_273_10",
          "S_50_50_298_0.01",
          "S_50_50_298_10",
          "S_20_80_273_0.01",
          "S_20_80_273_10",
          "S_20_80_298_0.01",
          "S_20_80_298_10"
        ],
        "properties": {
          "S_50_50_273_0.01": {
            "type": "object",
            "description": "MOF name -> Xe/Kr selectivity for 50/50 mixture at 273 K, 0.01 bar"
          },
          "S_50_50_273_10": {
            "type": "object",
            "description": "MOF name -> selectivity for 50/50 mixture, 273 K, 10 bar"
          },
          "S_50_50_298_0.01": {
            "type": "object",
            "description": "MOF name -> selectivity for 50/50 mixture, 298 K, 0.01 bar"
          },
          "S_50_50_298_10": {
            "type": "object",
            "description": "MOF name -> selectivity for 50/50 mixture, 298 K, 10 bar"
          },
          "S_20_80_273_0.01": {
            "type": "object",
            "description": "MOF name -> selectivity for 20/80 mixture, 273 K, 0.01 bar"
          },
          "S_20_80_273_10": {
            "type": "object",
            "description": "MOF name -> selectivity for 20/80 mixture, 273 K, 10 bar"
          },
          "S_20_80_298_0.01": {
            "type": "object",
            "description": "MOF name -> selectivity for 20/80 mixture, 298 K, 0.01 bar"
          },
          "S_20_80_298_10": {
            "type": "object",
            "description": "MOF name -> selectivity for 20/80 mixture, 298 K, 10 bar"
          }
        }
      },
      "description": "Xe/Kr selectivity at 0.01 bar and 10 bar for all six MOFs, eight condition keys, compared to paper-reported values with tolerances. MFM-138 is expected to show the highest selectivity under most conditions (trend check)."
    },
    {
      "file": "thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Qst_Xe",
          "Qst_Kr",
          "K_H_Xe",
          "K_H_Kr",
          "Henry_selectivity"
        ],
        "properties": {
          "Qst_Xe": {
            "type": "object",
            "description": "MOF name -> infinite dilution heat of adsorption for Xe, kJ/mol"
          },
          "Qst_Kr": {
            "type": "object",
            "description": "MOF name -> infinite dilution heat of adsorption for Kr, kJ/mol"
          },
          "K_H_Xe": {
            "type": "object",
            "description": "MOF name -> Henry constant for Xe, units mol·kg⁻¹·Pa⁻¹ ×10⁻⁵"
          },
          "K_H_Kr": {
            "type": "object",
            "description": "MOF name -> Henry constant for Kr, same units"
          },
          "Henry_selectivity": {
            "type": "object",
            "description": "MOF name -> Henry selectivity (K_H_Xe / K_H_Kr)"
          }
        }
      },
      "description": "Heats of adsorption (Qst) and Henry constants for Xe and Kr at infinite dilution, 298 K, compared to paper Tables 2-3 with tolerances."
    }
  ],
  "notes": "All three scored outputs are compared against paper-reported reference values using relative and absolute tolerances. No recomputation by the verifier; the checker directly compares the agent-reported numbers to the hidden gold."
}
```

## How you are scored
A hidden verifier will independently evaluate your three output files. The verifier compares the values you report in each artifact against reference results. Your final score is a weighted combination of the scores obtained on the structural properties file, the selectivity file, and the thermodynamic properties file. Reporting numbers without performing the required simulations and analysis will not earn credit; the verifier checks the content of your outputs and may also examine internal consistency and expected trends. No reference values or tolerances are provided in this instruction.
