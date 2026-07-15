# Spectroscopic calculation of P2 dissociation equilibrium constants

## Problem background
In the 1930s, the composition of phosphorus vapor at high temperatures was disputed. One set of experiments suggested measurable amounts of monatomic phosphorus (P), while another found none. The question can be resolved by computing the equilibrium constant for the dissociation P₂(g) ⇌ 2P(g) from spectroscopic molecular constants and standard statistical mechanics. The magnitude of the equilibrium constant determines whether dissociation is negligible or significant.

## Approach
Statistical mechanics relates the equilibrium constant K = P_P² / P_P₂ to the dissociation energy D₀ and the free energy functions of the species. For ideal gas P and P₂, the free energy functions are obtained from molecular partition functions (translational, rotational, vibrational) using the known vibrational frequency (780.76 cm⁻¹), anharmonicity (2.98 cm⁻¹), moment of inertia (90.47×10⁻⁴⁰ g·cm²), and electronic degeneracies (P: ²S, g=4; P₂: ¹Σ, g=1). The relation is ΔH₀⁰ = -RT ln K - RT Δ(log N₀ - log Q), where the free energy function difference Δ(log N₀ - log Q) is computed from the partition functions and D₀ = 115,450 cal/mol. Standard physical constants (N₀ = 6.022×10²³ mol⁻¹, R = 1.987 cal mol⁻¹ K⁻¹, h = 6.626×10⁻²⁷ erg·s, k = 1.381×10⁻¹⁶ erg K⁻¹) are used. For P only translational and electronic contributions matter; for P₂ all three internal contributions are computed. The workflow first computes the free energy functions, then solves the relation for K at each temperature.

## Reproduction target
Produce a JSON file named `p2_dissociation_equilibrium.json` containing the equilibrium constant K_atmos = P_P² / P_P₂ and its natural logarithm lnK at five temperatures: 1073, 1173, 1273, 1373, and 1473 K. The file must have the structure `{"units": "K_atmos dimensionless, lnK dimensionless", "entries": [ {"T_K": <Temperature in K>, "K_atmos": <float>, "lnK": <float>}, ... ]}` for all five temperatures in order.

## Assets

- Standard physical constants
- Molecular constants for P and P2

## Workflow steps

### Step 1: Compute free energy functions for P and P2
- Role: process
- Action: For each of the five temperatures (1073, 1173, 1273, 1373, 1473 K), compute the translational, rotational, and vibrational partition functions of gaseous P atom and P2 molecule using standard statistical mechanical formulas. Combine them to obtain the quantity -(F0 - H00)/T per mole (or equivalently, compute log Q for each species).
- Evidence: none

### Step 2: Calculate equilibrium constants for P2 dissociation
- Role: scored (load-bearing)
- Action: Using the free energy functions from Step 1 and the relation ΔH00 = -RT ln K - RT [ (log N0 - log Q)_products - (log N0 - log Q)_reactants ] with ΔH00 = 115,450 cal/mol, compute the equilibrium constant K_atmos = P_P^2 / P_{P2} at each temperature (1073, 1173, 1273, 1373, 1473 K). Also compute the natural logarithm ln K_atmos. Write the results to p2_dissociation_equilibrium.json.
- Output file: `/app/outputs/p2_dissociation_equilibrium.json`
- Format: json
- Contract: {
  "units": "K_atmos dimensionless, lnK dimensionless",
  "entries": [
    {"T_K": 1073, "K_atmos": <float>, "lnK": <float>},
    {"T_K": 1173, "K_atmos": <float>, "lnK": <float>},
    {"T_K": 1273, "K_atmos": <float>, "lnK": <float>},
    {"T_K": 1373, "K_atmos": <float>, "lnK": <float>},
    {"T_K": 1473, "K_atmos": <float>, "lnK": <float>}
  ]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/p2_dissociation_equilibrium.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### p2_dissociation_equilibrium.json
- path: `/app/outputs/p2_dissociation_equilibrium.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium constants K_atmos = P_P^2 / P_{P2} and their natural logarithms at five temperatures, matching the spectroscopic calculation of Table II.
- schema:
  - `type`: object
  - `required`:
    - `units`: string
    - `entries`: array of objects with T_K, K_atmos, lnK
  - `items`:
    - `T_K`: integer (temperature in K)
    - `K_atmos`: float
    - `lnK`: float

Notes: The task reproduces the spectroscopic calculation of P2 dissociation equilibrium constants from the paper. The checker compares the agent's submitted K_atmos and lnK against hidden gold values using a relative tolerance for K_atmos and absolute tolerance for lnK (whichever is looser). No network fetch for ground truth.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "p2_dissociation_equilibrium.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "units": "string",
          "entries": "array of objects with T_K, K_atmos, lnK"
        },
        "items": {
          "T_K": "integer (temperature in K)",
          "K_atmos": "float",
          "lnK": "float"
        }
      },
      "description": "Computed equilibrium constants K_atmos = P_P^2 / P_{P2} and their natural logarithms at five temperatures, matching the spectroscopic calculation of Table II."
    }
  ],
  "notes": "The task reproduces the spectroscopic calculation of P2 dissociation equilibrium constants from the paper. The checker compares the agent's submitted K_atmos and lnK against hidden gold values using a relative tolerance for K_atmos and absolute tolerance for lnK (whichever is looser). No network fetch for ground truth."
}
```

## How you are scored
A hidden verifier reads your submitted `p2_dissociation_equilibrium.json` and independently compares your K_atmos and lnK values for each temperature to the expected values using numerical tolerances. The verifier also checks structural compliance with the output contract. The final reward is a weighted average of the per-temperature agreement and format validity.
