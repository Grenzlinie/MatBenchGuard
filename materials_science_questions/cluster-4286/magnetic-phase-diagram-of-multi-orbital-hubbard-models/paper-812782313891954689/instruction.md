# Hartree‑Fock thermodynamic properties of a half‑filled Hubbard model

## Problem background
This task investigates the thermodynamic stability of spin-density waves (SDW) in a simplified model of an antiferromagnetic metal. The model consists of a single electron band with a Hubbard-type delta-function interaction, treated within the Hartree-Fock approximation. The interest is in whether a static spin-density wave state can be the ground state, and how its properties compare to those of the paramagnetic and ferromagnetic states. The system is studied at half-filling, where exact electron-hole symmetry simplifies the analysis. A special piecewise-linear energy band (the limit ε_i→0) is used to make the Hartree-Fock self-consistency equations analytically tractable, yet rich enough to exhibit the competition among the three phases. The task is to compute the temperature-dependent energy per atom, the order-parameter amplitude, the specific heat, and the entropy for the paramagnetic, ferromagnetic, and spin-density-wave states, and to compare them over a range of temperatures from zero up to above the transition temperatures.

## Approach
The Hartree-Fock approximation decouples the two-particle interaction, leading to a set of self-consistency equations that determine the spin-density-wave amplitude μ and the chemical potential (which is fixed to p = I/2 for n = 1). For the special piecewise-linear band in the limit ε_i→0, these equations reduce to algebraic relations that can be solved by root-finding. The three states are distinguished by a parameter λ: λ=0 (ferromagnetic), λ=1 (spin-density-wave with antiparallel spin alignment on adjacent (100) planes), and the paramagnetic state corresponds to μ=0. The interaction strength is set by the parameter Δ/I, here Δ = 0.2 I. At each temperature T (in units 1/k_B), the self-consistency condition for μ must be solved numerically. Once μ is known, the total energy per atom, the specific heat C = dE/dT, and the entropy S = -dF/dT can be evaluated. The paramagnetic energy and entropy are available in closed form. For the ferromagnetic and SDW states, a standard root-finding approach (e.g., bisection or Brent’s method) can determine μ(T) on a dense temperature grid. The temperature range should start at T=0 and extend to at least 1.5 times the Néel temperature of the SDW state, which must be found as part of the solution by locating where μ→0. The specific heat and entropy curves are then obtained by numerical differentiation or from the analytical expressions derived from the Hartree-Fock free energy. All quantities are to be expressed in reduced units: energies in units of I, temperatures in units of 1/k_B, and entropies and specific heats in units of k_B.

The following explicit Hartree‑Fock self‑consistency equations and thermodynamic formulas apply to the half‑filled band (n=1) with the piecewise‑linear band in the limit ε_i→0 and Δ=0.2I (I is taken as the energy unit, so set I=1 in the computation).

**Paramagnetic state (P):**

μ=0

Energy per atom: E_P(β) = -Δ tanh(βΔ/2) + 1/4

Entropy: S_P(β) = 2 ln 2 - βΔ tanh(βΔ/2) + 2 ln cosh(βΔ/2) (units of k_B)

Specific heat: C_P = dE_P/dT = -β^2 dE_P/dβ (compute analytically or by finite differences).

**Spin‑density‑wave state (SDW, λ=1):**
For β > β_N (T < T_N, where β_N = 1/(k_B T_N)):

Self‑consistency condition for the amplitude μ (dimensionless):
   I/(2d) tanh(β d/2) = 1,
   where d = sqrt(Δ^2 + (μ/2)^2) (using I=1).

Energy per atom:
   E_SDW(β) = - (Δ^2/d) tanh(β d/2) + (1/4)(1 - μ^2).

Entropy (analytic expression):
   S_SDW(β) = 2 ln 2 - (1+2d) ln(1+2d) - (1-2d) ln(1-2d) (units of k_B).

Specific heat: C_SDW = dE_SDW/dT = -β^2 dE_SDW/dβ (numeric differentiation recommended).

For β ≤ β_N (T ≥ T_N) the SDW state becomes paramagnetic; use the paramagnetic expressions (μ=0) for E_SDW, S_SDW, C_SDW.

The Néel temperature T_N satisfies the critical condition obtained by letting μ→0:
   I/(2Δ) tanh(β_N Δ/2) = 1   (solve for β_N).

**Ferromagnetic state (F, λ=0):**
For β > β_C (T < T_C) the amplitude μ_F is the solution of:
   μ_F = ½ [ tanh( β(Δ + μ_F/2)/2 ) - tanh( β(Δ - μ_F/2)/2 ) ].

Energy per atom:
   E_F(β) = - Δ μ_F sinh(βΔ) / sinh(β μ_F/2) + (1/4)(1 - μ_F^2).

For β ≤ β_C, μ_F = 0 and the system is paramagnetic; use paramagnetic energy and entropy for E_F, S_F, C_F.

The Curie temperature T_C is given by the condition obtained from the λ=0 self‑consistency equation as μ→0:
   (I β_C / 4) sech^2(β_C Δ/2) = 1.

**Numerical implementation:**

- Set up a temperature array T from 0 to at least 1.5 × T_N, with fine spacing near the transition points.
- At each T, compute β = 1/T (use a small finite T such as 1e-6 for T=0).
- For the paramagnetic state, evaluate E_P, C_P, S_P directly.
- For the SDW state: if β > β_N, solve the self‑consistency equation using a root‑finder (e.g., scipy.optimize.brentq) for μ in [0,1]; then compute E_SDW, S_SDW from the formulas above; C_SDW by numerical differentiation (e.g., finite differences or evaluate dE/dT by chain rule). For β ≤ β_N set μ_SDW=0, E_SDW = E_P, etc.
- For the ferromagnetic state: if β > β_C, solve for μ_F ∈ [0,1]; compute E_F; otherwise set μ_F=0, E_F = E_P.
- Ensure high accuracy (relative tolerance 1e-10) in root‑finding to obtain smooth curves.
- Output the table as a CSV file.

## Reproduction target
Produce a CSV file `thermodynamic_data.csv` containing the temperature-dependent Hartree-Fock thermodynamic quantities for the paramagnetic, ferromagnetic, and spin-density-wave (λ=1) states at half-filling (n=1) with Δ=0.2 I. The columns must be: T (temperature, units 1/k_B), E_P, E_F, E_SDW (energy per atom, units of I), mu_F, mu_SDW (amplitude, dimensionless), C_P, C_F, C_SDW (specific heat, units of k_B), S_P, S_SDW (entropy, units of k_B). The temperature grid must start at T=0 and extend to at least 1.5 times the Néel temperature T_N of the SDW state, with sufficient density to capture the rapid variations near the phase transitions. The row at T=0 must be included. The final CSV is the only required output and will be evaluated against physical and numerical checks by an automated verifier.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Hartree‑Fock thermodynamic curves
- Role: scored (load-bearing)
- Action: Implement the Hartree‑Fock self‑consistency equations for n=1, Δ=0.2I, and the band model in the limit ε_i→0. Solve for the temperature‑dependent energy per atom, amplitude, specific heat, and entropy for the paramagnetic (μ=0), ferromagnetic (λ=0), and spin‑density‑wave (λ=1) states. Sample a temperature grid from T=0 up to at least T=1.5×T_N (the SDW Néel temperature). For each temperature, compute E_P, E_F, E_SDW, mu_F, mu_SDW, C_P, C_F, C_SDW, S_P, S_SDW. Save the results to a CSV file.
- Output file: `/app/outputs/thermodynamic_data.csv`
- Format: csv
- Contract: Columns: T (temperature in units of 1/k_B), E_P, E_F, E_SDW (energy per atom in units of I), mu_F, mu_SDW (amplitude, dimensionless), C_P, C_F, C_SDW (specific heat in units of k_B), S_P, S_SDW (entropy in units of k_B). Each row corresponds to a temperature point. T values start at 0 and extend to at least 1.5 times the Néel temperature T_N.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_data.csv
- path: `/app/outputs/thermodynamic_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature‑dependent Hartree‑Fock thermodynamic quantities for paramagnetic, ferromagnetic, and spin‑density‑wave states at half‑filling with Δ=0.2I.
- schema:
  - `type`: table
  - `required_columns`: `T`, `E_P`, `E_F`, `E_SDW`, `mu_F`, `mu_SDW`, `C_P`, `C_F`, `C_SDW`, `S_P`, `S_SDW`
  - `units`:
    - `T`: 1/k_B
    - `E_P`: energy per atom in units of I
    - `E_F`: energy per atom in units of I
    - `E_SDW`: energy per atom in units of I
    - `mu_F`: dimensionless
    - `mu_SDW`: dimensionless
    - `C_P`: specific heat in units of k_B
    - `C_F`: specific heat in units of k_B
    - `C_SDW`: specific heat in units of k_B
    - `S_P`: entropy in units of k_B
    - `S_SDW`: entropy in units of k_B

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "E_P",
          "E_F",
          "E_SDW",
          "mu_F",
          "mu_SDW",
          "C_P",
          "C_F",
          "C_SDW",
          "S_P",
          "S_SDW"
        ],
        "units": {
          "T": "1/k_B",
          "E_P": "energy per atom in units of I",
          "E_F": "energy per atom in units of I",
          "E_SDW": "energy per atom in units of I",
          "mu_F": "dimensionless",
          "mu_SDW": "dimensionless",
          "C_P": "specific heat in units of k_B",
          "C_F": "specific heat in units of k_B",
          "C_SDW": "specific heat in units of k_B",
          "S_P": "entropy in units of k_B",
          "S_SDW": "entropy in units of k_B"
        }
      },
      "description": "Temperature‑dependent Hartree‑Fock thermodynamic quantities for paramagnetic, ferromagnetic, and spin‑density‑wave states at half‑filling with Δ=0.2I."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted `thermodynamic_data.csv` will be checked by an automated verifier program. The verifier recomputes key physical quantities from your CSV (such as zero-temperature energies, critical temperatures where the amplitudes vanish, energy ordering among the three phases, behaviour of the specific heat, and the high-temperature entropy limits) and compares them to expected values derived from the underlying model. It also checks numerical consistency, monotonicity, and the presence of required features like a specific-heat discontinuity at the transition. The verifier combines these checks into a weighted score between 0 and 1. You must solve the Hartree-Fock equations accurately to obtain a high score; simply returning approximate or made-up numbers will not suffice because the verifier has access to precise benchmark values (which are not disclosed to you) and will penalize deviations. No external datasets or models are required; the score depends solely on your computation.
