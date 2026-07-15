## Problem background

Magnetic circular dichroism (MCD) of spin‑forbidden d‑d transitions in high‑spin Fe³⁺ coordination complexes can be analyzed using ligand‑field theory. Two intensity‑generating mechanisms are considered: (i) odd‑parity vibrations (point‑dipole model) and (ii) an odd‑parity crystal field of D₃ symmetry. By computing electric dipole transition moments and Faraday parameters A, B, C from the ligand‑field wavefunctions, one can assign the observed absorption bands and explain the MCD line‑shape. This task reproduces the theoretical oscillator strengths and Faraday parameters obtained from such calculations for an octahedral Fe³⁺ system.

## Approach

The reproduction consists of two stages:

1. **Ligand‑field state calculation**: Using the adopted parameters Dq = 1500 cm⁻¹, Racah B = 600 cm⁻¹, Racah C = 3200 cm⁻¹, set up the Tanabe–Sugano energy matrices for the quartet states (⁴E_g, ⁴T₁g, ⁴T₂g) of the d⁵ configuration in an octahedral field. Solve the secular equations to obtain excitation energies and configuration‑mixed wavefunctions (the cubic‑field states). Store the resulting energies and wavefunction coefficients for use in the intensity steps.

2. **Intensity calculations**: For each of the two mechanisms (odd vibrations and odd crystal field), compute electric dipole transition moments using the Koide–Pryce formalism (point‑dipole ligand vibration model) and the closure approximation, incorporating spin‑orbit mixing between the ground ⁶A₁g and intermediate ⁴T₁g states. The following parameters are used:
   - Spin‑orbit coupling ζ = 400 cm⁻¹
   - Mean charge‑transfer energy δE = 10⁵ cm⁻¹
   - Metal‑ligand bond length R = 4 a₀
   - Radial expectation values (from Clementi's iron SCF wavefunction): ⟨r²⟩ = 1.538 a₀², ⟨r⁴⟩ = 5.852 a₀⁴, ⟨r⁶⟩ = 50.167 a₀⁶
   - Ligand mass M approximated by the mass of an oxygen atom
   - Assumed normal‑mode frequencies: T₁u(ν₃) = 200 cm⁻¹, T₁u(ν₄) = 400 cm⁻¹, T₂u(ν₆) = 100 cm⁻¹
   - Odd crystal field parameter B′ (Eq. 10) estimated from the cubic‑field splitting and ⟨r⁴⟩.

From the transition moments, compute oscillator strengths and then the Faraday parameters A, B, C and the combination (B + C/kT) (with kT = 200 cm⁻¹).

## Reproduction target

Produce the following four scored artifacts:
- Oscillator strengths for the spin‑forbidden transitions enabled by odd vibrations (12 entries).
- Oscillator strengths for the transitions enabled by the odd D₃ crystal field (4 entries).
- Faraday parameters A, B, C and (B + C/kT) for the odd‑vibration mechanism (12 entries).
- Faraday parameters A, B, C and (B + C/kT) for the odd‑crystal‑field mechanism (2 entries).

Each artifact must follow the exact schema described in the Output contract section.

## Assets

- **Python scientific computing stack** (numpy, scipy, sympy) – publicly available via PyPI; may be installed at runtime.
- No external datasets are required; all numeric inputs are given in this instruction.

## Workflow steps

### Step 1: Ligand‑field state calculation
- Role: process
- Action: Set up the Tanabe–Sugano matrices for the d⁵ quartet states in an octahedral field using the parameters Dq=1500, B=600, C=3200 cm⁻¹. Solve the secular equations to obtain the excitation energies and configuration‑mixed wavefunctions for the states listed below (energies in cm⁻¹). Save the results for use in later steps.
- Evidence: `/app/outputs/tanabe_sugano_energies.json` (optional, as a proof of execution)

### Step 2: Odd‑vibration oscillator strengths
- Role: scored (load‑bearing)
- Action: Using the wavefunctions from Step 1, compute electric dipole transition moments induced by the three odd vibrations T₁u(ν₃), T₁u(ν₄), T₂u(ν₆) via the point‑dipole ligand vibration model with spin‑orbit mixing and the closure approximation. Calculate the oscillator strengths for each (transition, vibration_mode) combination listed below and write the results as a JSON array.
- Output file: `/app/outputs/oscillator_strengths_odd_vibrations.json`
- Format: json
- Contract: Array of 12 objects, each with keys: `transition` (string), `vibration_mode` (string), `oscillator_strength` (float). The required combinations are:
  * Transition "6A1g→4T2g(1)" with vibration_modes "T1u(nu3)", "T1u(nu4)", "T2u(nu6)"
  * Transition "6A1g→4Eg(1)"  with vibration_modes "T1u(nu3)", "T1u(nu4)", "T2u(nu6)"
  * Transition "6A1g→4A1g"    with vibration_modes "T1u(nu3)", "T1u(nu4)", "T2u(nu6)"
  * Transition "6A1g→4T1g(1)" with vibration_modes "T1u(nu3)", "T1u(nu4)", "T2u(nu6)"
- Scoring: scored by hidden verifier

### Step 3: Odd‑crystal‑field oscillator strengths
- Role: scored
- Action: Using the same wavefunctions, compute electric dipole transition moments induced by a small odd‑parity D₃ crystal field with the point‑dipole model and closure approximation. Calculate the polarization‑labeled oscillator strengths for the following 4 (transition, polarization) combinations and write the results as a JSON array.
- Output file: `/app/outputs/oscillator_strengths_odd_crystal_field.json`
- Format: json
- Contract: Array of 4 objects, each with keys: `transition` (string), `polarization` (string: "σ" or "π"), `oscillator_strength` (float). The required combinations are:
  * Transition "6A1g→4T2g(1):→4E" with polarization "σ"
  * Transition "6A1g→4Eg(1):→4E"  with polarization "σ"
  * Transition "6A1g→4T1g(1):→4E" with polarization "σ"
  * Transition "6A1g→4T1g(1):→4A2" with polarization "π"
- Scoring: scored by hidden verifier

### Step 4: Faraday parameters – odd vibrations
- Role: scored (load‑bearing)
- Action: From the transition moments of Step 2, magnetic dipole matrix elements, and spin–orbit mixing with the ⁴T₁g states, compute the Faraday parameters A, B, C and the quantity (B + C/kT) for each (transition, vibration_mode) combination listed in Step 2. Output a JSON array with all 12 combinations.
- Output file: `/app/outputs/faraday_parameters_odd_vibrations.json`
- Format: json
- Contract: Array of 12 objects, each with keys: `transition` (string), `vibration_mode` (string), `A` (float), `B` (float), `C` (float), `B_plus_C_over_kT` (float). Use the same (transition, vibration_mode) combinations as in Step 2. Units: A, C in 10⁻²⁴ β e² cm²; B, B_plus_C_over_kT in 10⁻²⁴ β e² cm² / cm⁻¹.
- Scoring: scored by hidden verifier

### Step 5: Faraday parameters – odd crystal field
- Role: scored
- Action: Using the odd‑crystal‑field transition moments from Step 3 and spin–orbit coupling, compute the Faraday parameters A, B, C and (B + C/kT) for the following two transitions.
- Output file: `/app/outputs/faraday_parameters_odd_crystal_field.json`
- Format: json
- Contract: Array of 2 objects, each with keys: `transition` (string), `A` (float), `B` (float), `C` (float), `B_plus_C_over_kT` (float). The required transitions are:
  * "6A1g→4T2g(1):→4E"
  * "6A1g→4Eg(1):→4E"
- Scoring: scored by hidden verifier

## Output files

The following files must be placed under `/app/outputs`:
- `tanabe_sugano_energies.json` (evidence, optional)
- `oscillator_strengths_odd_vibrations.json` (scored)
- `oscillator_strengths_odd_crystal_field.json` (scored)
- `faraday_parameters_odd_vibrations.json` (scored)
- `faraday_parameters_odd_crystal_field.json` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### oscillator_strengths_odd_vibrations.json
- path: `/app/outputs/oscillator_strengths_odd_vibrations.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: 12 entries: all combinations of transitions 6A1g→4T2g(1), 6A1g→4Eg(1), 6A1g→4A1g, 6A1g→4T1g(1) with vibration modes T1u(nu3), T1u(nu4), T2u(nu6).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `transition`, `vibration_mode`, `oscillator_strength`
    - `properties`:
      - `transition`:
        - `type`: string
      - `vibration_mode`:
        - `type`: string
      - `oscillator_strength`:
        - `type`: number

### oscillator_strengths_odd_crystal_field.json
- path: `/app/outputs/oscillator_strengths_odd_crystal_field.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: 4 entries: transitions 6A1g→4T2g(1):→4E (σ), 6A1g→4Eg(1):→4E (σ), 6A1g→4T1g(1):→4E (σ), 6A1g→4T1g(1):→4A2 (π).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `transition`, `polarization`, `oscillator_strength`
    - `properties`:
      - `transition`:
        - `type`: string
      - `polarization`:
        - `type`: string
      - `oscillator_strength`:
        - `type`: number

### faraday_parameters_odd_vibrations.json
- path: `/app/outputs/faraday_parameters_odd_vibrations.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: 12 entries: same (transition, vibration_mode) combinations as the odd‑vibration oscillator strengths. Units: A, C in 10⁻²⁴ β e² cm²; B, B_plus_C_over_kT in 10⁻²⁴ β e² cm² / cm⁻¹.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `transition`, `vibration_mode`, `A`, `B`, `C`, `B_plus_C_over_kT`
    - `properties`:
      - `transition`:
        - `type`: string
      - `vibration_mode`:
        - `type`: string
      - `A`:
        - `type`: number
      - `B`:
        - `type`: number
      - `C`:
        - `type`: number
      - `B_plus_C_over_kT`:
        - `type`: number

### faraday_parameters_odd_crystal_field.json
- path: `/app/outputs/faraday_parameters_odd_crystal_field.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: 2 entries: transitions 6A1g→4T2g(1):→4E and 6A1g→4Eg(1):→4E. Units as above.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `transition`, `A`, `B`, `C`, `B_plus_C_over_kT`
    - `properties`:
      - `transition`:
        - `type`: string
      - `A`:
        - `type`: number
      - `B`:
        - `type`: number
      - `C`:
        - `type`: number
      - `B_plus_C_over_kT`:
        - `type`: number

Notes: All values must be computed using the parameters and formulas described in the instruction. The hidden verifier compares each entry to the reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "oscillator_strengths_odd_vibrations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "transition",
            "vibration_mode",
            "oscillator_strength"
          ],
          "properties": {
            "transition": {
              "type": "string"
            },
            "vibration_mode": {
              "type": "string"
            },
            "oscillator_strength": {
              "type": "number"
            }
          }
        }
      },
      "description": "12 entries: all combinations of transitions 6A1g→4T2g(1), 6A1g→4Eg(1), 6A1g→4A1g, 6A1g→4T1g(1) with vibration modes T1u(nu3), T1u(nu4), T2u(nu6)."
    },
    {
      "file": "oscillator_strengths_odd_crystal_field.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "transition",
            "polarization",
            "oscillator_strength"
          ],
          "properties": {
            "transition": {
              "type": "string"
            },
            "polarization": {
              "type": "string"
            },
            "oscillator_strength": {
              "type": "number"
            }
          }
        }
      },
      "description": "4 entries: transitions 6A1g→4T2g(1):→4E (σ), 6A1g→4Eg(1):→4E (σ), 6A1g→4T1g(1):→4E (σ), 6A1g→4T1g(1):→4A2 (π)."
    },
    {
      "file": "faraday_parameters_odd_vibrations.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "transition",
            "vibration_mode",
            "A",
            "B",
            "C",
            "B_plus_C_over_kT"
          ],
          "properties": {
            "transition": {
              "type": "string"
            },
            "vibration_mode": {
              "type": "string"
            },
            "A": {
              "type": "number"
            },
            "B": {
              "type": "number"
            },
            "C": {
              "type": "number"
            },
            "B_plus_C_over_kT": {
              "type": "number"
            }
          }
        }
      },
      "description": "12 entries: same (transition, vibration_mode) combinations as the odd‑vibration oscillator strengths. Units: A, C in 10⁻²⁴ β e² cm²; B, B_plus_C_over_kT in 10⁻²⁴ β e² cm² / cm⁻¹."
    },
    {
      "file": "faraday_parameters_odd_crystal_field.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "transition",
            "A",
            "B",
            "C",
            "B_plus_C_over_kT"
          ],
          "properties": {
            "transition": {
              "type": "string"
            },
            "A": {
              "type": "number"
            },
            "B": {
              "type": "number"
            },
            "C": {
              "type": "number"
            },
            "B_plus_C_over_kT": {
              "type": "number"
            }
          }
        }
      },
      "description": "2 entries: transitions 6A1g→4T2g(1):→4E and 6A1g→4Eg(1):→4E. Units as above."
    }
  ],
  "notes": "All values must be computed using the parameters and formulas described in the instruction. The hidden verifier compares each entry to the reference values with appropriate tolerances."
}
```

## How you are scored

A hidden verifier independently checks each scored artifact against reference values (the paper‑reported results) using appropriate tolerances. Each artifact carries a weight; the final reward is a weighted average of the scores for the individual artifacts. Reporting the correct answer from memory or by peeking is not sufficient – the verifier expects the artifacts to be generated by executing the described calculations.
