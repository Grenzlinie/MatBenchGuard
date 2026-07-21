# Four-atom Anderson model chemisorption: exact and approximate interaction energies

## Problem background
Chemisorption, the chemical bonding of an atom or molecule to a solid surface, is often described by a tight‑binding model where the interaction between an adatom and a substrate is represented by a short chain of atoms. In this task we consider a four‑atom Anderson‑type model: an adatom (index 0) attached to the end of a three‑atom chain (indices 1,2,3), with parameters for the adatom's orbital energy, intra‑atomic Coulomb repulsion, and hopping to the chain, as well as the hopping within the chain. At half‑filling (one electron per atom, total $S_z = 0$) the ground‑state of the combined system can be found exactly by diagonalising the Hamiltonian in a 36‑state basis. The goal is to compute the interaction energy (negative of the binding energy) between the adatom and the chain, and to compare the exact result with several approximate schemes that are frequently used to treat such systems. The approximations include a weak‑binding perturbation theory, a rebonded surface complex picture, restricted Hartree‑Fock, and unrestricted Hartree‑Fock. The task is to evaluate these quantities for a specified range of the model parameters and to check the predicted asymptotic behaviour in the weak‑binding limit.

## Model description

### Hamiltonian
The system is described by the Anderson Hamiltonian on a four‑site chain:

$$
\begin{aligned}
\mathcal{H} &= E_a^0 \sum_{\sigma} n_{a\sigma} + U n_{a\uparrow} n_{a\downarrow} \\
&\quad -V \sum_{\sigma}\left(c_{1\sigma}^{\dagger} c_{a\sigma} + c_{a\sigma}^{\dagger} c_{1\sigma}\right) \\
&\quad -T \sum_{i=1}^{2} \sum_{\sigma}\left(c_{i\sigma}^{\dagger} c_{i+1,\sigma} + c_{i+1,\sigma}^{\dagger} c_{i\sigma}\right),
\end{aligned}
$$

where
- $E_a^0$ : energy level of the adatom orbital,
- $U$ : intra‑atomic Coulomb repulsion on the adatom,
- $T$ : hopping between neighbouring chain atoms,
- $V$ : hopping between the adatom (site 0) and the first chain atom (site 1),
- $c_{i\sigma}^{\dagger}$ ($c_{i\sigma}$) creates (annihilates) an electron on site $i$ with spin $\sigma$,
- $n_{a\sigma} = c_{a\sigma}^{\dagger} c_{a\sigma}$.

The chain atoms have zero on‑site energy, fixing the band centre at zero. Throughout this task we use the **symmetric Anderson model**, i.e.

$$
E_a^0 = -\frac{U}{2},
$$

which guarantees particle‑hole symmetry.

The hopping parameters are fixed:
- $T = 0.5$,
- units are such that $2T = 1$ (the bandwidth of the infinite chain is $4T = 2$).

### Desorbed (V = 0) ground state
When $V = 0$ the adatom and the three‑atom chain are decoupled. The chain single‑particle Hamiltonian in the spin subspace is

$$
H_{\text{chain}} = \begin{pmatrix}
0 & -T & 0 \\
-T & 0 & -T \\
0 & -T & 0
\end{pmatrix},
$$

whose eigenvalues are $-\sqrt{2}T,\ 0,\ +\sqrt{2}T$. At half‑filling the two lowest single‑particle levels are doubly occupied, giving a chain ground‑state energy of $-2\sqrt{2}T$. The adatom holds one electron with energy $E_a^0 = -U/2$, and to satisfy total $S_z=0$ its spin is taken opposite to that of the singly occupied molecular orbital $|\psi_0\rangle$. The unperturbed ground‑state energy is therefore

$$
E_0 = -\frac{U}{2} - 2\sqrt{2}T.
$$

### Exact solution: $S_z=0$ basis
For the full chain of 4 atoms with two spin‑up and two spin‑down electrons ($S_z=0$) the Hilbert space is spanned by Slater determinants where each spin sector occupies two of the four single‑particle sites. The number of states is $\binom{4}{2}^2 = 36$.

Construct the basis as follows:
- Represent each spin configuration for the up electrons by a 4‑bit mask (bit $i$ = 1 if site $i$ is occupied). There are 6 such masks, each with exactly two bits set. The same set of masks is used for the down electrons.
- A full basis state is a pair (up_mask, down_mask). Total dimension = $6 \times 6 = 36$.

**Building the Hamiltonian matrix** ($H$ is $36\times 36$):

1. **Diagonal terms**:
   - Single‑particle on‑site energy: each electron on the adatom (site 0) contributes $-U/2$; electrons on chain sites contribute 0.
   - Coulomb repulsion: if both spin‑up and spin‑down electrons occupy the adatom (bit 0 set in both masks), add $U$.

2. **Hopping terms** (kinetic energy):
   The hopping amplitudes are $-V$ between sites 0 ↔ 1, and $-T$ between sites 1 ↔ 2 and 2 ↔ 3.

   For each link $(p,q)$ with amplitude $t$:
   - **Spin‑up sector**: if site $p$ is occupied and $q$ is empty in the up_mask, the electron can hop to $q$. The new mask is obtained by clearing bit $p$ and setting bit $q$. The matrix element between the new state and the original state is $-t$ multiplied by a fermion sign $(-1)^{n}$, where $n$ is the number of up electrons on sites strictly between $p$ and $q$.
   - **Spin‑down sector**: same rule applied to the down_mask.

   The resulting matrix is symmetrized: $H \leftarrow (H + H^\dagger)/2$.

3. **Diagonalisation**:
   Compute the eigenvalues of $H$. The lowest eigenvalue is the exact ground‑state energy $E_{\text{exact}}$.

The exact interaction energy is then

$$
\Delta W_{\text{exact}} = E_{\text{exact}} - E_0.
$$

### Approximate methods

#### 1. Weak‑binding limit (second‑order perturbation theory)
When $V^2 \lesssim UT$ the change in energy is dominated by second‑order processes in the adatom‑chain hopping $V$. Evaluating all Feynman paths yields the analytic expression

$$
\Delta W_{\text{weak}} = -\frac{V^2}{U + 2\sqrt{2}T} - \frac{4V^2}{U}.
$$

#### 2. Rebonded Surface Complex (RSC)
The RSC approximation treats the adatom (site 0) and its nearest neighbour (site 1) as an exactly solved **dimer**, then treats the remaining two‑site chain as a perturbation.

a) **Dimer ground‑state energy**:
   The dimer Hamiltonian in the $(|\uparrow,\downarrow\rangle, |\uparrow\downarrow,0\rangle)$ basis is solved exactly. The lowest eigenvalue is

   $$
   E_{\text{SC}} = -\frac{U}{4} - \sqrt{\frac{U^2}{16} + 4V^2}.
   $$

   Equivalently, $E_{\text{SC}} = -\frac{1}{2}\left(\frac{U}{2} + \sqrt{\left(\frac{U}{2}\right)^2 + 16V^2}\right)$.

b) **Separation energy**: detaching site 1 from the three‑atom chain while keeping the chain in its ground state costs

   $$
   \Delta E_{\text{sep}} = 2(\sqrt{2} - 1) T.
   $$

c) **Zero‑order RSC interaction energy (without rebonding)**:

   $$
   \Delta W_{\text{SC}} = (E_{\text{SC}} + \Delta E_{\text{sep}}) - E_0.
   $$

d) **Rebonding correction**:
   The dimer eigenstates couple to the remaining two‑atom chain via the hopping $T$. The second‑order perturbation correction is

   $$
   \Delta W_{R} = -T^{2}\left[
   \frac{\left(E_{\text{SC}}E_{-} + 2V^{2}\right)^{2}}
        {(2E_{-} + T - E_{\text{SC}})(E_{\text{SC}}^{2} + 4V^{2})(E_{-}^{2} + V^{2})}
   +
   \frac{\left(E_{\text{SC}}E_{+} + 2V^{2}\right)^{2}}
        {(2E_{+} + T - E_{\text{SC}})(E_{\text{SC}}^{2} + 4V^{2})(E_{+}^{2} + V^{2})}
   \right],
   $$

   where

   $$
   E_{\pm} = \frac{-U \pm \sqrt{U^{2} + 16V^{2}}}{4}.
   $$

   The denominator factors must be handled carefully: if any denominator is zero (unlikely for the parameter ranges used), set the corresponding term to zero.

   **Total RSC interaction energy**:

   $$
   \Delta W_{\text{RSC}} = \Delta W_{\text{SC}} + \Delta W_{R}.
   $$

#### 3. Restricted Hartree‑Fock (RHF)
In RHF all orbitals are spin‑independent. It leads to the closed‑form expression

$$
\Delta W_{\text{RHF}} = -\sqrt{2}\left(
   \sqrt{V^{2} + 2T^{2} + \sqrt{V^{4} + 4T^{4}}}
   + \sqrt{V^{2} + 2T^{2} - \sqrt{V^{4} + 4T^{4}}}
   - 2T\right).
$$

Note: the radicand of the second square root is always non‑negative.

#### 4. Unrestricted Hartree‑Fock (URHF)
URHF allows spin‑symmetry breaking. Introduce the magnetisation parameter

$$
x = \frac{\langle n_{a\uparrow}\rangle - \langle n_{a\downarrow}\rangle}{2}.
$$

The self‑consistent equations are solved numerically.

**Procedure**:

- For a given $x$, construct the spin‑dependent single‑particle Hamiltonian matrices (size $4\times 4$):

  $$
  H_{\uparrow} = \begin{pmatrix}
  -Ux & -V & 0 & 0 \\
  -V & 0 & -T & 0 \\
  0 & -T & 0 & -T \\
  0 & 0 & -T & 0
  \end{pmatrix},\qquad
  H_{\downarrow} = \begin{pmatrix}
  +Ux & -V & 0 & 0 \\
  -V & 0 & -T & 0 \\
  0 & -T & 0 & -T \\
  0 & 0 & -T & 0
  \end{pmatrix}.
  $$

- Diagonalise each matrix. From each spin sector fill the two lowest eigenstates (half‑filling) and sum their energies to obtain the total occupied single‑particle energy $E_{\text{occ}}(x)$.

- Compute the total URHF energy including the double‑counting correction:

  $$
  E_{\text{URHF}}(x) = E_{\text{occ}}(x) - U\!\left(\frac{1}{4} - x^{2}\right).
  $$

- The self‑consistent $x$ is the one that minimises $E_{\text{URHF}}(x)$ on the interval $0 \le x \le \frac{1}{2}$ (the upper bound comes from the fact that the adatom occupation cannot exceed $1$ per spin). Use any robust minimisation algorithm (e.g., golden‑section search, Brent's method) to find the optimal $x^{*}$.

- The URHF interaction energy is

  $$
  \Delta W_{\text{URHF}} = E_{\text{URHF}}(x^{*}) - E_0.
  $$

#### 5. Weak‑binding asymptotic ratio
Define the quantity

$$
R = \frac{|\Delta W_{\text{weak}}| \cdot U}{V^{2}}.
$$

From the explicit formula for $\Delta W_{\text{weak}}$ we obtain

$$
R = \frac{U}{U + 2\sqrt{2}T} + 4.
$$

## Reproduction target
Produce two CSV files:

1. `interaction_energies.csv`: For $U \in \{1.0, 2.5, 4.0\}$ and $V \in \{0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5\}$ (units where $2T = 1$, $T = 0.5$), compute and record the exact interaction energy $\Delta W$ (`exact_deltaW`) and the four approximate interaction energies (`weak_deltaW`, `RSC_deltaW`, `RHF_deltaW`, `URHF_deltaW`).

2. `weak_limits.csv`: For $V = 10^{-4}$, $T = 0.5$, compute the ratio $R = |\Delta W_{\text{weak}}| \cdot U / V^{2}$ for $U = 4.0$ and $U = 0.1$. Report the ratio in a column named `ratio`.

All energies are in units where $2T = 1$. The CSVs must contain the columns and precision such that a separate verification script can read them reliably.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute interaction energies
- Role: scored (load-bearing)
- Action: Implement the four‑atom Anderson model as described in **Model description**. For each $(U,V)$ pair compute $\Delta W$ exactly and via the four approximations using the formulas and procedures given above.
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: CSV header: `U,V,exact_deltaW,weak_deltaW,RSC_deltaW,RHF_deltaW,URHF_deltaW`. Each row is one $(U,V)$ combination. Values are floating‑point numbers (units such that $2T=1$, $T=0.5$).
- Scoring: scored by hidden verifier

### Step 2: Verify weak‑binding asymptotic limits
- Role: scored
- Action: Using the weak‑binding formula, compute the ratio $R = |\Delta W_{\text{weak}}| \cdot U / V^{2}$ for $U=4.0$ and $U=0.1$ with $V=10^{-4}$, $T=0.5$. Write the results to a CSV.
- Output file: `/app/outputs/weak_limits.csv`
- Format: csv
- Contract: CSV header: `U,V,ratio`. Two rows: one for $U=4.0$, $V=10^{-4}$ and one for $U=0.1$, $V=10^{-4}$. `ratio` is a floating‑point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.csv`
- `/app/outputs/weak_limits.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Interaction energies (negative of binding energy) for the four‑atom Anderson model for a grid of U and V values. The checker will recompute the exact interaction energy for hidden (U,V) pairs and the approximations, comparing with given tolerances.
- schema:
  - `type`: table
  - `required_columns`: `U`, `V`, `exact_deltaW`, `weak_deltaW`, `RSC_deltaW`, `RHF_deltaW`, `URHF_deltaW`
  - `units`:
    - `U`: 2T units (T=0.5)
    - `V`: 2T units
    - `exact_deltaW`: 2T units
    - `weak_deltaW`: 2T units
    - `RSC_deltaW`: 2T units
    - `RHF_deltaW`: 2T units
    - `URHF_deltaW`: 2T units

### weak_limits.csv
- path: `/app/outputs/weak_limits.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Verification of the weak‑binding asymptotic limits: |ΔW_w|·U/V² should approach ~5 for large U and ~4 for small U. The checker recomputes the ratio from the formula and checks agreement within a narrow tolerance.
- schema:
  - `type`: table
  - `required_columns`: `U`, `V`, `ratio`
  - `units`:
    - `U`: 2T units (T=0.5)
    - `V`: 2T units
    - `ratio`: dimensionless

Notes: The task is a pure numerical reproduction; no external data or pre‑trained models are required. The agent must implement the 36×36 Hamiltonian and the analytic formulas described above. The URHF solution may be obtained by any robust root‑finding/minimisation method. All energies are in units where $2T=1$ ($T=0.5$). The interaction energy is defined as $\Delta W = E_{\text{ground}} - E_0$, with $E_0$ given in the model description.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "V",
          "exact_deltaW",
          "weak_deltaW",
          "RSC_deltaW",
          "RHF_deltaW",
          "URHF_deltaW"
        ],
        "units": {
          "U": "2T units (T=0.5)",
          "V": "2T units",
          "exact_deltaW": "2T units",
          "weak_deltaW": "2T units",
          "RSC_deltaW": "2T units",
          "RHF_deltaW": "2T units",
          "URHF_deltaW": "2T units"
        }
      },
      "description": "Interaction energies (negative of binding energy) for the four-atom Anderson model for a grid of U and V values. The checker will recompute the exact interaction energy for hidden (U,V) pairs and the approximations, comparing with given tolerances."
    },
    {
      "file": "weak_limits.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "V",
          "ratio"
        ],
        "units": {
          "U": "2T units (T=0.5)",
          "V": "2T units",
          "ratio": "dimensionless"
        }
      },
      "description": "Verification of the weak-binding asymptotic limits: |ΔW_w| * U / V² should approach ~5 for large U and ~4 for small U. The checker recomputes the ratio from the formula and checks agreement within a narrow tolerance."
    }
  ],
  "notes": "The task is a pure numerical reproduction; no external data or pre-trained models are required. The agent must implement the 36×36 Hamiltonian and the analytic formulas. The URHF solution may be obtained by any robust root-finding/minimization method. All energies are in units where 2T=1 (T=0.5). The interaction energy is defined as ΔW = E_ground − E_0, with E_0 given in the problem background."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently recomputes the exact interaction energy and the four approximate energies for a secret subset of $(U,V)$ parameter pairs. The verifier will compare your reported values for those hidden pairs to its own recomputed results, using numerical tolerances that account for legitimate numerical differences. For the exact energy, the comparison is strict; for the approximate energies, a relative tolerance is applied. The weak‑binding limit file (`weak_limits.csv`) will also be checked by recomputing the ratio from the same formula and comparing with a small margin.

The overall reward is a weighted combination of the scores from the two artifacts, with most of the weight on the interaction energy table. Earning a high score requires that your computed values for the hidden $(U,V)$ pairs are correct within the allowed tolerances—simply copying published numbers without performing the actual computation will not pass because the hidden pairs are not disclosed.