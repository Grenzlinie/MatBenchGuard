# Floquet second‑order topological superconductor with periodically kicked mass term in a 2D topological insulator

## Problem background
This task investigates Floquet engineering of higher‑order topological superconductivity. We start from a two‑dimensional topological insulator proximitized with a \(d\)-wave superconductor. By applying a periodic kicking drive to the onsite mass term, the system is driven out of equilibrium. The interplay between dynamical time‑reversal‑symmetry breaking (from the drive) and an externally applied in‑plane Zeeman field can induce Floquet second‑order topological superconducting phases. The key signatures of these phases are zero‑energy Majorana corner modes and quantized topological invariants—the Floquet Wannier spectrum and Floquet quadrupole moment. The task is to construct the relevant Floquet operator, diagonalize it, and compute the quasienergy spectrum and these invariants for two Zeeman field amplitudes. The results will reveal whether the resulting phase is a weak or strong Floquet second‑order topological superconductor.

## Model – Bogoliubov‑de Gennes Hamiltonian

The system is described by the static Bogoliubov‑de Gennes (BdG) Hamiltonian on a square lattice:

```
H_BdG = 1/2 Σ_k Ψ_k^† H_0(k) Ψ_k
```

with the Nambu spinor (for momentum **k**) ordered as

```
Ψ_k = (c_{k,a↑}, c_{-k,a↑}^†, c_{k,a↓}, c_{-k,a↓}^†, c_{k,b↑}, c_{-k,b↑}^†, c_{k,b↓}, c_{-k,b↓}^†)^T .
```

The **8 × 8** Bloch Hamiltonian is

```
H_0(k) = ε(k) Γ₁ + λ_x sin k_x Γ₂ + λ_y sin k_y Γ₃ + Δ(k) Γ₄ + B_x Γ₅ ,
```

where

```
ε(k) = m₀ – t_x cos k_x – t_y cos k_y ,
Δ(k) = Δ₀ (cos k_x – cos k_y) ,
```

and the five Dirac matrices are (Kronecker products of Pauli matrices)

```
Γ₁ = σ_z ⊗ τ_z ,
Γ₂ = σ_x ⊗ s_z ⊗ τ_0 ,   but in the BdG basis we write Γ₂ = σ_x s_z (identity in τ implied)  → σ_x s_z
Γ₃ = σ_y ⊗ τ_z ,
Γ₄ = s_y ⊗ τ_y ,
Γ₅ = s_x ⊗ τ_z .
```

The Pauli matrices **σ** (upper‑script, orbital), **s** (middle, spin) and **τ** (lower, particle‑hole) act on the orbital (a,b), spin (↑,↓) and particle‑hole spaces respectively.  
Explicitly, the ordering inside the 8‑dimensional state is (spin ↑,↓ for each orbital and each particle‑hole sector). The direct‑product structure is:

- σ matrices act on orbital (a,b) (index 0)
- s matrices act on spin (↑,↓) (index 1)
- τ matrices act on particle‑hole (index 2)

Therefore, for any matrix **A** appearing above, one should take the Kronecker product with the required identity matrices to fill the 8‑dimensional space. The standard basis for the Kronecker product is: orbital ⊗ spin ⊗ particle‑hole.  
In that basis the matrices become:

```
Γ₁ = σ_z ⊗ 1_2 ⊗ τ_z
Γ₂ = σ_x ⊗ s_z ⊗ 1_2
Γ₃ = σ_y ⊗ 1_2 ⊗ τ_z
Γ₄ = 1_2 ⊗ s_y ⊗ τ_y
Γ₅ = 1_2 ⊗ s_x ⊗ τ_z
```

with each Pauli matrix normalised as usual.

## Driving protocol and Floquet operator

The onsite mass term is periodically kicked:

```
m(t) = m₁ Σ_{r=1}^{∞} δ(t – r T) ,
```

where T is the driving period and m₁ the kick amplitude.  
The exact Floquet evolution operator over one period factorises as

```
U(T) = exp(–i H_0(k) T) · exp(–i m₁ Γ₁) .
```

In real‑space open boundary conditions (OBC) we replace **k**‑dependent functions by their tight‑binding forms.
For the square lattice with sites (x,y) (x,y = 1,…,L):

- cos k_x → ½ (δ_{x+1,x´} + δ_{x-1,x´}) ⊗ δ_{y,y´}
- sin k_x → –i/2 (δ_{x+1,x´} – δ_{x-1,x´}) ⊗ δ_{y,y´}
(and similarly for k_y).

Consequently the full real‑space Hamiltonian `H0` is a **(8*L^2) × (8*L^2)** sparse matrix (L=25, 8 orbitals per site) built by placing the appropriate 8 × 8 block hopping matrices on each bond.  
The Floquet operator is then simply

```
U = expm(–1j * H0 * T) @ expm(–1j * m1 * Γ1_full)
```

where `Γ1_full` is the 8 × 8 Γ₁ block on each site (no hopping).

**Parameters to use:**

| symbol | value  | description                     |
|--------|--------|---------------------------------|
| t_x, t_y  | 1.0  | nearest‑neighbour hopping       |
| λ_x, λ_y  | 1.0  | spin‑orbit coupling              |
| m₀        | 2.5  | crystal‑field splitting          |
| Δ₀        | 0.6  | d‑wave pairing amplitude         |
| m₁        | –0.4 | kick amplitude                   |
| T         | 0.419| driving period                   |
| B_x       | 0.0 and 0.3 | Zeeman field (two cases) |

Lattice size: Lx = Ly = 25 (→ 5000 degrees of freedom).

## Effective high‑frequency Floquet Hamiltonian (for Wannier spectrum)

In the high‑frequency limit (T → 0, m₁ → 0) the effective time‑independent Hamiltonian is given by Eq. (6) of the paper:

```
H_Flq^eff(k) ≈ H_0(k) + (m₁/T) Γ₁ + m₁ Σ_{j=2}^{5} r_j(k) Γ_{j1} ,
```

with

```
r_j(k) = N_j(k) / |N(k)| ,
|N(k)| = ( Σ_{j=1}^{5} N_j(k)^2 )^{1/2} ,
```

where `N_j(k)` are the coefficients in front of the Γ matrices:

```
N₁(k) = ε(k)        (coefficient of Γ₁)
N₂(k) = λ_x sin k_x  (coefficient of Γ₂)
N₃(k) = λ_y sin k_y  (coefficient of Γ₃)
N₄(k) = Δ(k)         (coefficient of Γ₄)
N₅(k) = B_x          (coefficient of Γ₅) .
```

The commutator‑based matrices are

```
Γ_{j1} = (1/(2i)) [Γ_j, Γ₁] ,   j = 2,3,4,5 .
```

For the slab geometry (OBC along x, PBC along y) we discretise k_y ∈ [–π,π) with sufficiently many points (e.g. 101).  
At each k_y the effective Hamiltonian is an 8·Lx × 8·Lx matrix constructed using the same tight‑binding hopping rules for the k_x terms and treating the k_y‑dependent factors (cos k_y, sin k_y) as c‑numbers.

## Floquet Wannier spectrum computation

1. Choose a slab: open boundary in x (Lx=25 sites) and periodic boundary in y. For each discrete k_y, construct the effective Hamiltonian `H_Flq^eff(k_y)` (use the high‑frequency form given above) and diagonalise it.
2. Identify the *occupied* Floquet bands: those eigenstates whose quasienergy is ≤ 0. (The number N_occ is half of the total dimension, i.e. 4·Lx = 100 bands.)
3. Form the matrix `U_occ(k_y)` whose columns are the occupied eigenvectors at k_y.  
   Compute the overlap matrix between neighbouring k_y points:

   ```
   F_{mn}(k_y) = [U_occ^†(k_y + δk_y) · U_occ(k_y)]_{mn} .
   ```

4. The Wilson‑loop operator along the periodic direction is the ordered product over the k_y loop:

   ```
   W_y = Π_{k_y} F(k_y)   (starting from k_y=–π to π–δk_y).
   ```

   (Take care of the phase convention: use the same gauge for the eigenvectors across the loop.)
5. Diagonalise `W_y`; extract the phases θ_i = –i log λ_i (where λ_i are the eigenvalues of W_y). The **Floquet Wannier spectrum** is ν_i = θ_i / (2π) taken modulo 1, so that ν_i ∈ [0,1).

## Floquet quadrupole moment computation

The Floquet quadrupole moment is evaluated from the *exact* Floquet operator (not the effective Hamiltonian) using the many‑body ground state.  
Procedure (following the paper, Sec. II E):

1. Diagonalise the full OBC Floquet operator `U(T)` (from Step 1) for Lx=Ly=25. Obtain all eigenvectors and quasienergies.
2. Form the **many‑body ground state** by occupying all single‑particle Floquet states with quasienergy ≤ 0. (Because of particle‑hole symmetry, exactly half of the 5000 states satisfy this condition, giving N_occ = 2500.)
3. Create the **projector matrix** P onto the occupied subspace. If `V` is the 5000 × 2500 matrix whose columns are the occupied eigenvectors, then P = V·V^†.
4. Define the **position‑operator phase** matrix

   ```
   q = diag( exp( i 2π (x · y) / (Lx·Ly) ) ) ,
   ```
   where the site index runs over all lattice points with coordinates x,y ∈ {1,…,25}. (The exponential acts as the identity in orbital/spin/particle‑hole space, i.e. the same scalar is repeated for all 8 internal degrees of freedom on that site. Thus q is an 5000 × 5000 diagonal matrix.)
5. Compute

   ```
   Q_xy^Flq = (1/(2π)) Im log det[ V^† q V ]   (mod 1) .
   ```

   The result should be taken modulo 1 to obtain a value in [0,1).

   **Numerical note:** For a diagonal q the determinant can be calculated efficiently by forming the 2500 × 2500 matrix `V^† q V` and using `numpy.linalg.slogdet`.

## Reproduction target

Compute, for B_x = 0 and B_x = 0.3, the exact Floquet quasienergy spectrum on a 25×25 lattice with the parameters listed above. Save the sorted quasienergies to `quasienergy_bx0.json` and `quasienergy_bx03.json`. Construct the effective high‑frequency Floquet Hamiltonian in a slab geometry and compute the Floquet Wannier spectrum eigenvalues; save them to `fws.json` under keys `Bx0` and `Bx03`. Using the exact Floquet eigenstates in full OBC, compute the Floquet quadrupole moment modulo 1 and save the two values to `fqm.json`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Build Floquet evolution operators
- Role: process
- Action: Implement the tight‑binding Bogoliubov‑de Gennes Hamiltonian for the 2D square lattice with open boundary conditions (Lx=Ly=25) including the d‑wave pairing term and the periodic mass‑kick drive. Construct the two exact Floquet evolution operator matrices U(T) = exp(–i H0 T) exp(–i m1 Γ1) for B_x = 0 and B_x = 0.3. The operators are 5000×5000 sparse matrices. Store them for the subsequent diagonalisations.
- Evidence: The matrices are kept in memory; no separate checkpoint file is required as a scored output.

### Step 2: Floquet quasienergy spectrum for B_x = 0
- Role: scored (load‑bearing)
- Action: Diagonalise the Floquet operator U(T) for B_x = 0. Extract the Floquet quasienergies μ_m (taking the principal logarithm). Save the full **sorted** list of quasienergies to `/app/outputs/quasienergy_bx0.json`.
- Output file: `/app/outputs/quasienergy_bx0.json`
- Format: json
- Contract: JSON array of real numbers (length 5000)
- Scoring: scored by hidden verifier

### Step 3: Floquet quasienergy spectrum for B_x = 0.3
- Role: scored
- Action: Diagonalise the Floquet operator U(T) for B_x = 0.3. Save the **sorted** quasienergies to `/app/outputs/quasienergy_bx03.json`.
- Output file: `/app/outputs/quasienergy_bx03.json`
- Format: json
- Contract: JSON array of real numbers (length 5000)
- Scoring: scored by hidden verifier

### Step 4: Floquet Wannier spectrum
- Role: scored
- Action: Build the effective high‑frequency Floquet Hamiltonian in a slab geometry (open along x, 25 sites; periodic along y). Follow the method described above: discretise k_y, diagonalise the effective Hamiltonian, keep the occupied bands, construct the Wilson‑loop operator along k_y, compute its eigenvalues and convert to Wannier centres ν ∈ [0,1). Repeat for both B_x = 0 and B_x = 0.3. Save as a JSON object at `/app/outputs/fws.json` with keys `'Bx0'` and `'Bx03'`, each mapping to an array of eigenvalues.
- Output file: `/app/outputs/fws.json`
- Format: json
- Contract: JSON object with keys `'Bx0'` and `'Bx03'`, each an array of real numbers in [0,1)
- Scoring: scored by hidden verifier

### Step 5: Floquet quadrupole moment
- Role: scored
- Action: Using the exact Floquet operator eigenstates from the full OBC diagonalisations (Step 2/3), construct the many‑body ground state (all quasienergies ≤ 0) and compute the Floquet quadrupole moment Q_{xy}^{Flq} modulo 1 as described above. Perform for B_x = 0 and B_x = 0.3. Save the two results as a JSON object at `/app/outputs/fqm.json` with keys `'Bx0'` and `'Bx03'`, each a single real number.
- Output file: `/app/outputs/fqm.json`
- Format: json
- Contract: JSON object with keys `'Bx0'` and `'Bx03'`, each a single real number
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/quasienergy_bx0.json`
- `/app/outputs/quasienergy_bx03.json`
- `/app/outputs/fws.json`
- `/app/outputs/fqm.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### quasienergy_bx0.json
- path: `/app/outputs/quasienergy_bx0.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Floquet quasienergy spectrum for B_x = 0. The checker will count the number of quasienergies with |μ| < 1e‑5 and compare it to the expected count for this phase.
- schema:
  - `type`: array
  - `items`:
    - `type`: number
  - `required`:
  - `description`: Sorted list of 5000 real Floquet quasienergies.

### quasienergy_bx03.json
- path: `/app/outputs/quasienergy_bx03.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Floquet quasienergy spectrum for B_x = 0.3. The checker will count the number of quasienergies with |μ| < 1e‑5 and compare it to the expected count for this phase.
- schema:
  - `type`: array
  - `items`:
    - `type`: number
  - `required`:
  - `description`: Sorted list of 5000 real Floquet quasienergies.

### fws.json
- path: `/app/outputs/fws.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Floquet Wannier spectrum eigenvalues for the two phases. The checker will count the number of eigenvalues near 0.5 (within a small tolerance) and compare it to the expected topological signature.
- schema:
  - `type`: object
  - `required`:
    - `Bx0`: array of real numbers
    - `Bx03`: array of real numbers
  - `items`:
    - `Bx0`:
      - `type`: array
      - `items`:
        - `type`: number
    - `Bx03`:
      - `type`: array
      - `items`:
        - `type`: number
  - `description`: Floquet Wannier spectrum eigenvalues, each array containing real numbers in [0,1).

### fqm.json
- path: `/app/outputs/fqm.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Floquet quadrupole moment for the two phases. The checker will verify that each value is within a small tolerance of the expected quantised value.
- schema:
  - `type`: object
  - `required`:
    - `Bx0`: single real number
    - `Bx03`: single real number
  - `items`:
    - `Bx0`:
      - `type`: number
    - `Bx03`:
      - `type`: number
  - `description`: Floquet quadrupole moment values modulo 1.

Notes: Outputs cover the 2D FSOTSC core: quasienergy/Majorana corner modes and topological invariants. The checker validates discrete structural signatures against paper‑derived thresholds.

## Self‑check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "quasienergy_bx0.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "number"
        },
        "required": [],
        "description": "Sorted list of 5000 real Floquet quasienergies."
      },
      "description": "Floquet quasienergy spectrum for B_x=0. The checker will count the number of quasienergies with |μ| < 1e-5 and compare it to the expected count for this phase."
    },
    {
      "file": "quasienergy_bx03.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "number"
        },
        "required": [],
        "description": "Sorted list of 5000 real Floquet quasienergies."
      },
      "description": "Floquet quasienergy spectrum for B_x=0.3. The checker will count the number of quasienergies with |μ| < 1e-5 and compare it to the expected count for this phase."
    },
    {
      "file": "fws.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Bx0": "array of real numbers",
          "Bx03": "array of real numbers"
        },
        "items": {
          "Bx0": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "Bx03": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        },
        "description": "Floquet Wannier spectrum eigenvalues, each array containing real numbers in [0,1)."
      },
      "description": "Floquet Wannier spectrum eigenvalues for the two phases. The checker will count the number of eigenvalues near 0.5 (within a tolerance) and compare to the expected topological signature."
    },
    {
      "file": "fqm.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Bx0": "single real number",
          "Bx03": "single real number"
        },
        "items": {
          "Bx0": {
            "type": "number"
          },
          "Bx03": {
            "type": "number"
          }
        },
        "description": "Floquet quadrupole moment values modulo 1."
      },
      "description": "Floquet quadrupole moment for the two phases. The checker will verify that the value is within a tolerance of the expected quantised value."
    }
  ],
  "notes": "Outputs cover the 2D FSOTSC core: quasienergy/Majorana corner modes and topological invariants. The checker validates discrete structural signatures against paper-derived thresholds."
}
```