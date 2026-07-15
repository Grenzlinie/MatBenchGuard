# Thermodynamic equilibrium analysis of Fe-Cr-C hardfacing alloys

## Problem background
Iron-based alloys with high chromium and carbon content, used for hardfacing by arc welding, solidify with a microstructure of hard M7C3 carbides embedded in a metastable austenite matrix. The equilibrium phase stability of these alloys at elevated temperatures is critical because the transformation of austenite into a mixture of ferrite and additional carbides can degrade corrosion resistance and mechanical properties. Determining which phases are thermodynamically stable, their equilibrium volume fractions, and how alloying elements partition between phases provides the foundation for understanding and predicting the long‑term behaviour of these hardfacing deposits.

## Approach
The CALPHAD (CALculation of PHAse Diagrams) method is used to compute the equilibrium phase assemblages by minimising the total Gibbs free energy of the system. The calculations are performed with the open‑source software pycalphad, together with a publicly available thermodynamic database for the Fe–Cr–C–Mn–Si–Mo system. Two nominal alloy compositions from the literature are investigated:

- Alloy 1: Fe–29.19Cr–1.32Mn–0.59Si–0.01Mo–3.8C (wt%)
- Alloy 2: Fe–37.87Cr–4.5C–1.41Mn–0.86Si (wt%)

For each alloy, full equilibrium calculations are carried out over a wide temperature range (e.g. 700–1500 °C), allowing the phases LIQUID, FCC_A1 (austenite), BCC_A2 (ferrite), and M7C3. Additionally, a metastable equilibrium is calculated for alloy 1 by suppressing ferrite, so that only austenite and M7C3 are allowed, mimicking the kinetic freezing‑in observed during rapid weld cooling. From the resulting phase fraction and composition data the following quantities are extracted: equilibrium volume fractions at selected temperatures, the Cr partition coefficient between M7C3 and austenite, and the influence of silicon on austenite stability (by repeating the equilibrium calculation for alloy 2 after removing silicon and rescaling the remaining elements).

## Reproduction target
Perform the calculations described above and produce the following three scored artifacts:

1. **Phase fractions and stability** – From the full equilibrium data, extract the volume fractions of ferrite and M7C3 for alloy 1 at exactly 850 °C, the identity of the stable phases present in alloy 2 at 800 °C (a string such as `"ferrite+M7C3"` or `"austenite+M7C3"`), and the austenite volume fraction at 1300 °C from the metastable calculation for alloy 1. Write these results to `step_01_phase_fractions.json` according to its output schema.

2. **Cr partition coefficient** – Using the metastable equilibrium data at 1300 °C for alloy 1, compute the ratio of the atomic fraction of Cr in the M7C3 phase to that in the austenite phase. Record this coefficient in `step_02_partition_coefficient.json`.

3. **Effect of silicon on austenite stability** – Determine whether removing silicon from alloy 2 (and scaling the remaining elements proportionally) causes austenite (FCC_A1) to become a stable equilibrium phase at any temperature above 800 °C. Report the conclusion as a single line in `step_03_silicon_effect.txt`: either `"Yes, austenite appears at high temperature after removing silicon"` or `"No, austenite does not appear"`.

## Assets

- pycalphad: https://github.com/pycalphad/pycalphad
- Thermodynamic database for Fe-Cr-C-Mn-Si-Mo system: https://github.com/OpenCalphad/opencalphad-examples/tree/master/thermodynamic-data

## Workflow steps

### Step 1: Full equilibrium calculation for alloy 1 and alloy 2
- Role: process
- Action: Using pycalphad and the thermodynamic database, compute equilibrium phase fractions and compositions as a function of temperature (e.g., 700–1500°C) for both alloy 1 and alloy 2 with all major phases (LIQUID, FCC_A1, BCC_A2, M7C3) allowed. Save the full temperature-dependent phase data.
- Evidence: `/app/outputs/phase_data_alloy1.json, phase_data_alloy2.json`

### Step 2: Metastable equilibrium calculation for alloy 1 (ferrite suppressed)
- Role: process
- Action: Perform a ferrite-suppressed equilibrium calculation for alloy 1, allowing only FCC_A1 and M7C3, over the temperature range 1000–1500°C. Record phase compositions (atomic fractions) and the austenite volume fraction at each temperature.
- Evidence: `/app/outputs/metastable_data_alloy1.json`

### Step 3: Extract phase fractions and stability from equilibrium data
- Role: scored
- Action: From the equilibrium data, extract the volume fractions of ferrite and M7C3 for alloy 1 at exactly 850°C, the stable phases present in alloy 2 at 800°C, and the austenite volume fraction at 1300°C from the metastable data.
- Output file: `/app/outputs/step_01_phase_fractions.json`
- Format: json
- Contract: {"alloy1_vol_frac_ferrite_850C": float, "alloy1_vol_frac_M7C3_850C": float, "alloy2_stable_phase_at_800C": string, "alloy1_vol_frac_austenite_1300C": float}
- Scoring: scored by hidden verifier

### Step 4: Compute Cr partition coefficient
- Role: scored (load-bearing)
- Action: From the metastable equilibrium data at 1300°C, compute the Cr partition coefficient as the ratio of atomic fraction of Cr in M7C3 to that in austenite.
- Output file: `/app/outputs/step_02_partition_coefficient.json`
- Format: json
- Contract: {"Cr_partition_coefficient_1300C": float}
- Scoring: scored by hidden verifier

### Step 5: Equilibrium calculation for alloy 2 with and without silicon
- Role: process
- Action: Perform full equilibrium calculations for alloy 2 twice: once with the original Si content and once with Si set to zero (scaling other elements accordingly). For each case, determine whether austenite (FCC_A1) appears as a stable phase above 800°C.
- Evidence: `/app/outputs/si_effect_data.json`

### Step 6: Report silicon effect on austenite stability
- Role: scored
- Action: Based on the calculations from step05, write a single line stating whether removing silicon from alloy 2 causes austenite to become stable at high temperature. Use the format: 'Yes, austenite appears at high temperature after removing silicon' or 'No, austenite does not appear'.
- Output file: `/app/outputs/step_03_silicon_effect.txt`
- Format: txt
- Contract: Single line string
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phase_fractions.json`
- `/app/outputs/step_02_partition_coefficient.json`
- `/app/outputs/step_03_silicon_effect.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phase_fractions.json
- path: `/app/outputs/step_01_phase_fractions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted equilibrium volume fractions and stable phases from thermodynamic calculations.
- schema:
  - `type`: object
  - `required`:
    - `alloy1_vol_frac_ferrite_850C`: float
    - `alloy1_vol_frac_M7C3_850C`: float
    - `alloy2_stable_phase_at_800C`: string
    - `alloy1_vol_frac_austenite_1300C`: float

### step_02_partition_coefficient.json
- path: `/app/outputs/step_02_partition_coefficient.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed chromium partition coefficient between M7C3 and austenite at 1300°C.
- schema:
  - `type`: object
  - `required`:
    - `Cr_partition_coefficient_1300C`: float

### step_03_silicon_effect.txt
- path: `/app/outputs/step_03_silicon_effect.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Statement of the silicon effect on austenite stability in alloy 2.
- schema:
  - `type`: text
  - `required`: object
  - `description`: Single-line string stating whether silicon removal stabilizes austenite.

Notes: All comparisons are against paper-reported reference values with appropriate tolerances. Volume fractions and partition coefficient are checked within a tolerance; the silicon effect string must match the expected answer.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phase_fractions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alloy1_vol_frac_ferrite_850C": "float",
          "alloy1_vol_frac_M7C3_850C": "float",
          "alloy2_stable_phase_at_800C": "string",
          "alloy1_vol_frac_austenite_1300C": "float"
        }
      },
      "description": "Extracted equilibrium volume fractions and stable phases from thermodynamic calculations."
    },
    {
      "file": "step_02_partition_coefficient.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Cr_partition_coefficient_1300C": "float"
        }
      },
      "description": "Computed chromium partition coefficient between M7C3 and austenite at 1300°C."
    },
    {
      "file": "step_03_silicon_effect.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "description": "Single-line string stating whether silicon removal stabilizes austenite."
      },
      "description": "Statement of the silicon effect on austenite stability in alloy 2."
    }
  ],
  "notes": "All comparisons are against paper-reported reference values with appropriate tolerances. Volume fractions and partition coefficient are checked within a tolerance; the silicon effect string must match the expected answer."
}
```

## How you are scored
A hidden verifier inspects each of the three scored output files independently. For each file the verifier compares your reported value to a reference expectation that is derived from the thermodynamic analysis reported in the literature. Comparisons are made with appropriate tolerances to account for the use of a different software implementation and database, while still ensuring that the result reflects a genuine reproduction of the underlying physics. The three stages carry weights that sum to 1.0, with the main thermodynamic quantities (phase fractions and partition coefficient) receiving the largest shares. Your total reward is the weighted sum of the individual stage scores. Merely reporting a number that matches the reference is not sufficient – the verifier may also check internal consistency of your output with the computational steps you performed.
