# Kagome Heisenberg Antiferromagnet Phase Diagram via Nematic Bond Theory

## Problem background
The classical Heisenberg antiferromagnet on the kagome lattice is a canonical frustrated magnet. Owing to its corner‑sharing triangle geometry, the ground‑state manifold is extensively degenerate, supporting a highly correlated, fluctuating spin‑liquid regime over a broad temperature range. A central, long‑standing question is whether this spin‑liquid persists all the way to zero temperature or terminates in a thermodynamic phase transition that selects a long‑range ordered state. In addition, if an ordered phase does emerge, it is important to know whether the ordered moment saturates at low temperature or remains suppressed by domain walls and other topological defects.

The purpose of this task is to resolve these questions for the nearest‑neighbor kagome antiferromagnet, and to map the nearby phase diagram when second‑neighbor couplings are added, by computing free energies and order parameters from a well‑defined analytical framework. For comparison, the same framework will be applied to the pyrochlore antiferromagnet to test whether that three‑dimensional spin liquid orders.

## Approach
The analysis is performed using Nematic Bond Theory (NBT), a self‑consistent approach based on a large‑N_s expansion, where N_s = 3 is the number of spin components. NBT extends the usual self‑consistent Gaussian approximation by including momentum‑dependent self‑energies that suppress spatial fluctuations of the local spin length. The method represents the unit‑length spin constraint with a fluctuating constraint field; its uniform component Δ is treated self‑consistently, while non‑uniform components are incorporated diagrammatically. This yields dressed spin and constraint propagators linked by self‑consistent Dyson equations.

Explicitly, treat the kagome lattice as a triangular Bravais lattice with a 3‑site unit cell. The exchange matrix in reciprocal space for sublattice indices i,j is

$$
2 J_{\mathbf{q},ij} = 
\begin{pmatrix}
0 & J_1(1+e^{-i q_1})+J_2(e^{i q_2}+e^{i q_3}) & J_1(1+e^{i q_3})+J_2(e^{-i q_1}+e^{-i q_2}) \\
J_1(1+e^{i q_1})+J_2(e^{-i q_2}+e^{-i q_3}) & 0 & J_1(1+e^{-i q_2})+J_2(e^{i q_3}+e^{i q_1}) \\
J_1(1+e^{-i q_3})+J_2(e^{i q_1}+e^{i q_2}) & J_1(1+e^{i q_2})+J_2(e^{-i q_3}+e^{-i q_1}) & 0
\end{pmatrix}
$$

where \(q_i = \mathbf{q}\cdot\mathbf{a}_i\) and \(\mathbf{a}_1=(1,0),\mathbf{a}_2=(-1/2,\sqrt{3}/2),\mathbf{a}_3=-\mathbf{a}_1-\mathbf{a}_2\). To ensure positivity subtract the minimum eigenvalue of \(J_{\mathbf{q}}\) from the diagonal.

The renormalized spin propagator \(K_{\mathbf{q}}\) and the constraint‑field propagator \(D_{\mathbf{q}}\) are 3×3 matrices satisfying:

$$
K_{\mathbf{q},ij} = J_{\mathbf{q},ij} + \Delta_i \delta_{ij} + \Sigma_{\mathbf{q},ij} \qquad (1)
$$
$$
D_{\mathbf{q},ij}^{-1} = \frac{N_s}{2} \sum_{\mathbf{p}} K_{\mathbf{q}+\mathbf{p},ij}^{-1} K_{\mathbf{p},ji}^{-1} \qquad (2)
$$
$$
\Sigma_{\mathbf{q},ij} = \sum_{\mathbf{p} \neq 0} K_{\mathbf{q}-\mathbf{p},ij}^{-1} D_{\mathbf{p},ij} \qquad (3)
$$

where \(\Delta_i\) is the uniform constraint field on sublattice i, and \(\Sigma\) is the momentum‑dependent self‑energy. The inverse temperature follows from the saddle‑point condition enforcing unit spin length on each sublattice:

$$
\beta = \frac{N_s}{2 N_c} \sum_{\mathbf{q}} K_{\mathbf{q},ii}^{-1} \quad \text{for } i=1,2,3 \qquad (4)
$$

with \(N_c\) the number of unit cells (\(N=3N_c\)). For a fixed set of Δ values, equations (1)–(3) are iterated starting from an initial guess for Σ (often random for the spin‑liquid branch, or biased). After convergence (when three consecutive temperature values differ by <10⁻¹³), the free energy per spin is computed from

$$
f = -\frac{N_s T}{2 N} \sum_{\mathbf{q}} \ln\det(\pi T K_{\mathbf{q}}^{-1}) 
+ \frac{T}{2 N} \sum_{\mathbf{q}} \ln\det\!\Big(\frac{\pi T^2}{2 N_c} D_{\mathbf{q}}^{-1}\Big)
- \frac{N_c}{N} \sum_i \Delta_i 
- \frac{N_s T}{2 N} \operatorname{tr}\big(K_{\mathbf{q}}^{-1} \Sigma_{\mathbf{q}}\big) \qquad (5)
$$

with T obtained from (4). By varying Δ, free‑energy branches for different thermodynamic states are traced. Different initialisations of Σ can converge to different branches, corresponding to competing states: a disordered spin liquid (random initial Σ), a coplanar √3×√3 ordered state (biased initial Σ, e.g. from a low‑T solution of the model with a small ferromagnetic J₂), a coplanar q=0 state, and the cuboc1 state. For each converged branch the free energy per spin and spin correlations are recorded. The stable phase at a given temperature is the one with the lowest free energy.

The spin correlation \(\langle \mathbf{S}_{-\mathbf{q},i} \cdot \mathbf{S}_{\mathbf{q},j}\rangle = N_s T (K_{-\mathbf{q},ij}^{-1} + K_{\mathbf{q},ji}^{-1})/4\) allows calculation of the ordered moment squared at the √3×√3 wavevector \(\mathbf{Q}=(4\pi/3,0)\):

$$
m_{\mathrm{AF}}^2 = \frac{6}{N^2} \sum_{l,\mathbf{R},\mathbf{R}'} \langle \mathbf{S}_{\mathbf{R},l} \cdot \mathbf{S}_{\mathbf{R}',l} \rangle e^{i \mathbf{Q}\cdot(\mathbf{R}-\mathbf{R}')}
$$
where the real‑space correlation is obtained by Fourier back‑transform. The specific heat \(c_v\) is extracted from the derivative of the free energy with respect to temperature.

The workflow first implements the NBT self‑consistency loop for the nearest‑neighbour kagome model (J₁=1, J₂=0) and computes free energies for the spin liquid and √3×√3 branches. It then extends the implementation to include a second‑neighbour coupling J₂, probing selected values that define the phase boundaries and a fine grid near the triple point. Finally, the same machinery is applied to the nearest‑neighbour pyrochlore antiferromagnet, comparing the spin liquid free energy with that of Néel and SLP‑X ordered states (using the pyrochlore lattice vectors and exchange matrix).

## Reproduction target
Implement the full NBT pipeline for both the kagome and pyrochlore Heisenberg antiferromagnets and extract the following quantitative results, all reported in units of J₁:

1. For the nearest‑neighbour kagome model (J₂=0):
   - The first‑order transition temperature T_c where the spin‑liquid and √3×√3 free energies cross.
   - The latent heat per spin ℓ_h, computed from the slope discontinuity at T_c.
   - The squared ordered moment m²_AF at the √3×√3 wavevector, evaluated at the lowest temperature reached.

2. For two critical second‑neighbour couplings: one on the ferromagnetic side (J₂ = -2.139×10⁻³) and one on the antiferromagnetic side (J₂ = 1.239×10⁻²). For each:
   - The transition temperature T_c and latent heat ℓ_h from the spin liquid to the relevant ordered branch.

3. A fine scan of J₂ values near zero to locate the triple point where the spin liquid, √3×√3, and q=0 phases coexist. Report the (J₂, T_c) coordinates of the triple point.

4. The zero‑temperature specific heat c_v of the √3×√3 phase, extrapolated from low‑temperature data.

5. For the pyrochlore antiferromagnet, determine whether any ordered branch (Néel or SLP‑X) has a lower free energy than the spin liquid down to at least T = 10⁻⁹ J₁. Report a boolean flag, the free‑energy difference per spin at the lowest temperature, and that temperature.

All results are to be collected into a single JSON file at /app/outputs/results.json according to the schema specified in the output contract. Ensure that the numerical values extracted from the free‑energy curves correspond to the thermodynamically stable (lowest‑free‑energy) branches.

## Assets
There are no external datasets, pre‑trained models, or specialised tools required beyond standard open‑source scientific computing packages for Python (e.g., numpy, scipy). Everything needed is obtained from the method description in the approach section. No additional retrievable resources are listed because the task is self‑contained once those libraries are installed.

## Workflow steps

### Step 1: Implement NBT and compute free energies for nearest-neighbor kagome model
- Role: process
- Action: Implement the Nematic Bond Theory (NBT) self-consistent equations for the kagome Heisenberg antiferromagnet with nearest-neighbor coupling J₁=1. Solve iteratively for large system sizes (L≥30) starting from random initial self-energies (spin liquid branch) and from a biased initial self-energy (√3×√3 branch). Obtain converged free energy per spin as a function of temperature for both branches, and record spin correlation data needed to compute the ordered moment.
- Evidence: `/app/outputs/kagome_J2_0_free_energy.json`

### Step 2: Run NBT for J₁‑J₂ kagome model at critical J₂ values and around triple point
- Role: process
- Action: Extend the NBT implementation to include second-neighbor coupling J₂ (using the exchange matrix from the paper's method). Run simulations for J₂ = -2.139×10⁻³, J₂ = 1.239×10⁻², and a fine grid of J₂ values in [-2×10⁻⁴, 2×10⁻⁴] to resolve the triple point. For each J₂, converge the spin liquid, √3×√3, and q=0 branches and record free energy vs temperature.
- Evidence: `/app/outputs/kagome_J2_scan_free_energy.json`

### Step 3: Run NBT for pyrochlore Heisenberg antiferromagnet
- Role: process
- Action: Implement NBT for the pyrochlore lattice with nearest-neighbor antiferromagnetic coupling J₁=1. Run simulations for the spin liquid, Néel, and SLP-X states. Record free energy vs temperature down to at least T=10⁻⁹ J₁ and compute specific heat.
- Evidence: `/app/outputs/pyrochlore_results.json`

### Step 4: Extract key quantitative results and write scored output
- Role: scored (load-bearing)
- Action: From the free energy curves and correlation data produced in steps 01–03, extract the following quantities and write them to results.json:
- J₂=0: transition temperature Tc (from free energy crossing of spin liquid and √3×√3 branches), latent heat per spin, ordered moment squared m_AF² at the lowest temperature computed.
- J₂=-2.139×10⁻³ and J₂=1.239×10⁻²: transition temperature Tc and latent heat.
- Triple point: J₂ and Tc coordinates (where free energies of spin liquid, √3×√3, and q=0 branches are equal).
- Zero-temperature specific heat c_v of the √3×√3 phase.
- Pyrochlore: whether any ordered state has lower free energy (boolean), free energy difference per spin at the lowest temperature, and lowest temperature.
All values in units of J₁; Tc and latent heat to 5 significant digits.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON object with fields: J2_0 (object with Tc, latent_heat, mAF2_lowest_T), J2_critical_sqrt3 (object with Tc, latent_heat), J2_critical_q0 (object with Tc, latent_heat), triple_point (object with J2, Tc), cv_sqrt3_T0 (float), pyrochlore (object: ordered_state_found (bool), free_energy_diff (float), lowest_T (float)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: A single JSON file containing the paper's headline quantitative results: transition parameters, ordered moment, triple point, specific heat, and pyrochlore verification.
- schema:
  - `type`: object
  - `required`: `J2_0`, `J2_critical_sqrt3`, `J2_critical_q0`, `triple_point`, `cv_sqrt3_T0`, `pyrochlore`
  - `properties`:
    - `J2_0`:
      - `type`: object
      - `required`: `Tc`, `latent_heat`, `mAF2_lowest_T`
      - `properties`:
        - `Tc`:
          - `type`: number
        - `latent_heat`:
          - `type`: number
        - `mAF2_lowest_T`:
          - `type`: number
    - `J2_critical_sqrt3`:
      - `type`: object
      - `required`: `Tc`, `latent_heat`
      - `properties`:
        - `Tc`:
          - `type`: number
        - `latent_heat`:
          - `type`: number
    - `J2_critical_q0`:
      - `type`: object
      - `required`: `Tc`, `latent_heat`
      - `properties`:
        - `Tc`:
          - `type`: number
        - `latent_heat`:
          - `type`: number
    - `triple_point`:
      - `type`: object
      - `required`: `J2`, `Tc`
      - `properties`:
        - `J2`:
          - `type`: number
        - `Tc`:
          - `type`: number
    - `cv_sqrt3_T0`:
      - `type`: number
    - `pyrochlore`:
      - `type`: object
      - `required`: `ordered_state_found`, `free_energy_diff`, `lowest_T`
      - `properties`:
        - `ordered_state_found`:
          - `type`: boolean
        - `free_energy_diff`:
          - `type`: number
        - `lowest_T`:
          - `type`: number

Notes: The agent must produce results.json by running the full NBT pipeline described in the workflow. The checker compares the reported numeric values to hidden paper‑derived gold references with per‑field tolerances (e.g., 10% relative for temperatures and latent heat, absolute tolerances for ordered moment and specific heat). All values are in units of J₁.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "J2_0",
          "J2_critical_sqrt3",
          "J2_critical_q0",
          "triple_point",
          "cv_sqrt3_T0",
          "pyrochlore"
        ],
        "properties": {
          "J2_0": {
            "type": "object",
            "required": [
              "Tc",
              "latent_heat",
              "mAF2_lowest_T"
            ],
            "properties": {
              "Tc": {
                "type": "number"
              },
              "latent_heat": {
                "type": "number"
              },
              "mAF2_lowest_T": {
                "type": "number"
              }
            }
          },
          "J2_critical_sqrt3": {
            "type": "object",
            "required": [
              "Tc",
              "latent_heat"
            ],
            "properties": {
              "Tc": {
                "type": "number"
              },
              "latent_heat": {
                "type": "number"
              }
            }
          },
          "J2_critical_q0": {
            "type": "object",
            "required": [
              "Tc",
              "latent_heat"
            ],
            "properties": {
              "Tc": {
                "type": "number"
              },
              "latent_heat": {
                "type": "number"
              }
            }
          },
          "triple_point": {
            "type": "object",
            "required": [
              "J2",
              "Tc"
            ],
            "properties": {
              "J2": {
                "type": "number"
              },
              "Tc": {
                "type": "number"
              }
            }
          },
          "cv_sqrt3_T0": {
            "type": "number"
          },
          "pyrochlore": {
            "type": "object",
            "required": [
              "ordered_state_found",
              "free_energy_diff",
              "lowest_T"
            ],
            "properties": {
              "ordered_state_found": {
                "type": "boolean"
              },
              "free_energy_diff": {
                "type": "number"
              },
              "lowest_T": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "A single JSON file containing the paper's headline quantitative results: transition parameters, ordered moment, triple point, specific heat, and pyrochlore verification."
    }
  ],
  "notes": "The agent must produce results.json by running the full NBT pipeline described in the workflow. The checker compares the reported numeric values to hidden paper‑derived gold references with per‑field tolerances (e.g., 10% relative for temperatures and latent heat, absolute tolerances for ordered moment and specific heat). All values are in units of J₁."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads /app/outputs/results.json. The verifier checks each required field against independently determined reference values derived from the published study. The comparison uses per‑field tolerances that account for the expected spread of a correct re‑implementation (e.g., relative tolerances for temperatures and latent heats, absolute tolerances for ordered moment and specific heat).

Each field carries a weight; the total reward is a weighted sum of the field‑level scores, normalised to the interval [0,1]. A perfect match to the hidden reference within the allowed tolerances yields full credit. Note that the verifier only inspects your written output — it does not re‑execute your code or access intermediate evidence files. Therefore, it is essential that you faithfully run the entire NBT pipeline and report the extracted quantities accurately; fabricating numbers that appear reasonable will not pass the verifier’s checks.
