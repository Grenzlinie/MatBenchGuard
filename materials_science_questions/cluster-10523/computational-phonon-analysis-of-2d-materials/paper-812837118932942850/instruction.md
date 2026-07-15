# DFT Phonon and Electronic Structure of Na-Intercalated Graphene Layers

## Problem background
Sodium-ion batteries require high-capacity anode materials. Non-graphitizable (hard) carbon can reversibly store ~250 mAh/g of Na, but the atomic-scale insertion mechanism remains debated. A joint experimental–theoretical study used operando Raman spectroscopy and density functional theory (DFT) calculations on Na-intercalated graphitic model structures to propose a four-stage insertion process. The DFT results revealed characteristic changes in the G-band phonon frequency and the electronic band crossing at the K-point as Na content increases, providing a link between the Raman signatures and the insertion stages. Quantifying these DFT-predicted properties—the Γ-point G-band frequency, the K-point crossing energy relative to the Fermi level, and the intercalation voltage—for a series of NaCx model compounds is the computational target of this task. Performing these calculations tests the electronic and vibrational basis of the insertion mechanism without requiring experimental data.

## Approach
The approach relies on first-principles DFT calculations with a van der Waals functional to describe the graphitic layers and intercalated Na atoms. Periodic slab models are constructed for pristine graphite (AB stacking) and for AA-stacked graphene layers intercalated with Na at four stoichiometries: NaC₄₈, NaC₂₄, NaC₁₂, and NaC₆. For each pristine model, the geometry is relaxed, and the phonon dispersion and electronic band structure are computed. The G-band frequency is extracted from the phonon dispersion as the highest optical mode at the Γ-point. The K-point crossing energy is obtained from the electronic band structure as the energy of the highest occupied band at the K-point relative to the Fermi level. To compute the intercalation voltage, defective models are used: one mono-vacancy is introduced per carbon layer (one carbon atom removed per layer) to stabilize Na intercalation, following the methodology of the original study. A separate DFT geometry relaxation and total-energy calculation is performed on each defective NaCₓ model, and the average intercalation voltage for each Na addition step is calculated from the total energies using the standard expression V = –[E(NaₓC) – E(Naₓ₋₁C) – μ(Na)]/(e·F), with the chemical potential μ(Na) taken from bulk sodium metal. This computational workflow yields the three target quantities for each stoichiometry (phonon and band structure from the pristine model, voltage from the defective model), enabling a systematic comparison with the reported experimental trends.

## Reproduction target
Your goal is to produce a single JSON file step_01_dft_results.json that contains an array of five objects, one for each stoichiometry: graphite_AB, NaC48, NaC24, NaC12, NaC6. Each object must include the following keys: 'stoichiometry' (string), 'g_band_frequency_cm1' (number, the Γ-point G-band frequency in cm⁻¹), 'k_point_crossing_energy_eV' (number, the energy of the highest occupied band at the K-point relative to the Fermi level, in eV; a positive value means the crossing lies above the Fermi level), and 'intercalation_voltage_V' (number or null, the average intercalation voltage in V for the step adding Na to reach that stoichiometry; null for graphite). The computed values must result from a self-consistent DFT calculation following the approach described above. The JSON file must conform to this exact schema; no additional fields are required.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE) v1.3.0: https://www.quantum-espresso.org/pseudopotentials/sssp-efficiency-pbe-v1-3-0
- phonopy: phonopy
- BandUP / phonon unfolding tools

## Workflow steps

### Step 1: Construct atomic model structures
- Role: process
- Action: Generate periodic slab models for graphite (AB stacking), AA-stacked graphene layers, and intercalated structures NaC48, NaC24, NaC12, NaC6 using known lattice parameters of graphite/graphene. Place Na atoms at high-symmetry intercalation sites consistent with stage I/II configurations described in the paper. Additionally, generate a corresponding set of structures with one mono-vacancy per carbon layer (remove one C atom per layer) for use in the voltage calculation.
- Evidence: `/app/outputs/structure_files.log`

### Step 2: DFT calculations of phonon, electronic, and voltage properties
- Role: scored (load-bearing)
- Action: On the pristine model structures (graphite_AB, NaC48, NaC24, NaC12, NaC6), perform DFT geometry relaxation using a van der Waals functional (optPBE-vdW or comparable). Compute phonon dispersion curves via finite-displacement method (phonopy) and extract the Γ-point frequency of the G-band mode. Compute electronic band structure along Γ-K-M-Γ and determine the energy of the highest occupied band at the K-point relative to the Fermi level. On the corresponding defective model structures (each with one mono-vacancy per carbon layer), perform separate DFT geometry relaxation and total-energy calculations. Derive average intercalation voltages for successive Na additions as V = -[E(NaxC) - E(Nax-1C) - μ(Na)]/e·F, using Na metal as reference. Output all values in step_01_dft_results.json.
- Output file: `/app/outputs/step_01_dft_results.json`
- Format: json
- Contract: Array of objects with keys: stoichiometry (string), g_band_frequency_cm1 (number), k_point_crossing_energy_eV (number), intercalation_voltage_V (number|null for graphite_AB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dft_results.json
- path: `/app/outputs/step_01_dft_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored artifact containing the computed DFT phonon, electronic, and voltage properties for the series of Na-intercalated graphitic model structures. The checker will compare each stoichiometry's values against hidden gold trends and tolerances to verify reproduction of the key computational findings.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `stoichiometry`, `g_band_frequency_cm1`, `k_point_crossing_energy_eV`, `intercalation_voltage_V`
    - `properties`:
      - `stoichiometry`:
        - `type`: string
        - `enum`: `graphite_AB`, `NaC48`, `NaC24`, `NaC12`, `NaC6`
      - `g_band_frequency_cm1`:
        - `type`: number
        - `unit`: cm⁻¹
        - `description`: Γ-point G-band phonon frequency
      - `k_point_crossing_energy_eV`:
        - `type`: number
        - `unit`: eV
        - `description`: Energy of the highest occupied band at the K-point relative to the Fermi level (positive means crossing above Fermi, negative below)
      - `intercalation_voltage_V`:
        - `type`: `number`, `null`
        - `unit`: V
        - `description`: Average intercalation voltage for the step from the previous Na content; null for graphite_AB

Notes: The agent must perform full DFT calculations; no intermediate DFT outputs are scored, only this final JSON file. The checker verifies that G-band frequency decreases monotonically with Na content, K-point crossing is above Fermi for low Na and below for high Na, and intercalation voltages are positive up to NaC24 and negative beyond. Tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "stoichiometry",
            "g_band_frequency_cm1",
            "k_point_crossing_energy_eV",
            "intercalation_voltage_V"
          ],
          "properties": {
            "stoichiometry": {
              "type": "string",
              "enum": [
                "graphite_AB",
                "NaC48",
                "NaC24",
                "NaC12",
                "NaC6"
              ]
            },
            "g_band_frequency_cm1": {
              "type": "number",
              "unit": "cm⁻¹",
              "description": "Γ-point G-band phonon frequency"
            },
            "k_point_crossing_energy_eV": {
              "type": "number",
              "unit": "eV",
              "description": "Energy of the highest occupied band at the K-point relative to the Fermi level (positive means crossing above Fermi, negative below)"
            },
            "intercalation_voltage_V": {
              "type": [
                "number",
                "null"
              ],
              "unit": "V",
              "description": "Average intercalation voltage for the step from the previous Na content; null for graphite_AB"
            }
          }
        }
      },
      "description": "Scored artifact containing the computed DFT phonon, electronic, and voltage properties for the series of Na-intercalated graphitic model structures. The checker will compare each stoichiometry's values against hidden gold trends and tolerances to verify reproduction of the key computational findings."
    }
  ],
  "notes": "The agent must perform full DFT calculations; no intermediate DFT outputs are scored, only this final JSON file. The checker verifies that G-band frequency decreases monotonically with Na content, K-point crossing is above Fermi for low Na and below for high Na, and intercalation voltages are positive up to NaC24 and negative beyond. Tolerances are hidden."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier that checks your step_01_dft_results.json file. The verifier compares each stoichiometry's reported quantities against hidden reference data derived from the original study. The verifier assigns a reward between 0 and 1 based on how well your computed results match the hidden gold, taking into account tolerances and consistency criteria. Simply inserting numbers from a publication without actually performing the required computational workflow will not succeed.
