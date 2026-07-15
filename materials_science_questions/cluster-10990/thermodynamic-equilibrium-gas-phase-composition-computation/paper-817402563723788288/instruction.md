# Thermodynamic Equilibrium Gas Composition and Boron Droplet Size for BNNT Growth

## Problem background
In high-temperature plasma synthesis of boron-nitride nanotubes (BNNTs), a boron-rich feedstock is evaporated in a nitrogen atmosphere. As the gas cools, liquid boron droplets nucleate first, then nitrogen from the surrounding gas is incorporated into the droplets, leading to the growth of BNNTs on their surfaces. Understanding which gas-phase species are the dominant nitrogen carriers and what diameter the boron droplets attain under reactor conditions is essential for controlling the synthesis process. Thermodynamic modelling and simple agglomeration theory can address these open questions by predicting the equilibrium gas composition and the resulting boron droplet size.

## Approach
The equilibrium composition of the B-N gas mixture is obtained by minimising the Gibbs free energy, which yields analytical Arrhenius-type expressions for the partial pressures of key species. These expressions depend only on temperature and total pressure (boron condensation is accounted for, so the initial boron fraction does not affect gas-phase composition). Separately, the average boron droplet diameter that forms during cooldown is estimated using a simple agglomeration model. The model computes the droplet size from the initial boron atomic density, the temperature interval between nucleation and BNNT formation, and the gas cooling rate. The task is to implement these analytical formulas and evaluate them for the specified conditions.

## Reproduction target
Compute the equilibrium partial pressures (atm) of the major gas-phase species (B, N, BN, B₂N, N₂, N₃, B₂, B₃) for a B-N mixture at 1 atm total pressure, at seven temperatures from 2000 K to 5000 K. Using the given reactor parameters (initial boron atom density 3×10²² m⁻³, nucleation temperature 3200 K, formation temperature 2800 K, cooling rate 6×10⁴ K/s), compute the resulting boron droplet diameter (in nanometres). The output is a CSV of partial pressures versus temperature and a single text file containing the droplet diameter.

## Assets

- Python scientific computing stack: numpy

## Workflow steps

### Step 1: Compute equilibrium partial pressures via Arrhenius formulas
- Role: scored
- Action: Compute equilibrium partial pressures (atm) of species B, N, BN, B₂N, N₂, N₃, B₂, B₃ at temperatures 2000 K, 2500 K, 3000 K, 3500 K, 4000 K, 4500 K, 5000 K for a B-N mixture at total pressure 1 atm, using the analytical Arrhenius expressions simplified for p=1 atm and p0=1 atm to p_i = A_i * exp(-T_char_i / T) for species i. For N₂, compute its partial pressure as 1 atm minus the sum of the other partial pressures. The coefficients A_i (in atm) and T_char_i (in K) are:

  | Species | A (atm) | T_char (K) |
  |---------|----------|------------|
  | B       | 515000   | 58800      |
  | N       | 3600     | 58100      |
  | BN      | 359000   | 65000      |
  | B₂N     | 535000   | 40700      |
  | N₃      | 2.9e-3   | 51700      |
  | B₂      | 1962000  | 81900      |
  | B₃      | 238000   | 74100      |

  Boron condensation is accounted for, so gas-phase composition depends only on temperature and total pressure, not on initial boron fraction. Output a CSV file with one row per temperature.
- Output file: `/app/outputs/thermodynamic_composition.csv`
- Format: csv
- Contract: CSV with columns: Temperature_K, p_B_atm, p_N_atm, p_BN_atm, p_B2N_atm, p_N2_atm, p_N3_atm, p_B2_atm, p_B3_atm. All pressures in atm. One row per temperature.
- Scoring: scored by hidden verifier

### Step 2: Compute boron droplet diameter via agglomeration theory
- Role: scored (load-bearing)
- Action: Compute the average boron droplet diameter D (nanometers) using the agglomeration formula from the paper: D = (2 r₀)^(9/5) n₀^(2/5) (2π k (T_nucl + T_end) / m_B)^(1/5) ((T_nucl - T_end) / ℜ₀)^(2/5). Use the following constants: r₀ = 1.2×10⁻¹⁰ m (Wigner-Seitz radius), n₀ = 3×10²² m⁻³ (initial boron atom density), T_nucl = 3200 K (nucleation temperature), T_end = 2800 K (BNNT formation temperature), ℜ₀ = 6×10⁴ K/s (cooling rate), m_B = 1.79×10⁻²⁶ kg (boron atom mass), k = 1.380649×10⁻²³ J/K (Boltzmann constant). Output the result as a single line in a text file.
- Output file: `/app/outputs/droplet_diameter.txt`
- Format: txt
- Contract: A single line containing the numeric value of the boron droplet diameter D in nanometers (e.g., '20.0').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_composition.csv`
- `/app/outputs/droplet_diameter.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_composition.csv
- path: `/app/outputs/thermodynamic_composition.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium partial pressures of B, N, BN, B₂N, N₂, N₃, B₂, and B₃ at 7 temperatures (2000–5000 K) for a B-N mixture at 1 atm. The checker will recompute relative errors against a hidden reference and check monotonic trends.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `p_B_atm`, `p_N_atm`, `p_BN_atm`, `p_B2N_atm`, `p_N2_atm`, `p_N3_atm`, `p_B2_atm`, `p_B3_atm`
  - `units`:
    - `Temperature_K`: K
    - `p_B_atm`: atm
    - `p_N_atm`: atm
    - `p_BN_atm`: atm
    - `p_B2N_atm`: atm
    - `p_N2_atm`: atm
    - `p_N3_atm`: atm
    - `p_B2_atm`: atm
    - `p_B3_atm`: atm

### droplet_diameter.txt
- path: `/app/outputs/droplet_diameter.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Boron droplet diameter in nanometers computed for the ICP reactor conditions. The checker compares this value to the paper-reported gold within a tolerance.
- schema:
  - `type`: text
  - `required`:
    - `line`: numeric

Notes: The task covers the paper's main thermodynamic composition and droplet size predictions using analytically derived formulas. No process steps are needed because the coefficients are provided directly in the instruction; the agent solely computes the scored outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_composition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "p_B_atm",
          "p_N_atm",
          "p_BN_atm",
          "p_B2N_atm",
          "p_N2_atm",
          "p_N3_atm",
          "p_B2_atm",
          "p_B3_atm"
        ],
        "units": {
          "Temperature_K": "K",
          "p_B_atm": "atm",
          "p_N_atm": "atm",
          "p_BN_atm": "atm",
          "p_B2N_atm": "atm",
          "p_N2_atm": "atm",
          "p_N3_atm": "atm",
          "p_B2_atm": "atm",
          "p_B3_atm": "atm"
        }
      },
      "description": "Equilibrium partial pressures of B, N, BN, B₂N, N₂, N₃, B₂, and B₃ at 7 temperatures (2000–5000 K) for a B-N mixture at 1 atm. The checker will recompute relative errors against a hidden reference and check monotonic trends."
    },
    {
      "file": "droplet_diameter.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "line": "numeric"
        }
      },
      "description": "Boron droplet diameter in nanometers computed for the ICP reactor conditions. The checker compares this value to the paper-reported gold within a tolerance."
    }
  ],
  "notes": "The task covers the paper's main thermodynamic composition and droplet size predictions using analytically derived formulas. No process steps are needed because the coefficients are provided directly in the instruction; the agent solely computes the scored outputs."
}
```

## How you are scored
A hidden verifier will independently assess each workflow stage. For Step 1, your CSV will be compared against reference partial pressures computed from the same analytical formulas; the verifier checks relative errors and monotonic trends, and rewards your result in proportion to its accuracy. For Step 2, your droplet diameter will be compared against a reference value within a tolerance. The final score is a weighted combination of the scores from the two stages — reporting the paper’s numbers without executing the computation is not sufficient.
