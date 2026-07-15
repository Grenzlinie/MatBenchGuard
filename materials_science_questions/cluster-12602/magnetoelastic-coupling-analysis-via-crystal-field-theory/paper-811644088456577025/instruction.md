# Mean-field p-T and p-H phase diagram under competing dipole and hexadecapole orders

## Problem background
URu2Si2 exhibits a phase transition at 17.5 K into a mysterious "hidden order" phase whose order parameter has remained unidentified for decades. One compelling theoretical proposal is an antiferro ordering of an electric hexadecapole moment of $xy(x^2-y^2)$ symmetry, described by a localized $f$-electron mean-field model with two competing staggered order parameters: a magnetic dipole ($\sigma$) and the hexadecapole ($\xi$). This model can give rise to a pressure–temperature ($p$–$T$) phase diagram featuring a tricritical point and a first-order boundary between a low-pressure antiferro-hexadecapole (AFH) phase and a high-pressure antiferromagnetic (AFM) phase. In this task, we aim to re-derive the key critical pressures of this mean-field model to test its viability as a description of the hidden order.

## Approach
Implement the low-lying crystalline electric field (CEF) model for $J=4$ multiplet under tetragonal symmetry, restricted to three singlets: $\Gamma_1^{(1)}$ (energy $E_1^{(1)} = 0$ K), $\Gamma_2$ ($E_2 = 50$ K), and $\Gamma_1^{(2)}$ ($E_1^{(2)} = 170$ K). The mixing angle of the CEF wavefunctions is $\theta = 0.998$. Construct the reduced dipole operator $\sigma$ (proportional to $J_z$) and the hexadecapole operator $\xi$ (proportional to $H_z^\alpha$) as $3\times3$ matrices in this basis, following the explicit forms from the literature.

The mean-field Hamiltonian on a bipartite lattice (coordination number $z=8$) is
$H = \frac{J}{z} \sum_{\langle i,j\rangle} \sigma_i \sigma_j + \frac{D}{z} \sum_{\langle i,j\rangle} \xi_i \xi_j + \sum_i H_i^{\mathrm{CEF}}$,
plus a possible Zeeman term for the $p$–$H$ sweep (applied along the $c$-axis). The exchange couplings are assumed to depend linearly on pressure around an unknown tricritical pressure $p_c$:
$J(p) = J_c + \alpha(p - p_c)$, $D(p) = D_c + \beta(p - p_c)$,
with $J_c = 40.6$ K, $D_c = 91.4$ K, $\alpha = 1.27$ K/GPa, $\beta = 1.0$ K/GPa.

For a given temperature and pressure, solve the self-consistency equations for the staggered order parameters $\sigma(Q)$ and $\xi(Q)$ (the $A$–$B$ sublattice amplitudes) by iterating to convergence. For each solution (AFH, AFM, paramagnetic), compute the free energy to determine the stable phase. Perform this over a grid of pressure and temperature, and also at $T=0$ for the pressure–magnetic field sweep. From the phase diagrams, extract:
- the tricritical pressure $p_c$, where the paramagnetic-to-ordered transition changes from second- to first-order;
- the zero-temperature AFH–AFM transition pressure $p_{\mathrm{trans}}$, where the two ordered phases have equal free energy;
- confirm whether the AFH–AFM boundary is first-order.
Optionally, report the ambient-pressure hidden-order transition temperature $T_{\mathrm{HO}}$.

## Reproduction target
Produce a single JSON file containing the computed tricritical pressure (in GPa), the zero-temperature AFH–AFM transition pressure (in GPa), a boolean indicating whether the AFH–AFM phase boundary is first-order, and optionally the ambient-pressure hidden-order transition temperature (in K). The target is to implement the mean-field model correctly and obtain these quantities from the numerical solution of the self-consistency equations; there is no external data to match.

## Assets
No external datasets, models, or specialized software are required. The computation can be carried out in any programming language using standard numerical libraries (e.g., Python with NumPy and SciPy).

## Workflow steps

### Step 1: Mean-field phase diagram computation
- Role: scored (load-bearing)
- Action: Build the three-singlet CEF model with energies E1(1)=0 K, E2=50 K, E1(2)=170 K and mixing angle θ=0.998. Construct the reduced dipole σ and hexadecapole ξ matrices. Implement the mean-field Hamiltonian with nearest-neighbor exchange couplings J(p) and D(p) that depend linearly on pressure: J(p)=Jc + α(p - pc), D(p)=Dc + β(p - pc) using Jc=40.6 K, Dc=91.4 K, α=1.27 K/GPa, β=1.0 K/GPa, and coordination number z=8. Solve the mean-field self-consistency equations for staggered order parameters σ(Q) and ξ(Q) over a pressure-temperature grid (and at T=0 for the p-H sweep). Compare free energies of AFH, AFM, and paramagnetic solutions to determine phase stability. Identify the tricritical pressure pc (separating low-p AFH and high-p AFM phases), the zero-temperature AFH–AFM transition pressure, confirm the first-order nature of the AFH–AFM boundary, and optionally extract the ambient-pressure hidden-order transition temperature. Output the results to a JSON file.
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
