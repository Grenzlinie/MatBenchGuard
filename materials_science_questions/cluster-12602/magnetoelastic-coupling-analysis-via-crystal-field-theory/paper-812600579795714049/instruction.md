# Compute third-order magnetic susceptibility from crystal-field theory

## Problem background
In cubic rare-earth intermetallic compounds, the magnetization in the paramagnetic regime is influenced not only by the crystal electric field (CEF) and Heisenberg (bilinear) exchange, but also by quadrupolar interactions—magnetoelastic coupling and quadrupolar exchange between the 4f ions. The usual first-order magnetic susceptibility χ_M^(1) is isotropic in the cubic phase and depends only on bilinear exchange, but the third-order susceptibility χ_M^(3), which characterizes the curvature of the magnetization curve, becomes anisotropic and receives a direct contribution from the induced quadrupolar moment. This makes χ_M^(3) a sensitive probe of both tetragonal (G₁) and trigonal (G₂) quadrupolar couplings.

In this task you will compute χ_M^(1) and χ_M^(3) from first principles using the analytical mean-field expressions that follow from perturbation theory, for a given set of CEF parameters, bilinear exchange strength, and quadrupolar coefficients.

## Theory

### 1. Physical constants and ion properties
We consider a Tm³⁺ ion with total angular momentum **J = 6** and Landé factor

**g_J = 7/6.**

The Bohr magneton and Avogadro’s number are
μ_B = 9.274009 × 10⁻²¹ emu,
N_A = 6.02214076 × 10²³ mol⁻¹.

All energies are expressed in **kelvin** (K).  Temperature *T* is also in kelvin; hence the inverse temperature is β = 1/T.  The Boltzmann constant *k*_B is absorbed into the energy scale.

### 2. Crystal‑field Hamiltonian (Lea–Leask–Wolf form)
In the |J,M_J⟩ basis (*M_J* = +J,…,−J) the cubic CEF Hamiltonian is constructed from the fourth‑ and sixth‑order Stevens operators.  For a total angular momentum **J = 6** the Lea‑Leask‑Wolf parameters are

**W** (energy scale, K), **x** (−1 ≤ x ≤ 1).

The Hamiltonian reads

```
H_CEF = W [ x · O₄/F₄  +  (1 − |x|) · O₆/F₆ ]
```

with the cubic operator combinations

```
O₄ = O₄⁰ + 5 O₄⁴
O₆ = O₆⁰ − 21 O₆⁴
```

and the **normalisation constants** for J = 6:

**F₄ = 60,   F₆ = 2520.**

The required Stevens operators in the |J,M_J⟩ basis are:

- J_z :  (J_z)_{M,M'} = M δ_{M,M'}
- J_+, J_− : the standard raising/lowering operators
- O₂⁰ = 3 J_z² – J(J+1)  
- O₄⁰ = 35 J_z⁴ – [30 J(J+1) – 25] J_z² + [3 J²(J+1)² – 6 J(J+1)]  
- O₄⁴ = ½ (J_+⁴ + J_−⁴)  
- O₆⁰ = 231 J_z⁶ – [315 J(J+1) – 735] J_z⁴  
        + [105 J²(J+1)² – 525 J(J+1) + 294] J_z²  
        – [5 J³(J+1)³ – 40 J²(J+1)² + 60 J(J+1)]  
- O₆⁴ = ¼ (J_+⁴ + J_−⁴) (11 J_z² – J(J+1) – 38)

(All operators are expressed as (2J+1)×(2J+1) matrices.)

### 3. Diagonalisation and matrix elements for the [001] direction
Diagonalise H_CEF to obtain the eigen‑energy states

|i⟩  with  energy *E_i*   (i = 1,…,13 for J=6).

In the same eigenbasis compute the matrix elements of

- **J_z**  →  (J_z)_{ij} = ⟨i| J_z |j⟩
- **O₂⁰**   →  Q_{ij}   = ⟨i| O₂⁰ |j⟩

All matrix elements are complex numbers; use real parts where appropriate (expect real diagonal elements).

### 4. Pure‑CEF susceptibilities (Appendix A of the paper)
Define the Boltzmann weights at temperature *T* (K):

p_i = e^{−β E_i} / Z,   Z = Σ_j e^{−β E_j},   β = 1/T.

From the eigenvalues and the matrix elements (J_z)_{ij} and Q_{ij} the four CEF‑only susceptibilities are computed by the following perturbation‑theory sums.

---

**First‑order magnetic susceptibility**  χ₀^(1)

```
S₁ = Σ_i p_i [ −2 Σ_{j≠i} |(J_z)_{ij}|² / (E_j – E_i)  +  β |(J_z)_{ii}|² ]
χ₀^(1) = (g_J² μ_B² N_A) S₁      (emu/mol)
```

*χ₀^(1) is isotropic in cubic symmetry; the same value applies for both [001] and [111] directions.*

---

**Strain susceptibility**  χ₂

```
S₂ = Σ_i p_i [ −2 Σ_{j≠i} |Q_{ij}|² / (E_j – E_i)  +  β |Q_{ii}|² ]
χ₂ = S₂                          (dimensionless, units of K⁻¹)
```

*χ₂ is not multiplied by g_J² μ_B² N_A because it characterises the response of the quadrupolar operator to strain in energy units K.*

---

**Quadrupolar‑field susceptibility**  χ₂^(2)

```
S₂₂ = Σ_i p_i [ … (triple sum) … ]
```

Explicitly:

```
S₂₂ = Σ_i p_i { 
        Σ_{j≠i} Σ_{k≠i}  [ (J_z)_{ij} Q_{jk} (J_z)_{ki} + 2 Q_{ij} (J_z)_{jk} (J_z)_{ki} ] / [(E_i–E_j)(E_i–E_k)]
      + Σ_{j≠i} [ −( |(J_z)_{ij}|² Q_{ii} + 2 Q_{ij} (J_z)_{ji} (J_z)_{ii} ) / (E_i–E_j) ] × (1/(E_i–E_j) + β)
      + ½ β² |(J_z)_{ii}|² Q_{ii}
    }
χ₂^(2) = (g_J² μ_B² N_A) S₂₂    (units of emu·mol⁻¹·K⁻¹)
```

---

**Third‑order CEF magnetic susceptibility**  χ₀^(3)

```
χ₀^(3) = −½ β [χ₀^(1)]² + (g_J⁴ μ_B⁴ N_A) Σ_i p_i T_i
```

where the term *T_i* collects the fourth‑order perturbation contributions:

```
T_i = 
   Σ_{j≠i} Σ_{k≠i} Σ_{l≠i} [ −4 (J_z)_{ij} (J_z)_{jk} (J_z)_{kl} (J_z)_{li} / ((E_i–E_j)(E_i–E_k)(E_i–E_l)) ]
 + Σ_{j≠i} Σ_{k≠i} [ 2( |(J_z)_{ij}|² |(J_z)_{ik}|² + 2 (J_z)_{ij} (J_z)_{jk} (J_z)_{ki} (J_z)_{ii} ) / ((E_i–E_j)(E_i–E_k)) ] × (2/(E_i–E_j) + β)
 + Σ_{j≠i} [ −2 |(J_z)_{ii}|² |(J_z)_{ij}|² / (E_i–E_j) ] × ( 2/(E_i–E_j)² + 2/((E_i–E_j)T) + 1/T² )
 + (1/(6 T³)) |(J_z)_{ii}|⁴
```

*Once multiplied by g_J⁴ μ_B⁴ N_A and combined with the −½β[χ₀^(1)]² term, χ₀^(3) has units of emu·mol⁻¹·Oe⁻³ (because M = χ₀^(1) H + χ₀^(3) H³ with H in Oe).*

---

### 5. Rotation to the [111] direction (Appendix B)
To handle the magnetic field applied along [111], the coordinate system is rotated so that the new z' axis points along [111].

**Procedure (deterministic)**  
Use `scipy.spatial.transform.Rotation.align_vectors`:

```
from scipy.spatial.transform import Rotation
import numpy as np
v_src = np.array([0, 0, 1])
v_dst = np.array([1, 1, 1]) / np.sqrt(3)
R = Rotation.align_vectors([v_dst], [v_src])[0].as_matrix()
```

This yields a 3×3 orthogonal matrix **R** that maps the original (x,y,z) frame to a new (x',y',z') frame with z' along [111].  

Define the **primed angular momentum operators**:

```
J_x' = R[0,0] J_x + R[0,1] J_y + R[0,2] J_z
J_y' = R[1,0] J_x + R[1,1] J_y + R[1,2] J_z
J_z' = R[2,0] J_x + R[2,1] J_y + R[2,2] J_z
```

where J_x, J_y, J_z are the original matrices in the |J,M_J⟩ basis.  
Construct the corresponding Stevens operators **O₄' and O₆'** using the same algebraic expressions as before, but replacing J_z → J_z', J_+ → J_x'+iJ_y', J_− → J_x'−iJ_y'.  Then assemble the rotated CEF Hamiltonian

```
H_CEF' = W [ x O₄'/F₄ + (1−|x|) O₆'/F₆ ].
```

Diagonalise H_CEF' to obtain primed eigen‑energies and eigenvectors.  In this primed basis compute the matrix elements of **J_z'** and the primed quadrupolar operator

**O₂⁰'** = 3 (J_z')² − J(J+1).

Finally, evaluate the **primed susceptibilities** using exactly the same summation formulas as in Sec. 4, but with the primed eigenvalues and matrix elements.  Denote the results

χ₀^(3)',  χ₂',  χ₂^(2)' .

*Note: χ₀^(1) is isotropic, so you may reuse the [001] value.*

### 6. Exchange‑enhanced (total) susceptibilities
The bilinear exchange is parameterized by the paramagnetic Curie temperature Θ^*.  The corresponding mean‑field coefficient *n* is

```
C = g_J² μ_B² J(J+1) / 3
n = Θ^* / C
```

The **first‑order magnetic susceptibility** is enhanced by *n* only:

```
χ_M^(1)(T) = χ₀^(1)(T) / (1 − n χ₀^(1)(T))          (6)
```

The **third‑order magnetic susceptibility** for **H ∥ [001]** is given by Eq. (7) of the paper:

```
χ_M^(3)_001(T) =  χ₀^(3)(T) / D⁴  +  2 G₁ [χ₂^(2)(T)]² / [ D⁴ ( 1 − G₁ χ₂(T) ) ]      (7)
```

with the common factor

```
D(T) = 1 − n χ₀^(1)(T).
```

For **H ∥ [111]** the analogous expression involves the primed susceptibilities and the trigonal quadrupolar coefficient G₂:

```
χ_M^(3)_111(T) =  χ₀^(3)'(T) / D⁴  +  (1/6) G₂ [χ₂^(2)'(T)]² / [ D⁴ ( 1 − (1/12) G₂ χ₂'(T) ) ] .
```

The numerical factors (1/6 and 1/12) arise from the projection of the quadrupolar operators onto the trigonal symmetry modes (see Appendix B of the paper).

---

## Parameters
Use the following physical parameters to compute the susceptibilities:

| Symbol        | Value               | Description |
|---------------|---------------------|-------------|
| Θ^*           | −3.0 K              | Bilinear exchange parameter (n = Θ^*/C) |
| W             | 1.4 K               | CEF energy scale |
| x             | −0.42               | Lea‑Leask‑Wolf mixing parameter |
| G₁            | 0.0103 K            | Tetragonal total quadrupolar coefficient |
| G₂            | −0.06 K             | Trigonal total quadrupolar coefficient |

All susceptibilities are expressed in **emu/mol** (CGS).  The temperature grid should cover the paramagnetic range, e.g. 5 K to 100 K, with a spacing fine enough to resolve the behaviour of χ_M^(3) near any sign change.

## Assets
- numpy
- scipy

## Workflow steps

### Step 1: Diagonalize cubic CEF Hamiltonian for J=6
- Role: process
- Action: Construct the cubic crystal‑field Hamiltonian in the |J,M_J⟩ basis using the Lea‑Leask‑Wolf operator equivalents with the parameters W and x for J=6. Diagonalise to obtain eigenvalues E_i and eigenvectors. Compute the matrix elements of J_z and O₂⁰ between all eigenstates. **No output file is required for this step; the results are kept in memory for the subsequent steps.**

### Step 2: Compute CEF‑only susceptibilities
- Role: process
- Action: Using the eigenvalues, eigenvectors, and matrix elements from Step 1, evaluate the four pure‑CEF susceptibilities χ₀^(1), χ₀^(3), χ₂, χ₂^(2) as functions of temperature according to the formulas in Sec. 4. Perform the coordinate rotation to the [111] direction as described in Sec. 5, rediagonalise the rotated Hamiltonian, and compute the primed susceptibilities χ₀^(3)', χ₂', χ₂^(2)'. **No output file is required for this step; keep the arrays in memory.**

### Step 3: Total first‑order magnetic susceptibility
- Role: scored
- Action: From the CEF‑only χ₀^(1)(T) and the bilinear exchange coefficient *n*, compute the exchange‑enhanced first‑order magnetic susceptibility χ_M^(1)(T) using Eq. (6). Output a CSV file with columns `T`, `chi_M1`.
- Output file: `/app/outputs/chi_M1.csv`
- Format: csv
- Contract: Columns: T (float, Kelvin), chi_M1 (float, emu/mol). Header line expected.
- Scoring: scored by hidden verifier

### Step 4: Total third‑order magnetic susceptibility
- Role: scored (load‑bearing)
- Action: From the CEF‑only susceptibilities and the parameters *n*, G₁, G₂, compute the total third‑order magnetic susceptibility χ_M^(3)(T) for the [001] and [111] directions using the formulas in Sec. 6. Output a CSV file with columns `T`, `chi_M3_001`, `chi_M3_111`.
- Output file: `/app/outputs/chi_M3.csv`
- Format: csv
- Contract: Columns: T (float, Kelvin), chi_M3_001 (float, H∥[001]), chi_M3_111 (float, H∥[111]). Header line expected.
- Scoring: scored by hidden verifier

## Output files
Write the following files under `/app/outputs`:
- `/app/outputs/chi_M1.csv`
- `/app/outputs/chi_M3.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi_M1.csv
- path: `/app/outputs/chi_M1.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total first-order magnetic susceptibility χ_M^(1) as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `chi_M1`
  - `units`:
    - `T`: Kelvin
    - `chi_M1`: emu/mol

### chi_M3.csv
- path: `/app/outputs/chi_M3.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total third-order magnetic susceptibility χ_M^(3) for [001] and [111] directions as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `chi_M3_001`, `chi_M3_111`
  - `units`:
    - `T`: Kelvin
    - `chi_M3_001`: emu/mol
    - `chi_M3_111`: emu/mol

Notes: The task computes theoretical susceptibilities for a prescribed set of physical parameters (W, x, Θ^*, G₁, G₂) over a user‑defined temperature grid. The fitting to experimental magnetization data is excluded because the original experimental data are not publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chi_M1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "chi_M1"
        ],
        "units": {
          "T": "Kelvin",
          "chi_M1": "emu/mol"
        }
      },
      "description": "Total first-order magnetic susceptibility χ_M^(1) as a function of temperature."
    },
    {
      "file": "chi_M3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "chi_M3_001",
          "chi_M3_111"
        ],
        "units": {
          "T": "Kelvin",
          "chi_M3_001": "emu/mol",
          "chi_M3_111": "emu/mol"
        }
      },
      "description": "Total third-order magnetic susceptibility χ_M^(3) for [001] and [111] directions as a function of temperature."
    }
  ],
  "notes": "The task computes theoretical susceptibilities for a prescribed set of physical parameters (W, x, Θ*, G1, G2) over a user-defined temperature grid. The fitting to experimental magnetization data is excluded because the original experimental data are not publicly available."
}
```

## How you are scored
A hidden verifier will score your submission independently. For each of the scored workflow steps (total first‑order and total third‑order susceptibility files) it will read your CSV tables and compare the susceptibility values against a reference computation that uses the same theoretical framework but with hidden parameter sets and hidden temperature evaluation points. The reward is the weighted sum of the scores from these two steps, with the third‑order susceptibility carrying the larger weight because of its central role. For a directional metric like susceptibility, the comparison rewards values that meet or exceed a quality threshold rather than penalizing small implementation‑dependent differences; the exact thresholds are hidden. Simply reporting a number from the literature is insufficient—the verifier checks the shape and temperature dependence of the computed curves, so you must genuinely execute the diagonalization and susceptibility evaluation pipeline.