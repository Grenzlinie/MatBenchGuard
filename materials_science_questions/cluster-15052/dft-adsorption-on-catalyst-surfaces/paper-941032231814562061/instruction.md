# DFT Screening Protocol for Zr-Anchored Porphyrin NRR Catalysts

## Problem background
Electrocatalytic nitrogen reduction to ammonia under ambient conditions is a sustainable alternative to the energy‑intensive Haber‑Bosch process. Single‑atom catalysts anchored on two‑dimensional porphyrin sheets have shown promise, but their activity and selectivity are often limited by the competing hydrogen evolution reaction (HER). Coordination engineering – tuning the local atomic environment of the metal centre – offers a route to improve catalytic performance for the nitrogen reduction reaction (NRR). In this work, a series of Zr‑anchored porphyrin monolayers with varying C/N/O coordination patterns were designed and evaluated through a multi‑step computational screening protocol aimed at identifying candidates that spontaneously adsorb N₂, exhibit low free‑energy penalties for key proton‑electron transfer steps, and suppress H⁺ adsorption. The target of this reproduction is to implement that screening protocol and determine which of the considered catalysts pass the thermodynamic filters, what the NRR free‑energy landscape looks like for the best catalyst, and whether dynamic competition between N₂ and H⁺ favours N₂ coverage.

## Approach
The approach uses first‑principles density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional, a DFT‑D3 dispersion correction, and a Hubbard U term on Zr‑d electrons to capture strong correlation. After building slab models of a porphyrin monolayer with a single Zr atom coordinated by the specified pattern, spin‑polarised geometry optimizations and vibrational frequency calculations are performed to obtain total energies, zero‑point energies, and entropy corrections. Gibbs free energies of reaction intermediates are then computed within the Computational Hydrogen Electrode (CHE) model at 298.15 K.

The screening logic proceeds through three thermodynamic filters:
1) Spontaneous N₂ adsorption – the Gibbs free energy of N₂ binding (end‑on and side‑on geometries) must be negative.
2) First proton‑electron transfer – the free‑energy change for *N₂ + H⁺ + e⁻ → *N₂H must not exceed a chosen threshold.
3) Last proton‑electron transfer – the free‑energy change for *NH₂ + H⁺ + e⁻ → *NH₃ must not exceed the same threshold.

Catalysts that pass all three steps are carried forward. A fourth, competition‑based step uses ab initio molecular dynamics (AIMD) at room temperature to assess whether *N₂ coverage dominates over *H on the active site.

For the catalyst that emerges as the most active, all plausible NRR reaction pathways (distal, alternating, consecutive, enzymatic, and hybrid sequences) are mapped using the CHE model, and the pathway with the lowest onset potential (most positive elementary step) is identified, together with the potential‑determining step (PDS).

This reproduction focuses on six representative catalysts: the five that passed the full screening in the original study (ZrPP‑C₃O, ZrPP‑N₄, ZrPP‑N₂C₂‑n, ZrPP‑C₂O₂‑o, ZrPP‑C₂O₂‑n) and one candidate that was eliminated (ZrPP‑C₄).

## Reproduction target
1. Compute the Gibbs free energies of N₂ adsorption (ΔG*N₂), the first proton‑electron transfer (ΔG*N₂→*N₂H), and the last proton‑electron transfer (ΔG*NH₂→*NH₃) for all six catalysts in both end‑on and side‑on geometries, and write them to `step_02_free_energies.csv`.
2. Apply the three thermodynamic screening thresholds to produce the shortlist of catalysts that pass all steps; report the pass/fail status in `step_01_screening_shortlist.csv`.
3. For the catalyst ZrPP‑C₃O, explore the full NRR reaction network, compute Gibbs free energy diagrams, and determine the optimal pathway (lowest onset potential) along with the potential‑determining step. Report the result in `step_03_optimal_pathway.json`.
4. Perform AIMD on ZrPP‑C₃O at room temperature in the presence of both N₂ and proton sources. Analyze the trajectory to extract the final coverage fractions of *N₂ and *H and record them in `step_04_AIMD_result.json`, along with the pass/fail outcome for the fourth screening step (N₂ coverage ≥ H⁺ coverage).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build atomic models for six catalysts
- Role: process
- Action: Construct the unit cell/slab of a porphyrin monolayer and create the six Zr‑porphyrin catalysts: ZrPP‑C3O, ZrPP‑N4, ZrPP‑N2C2‑n, ZrPP‑C2O2‑o, ZrPP‑C2O2‑n, and the eliminated candidate ZrPP‑C4. Place a single Zr atom at the centre coordinated by the specified C/N/O pattern and add at least 15 Å vacuum layer. Generate both bare surfaces and adsorbate‑covered structures (end‑on and side‑on N2, N2H, NH2, NH3) as needed for subsequent steps.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: DFT structure optimization and vibrational frequencies
- Role: process
- Action: For each catalyst and adsorption configuration, perform spin‑polarized DFT calculations with PBE functional, DFT‑D3 dispersion correction, and a Hubbard U=2.0 eV on Zr‑d electrons. Use plane‑wave cutoff 450 eV, Γ‑centred k‑mesh appropriate for the slab, converge forces to <0.01 eV/Å. After geometry optimization, compute vibrational frequencies (Γ‑point only) to extract zero‑point energies and entropy corrections at 298.15 K. Also compute total energies of isolated N2, H2, and H2O (if needed) in the same computational setup. Summarize total energies and frequency data in a JSON file.
- Evidence: `/app/outputs/dft_energies_summary.json`

### Step 3: Compute Gibbs free energies for screening steps
- Role: scored (load-bearing)
- Action: Using the DFT energies and vibrational data from s02, compute Gibbs free energy of each intermediate as G = E_DFT + E_ZPE − T·S (T = 298.15 K). Then derive the adsorption/reaction free energies: ΔG*N2 (end‑on and side‑on), ΔG first proton‑electron transfer (*N2 → *N2H), and ΔG last proton‑electron transfer (*NH2 → *NH3) for every catalyst/configuration, applying the Computational Hydrogen Electrode (CHE) model. Output a CSV file with all values.
- Output file: `/app/outputs/step_02_free_energies.csv`
- Format: csv
- Contract: Columns: catalyst_id (string), geometry (end-on or side-on), Delta_G_N2_ads (float, eV), Delta_G_first_proton (float, eV), Delta_G_last_proton (float, eV). Numeric values with 2 decimal places.
- Scoring: scored by hidden verifier

### Step 4: Apply screening criteria and produce shortlist
- Role: scored
- Action: From the free energies, apply three thermodynamic screening steps: (1) catalysts with ΔG*N2 < 0 for at least one geometry are retained; (2) catalysts with ΔG first protonation ≤ 0.8 eV are retained; (3) catalysts with ΔG last protonation ≤ 0.8 eV are retained. Report pass/fail for each criterion and the final shortlist of catalysts that pass all three.
- Output file: `/app/outputs/step_01_screening_shortlist.csv`
- Format: csv
- Contract: Columns: catalyst_id (string), passed_step1 (bool), passed_step2 (bool), passed_step3 (bool), final_shortlist (bool). One row per catalyst (six considered).
- Scoring: scored by hidden verifier

### Step 5: Optimal NRR pathway for ZrPP‑C3O
- Role: scored (load-bearing)
- Action: For catalyst ZrPP‑C3O, explore all plausible NRR reaction pathways (distal, alternating, consecutive, enzymatic, and hybrid sequences such as EC and CEC). Compute Gibbs free energy diagrams using the CHE model. Identify the pathway with the lowest onset potential (most positive ΔG step) and report the sequence of intermediates, the potential‑determining step (PDS), and the onset potential.
- Output file: `/app/outputs/step_03_optimal_pathway.json`
- Format: json
- Contract: JSON object with keys: catalyst (string), optimal_pathway_name (string), steps (list of {intermediate: string, Delta_G: number (eV)}), PDS (string), onset_potential (float, eV).
- Scoring: scored by hidden verifier

### Step 6: AIMD competition between N2 and H⁺ on ZrPP‑C3O
- Role: scored (load-bearing)
- Action: Perform ab initio molecular dynamics (AIMD) on ZrPP‑C3O at room temperature in the presence of both N2 and proton species. Run for a sufficient duration (e.g., 10 ps) and analyze radial distribution functions/trajectory to extract final coverage fractions of *N2 and *H at adsorption sites. Determine whether the catalyst passes the fourth screening step (N2 coverage ≥ H⁺ coverage).
- Output file: `/app/outputs/step_04_AIMD_result.json`
- Format: json
- Contract: JSON object with keys: catalyst (string), temperature_K (number), total_time_ps (number), final_N2_coverage (float, fraction of sites occupied by N2), final_H_coverage (float, fraction of sites occupied by H), passed_step4 (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_free_energies.csv`
- `/app/outputs/step_01_screening_shortlist.csv`
- `/app/outputs/step_03_optimal_pathway.json`
- `/app/outputs/step_04_AIMD_result.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_free_energies.csv
- path: `/app/outputs/step_02_free_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Gibbs free energies for N2 adsorption and protonation steps for six catalysts. Checker compares against paper values within ±0.1 eV.
- schema:
  - `type`: table
  - `required_columns`: `catalyst_id`, `geometry`, `Delta_G_N2_ads`, `Delta_G_first_proton`, `Delta_G_last_proton`
  - `units`:
    - `Delta_G_N2_ads`: eV
    - `Delta_G_first_proton`: eV
    - `Delta_G_last_proton`: eV

### step_01_screening_shortlist.csv
- path: `/app/outputs/step_01_screening_shortlist.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Screening outcome: pass/fail for each thermodynamic step and final shortlist membership. Checker verifies the final shortlist consists of the five catalysts from the paper.
- schema:
  - `type`: table
  - `required_columns`: `catalyst_id`, `passed_step1`, `passed_step2`, `passed_step3`, `final_shortlist`

### step_03_optimal_pathway.json
- path: `/app/outputs/step_03_optimal_pathway.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimal NRR pathway details for ZrPP‑C3O including onset potential. Checker compares onset potential to paper’s 0.47 V within ±0.1 V.
- schema:
  - `type`: object
  - `required`:
    - `catalyst`: string
    - `optimal_pathway_name`: string
    - `steps`: array of {intermediate: string, Delta_G: number}
    - `PDS`: string
    - `onset_potential`: number
  - `units`:
    - `onset_potential`: eV

### step_04_AIMD_result.json
- path: `/app/outputs/step_04_AIMD_result.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: AIMD competition result for ZrPP‑C3O: N2 vs H⁺ coverage and passed_step4. Checker verifies passed_step4 is true and coverage ratios are plausible.
- schema:
  - `type`: object
  - `required`:
    - `catalyst`: string
    - `temperature_K`: number
    - `total_time_ps`: number
    - `final_N2_coverage`: number
    - `final_H_coverage`: number
    - `passed_step4`: boolean

Notes: Free energies, shortlist, and optimal pathway onset potential are compared against paper‑reported reference values with tolerances. AIMD result is checked for structural consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "catalyst_id",
          "geometry",
          "Delta_G_N2_ads",
          "Delta_G_first_proton",
          "Delta_G_last_proton"
        ],
        "units": {
          "Delta_G_N2_ads": "eV",
          "Delta_G_first_proton": "eV",
          "Delta_G_last_proton": "eV"
        }
      },
      "description": "Computed Gibbs free energies for N2 adsorption and protonation steps for six catalysts. Checker compares against paper values within ±0.1 eV."
    },
    {
      "file": "step_01_screening_shortlist.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "catalyst_id",
          "passed_step1",
          "passed_step2",
          "passed_step3",
          "final_shortlist"
        ]
      },
      "description": "Screening outcome: pass/fail for each thermodynamic step and final shortlist membership. Checker verifies the final shortlist consists of the five catalysts from the paper."
    },
    {
      "file": "step_03_optimal_pathway.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "catalyst": "string",
          "optimal_pathway_name": "string",
          "steps": "array of {intermediate: string, Delta_G: number}",
          "PDS": "string",
          "onset_potential": "number"
        },
        "units": {
          "onset_potential": "eV"
        }
      },
      "description": "Optimal NRR pathway details for ZrPP‑C3O including onset potential. Checker compares onset potential to paper’s 0.47 V within ±0.1 V."
    },
    {
      "file": "step_04_AIMD_result.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "catalyst": "string",
          "temperature_K": "number",
          "total_time_ps": "number",
          "final_N2_coverage": "number",
          "final_H_coverage": "number",
          "passed_step4": "boolean"
        }
      },
      "description": "AIMD competition result for ZrPP‑C3O: N2 vs H⁺ coverage and passed_step4. Checker verifies passed_step4 is true and coverage ratios are plausible."
    }
  ],
  "notes": "Free energies, shortlist, and optimal pathway onset potential are compared against paper‑reported reference values with tolerances. AIMD result is checked for structural consistency."
}
```

## How you are scored
Every artifact you produce (`step_02_free_energies.csv`, `step_01_screening_shortlist.csv`, `step_03_optimal_pathway.json`, `step_04_AIMD_result.json`) will be checked by a hidden automated verifier. The verifier has access to reference values derived from the original study and scores each artifact independently, then combines the scores by assigned weights into a final reward between 0 and 1. The free‑energy table is scored by comparing your computed ΔG values to the expected values within a small tolerance; the screening shortlist must exactly contain the correct set of catalysts; the optimal pathway’s onset potential is compared against a reference value; and the AIMD result is verified for physical plausibility and for the requirement that passed_step4 be true. The verifier does not require a specific DFT code, but your reported numbers must fall within the tolerance windows that account for the use of an open‑source alternative to the original implementation.
