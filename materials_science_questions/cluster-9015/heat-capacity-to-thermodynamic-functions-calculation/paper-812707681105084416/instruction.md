# Thermodynamic equilibria of solid BN modifications in CVD system

## Problem background
Chemical vapour deposition (CVD) of boron nitride can produce films of different boron‑nitride polymorphs (hexagonal h‑BN, cubic c‑BN, and wurtzite w‑BN). Understanding the thermodynamic stability of these condensed phases under broad CVD conditions is critical for process design. This problem addresses the B–N–H–Cl–He system at sub‑atmospheric and atmospheric total pressures, over a wide range of atomic input ratios and temperatures, using Gibbs free‑energy minimization. New thermochemical data for the BN modifications imply that the relative phase stabilities differ from the earlier convention, and a key open question is which condensed phase(s) are stable in different parameter regimes and at what temperature the dominant BN phase may change.

## Approach
The approach is purely thermodynamic: the equilibrium state of the open B–N–H–Cl–He system is obtained by minimizing the Gibbs free energy per mole of a chosen non‑depositing element, under the constraints of mass balances for each element and Dalton’s law. The condensed phases (h‑BN, c‑BN, w‑BN, and elemental B) are treated as stoichiometric solids of fixed composition. Gas‑phase species are described by their standard thermodynamic functions (enthalpy, entropy, and heat‑capacity polynomials) together with their partial pressures. The minimizer performs a global search over the possible combinations of condensed phases to find the set that yields the lowest free energy for each set of conditions (temperature, total pressure, and initial atomic ratios). For all gaseous species and for h‑BN, the required thermodynamic data are taken from established public compilations (e.g. NIST‑JANAF or NASA CEA). The thermodynamic data for c‑BN and w‑BN are provided directly in this instruction as polynomial coefficients. By scanning the parameter space (T, P, and atomic concentration ratios) and recording the stable condensed phase, one can map the phase stability boundaries and locate the temperature at which the stable BN phase changes. Additionally, for a fixed input atomic ratio, the equilibrium gas‑phase composition is computed at specified temperatures and pressures, reporting all species with a mole fraction of at least 1 × 10⁻⁸.

## Reproduction target
1. Determine the thermodynamically stable condensed phase (h‑BN, c‑BN, w‑BN, B, or none) over the ranges: T = 673–2273 K; total pressure P = 1.013 × 10⁵ Pa and P = 1.013 × 10³ Pa; atomic ratios n_B/n_N = 0.1–10, n_Cl/n_H = 0.1–1.0, n_He/n_N = 0.1–60. From these data, identify the temperature (the transition temperature) at which the stable condensed phase changes for the stoichiometric input ratio n_B/n_N = 1:1.
2. For the fixed initial atomic ratio n_B:n_N:n_Cl:n_H:n_He = 1:1:3:3:10, compute the equilibrium mole fractions of all gas‑phase species at T = 1400 K and T = 800 K for both total pressures (1.013 × 10⁵ Pa and 1.013 × 10³ Pa). Include every species with mole fraction ≥ 1 × 10⁻⁸.

## Assets

- Standard thermodynamic data for gaseous and condensed species (H, H₂, NH, NH₂, NH₃, N₂H₂, N₂H₄, N, N₂, BH, BH₂, BH₃, B₂H₆, B₃N₃H₆, BH₃·NH₃, B, B₂, BN, BCl, BCl₂, BCl₃, B₂Cl₄, BHCl, BHCl₂, BH₂Cl, Cl₂, Cl, HCl, He, h-BN, B)
- Thermodynamic data for c-BN (cubic BN) are:
  - ΔfH°(298 K) = -266.8 kJ·mol⁻¹
  - S°(298 K) = 6.682 J·K⁻¹·mol⁻¹
  - C_p(T) = 26.6008 + 1.91239×10⁻²·T - 1.45856×10⁶·T⁻² (J·K⁻¹·mol⁻¹, T in K)
- Thermodynamic data for w-BN (wurtzite BN) are:
  - ΔfH°(298 K) = -263.2 kJ·mol⁻¹
  - S°(298 K) = 7.237 J·K⁻¹·mol⁻¹
  - C_p(T) = 28.2590 + 1.67589×10⁻²·T - 1.49371×10⁶·T⁻² (J·K⁻¹·mol⁻¹, T in K)

## Workflow steps

### Step 1: Thermodynamic data and Gibbs minimizer setup
- Role: process
- Action: Obtain standard thermodynamic data (standard enthalpy, entropy, heat capacity coefficients) for all required gaseous species and h-BN from a public database. Implement a Gibbs free energy minimization algorithm for an open system with constraints (mass balances and Dalton's law). Incorporate the BN polynomial coefficients for c-BN and w-BN provided in the instruction.
- Evidence: `/app/outputs/setup_complete.txt`

### Step 2: Phase stability calculation
- Role: scored (load-bearing)
- Action: Run the Gibbs free energy minimizer over the parameter ranges: T=673–2273 K, P=1.013×10^5 Pa and 1.013×10^3 Pa, n_B/n_N=0.1–10, n_Cl/n_H=0.1–1.0, n_He/n_N=0.1–60. For each condition, record the thermodynamically stable condensed phase (h-BN, c-BN, w-BN, B, or none).
- Output file: `/app/outputs/phase_stability.tsv`
- Format: tsv
- Contract: TSV with columns: T (K), P (Pa), n_B_n_N (float), n_Cl_n_H (float), n_He_n_N (float), stable_phase (string: one of h-BN, c-BN, w-BN, B, none).
- Scoring: scored by hidden verifier

### Step 3: Equilibrium gas composition at specific conditions
- Role: scored
- Action: Run the minimizer for the fixed input atomic ratio n_B:n_N:n_Cl:n_H:n_He = 1:1:3:3:10 at T=1400 K and T=800 K, at total pressures P=1.013×10^5 Pa and P=1.013×10^3 Pa. Output the equilibrium mole fractions of all gaseous species with mole fraction ≥ 1×10^{-8}.
- Output file: `/app/outputs/gas_composition.tsv`
- Format: tsv
- Contract: TSV with columns: T (K), P (Pa), species (string), mole_fraction (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_stability.tsv`
- `/app/outputs/gas_composition.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_stability.tsv
- path: `/app/outputs/phase_stability.tsv`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Maps the stable condensed phase across the parameter ranges. The checker will derive the c-BN/h-BN transition temperature and verify phase stability patterns.
- schema:
  - `type`: table
  - `required_columns`: `T`, `P`, `n_B_n_N`, `n_Cl_n_H`, `n_He_n_N`, `stable_phase`
  - `units`:
    - `T`: K
    - `P`: Pa

### gas_composition.tsv
- path: `/app/outputs/gas_composition.tsv`
- format: tsv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium gas mole fractions for the fixed input ratio 1:1:3:3:10 at 800 K and 1400 K, at both pressures. Compared to paper's Table 2 with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `P`, `species`, `mole_fraction`
  - `units`:
    - `T`: K
    - `P`: Pa

Notes: The BN polynomial coefficients for c-BN and w-BN are provided directly in the instruction. The checker will automatically determine the h-BN/c-BN transition temperature from the phase_stability data and compare gas fractions to reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_stability.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P",
          "n_B_n_N",
          "n_Cl_n_H",
          "n_He_n_N",
          "stable_phase"
        ],
        "units": {
          "T": "K",
          "P": "Pa"
        }
      },
      "description": "Maps the stable condensed phase across the parameter ranges. The checker will derive the c-BN/h-BN transition temperature and verify phase stability patterns."
    },
    {
      "file": "gas_composition.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P",
          "species",
          "mole_fraction"
        ],
        "units": {
          "T": "K",
          "P": "Pa"
        }
      },
      "description": "Equilibrium gas mole fractions for the fixed input ratio 1:1:3:3:10 at 800 K and 1400 K, at both pressures. Compared to paper's Table 2 with tolerance."
    }
  ],
  "notes": "The BN polynomial coefficients for c-BN and w-BN are provided directly in the instruction. The checker will automatically determine the h-BN/c-BN transition temperature from the phase_stability data and compare gas fractions to reference values."
}
```

## How you are scored
A hidden verifier independently examines your submitted output files. The verifier extracts the transition temperature and the phase‑stability pattern from phase_stability.tsv, and compares the gas‑phase mole fractions from gas_composition.tsv against reference values. Each of the two scored artifacts contributes a weighted share to the final reward, with the phase‑stability artifact carrying the larger weight. Reporting the correct structural output is required; simply printing a final summary number is not sufficient. The verifier uses tolerances appropriate for numerical re‑implementation of the thermodynamic minimizer.
