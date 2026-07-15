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
4. A CSV of estimated activation energies and Arrhenius rate constants for the target reactions at specified temperatures.
The agent must use the provided molecular structures, reaction list, and literature Ea values; the DFT calculations must use the specified functional protocol with an open‑source code.

## Assets

- Open-source DFT code (e.g., CP2K, ORCA, Quantum ESPRESSO): https://www.cp2k.org/
- Literature activation energies for SiH4-C3H8-H2 system reactions
- Molecular structures for gas-phase species
- List of reactions for free energy and rate constant computation

## Workflow steps

### Step 1: DFT Thermochemistry
- Role: scored
- Action: For each species in the provided structure file, perform geometry optimization with LDA (VWN functional) followed by free-energy and vibrational frequency calculation with GGA (PW91 functional) using an open-source DFT code. Extract enthalpy H, entropy S, and heat capacity Cp as functions of temperature. Report results at least at T = 298.15 K and any other temperatures required for subsequent ΔG calculations.
- Output file: `/app/outputs/step_01_thermochemistry.csv`
- Format: csv
- Contract: CSV with columns: species (string), T (float, K), H (float, kJ/mol), S (float, J/mol·K), Cp (float, J/mol·K)
- Scoring: scored by hidden verifier

### Step 2: Reaction Free Energy Differences
- Role: scored
- Action: For each reaction in the provided reaction list, compute the Gibbs free energy difference ΔG at 0 K using the free energies of products and reactants derived from Step 1. Report ΔG in kJ/mol.
- Output file: `/app/outputs/step_02_deltaG.csv`
- Format: csv
- Contract: CSV with columns: reaction_id (string), reactants (string), products (string), DeltaG_0K (float, kJ/mol)
- Scoring: scored by hidden verifier

### Step 3: LFER Correlation Fit
- Role: scored
- Action: Using the provided literature activation energies for the SiH4-C3H8-H2 reactions and the computed ΔG values from Step 2 for those same reactions, fit a linear free-energy relation of the form Ea = slope × ΔG + intercept. Only use reactions with ΔG > 0 for the fit; for ΔG ≤ 0 the activation energy is taken as zero. Report the fitted slope (dimensionless) and intercept (kJ/mol).
- Output file: `/app/outputs/step_03_LFER_fit.csv`
- Format: csv
- Contract: CSV with columns: parameter (string), value (float). parameter must be 'slope' (dimensionless) or 'intercept' (kJ/mol).
- Scoring: scored by hidden verifier

### Step 4: Arrhenius Rate Constants
- Role: scored (load-bearing)
- Action: For each reaction in the provided target set, estimate the activation energy Ea by applying the LFER correlation from Step 3 to the computed ΔG from Step 2 (Ea = 0 when ΔG ≤ 0). Then compute the Arrhenius rate constant k = A * exp(-Ea/(R*T)) with A = 1e14 s⁻¹ and temperature exponent n = 0, at the specified temperatures T. Report Ea and k for each reaction and temperature.
- Output file: `/app/outputs/step_04_rate_constants.csv`
- Format: csv
- Contract: CSV with columns: reaction_id (string), T (float, K), Ea (float, kJ/mol), A (float, s⁻¹), k (float, s⁻¹)
- Scoring: scored by hidden verifier

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
- target_policy: reference_match
- description: Thermochemical properties H, S, Cp for each species at the required temperatures.
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
- description: Reaction Gibbs free energy differences ΔG at 0 K.
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
- description: LFER fit parameters: slope (dimensionless) and intercept (kJ/mol).
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`
  - `units`: object

### step_04_rate_constants.csv
- path: `/app/outputs/step_04_rate_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Estimated activation energies and Arrhenius rate constants. Checker also verifies self-consistency: recomputes k from Ea and A.
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `T`, `Ea`, `A`, `k`
  - `units`:
    - `T`: K
    - `Ea`: kJ/mol
    - `A`: s⁻¹
    - `k`: s⁻¹

Notes: The task excludes the thermo-fluid reactor simulation (stage 4) due to dependence on an unrecoverable reference and underspecified geometry. The pipeline covers the core first-principles thermochemistry and rate constant estimation from DFT through LFER. Hidden checker compares submitted values to pre-computed references (using the same functional protocol) within tolerances that account for numerical differences between DFT codes, and also checks consistency of step 04.

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
      "target_policy": "reference_match",
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
      "description": "Thermochemical properties H, S, Cp for each species at the required temperatures."
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
      "description": "Reaction Gibbs free energy differences ΔG at 0 K."
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
      "description": "LFER fit parameters: slope (dimensionless) and intercept (kJ/mol)."
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
      "description": "Estimated activation energies and Arrhenius rate constants. Checker also verifies self-consistency: recomputes k from Ea and A."
    }
  ],
  "notes": "The task excludes the thermo-fluid reactor simulation (stage 4) due to dependence on an unrecoverable reference and underspecified geometry. The pipeline covers the core first-principles thermochemistry and rate constant estimation from DFT through LFER. Hidden checker compares submitted values to pre-computed references (using the same functional protocol) within tolerances that account for numerical differences between DFT codes, and also checks consistency of step 04."
}
```

## How you are scored
A hidden verifier independently evaluates each of the four output files. For the thermochemistry and ΔG tables, the verifier compares your reported values to pre‑computed reference values obtained with the same DFT protocol, using tolerances that account for numerical differences between DFT codes. For the LFER fit, the verifier checks that the slope and intercept match the correct fit derived from the same data and the rule that only reactions with ΔG > 0 are used. For the rate constants, the verifier first checks self‑consistency (recomputes k from your reported Ea and A) and then compares the Ea values against hidden reference values derived from the correct LFER rule. Your final reward is a weighted combination of the scores from the four stages. Reporting the paper's published numbers is not sufficient; you must genuinely execute the pipeline and produce artifacts that are consistent with the hidden reference computations.
