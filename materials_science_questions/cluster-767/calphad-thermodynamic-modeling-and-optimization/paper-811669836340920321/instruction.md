# Gibbs Energy Minimization for Cementitious Solid-Aqueous Equilibria

## Problem background
Cementitious materials serve as engineered barriers in radioactive waste disposal, and long‑term predictions of their chemical stability rely on thermodynamic models. This task evaluates a solid‑solution–aqueous‑solution (SSAS) model based on Gibbs energy minimization (GEM) to predict phase equilibria and pore water compositions in the Na–Ca–Mg–Fe–Al–Si–S–H–O system. The model computes equilibrium phase amounts, aqueous speciation, pH, and total dissolved concentrations. The goal is to produce these quantities for CSH solubility in pure water as a function of Ca/Si ratio, and for cement pore waters of two aging times, using provided thermodynamic data and an open‑source GEM solver.

## Approach
The modeling approach uses Gibbs energy minimization (GEM), which finds the equilibrium distribution of species and phases given temperature, pressure, bulk composition, and standard‑state Gibbs energies for all species. The system includes an aqueous electrolyte with activity coefficients described by the extended Debye–Hückel equation (common third parameter 0.064), single‑component solids (portlandite, ettringite, hydrotalcite), and three ideal solid solutions: CSH1 (SiO₂, Ca₀.₉SiH₁.₈O₃.₈, CaH₂SiO₄·NaOH), CSH2 (Ca₀.₉SiH₁.₈O₃.₈, Ca₁.₇H₃.₄SiO₅.₄·4H₂O, CaH₂SiO₄·NaOH), and hydrogarnet (C₃AH₆, C₃FH₆, C₃AS₃). Thermodynamic data (standard‑state ΔG°₂₉₈.₁₅ for all aqueous species and solid end‑members) are provided. Cement bulk compositions from two public references are used as input together with water/solid ratio 0.5. Two variants of the sodium‑bearing end‑member’s ΔG° are considered: an uncorrected and a corrected value, to assess the model’s sensitivity to this parameter. All calculations are performed at 298.15 K and 1 bar.

## Reproduction target
Implement the GEM‑based SSAS model using an open‑source GEM solver. Run equilibrium calculations for 10 CSH solubility conditions (Ca/Si mole ratios 0.2, 0.4, …, 2.0 with 1 mol (CaO+SiO₂) per 1 kg H₂O), and for cement porewater compositions of an 84‑day and a 300‑day Portland cement at a water/solid ratio of 0.5, each with two Na end‑member energies (uncorrected ΔG° = −2211864 J/mol and corrected ΔG° = −2194864 J/mol). For each case, extract total aqueous concentrations (mol/L) of Ca, Si, Al, SO₄, Mg, Na and pH, and write them to a CSV file `predictions.csv` with columns: test_case, Ca, Si, Al, SO4, Mg, Na, pH. The test_case names are CSH_0.2 … CSH_2.0, PW84U, PW84C, PW300U, PW300C.

## Assets

- 84-day Portland cement composition
- 300-day Portland cement composition
- Open-source Gibbs energy minimization code: http://gems.web.psi.ch/
- Standard Gibbs energies (ΔG°₂₉₈.₁₅) and end-member stoichiometries

## Workflow steps

### Step 1: Obtain cement bulk compositions
- Role: process
- Action: Retrieve the bulk oxide chemical compositions (mass fractions of Na₂O, CaO, MgO, Fe₂O₃, Al₂O₃, SiO₂, SO₃, etc.) for the 84-day (Page & Vennesland 1983) and 300-day (Andersson et al. 1989) Portland cement samples from the cited references.
- Evidence: `/app/outputs/composition_data.json`

### Step 2: Assemble GEM input system
- Role: process
- Action: Construct the multiphase thermodynamic system for Gibbs energy minimization using an open-source GEM solver. Include: (i) aqueous electrolyte with all species from the provided thermodynamic list and activity coefficients by the extended Debye-Hückel equation (common third parameter 0.064), (ii) single-component solids CH, Aft, Htc, (iii) ideal solid solutions CSH1 (end-members SiO₂, Ca₀.₉SiH₁.₈O₃.₈, CaH₂SiO₄·NaOH), CSH2 (end-members Ca₀.₉SiH₁.₈O₃.₈, Ca₁.₇H₃.₄SiO₅.₄·4H₂O, CaH₂SiO₄·NaOH), and hydrogarnet (end-members C₃AH₆, C₃FH₆, C₃AS₃). Use the standard Gibbs energies provided for each end-member and species. Set T=298.15 K, P=1 bar. Ignore potassium as it is not part of the modeled system.
- Evidence: `/app/outputs/system_definition.log`

### Step 3: Run GEM simulations for CSH solubility and cement porewater
- Role: scored (load-bearing)
- Action: Perform GEM equilibrium calculations for all test cases. CSH solubility: bulk of 1 mol (CaO+SiO₂) per 1 kg H₂O at Ca/Si mole ratios 0.2, 0.4, 0.6, …, 2.0. Cement porewater: bulk composition defined by the cement oxide masses from step 01 and a water/solid ratio of 0.5 kg H₂O per kg solids, for both 84-day and 300-day cements. For each cement, run the simulation first with the uncorrected ΔG°(CN₀.₅SH₁.₅) = −2211864 J/mol and then with the corrected ΔG° = −2194864 J/mol. For every case extract the total aqueous concentrations (mol/L) of Ca, Si, Al, SO₄, Mg, Na and the pH. Write all results to predictions.csv with columns: test_case, Ca, Si, Al, SO4, Mg, Na, pH.
- Output file: `/app/outputs/predictions.csv`
- Format: csv
- Contract: Columns: test_case (string; one of CSH_0.2, CSH_0.4, …, CSH_2.0, PW84U, PW84C, PW300U, PW300C), Ca (float, mol/L), Si (float, mol/L), Al (float, mol/L), SO4 (float, mol/L), Mg (float, mol/L), Na (float, mol/L), pH (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predictions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predictions.csv
- path: `/app/outputs/predictions.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted equilibrium total aqueous concentrations and pH from the GEM-based SSAS model. The checker recomputes the sum of absolute log10 differences between these values and the paper's reported results; full credit is awarded when total error is within the hidden tolerance, with linear decay beyond it.
- schema:
  - `type`: table
  - `required_columns`: `test_case`, `Ca`, `Si`, `Al`, `SO4`, `Mg`, `Na`, `pH`
  - `units`:
    - `Ca`: mol/L
    - `Si`: mol/L
    - `Al`: mol/L
    - `SO4`: mol/L
    - `Mg`: mol/L
    - `Na`: mol/L
    - `pH`: dimensionless

Notes: The thermodynamic data (ΔG° values and stoichiometries) are provided in the instruction document. The cement bulk compositions must be retrieved from the specified references. The GEM solver may be any open-source implementation, e.g., GEMS3K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "test_case",
          "Ca",
          "Si",
          "Al",
          "SO4",
          "Mg",
          "Na",
          "pH"
        ],
        "units": {
          "Ca": "mol/L",
          "Si": "mol/L",
          "Al": "mol/L",
          "SO4": "mol/L",
          "Mg": "mol/L",
          "Na": "mol/L",
          "pH": "dimensionless"
        }
      },
      "description": "Predicted equilibrium total aqueous concentrations and pH from the GEM-based SSAS model. The checker recomputes the sum of absolute log10 differences between these values and the paper's reported results; full credit is awarded when total error is within the hidden tolerance, with linear decay beyond it."
    }
  ],
  "notes": "The thermodynamic data (ΔG° values and stoichiometries) are provided in the instruction document. The cement bulk compositions must be retrieved from the specified references. The GEM solver may be any open-source implementation, e.g., GEMS3K."
}
```

## How you are scored
A hidden verifier will independently score the submitted `predictions.csv`. It reads your predicted values and compares them to reference values derived from experimental data using a metric based on the sum of absolute differences in log‑scale concentrations, with a tolerance that accounts for solver‑to‑solver variability. The reward is computed from the total error relative to a hidden threshold. Additionally, the verifier may check structural trends (e.g., that the corrected model yields a noticeable shift relative to the uncorrected model for the cement pore water cases). The final reward combines the scoring of the scored artifact; simply reporting known numbers from the literature is insufficient because the tolerance is set to reward a genuine re‑run of the GEM computation.
