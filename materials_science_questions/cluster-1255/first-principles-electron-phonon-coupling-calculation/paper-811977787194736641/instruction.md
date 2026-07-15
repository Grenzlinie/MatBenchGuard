# Liquid Metal Resistivity via Mode-Coupling Approximation

## Problem background
The electrical resistivity of liquid metals and its temperature coefficient of resistivity (TCR) are fundamental transport properties that reveal the role of disorder and electron‑phonon interactions. This task calculates the dc resistivity and TCR for five liquid metals (Ag, Au, Fe, Ni, Eu) at their melting points using the mode‑coupling approximation of Götze. The method combines KKR‑derived potential form factors to describe local and non‑local scattering with a self‑consistent integral‑equation framework. The computed quantities are the resistivity in μΩ·cm and the TCR in 10⁻⁵ K⁻¹.

## Approach
The mode‑coupling formalism expresses the dc conductivity in terms of density and momentum correlation functions. Effective disorder potentials are built from KKR matrix elements using logarithmic derivatives of the muffin‑tin wave functions, separating a local part \(u_1(q)\) and a non‑local part \(u_2(q)\). The static structure factor is modelled with the Percus‑Yevick hard‑sphere approximation. The core of the method is a set of coupled integral equations for the relaxation kernels (\(L_0\), \(M_0\), \(L_T\), \(M_T\)) and the density and transverse momentum correlation functions. For each metal, the equations are iterated to self‑consistency at the given melting temperature \(T^*\), using the electron‑phonon coupling parameter \(|V|\) and potential fluctuation cutoff \(q_0\) as adjustable inputs. The converged kernels yield the dc conductivity, which is then converted to resistivity and used to extract the TCR from the temperature dependence encoded in the thermal kernels.

## Mathematical formulation

All quantities are in atomic units (ℏ = m_e = e = a_B = 1) except where noted. Energy and potential values are converted from Rydbergs (1 Ry = 0.5 Ha) to Hartree for internal consistency (multiply by 0.5).

### Input data

Material constants (from Table 1 of the paper):

| metal | E_F (Ry) | K_F (a.u.) | R_hard (a.u.) | Ω (a.u.³) | R_MT (a.u.) | δ₀ (rad) | δ₁ (rad) | δ₂ (rad) | η  | Z_N |
|-------|----------|-------------|---------------|-----------|-------------|-----------|-----------|-----------|----|-----|
| Ag    | 0.481    | 0.611       | 2.40          | 129.7     | 2.35        | -0.201    | 0.004     | 3.02      | 0.45 | 1 |
| Au    | 0.535    | 0.612       | 2.405         | 129.6     | 2.580       | -0.345    | -0.062    | 2.955     | 0.45 | 1 |
| Fe    | 0.770    | 0.693       | 2.12          | 88.8      | 2.23        | -0.479    | -0.71     | 2.52      | 0.45 | 2 |
| Ni    | 0.609    | 0.699       | 2.343         | 86.7      | 2.315       | -0.243    | 0.025     | 2.894     | 0.45 | 2 |
| Eu    | 0.224    | 0.544       | 3.42          | 367.0     | 2.43        | -0.660    | -0.198    | 0.208     | 0.45 | 2 |

Adjusted parameters and temperature (from Table 2):

| metal | T* (K) | |V| (Ry) | q₀ (a.u.⁻¹) |
|-------|--------|-----------|--------------|
| Ag    | 1273   | 0.0147    | 2.108        |
| Au    | 1336   | 0.0054    | 1.60         |
| Fe    | 1833   | 0.0034    | 2.108        |
| Ni    | 1773   | 0.0247    | 2.118        |
| Eu    | 1103   | 1.9       | 2.108        |

### Potential form factors

The KKR matrix element $\Gamma_q^{KKR}(l)$ for angular momentum $l=0,1,2$ is (Eq. 1)

$$ \Gamma_q^{KKR}(l) = \frac{4\pi R_{MT}^2}{\Omega} (2l+1) \, j_l(K R_{MT}) \, j_l(|\mathbf{K}+\mathbf{q}|R_{MT}) \; L_l , $$

where $K = K_F$, $|\mathbf{K}+\mathbf{q}| = \sqrt{K_F^2 + q^2 + 2 K_F q \cos\theta}$ with $\cos\theta = 1 - q^2/(2 K_F^2)$. The logarithmic derivative is (Eq. 2)

$$ L_l = \sqrt{E_F} \frac{ \cos\delta_l \, j_l'(x) - \sin\delta_l \, n_l'(x) }{ \cos\delta_l \, j_l(x) - \sin\delta_l \, n_l(x) } , $$

with $x = K_F R_{MT}$, and $j_l, n_l$ are spherical Bessel and Neumann functions; derivative is with respect to the argument $x$.

The local and non‑local potential form factors are (Eq. 3)

$$ u_1(q) = \Gamma_q^{KKR}(l=0) + \Gamma_q^{KKR}(l=1), \qquad u_2(q) = \Gamma_q^{KKR}(l=2). $$

### Percus–Yevick structure factor $S(q)$

For hard spheres with packing fraction $\eta = 0.45$ and diameter $d = 2 R_{\text{hard}}$, the number density is $n = 6\eta/(\pi d^3)$. The direct correlation function is

$$ c(q) = -24\eta \Bigg[ \frac{\alpha}{x^3}(\sin x - x\cos x) + \frac{\beta}{x^2}\big(2x\sin x + (2-x^2)\cos x -2\big) + \frac{\gamma}{x^5}\big(-x^4\cos x + 4[(3x^2-6)\cos x + (x^3-6x)\sin x + 6]\big) \Bigg], $$

with $x = q d$ and
$$ \alpha = \frac{(1+2\eta)^2}{(1-\eta)^4},\qquad \beta = -\frac{6\eta (1+\eta/2)^2}{(1-\eta)^4},\qquad \gamma = \frac{\eta \alpha}{2}. $$
Then
$$ S(q) = \frac{1}{1 - n c(q)}. $$

### Electron density and density of states

Electron density: $n_e = Z_N / \Omega$.

Density of states per unit volume (free‑electron): $\varrho_F = k_F/(\pi^2)$.

### Self‑consistent iteration for mode‑coupling

The unknown spectral functions are $L_0''(0), M_0''(0), \Phi_1''(q,0), \Phi_t''(q,0), \Phi''(q,0)$. The iteration uses a q‑grid $q_i \in [0,q_0]$.

1. Initialize $L_0'' = 0$, $M_0'' = 0$, and the correlation functions to zero.

2. Compute the transverse momentum correlation function $\Phi_t''(q)$ from Eqs. (A10–A12) using $M_0(z) = i M_0''$:
   $$ g_t(q) = \frac{1}{8}\left[ (5-3Q^2) + \frac{3}{2Q}(1-Q^2)^2 \ln\left|\frac{1+Q}{1-Q}\right| \right], \quad Q = q/(2K_F). $$
   $$ X_t^0(q, iM_0'') = \frac{1}{8} \Bigg[ (5-3Q^2) + \frac{3}{Q^2}\frac{(M_0'')^2}{(4E_F)^2} \\
   \quad + \frac{3}{4 Q^5} \Big( (i M_0''/(4E_F) - \Omega_+)^2 (i M_0''/(4E_F) - \Omega_-)^2 \ln\frac{i M_0''/(4E_F)-\Omega_+}{i M_0''/(4E_F)-\Omega_-} \\
   + (i M_0''/(4E_F)+\Omega_+)^2 (i M_0''/(4E_F)+\Omega_-)^2 \ln\frac{i M_0''/(4E_F)+\Omega_+}{i M_0''/(4E_F)-\Omega_-} \Big) \Bigg], $$
   with $\Omega_\pm = Q^2 \pm Q$. Then
   $$ \Phi_t''(q) = \frac{n_e}{M_0''} \, \mathrm{Im}\big[ X_t^0(q, i M_0'') \big]. $$

3. Compute the density correlation function $\Phi''(q)$ from Eq. (A5) with $z=0$:
   - Compute the bare polarizability $\Phi^0(q, i M_0'')$:
     $$ \Phi^0(q, i M_0'') = \frac{\varrho_F}{i M_0''} \big[ K^0(Q, w) - K^0(Q) \big], \quad w = \frac{i M_0''}{4E_F}, $$
     with $K^0(Q)$ given by Eq. (A7) and $K^0(Q,w)$ by Eq. (A8):
     $$ K^0(Q) = \frac12 + \frac{1}{4Q}(1-Q^2) \ln\left|\frac{Q+1}{Q-1}\right|, $$
     $$ K^0(Q,w) = \frac12 + \frac{1}{8Q} \Bigg[ \big(1-(Q-\frac{w}{Q})^2\big) \ln\frac{Q+1-\frac{w}{Q}}{Q-1-\frac{w}{Q}} + \big(1-(Q+1+\frac{w}{Q})^2\big) \ln\frac{Q+1+\frac{w}{Q}}{Q-1+\frac{w}{Q}} \Bigg]. $$
   - Compute the generalised compressibility $g(q) = \varrho_F K^0(Q)$.
   - Compute the denominator $D = 1 + \big[ M_0'' - \frac13 (q\xi)^2 L_0'' / g(q) \big] \Phi^0 / g(q)$, with $\xi = 2K_F/q_0$.
   - Then $\Phi(q,0) = \Phi^0 / D$, and $\Phi''(q) = \mathrm{Im}[\Phi]$. (Note: $M_0(z)=i M_0''$, $L_0(z)=i L_0''$, $\Phi^0$ is complex.)

4. Compute the longitudinal momentum correlation function from Eq. (A9):
   $$ \Phi_1''(q) = \frac{1}{3} (q\xi)^2 \frac{(L_0'')^2}{g(q)^2} \, \Phi''(q). $$

5. Compute the disorder‑averaged potentials using Eq. (A14) with $X_i=1$:
   $$ \langle|U_1(q)|^2\rangle = |u_1(q)|^2 S(q), $$
   $$ \langle|U_2(q)|^2\rangle = |u_2(q)|^2 S(q), $$
   $$ \langle U_1^*(q) U_2(q)\rangle = |u_1(q)| |u_2(q)| S(q). $$

6. Update the static relaxation kernels:
   $$ L_0'' = \frac{4}{q_0^7} \int_0^{q_0} dq\, q^2 \langle|U_2|^2\rangle \big[ \Phi_1''(q) + 2 \Phi_t''(q) \big], $$
   $$ M_0'' = \frac{1}{n_e q_0^3} \int_0^{q_0} dq\, q^4 \Big[ \langle|U_1|^2\rangle + 2 q_0^{-2} \langle U_1^* U_2\rangle E(q) + q_0^{-4} \langle|U_2|^2\rangle E(q)^2 \Big] \Phi''(q). $$
   Here $E(q) = (q_0^2 - q^2)/q^2$ for $0 < q \le q_0$, and $E(0)$ is taken as the limit $\lim_{q\to0} (q_0^2/q^2 - 1) \to \infty$ but multiplied by factors that vanish; in practice the integrand at $q=0$ is zero.

7. Iterate steps 2–6 until the maximum relative change in $L_0''$ and $M_0''$ is below $10^{-6}$.

### Temperature‑dependent kernels and final results

8. After convergence, compute the temperature‑dependent kernels using the converged spectral functions and the temperature $T^*$ from the table. The temperature factor $S_T(q)$ is taken proportional to $T^*$; we absorb the proportionality constant into $|V|$, effectively setting $S_T(q) = T^*$ for the integrands. Thus
   $$ L_T'' = \frac{4}{q_0^7} \int_0^{q_0} dq\, (q\,|V|)^2 \, \big[ \Phi_1''(q) + 2 \Phi_t''(q) \big] \, T^*, $$
   $$ M_T'' = \frac{1}{n_e q_0^7} \int_0^{q_0} dq\, \big[ q^2 E(q) |V| \big]^2 \, \Phi''(q) \, T^*. $$

9. DC conductivity in atomic units:
   $$ \sigma = \frac{n_e}{M_0'' + M_T''} + (L_0'' + L_T''). $$

10. Convert to resistivity in $\mu\Omega\cdot\mathrm{cm}$:
    The conversion factor from a.u. of conductivity to $(\mu\Omega\cdot\mathrm{cm})^{-1}$ is $C = 0.2434$. Hence
    $$ \rho (\mu\Omega\cdot\mathrm{cm}) = \frac{1}{C \cdot \sigma}. $$

11. Temperature coefficient of resistivity (TCR):
    $$ \mathrm{TCR} = \frac{1}{\rho}\frac{d\rho}{dT} = -\frac{1}{\sigma}\frac{d\sigma}{dT}. $$
    Using $M_T'' \propto T^*$ and $L_T'' \propto T^*$, we have:
    $$ \frac{d\sigma}{dT} = -\frac{n_e}{(M_0''+M_T'')^2} \frac{M_T''}{T^*} + \frac{L_T''}{T^*}. $$
    Therefore,
    $$ \mathrm{TCR} = \frac{1}{\sigma} \left[ \frac{n_e}{(M_0''+M_T'')^2} \frac{M_T''}{T^*} - \frac{L_T''}{T^*} \right]. $$
    The result is in $\mathrm{K}^{-1}$; multiply by $10^5$ to obtain TCR in $10^{-5}\,\mathrm{K}^{-1}$.

12. Output the resistivity ($\mu\Omega\mathrm{cm}$) and TCR ($10^{-5}\,\mathrm{K}^{-1}$) for each metal.

### Numerical guidance

Use a q‑grid of at least 200 points between 0 and $q_0$. A quadrature such as Simpson’s rule with a small cutoff near 0 (e.g., $q_{\min}=10^{-4}$) avoids singularities. Spherical Bessel functions can be computed using SciPy’s recurrence routines. To stabilise the iteration, under‑relaxation (e.g., mixing 0.5 of the new kernels with the old) is recommended.

## Reproduction target
Using the published input parameters (Fermi energy, Fermi wave vector, atomic volume, muffin‑tin radius, phase shifts \(\delta_0\)–\(\delta_2\), packing fraction \(\eta=0.45\), effective valence \(Z_N\)) and the adjusted values of \(T^*\), \(|V|\), and \(q_0\) specific to each metal, compute the dc resistivity (μΩ·cm) and TCR (10⁻⁵ K⁻¹) for Ag, Au, Fe, Ni, and Eu. Output the results as a CSV file, `resistivity_TCR.csv`, with columns `metal`, `resistivity`, `TCR`. No external dataset download is required; all parameters are taken from the paper's tables.

## Assets

- Python with NumPy/SciPy: numpy, scipy

## Workflow steps

### Step 1: Compute resistivity and TCR via mode-coupling solver
- Role: process
- Action: For each of the five liquid metals (Ag, Au, Fe, Ni, Eu), load the material input parameters (Fermi energy, Fermi wave vector, atomic volume, muffin-tin radius, phase shifts, packing fraction, effective valence) as given in the published literature values compiled by the paper. Compute the KKR matrix elements using the explicit expression and logarithmic derivative formula to obtain local u1(q) and non-local u2(q) potential form factors. Use the Percus-Yevick hard-sphere model for the static structure factor S(q). Set up the mode-coupling equations (density, longitudinal and transverse momentum correlation functions, Lindhard function, relaxation kernels, and dc conductivity expression) from the Appendix. Using the specified melting temperature T*, electron-phonon coupling parameter |V|, and potential fluctuation cutoff q0 for each metal, iterate the coupled integral equations self-consistently until convergence of the imaginary parts. Compute the dc conductivity, convert to resistivity in μΩ·cm, and determine the temperature coefficient of resistivity (TCR) from the temperature-dependent kernel parts.
- Evidence: `/app/outputs/calculation_log.json`

### Step 2: Export final resistivity and TCR
- Role: scored (load-bearing)
- Action: Write a CSV file containing the computed resistivity (μΩ·cm) and TCR (10⁻⁵ K⁻¹) for Ag, Au, Fe, Ni, Eu using the results from the mode-coupling solver.
- Output file: `/app/outputs/resistivity_TCR.csv`
- Format: csv
- Contract: Columns: metal (string), resistivity (float, μΩ·cm), TCR (float, 10⁻⁵ K⁻¹). One row per metal.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/resistivity_TCR.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### resistivity_TCR.csv
- path: `/app/outputs/resistivity_TCR.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV with columns: metal (string, one of Ag/Au/Fe/Ni/Eu), resistivity (float), TCR (float). The checker compares each row to hidden gold values from the paper's reported Table 2 with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `resistivity`, `TCR`
  - `units`:
    - `resistivity`: μΩ·cm
    - `TCR`: 10⁻⁵ K⁻¹

Notes: The task uses the final adjusted parameters |V| and q0 directly from the paper (Table 2) without requiring the agent to perform the parameter fitting stage. The solver must implement the full KKR potential model, Percus-Yevick S(q), and the mode-coupling equations as described.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "resistivity_TCR.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "resistivity",
          "TCR"
        ],
        "units": {
          "resistivity": "μΩ·cm",
          "TCR": "10⁻⁵ K⁻¹"
        }
      },
      "description": "CSV with columns: metal (string, one of Ag/Au/Fe/Ni/Eu), resistivity (float), TCR (float). The checker compares each row to hidden gold values from the paper's reported Table 2 with tolerances."
    }
  ],
  "notes": "The task uses the final adjusted parameters |V| and q0 directly from the paper (Table 2) without requiring the agent to perform the parameter fitting stage. The solver must implement the full KKR potential model, Percus-Yevick S(q), and the mode-coupling equations as described."
}
```

## How you are scored
A hidden verifier reads your `resistivity_TCR.csv` and compares each metal's resistivity and TCR to hidden reference values derived from the paper. The comparison uses tolerances appropriate for an independent re‑implementation (the exact tolerances are not revealed). Your final reward is proportional to the number of metals whose values meet the tolerance criteria, with a minimum reward for correctly formatted partial outputs. No credit is given for merely reporting the paper's numbers; you must actually execute the solver workflow.
