# Methanol Dehydrogenation on Rh(111): DFT and Microkinetic Modeling

## Problem background
Methanol dehydrogenation on the Rh(111) surface is prototypical for hydrogen production from liquid methanol for fuel cells. The reaction network involves multiple parallel pathways (initial O–H vs. C–H bond scission, followed by further dehydrogenations) and the dominant mechanism can shift with temperature and pressure. The challenge is to predict, from first principles, which pathways dominate, what surface coverages result, and how the overall rate, apparent activation energy, and reaction order depend on conditions.

## Approach
The workflow combines periodic density functional theory (DFT) with microkinetic modeling. First, a Rh(111) slab model is built and DFT is used to optimize geometries of all adsorbed intermediates and to locate transition states for every O–H and C–H bond scission step. Adsorption energies, activation barriers, and vibrational frequencies are computed with a GGA functional (PW91 or PBE) in an open-source DFT code. The coverage dependence of CO adsorption energy is also determined separately. These DFT-derived parameters then feed a 14-step microkinetic model that uses transition-state theory for forward rate constants and a coverage-dependent CO binding energy. Steady-state equations are solved for two regimes: ultra-high vacuum (100–300 K, 10⁻⁶ Torr) and high-temperature/high-pressure (500–1000 K, 0.025–375 Torr). From the solution we extract dominant pathways (via flux analysis), surface coverages versus temperature, overall reaction rates versus temperature, apparent activation energies, and reaction orders.

## Reproduction target
The goal is to produce two scored artifacts:
(1) DFT adsorption energies for ten key surface intermediates (CH₃OH, CH₃O, CH₂OH, CH₂O, CHOH, CHO, COH, CO, H, H₂) on Rh(111) in kcal/mol, written to `dft_adsorption_energies.json`.
(2) Microkinetic simulation results written to `microkinetic_results.json`, containing:
    - dominant reaction pathways (list of strings) under UHV and high-T/p conditions;
    - a series of temperatures (in K) with the corresponding coverages (in ML) of CO, COH, and vacant sites under UHV;
    - a series of temperatures and pressures (in K and Torr) with the overall methanol decomposition rate under high-T/p conditions;
    - a series of temperatures (in K) with the apparent activation energy (in kcal/mol) at 375 Torr;
    - a series of methanol partial pressures (in Torr) with the reaction order at 900 K.
All quantities must be derived from your own DFT calculations and microkinetic solver; the task is to re-produce the physical trends, not to match a pre-given table.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- Rh pseudopotential (PBE/PW91): http://www.pseudo-dojo.org/
- Python with numpy and scipy: numpy scipy

## Workflow steps

### Step 1: DFT calculations of adsorption geometries and transition states
- Role: process
- Action: Build a Rh(111) 2×2 slab with 10 Å vacuum, perform geometry optimizations for all adsorbed intermediates (CH₃OH, CH₃O, CH₂OH, CH₂O, CHOH, CHO, COH, CO, H, H₂) and transition states for all 11 elementary O‑H and C‑H bond scission steps. Compute adsorption energies, activation barriers, and vibrational frequencies using the PW91 (or PBE) functional within an open-source DFT code.
- Evidence: `/app/outputs/dft_calc_log.txt`

### Step 2: CO adsorption energy as a function of coverage
- Role: process
- Action: Compute CO binding energies on Rh(111) at several coverages (e.g., 1/4, 1/2, 3/4, 1 ML) to derive the linear correction E_ads^CO(θ) = -25.5 θ + 52.0 kcal/mol.
- Evidence: `/app/outputs/co_coverage_calc_log.txt`

### Step 3: Report DFT adsorption energies
- Role: scored
- Action: Assemble the computed adsorption energies (most stable configuration, after zero‑point energy correction if available) for all 10 key species and write them to dft_adsorption_energies.json.
- Output file: `/app/outputs/dft_adsorption_energies.json`
- Format: json
- Contract: JSON object: { "CH3OH": number, "CH3O": number, "CH2OH": number, "CH2O": number, "CHOH": number, "CHO": number, "COH": number, "CO": number, "H": number, "H2": number } (units: kcal/mol)
- Scoring: scored by hidden verifier

### Step 4: Microkinetic simulation and analysis
- Role: scored (load-bearing)
- Action: Build the 14‑step microkinetic model using the DFT‑derived adsorption energies, activation barriers, vibrational frequencies, and the CO coverage relation. Solve the steady‑state equations for the UHV regime (100–300 K, 10⁻⁶ Torr) and the high‑T/p regime (500–1000 K, 0.025–375.03 Torr). Extract surface coverages, elementary step rates, overall rate, dominant pathways, apparent activation energy vs. temperature, and methanol reaction order vs. pressure. Write all results to microkinetic_results.json.
- Output file: `/app/outputs/microkinetic_results.json`
- Format: json
- Contract: JSON object with keys: "dominant_pathways" (list of strings), "coverage_vs_T_UHV" (list of {T, theta_CO, theta_COH, theta_vacant}), "rate_vs_T_highP" (list of {T, P, rate}), "apparent_activation_energy_vs_T" (list of {T, H_star}), "reaction_order_vs_p" (list of {P, alpha}); all numeric values in the units reported in the paper (K, ML, Torr, kcal/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_adsorption_energies.json`
- `/app/outputs/microkinetic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_adsorption_energies.json
- path: `/app/outputs/dft_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed DFT adsorption energies (most stable configuration, ZPE corrected if available) for all key intermediates. Values are compared to the paper's reported adsorption energies with a per-species tolerance to account for functional/code differences.
- schema:
  - `type`: object
  - `required`: `CH3OH`, `CH3O`, `CH2OH`, `CH2O`, `CHOH`, `CHO`, `COH`, `CO`, `H`, `H2`
  - `properties`:
    - `CH3OH`:
      - `type`: number
      - `unit`: kcal/mol
    - `CH3O`:
      - `type`: number
      - `unit`: kcal/mol
    - `CH2OH`:
      - `type`: number
      - `unit`: kcal/mol
    - `CH2O`:
      - `type`: number
      - `unit`: kcal/mol
    - `CHOH`:
      - `type`: number
      - `unit`: kcal/mol
    - `CHO`:
      - `type`: number
      - `unit`: kcal/mol
    - `COH`:
      - `type`: number
      - `unit`: kcal/mol
    - `CO`:
      - `type`: number
      - `unit`: kcal/mol
    - `H`:
      - `type`: number
      - `unit`: kcal/mol
    - `H2`:
      - `type`: number
      - `unit`: kcal/mol

### microkinetic_results.json
- path: `/app/outputs/microkinetic_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Microkinetic simulation results including dominant reaction pathways, CO/COH coverages vs temperature under UHV, overall rate vs temperature at high pressures, apparent activation energy vs temperature, and methanol reaction order vs pressure. The checker validates structural trends and pattern matches rather than exact numeric equality.
- schema:
  - `type`: object
  - `required`: `dominant_pathways`, `coverage_vs_T_UHV`, `rate_vs_T_highP`, `apparent_activation_energy_vs_T`, `reaction_order_vs_p`
  - `properties`:
    - `dominant_pathways`:
      - `type`: array
      - `items`:
        - `type`: string
    - `coverage_vs_T_UHV`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `T`, `theta_CO`, `theta_COH`, `theta_vacant`
    - `rate_vs_T_highP`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `T`, `P`, `rate`
    - `apparent_activation_energy_vs_T`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `T`, `H_star`
    - `reaction_order_vs_p`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `P`, `alpha`

Notes: Tolerance for DFT adsorption energies is set on a per-species basis to account for expected systematic shifts between the open-source DFT implementation and the paper's DMol³ results. The microkinetic results are evaluated on the correctness of qualitative trends (dominant pathways, peak temperatures, monotonicity of activation energy, pressure dependence of reaction order).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CH3OH",
          "CH3O",
          "CH2OH",
          "CH2O",
          "CHOH",
          "CHO",
          "COH",
          "CO",
          "H",
          "H2"
        ],
        "properties": {
          "CH3OH": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "CH3O": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "CH2OH": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "CH2O": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "CHOH": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "CHO": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "COH": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "CO": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "H": {
            "type": "number",
            "unit": "kcal/mol"
          },
          "H2": {
            "type": "number",
            "unit": "kcal/mol"
          }
        }
      },
      "description": "Computed DFT adsorption energies (most stable configuration, ZPE corrected if available) for all key intermediates. Values are compared to the paper's reported adsorption energies with a per-species tolerance to account for functional/code differences."
    },
    {
      "file": "microkinetic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "dominant_pathways",
          "coverage_vs_T_UHV",
          "rate_vs_T_highP",
          "apparent_activation_energy_vs_T",
          "reaction_order_vs_p"
        ],
        "properties": {
          "dominant_pathways": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "coverage_vs_T_UHV": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "T",
                "theta_CO",
                "theta_COH",
                "theta_vacant"
              ]
            }
          },
          "rate_vs_T_highP": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "T",
                "P",
                "rate"
              ]
            }
          },
          "apparent_activation_energy_vs_T": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "T",
                "H_star"
              ]
            }
          },
          "reaction_order_vs_p": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "P",
                "alpha"
              ]
            }
          }
        }
      },
      "description": "Microkinetic simulation results including dominant reaction pathways, CO/COH coverages vs temperature under UHV, overall rate vs temperature at high pressures, apparent activation energy vs temperature, and methanol reaction order vs pressure. The checker validates structural trends and pattern matches rather than exact numeric equality."
    }
  ],
  "notes": "Tolerance for DFT adsorption energies is set on a per-species basis to account for expected systematic shifts between the open-source DFT implementation and the paper's DMol³ results. The microkinetic results are evaluated on the correctness of qualitative trends (dominant pathways, peak temperatures, monotonicity of activation energy, pressure dependence of reaction order)."
}
```

## How you are scored
A hidden verifier scores each workflow stage's output artifact independently and combines the scores with predetermined weights into a final reward.

For the DFT adsorption energies (Step 3), the verifier compares your computed value for each species to a hidden reference within a per‑species tolerance; species that fall within tolerance earn credit.

For the microkinetic results (Step 4), the verifier performs a structural audit: it checks that the reported dominant pathways follow the expected physical ordering under the two condition regimes, that coverage and rate curves exhibit the correct shape and peak positions (e.g., a CO coverage maximum near 160 K in UHV, a rate peak in the 850‑950 K range at high pressures), that the apparent activation energy decreases monotonically with temperature, and that the methanol reaction order at 900 K decreases with increasing partial pressure. The verifier does not require exact numeric equality but assesses whether your results are physically consistent with the reaction model you built.

Simply reporting the paper’s published numbers without executing the DFT and microkinetic workflow will not satisfy the verifier’s checks, because the trends must emerge from your own calculations.
