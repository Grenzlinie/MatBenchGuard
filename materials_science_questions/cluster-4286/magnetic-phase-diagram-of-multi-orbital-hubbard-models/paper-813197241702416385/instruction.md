# Mean-field magnetic phase diagram of an orbitally degenerate Anderson lattice

## Problem background
Heavy-fermion materials, such as certain rare-earth and actinide compounds, exhibit a complex interplay between itinerant conduction electrons and nearly localized f-electrons. At low temperatures, these systems often show coherent Fermi-liquid behavior, but magnetic instabilities—particularly ferromagnetism—can emerge depending on the f-level energy, Coulomb repulsion, and orbital degeneracy. Understanding the conditions under which a paramagnetic metallic state becomes unstable toward ferromagnetic long-range order is a central question in strongly correlated electron physics. This task addresses that question within a mean-field theory of the orbitally degenerate Anderson lattice, where the f-shell correlations are treated using slave bosons that project onto relevant electronic configurations (f⁰, f¹, f²). The goal is to numerically solve the self-consistency equations and determine key quantities such as occupation probabilities of the f configurations, total f-electron number, magnetization, and the energy gap in the Kondo-insulating regime, as a function of model parameters.

## Approach

### Model and lattice setup
The Anderson lattice has N‑fold orbital degeneracy, on‑site Coulomb repulsion U, hybridization V, and f‑level energy \varepsilon_f. Conduction electrons form a flat band of half‑bandwidth D = 10 V; the density of states per spin and orbital is \rho(\epsilon)=1/(2D) for -D \le \epsilon \le D, zero otherwise. Total electron density is fixed at n = 1.8 per site (except for the Kondo insulator which is half‑filled). All energies are measured in units of V (set V=1 throughout the computation).

In the slave‑boson mean‑field, only the f^0, f^1 and f^2 configurations are kept. The boson amplitudes are e (f^0), p_\sigma (f^1 with spin \sigma), and a single parameter d for the f^2 configurations after imposing the simplification d_\sigma^2 = p_\sigma^2 d^2 and d_0^2 = p_\uparrow p_\downarrow d^2.

### Paramagnetic metal (finite U, zero field)
For the paramagnetic phase p_\uparrow = p_\downarrow = p. The equations that determine e, p, d, the chemical potential \mu and the Lagrange multiplier \lambda^{(2)} are:

1. Completeness constraint
   $$e^{2} + N p^{2}\bigl[2 + (2N-1) d^{2}\bigr] = 1$$

2. f‑occupation per spin‑orbital
   $$A = p^{2}\bigl[1 + (2N-1) d^{2}\bigr]$$

3. Hybridisation renormalisation
   $$Z = \frac{p\bigl(e + (2N-1) p d\bigr)}{\sqrt{A(1-A)}}$$

4. Chemical potential (flat band, n = 1.8)
   $$\mu = D\Bigl(\frac{n}{N} - 1 - 2A\Bigr)$$

5. Renormalised f‑level
   $$\tilde\varepsilon_f = \mu + \frac{Z^{2} V^{2}}{2 D A}$$

6. Hybridization amplitude
   $$C \equiv \langle f^\dagger_{im\sigma} c_{im\sigma}\rangle
      = -\frac{V Z}{2D}\,
        \ln\!\left(\frac{D+\tilde\varepsilon_f}{\tilde\varepsilon_f-\mu}\right)$$

7. Lagrange multiplier \lambda^{(2)}
   $$\lambda^{(2)} = V\Bigl(\frac{1}{p}\frac{\partial Z}{\partial p}
                    - \frac{d}{p^{2}}\frac{\partial Z}{\partial d}
                    - \frac{2N}{e}\frac{\partial Z}{\partial e}\Bigr) C$$

8. Consistency condition for U
   $$U = 2V\Bigl(\frac{N}{e}\frac{\partial Z}{\partial e}
                - \frac{1}{(2N-1) p^{2} d}\frac{\partial Z}{\partial d}\Bigr) C
         + 2\lambda^{(2)}$$

The derivatives of Z are:

$$
\begin{aligned}
\frac{\partial Z}{\partial e} &= \frac{p}{\sqrt{A(1-A)}},\\[4pt]
\frac{\partial Z}{\partial p} &=
   \frac{e + 2(2N-1) p d}{\sqrt{A(1-A)}}
   - \frac{p(e + (2N-1)p d)(1-2A)(1+(2N-1)d^{2})}{[A(1-A)]^{3/2}},\\[4pt]
\frac{\partial Z}{\partial d} &=
   \frac{(2N-1)p^{2}}{\sqrt{A(1-A)}}
   - \frac{p^{3}(e + (2N-1)p d)(1-2A)(2N-1)d}{[A(1-A)]^{3/2}} .
\end{aligned}
$$

Given \varepsilon_f and U, equations (1)–(8) must be solved for e, p, d.
Use the constraint (1) to express p^{2} in terms of e and d, then solve
for e and d such that the predicted U (8) equals the target U.
The converged solution yields the occupation probabilities
e^{2}, p^{2}, d^{2} and the total f‑electron number
n_f = 2 N A.

### Ferromagnetic metal and phase boundary (finite U, B=0)
Allow spin‑dependent p_\uparrow, p_\downarrow (still described by a single d).
The constraint becomes

$$
e^{2} + N\Bigl(1+\frac{N-1}{2}d^{2}\Bigr)(p_\uparrow^{2}+p_\downarrow^{2})
       + N^{2} p_\uparrow p_\downarrow d^{2} = 1 .
$$

For each spin,

$$
A_\sigma = p_\sigma^{2} + (N-1) p_\sigma^{2} d^{2} + N p_\sigma p_{-\sigma} d^{2},
\qquad
Z_\sigma = \frac{p_\sigma\bigl(e + (N-1) p_\sigma d\bigr)
           + N p_\sigma^{1/2} p_{-\sigma}^{3/2} d}{\sqrt{A_\sigma(1-A_\sigma)}} .
$$

The chemical potential is

$$
\mu = D\Bigl(\frac{n}{N} - 1 - (A_\uparrow+A_\downarrow)\Bigr),
\qquad
\tilde\varepsilon_{f\sigma} = \mu + \frac{Z_\sigma^{2} V^{2}}{2 D A_\sigma} .
$$

The hybridisation amplitudes are

$$
C_\sigma = -\frac{V Z_\sigma}{2D}
           \ln\!\left(\frac{D+\tilde\varepsilon_{f\sigma}}
                           {\tilde\varepsilon_{f\sigma}-\mu}\right).
$$

The self‑consistent equations for \lambda_\sigma^{(2)} and d are obtained from
the stationary conditions of the ground‑state energy (see paper Eqs. (3.10)).
They can be written as

$$
\begin{aligned}
\lambda_\sigma^{(2)} &=
   \frac{V\sum_{\sigma'}\bigl(2\frac{\partial Z_{\sigma'}}{\partial p_\sigma}
        - \frac{N}{e}\frac{\partial Z_{\sigma'}}{\partial e}
          \bigl[2p_\sigma + ((N-1)p_\sigma + N p_{-\sigma})d^{2}\bigr]\bigr) C_{\sigma'}
        + U\bigl[(N-1)p_\sigma + N p_{-\sigma}\bigr]d^{2}}
        {2p_\sigma\bigl[1+(N-1)d^{2}\bigr] + N p_{-\sigma} d^{2}},\\[8pt]
0 &=
   V\sum_{\sigma}\Bigl(\frac{\partial Z_\sigma}{\partial d}
        - \frac{N d}{e}\frac{\partial Z_\sigma}{\partial e}
          \Bigl(\frac{N-1}{2}(p_\uparrow^{2}+p_\downarrow^{2})
                + N p_\uparrow p_\downarrow\Bigr)\Bigr) C_\sigma
   + U d\Bigl(\frac{N-1}{2}(p_\uparrow^{2}+p_\downarrow^{2})
              + N p_\uparrow p_\downarrow\Bigr) \\
  &\qquad - d\sum_\sigma \lambda_\sigma^{(2)}
                \bigl[N p_{-\sigma} + (N-1) p_\sigma\bigr] .
\end{aligned}
$$

The last equation serves as a consistency condition that determines the
required d for given U; it replaces the simple U‑prediction used in the
paramagnetic case.

To find the phase boundary, scan U for each fixed \varepsilon_f and N.
For each U, first solve the paramagnetic equations. Then search for
a ferromagnetic solution with p_\uparrow \neq p_\downarrow. The ground‑state
energy must be compared: the energy of the hybridised bands is obtained by
summing over occupied single‑particle states,

$$
E_{\text{band}} = \frac{1}{2D}\sum_{\sigma}
   \int_{-D}^{D} d\epsilon\,
   \Bigl[ E_{-,\sigma}(\epsilon)\,\theta(\mu - E_{-,\sigma}(\epsilon))
         + E_{+,\sigma}(\epsilon)\,\theta(\mu - E_{+,\sigma}(\epsilon))\Bigr],
$$

with

$$
E_{\pm,\sigma}(\epsilon) = \frac12\Bigl(
   \tilde\varepsilon_{f\sigma} + \epsilon
   \pm \sqrt{(\tilde\varepsilon_{f\sigma} - \epsilon)^{2} + 4 Z_\sigma^{2} V^{2}}
   \Bigr).
$$

The boson contribution to the energy per site is evaluated from the
constant terms of the mean‑field Hamiltonian (3.7) using the
self‑consistent parameters. The total energy is
E_{\text{tot}} = E_{\text{band}} + E_{\text{boson}}.
The critical U_c is the smallest U for which a ferromagnetic solution
exists and has lower total energy than the paramagnetic solution.

### U → ∞ limit (metallic magnetization)
Only the f^0 and f^1 configurations survive; d=0 identically.
The unknowns are e, p_\uparrow, p_\downarrow. The constraint reduces to

$$
e^{2} + N(p_\uparrow^{2}+p_\downarrow^{2}) = 1 .
$$

The self‑consistency equations are

$$
\begin{aligned}
\frac{V^{2}}{2D}\bigl[1-N(p_\uparrow^{2}+p_\downarrow^{2})\bigr]
&\Bigl(\frac{1}{(1-p_\uparrow^{2})^{2}}\ln F_\uparrow
   - \frac{1}{(1-p_\downarrow^{2})^{2}}\ln F_\downarrow\Bigr)
   = \tilde\varepsilon_{f\downarrow} - \tilde\varepsilon_{f\uparrow} - 2B,\\[6pt]
\frac{V^{2}}{2D}\Bigl[
   \frac{2N-1+N(p_\downarrow^{2}-p_\uparrow^{2})}{(1-p_\uparrow^{2})^{2}}\ln F_\uparrow
  +\frac{2N-1+N(p_\uparrow^{2}-p_\downarrow^{2})}{(1-p_\downarrow^{2})^{2}}\ln F_\downarrow\Bigr]
  = \tilde\varepsilon_{f\downarrow} + \tilde\varepsilon_{f\uparrow} - 2\varepsilon_f ,
\end{aligned}
$$

where the factor F_\sigma and the effective \tilde\varepsilon_{f\sigma} depend on
the position of \mu relative to the hybridisation gaps:

- **Regime (i)** – \mu below the lower majority gap:
  $$F_\sigma = \frac{D+\tilde\varepsilon_{f\sigma}}{\tilde\varepsilon_{f\sigma}-\mu},\qquad
  \tilde\varepsilon_{f\sigma} = \mu
    + \frac{1-N(p_\uparrow^{2}+p_\downarrow^{2})}{p_\sigma^{2}(1-p_\sigma^{2})}
      \frac{V^{2}}{2D}.$$

- **Regime (ii)** – \mu inside the majority gap:
  $$F_\uparrow = \frac{1-p_\uparrow^{2}}{1-N(p_\uparrow^{2}+p_\downarrow^{2})}
                \frac{D^{2}-\tilde\varepsilon_{f\uparrow}^{2}}{V^{2}},\quad
  \tilde\varepsilon_{f\uparrow} = D(1-2 p_\uparrow^{2}).$$

- **Regime (iii)** – \mu above the majority gap:
  $$F_\uparrow = \frac{D-\tilde\varepsilon_{f\uparrow}}{\mu-\tilde\varepsilon_{f\uparrow}},\quad
  \tilde\varepsilon_{f\uparrow} = \mu
    - \frac{1-N(p_\uparrow^{2}+p_\downarrow^{2})}{(1-p_\uparrow^{2})^{2}}
      \frac{V^{2}}{2D}.$$

For the minority band one always uses regime (i). The chemical potential is
\mu = D\bigl(n/N - 1 - p_\uparrow^{2} - p_\downarrow^{2}\bigr).
Solve the above equations to obtain p_\uparrow, p_\downarrow and compute the
magnetisation m = p_\uparrow^{2} - p_\downarrow^{2}.

### Kondo insulator (N = 2, electron‑hole symmetry)
The f level is \varepsilon_f = -3U/2, ensuring electron‑hole symmetry.
The slave‑boson amplitudes are e (for f^0 and f^4), p (f^1 and f^3), d (f^2).
The self‑consistency equations are

$$
\begin{aligned}
e^{2} + 4p^{2} + 3d^{2} &= \tfrac12,\\[2pt]
Z &= 4p(e+3d),\"[2pt]
C &= -\frac{V Z}{D}\ln\Bigl(\frac{D}{Z V}\Bigr),\"[2pt]
\lambda^{(1)} &= -3U - 2V\frac{C}{e}\frac{\partial Z}{\partial e},\\[2pt]
\lambda^{(2)} &= \tfrac12\bigl( -3U - 2V\frac{C}{p}\frac{\partial Z}{\partial p}
                     - \lambda^{(1)} \bigr),\"[2pt]
\bigl\langle f^\dagger c \bigr\rangle &= C,\\[2pt]
\bigl\langle f^\dagger f \bigr\rangle &= \tfrac12,\qquad
E_{\text{gap}} = 2\frac{Z^{2} V^{2}}{D}.
\end{aligned}
$$

These can be reduced to the two equations

$$
\begin{aligned}
p^{2} &= \tfrac18\bigl(1 - 6d^{2} - 2e^{2}\bigr),\\
4d\bigl(1 - 6d^{2} - 4e^{2} - 6ed\bigr)
      &= 3(d-e)\bigl(1 - 6d^{2} - 2e^{2}\bigr),\\
\frac{(d-e)(e+3d)(1-6d^{2}-2e^{2})}{e d}\,
   \ln\!\Bigl[\frac{D^{2}}{2(e+3d)^{2}(1-6d^{2}-e^{2})V^{2}}\Bigr]
   &= \frac{U D}{V^{2}} .
\end{aligned}
$$

Solve the last equation together with the first two to obtain e, p, d for a
given U/V, then compute e^{2}, p^{2}, d^{2} and the gap E_{\text{gap}}/V.

### Solving strategy
- Use numerical root‑finding (e.g. SciPy’s `fsolve` or `root`) for the
  coupled non‑linear equations.
- For the metallic paramagnet and ferromagnet, start from an initial guess
  (e.g. e=0.5, p=0.5, d=0.1) and iterate.
- For the phase boundary, perform a bisection in U: at each trial U,
  solve the paramagnetic equations and attempt to find a ferromagnetic
  solution; U_c is the transition point.
- All integrals over \epsilon can be evaluated analytically for the
  flat band (the indefinite integrals are elementary).

## Required parameter grids

The following independent parameter combinations must be evaluated.
Produce exactly one entry for each combination.

### metallic_phase_boundary
- N ∈ {1, 3, 5}
- For each N, \varepsilon_f / V ∈ {-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0}
- Output U_c / V (the critical Coulomb repulsion above which the
  paramagnetic state is the ground state).

### metallic_magnetization
- N = 1
- \varepsilon_f / V ∈ {5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0}
- For each \varepsilon_f / V, B / V ∈ {0.0, 0.02, 0.05, 0.1}
- Output magnetization m = p_\uparrow^{2} - p_\downarrow^{2}.

### metallic_occupations
- N ∈ {1, 3, 5}
- \varepsilon_f / V ∈ {-2.0, -1.0, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0}
- Fixed U / V = 1.0
- Output e^{2}, p^{2}, d^{2} and total f‑electron number n_f.

### kondo_insulator
- N = 2
- U / V ∈ {0.0, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0}
- Output e^{2}, p^{2}, d^{2} and E_{\text{gap}} / V.

## Reproduction target
Compute the following four sets of quantities from the slave-boson mean-field theory described above:

1. **Metallic ferromagnetic phase boundary** – For orbital degeneracies N = 1, 3, 5, determine the critical Coulomb repulsion U_c / V as a function of f-level position ε_f / V (in zero magnetic field) below which the paramagnetic state is unstable toward ferromagnetism.

2. **Metallic magnetization (U → ∞ limit)** – For N = 1, compute the magnetization m as a function of ε_f / V at several values of the external magnetic field B / V, showing the spontaneous magnetization and the effect of the field.

3. **Metallic occupation probabilities** – For the paramagnetic state at fixed U = V and zero field, compute the probabilities e² (f⁰), p² (f¹), d² (f²), and the total f-electron number n_f as a function of ε_f / V for N = 1, 3, 5.

4. **Kondo insulator (N = 2)** – For the electron-hole symmetric Kondo insulator, compute the occupation probabilities e², p², d² and the energy gap E_gap / V as a function of U / V.

All results must be written to `/app/outputs/all_results.json` following the output contract below. The parameters D = 10 V and n = 1.8 electrons per site are fixed throughout, except for the insulator case which is half-filled.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve slave-boson mean-field equations and produce aggregate results
- Role: scored (load-bearing)
- Action: Implement the self-consistency equations for the Anderson lattice slave-boson mean-field model with orbital degeneracy N, finite U, and flat conduction-band density of states (bandwidth 2D, D=10V). Compute occupation probabilities of f-electron configurations, total f-electron number, magnetization, and Kondo insulator energy gap for the metallic paramagnetic, ferromagnetic, and symmetric Kondo insulator cases. Solve for N=1,3,5 at specified parameter points (epsilon_f, U) and for the N=2 electron-hole symmetric insulator. Output all numerical results as a single structured JSON file.
- Output file: `/app/outputs/all_results.json`
- Format: json
- Contract: JSON object with top-level keys: 'metallic_phase_boundary' (array of objects with keys N, epsilon_f_over_V, U_c_over_V), 'metallic_magnetization' (array of objects with keys N, epsilon_f_over_V, B_over_V, magnetization), 'metallic_occupations' (array of objects with keys N, epsilon_f_over_V, e2, p2, d2, n_f), 'kondo_insulator' (array of objects with keys U_over_V, e2, p2, d2, gap_over_V)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/all_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### all_results.json
- path: `/app/outputs/all_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Numerically computed quantities from the slave-boson mean-field theory, covering metallic phase boundary, magnetization, occupation probabilities, and Kondo insulator gap. The checker will compare each field's values to the paper-reported numbers with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `metallic_phase_boundary`, `metallic_magnetization`, `metallic_occupations`, `kondo_insulator`
  - `metallic_phase_boundary`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `N`, `epsilon_f_over_V`, `U_c_over_V`
      - `properties`:
        - `N`:
          - `type`: integer
        - `epsilon_f_over_V`:
          - `type`: number
        - `U_c_over_V`:
          - `type`: number
  - `metallic_magnetization`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `N`, `epsilon_f_over_V`, `B_over_V`, `magnetization`
      - `properties`:
        - `N`:
          - `type`: integer
        - `epsilon_f_over_V`:
          - `type`: number
        - `B_over_V`:
          - `type`: number
        - `magnetization`:
          - `type`: number
  - `metallic_occupations`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `N`, `epsilon_f_over_V`, `e2`, `p2`, `d2`, `n_f`
      - `properties`:
        - `N`:
          - `type`: integer
        - `epsilon_f_over_V`:
          - `type`: number
        - `e2`:
          - `type`: number
        - `p2`:
          - `type`: number
        - `d2`:
          - `type`: number
        - `n_f`:
          - `type`: number
  - `kondo_insulator`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `U_over_V`, `e2`, `p2`, `d2`, `gap_over_V`
      - `properties`:
        - `U_over_V`:
          - `type`: number
        - `e2`:
          - `type`: number
        - `p2`:
          - `type`: number
        - `d2`:
          - `type`: number
        - `gap_over_V`:
          - `type`: number

Notes: The task is purely computational; all parameters and equations are given in the method description. The agent must implement the mean-field equations and solve them over the specified parameter ranges.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "all_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "metallic_phase_boundary",
          "metallic_magnetization",
          "metallic_occupations",
          "kondo_insulator"
        ],
        "metallic_phase_boundary": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "N",
              "epsilon_f_over_V",
              "U_c_over_V"
            ],
            "properties": {
              "N": {
                "type": "integer"
              },
              "epsilon_f_over_V": {
                "type": "number"
              },
              "U_c_over_V": {
                "type": "number"
              }
            }
          }
        },
        "metallic_magnetization": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "N",
              "epsilon_f_over_V",
              "B_over_V",
              "magnetization"
            ],
            "properties": {
              "N": {
                "type": "integer"
              },
              "epsilon_f_over_V": {
                "type": "number"
              },
              "B_over_V": {
                "type": "number"
              },
              "magnetization": {
                "type": "number"
              }
            }
          }
        },
        "metallic_occupations": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "N",
              "epsilon_f_over_V",
              "e2",
              "p2",
              "d2",
              "n_f"
            ],
            "properties": {
              "N": {
                "type": "integer"
              },
              "epsilon_f_over_V": {
                "type": "number"
              },
              "e2": {
                "type": "number"
              },
              "p2": {
                "type": "number"
              },
              "d2": {
                "type": "number"
              },
              "n_f": {
                "type": "number"
              }
            }
          }
        },
        "kondo_insulator": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "U_over_V",
              "e2",
              "p2",
              "d2",
              "gap_over_V"
            ],
            "properties": {
              "U_over_V": {
                "type": "number"
              },
              "e2": {
                "type": "number"
              },
              "p2": {
                "type": "number"
              },
              "d2": {
                "type": "number"
              },
              "gap_over_V": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Numerically computed quantities from the slave-boson mean-field theory, covering metallic phase boundary, magnetization, occupation probabilities, and Kondo insulator gap. The checker will compare each field's values to the paper-reported numbers with appropriate tolerances."
    }
  ],
  "notes": "The task is purely computational; all parameters and equations are given in the method description. The agent must implement the mean-field equations and solve them over the specified parameter ranges."
}
```

## How you are scored
A hidden verifier will load your `/app/outputs/all_results.json` and compare the computed values in each of the four top-level keys against the expected results derived from the paper’s reported data. Each field (e.g., phase boundary critical U, magnetization, occupation probabilities, energy gap) is checked independently with appropriate tolerances. The reward is monotonic: a more accurate match to the reference yields a higher score, and a result that matches or beats the reference performance threshold earns full credit. Purely structural checks (e.g., presence of required keys, correct array shapes, trends such as magnetization increasing with decreasing ε_f or gap decreasing with U) also contribute to the score but carry lower weight than the numerical comparisons. The verifier does not depend on any external resources and runs entirely within the evaluation sandbox.
