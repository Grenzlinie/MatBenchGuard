# Reproduce zero-temperature phase diagram and finite-temperature transition in a frustrated spin ladder using bond-mean-field theory

## Problem background
The problem concerns quantum and classical criticalities in the frustrated spin-1/2 antiferromagnetic Heisenberg model on a two-leg ladder. The system consists of two parallel chains of N sites each, with spin interactions along the chains (J), across rungs (J⊥), and along diagonals (J×). Frustration arises from the competition of these couplings, which can stabilize different short-range-ordered spin liquid states without conventional long-range magnetic order. Understanding which state is the ground state for a given pair of dimensionless coupling ratios α1 = J⊥/J and α2 = J×/J, and how thermal fluctuations drive transitions between these states, is the central question. The target is to compute the zero-temperature phase classification, the critical temperature of a thermally induced transition, and the behaviour of the uniform spin susceptibility at that transition, entirely from the underlying model Hamiltonian and mean-field theory.

## Approach
The reproduction uses bond-mean-field theory (BMFT) based on a Jordan–Wigner transformation that maps the spin Hamiltonian to interacting spinless fermions. The key idea is to decouple the fermionic interaction terms using mean-field bond parameters that capture short-range spin correlations: Q (along chains), P (along rungs), and P' (along diagonals). This leads to a quadratic mean-field Hamiltonian that can be diagonalized in momentum space, yielding four eigenenergy bands for each of three candidate ordered states, labelled Néel-type (N), ferromagnetic-chain-type (F), and ferromagnetic-rung-type (R). For each state, the free energy per site is expressed in terms of the bond parameters and the eigenenergies. Minimising the free energy with respect to Q, P, P' gives a set of self-consistent integral equations that must be solved numerically. At each temperature T, the self-consistent solutions for the three candidate states are obtained, and the state with the lowest free energy is identified as the stable one. The ground-state phase is determined by evaluating this comparison at T = 0. Finite-temperature transitions are located by sweeping temperature and finding the crossing point of the free energies of two competing states. The uniform static magnetic susceptibility χ(T) is computed using linear response by adding a small Zeeman coupling and evaluating the resulting shift in the filled bands, using the converged self-consistent solution at each temperature.

### Key equations

**Model Hamiltonian** (spin‑1/2 on a two‑leg ladder with N sites per chain):

$$ H = J \sum_{i=1}^N \sum_{j=1}^2 \mathbf{S}_{i,j}\!\cdot\!\mathbf{S}_{i+1,j} + J_\perp \sum_{i=1}^N \mathbf{S}_{i,1}\!\cdot\!\mathbf{S}_{i,2} + J_\times \sum_{i=1}^N \big( \mathbf{S}_{i,1}\!\cdot\!\mathbf{S}_{i+1,2} + \mathbf{S}_{i+1,1}\!\cdot\!\mathbf{S}_{i,2} \big) . $$

**Jordan–Wigner transformation** (with the phase assignment that eliminates the phase string in the BMFT):

$$ S_{i,j}^- = c_{i,j} e^{i\phi_{i,j}}, \quad S_{i,j}^z = n_{i,j} - \tfrac12, \quad n_{i,j}=c_{i,j}^\dagger c_{i,j}, $$

$$ \phi_{i,1} = \pi\sum_{d=0}^{i-1}\sum_{f=1}^2 n_{d,f}, \qquad \phi_{i,2} = \pi\!\left(\sum_{d=0}^{i-1}\sum_{f=1}^2 n_{d,f} + n_{i,1}\right). $$

**BMFT bond parameters and decoupling** (Hartree–Fock approximation):

$$ Q = \langle c_{i,j} c_{i+1,j}^\dagger \rangle,\quad P = \langle c_{i,j} c_{i,j+1}^\dagger \rangle,\quad P' = \langle c_{i+1,j} c_{i,j+1}^\dagger \rangle . $$

The Ising interaction, e.g. along chain 1, is decoupled as  
$$ (c_{i,1}^\dagger c_{i,1} - \tfrac12)(c_{i+1,1}^\dagger c_{i+1,1} - \tfrac12) \approx Q c_{i,1}^\dagger c_{i+1,1} + Q^* c_{i+1,1}^\dagger c_{i,1} + |Q|^2 . $$

An alternating phase of π along each chain is introduced (phase per plaquette = π) so that the Hamiltonian reduces to a quadratic fermionic form in Nambu space. Diagonalising that 4×4 Nambu matrix gives the eigenenergies.

**Eigenenergies** for the three competing short‑range‑ordered states (N = Néel‑type, F = ferromagnetic‑chain‑type, R = ferromagnetic‑rung‑type). The renormalised couplings are

$$ J_1 = J(1+2Q), \quad J_{\perp1} = J_\perp(1+2P), \quad J_{\times1} = J_\times(1+2P'). $$

$$
\begin{aligned}
E_N(k) &= \pm J_{\times1}\cos k \pm \sqrt{ J_1^{2}\sin^{2}k + \frac{J_{\perp1}^{2}}{4} } ,\\
E_F(k) &= \pm J_1\cos k \pm \sqrt{ J_{\times1}^{2}\sin^{2}k + \frac{J_{\perp1}^{2}}{4} } ,\\
E_R(k) &= \pm \frac{J_{\perp1}}{2} \pm \sqrt{ J_1^{2}\sin^{2}k + J_{\times1}^{2}\cos^{2}k } .
\end{aligned}
$$

**Free energy per site** (sum over the four bands $p=1,\dots,4$):

$$ F = J Q^{2} + \frac{1}{2}J_\perp P^{2} + J_\times P'^{\,2} - \frac{k_{\!B}T}{4N}\sum_k\sum_{p=1}^{4} \ln\!\big[1 + e^{-\beta E_p(k)}\big] . $$

**Self‑consistent equations** (obtained from $\partial F/\partial Q = \partial F/\partial P = \partial F/\partial P' = 0$):

$$
\begin{aligned}
Q &= -\frac{1}{8NJ} \sum_k \sum_{p=1}^4 \frac{\partial E_p(k)}{\partial Q}\, n_F[E_p(k)],\\
P &= -\frac{1}{4NJ_\perp} \sum_k \sum_{p=1}^4 \frac{\partial E_p(k)}{\partial P}\, n_F[E_p(k)],\\
P' &= -\frac{1}{8NJ_\times} \sum_k \sum_{p=1}^4 \frac{\partial E_p(k)}{\partial P'}\, n_F[E_p(k)],
\end{aligned}
$$

where $n_F(\varepsilon) = 1/(e^{\beta\varepsilon}+1)$ and the derivatives are taken from the explicit expressions, e.g. $\partial E_p/\partial Q = (\partial E_p/\partial J_1)\cdot 2J$, etc.

**Uniform spin susceptibility** (from linear response to a Zeeman field $-h\sum S^z$). After adding the field, the eigenenergies $E_p(k;h)$ acquire a field‑dependence. The susceptibility per site is

$$ \chi = \frac{1}{N}\sum_k \sum_{p=1}^4 \left.\frac{\partial n_F(E_p)}{\partial h}\right|_{h=0} \approx \frac{1}{N}\sum_k \sum_{p=1}^4 n_F'(E_p) \left(\frac{\partial E_p}{\partial h}\right)^2 , $$

evaluated at the self‑consistent solution for the chosen temperature. The derivative $\partial E_p/\partial h$ is obtained by treating the Zeeman term as a shift of the chemical potential or by explicitly solving the mean‑field equations in the presence of a small finite $h$ (the agent may use a finite‑difference approach with $h \ll J$).

## Reproduction target
Construct a parameter grid of coupling ratios α1 ∈ [0, 2] and α2 ∈ [0, 2] with a step of 0.1, plus the two extra points (α1=0.6, α2=0.5) and (α1=1.25, α2=2.0). Solve the BMFT self-consistent equations numerically for each grid point at T = 0 and for each of the three states N, F, R. From the resulting free energies, classify each grid point by the state with the lowest free energy and record the stable ground-state phase. For the two extra coupling points, perform a temperature sweep (starting from low T up to where a crossing occurs) and pinpoint the temperature T_c at which the free energy of the R-type state crosses that of the N-type state. Report these two transition temperatures. Finally, for (α1=0.6, α2=0.5), compute the spin susceptibility χ at T = 0.2 and T = 0.6 (in units of kB T/J) and record the values.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Parameter grid preparation
- Role: process
- Action: Define a parameter grid of coupling ratios (α1 = J⊥/J, α2 = J×/J) covering the region 0 ≤ α1 ≤ 2, 0 ≤ α2 ≤ 2 with a step of 0.1. Also include the two specific points (α1=0.6, α2=0.5) and (α1=1.25, α2=2.0) for the finite-temperature transition. Output the full list of (α1, α2) pairs to a CSV file.
- Evidence: `/app/outputs/parameter_grid.csv`

### Step 2: BMFT self-consistent solver
- Role: process
- Action: Implement the bond-mean-field theory for the frustrated spin-1/2 two-leg Heisenberg ladder. For each target (α1, α2) and temperature T, use the eigenenergy formulas for the three competing short-range-ordered states (N, F, R) and the self-consistent equations for bond parameters Q, P, P' to numerically determine the bond parameters and the free energy per site F for each state. Store the converged free energies.
- Evidence: `/app/outputs/free_energies.csv`

### Step 3: Zero-temperature phase classification
- Role: scored (load-bearing)
- Action: Using the free energies at T=0 for all (α1, α2) points prepared in step_00, identify the state with the lowest free energy. Write the stable phase string (N, F, or R) for each point as the ground-state phase.
- Output file: `/app/outputs/zero_T_phases.csv`
- Format: csv
- Contract: columns: alpha1 (float), alpha2 (float), stable_phase (string: N/R/F). One row per prescribed point.
- Scoring: scored by hidden verifier

### Step 4: Finite-temperature R–N transition temperature
- Role: scored
- Action: For the two coupling sets (α1=0.6, α2=0.5) and (α1=1.25, α2=2.0), perform a temperature sweep solving the self-consistent equations at each T. Locate the temperature T_c where the free energy of the R-type state crosses that of the N-type state (first-order thermal transition). Report the transition temperature.
- Output file: `/app/outputs/transition_temperatures.csv`
- Format: csv
- Contract: columns: alpha1 (float), alpha2 (float), T_c (float). Two rows: (0.6, 0.5) and (1.25, 2.0).
- Scoring: scored by hidden verifier

### Step 5: Susceptibility trend check
- Role: scored
- Action: For the coupling set α1=0.6, α2=0.5, compute the uniform static magnetic susceptibility χ at temperatures T=0.2 and T=0.6 (in units of k_B T/J). Use the self-consistent solution at each temperature and the appropriate formula (derived from the Zeeman coupling) to compute χ. Output the values.
- Output file: `/app/outputs/susceptibility_trend.csv`
- Format: csv
- Contract: columns: alpha1 (float), alpha2 (float), T (float), chi (float). For α1=0.6, α2=0.5 with T=0.2 and 0.6.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zero_T_phases.csv`
- `/app/outputs/transition_temperatures.csv`
- `/app/outputs/susceptibility_trend.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zero_T_phases.csv
- path: `/app/outputs/zero_T_phases.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ground-state phase labels (N, R, or F) for a grid of coupling ratios. The checker compares each point against hidden gold extracted from the paper's zero-temperature phase diagram. Exact match is required; partial credit per point.
- schema:
  - `type`: table
  - `required_columns`: `alpha1`, `alpha2`, `stable_phase`

### transition_temperatures.csv
- path: `/app/outputs/transition_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Thermal transition temperatures T_c (in units of k_B T/J) from the R-type to the N-type state for two specific coupling sets. The checker compares the reported values to hidden gold transition temperatures with a predefined tolerance.
- schema:
  - `type`: table
  - `required_columns`: `alpha1`, `alpha2`, `T_c`

### susceptibility_trend.csv
- path: `/app/outputs/susceptibility_trend.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Uniform spin susceptibility χ at two temperatures for one coupling set. The checker verifies that χ at T=0.6 is greater than χ at T=0.2 (structural inequality), confirming the increasing trend through the thermal transition.
- schema:
  - `type`: table
  - `required_columns`: `alpha1`, `alpha2`, `T`, `chi`

Notes: The scored artifacts collectively reproduce the core computational claims of the paper: the zero-temperature phase diagram, two specific finite-temperature transition points, and the trend of increasing susceptibility at the transition. All numeric gold values remain hidden from the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zero_T_phases.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha1",
          "alpha2",
          "stable_phase"
        ]
      },
      "description": "Ground-state phase labels (N, R, or F) for a grid of coupling ratios. The checker compares each point against hidden gold extracted from the paper's zero-temperature phase diagram. Exact match is required; partial credit per point."
    },
    {
      "file": "transition_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha1",
          "alpha2",
          "T_c"
        ]
      },
      "description": "Thermal transition temperatures T_c (in units of k_B T/J) from the R-type to the N-type state for two specific coupling sets. The checker compares the reported values to hidden gold transition temperatures with a predefined tolerance."
    },
    {
      "file": "susceptibility_trend.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha1",
          "alpha2",
          "T",
          "chi"
        ]
      },
      "description": "Uniform spin susceptibility χ at two temperatures for one coupling set. The checker verifies that χ at T=0.6 is greater than χ at T=0.2 (structural inequality), confirming the increasing trend through the thermal transition."
    }
  ],
  "notes": "The scored artifacts collectively reproduce the core computational claims of the paper: the zero-temperature phase diagram, two specific finite-temperature transition points, and the trend of increasing susceptibility at the transition. All numeric gold values remain hidden from the public contract."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the three required output files: `zero_T_phases.csv`, `transition_temperatures.csv`, and `susceptibility_trend.csv`. For `zero_T_phases.csv`, each row's `stable_phase` label is compared against a hidden gold list extracted from the paper’s zero-temperature phase diagram; exact match is required, with partial credit awarded per point. For `transition_temperatures.csv`, the two reported T_c values are compared to hidden reference values (the paper’s reported transition temperatures) within a pre-defined tolerance. For `susceptibility_trend.csv`, the verifier checks that χ at T = 0.6 is strictly greater than χ at T = 0.2 — a structural inequality confirming the increasing trend through the transition. The three scores are combined by weight to produce a final reward between 0 and 1. Merely quoting the paper’s numbers is not sufficient; your workflow must produce these outputs by actually executing the BMFT solver.
