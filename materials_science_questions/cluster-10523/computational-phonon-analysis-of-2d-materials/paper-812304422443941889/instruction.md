# Phonon Dispersion in Distorted 2D Peierls Phase

## Problem background
The Peierls phase in a two-dimensional (2D) half-filled square-lattice Su-Schrieffer-Heeger (SSH) model exhibits static lattice distortions with multiple wavevectors parallel to the nesting vector Q=(π,π). Different distortion patterns—different combinations of Fourier components—can have the same ground-state energy but modify the Brillouin zone, leading to distinct phonon branch structures and gap positions. This task investigates the phonon dispersion (squared frequencies ω² as a function of wavevector q) at zero temperature for two such distortion patterns.

## Model and parameters
The 2D SSH Hamiltonian on an N×N square lattice (periodic boundary conditions) is:

$$
\begin{aligned}
H = & -\sum_{i,j,s} \Big\{ \big[t_0 - \alpha (u_x(i+1,j)-u_x(i,j))\big] (c_{i+1,j,s}^\dagger c_{i,j,s} + c_{i,j,s}^\dagger c_{i+1,j,s}) \Big. \\
    & \Big. + \big[t_0 - \alpha (u_y(i,j+1)-u_y(i,j))\big] (c_{i,j+1,s}^\dagger c_{i,j,s} + c_{i,j,s}^\dagger c_{i,j+1,s}) \Big\} \\
    & + \frac{K}{2} \sum_{i,j} \big[ (u_x(i+1,j)-u_x(i,j))^2 + (u_y(i,j+1)-u_y(i,j))^2 \big] \\
    & + \frac{M}{2} \sum_{i,j} \big[ \dot{u}_x(i,j)^2 + \dot{u}_y(i,j)^2 \big] .
\end{aligned}
$$

Adopt the following numerical values (natural units):

- Transfer integral \( t_0 = 1 \)
- Lattice force constant \( K = 1 \)
- Ion mass \( M = 1 \)
- Electron‑lattice coupling \( \alpha = \sqrt{0.65} \approx 0.8062 \) (so that the dimensionless coupling \( \lambda \equiv \frac{\alpha^2}{K t_0} = 0.65 \)).

Lattice distortion is encoded in bond variables  
\( x_{\boldsymbol{r}} = u_x(\boldsymbol{r}+\boldsymbol{e}_x) - u_x(\boldsymbol{r}) \),  
\( y_{\boldsymbol{r}} = u_y(\boldsymbol{r}+\boldsymbol{e}_y) - u_y(\boldsymbol{r}) \).

The static Peierls distortions are taken to contain only Fourier components with wavevectors parallel to \( \boldsymbol{Q}=(\pi,\pi) \). Two patterns are studied:

- **Pattern (a)**: components with wavevectors \( \boldsymbol{Q} \) and \( \boldsymbol{Q}/2 \).
- **Pattern (b)**: components with wavevectors \( \boldsymbol{Q} \), \( \boldsymbol{Q}/4 \), and \( 3\boldsymbol{Q}/4 \).

Correspondingly the distortion fields are parameterised as  
\( x_{\boldsymbol{r}} = x_Q (-1)^{i+j} + \big[ x_{Q/2} e^{i\boldsymbol{Q}/2 \cdot \boldsymbol{r}} + \text{c.c.} \big] \) (and analogously for \( y_{\boldsymbol{r}} \)) for pattern (a), while for pattern (b)

\( x_{\boldsymbol{r}} = x_Q (-1)^{i+j} + \big[ x_{Q/4} e^{i\boldsymbol{Q}/4 \cdot \boldsymbol{r}} + x_{3Q/4} e^{i 3\boldsymbol{Q}/4 \cdot \boldsymbol{r}} + \text{c.c.} \big] \) (and analogously for \( y_{\boldsymbol{r}} \)).

Here \( x_q, y_q \) are complex Fourier amplitudes; the system size N is taken even and the Bravais lattice vectors are \( \boldsymbol{e}_x=(1,0), \boldsymbol{e}_y=(0,1) \).

Substituting these expressions into the static electronic part of \( H \) yields the momentum‑space representation (see Eq. (2.4) of the paper):

$$
\begin{aligned}
H_{\text{el}} = & \sum_{\boldsymbol{k},s} \epsilon_{\boldsymbol{k}} c_{\boldsymbol{k},s}^\dagger c_{\boldsymbol{k},s}
+ \alpha \sum_{\boldsymbol{k},s} 2i \big( x_Q \sin k_x + y_Q \sin k_y \big) c_{\boldsymbol{k}+\boldsymbol{Q},s}^\dagger c_{\boldsymbol{k},s} \\
& + \alpha \sum_{q \in S} \sum_{\boldsymbol{k},s} 2\Big\{ e^{-i q/2}\big[ x_q \cos(k_x+\tfrac{q}{2}) + y_q \cos(k_y+\tfrac{q}{2}) \big] c_{\boldsymbol{k}+\boldsymbol{q},s}^\dagger c_{\boldsymbol{k},s} \\
& \qquad\qquad\qquad +\, e^{i q/2}\big[ x_q^* \cos(k_x-\tfrac{q}{2}) + y_q^* \cos(k_y-\tfrac{q}{2}) \big] c_{\boldsymbol{k}-\boldsymbol{q},s}^\dagger c_{\boldsymbol{k},s} \Big\}
\end{aligned}
$$

with \( \epsilon_{\boldsymbol{k}} = -2t_0 (\cos k_x + \cos k_y) \), \( S = \{Q/2\} \) for pattern (a) and \( S = \{Q/4, 3Q/4\} \) for pattern (b).

The lattice elastic energy is

\[
E_{\text{latt}} = N^2 \frac{K}{2} \big( |x_Q|^2+|y_Q|^2 \big) + N^2 K \sum_{q\in S} \big( |x_q|^2+|y_q|^2 \big) .
\]

## Approach – overview
You will implement the self‑consistent solution of the electronic structure for the two distortion patterns on a \( 64\times 64 \) lattice at \( T=0 \) and \( \lambda=0.65 \), then construct the phonon dynamical matrix and obtain the squared phonon frequencies \( \omega^2 \) along the diagonal \( \boldsymbol{q}=(q,q) \) in the reduced Brillouin zone.

---

## Workflow steps

### Step 1: Solve static Peierls distortions and electronic structure
- **Role:** process
- **Action:** For each pattern (a) and (b), self‑consistently determine the complex Fourier amplitudes \( x_Q, y_Q, x_q, y_q \) and the electronic eigenstates by minimising the total energy.  
  Use the group‑index formulation explained below: because the Hamiltonian couples only wavevectors that differ by vectors parallel to \( \boldsymbol{Q} \), the electronic Hilbert space splits into \( N \) independent groups labelled by an offset \( p \in [0,2\pi) \). For a given group \( p \), the basis consists of plane waves \( |\boldsymbol{k}_{n,p}\rangle \) with \( \boldsymbol{k}_{n,p} = (k_n, k_n+p) \), \( k_n = 2\pi n/N \), \( n = -N/2+1,\dots,N/2 \) (folded into the first Brillouin zone). The Hamiltonian within each group is a \( N\times N \) matrix whose elements follow from the momentum‑space representation above.  
  Initialise the amplitudes with small random values, diagonalise the group Hamiltonians to obtain electron eigenenergies \( \varepsilon_{u,p} \) and eigenfunctions \( \phi_{u,p}(\boldsymbol{r}) = \frac{1}{N} \sum_n A_{u,p}(k_n) e^{i\boldsymbol{k}_{n,p}\cdot\boldsymbol{r}} \).  
  Compute the total energy \( E_{\text{tot}} = \sum_{u,p} f(\varepsilon_{u,p})\varepsilon_{u,p} + E_{\text{latt}} \) (with \( f \) the Fermi function at \( T=0 \)), then update the amplitudes by gradient descent or a similar relaxation scheme until convergence (energy change \( < 10^{-10} \) and gradient norm small). The ground state is highly degenerate; any converged set of amplitudes that satisfies the pattern constraints is acceptable.

### Step 2: Build phonon dynamical matrices
- **Role:** process
- **Action:** For each converged static state, construct the phonon dynamical matrix in the reduced‑zone framework, focusing on the group index \( q' = 0 \).  
  The linear mode frequencies for a phonon wavevector \( \boldsymbol{q}' \) (both components \( q_x=q_y=q' \)) are obtained from the eigenvalue problem  

  \[
  M \omega^2 \, \delta \tilde{u}_a(\boldsymbol{q}') = \sum_b D_{ab}(\boldsymbol{q}') \, \delta \tilde{u}_b(\boldsymbol{q}'),
  \]

  where \( a,b \in \{x,y\} \) and the \( 2N\times 2N \) matrix \( D_{ab}(\boldsymbol{q}') \) (for a given \( q' \)) has elements labelled by the \( N \) wavevectors \( k_n \) within the group. The explicit construction proceeds as follows:

  1. **Lattice part** – diagonal spring term:
     \[
     D_{ab}^{\text{lat}}(n,m) = \delta_{ab}\,\delta_{nm}\, \frac{2K}{M}\big(1-\cos k_n\big) .
     \]

  2. **Electronic polarisation** – for the phonon at \( q' \), compute
     \[
     \Pi_{ab}(n,m) = \frac{2\alpha^2}{M} \sum_{p} \sum_{u,v} \frac{f(\varepsilon_{u,p}) - f(\varepsilon_{v,p+q'})}
     {\varepsilon_{u,p} - \varepsilon_{v,p+q'}} 
     \, J_{u,p;v,p+q'}^{a}(k_n) \; \big[ J_{u,p;v,p+q'}^{b}(k_m) \big]^* .
     \]
     The current matrix elements are derived from the electron‑phonon vertex in the momentum‑space Hamiltonian:
     \[
     \begin{aligned}
     J_{u,p;v,p+q'}^{x}(k_n) &= \sum_{l} A_{u,p}^*(k_l) \, A_{v,p+q'}(k_l+q') \; \times \\
     &\quad \Big[ 2i \sin\!\big(k_l + \tfrac{q'}{2}\big) \, \delta_{k_l + \tfrac{q'}{2}, k_n} 
              + 2i \sin\!\big(k_l - \tfrac{q'}{2}\big) \, \delta_{k_l - \tfrac{q'}{2}, k_n} \Big] , \\
     J_{u,p;v,p+q'}^{y}(k_n) &= \sum_{l} A_{u,p}^*(k_l) \, A_{v,p+q'}(k_l+q') \; \times \\
     &\quad \Big[ 2i \sin\!\big(k_l+p + \tfrac{q'}{2}\big) \, \delta_{k_l+p + \tfrac{q'}{2}, k_n+p} 
              + 2i \sin\!\big(k_l+p - \tfrac{q'}{2}\big) \, \delta_{k_l+p - \tfrac{q'}{2}, k_n+p} \Big] .
     \end{aligned}
     \]
     (Only terms that survive the Kronecker deltas contribute.)  

  3. **Full matrix** – \( D_{ab}(n,m) = D_{ab}^{\text{lat}}(n,m) + \Pi_{ab}(n,m) \).

  For this task you only need the matrix with \( q' = 0 \).

### Step 3: Output phonon dispersion for pattern (a)
- **Role:** scored (load‑bearing)
- **Action:** Diagonalise the dynamical matrix \( D(q') \) for \( q' = 0, \dots, N/4 \) (all values are \( q = q' \times N/(2\pi) \) integers). For each \( q' \), sort the eigenvalues \( \omega^2 \) in ascending order and write them to `dispersion_pattern_a.csv`.
- **Output file:** `/app/outputs/dispersion_pattern_a.csv`
- **Format:** csv
- **Contract:** A CSV file with header `q` followed by columns `omega2_0`, `omega2_1`, … up to the number of branches for the pattern. The columns are sorted in ascending order of squared frequency. `q` is an integer giving \( q' \times N/(2\pi) \). All `omega2_i` are floats.
- **Scoring:** scored by hidden verifier

### Step 4: Output phonon dispersion for pattern (b)
- **Role:** scored (load‑bearing)
- **Action:** Diagonalise the dynamical matrix for \( q' = 0, \dots, N/8 \) (integers), sort eigenvalues, and write them to `dispersion_pattern_b.csv`.
- **Output file:** `/app/outputs/dispersion_pattern_b.csv`
- **Format:** csv
- **Contract:** As for pattern (a): header `q` then `omega2_0`, `omega2_1`, … sorted ascending. `q` is integer.
- **Scoring:** scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_pattern_a.csv`
- `/app/outputs/dispersion_pattern_b.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_pattern_a.csv
- path: `/app/outputs/dispersion_pattern_a.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion for pattern (a). Used to verify branch count and gap positions.
- schema:
  - `type`: table
  - `columns`:
    - `name`: q
    - `type`: integer
    - `name_pattern`: omega2_\d+
    - `type`: float
    - `sorted`: True

### dispersion_pattern_b.csv
- path: `/app/outputs/dispersion_pattern_b.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion for pattern (b). Used to verify branch count and gap positions.
- schema:
  - `type`: table
  - `columns`:
    - `name`: q
    - `type`: integer
    - `name_pattern`: omega2_\d+
    - `type`: float
    - `sorted`: True

Notes: The checker parses the header to determine the number of `omega2` columns (branch count) and then performs a structural audit (branch count, zero modes at \(\Gamma\), and phonon gaps). The contract does not prescribe a fixed number of columns.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists and CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_pattern_a.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "columns": [
          { "name": "q", "type": "integer" },
          { "name_pattern": "omega2_\\d+", "type": "float", "sorted": true }
        ]
      }
    },
    {
      "file": "dispersion_pattern_b.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "columns": [
          { "name": "q", "type": "integer" },
          { "name_pattern": "omega2_\\d+", "type": "float", "sorted": true }
        ]
      }
    }
  ]
}
```

## How you are scored
A hidden verifier independently examines each output CSV. It checks structural properties of the dispersion that are physically determined by the model for each pattern:

- Correct number of phonon branches (i.e. the number of `omega