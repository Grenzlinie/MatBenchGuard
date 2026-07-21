# Impurity-induced LDOS, spin texture, and RKKY interaction on topological superconductor surface

## Problem background
We consider a magnetic impurity placed on the surface of a three-dimensional topological superconductor, specifically a superconducting doped topological insulator such as CuxBi2Se3 in the odd-parity triplet pairing phase. The surface of this material hosts gapless Majorana fermion modes that are protected by time-reversal symmetry. Because of spin-orbit and pairing symmetries, a magnetic impurity couples almost exclusively to the out-of-plane (Ising) component of the surface spin density. This impurity scattering is predicted to induce in-gap bound states, modify the local density of states (LDOS) around the impurity, generate a distinctive energy-resolved spin texture, and mediate an RKKY interaction between impurities. The goal of this computational task is to evaluate these observables for a fixed impurity coupling strength and to extract their spatial decay laws, their symmetry properties under energy reversal, and the sign of the magnetic interaction between impurities.

## Approach
We work with the low-energy effective Hamiltonian for the gapless Majorana surface modes. A static magnetic impurity is modelled by a local scattering potential whose matrix element is proportional to the out-of-plane spin density, with strength Unz. The impurity effect is treated within the T‑matrix formalism, using the bare retarded Green’s function of the Majorana surface states. In real space, this bare Green’s function is expressed in terms of Bessel functions of the first and second kind (J0, Y0, J1, Y1). The full impurity‑renormalized Green’s function then yields analytic expressions for the modification of the LDOS and the energy‑resolved spin density vector as functions of distance R and energy ω. The RKKY spin susceptibility χzz(R) is obtained by integrating out the Majorana modes. All quantities are evaluated numerically using the scipy library for the required Bessel functions. The energy unit is set to Δ = 1, the length unit to a = 1 (where a = ℏvs/Δ), and the impurity coupling is fixed to Unz = 1.0. A short-distance cutoff a0 = 0.01a is used to regularize the on‑site Green’s function when needed.

### Analytic formulas to be implemented

**Bare Green’s function components**
For a given energy ω (in units of Δ) and distance R (in units of a), define the complex functions

\[
\begin{aligned}
f_0(R,\omega) &= -\operatorname{sgn}(\omega) J_0(|\omega|R) - i\, Y_0(|\omega|R),\\
f_1(R,\omega) &= -i\, J_1(|\omega|R) + \operatorname{sgn}(\omega)\, Y_1(|\omega|R),
\end{aligned}
\]

where \(J_0,J_1\) and \(Y_0,Y_1\) are the Bessel functions of the first and second kind, respectively, and \(\operatorname{sgn}(\omega)\) is the sign of ω (the convention \(\operatorname{sgn}(0)=0\) can be used, though ω = 0 is not needed except at the limit).

The unperturbed on‑site Green’s function at the short‑distance cutoff a0 is

\[
g_0(\omega) = \frac{i\omega}{4}\, f_0(a_0, \omega).
\]

**Scattering amplitude**
The impurity scattering introduces a frequency‑dependent factor

\[
B(\omega) = \frac{U n_z \,\omega^2}{16\pi\, \bigl[1 - (U n_z)^2 \, g_0(\omega)^2\bigr]},
\]

where \(U n_z = 1.0\) is the product of the exchange coupling and the classical impurity spin projection onto the Ising direction (normal to the surface).

**LDOS – local density of states**
The impurity‑modified LDOS at position \(\mathbf{R}\) (with distance \(R = |\mathbf{R}|\)) and energy ω is

\[
\rho(R,\omega) = \frac{|\omega|}{4} \;+\; 2\,U n_z\;\operatorname{Im}\!\Bigl[ B(\omega)\,\bigl(f_0(R,\omega)^2 - f_1(R,\omega)^2\bigr) \Bigr].
\]

The first term is the pristine surface LDOS; the second term is the impurity‑induced correction.

**Energy‑resolved spin density vector**
The three components of the spin density at energy ω and at position \(\mathbf{R}\) (with angle \(\theta_R\) measured from the x‑axis, so that \(\cos\theta_R = R_x/R\), \(\sin\theta_R = R_y/R\)) are

\[
\begin{aligned}
s_z(R,\omega) &= \operatorname{Im}\!\Bigl[ B(\omega)\,\bigl(f_0(R,\omega)^2 + f_1(R,\omega)^2\bigr) \Bigr],\\[4pt]
s_x(R,\omega) &= \operatorname{Im}\!\Bigl[ B(\omega)\,\bigl(-2i\,f_0(R,\omega)\,f_1(R,\omega)\cos\theta_R\bigr) \Bigr],\\[4pt]
s_y(R,\omega) &= \operatorname{Im}\!\Bigl[ B(\omega)\,\bigl(-2i\,f_0(R,\omega)\,f_1(R,\omega)\sin\theta_R\bigr) \Bigr].
\end{aligned}
\]

For the purpose of this task you may choose \(\theta_R = 0\) (placing the observation point on the x‑axis), which makes \(s_y = 0\).

**RKKY spin susceptibility**
The impurity‑mediated RKKY interaction between two classical impurities separated by a distance R yields the out‑of‑plane spin susceptibility

\[
\chi_{zz}(R) = -\frac{1}{8\pi R^3}.
\]

This expression is valid in the limit of large separation (the same length units apply).

**Impurity‑induced bound‑state resonance energy**
A localized in‑gap bound state appears when the scattering amplitude diverges, i.e., when the denominator of \(B(\omega)\) vanishes. The resonance energy \(\omega_{\text{loc}}\) is therefore the positive solution of

\[
|U n_z\, g_0(\omega)| = 1.
\]

Numerically solve this equation for \(\omega > 0\) using the same cutoff \(a_0 = 0.01\) and the fixed coupling \(U n_z = 1.0\).

## Reproduction target
Using the parameters \(U n_z = 1.0\), Δ = 1, a = 1, and the short‑distance cutoff \(a_0 = 0.01\), compute the following four target quantities:

(a) the impurity‑modified LDOS \(\rho(R, \omega = -0.7\Delta)\) on a spatial grid of at least 20 distances R between 0.1a and 10a, to determine its spatial decay behaviour;

(b) the three components of the energy‑resolved spin density vector \(s_x(R,\omega), s_y(R,\omega), s_z(R,\omega)\) at a fixed distance R = 0.5a, for at least 200 equally spaced energies ω from \(-\Delta\) to \(\Delta\), to reveal the parity of each component under \(\omega \to -\omega\) and to test a sum rule for the in‑plane components;

(c) the RKKY susceptibility \(\chi_{zz}(R)\) on the same spatial grid as in (a), to extract its distance dependence and its sign;

(d) the positive impurity‑induced bound‑state resonance energy \(\omega_{\text{loc}}\) (in units of Δ) obtained by solving the pole condition \(|U n_z g_0(\omega)| = 1\) at the given coupling strength.

## Assets

- scipy: scipy

## Workflow steps

### Step 1: Compute LDOS spatial decay
- Role: scored
- Action: Evaluate the impurity-modified local density of states \(\rho(R, \omega = -0.7\Delta)\) using the analytic formulas above (impurity coupling \(U n_z = 1.0\), energy unit Δ = 1, length unit a = 1, cutoff \(a_0 = 0.01\)) for at least 20 R values from 0.1a to 10a, and write the results to `ldos_decay.csv`.
- Output file: `/app/outputs/ldos_decay.csv`
- Format: csv
- Contract: Columns: `R` (distance in units of a), `rho` (LDOS dimensionless at ω = -0.7Δ). At least 20 rows.
- Scoring: scored by hidden verifier

### Step 2: Compute energy-resolved spin density parity
- Role: scored
- Action: Evaluate the spin density components \(s_x, s_y, s_z\) at R = 0.5a for ω from -Δ to Δ (at least 200 equally spaced points) using the analytic formulas (same parameters, position on the x‑axis, i.e. θ_R = 0), and write the results to `spin_parity.csv`.
- Output file: `/app/outputs/spin_parity.csv`
- Format: csv
- Contract: Columns: `omega` (in units of Δ), `s_x`, `s_y`, `s_z` (dimensionless). At least 200 rows.
- Scoring: scored by hidden verifier

### Step 3: Compute RKKY susceptibility spatial decay
- Role: scored
- Action: Compute the RKKY spin susceptibility \(\chi_{zz}(R)\) using the analytic expression above (with a=1) for at least 20 R values from 0.1a to 10a, and write the results to `rkky_decay.csv`.
- Output file: `/app/outputs/rkky_decay.csv`
- Format: csv
- Contract: Columns: `R` (in units of a), `chi_zz` (dimensionless). At least 20 rows.
- Scoring: scored by hidden verifier

### Step 4: Compute impurity-induced bound state resonance energy
- Role: scored (load-bearing)
- Action: Determine the resonance energy \(\omega_{\text{loc}}\) by solving the pole condition \(|U n_z g_0(\omega)| = 1\) with the short-distance cutoff \(a_0 = 0.01\) and \(U n_z = 1.0\), and write the positive value (in units of Δ) to `resonance_energy.txt`.
- Output file: `/app/outputs/resonance_energy.txt`
- Format: txt
- Contract: Single floating-point number: \(\omega_{\text{loc}}\) in units of Δ.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ldos_decay.csv`
- `/app/outputs/spin_parity.csv`
- `/app/outputs/rkky_decay.csv`
- `/app/outputs/resonance_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ldos_decay.csv
- path: `/app/outputs/ldos_decay.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: LDOS values at ω = -0.7Δ for a grid of R. The checker recomputes the exact values from the analytic formula and verifies spatial decay behavior.
- schema:
  - `type`: table
  - `required_columns`: `R`, `rho`
  - `units`:
    - `R`: distance in units of a
    - `rho`: dimensionless

### spin_parity.csv
- path: `/app/outputs/spin_parity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy-resolved spin density at fixed R. The checker recomputes the exact values and verifies parity properties and a sum rule for in-plane components.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `s_x`, `s_y`, `s_z`
  - `units`:
    - `omega`: energy in units of Δ
    - `s_x`: dimensionless
    - `s_y`: dimensionless
    - `s_z`: dimensionless

### rkky_decay.csv
- path: `/app/outputs/rkky_decay.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: RKKY susceptibility χ_zz for a grid of R. The checker recomputes the exact values and verifies spatial decay behavior and sign.
- schema:
  - `type`: table
  - `required_columns`: `R`, `chi_zz`
  - `units`:
    - `R`: distance in units of a
    - `chi_zz`: dimensionless

### resonance_energy.txt
- path: `/app/outputs/resonance_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Resonance energy ω_loc from the pole condition |U n_z g_0| = 1 for U n_z = 1.0. The checker recomputes ω_loc and compares within a tight relative tolerance.
- schema:
  - `type`: text

Notes: All scored artifacts are recomputed by the checker using the same analytic formulas and identical parameters (U n_z = 1.0, a = 1, Δ = 1, a0 = 0.01a). The checker also performs structural checks: decay exponent and sign for LDOS and RKKY, parity and sum rule for spin density. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ldos_decay.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "rho"
        ],
        "units": {
          "R": "distance in units of a",
          "rho": "dimensionless"
        }
      },
      "description": "LDOS values at ω = -0.7Δ for a grid of R. The checker recomputes the exact values from the analytic formula and verifies spatial decay behavior."
    },
    {
      "file": "spin_parity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "s_x",
          "s_y",
          "s_z"
        ],
        "units": {
          "omega": "energy in units of Δ",
          "s_x": "dimensionless",
          "s_y": "dimensionless",
          "s_z": "dimensionless"
        }
      },
      "description": "Energy-resolved spin density at fixed R. The checker recomputes the exact values and verifies parity properties and a sum rule for in-plane components."
    },
    {
      "file": "rkky_decay.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "chi_zz"
        ],
        "units": {
          "R": "distance in units of a",
          "chi_zz": "dimensionless"
        }
      },
      "description": "RKKY susceptibility χ_zz for a grid of R. The checker recomputes the exact values and verifies spatial decay behavior and sign."
    },
    {
      "file": "resonance_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Resonance energy ω_loc from the pole condition |U n_z g_0| = 1 for U n_z = 1.0. The checker recomputes ω_loc and compares within a tight relative tolerance."
    }
  ],
  "notes": "All scored artifacts are recomputed by the checker using the same analytic formulas and identical parameters (U n_z = 1.0, a = 1, Δ = 1, a0 = 0.01a). The checker also performs structural checks: decay exponent and sign for LDOS and RKKY, parity and sum rule for spin density. No gold values or tolerances are disclosed here."
}
```