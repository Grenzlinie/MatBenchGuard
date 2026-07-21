# DFT Thermochemistry and LFER for Gas-Phase Reaction Rates

## Problem background
High-temperature chemical vapor deposition (HTCVD) of silicon carbide (SiC) requires gas-phase reaction rate constants for reactor simulations, but experimental kinetic data are often missing for new precursor chemistries. This task implements a simulation framework that estimates Arrhenius parameters from first-principles DFT thermochemistry combined with a linear free-energy relation (LFER) observed in a reference system, enabling prediction of reaction rates for a new chlorinated precursor system without dedicated experiments.

## Approach
The framework relies on the observation that for gas-phase reactions, the activation energy Ea correlates with the Gibbs free energy difference ΔG through a linear free-energy relation (LFER) when ΔG is positive; for exergonic reactions (ΔG ≤ 0), Ea is near zero. First, thermodynamic properties (enthalpy, entropy, heat capacity) for all relevant gas-phase species are computed from first principles using density functional theory (DFT) with a two-functional protocol: geometry optimization at the LDA (VWN) level, followed by free-energy and vibrational analysis at the GGA (PW91) level. Reaction Gibbs free energies ΔG are then calculated from the product–reactant free-energy differences. Using a provided set of literature activation energies for the SiH₄‑C₃H₈‑H₂ system, a linear fit Ea = slope × ΔG + intercept is obtained using only reactions with ΔG > 0. This LFER is then applied to new reactions from the SiCl₄‑C₃H₈‑H₂ system to estimate their activation energies. Finally, Arrhenius rate constants k = A exp(‑Ea/RT) are assembled with a fixed pre‑exponential factor A = 10¹⁴ s⁻¹ and temperature exponent n = 0. The entire pipeline is executed with an open‑source DFT code (e.g., CP2K, ORCA, or Quantum ESPRESSO) instead of the proprietary DMol³ originally used.

## Reproduction target
Produce the four scored artifacts:
1. A CSV of thermochemical properties (H, S, Cp) at 298.15 K for the provided gas-phase species.
2. A CSV of reaction ΔG at 0 K for the provided list of reactions.
3. A CSV containing the fitted LFER slope and intercept from the correlation.
4. A CSV of estimated activation energies and Arrhenius rate constants for the target reactions at specified temperatures (2000 K and 2500 K).

The agent must use the provided molecular structures, reaction list, and literature Ea values; the DFT calculations must use the specified functional protocol with an open‑source code.

## Assets
All required input files are located under `/app/assets`:

- Molecular structures for gas-phase species: `/app/assets/structures.xyz`  
  (contains initial atomic coordinates/connectivity for all required species; use any format such as XYZ or SMILES)
- Reaction list for free energy and rate constant computation: `/app/assets/reactions.csv`  
  (each row gives a reaction with a unique `reaction_id`, `reactants` string, and `products` string; includes both SiH₄‑C₃H₈‑H₂ reactions (for LFER) and SiCl₄‑C₃H₈‑H₂ reactions)
- Literature activation energies for SiH₄‑C₃H₈‑H₂ system reactions: `/app/assets/literature_Ea.csv`  
  (CSV with columns `reaction_id` and `Ea_kJmol`; extracted from Ref. [3] in the paper)
- Open-source DFT code (e.g., CP2K, ORCA, Quantum ESPRESSO): https://www.cp2k.org/  
  (any DFT code that supports LDA (VWN) optimization and GGA (PW91) vibrational analysis is acceptable)

## Workflow steps

### Step 1: DFT Thermochemistry
- Role: scored
- Action: For each species in `/app/assets/structures.xyz`, perform geometry optimization with LDA (VWN functional) followed by free-energy and vibrational frequency calculation with GGA (PW91 functional) using an open-source DFT code. Extract enthalpy H, entropy S, and heat capacity Cp as functions of temperature. Report results at least at T = 298.15 K (other temperatures required for subsequent ΔG calculations should also be reported if needed).
- Output file: `/app/outputs/step_01_thermochemistry.csv`
- Format: csv
- Contract: CSV with columns: species (string), T (float, K), H (float, kJ/mol), S (float, J/mol·K), Cp (float, J/mol·K)
- Scoring: The verifier checks that every expected species is present at 298.15 K and that the reported H, S, Cp values fall within very wide physical plausibility bounds. No numerical comparison to hidden reference values is performed for this step.

### Step 2: Reaction Free Energy Differences
- Role: scored
- Action: For each reaction in `/app/assets/reactions.csv`, compute the Gibbs free energy difference ΔG at 0 K using the free energies of products and reactants derived from Step 1. Report ΔG in kJ/mol.
- Output file: `/app/outputs/step_02_deltaG.csv`
- Format: csv
- Contract: CSV with columns: reaction_id (string), reactants (string), products (string), DeltaG_0K (float, kJ/mol)
- Scoring: scored by hidden verifier comparing your reported values to pre‑computed reference values within specified tolerances.

### Step 3: LFER Correlation Fit
- Role: scored
- Action: Using the literature activation energies from `/app/assets/literature_Ea.csv` together with the computed ΔG values from Step 2 for those same reactions, fit a linear free-energy relation of the form Ea = slope × ΔG + intercept. Only use reactions with ΔG > 0 for the fit; for ΔG ≤ 0 the activation energy is taken as zero. Report the fitted slope (dimensionless) and intercept (kJ/mol).
- Output file: `/app/outputs/step_03_LFER_fit.csv`
- Format: csv
- Contract: CSV with columns: parameter (string), value (float). parameter must be 'slope' (dimensionless) or 'intercept' (kJ/mol).
- Scoring: scored by hidden verifier; the verifier recomputes the LFER from your ΔG values and the hidden literature data, and checks that your slope and intercept match the recomputed values within tight tolerances.

### Step 4: Arrhenius Rate Constants
- Role: scored (load-bearing)
- Action: For each reaction listed in `/app/assets/reactions.csv` (the same list used in Step 2), estimate the activation energy Ea by applying the LFER correlation from Step 3 to the computed ΔG from Step 2 (Ea = 0 when ΔG ≤ 0). Then compute the Arrhenius rate constant k = A * exp(-Ea/(R*T)) with pre‑exponential factor A = 1e14 s⁻¹, temperature exponent n = 0, and gas constant R = 0.0083144621 kJ mol⁻¹ K⁻¹. Perform this calculation at the two specified temperatures: **T = 2000 K** and **T = 2500 K**. Report Ea and k for each reaction at each temperature.
- Output file: `/app/outputs/step_04_rate_constants.csv`
- Format: csv
- Contract: CSV with columns: reaction_id (string), T (float, K), Ea (float, kJ/mol), A (float, s⁻¹), k (float, s⁻¹)
- Scoring: scored by hidden verifier that checks self‑consistency (recomputes k from your Ea and A) and compares Ea against expected values derived from the correct LFER rule.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermochemistry.csv`
- `/app/outputs/step_02_deltaG.csv`
- `/app/outputs/step_03_LFER_fit.csv`
- `/app/outputs/step_04_rate_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermochemistry.csv
- path: `/app/outputs/step_01_thermochemistry.csv`
- format: csv
- purpose: scored
- target_policy: presence_sanity
- description: Thermochemical properties H, S, Cp for each species at the required temperatures. Verifier checks species presence and physical plausibility.
- schema:
  - `type`: table
  - `required_columns`: `species`, `T`, `H`, `S`, `Cp`
  - `units`:
    - `T`: K
    - `H`: kJ/mol
    - `S`: J/mol·K
    - `Cp`: J/mol·K

### step_02_deltaG.csv
- path: `/app/outputs/step_02_deltaG.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reaction Gibbs free energy differences ΔG at 0 K. Verifier compares against reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `reactants`, `products`, `DeltaG_0K`
  - `units`:
    - `DeltaG_0K`: kJ/mol

### step_03_LFER_fit.csv
- path: `/app/outputs/step_03_LFER_fit.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: LFER fit parameters: slope (dimensionless) and intercept (kJ/mol). Verifier recomputes the fit from your ΔG and the hidden literature data.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`
  - `units`: object

### step_04_rate_constants.csv
- path: `/app/outputs/step_04_rate_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Estimated activation energies and Arrhenius rate constants at 2000 K and 2500 K. Verifier checks self-consistency (recomputes k from Ea and A) and compares Ea against expected values.
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `T`, `Ea`, `A`, `k`
  - `units`:
    - `T`: K
    - `Ea`: kJ/mol
    - `A`: s⁻¹
    - `k`: s⁻¹

Notes: The task excludes the thermo-fluid reactor simulation (stage 4) due to dependence on an unrecoverable reference and underspecified geometry. The pipeline covers the core first-principles thermochemistry and rate constant estimation from DFT through LFER.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermochemistry.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "presence_sanity",
      "schema": {
        "type": "table",
        "required_columns": [
          "species",
          "T",
          "H",
          "S",
          "Cp"
        ],
        "units": {
          "T": "K",
          "H": "kJ/mol",
          "S": "J/mol·K",
          "Cp": "J/mol·K"
        }
      },
      "description": "Thermochemical properties H, S, Cp for each species at the required temperatures. Verifier checks species presence and physical plausibility."
    },
    {
      "file": "step_02_deltaG.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "reactants",
          "products",
          "DeltaG_0K"
        ],
        "units": {
          "DeltaG_0K": "kJ/mol"
        }
      },
      "description": "Reaction Gibbs free energy differences ΔG at 0 K. Verifier compares against reference values within tolerances."
    },
    {
      "file": "step_03_LFER_fit.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value"
        ],
        "units": {}
      },
      "description": "LFER fit parameters: slope (dimensionless) and intercept (kJ/mol). Verifier recomputes the fit from your ΔG and the hidden literature data."
    },
    {
      "file": "step_04_rate_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "T",
          "Ea",
          "A",
          "k"
        ],
        "units": {
          "T": "K",
          "Ea": "kJ/mol",
          "A": "s⁻¹",
          "k": "s⁻¹"
        }
      },
      "description": "Estimated activation energies and Arrhenius rate constants at 2000 K and 2500 K. Verifier checks self-consistency and compares Ea against expected values."
    }
  ],
  "notes": "The task excludes the thermo-fluid reactor simulation (stage 4) due to dependence on an unrecoverable reference and underspecified geometry. The pipeline covers the core first-principles thermochemistry and rate constant estimation from DFT through LFER."
}
```

## How you are scored
A hidden verifier independently evaluates each of the four output files. For the thermochemistry table, the verifier only checks that all expected species are present at 298.15 K and that the reported H, S, Cp fall within very wide physical plausibility ranges; no numerical comparison to reference values is performed. For the ΔG table, the verifier compares your reported values to pre‑computed reference values obtained with the same DFT protocol, using generous tolerances. For the LFER fit, the verifier recomputes the slope and intercept from your own ΔG values and the hidden literature Ea data, checking for exact agreement within numerical tolerance. For the rate constants, the verifier first checks self‑consistency (recomputes k from your reported Ea and A) and then compares the Ea values against hidden reference values derived from the correct LFER rule. Your final reward is a weighted combination of the scores from the four stages. Reporting the paper's published numbers is not sufficient; you must genuinely execute the pipeline and produce artifacts that are consistent with the hidden reference computations.