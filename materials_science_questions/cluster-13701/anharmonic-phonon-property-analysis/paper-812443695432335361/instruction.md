# Quadrupole Phonon Model Fitting and Anharmonic Observables for ¹¹⁴Cd

## Problem background
Even‑even spherical nuclei exhibit collective vibrational motion that can be modelled with quadrupole phonons. The simple harmonic picture, however, fails to account for observed deviations in energy level spacings and electromagnetic transition properties. A quadrupole phonon model that includes anharmonic coupling terms among phonons can capture these deviations. This task reproduces a numerical implementation of such a model, fitting it to the experimental level spectrum of the nucleus ¹¹⁴Cd and computing the resulting anharmonic energy levels and electromagnetic observables.

## Model definition

### 1. Quadrupole phonon operators
The basic degrees of freedom are boson creation and annihilation operators for quadrupole phonons. The phonon carries angular momentum 2.

- Creation operator: \(B_{2m}^{\dagger}\) (with \(m = -2, -1, 0, 1, 2\)).
- Annihilation operator: \(B_{2m}\).
- Standard boson commutation relations:
  \[
  [B_{2m}, B_{2m'}^{\dagger}] = \delta_{m m'},\qquad
  [B_{2m}, B_{2m'}] = 0,\qquad
  [B_{2m}^{\dagger}, B_{2m'}^{\dagger}] = 0 .
  \]
- Time‑reversed (spherical tensor) form:
  \[
  \tilde{B}_{2m} = (-1)^{2-m} B_{2,-m}.
  \]
  Under this convention \(\tilde{B}_{2m}\) transforms as a spherical tensor of rank 2, component \(m\).

### 2. Hamiltonian
The model Hamiltonian is given by the scalar‑coupled expansion (Eq. 4 of the paper):

\[
\begin{aligned}
H &= \omega_0\,(5)^{\frac12} [B^{\dagger} \tilde{B}]^{0}
     + w_2 \Big\{ [B^{\dagger} B^{\dagger}]^{0} + [\tilde{B} \tilde{B}]^{0} \Big\} \\
  &\quad + w_3 \Big\{ [B^{\dagger} B^{\dagger} B^{\dagger}]^{0}
                     + [B^{\dagger} B^{\dagger} \tilde{B}]^{0}
                     + [B^{\dagger} \tilde{B} \tilde{B}]^{0}
                     + [\tilde{B} \tilde{B} \tilde{B}]^{0} \Big\} \\
  &\quad + w_4 \Big\{ [B^{\dagger} B^{\dagger} B^{\dagger} B^{\dagger}]^{0}
                     + [B^{\dagger} B^{\dagger} B^{\dagger} \tilde{B}]^{0}
                     + \dots \Big\} + \dots
\end{aligned}
\]

The square brackets with superscript \(0\) denote coupling of the enclosed spherical tensors to total angular momentum zero. For two tensors \(T^{(L)}\) and \(U^{(L')}\) the scalar product is

\[
[T^{(L)} U^{(L')}]^{0}_0 = \sum_{m,m'} C_{Lm, L'm'}^{00}\; T^{(L)}_m U^{(L')}_{m'} ,
\]

with the Clebsch‑Gordan coefficient \(C_{Lm,L'm'}^{00} = \delta_{L L'}\,\frac{(-1)^{L-m}}{\sqrt{2L+1}}\).  
Explicitly, e.g., \([B^{\dagger} B^{\dagger}]^{0} = \frac{1}{\sqrt{5}} \sum_{m=-2}^{2} (-1)^{2-m} B_{2m}^{\dagger} B_{2,-m}^{\dagger}\).

The term \([B^{\dagger} \tilde{B}]^{0}\) is the phonon number operator up to a factor:
\[
[B^{\dagger} \tilde{B}]^{0} = \frac{1}{\sqrt{5}} \sum_{m} (-1)^{2-m} B_{2m}^{\dagger} \tilde{B}_{2,-m}
= \frac{1}{\sqrt{5}} \sum_{m} B_{2m}^{\dagger} B_{2m},
\]
so that \(\omega_0\,(5)^{\frac12} [B^{\dagger} \tilde{B}]^{0} = \omega_0 \sum_m B_{2m}^{\dagger} B_{2m}\).

Higher‑order couplings are defined analogously, always coupling all operators to a total angular momentum zero. For instance,
\[
[B^{\dagger} B^{\dagger} B^{\dagger}]^{0} =
\frac{1}{\sqrt{5}} \sum_{m_1,m_2} C_{2m_1,2m_2}^{2,\mu}
C_{2\mu,2m_3}^{00}\; B_{2m_1}^{\dagger} B_{2m_2}^{\dagger} B_{2m_3}^{\dagger}
\]
with summation over all magnetic quantum numbers and \(\mu\).

### 3. Truncated basis
The wavefunctions of low‑lying states are expanded in a basis containing up to **three phonons**. The basis states for a given total angular momentum \(J\) and projection \(M\) are obtained by coupling \(N\) phonon creation operators (\(N=0,1,2,3\)) and applying them to the boson vacuum \(|0\rangle\). Because phonons are identical bosons, only totally symmetric states are possible.

For each \(J\) the following basis vectors are used (they are taken to be orthonormal):

- **\(J=0\)**:
  \[
  \begin{aligned}
  |1\rangle &= |0\rangle, \\
  |2\rangle &= \big(B^{\dagger} B^{\dagger}\big)^{0}_0 |0\rangle, \\
  |3\rangle &= \big( (B^{\dagger} B^{\dagger})^{2} B^{\dagger} \big)^{0}_0 |0\rangle .
  \end{aligned}
  \]
  The two‑phonon state is coupled from two \(B^{\dagger}\) to total 0:
  \[
  \big(B^{\dagger} B^{\dagger}\big)^{0}_0 =
  \frac{1}{\sqrt{5}} \sum_m (-1)^{2-m} B_{2m}^{\dagger} B_{2,-m}^{\dagger}.
  \]
  The three‑phonon state is obtained by first coupling two phonons to angular momentum 2, then coupling the third to total 0:
  \[
  \big( (B^{\dagger} B^{\dagger})^{2} B^{\dagger} \big)^{0}_0 =
  \sum_{m_1,m_2,m_3} C_{2m_1,2m_2}^{2,\mu}\,
  C_{2\mu, 2m_3}^{00}\; B_{2m_1}^{\dagger} B_{2m_2}^{\dagger} B_{2m_3}^{\dagger}.
  \]

  All basis states are normalised: \(\langle i|j\rangle = \delta_{ij}\).  (Normalisation factors are absorbed in the definition; you may verify them numerically.)

- **\(J=2\)**:
  \[
  \begin{aligned}
  |1_M\rangle &= B_{2M}^{\dagger} |0\rangle, \\
  |2_M\rangle &= \big(B^{\dagger} B^{\dagger}\big)^{2}_M |0\rangle, \\
  |3_M\rangle &= \big( (B^{\dagger} B^{\dagger})^{L} B^{\dagger} \big)^{2}_M |0\rangle,
                \quad \text{with } L=2\text{ or }4.
  \end{aligned}
  \]
  The coupling sequence for the three‑phonon state is not unique; however the space spanned by the two independent couplings (\(L=2\) and \(L=4\)) has dimension 2.  To obtain an orthonormal basis one may construct the matrix of overlaps of the two three‑phonon states and diagonalise it, keeping only the state that is linearly independent from the one‑ and two‑phonon states.  In practice, for the present calculation you may choose the coupling \(L=2\) and then orthogonalise the resulting 3‑phonon vector against \(|1_M\rangle\) and \(|2_M\rangle\) using a Gram–Schmidt procedure.  (The coupling \(L=4\) can be omitted; the essential physics is contained in the \(L=2\) coupling because the Hamiltonian is rotationally invariant and the matrix elements are insensitive to this choice as long as one consistent three‑phonon \(2^{+}\) state is defined.)

  The normalised two‑phonon state is
  \[
  \big(B^{\dagger} B^{\dagger}\big)^{2}_M =
  \sum_{m_1,m_2} C_{2m_1,2m_2}^{2,M}\; B_{2m_1}^{\dagger} B_{2m_2}^{\dagger}.
  \]

- **\(J=4\)**:
  Only one basis state is needed for the present calculation:
  \[
  |1_M\rangle = \big(B^{\dagger} B^{\dagger}\big)^{4}_M |0\rangle .
  \]
  Additional higher‑phonon states for \(4^{+}\) are not required to describe the lowest two \(4^{+}\) levels in the fitting procedure described below.

### 4. Hamiltonian matrix elements
Matrix elements of \(H\) are evaluated between the orthonormal basis states using the boson commutation relations and the explicit coupling formulas.  Because the total angular momentum is conserved, the matrix is block‑diagonal in \(J\).  The following expressions give the non‑zero, non‑trivial elements for each block.  All energies are expressed in MeV.

#### 4.1 \(J=0\) block
Basis order: \(\{|1\rangle, |2\rangle, |3\rangle\}\) as defined above.
\[
\begin{aligned}
H_{11} &= 0, \\
H_{22} &= 2\omega_0 + 2\sqrt{5}\,w_4, \\
H_{33} &= 3\omega_0 + 6\sqrt{5}\,w_4, \\
H_{12} &= H_{21} = \sqrt{2}\,w_2, \\
H_{13} &= H_{31} = \sqrt{\frac{6}{5}}\; w_3, \\
H_{23} &= H_{32} = \sqrt{\frac{12}{5}}\; w_3 + \sqrt{\frac{54}{5}}\; w_4\,? \quad \text{(need careful derivation)}.
\end{aligned}
\]

**Important**: The above matrix elements are schematic; the exact numerical coefficients depend on the normalisation of the basis states and the correct evaluation of the scalar‑coupled products.  For a faithful implementation you **must** compute the matrix elements yourself by explicitly applying the operators to the basis states, using the boson algebra and the coupling rules.  The following procedure is recommended:

- Represent each basis vector as a linear combination of Fock states \(|n_{-2}, n_{-1}, n_0, n_1, n_2\rangle\) with total phonon number \(N=\sum n_i\le 3\).
- For each term in \(H\) (a product of \(B^{\dagger}\) and \(B\)), compute its action on each basis state, simplify using commutation relations, and evaluate inner products.
- Because the Hilbert space is small, this can be done analytically with a computer algebra system or by writing a small script that symbolically manipulates the boson operators.

The final matrix elements will be linear combinations of \(\omega_0, w_2, w_3, w_4\).  Carefully check Hermiticity.

#### 4.2 \(J=2\) block
Basis order: \(\{|1_M\rangle, |2_M\rangle, |3_M\rangle\}\) (after orthogonalisation).  The matrix elements are analogous, with coefficients that differ because of angular momentum coupling factors.  Again, explicit computation is required.

#### 4.3 \(J=4\) block
Only one basis vector: \(\langle \text{two‑phonon }4^{+}| H |\text{two‑phonon }4^{+}\rangle = 2\omega_0 + \text{correction from }w_4\).  For the purpose of fitting, you may either include this block or treat the \(4^{+}\) states entirely from the fitted parameters and the \(2^{+}\) block.

### 5. Fitting procedure
The experimental energies of the first three \(2^{+}\) states in ¹¹⁴Cd are known:

\[
E_{2^+}^{\text{exp}} = 0.5585\ \text{MeV},\quad
E_{2'^+}^{\text{exp}} = 1.208\ \text{MeV},\quad
E_{2''^+}^{\text{exp}} = 1.840\ \text{MeV}.
\]

These values are taken as diagonal elements of the “true” Hamiltonian in a special basis.  The central idea is to require that the eigenvalues of the model Hamiltonian \(H(\omega_0, w_2, w_3, w_4)\) in the \(J=2\) block, after diagonalisation, exactly reproduce these three experimental energies.  This fixes the four parameters up to an overall scale, which is already set by the experimental energies themselves.

**Practical algorithm**:
1. Build the \(3\times3\) Hamiltonian matrix \(H^{(2)}\) in the \(J=2\) basis as a function of the parameters \(\omega_0, w_2, w_3, w_4\).
2. Compute the eigenvalues \(E_i(\omega_0,\dots)\).
3. Find the parameters that minimise
   \[
   \chi^2 = \sum_{i=1}^{3} \big( E_i(\omega_0,\dots) - E_{i}^{\text{exp}} \big)^2 .
   \]
   Because the eigenenergies are non‑linear functions of the parameters, use a numerical minimiser (e.g., `scipy.optimize.minimize`).
4. Once the parameters are obtained, compute the \(J=0\) and \(J=4\) Hamiltonian blocks and diagonalise them to obtain the \(0^{+}\) and \(4^{+}\) excited energies.  The first \(0^{+}\) state must be the ground state (experimentally the ground state energy is defined as zero).  The model yields a ground‑state energy that is not zero a priori; set the overall energy zero by subtracting the ground‑state eigenvalue from all energies.  Then read off the excited \(0^{+}\) and \(4^{+}\) energies.

**Iterative refinement** (optional but recommended):  
If the minimisation does not converge or yields unrealistic parameters, try different initial guesses and repeat the whole cycle until the calculated \(2^{+}\) energies match the experimental ones within \(10^{-4}\) MeV.

### 6. Electromagnetic observables — E2 transition operator
The electric quadrupole (E2) transition operator is expanded in phonon operators.  The leading‑order term (which is sufficient for reproducing the published ratios) is the linear expression:

\[
T(E2, \mu) = e_{\text{eff}} \Big( B_{2\mu}^{\dagger} + (-1)^{\mu} \tilde{B}_{2,-\mu} \Big),
\]

where \(e_{\text{eff}}\) is an effective charge.  Because we require only **ratios** of reduced transition probabilities and quadrupole moments, the overall factor \(e_{\text{eff}}\) cancels and can be set to 1.

- **Reduced transition probability** for a transition \(|J_i\rangle \to |J_f\rangle\):
  \[
  B(E2; J_i \to J_f) = \frac{|\langle J_f || T(E2) || J_i \rangle|^2}{2J_i+1}.
  \]
- **Quadrupole moment** of a state \(|J\rangle\) (with \(J\ge1\)):
  \[
  Q(J) = \langle JJ | T(E2,0) | JJ \rangle
       = C_{J2J}^{J0}\,\frac{ \langle J || T(E2) || J \rangle }{ \sqrt{2J+1} },
  \]
  where the Clebsch‑Gordan coefficient \(C_{J2J}^{J0}\) can be evaluated.  For \(J=2\), \(C_{220}^{20} = -\sqrt{2/7}\).
  The ratio \(Q_{22}/Q_{20}\) required in the output is simply the ratio of the quadrupole moments of the first two \(2^{+}\) states:
  \[
  \frac{Q(2'_1)}{Q(2_1)} .
  \]

**Computation of reduced matrix elements**:  
Given the wavefunction expansion coefficients for each state (obtained from the diagonalisation of \(H^{(2)}\) and \(H^{(0)}\)), evaluate the reduced matrix element of \(T(E2)\) between the states using the basis matrix elements \(\langle n' J' || T(E2) || n J \rangle\).  These can be derived from the action of \(B^{\dagger}\) and \(\tilde{B}\) on the basis vectors.  For example, for the linear operator,
\[
\langle J' M' | T(E2,\mu) | J M \rangle
= \delta_{\mu, M'-M} \big( \langle J' || B^{\dagger} || J \rangle
   + (-1)^{J-M} \langle J' || \tilde{B} || J \rangle \text{ with appropriate factor} \dots \big).
\]
The required reduced matrix elements can be evaluated directly using the Fock‑space representation or by employing angular momentum algebra (Wigner–Eckart theorem).  Since the basis is small, a direct numerical calculation of the matrix elements in the \(m\)-scheme and subsequent extraction of the reduced matrix elements via the Wigner–Eckart theorem is straightforward.

**The required ratios**:
1. \(B(E2, 2' \to 0) / B(E2, 2 \to 0)\)
2. \(B(E2, 2' \to 2) / B(E2, 2 \to 0)\)
3. \(B(E2, 0' \to 2) / B(E2, 2 \to 0)\)
4. \(Q(2') / Q(2)\)  (the quadrupole moment ratio \(Q_{22}/Q_{20}\)).

All quantities are dimensionless.

## Reproduction target
Implement the complete quadrupole phonon model fitting procedure for ¹¹⁴Cd as described above, using the experimental \(2^{+}\) energies. From the fitted model, compute the anharmonic energies (in MeV) of the following seven states:

- \(2^{+}\), \(2'^{+}\), \(2''^{+}\)
- \(0'^{+}\), \(0''^{+}\)
- \(4^{+}\), \(4'^{+}\)

Write these as a CSV file with columns `state_label` and `energy_MeV` to `computed_energies.csv`.

Then, using the wavefunction expansion coefficients obtained from the fit and the E2 transition operator defined above, compute the four dimensionless ratios listed. Write the results to `electromagnetic_observables.csv` with columns `observable` and `value`.

All quantities must be derived from the fitted model; do not copy values from any external source.

## Assets
- Experimental \(2^{+}\) energy levels of ¹¹⁴Cd (provided in the text).
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Fit quadrupole phonon model to experimental 2⁺ energies
- Role: process
- Action: Implement the Hamiltonian matrix elements for the \(J=2\) block as described in Section 4.2, diagonalise the matrix, and use a numerical optimiser to fit the parameters \(\omega_0, w_2, w_3, w_4\) so that the three eigenvalues match the experimental \(2^{+}\) energies.  Then compute the \(J=0\) and \(J=4\) blocks, diagonalise, and obtain the full set of excited energies.  The fitting parameters are kept internally (no output file required).
- Evidence: (none; parameters are used in subsequent steps)

### Step 2: Compute anharmonic energy levels
- Role: scored (load-bearing)
- Action: Using the fitted phonon model from the previous step, produce the energies (in MeV) of the seven states specified above. Write the state labels and computed energies to `computed_energies.csv`.
- Output file: `/app/outputs/computed_energies.csv`
- Format: csv
- Contract: columns: `state_label` (string), `energy_MeV` (float); 7 rows with labels `2+`, `2'+`, `2''+`, `0'+`, `0''+`, `4+`, `4'+`.
- Scoring: scored by hidden verifier

### Step 3: Calculate electromagnetic observables
- Role: scored (load-bearing)
- Action: Using the wavefunction coefficients and the E2 transition operator defined in Section 6, compute the four required dimensionless ratios. Write the results to `electromagnetic_observables.csv` with one row per observable.
- Output file: `/app/outputs/electromagnetic_observables.csv`
- Format: csv
- Contract: columns: `observable` (string), `value` (float); rows: `B(E2,2'→0)/B(E2,2→0)`, `B(E2,2'→2)/B(E2,2→0)`, `B(E2,0'→2)/B(E2,2→0)`, `Q22/Q20`.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_energies.csv`
- `/app/outputs/electromagnetic_observables.csv`

## Output contract

(Content identical to the existing output contract in grading_spec, repeated for the agent’s convenience.)

### computed_energies.csv
- path: `/app/outputs/computed_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- schema:
  - `type`: table
  - `required_columns`: `state_label`, `energy_MeV`
  - `units`: `energy_MeV` in MeV
- description: Computed anharmonic energy levels for seven states in ¹¹⁴Cd.

### electromagnetic_observables.csv
- path: `/app/outputs/electromagnetic_observables.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- schema:
  - `type`: table
  - `required_columns`: `observable`, `value`
- description: Computed B(E2) ratios and quadrupole moment ratio for ¹¹⁴Cd.

Notes: The scorer compares the agent's computed values against hidden reference values from the original paper using tolerances (0.05 MeV for energies, 0.1 for B(E2) ratios, 0.2 for Q22/Q20). The fitting step must be executed; the scored steps are load-bearing.

## Self-check before finishing (optional, not scored)

(Content identical to the existing self-check block.)

```json
{
  "outputs": [
    {
      "file": "computed_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": ["state_label", "energy_MeV"],
        "units": {"energy_MeV": "MeV"},
        "description": "Each row contains a state label (string) and its computed energy (float in MeV)."
      },
      "description": "Computed anharmonic energy levels for seven states in 114Cd."
    },
    {
      "file": "electromagnetic_observables.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": ["observable", "value"],
        "description": "Each row contains an observable identifier (string) and its computed dimensionless value (float)."
      },
      "description": "Computed B(E2) ratios and quadrupole moment ratio for 114Cd."
    }
  ],
  "notes": "..."
}
```

## How you are scored
Each scored artifact is evaluated by an automated verifier that compares your computed values against expected reference values within prescribed tolerances.  For the energy levels, an absolute tolerance of 0.05 MeV is applied.  For the electromagnetic ratios, tolerances of 0.1 (B(E2) ratios) and 0.2 (Q22/Q20) are used.  The final reward is a weighted combination of how many of the required entries meet these tolerance criteria.  You must perform the fitting procedure described in the steps; directly copying values from the paper without performing the fit will not produce valid results, as the expected reference values assume a proper numerical fitting process.