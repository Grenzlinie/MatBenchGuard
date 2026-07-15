# Hall and Magnetoresistance Factors in Bismuth from a Two‑Band Nonparabolic Model

## Problem background
Undoped bismuth is a semimetal whose transport properties are strongly influenced by the non‑parabolic shape of its L‑band electron pockets and the presence of a parabolic T‑hole band. In many analyses of galvanomagnetic data the Hall factor and magnetoresistance factor are assumed to be unity, but the combination of non‑parabolicity and recombination scattering can cause these factors to vary significantly with temperature. This task computes the values of these factors for electrons and holes over the temperature range 77–300 K, using a two‑band ellipsoidal non‑parabolic model that accounts for the temperature‑dependent band gap and for recombination scattering between the bands. The computed factors are then used to interpret experimental mobility and concentration data, revealing how strongly the factors deviate from unity and how they affect the derived transport coefficients.

## Approach
The model treats the three electron L‑pockets with a non‑parabolic dispersion relation, each described by a single density‑of‑states effective mass, and the T‑hole pocket as parabolic with its own effective mass. The energy‑dependent relaxation time of electrons contains an intra‑band acoustic‑like term and a term describing recombination transitions into the hole band; the hole relaxation time has analogous intra‑band and recombination contributions. The band‑gap energy that enters the non‑parabolicity is taken from magneto‑optical measurements and is temperature‑dependent; the overlap between the L‑band edge and the T‑hole band edge is treated as constant. The density‑of‑states effective masses are not known a priori for temperatures above 100 K. Therefore, at each temperature the masses are determined by an iterative procedure: the masses are adjusted until the electron mobility along the ellipsoid axis close to the trigonal direction and the hole mobility in the direction perpendicular to that axis, calculated from the model, match a set of experimentally measured mobilities that are given in the workflow instructions. Once the masses are known, the Hall factor A = ⟨τ²⟩/⟨τ⟩² and the magnetoresistance factor M = ⟨τ³⟩/⟨τ⟩³ are computed for both carrier types by performing energy averages over the appropriate non‑parabolic density of states. The computations involve numerical integration and root‑finding, for which standard numerical libraries are sufficient.

### Model equations

The relaxation times for L‑electrons (τ_N) and T‑holes (τ_P) are given by:

τ_N^{-1}(ε) = C_N (k_B T / 1 meV)^{3/2} m_dL^{*3/2} [ε (1 + ε/ε_g)]^{1/2} (1 + 2ε/ε_g) + C_R (k_B T / 1 meV)^{3/2} m_dT^{*3/2} (ε_LT − ε)^{1/2},

τ_P^{-1}(ε) = C_P (k_B T / 1 meV)^{3/2} m_dT^{*3/2} (ε_LT − ε)^{1/2} + 3 C_R (k_B T / 1 meV)^{3/2} m_dL^{*3/2} [ε (1 + ε/ε_g)]^{1/2} (1 + 2ε/ε_g),

where ε is the electron energy measured from the L‑band edge (in units of k_B T), ε_g = E_g/(k_B T) is the dimensionless gap, ε_LT = E_LT/(k_B T) is the dimensionless overlap, m_dL* and m_dT* are the density‑of‑states effective masses of one ellipsoid in units of the free electron mass. The scattering coefficients are:

C_N = 4.8 × 10^11 s⁻¹,  C_P = 0.8 × 10^11 s⁻¹,  C_R = x C_N with x = 0.3.

The L‑band density of states (arbitrary normalisation) is:

g_L(ε) ∝ [ε (1 + ε/ε_g)]^{1/2} (1 + 2ε/ε_g),

and the parabolic T‑hole band has g_T(ε) ∝ (ε_LT − ε)^{1/2} for ε ≤ ε_LT.

Thermal occupation is described by Fermi‑Dirac statistics with a temperature‑dependent chemical potential ζ (in units of k_B T). The electron concentration in one L‑valley is

n = A ∫ g_L(ε) f(ε; ζ) dε,  f(ε; ζ) = 1/(exp(ε − ζ) + 1),

with the normalisation constant A cancelling in all averages. Charge neutrality (three L‑valleys, one T‑valley) determines ζ. The intrinsic carrier concentration is N = n_L = p_T.

Hall and magnetoresistance factors are defined as:

A = ⟨τ²⟩ / ⟨τ⟩²,  M = ⟨τ³⟩ / ⟨τ⟩³,

where the averages are over the respective band using the Fermi‑Dirac distribution:

⟨X⟩ = (∫ X(ε) g(ε) f(ε; ζ) dε) / (∫ g(ε) f(ε; ζ) dε).

### Mobility computation and iterative fitting

The electron mobility along the ellipsoid axis close to the trigonal direction (μ₃) and the hole mobility perpendicular to it (ν₁) are assumed to be proportional to the energy‑weighted average of τ:

μ₃ ∝ (1 / m_dL*) ⋅ (⟨τ ε⟩ / ⟨ε⟩),  ν₁ ∝ (1 / m_dT*) ⋅ (⟨τ ε⟩ / ⟨ε⟩).

The (unknown) proportionality constants are determined from the condition that at T = 77 K, with the fixed masses m_dL* = 0.0112, m_dT* = 0.16 and the scattering parameters listed above, the computed mobility must equal the experimental target values:

μ₃(77 K) = 30.0 m²/V·s,  ν₁(77 K) = 10.4 m²/V·s.

Once the scaling factors are fixed, the same factors are used for all higher temperatures.

### Fixed parameters and target mobilities

A summary of all fixed parameters:

| Parameter | Value |
|-----------|-------|
| C_N | 4.8 × 10^11 s⁻¹ |
| C_P | 0.8 × 10^11 s⁻¹ |
| x = C_R/C_N | 0.3 |
| E_g(T) (meV) | 13.6 + 2.1 × 10⁻³ T + 2.5 × 10⁻⁴ T² |
| E_LT (meV) | 39.2 |
| m_dL* (initial at 77 K) | 0.0112 |
| m_dT* (initial at 77 K) | 0.16 |

Experimental target mobilities (from Table 2) that must be matched during the mass fitting:

| T (K) | μ₃ (m²/V·s) | ν₁ (m²/V·s) |
|-------|------|------|
| 77    | 30.0 | 10.4 |
| 100   | 17.7 | 6.71 |
| 140   | 8.0  | 3.14 |
| 180   | 4.01 | 1.74 |
| 220   | 2.17 | 1.03 |
| 260   | 1.28 | 0.64 |
| 300   | 0.77 | 0.42 |

### Iterative procedure

For each temperature T ≥ 100 K, start with an initial guess for m_dL* and m_dT* (e.g., the converged values from the previous temperature, or the 77 K values for the first step). Compute the chemical potential ζ and carrier concentration N self‑consistently. Evaluate the mobilities μ₃ and ν₁ using the proportionality constants fixed at 77 K. If the calculated mobilities differ from the target values, adjust the masses (e.g., using a root‑finding algorithm) and repeat until convergence. After convergence, compute the Hall factor A_N, A_P and magnetoresistance factor M_N, M_P from the averages ⟨τ²⟩ and ⟨τ³⟩, and write the final factors to the scored output file.

## Reproduction target
Implement the described two‑band non‑parabolic model with recombination scattering. For each of the seven temperatures (77, 100, 140, 180, 220, 260, 300 K) determine the density‑of‑states effective masses of the L‑electrons and T‑holes by matching the computed mobilities to the given experimental target values. Using the resulting masses, compute the electron Hall factor A_N, electron magnetoresistance factor M_N, hole Hall factor A_P, and hole magnetoresistance factor M_P, and write them to the CSV file `/app/outputs/hall_magnetoresistance_factors.csv` with the required columns. The factors should be evaluated using the definitions A = ⟨τ²⟩/⟨τ⟩² and M = ⟨τ³⟩/⟨τ⟩³ with energy averaging over the non‑parabolic density of states.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Determine temperature‑dependent effective masses
- Role: process
- Action: For each temperature (77, 100, 140, 180, 220, 260, 300 K) determine the density‑of‑states effective masses m_dL*(T) and m_dT*(T) by an iterative procedure: adjust the masses until the computed electron mobility μ₃ and hole mobility ν₁ (using the two‑band non‑parabolic model with the given scattering parameters, temperature‑dependent band gap E_g(T), and fixed band overlap E_LT) agree with the target experimental mobilities (μ₃_target, ν₁_target) listed in the instruction.
- Evidence: `/app/outputs/effective_masses.csv`

### Step 2: Compute Hall and magnetoresistance factors
- Role: scored (load-bearing)
- Action: Using the effective masses obtained in step_01, compute the electron Hall factor A_N, electron magnetoresistance factor M_N, hole Hall factor A_P, and hole magnetoresistance factor M_P at each temperature from the energy‑dependent relaxation times τ_N and τ_P of the two‑band model, according to the definitions A = ⟨τ²⟩/⟨τ⟩² and M = ⟨τ³⟩/⟨τ⟩³, with energy averaging over the non‑parabolic density of states.
- Output file: `/app/outputs/hall_magnetoresistance_factors.csv`
- Format: csv
- Contract: CSV table with columns: T, A_N, M_N, A_P, M_P. Temperature T is integer Kelvin; A_N, M_N, A_P, M_P are dimensionless floating‑point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hall_magnetoresistance_factors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hall_magnetoresistance_factors.csv
- path: `/app/outputs/hall_magnetoresistance_factors.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed Hall and magnetoresistance factors for electrons and holes at T = 77, 100, 140, 180, 220, 260, 300 K. Each row corresponds to one temperature. The checker reads the CSV and compares the factor values to the hidden gold from the paper with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `A_N`, `M_N`, `A_P`, `M_P`
  - `units`:
    - `T`: K
    - `A_N`: dimensionless
    - `M_N`: dimensionless
    - `A_P`: dimensionless
    - `M_P`: dimensionless

Notes: The output contract declares a single scored artifact. The checker performs a T0 result‑level comparison using hidden tolerances derived from the paper’s Table 1. The process step evidence (effective_masses.csv) is not scored but documents the mass determination.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hall_magnetoresistance_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "A_N",
          "M_N",
          "A_P",
          "M_P"
        ],
        "units": {
          "T": "K",
          "A_N": "dimensionless",
          "M_N": "dimensionless",
          "A_P": "dimensionless",
          "M_P": "dimensionless"
        }
      },
      "description": "Computed Hall and magnetoresistance factors for electrons and holes at T = 77, 100, 140, 180, 220, 260, 300 K. Each row corresponds to one temperature. The checker reads the CSV and compares the factor values to the hidden gold from the paper with appropriate tolerances."
    }
  ],
  "notes": "The output contract declares a single scored artifact. The checker performs a T0 result‑level comparison using hidden tolerances derived from the paper’s Table 1. The process step evidence (effective_masses.csv) is not scored but documents the mass determination."
}
```

## How you are scored
After your run, a hidden verifier reads your `/app/outputs/hall_magnetoresistance_factors.csv`. It compares each factor value (A_N, M_N, A_P, M_P) at every temperature to reference values derived from the original study, using hidden tolerances that accommodate legitimate numerical variations while rejecting random guesses. The verifier also checks that the electron factors increase monotonically with temperature and that the hole factors remain close to 1. The final reward is a scalar between 0 and 1 that combines per‑value agreement scores and a trend‑compliance score. Only the file `hall_magnetoresistance_factors.csv` is scored; intermediate artifacts such as the effective‑mass log are audited but do not directly contribute to the reward. Reporting the correct values without actually implementing the model will not pass the tolerance checks.
