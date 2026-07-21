# Two-dimensional superfluid transition of adsorbed atomic hydrogen: numerical computation of surface density and KT temperature

## Problem background
Atomic hydrogen spin-polarized (H↓) can form a dilute gas that adsorbs on a superfluid helium film. The adsorbed two-dimensional layer may undergo a Kosterlitz-Thouless (KT) superfluid transition at experimentally accessible temperatures. This task computes the film's surface density as a function of temperature for several bulk gas densities, and determines the KT transition temperature, using an improved finite-temperature theory that is exact to leading order in density. The results are used to assess the conditions under which a 2D superfluid transition is expected.

## Physical model and equations

### Units and constants
Use the following fundamental constants:
- Planck constant \(h = 6.62607015\times10^{-34}\,\text{J·s}\),
- reduced Planck constant \(\hbar = h/(2\pi)\),
- Boltzmann constant \(k_{\rm B} = 1.380649\times10^{-23}\,\text{J/K} = 8.617333262\times10^{-5}\,\text{eV/K}\),
- atomic hydrogen mass \(M = 1.6735575\times10^{-27}\,\text{kg}\) (the hydrogen atom mass),
- conversion between K and atomic units of energy: 1 Hartree = 315774.6 K,
- Bohr radius \(a_0 = 0.529177\,\text{\AA}\).

All length scales in the two-body potential are given in atomic units (bohr), and energies in hartree; convert to Kelvins as needed.

### Bulk gas chemical potential
The bulk H↓ gas is treated as a classical ideal gas:
\[
\mu_{\rm G}(n,T) = k_{\rm B}T \ln\left(n\lambda^3\right),
\]
where \(n\) is the bulk number density and \(\lambda = h/\sqrt{2\pi M k_{\rm B}T}\) is the thermal de Broglie wavelength.

### 2D film chemical potential (single component)
The 2D chemical potential of the adsorbed film is
\[
\mu_{2{\rm D}}(n_s,T) = \mu_{2{\rm D}}^0(n_s,T) + \Delta\mu(n_s,T),
\]
with the ideal 2D Bose gas contribution
\[
\mu_{2{\rm D}}^0(n_s,T) = k_{\rm B}T \ln\!\left[1 - \exp\left(-n_s\lambda^2\right)\right],
\]
and the interaction correction \(\Delta\mu\) given by an exact leading-order finite-temperature expression:
\[
\Delta\mu(n_s,T) = \frac{\sum_{{\bf p},{\bf p}'} f_{{\bf p}{\bf p}'} \left(\partial n_p^0 / \partial \varepsilon_p^0\right) n_{p'}^0}{\sum_{\bf p} \partial n_p^0 / \partial \varepsilon_p^0}.
\]
Here \(\varepsilon_p^0 = p^2/(2M)\) and
\[
n_p^0 = \left[\exp\!\left(\frac{\varepsilon_p^0 - \mu_{2{\rm D}}^0}{k_{\rm B}T}\right) - 1\right]^{-1}.
\]

The function \(f_{{\bf p}{\bf p}'}\) encodes two-body interactions in two dimensions. For a single-component spin-polarized Bose gas it is obtained from the scattering phase shifts \(\delta_m(k)\) as
\[
f_{{\bf p}{\bf p}'} = -\frac{8}{MA} \sum_{m\;{\rm even}} \delta_m(k),
\]
with \(k = |{\bf p} - {\bf p}'|/2\), \(M\) the atomic mass, and \(A\) the area of the system (the factor 8 comes from the factor 4 in the general expression multiplied by a factor 2 due to Bose statistics; for identical spinless particles the sum is restricted to even partial waves and an additional factor of 2 accounts for particle indistinguishability). In practice the discrete sums over momenta are converted to integrals using \(\sum_{\bf p}\to A\int d^2p/(2\pi\hbar)^2\); the area \(A\) cancels in the final expression for \(\Delta\mu\).

### 2D film chemical potential (equal‑concentration mixture)
For a 50:50 mixture of the hyperfine states \(|a\rangle\) and \(|b\rangle\), the chemical potential is
\[
\mu_{2{\rm D}}^{\rm MIX}(n_s,T) = \mu_{2{\rm D}}^0\!\left(\frac{n_s}{2},T\right) + \Delta\mu^{\rm MIX}\!\left(\frac{n_s}{2},T\right).
\]
The correction \(\Delta\mu^{\rm MIX}\) is computed from the same formula (4) as \(\Delta\mu\), but with \(f_{{\bf p}{\bf p}'}\) replaced by \(f_{{\bf p}{\bf p}'}^{aa}+f_{{\bf p}{\bf p}'}^{ab}\). Because the two states interact through the same H–H potential, \(f^{aa}=f^{ab}=f\) so effectively one uses \(2f_{{\bf p}{\bf p}'}\) together with the reduced density \(n_s/2\) throughout.

### Scattering phase shifts
The phase shifts \(\delta_m(k)\) are obtained by solving the radial Schrödinger equation for the relative coordinate with reduced mass \(\mu_{\rm red} = M/2\). Let \(u_{m}(r) = r R_{m}(r)\). The equation is
\[
\left[-\frac{\hbar^2}{2\mu_{\rm red}}\frac{d^2}{dr^2} + V(r) + \frac{\hbar^2 m(m+1)}{2\mu_{\rm red} r^2}\right] u_m(r) = E\, u_m(r),\quad E = \frac{\hbar^2 k^2}{2\mu_{\rm red}}.
\]
Boundary conditions:
- \(u_m(0) = 0\),
- for large \(r\), \(u_m(r) \sim \sin(kr - m\pi/2 + \delta_m(k))\).

The solution is performed numerically using the Numerov method. After obtaining the wave function, the phase shift \(\delta_m(k)\) is extracted by matching at a large radius.

### Triplet H–H interaction potential
The analytic form for the triplet potential is, in atomic units (\(r\) in \(a_0\), energy in Hartree):
\[
V(r) = \exp\!\left(0.09678 - 1.10173\, r - 0.039\, r^{2}\right)
      + C(r)\left(\frac{6.5}{r^{6}} + \frac{124}{r^{8}} + \frac{3285}{r^{10}}\right),
\]
with
\[
C(r) = \begin{cases}
1, & r > 10.0378, \\
\exp\!\left[-\left(\frac{10.0378}{r} - 1\right)^{2}\right], & r \leq 10.0378.
\end{cases}
\]

### T = 0 chemical potential
For the zero-temperature limit, the interaction is weakly attractive and can be modelled with a hard-disc potential whose radius equals the 3D scattering length. The leading-order expression for the 2D chemical potential is
\[
\mu_{2{\rm D}}(n_s,0) = -\frac{4\pi\hbar^2}{M} \frac{n_s}{\ln(n_s a^2)},
\]
with scattering length \(a = 0.727\,\text{\AA}\), which is obtained from effective-range theory for the triplet potential above.

### Constructing \(f_{{\bf p}{\bf p}'}(k)\)
For each required angular momentum index \(m\) (even integers), compute \(\delta_m(k)\) on a grid of \(k\) values. Construct \(f_{{\bf p}{\bf p}'}(k) = -\frac{8}{MA} \sum_{m\;{\rm even}} \delta_m(k)\) up to a cutoff where the series has converged. Because \(f_{{\bf p}{\bf p}'}\) enters only in the combination that cancels \(A\), it is convenient to absorb the factor \(1/A\) into a momentum integral weight. The resulting function of \(k\) is interpolated (e.g., with a cubic spline) for efficient use in the integrals for \(\Delta\mu\).

### Triple‑integral evaluation of \(\Delta\mu\)
The expression for \(\Delta\mu\) is transformed to a triple integral over momenta that is computed numerically via Romberg integration. The necessary kernels involve the interpolated \(f(k)\) and the Bose occupation numbers computed from the current estimate of \(\mu_{2{\rm D}}^0\).

### Low‑temperature interpolation
The finite‑temperature theory is valid only above the KT transition. For \(T < T_{\rm KT}\) the chemical potential is approximated by a linear interpolation between the \(T=0\) value and the value at \(T_{\rm KT}\):
\[
\mu_{2{\rm D}}(n_s,T) = \mu_{2{\rm D}}(n_s,0) + \frac{T}{T_{\rm KT}}\left[\mu_{2{\rm D}}(n_s,T_{\rm KT}) - \mu_{2{\rm D}}(n_s,0)\right].
\]
The KT temperature is determined self‑consistently from the condition \(n_s\lambda^2 = 4\) (see below).

### Equilibrium and KT condition
The film density \(n_s\) at given bulk density \(n_{\rm gas}\) and temperature \(T\) is obtained by solving
\[
\mu_{\rm G}(n_{\rm gas},T) = E_a + \mu_{2{\rm D}}(n_s,T),
\]
with the adsorption energy \(E_a = 0.9\,\text{K}\). For the mixture the left‑hand side uses \(\mu_{\rm G}\) as before (the bulk gas is still treated as a classical ideal gas) and the right‑hand side uses \(\mu_{2{\rm D}}^{\rm MIX}\).

The KT transition temperature \(T_{\rm KT}\) for a given bulk density is located by finding the temperature at which the self‑consistent film density satisfies
\[
n_s\lambda^2 = 4,
\]
assuming the superfluid density equals the total film density and the effective mass \(M^*=M\).

## Approach
The calculation proceeds through several numerical stages:
1. Compute scattering phase shifts \(\delta_m(k)\) by solving the radial Schrödinger equation with the triplet potential using the Numerov method.
2. Construct the effective momentum‑dependent interaction kernel \(f_{{\bf p}{\bf p}'}(k)\) from the phase shifts, interpolating for later integration.
3. Evaluate the interaction shift \(\Delta\mu\) at finite temperature via the formula above, using Romberg integration (after converting sums to integrals).
4. For \(0 < T < T_{\rm KT}\), linearly interpolate between the \(T=0\) value and the finite‑temperature value at \(T_{\rm KT}\).
5. Solve the equilibrium condition to obtain \(n_s(T)\) for each required bulk density and for single‑component and mixture cases.
6. Determine \(T_{\rm KT}\) by enforcing \(n_s\lambda^2 = 4\) on the resulting \(n_s(T)\) curves.

## Reproduction target
The reproduction target consists of three computed quantities:
- The 2D chemical potential \(\mu_{2{\rm D}}\) as a function of temperature at a fixed surface density \(n_s = 10^{13}\,\text{cm}^{-2}\) (file `mu_vs_T.csv`).
- The surface density \(n_s\) as a function of temperature for three bulk gas densities (\(1\times10^{17}\), \(1\times10^{18}\), \(1\times10^{19}\,\text{cm}^{-3}\)) for both a single‑component H↓ gas and an equal‑concentration mixture of hyperfine states (file `ns_vs_T.csv`).
- The KT transition temperature at a bulk gas density of \(1\times10^{18}\,\text{cm}^{-3}\) for the mixture and for the single‑type H↓ (file `KT_temperatures.json`).

## Assets
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute scattering phase shifts
- Role: process
- Action: Compute scattering phase shifts \(\delta_m(k)\) as a function of relative momentum \(k\) for even angular momenta \(m\) up to convergence, by solving the radial Schrödinger equation numerically with the Numerov method and the triplet potential. Extract \(\delta_m(k)\) at large \(r\).
- Evidence: none

### Step 2: Construct effective interaction \(f_{{\bf p}{\bf p}'}\)
- Role: process
- Action: From the phase shifts construct the function \(f(k) \propto \sum_{m\;{\rm even}} \delta_m(k)\), absorb the area factor appropriately, and produce an interpolated function or table for subsequent integration.
- Evidence: none

### Step 3: Compute 2D chemical potential \(\mu_{2{\rm D}}\) for fixed surface density
- Role: scored
- Action: Compute the total 2D chemical potential for \(n_s = 10^{13}\,\text{cm}^{-2}\) as a function of temperature \(T\).
  - For \(T > T_{\rm KT}\): compute \(\mu_{2{\rm D}}^0\), occupation numbers, energy derivatives, and the interaction shift \(\Delta\mu\) via the integral expression, using Romberg integration.
  - For \(T = 0\): use the hard‑disc formula with \(a = 0.727\,\text{\AA}\).
  - For \(0 < T < T_{\rm KT}\): linearly interpolate between the \(T=0\) value and the full result at \(T_{\rm KT}\).
- Output file: `/app/outputs/mu_vs_T.csv`
- Format: csv
- Contract: Columns: `T (K)`, `mu_2D (K)`. At least 50 rows covering \(T = 0.01\) to \(0.50\,\text{K}\).
- Scoring: scored by hidden verifier

### Step 4: Determine surface density \(n_s(T)\) from equilibrium
- Role: scored (load-bearing)
- Action: For each bulk gas density \(n_{\rm gas} \in \{10^{17}, 10^{18}, 10^{19}\}\,\text{cm}^{-3}\) and for both single‑type H↓ and a 50:50 mixture, solve \(\mu_{\rm G}(n_{\rm gas},T) = E_a + \mu_{2{\rm D}}(n_s,T)\) to obtain the film density \(n_s\) as a function of \(T\).
  - For the mixture, use \(\mu_{2{\rm D}}^{\rm MIX}\) as defined above (ideal part with \(n_s/2\) and interaction correction with \(2f\) and \(n_s/2\)).
  - Total \(\mu_{2{\rm D}}\) includes the low‑\(T\) interpolation.
- Output file: `/app/outputs/ns_vs_T.csv`
- Format: csv
- Contract: Columns: `n_gas (cm^{-3})`, `component` (either `mixture` or `single`), `T (K)`, `n_s (cm^{-2})`. At least 50 temperature points per curve.
- Scoring: scored by hidden verifier

### Step 5: Locate KT superfluid transition temperatures
- Role: scored
- Action: For \(n_{\rm gas} = 10^{18}\,\text{cm}^{-3}\), find the temperature \(T_{\rm KT}\) at which the \(n_s(T)\) curve from step 4 satisfies \(n_s\lambda^2 = 4\). Report \(T_{\rm KT}\) for both mixture and single‑type H↓.
- Output file: `/app/outputs/KT_temperatures.json`
- Format: json
- Contract: JSON object with keys `mixture` and `single`, values in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mu_vs_T.csv`
- `/app/outputs/ns_vs_T.csv`
- `/app/outputs/KT_temperatures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mu_vs_T.csv
- path: `/app/outputs/mu_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: 2D chemical potential as a function of temperature at \(n_s = 10^{13}\,\text{cm}^{-2}\). The checker compares against reference values derived from the published computation.
- schema:
  - `type`: table
  - `required_columns`: `T`, `mu_2D`
  - `units`:
    - `T`: K
    - `mu_2D`: K

### ns_vs_T.csv
- path: `/app/outputs/ns_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface density as a function of temperature for given gas densities and mixture/single cases. The checker verifies the shape and representative point values against the published curves.
- schema:
  - `type`: table
  - `required_columns`: `n_gas`, `component`, `T`, `n_s`
  - `units`:
    - `n_gas`: cm\(^{-3}\)
    - `T`: K
    - `n_s`: cm\(^{-2}\)

### KT_temperatures.json
- path: `/app/outputs/KT_temperatures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: KT transition temperatures at \(n_{\rm gas}=10^{18}\,\text{cm}^{-3}\) for mixture and single-type H↓. The checker compares against reference values derived from the published calculation.
- schema:
  - `type`: object
  - `required`:
    - `mixture`: number (K)
    - `single`: number (K)

Notes: All required physical constants, the triplet potential, and the scattering length are given above; the agent must implement the numerical methods (Numerov, Romberg integration, etc.). The checker evaluates the output curves and KT temperatures against benchmarks with appropriate tolerances; simply reporting values without a genuine physics‑based computation will not suffice.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mu_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "mu_2D"
        ],
        "units": {
          "T": "K",
          "mu_2D": "K"
        }
      },
      "description": "2D chemical potential as a function of temperature at n_s = 1e13 cm^{-2}. The checker compares against reference values derived from the published computation."
    },
    {
      "file": "ns_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_gas",
          "component",
          "T",
          "n_s"
        ],
        "units": {
          "n_gas": "cm^{-3}",
          "T": "K",
          "n_s": "cm^{-2}"
        }
      },
      "description": "Surface density as a function of temperature for given gas densities and mixture/single cases. The checker verifies the shape and representative point values against the published curves."
    },
    {
      "file": "KT_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "mixture": "number (K)",
          "single": "number (K)"
        }
      },
      "description": "KT transition temperatures at n_gas = 1e18 cm^{-3} for mixture and single-type H↓. The checker compares against reference values derived from the published calculation."
    }
  ],
  "notes": "All required physical constants, the triplet potential, and the scattering length are given in the task description; the agent must implement the numerical methods. The checker will compare the agent's curves and reported KT temperatures against benchmarks with appropriate tolerances."
}
```