# Mean-field p-T and p-H phase diagram under competing dipole and hexadecapole orders

## Problem background
URu2Si2 exhibits a phase transition at 17.5 K into a mysterious "hidden order" phase whose order parameter has remained unidentified for decades. One compelling theoretical proposal is an antiferro ordering of an electric hexadecapole moment of $xy(x^2-y^2)$ symmetry, described by a localized $f$-electron mean-field model with two competing staggered order parameters: a magnetic dipole ($\sigma$) and the hexadecapole ($\xi$). This model can give rise to a pressure–temperature ($p$–$T$) phase diagram featuring a tricritical point and a first-order boundary between a low-pressure antiferro-hexadecapole (AFH) phase and a high-pressure antiferromagnetic (AFM) phase. In this task, we aim to re-derive the key critical pressures of this mean-field model to test its viability as a description of the hidden order.

## Approach
Implement the low-lying crystalline electric field (CEF) model for $J=4$ multiplet under tetragonal symmetry, restricted to three singlets: $\Gamma_1^{(1)}$ (energy $E_1^{(1)} = 0$ K), $\Gamma_2$ ($E_2 = 50$ K), and $\Gamma_1^{(2)}$ ($E_1^{(2)} = 170$ K). The CEF wavefunctions are given by:

$$
\begin{aligned}
|\Gamma_1^{(1)}\rangle &= \frac{1}{\sqrt{2}}\sin\theta\,(|+4\rangle+|-4\rangle) + \cos\theta\,|0\rangle,\\
|\Gamma_2\rangle &= \frac{1}{\sqrt{2}}(|+4\rangle-|-4\rangle),\\
|\Gamma_1^{(2)}\rangle &= \frac{1}{\sqrt{2}}\cos\theta\,(|+4\rangle+|-4\rangle) - \sin\theta\,|0\rangle,
\end{aligned}
$$

with the mixing angle $\theta = 0.998$ rad.

The relevant operators in the $|J=4, m\rangle$ basis are defined as follows.

**Reduced dipole operator $\sigma$** (proportional to $J_z$):
$$
\sigma = J_z, \qquad \langle m'|\sigma|m\rangle = m\,\delta_{m',m}, \quad m=-4,-3,\dots,4.
$$

**Hexadecapole operator $\xi$** (proportional to $H_z^\alpha$):
In the $J=4$ subspace the hexadecapole operator of $xy(x^2-y^2)$ symmetry is realized by the symmetrized fourth‑order ladder combination
$$
\xi = \frac{1}{2}\left(J_+^4 + J_-^4\right),
$$
where the ladder operators act as
$$
\langle m\pm1|J_\pm|m\rangle = \sqrt{20 - m(m\pm1)}.
$$
Using these definitions, compute the $3\times3$ matrix representations of $\sigma$ and $\xi$ in the orthonormal basis ordered as $\{|\Gamma_1^{(1)}\rangle, |\Gamma_2\rangle, |\Gamma_1^{(2)}\rangle\}$. All matrix elements are real and symmetric.

The mean-field Hamiltonian on a bipartite lattice (coordination number $z=8$) is
$$
H = \frac{J}{z} \sum_{\langle i,j\rangle} \sigma_i \sigma_j + \frac{D}{z} \sum_{\langle i,j\rangle} \xi_i \xi_j + \sum_i H_i^{\mathrm{CEF}},
$$
plus a possible Zeeman term for the $p$–$H$ sweep (applied along the $c$-axis). The exchange couplings are assumed to depend linearly on pressure around an unknown tricritical pressure $p_c$:
$$
J(p) = J_c + \alpha(p - p_c), \qquad D(p) = D_c + \beta(p - p_c),
$$
with $J_c = 40.6$ K, $D_c = 91.4$ K, $\alpha = 1.27$ K/GPa, $\beta = 1.0$ K/GPa.

Because the coupling parameters themselves depend on the unknown $p_c$, the problem must be solved **self‑consistently**:
1. Start with an initial guess for $p_c$ (e.g. $1.5$ GPa).
2. For this guess, construct $J(p)$ and $D(p)$ for a grid of pressure $p$ and temperature $T$.
3. Solve the mean‑field self‑consistency equations for the staggered order parameters $\sigma(Q)$ and $\xi(Q)$ (the $A$–$B$ sublattice amplitudes) by iterating to convergence.
4. Compare free energies of the AFH, AFM and paramagnetic solutions to determine the stable phase at each $(p,T)$.
5. From the computed phase diagram, identify the **tricritical point** – the pressure at which the paramagnetic‑to‑ordered transition changes from second‑order to first‑order (the termination of the continuous transition line). Denote this pressure $p^*$.
6. Update $p_c = p^*$ and repeat steps 2–5 until convergence, e.g. $|p_c^{\mathrm{new}} - p_c^{\mathrm{old}}| < 10^{-3}$ GPa.

The converged value of $p_c$ is the self‑consistent tricritical pressure. From the final phase diagram also extract:
- the zero‑temperature AFH–AFM transition pressure $p_{\mathrm{trans}}$ (where the free energies of the AFH and AFM phases are equal at $T=0$);
- confirm whether the AFH–AFM boundary is first‑order;
- optionally, the ambient‑pressure hidden‑order transition temperature $T_{\mathrm{HO}}$ (the paramagnetic‑to‑AFH transition at $p=0$).

Note: The $p$–$H$ sweep is not required for scoring; if you implement it, a Zeeman term $-g\mu_B B J_z$ can be added, but it does not affect the scored outputs.

## Reproduction target
Produce a single JSON file containing the computed tricritical pressure (in GPa), the zero-temperature AFH–AFM transition pressure (in GPa), a boolean indicating whether the AFH–AFM phase boundary is first-order, and optionally the ambient-pressure hidden-order transition temperature (in K). The target is to implement the mean-field model correctly and obtain these quantities from the numerical solution of the self-consistency equations; there is no external data to match.

## Assets
No external datasets, models, or specialized software are required. The computation can be carried out in any programming language using standard numerical libraries (e.g., Python with NumPy and SciPy).

## Workflow steps

### Step 1: Mean-field phase diagram computation
- Role: scored (load-bearing)
- Action: Build the three-singlet CEF model as described in the Approach section. Construct the $3\times3$ matrices of $\sigma$ and $\xi$ using the provided wavefunctions and operator definitions. Implement the mean-field Hamiltonian with nearest-neighbor exchange couplings $J(p)$ and $D(p)$ that depend linearly on pressure, with the unknown tricritical pressure $p_c$ treated self‑consistently (see iteration scheme in Approach). Solve the mean-field self-consistency equations for staggered order parameters over a pressure‑temperature grid (and at $T=0$ for the $p$–$H$ sweep if desired). Compare free energies to determine phase stability. Extract the self‑consistent tricritical pressure $p_c$, the zero‑temperature AFH–AFM transition pressure, confirm the first‑order nature of the AFH–AFM boundary, and optionally the ambient‑pressure hidden‑order transition temperature. Output the results to a JSON file.
- Output file: `/app/outputs/phase_diagram_results.json`
- Format: json
- Contract: {"tricritical_pressure_GPa": number, "zero_T_AFH_AFM_transition_pressure_GPa": number, "phase_boundary_first_order": boolean, "ambient_pressure_T_HO_K": number (optional)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_results.json
- path: `/app/outputs/phase_diagram_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The key critical pressures and the first-order character of the AFH–AFM boundary computed from the mean-field model.
- schema:
  - `type`: object
  - `required`: `tricritical_pressure_GPa`, `zero_T_AFH_AFM_transition_pressure_GPa`, `phase_boundary_first_order`
  - `properties`:
    - `tricritical_pressure_GPa`:
      - `type`: number
      - `unit`: GPa
    - `zero_T_AFH_AFM_transition_pressure_GPa`:
      - `type`: number
      - `unit`: GPa
    - `phase_boundary_first_order`:
      - `type`: boolean
    - `ambient_pressure_T_HO_K`:
      - `type`: number
      - `unit`: K
      - `optional`: True

Notes: The scored quantities are the tricritical pressure and the zero-temperature AFH–AFM transition pressure. The boundary must be declared first-order (true). The ambient-pressure hidden-order temperature is optional for scoring. The hidden checker compares against reference values derived from the model parameters using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "tricritical_pressure_GPa",
          "zero_T_AFH_AFM_transition_pressure_GPa",
          "phase_boundary_first_order"
        ],
        "properties": {
          "tricritical_pressure_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "zero_T_AFH_AFM_transition_pressure_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "phase_boundary_first_order": {
            "type": "boolean"
          },
          "ambient_pressure_T_HO_K": {
            "type": "number",
            "unit": "K",
            "optional": true
          }
        }
      },
      "description": "The key critical pressures and the first-order character of the AFH–AFM boundary computed from the mean-field model."
    }
  ],
  "notes": "The scored quantities are the tricritical pressure and the zero-temperature AFH–AFM transition pressure. The boundary must be declared first-order (true). The ambient-pressure hidden-order temperature is optional for scoring. The hidden checker compares against reference values derived from the model parameters using appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your `phase_diagram_results.json` and compares your reported tricritical pressure and zero‑T AFH–AFM transition pressure to reference values derived from the model's parameters, using appropriate tolerances. It also checks the consistency of the `phase_boundary_first_order` flag. The final reward is computed from these comparisons; simply reporting the correct numbers is not sufficient to pass the scoring logic, but a correct implementation will produce values close to the reference.