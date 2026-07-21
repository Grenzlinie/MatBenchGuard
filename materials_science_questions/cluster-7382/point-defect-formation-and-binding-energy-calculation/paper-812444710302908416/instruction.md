## Problem background
Nonstoichiometric compounds exhibit deviations from ideal stoichiometry due to the presence of point defects. When the deviation is large, interactions between defects become important and can significantly affect the thermodynamic activity of the components. Characterizing the predominant defect type and the free energy of interaction between like defects is essential for understanding the stability and phase behavior of such materials. This task addresses three model systems: yttrium dihydride (YH₂₋δ, hydrogen deficient), cerium dihydride (CeH₂₊δ, hydrogen excess), and thorium monocarbide (ThC₁₋δ, carbon deficient).

## Approach
The general approach is based on a theoretical extension of the Bragg–Williams approximation, which provides analytical activity–composition relations for compounds MX_s with large deviations from stoichiometry, assuming only one type of point defect is dominant and that there are pairwise interactions among the randomly distributed defects. For a given compound, one examines different candidate defect models (e.g., M vacancies, X interstitials, X substitutionals for positive deviations; X vacancies, M interstitials, M substitutionals for negative deviations) and, for each model, defines diagnostic variables y and x that are linear functions when the assumed defect is indeed predominant:
y = p + q x   (where p contains the defect formation energy and q is related to the pairwise interaction free energy ξ).

By plotting the measured activity a_X (or a_M) against composition δ in terms of y and x for each defect model, one identifies the model that yields the best straight line (highest R²). The slope q of that line then gives the interaction free energy ξ, and, for the case of YH₂₋δ, the temperature dependence of ξ is further used to extract the vacancy‑pair formation enthalpy and entropy.

### Explicit formulas for y and x
For a compound with stoichiometric formula MX_s:
- **Positive deviation (δ > 0, formula MX_{s+δ})** – the three candidate defect models are M vacancies, X interstitials, and X substitutionals. The formulas for y = y(a_X, δ) and x = x(δ) are:
  1) M vacancies:  
     y = ln[ a_X · ((s+δ)/δ)^{1/s} ]  
     x = δ(2s+δ) / (s+δ)²
  2) X interstitials:  
     y = ln[ a_X · ((α − δ)/δ) ]  
     x = δ  
     (α is the number of interstitial sites per M site; for the fluorite‑related dihydrides α = 2.)
  3) X substitutionals:  
     y = ln[ a_X · ((s+1+δ)/δ)^{1/(s+1)} ]  
     x = δ(2s+δ+2) / (s+1+δ)²

- **Negative deviation (δ > 0, formula MX_{s−δ})** – the candidates are X vacancies, M interstitials, and M substitutionals:
  1) X vacancies:  
     y = ln( δ a_X / (s−δ) )  
     x = δ
  2) M interstitials:  
     y = ln a_X + (1/s) ln[ α^α (s−δ)^α δ / (α s − αδ − δ)^{α+1} ]  
     x = δ(2s−δ) / (s−δ)²
  3) M substitutionals:  
     y = ln a_X + (s/(s+1)) ln[ (s² + s − sδ) δ^{1/s} ] − ln[ (s+1)(s−δ) ]  
     x = δ(2s+2−δ) / (s+1−δ)²

For thorium monocarbide, the data are reported as thorium activity a_Th in ThC₁₋δ. Analyse the compound as CTh₁₊δ with M = C, X = Th and s = 1. In that case a_X = a_Th and δ is the deviation from the stoichiometric CTh composition (δ > 0 corresponds to positive deviation).

### Conversion of slope to interaction energy
Once the best model is identified and its slope q is obtained, the pairwise interaction free energy ξ is computed from q. The exact relation depends on the defect type:
- For X vacancies (negative deviation):  ξ = − q · s · kT / z_X  
- For X interstitials (positive deviation): ξ = q · α · kT / z_I  (with α the interstitial sites per M site)
- For M vacancies (positive deviation): the slope q = (z_M ξ) / (2 s kT) so ξ = 2 s kT q / z_M  (but one can use the derived formula from the origin paper; in practice for CeH₂ and ThC the appropriate conversion is applied.)

To perform the conversion, you need the coordination numbers z_X, z_I, z_M appropriate for the crystal structures. Use the following structural parameters:
- YH₂₋δ: s = 2, H‑vacancy: z_X = 6
- CeH₂₊δ: s = 2, α = 2, H‑interstitial: z_I = 12
- CTh₁₊δ (ThC₁₋δ): s = 1, α = 1, C‑vacancy: z_M = 6  (for NaCl‑type, where M = C)

These z values are based on the nearest‑neighbour coordination of the defect sublattice in the fluorite (dihydrides) and rock‑salt (ThC) structures.

## Reproduction target
Apply the above method to the experimental activity data of the three systems, using the isotherms reported in the original publications. The goal is to:
1. Determine the predominant defect type in each system (verified by the highest R² among candidate models).
2. Compute the pairwise defect interaction free energy ξ at each reported temperature.
3. For YH₂₋δ, additionally determine the vacancy‑pair formation enthalpy (in kcal/mol) and entropy (in cal/(deg·mol)) from the linear temperature dependence of ξ.

All temperatures that appear in the published datasets must be included. Specifically:
- YH₂₋δ: isotherms at 601, 651, 701, 750, 800, 850, 899, and 949 °C (Yannopoulos et al.)
- CeH₂₊δ: isotherms at 300, 400, 500, 550, 600, and 650 °C (Lundin data)
- ThC₁₋δ (as CTh₁₊δ): isotherms at 1000, 1100, and 1200 K (Satow data).

## Assets
You need the original experimental activity data from the following publications. Digitise or manually extract the data points from the figures/tables.

1. **YH₂₋δ hydrogen activity data**  
   Source: Yannopoulos, L. N., Edwards, R. K. and Wahlbeck, P. G., J. Phys. Chem. 69, 2512 (1965).  
   Access: DOI 10.1021/j100892a006

2. **CeH₂₊δ hydrogen activity data**  
   Source: Lundin, C. E., Trans. AIME 236, 978 (1966).  
   Access: no DOI; find via publisher or library.

3. **ThC₁₋δ thorium activity data**  
   Source: Satow, T., J. Nucl. Mater. 21, 255 (1967).  
   Access: DOI 10.1016/0022-3115(67)90184-5

In addition, you may use the standard Python scientific stack (numpy, scipy, matplotlib, pandas) for data processing and linear regression.

## Workflow steps

### Step 1: Extract experimental activity data
- Role: process
- Action: Digitise or manually extract the activity‑composition data for YH₂₋δ, CeH₂₊δ, and CTh₁₊δ (from ThC₁₋δ) at all reported temperatures. For each system, create a CSV file with the columns `temperature`, `composition_delta` (δ), and `activity_X` (a_H for hydrides, a_Th for carbide). For ThC, convert δ to the CTh₁₊δ notation (δ > 0 for positive deviation).
- Evidence: `/app/outputs/extracted_data.zip`

### Step 2: Compute diagnostic variables and perform linear regression
- Role: scored (load-bearing)
- Action: For each system and each isotherm, compute y and x for every candidate defect model using the formulas listed in the Approach section. For YH₂₋δ use the negative‑deviation set (three models); for CeH₂₊δ and CTh₁₊δ use the positive‑deviation set (three models). Perform ordinary least‑squares linear regression of y on x for each model; record the R², slope, and intercept.
- Output file: `/app/outputs/diagnostics.csv`
- Format: csv
- Contract: The file must contain exactly the columns `system` (str), `defect_model` (str), `temperature` (numeric), `x_i` (numeric), `y_i` (numeric), `R_squared` (numeric), `slope` (numeric), and `intercept` (numeric). One row per defect model per isotherm per system.
- Scoring: scored by hidden verifier

### Step 3: Extract interaction energies and formation parameters
- Role: scored
- Action: From the slopes of the best‑fit models in `diagnostics.csv` (the one with highest R² for each system at each temperature), compute the pairwise interaction free energy ξ using the conversion formulas and the structural parameters given in the Approach. For YH₂₋δ, compile ξ vs. temperature (in K), perform a linear fit ξ = ΔH − T·ΔS, and extract the vacancy‑pair formation enthalpy (kcal/mol) and entropy (cal/(deg·mol)). Write all results to a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: The JSON object must conform to the structure described in the Output contract section below.
- Scoring: scored by hidden verifier

## Output files
All output files go in `/app/outputs/`. The required scored files are:
- `/app/outputs/diagnostics.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diagnostics.csv
- path: `/app/outputs/diagnostics.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Diagnostic data for each defect model at each temperature for YH2, CeH2, and ThC. The verifier recomputes linear regressions from the provided (x_i,y_i) pairs and checks slope consistency.
- schema:
  - `type`: table
  - `required_columns`: `system`, `defect_model`, `temperature`, `x_i`, `y_i`, `R_squared`, `slope`, `intercept`

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Final extracted interaction energies, defect types, and for YH2 the formation enthalpy and entropy. The verifier compares these reported values to a hidden paper-based gold within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `YH2`:
      - `type`: object
      - `required`:
        - `temperatures_C`: list of number
        - `xi_H_values_kcal_per_mol`: list of number
        - `formation_enthalpy_kcal_per_mol`: number
        - `formation_entropy_cal_per_deg_mol`: number
        - `identified_defect`: string
    - `CeH2`:
      - `type`: object
      - `required`:
        - `temperatures_C`: list of number
        - `xi_H_values_kcal_per_mol`: list of number
        - `identified_defect`: string
    - `ThC`:
      - `type`: object
      - `required`:
        - `temperatures_K`: list of number
        - `xi_C_values_kcal_per_mol`: list of number
        - `identified_defect`: string

Notes: All temperatures for YH2 and CeH2 are in °C; for ThC they are in K. The formation enthalpy is in kcal/mol, the entropy in cal/(deg·mol).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diagnostics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "defect_model",
          "temperature",
          "x_i",
          "y_i",
          "R_squared",
          "slope",
          "intercept"
        ]
      },
      "description": "Diagnostic data for each defect model at each temperature for YH2, CeH2, and ThC. The verifier recomputes linear regressions from the provided (x_i,y_i) pairs and checks slope consistency."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "YH2": {
            "type": "object",
            "required": {
              "temperatures_C": "list of number",
              "xi_H_values_kcal_per_mol": "list of number",
              "formation_enthalpy_kcal_per_mol": "number",
              "formation_entropy_cal_per_deg_mol": "number",
              "identified_defect": "string"
            }
          },
          "CeH2": {
            "type": "object",
            "required": {
              "temperatures_C": "list of number",
              "xi_H_values_kcal_per_mol": "list of number",
              "identified_defect": "string"
            }
          },
          "ThC": {
            "type": "object",
            "required": {
              "temperatures_K": "list of number",
              "xi_C_values_kcal_per_mol": "list of number",
              "identified_defect": "string"
            }
          }
        }
      },
      "description": "Final extracted interaction energies, defect types, and for YH2 the formation enthalpy and entropy. The verifier compares these reported values to a hidden paper-based gold within tolerance."
    }
  ],
  "notes": "All temperatures for YH2 and CeH2 are in °C; for ThC they are in K. The formation enthalpy is in kcal/mol, the entropy in cal/(deg·mol)."
}
```

## How you are scored
A hidden verifier independently analyses your submitted artifacts. It will:
- Load `diagnostics.csv` and, for each system, recompute the linear regression from the provided (x_i, y_i) points to check R², slope, and intercept consistency.
- Identify the dominant defect model from the highest R² and compare your chosen model.
- Using the recomputed slopes, calculate the interaction energies ξ and compare them to a hidden reference within tolerance.
- For YH₂₋δ, recompute the ξ vs T linear fit and compare the formation enthalpy and entropy to reference values.
Your final score is a weighted combination of the accuracy of the defect identification, the interaction energies, and the formation parameters. Simply reporting the expected numbers without the supporting diagnostics will not pass.
