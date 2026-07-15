# Compute Zn-Sn Binary Eutectic and ZnSe Solubility in Sn via CALPHAD Modeling

## Problem background
The Zn-Sn-Se ternary system is important for liquid phase epitaxy of ZnSe, where tin (Sn) serves as a solvent. A key practical question is the equilibrium phase boundaries that determine the solubility of ZnSe in liquid tin and the Zn-Sn binary eutectic. This task requires computing these phase equilibria from a CALPHAD-type thermodynamic model, providing predictive understanding of growth conditions and layer composition for the ZnSe/Sn system.

## Approach
The thermodynamic model represents the Gibbs free energy of the liquid and solid phases involved. The liquid free energy includes contributions from binary mixing enthalpies and excess entropies for each of the three binary subsystems (Zn-Sn, Zn-Se, Sn-Se), plus ternary interaction corrections. The free energy of solid ZnSe is expressed in terms of its melting entropy and melting temperature. Equilibrium is determined by minimizing the total free energy of the system using a simplex algorithm. For the Zn-Sn binary, the two liquidus branches are computed and their intersection yields the eutectic point. For the ternary Zn-Sn-Se system, the liquidus along the composition line x_Zn = x_Se is found by minimizing the free energy at each target composition and temperature.

### Thermodynamic model equations and parameters

All energies are expressed per mole of atoms. The gas constant R = 8.314 J/(mol·K).

**Reference states:** The free energy of pure solid element i is given by G_i^S = S_i^F (T - T_i^F), where T_i^F and S_i^F are the melting temperature and melting entropy. The melting entropies and temperatures for the elements and compounds are listed in Table 1.

**Table 1: Melting properties**

| Phase               | T^F (K) | L^F (kJ/mol-atoms) | S^F (J/(K·mol-atoms)) |
|---------------------|---------|--------------------|-----------------------|
| Zn(s)               | 692.68  | 1.750              | 2.525                 |
| Sn(s)               | 505.08  | 1.720              | 3.404                 |
| ZnSe (Zn_0.5Se_0.5) | 1788    | 8.0                | 4.47                  |
| SnSe (Sn_0.5Se_0.5) | 1153    | 9.4                | 8.153                 |

**Liquid mixing enthalpy and excess entropy polynomials**

For each binary system, the molar mixing enthalpy (^M H_{i-j}^L) and excess entropy (^xs S_{i-j}^L) are expressed as functions of mole fractions x_i and x_j. The coefficients absorb the conversion factor 4.184 to express the originally thermochemical calorie-based quantities in joules.

**Zn–Sn binary:**
^M H_Zn-Sn^L = x_Zn x_Sn [2.360 + 0.907 (x_Zn - x_Sn) + 0.216 (x_Zn - x_Sn)^2] * 4.184  kJ/mol   (Eq.1)
^xs S_Zn-Sn^L = x_Zn x_Sn [1.42  + 0.58  (x_Zn - x_Sn) + 0.12  (x_Zn - x_Sn)^2] * 4.184  J/(K·mol)  (Eq.2)

**Zn–Se binary:**
^M H_Zn-Se^L = x_Zn x_Se [17.663 - 8.782 (x_Zn - x_Se) + 8.525 (x_Zn - x_Se)^2] * 4.184  kJ/mol   (Eq.6)
^xs S_Zn-Se^L = x_Zn x_Se [4.10  - 0.73  (x_Zn - x_Se)]                     * 4.184  J/(K·mol)  (Eq.7)

**Sn–Se binary:**
^M H_Sn-Se^L = x_Sn x_Se [5.086 + 2.936 (x_Sn - x_Se) - 3.846 (x_Sn - x_Se)^2] * 4.184  kJ/mol   (Eq.8)
^xs S_Sn-Se^L = x_Sn x_Se [-0.05 + 0.63  (x_Sn - x_Se)]                     * 4.184  J/(K·mol)  (Eq.9)

**Ternary interaction coefficients (Table 2)**
For the Zn–Sn–Se liquid, the excess free energy includes a product term of the form x_Zn x_Sn x_Se * Σ (α_i - β_i T) x_i, where i = Zn, Sn, Se. The coefficients are:

α_Zn = 2742 * 4.184  kJ/mol   ;   β_Zn = -60.6 * 4.184  kJ/(K·mol)
α_Sn = 3787 * 4.184  kJ/mol   ;   β_Sn =   2.9 * 4.184  kJ/(K·mol)
α_Se = -3885 * 4.184 kJ/mol   ;   β_Se =  55.8 * 4.184  kJ/(K·mol)

**Total free energy and minimization**
The total Gibbs free energy of the system at temperature T and global composition is (Eq.5):
G = α G^S + (1-α) [ ^xs G^L + R T Σ_i x_i ln x_i ]
where α is the crystallized fraction of solid (0 ≤ α ≤ 1), G^S is the free energy of the solid phase (taken as pure ZnSe when computing the ZnSe liquidus), and ^xs G^L is the sum of the binary excess contributions ( ^M H_{i-j}^L - T ^xs S_{i-j}^L ) over all pairs plus the ternary term. For a given temperature and global composition, the equilibrium state (mole fractions in the liquid, α) is the one that minimizes G, subject to mass conservation and x_Zn = x_Se when computing the ZnSe solubility curve. The minimization is performed using the simplex (Nelder‑Mead) algorithm.

## Reproduction target
Determine the Zn-Sn binary eutectic point: temperature (in K) and the mole fraction of Zn at the eutectic composition. Also compute the ternary liquidus curve for compositions satisfying x_Zn = x_Se (solubility of ZnSe in Sn) at the following ZnSe mole fractions: 0.005, 0.0075, 0.01, 0.0125, 0.015, 0.0175, 0.02, 0.0225, 0.025, 0.0275, 0.03, 0.0325, 0.035, 0.0375, 0.04, 0.0425, 0.045, 0.0475, 0.05. For each composition, output the liquidus temperature.

## Assets

- SciPy: scipy

## Workflow steps

### Step 1: Calculate Zn-Sn binary eutectic
- Role: scored (load-bearing)
- Action: Define the free enthalpy of the liquid phase using the Zn-Sn mixing enthalpy and excess entropy expressions, and the solid free enthalpies of Zn and Sn from their melting entropies and temperatures. Compute the two liquidus branches by minimizing the total free enthalpy, and find their intersection to obtain the eutectic temperature (in K) and the mole fraction of Zn.
- Output file: `/app/outputs/step_01_binary_eutectic.csv`
- Format: csv
- Contract: Columns: eutectic_temperature_K (float), eutectic_Zn_mole_fraction (float). Single row.
- Scoring: scored by hidden verifier

### Step 2: Calculate ZnSe solubility curve in Sn ternary liquidus
- Role: scored (load-bearing)
- Action: Using the full thermodynamic model for the Zn-Sn-Se system (binary mixing parameters for Zn-Sn, Zn-Se, Sn-Se, ternary interaction coefficients, and the free enthalpy of solid ZnSe from its melting entropy and temperature), implement total free energy minimization for compositions that satisfy x_Zn = x_Se. Compute the liquidus temperature at a series of mole fractions from 0.005 to 0.05 in steps of 0.0025.
- Output file: `/app/outputs/step_01_ternary_liquidus.csv`
- Format: csv
- Contract: Columns: temperature_K (float), mole_fraction_ZnSe (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_binary_eutectic.csv`
- `/app/outputs/step_01_ternary_liquidus.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_binary_eutectic.csv
- path: `/app/outputs/step_01_binary_eutectic.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The Zn-Sn eutectic temperature (K) and the mole fraction of Zn at the eutectic point.
- schema:
  - `type`: table
  - `required_columns`: `eutectic_temperature_K`, `eutectic_Zn_mole_fraction`

### step_01_ternary_liquidus.csv
- path: `/app/outputs/step_01_ternary_liquidus.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: The calculated liquidus temperature as a function of the mole fraction of ZnSe (with x_Zn = x_Se) in the Sn-based ternary liquid.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `mole_fraction_ZnSe`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_binary_eutectic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "eutectic_temperature_K",
          "eutectic_Zn_mole_fraction"
        ]
      },
      "description": "The Zn-Sn eutectic temperature (K) and the mole fraction of Zn at the eutectic point."
    },
    {
      "file": "step_01_ternary_liquidus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "mole_fraction_ZnSe"
        ]
      },
      "description": "The calculated liquidus temperature as a function of the mole fraction of ZnSe (with x_Zn = x_Se) in the Sn-based ternary liquid."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be checked by a hidden verifier that independently implements the same thermodynamic model described above and computes reference values for the binary eutectic and ternary liquidus. The verifier compares your submitted CSV files against these hidden references. Each workflow stage is scored separately, and the final reward combines the results. Merely stating the paper's reported numbers without computing them from the model will not pass, because the verifier expects the outputs to be produced by an actual implementation of the free energy minimization procedure.
