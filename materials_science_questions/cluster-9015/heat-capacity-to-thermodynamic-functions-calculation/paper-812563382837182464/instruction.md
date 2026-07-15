# Thermodynamic Modeling of WTe2 and Chemical Vapor Transport Mechanism

## Problem background
Two-dimensional tungsten ditelluride (WTe₂) is a layered transition metal dichalcogenide with a thermodynamically stable distorted octahedral structure at room temperature. Its electronic properties—semimetallic behavior, giant magnetoresistance, and topological features—make high-quality few-layer crystals highly desirable for quantum transport studies. Bottom-up synthesis via chemical vapor transport (CVT) with halogen additives offers a controllable route, but the growth conditions depend sensitively on the underlying thermodynamics of the W–Te–Br system. Rational synthesis planning therefore requires computational thermodynamic modeling: using the CALPHAD method to optimize the thermodynamic description of WTe₂, simulate the gas-phase composition under CVT conditions, and deduce the transport mechanism. The task is to reproduce this thermodynamic evaluation and identify the dominant species and net reaction that drive the crystal growth.

## Approach
The work proceeds in three stages, all implemented with open-source CALPHAD tools (pycalphad) and standard element databases (SGTE). First, a thermodynamic optimization of WTe₂ is performed by fitting experimental data: the binary W–Te phase diagram (peritectic and eutectic points), the temperature‑dependent decomposition vapor pressure, low‑temperature heat capacity, and the standard enthalpy of formation. This yields the optimized standard formation enthalpy, standard entropy, and temperature‑piecewise heat capacity coefficients, as well as the peritectic temperature read from the computed phase diagram.

Second, using the optimized WTe₂ data together with known thermodynamic properties of Br‑containing gaseous species, heterogeneous equilibrium calculations are carried out to determine the gas‑phase composition above solid WTe₂ with a small bromine addition (~5 atom‑%) at a typical CVT temperature (~700 °C). This identifies the dominant gas species and their partial pressures.

Third, transport efficiencies are evaluated for a fixed temperature gradient (source T₂=1100 K, sink T₁=1000 K) from the change in partial pressures of each gaseous species. Species with a negative efficiency serve as the transport agent, while those with positive efficiency are the migrating species that actually carry the mass. The net heterogeneous reaction that captures the CVT mechanism is then formulated from these roles. All required publicly available datasets (phase diagram, vapor pressure, heat capacity, enthalpy of formation, and reference Cp functions) are cited in the assets list; the computation is CPU‑only and completes within roughly one hour on standard hardware.

## Reproduction target
Produce the following three output files in `/app/outputs`:

1. `optimized_thermodynamic_data.json` – contains the optimized standard formation enthalpy ΔfH°(298 K) in kJ mol⁻¹, standard entropy S°(298 K) in J mol⁻¹ K⁻¹, the Cp coefficients (four‑parameter sets a0, a1, a2, a3) for the three temperature intervals 1–145 K, 145–298 K, and 298–1501 K, and the peritectic temperature in °C.

2. `gas_phase_analysis.json` – reports the equilibrium gas‑phase composition above solid WTe₂ with ~5 atom‑% bromine at ~700 °C: a list of all species with their partial pressures in bar, the subset of species considered dominant, and any pertinent notes.

3. `transport_efficiency_analysis.json` – for the temperature gradient T₂=1100 K, T₁=1000 K, provides the transport efficiency w(i) of each gaseous species, identifies the transport agent (negative efficiency) and the migrating species (positive efficiencies), and gives the deduced net CVT reaction equation.

## Assets

- pycalphad: https://github.com/pycalphad/pycalphad
- SGTE Pure Elements Database: pycalphad (embedded)
- W–Te binary phase diagram data (Predel, 1998): 10.1007/10551312_282S
- Vapor pressure data for WTe2 (Obolonchik & Nesterovskaja, 1971)
- Low-temperature heat capacity of WTe2 (Callanan et al., 1992)
- Standard molar enthalpy of formation of WTe2 (O'Hare & Hope, 1992)
- MoTe2 heat capacity function (for extrapolation)

## Workflow steps

### Step 1: Optimize thermodynamic data for WTe2
- Role: scored (load-bearing)
- Action: Using open-source CALPHAD tools (e.g., pycalphad) with standard element databases and literature experimental data (phase diagram, vapor pressure, heat capacity, enthalpy of formation), perform a thermodynamic optimization of WTe2. Fit the binary W–Te phase diagram and vapor pressure behavior to obtain optimized standard formation enthalpy ΔfH°(298 K), standard entropy S°(298 K), and Cp coefficients over three temperature intervals. Determine the peritectic temperature from the calculated phase diagram. Write all optimized parameters to the output file.
- Output file: `/app/outputs/optimized_thermodynamic_data.json`
- Format: json
- Contract: JSON with keys: delta_H_formation (number, kJ/mol), S_entropy (number, J/(mol*K)), Cp_coefficients (array of 3 sub-arrays, each [a0, a1, a2, a3] for T ranges 1…145 K, 145…298 K, 298…1501 K), peritectic_temperature_C (number).
- Scoring: scored by hidden verifier

### Step 2: Compute gas-phase composition in W–Te–Br system
- Role: scored
- Action: Using the optimized thermodynamic data from step_01 and available standard data for Br-containing species, perform heterogeneous equilibrium calculations to determine the gas-phase composition above solid WTe2 with bromine addition (approximately 5 atom % Br) at a typical CVT temperature (around 700°C). Identify the dominant gaseous species and their partial pressures. Write the results, listing all species and marking those considered dominant.
- Output file: `/app/outputs/gas_phase_analysis.json`
- Format: json
- Contract: JSON with keys: temperature_C (number), bromine_content_at_percent (number), gas_species (array of objects {species: string, partial_pressure_bar: number}), dominant_species (array of species names), notes (string).
- Scoring: scored by hidden verifier

### Step 3: Analyze transport efficiencies and deduce CVT mechanism
- Role: scored
- Action: For a temperature gradient T2=1100 K (source), T1=1000 K (sink), compute transport efficiencies w(i) of the gaseous species using their partial pressures at the two temperatures (e.g., w(i) = (p_i(T2) - p_i(T1)) / sum_j |p_j(T2)-p_j(T1)|). Identify the species with negative w(i) as the transport agent, and those with positive w(i) as the migrating species responsible for mass transport. Deduce the net heterogeneous CVT equilibrium that drives the transport. Write the species names, their efficiencies, the identified roles, and the reaction equation.
- Output file: `/app/outputs/transport_efficiency_analysis.json`
- Format: json
- Contract: JSON with keys: temperature_gradient (object {T2_K: number, T1_K: number}), species_efficiency (array of objects {species: string, efficiency: number}), transport_agent (string), migrating_species (array of strings), net_reaction (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_thermodynamic_data.json`
- `/app/outputs/gas_phase_analysis.json`
- `/app/outputs/transport_efficiency_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_thermodynamic_data.json
- path: `/app/outputs/optimized_thermodynamic_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized standard formation enthalpy, standard entropy, Cp coefficients, and peritectic temperature of WTe2. Checked against paper-reported gold values with absolute tolerances.
- schema:
  - `type`: object
  - `required`: `delta_H_formation`, `S_entropy`, `Cp_coefficients`, `peritectic_temperature_C`
  - `units`:
    - `delta_H_formation`: kJ/mol
    - `S_entropy`: J/(mol*K)
    - `peritectic_temperature_C`: °C
  - `properties`:
    - `delta_H_formation`:
      - `type`: number
    - `S_entropy`:
      - `type`: number
    - `Cp_coefficients`:
      - `type`: array
      - `items`:
        - `type`: array
        - `minItems`: 4
        - `maxItems`: 4
    - `peritectic_temperature_C`:
      - `type`: number

### gas_phase_analysis.json
- path: `/app/outputs/gas_phase_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Gas-phase composition at the selected CVT conditions. Structural audit verifies that the dominant_species list contains WBr4, TeBr2, Te2 and that partial pressures are plausible.
- schema:
  - `type`: object
  - `required`: `temperature_C`, `bromine_content_at_percent`, `gas_species`, `dominant_species`, `notes`
  - `units`:
    - `temperature_C`: °C
  - `properties`:
    - `temperature_C`:
      - `type`: number
    - `bromine_content_at_percent`:
      - `type`: number
    - `gas_species`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `species`, `partial_pressure_bar`
    - `dominant_species`:
      - `type`: array
      - `items`:
        - `type`: string
    - `notes`:
      - `type`: string

### transport_efficiency_analysis.json
- path: `/app/outputs/transport_efficiency_analysis.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Transport efficiencies and deduced CVT mechanism. Structural audit verifies transport_agent='TeBr2', migrating_species includes WBr4 and Te2, and net_reaction matches the expected equilibrium.
- schema:
  - `type`: object
  - `required`: `temperature_gradient`, `species_efficiency`, `transport_agent`, `migrating_species`, `net_reaction`
  - `properties`:
    - `temperature_gradient`:
      - `type`: object
      - `required`: `T2_K`, `T1_K`
    - `species_efficiency`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `species`, `efficiency`
    - `transport_agent`:
      - `type`: string
    - `migrating_species`:
      - `type`: array
      - `items`:
        - `type`: string
    - `net_reaction`:
      - `type`: string

Notes: The experimental synthesis and characterization steps are excluded. Only the thermodynamic modeling and CVT simulation are reproduced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_thermodynamic_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "delta_H_formation",
          "S_entropy",
          "Cp_coefficients",
          "peritectic_temperature_C"
        ],
        "units": {
          "delta_H_formation": "kJ/mol",
          "S_entropy": "J/(mol*K)",
          "peritectic_temperature_C": "°C"
        },
        "properties": {
          "delta_H_formation": {
            "type": "number"
          },
          "S_entropy": {
            "type": "number"
          },
          "Cp_coefficients": {
            "type": "array",
            "items": {
              "type": "array",
              "minItems": 4,
              "maxItems": 4
            }
          },
          "peritectic_temperature_C": {
            "type": "number"
          }
        }
      },
      "description": "Optimized standard formation enthalpy, standard entropy, Cp coefficients, and peritectic temperature of WTe2. Checked against paper-reported gold values with absolute tolerances."
    },
    {
      "file": "gas_phase_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "temperature_C",
          "bromine_content_at_percent",
          "gas_species",
          "dominant_species",
          "notes"
        ],
        "units": {
          "temperature_C": "°C"
        },
        "properties": {
          "temperature_C": {
            "type": "number"
          },
          "bromine_content_at_percent": {
            "type": "number"
          },
          "gas_species": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "species",
                "partial_pressure_bar"
              ]
            }
          },
          "dominant_species": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "notes": {
            "type": "string"
          }
        }
      },
      "description": "Gas-phase composition at the selected CVT conditions. Structural audit verifies that the dominant_species list contains WBr4, TeBr2, Te2 and that partial pressures are plausible."
    },
    {
      "file": "transport_efficiency_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "temperature_gradient",
          "species_efficiency",
          "transport_agent",
          "migrating_species",
          "net_reaction"
        ],
        "properties": {
          "temperature_gradient": {
            "type": "object",
            "required": [
              "T2_K",
              "T1_K"
            ]
          },
          "species_efficiency": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "species",
                "efficiency"
              ]
            }
          },
          "transport_agent": {
            "type": "string"
          },
          "migrating_species": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "net_reaction": {
            "type": "string"
          }
        }
      },
      "description": "Transport efficiencies and deduced CVT mechanism. Structural audit verifies transport_agent='TeBr2', migrating_species includes WBr4 and Te2, and net_reaction matches the expected equilibrium."
    }
  ],
  "notes": "The experimental synthesis and characterization steps are excluded. Only the thermodynamic modeling and CVT simulation are reproduced."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently scores each of the three output artifacts.

- Step 1 (`optimized_thermodynamic_data.json`) is compared against a hidden reference with appropriate tolerances on the key thermodynamic parameters and peritectic temperature.
- Step 2 (`gas_phase_analysis.json`) is checked for structural correctness: the dominant‑species list must contain the expected key species, and partial pressures must be physically plausible.
- Step 3 (`transport_efficiency_analysis.json`) is verified structurally: the transport agent and migrating species must match the mechanism derived from equilibrium thermodynamics, and the net reaction must be correctly identified.

The three stages contribute weights of approximately 0.4, 0.3, and 0.3, respectively, to the final reward, which is a single float between 0 and 1 (higher is better). The verifier expects the artifacts to genuinely reflect the outcome of your computational workflow; simply reproducing known literature numbers without performing the thermodynamic calculations is not sufficient.
