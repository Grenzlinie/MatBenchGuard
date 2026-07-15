# Derive low-temperature spin-wave frequency and damping from MGA for classical spin chain

## Problem background
The spectral density method (SDM) is a technique for obtaining self-consistent descriptions of excitation spectra in many-body systems. Traditionally it uses a polar (undamped) ansatz, which discards damping effects. Extending SDM to include finite lifetime widths with a Gaussian ansatz has been done for Fermi systems, but applying it to classical and Bose systems introduces sign-definiteness and divergence problems. This work proposes a Modified Gaussian Ansatz (MGA) that multiplies the spectral density by a factor that restores physical behavior—specifically, for classical systems the factor is the frequency ω. The approach is tested on a classical isotropic spin‑S ferromagnetic linear chain in an external magnetic field, aiming to compute the low‑temperature spin‑wave frequency, damping, magnetization, and spin correlation function in a self‑consistent manner that includes damping.

## Approach
We consider the classical spin‑S ferromagnetic chain Hamiltonian in an external magnetic field:
\[ \mathcal{H} = -I \sum_{i=1}^{N} \mathbf{S}_i \cdot \mathbf{S}_{i+1} - h \sum_{i=1}^{N} S_i^z, \]
where \(I\) (exchange) and \(h\) (field) are positive, and spins are described in terms of canonical variables \(\{\varphi_i, S_i^z\}\).

The object of interest is the spectral density
\[ \Lambda_k(\omega) = -\mathrm{i} \int_{-\infty}^{+\infty} dt\, e^{i\omega t} \langle \{ S_{-k}^-, S_k^+(t) \} \rangle, \]
with \(S_k^\pm = S_k^x \pm i S_k^y\) the Fourier components of the spins. Within the spectral density method we adopt the Modified Gaussian Ansatz (MGA)
\[ \Lambda_k(\omega) = 2\pi\,\omega\,\lambda_k \frac{ \exp[-(\omega-\omega_k)^2/\Gamma_k] }{ \sqrt{\pi\,\Gamma_k} }, \]
subject to the condition \(\omega_k^2/\Gamma_k \gg 1\) at low temperatures.

The unknown parameters \(\lambda_k,\omega_k,\Gamma_k\) are determined from the first three spectral moments:
\[
\begin{aligned}
\int_{-\infty}^{+\infty} \frac{d\omega}{2\pi} \Lambda_k(\omega) &= 2 N m, \\
\int_{-\infty}^{+\infty} \frac{d\omega}{2\pi} \omega \Lambda_k(\omega) &= 2 I (1-\cos k) \frac{1}{N}\sum_p \cos p \Bigl[ \langle S_p^- S_{-p}^- \rangle + 2 \langle S_p^z S_{-p}^z \rangle \Bigr] + 2 h N m, \\
\int_{-\infty}^{+\infty} \frac{d\omega}{2\pi} \omega^2 \Lambda_k(\omega) &= 4 I (1-\cos k)[2 I m (1-\cos k) + h] \frac{1}{N}\sum_p \cos p \langle S_p^+ S_{-p}^- \rangle \\
&\qquad + 8 I (1-\cos k)[I m (1-\cos k) + h] \frac{1}{N}\sum_p \cos p \langle S_p^z S_{-p}^z \rangle + 2 h^2 N m.
\end{aligned}
\]

In (3) we used the decoupling approximations \(\langle S_k^z S_p^+ S_q^- \rangle \to \langle S_k^z \rangle \langle S_p^+ S_q^- \rangle\) and \(\langle S_k^z S_p^z S_q^z \rangle \to \langle S_k^z \rangle \langle S_p^z S_q^z \rangle\).

Using the exact relation \(\langle S_p^+ S_{-p}^- \rangle = T \int \frac{d\omega}{2\pi} \frac{\Lambda_p(\omega)}{\omega}\) and, for low fields, the approximation \(S_i^z \approx S - \frac{1}{2S} S_i^+ S_i^-\), one finds
\[
\frac{1}{N}\sum_p \cos p \langle S_p^z S_{-p}^z \rangle \simeq N S^2 - \frac{1}{N}\sum_p \langle S_p^+ S_{-p}^- \rangle + \frac{T}{4 S^2} \frac{1}{N^3} \sum_{k_3,k_4} e^{i(k_3+k_4)} \int \frac{d\omega}{2\pi} \frac{\Lambda_{k_3,k_4}(\omega)}{\omega},
\]
where the higher‑order spectral density \(\Lambda_{k_3,k_4}\) is decoupled as
\[
\Lambda_{k_3,k_4}(\omega) = -\Bigl[ \delta_{k_3,-k_4} \sum_{k_1} \langle S_{k_1}^+ S_{-k_1}^- \rangle + \langle S_{k_3}^+ S_{-k_3}^- \rangle \Bigr] \Lambda_{k_4}(\omega).
\]

Putting everything together yields a closed system of self‑consistent equations:
\[
\begin{aligned}
\lambda_k &= 2 N m / \omega_k,\\[2pt]
\omega_k + \frac{\Gamma_k}{2\omega_k} &= h + 2 I (1-\cos k)\Bigl[ T(\alpha_1-\alpha_2) + S - \frac{m T^2}{S^2}(\alpha_1^2+\alpha_2^2) \Bigr],\[2pt]
\omega_k^2 + \frac{3}{2}\Gamma_k &= h^2 + 8 I^2 (1-\cos k)^2 m\Bigl[ T(\alpha_1-\alpha_2/2) + \frac12\bigl(S - \frac{m T^2}{S^2}(\alpha_1^2+\alpha_2^2)\bigr) \Bigr] \\
&\qquad + 4 I h (1-\cos k)\Bigl[ T(\alpha_1-\alpha_2) + S - \frac{m T^2}{S^2}(\alpha_1^2+\alpha_2^2) \Bigr],
\end{aligned}
\]
with the magnetization and auxiliary integrals
\[
m \simeq S - \frac{T\alpha_2}{1 - T\alpha_2/S}, \qquad
\alpha_1(T) = \frac{1}{\pi}\int_0^\pi dp\,\frac{\cos p}{\omega_p}, \qquad
\alpha_2(T) = \frac{1}{\pi}\int_0^\pi dp\,\frac{1}{\omega_p}.
\]

In the low‑temperature limit, where \(\omega_k^2/\Gamma_k \gg 1\), the system (4) can be solved analytically. Perform this solution to leading order in \(T\), obtaining explicit formulas for \(\omega_k\), \(\Gamma_k\), and the magnetization \(m\). Then compute the correlation function from \(\langle S_k^+ S_{-k}^- \rangle = T\,\lambda_k\) using the expression for \(\lambda_k\) in (4).

These derived formulas constitute the low‑temperature analytical results to be implemented as numeric Python functions.

## Reproduction target
Produce a Python module `derived_expressions.py` that exposes four functions computing the low‑temperature analytic results:
- `omega(k, I, h, S, T)` → float: spin‑wave frequency spectrum,
- `Gamma(k, I, h, S, T)` → float: damping factor,
- `magnetization(I, h, S, T)` → float: magnetization,
- `correlation(k, I, h, S, T)` → float: normalized spin correlation function ⟨S_k⁺ S₋ₖ⁻⟩/(N S²).
All inputs are scalar numerics (k in [0, 2π], positive exchange I, field h, spin S, low temperature T). The module must be self‑contained (imports allowed) and runnable with standard Python 3.

## Assets

- SymPy: sympy
- NumPy: numpy

## Workflow steps

### Step 1: Derive self-consistent equations with MGA
- Role: process
- Action: Set up the classical spin-S ferromagnetic chain Hamiltonian in external field, define the spectral density and assume the modified Gaussian ansatz (MGA) with F(ω)=ω. Compute the first three spectral moments using the decoupling approximations described in the paper. Express the correlation functions in terms of the spectral density, apply the low-field approximation for the z-component, and decouple the higher-order spectral density to obtain the closed self-consistent equations for λ_k, ω_k, Γ_k, and magnetization m, along with the definitions of α₁ and α₂.
- Evidence: `/app/outputs/derivation_report.txt`

### Step 2: Produce low-temperature analytical expressions
- Role: scored (load-bearing)
- Action: Solve the self-consistent equations analytically in the low-temperature limit under the condition ω_k²/Γ_k ≫ 1. Implement four Python functions in derived_expressions.py that compute the low-temperature results: omega(k, I, h, S, T) -> float (frequency spectrum), Gamma(k, I, h, S, T) -> float (damping factor), magnetization(I, h, S, T) -> float (magnetization), correlation(k, I, h, S, T) -> float (normalized spin correlation function). Each function must accept scalar numeric inputs and return the corresponding quantity as a float according to the paper's derived analytical expressions.
- Output file: `/app/outputs/derived_expressions.py`
- Format: txt
- Contract: Python module containing functions: omega(k, I, h, S, T) -> float; Gamma(k, I, h, S, T) -> float; magnetization(I, h, S, T) -> float; correlation(k, I, h, S, T) -> float. All inputs are scalar numerics (k in [0, 2π], I>0 exchange, h>0 field, S>0 spin, T>0 low temperature).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/derived_expressions.py`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### derived_expressions.py
- path: `/app/outputs/derived_expressions.py`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Scored module containing the low-temperature analytical expressions for spin-wave frequency, damping, magnetization, and spin correlation function derived from the MGA approach for the classical spin chain.
- schema:
  - `type`: python_module
  - `functions`: `omega(k, I, h, S, T) -> float`, `Gamma(k, I, h, S, T) -> float`, `magnetization(I, h, S, T) -> float`, `correlation(k, I, h, S, T) -> float`
  - `notes`: All inputs are scalars; output is a float representing the physical quantity as defined in the low-temperature limit.

Notes: The checker will import derived_expressions.py and compare the numeric output of each function to the paper's exact formulas at hidden parameter values using a relative tolerance. The functions must be deterministic and numerically stable.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "derived_expressions.py",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "python_module",
        "functions": [
          "omega(k, I, h, S, T) -> float",
          "Gamma(k, I, h, S, T) -> float",
          "magnetization(I, h, S, T) -> float",
          "correlation(k, I, h, S, T) -> float"
        ],
        "notes": "All inputs are scalars; output is a float representing the physical quantity as defined in the low-temperature limit."
      },
      "description": "Scored module containing the low-temperature analytical expressions for spin-wave frequency, damping, magnetization, and spin correlation function derived from the MGA approach for the classical spin chain."
    }
  ],
  "notes": "The checker will import derived_expressions.py and compare the numeric output of each function to the paper's exact formulas at hidden parameter values using a relative tolerance. The functions must be deterministic and numerically stable."
}
```

## How you are scored
After submission, a hidden verifier imports `derived_expressions.py` and evaluates each of the four functions at multiple hidden sets of parameter values (k, I, h, S, T). The returned numbers are compared to the paper’s exact low‑temperature formulas. The verifier computes a numeric reward that reflects the agreement across all functions; reporting numbers without implementing the correct analytical expressions will not earn credit.
