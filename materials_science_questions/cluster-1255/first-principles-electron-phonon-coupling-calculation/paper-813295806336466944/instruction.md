# Correlated squeezed-state variational ansatz for electron-phonon system ground state

## Problem background
The system under study is an electron‑phonon system with strong electron‑phonon interaction and a weak on‑site Coulomb repulsion, described by the Hubbard–Holstein model. The key challenge is to accurately determine the ground‑state properties of such a system, because the interplay of electron itinerancy, local attraction, and polaron formation strongly affects the resulting electronic and superconducting behaviour. The goal is to compute the ground‑state energy per site, the superconducting energy gap, and the condensation energy for both a square lattice and a simple cubic lattice, and to assess the role of intersite phonon correlations beyond previous uncorrelated treatments.

## Approach

### Model Hamiltonian
The system is described by the Hamiltonian

```
H = Σ_{i,σ} (E-μ) d†_{iσ} d_{iσ} + Σ_{⟨i,j⟩,σ} T d†_{iσ} d_{jσ} + Σ_i ħω b†_i b_i
    + Σ_i U d†_{i↑} d_{i↑} d†_{i↓} d_{i↓} + Σ_{i,σ} g d†_{iσ} d_{iσ} (b†_i + b_i) .
```

Here μ is the chemical potential, d and b are electron and phonon annihilation operators, ⟨i,j⟩ denotes nearest neighbours, and the material parameters are:
- phonon energy `ħω = 0.08`
- electron‑phonon coupling `J ≡ g²/(ħω) = 0.3`
- on‑site Coulomb repulsion `U = 0.3`
- electron density `n = 0.8` (average number of electrons per site)
- bare half‑bandwidth `D = 1` (this sets the energy scale)
- local electron level `E` is set to `0`, as only the combination with the chemical potential matters.

### Transformations
Apply the Lang‑Firsov unitary displacement transformation

```
D = exp{ -(g/ħω) Σ_{i,σ} d†_{iσ} d_{iσ} (b†_i - b_i) }
```

followed by a single‑mode squeezing transformation

```
S = exp{ α Σ_i (b†²_i - b²_i) }   with τ ≡ exp(-2α) .
```

After these two steps the Hamiltonian becomes (Eq. (5) of the paper)

```
H̃ = S† D† H D S
   = Σ_{i,σ} (E-μ) d†_{iσ} d_{iσ}
     + Σ_{⟨i,j⟩,σ} T d†_{iσ} d_{jσ} exp{ (g/ħω) τ [(b†_i-b_i)-(b†_j-b_j)] }
     + ¼ Σ_i ħω exp(4α) (b†_i+b_i)² - ¼ Σ_i ħω exp(-4α) (b†_i-b_i)²
     - ½ N ħω + Σ_i U d†_{i↑} d_{i↑} d†_{i↓} d_{i↓}
     - Σ_{i,σ,σ'} J d†_{iσ} d_{iσ} d†_{iσ'} d_{iσ'}   (J = g²/ħω) .
```

### Correlated phonon state and effective electronic Hamiltonian
To account for intersite phonon correlations beyond the Hartree approximation we introduce a correlated multi‑mode squeezed vacuum state

```
|Ψ_p⟩ = exp{ ½ Σ_{i≠j} β_{ij} (b†_i b†_j - b_i b_j) } |vac⟩ .
```

We restrict the correlation matrix to uniform nearest‑neighbour correlations: `β_{ij} = β` if i,j are nearest neighbours and zero otherwise. The parameter `β` is real and, together with `τ`, will be optimized.

Averaging `H̃` over `|Ψ_p⟩` yields an effective electronic Hamiltonian (Eq. (13))

```
H_eff = Σ_{i,σ} (E_e - μ) d†_{iσ} d_{iσ} + Σ_{⟨i,j⟩,σ} T_e d†_{iσ} d_{jσ}
        + Σ_i U_e d†_{i↑} d_{i↑} d†_{i↓} d_{i↓} + N C(τ,β) ,
```

with
- `E_e = E - J`
- `U_e = U - 2J`   (the effective on‑site interaction becomes attractive when J > U/2)
- `T_e` is the renormalized hopping integral
- `C(τ,β)` is the phonon‑mediated constant energy per site:
```
C(τ,β) = ¼ ħω [ e^{4α} [e^{2β}]_{00} + e^{-4α} [e^{-2β}]_{00} ] - ½ ħω .
```

Here `[e^{±2β}]_{00}` denotes a diagonal matrix element of the exponential of the matrix `β_{ij}`. For a d‑dimensional hypercubic lattice with nearest‑neighbour `β` it can be expressed as a momentum‑space integral:

```
[e^{±2β}]_{00} = ∫_{BZ} (d^d k)/(2π)^d  exp{ ±4β Σ_{ν=1}^{d} cos(k_ν) } .
```

You must evaluate this integral numerically for each lattice type (square: d=2, cubic: d=3).  The Brillouin‑zone integration is over `k_ν ∈ [-π,π]`.

### Renormalized hopping and effective bandwidth
The hopping renormalization is given by Eq. (19) of the paper:

```
T_e = T  exp{ -½ (g/ħω)²  R(α,β) } ,
where
R(α,β) = [ cosh(2α) - sinh(2α) e^{-2β} ] / [ cosh(2α) + sinh(2α) e^{-2β} ] .
```

Using `τ = exp(-2α)`, the hyperbolic functions can be written as
```
cosh(2α) = (τ + 1/τ)/2,   sinh(2α) = (1/τ - τ)/2 .
```
Thus `R` becomes a simple algebraic function of `τ` and `β`.  The absolute value of the bare hopping `T` is not needed because it only appears through ratios that are absorbed in the definition of the effective half‑bandwidth below.

We adopt a **square (box) density of states** for the electrons:
```
g(ε) = 1 / (2 D_eff)   for |ε| < D_eff,   zero otherwise.
```
The effective half‑bandwidth scales with the hopping renormalization:
```
D_eff = D × (T_e / T) .
```
Physical constraint: `0 < τ ≤ 1` (equivalently `α ≥ 0`).  The parameter `β` can take small negative values (the optimal `β` is negative in the paper).

### BCS mean‑field treatment
The effective electronic model is an attractive Hubbard model (`U_e = U - 2J = -0.3` for the given parameters).  It is solved within the standard BCS theory extended to include an arbitrary chemical potential `μ̃ ≡ μ - E_e`.  Because we set `E = 0`, we have `E_e = -J` and `μ̃ = μ + J`.  All equations below are written per lattice site.

**Superconducting state (Δ ≠ 0)**
Introduce the BCS gap `Δ ≥ 0` (to be determined).  The quasiparticle energy is
```
E(ε) = sqrt( (ε - μ̃)² + Δ² ) .
```
The occupation factor is `v(ε)² = ½ [1 - (ε - μ̃)/E(ε)]`.

The gap equation
```
1 = |U_e| ∫_{-D_eff}^{D_eff} g(ε)  dε / (2 E(ε))
```
or, equivalently,
```
1 = (|U_e| / (2 D_eff)) ∫_{-D_eff}^{D_eff} dε / E(ε) .
```

The electron‑density equation
```
n = 2 ∫_{-D_eff}^{D_eff} g(ε) v(ε)² dε
  = 1 - ∫_{-D_eff}^{D_eff} g(ε) (ε - μ̃) / E(ε) dε .
```

For a given pair `(τ, β)` the two coupled equations are solved numerically for `Δ` and `μ̃`.  The electronic energy per site is
```
E_el = 2 ∫_{-D_eff}^{D_eff} ε g(ε) v(ε)² dε  - μ̃ n  + Δ² / |U_e| .
```

**Normal state (Δ = 0)**
When `Δ = 0` the density equation reduces to
```
n = (D_eff + μ̃) / D_eff    ⇒    μ̃ = D_eff (n - 1) .
```
The electronic energy is purely kinetic:
```
E_el(Δ=0) = ∫_{-D_eff}^{μ̃} (ε / D_eff) dε   (already including the -μ̃ n term correctly).
```
It can be evaluated analytically:
```
E_el(Δ=0) = (μ̃² - D_eff²) / (2 D_eff) - μ̃ n .
```

**Total energy per site**
To obtain the total ground‑state energy add the phonon contribution:
```
E_tot(τ, β, Δ, μ̃) = E_el + C(τ, β) .
```
For the superconducting state `E_el` is the BCS electronic energy with the self‑consistent `(Δ, μ̃)`.  For the normal state use `Δ = 0` and the corresponding `μ̃`.

### Variational optimization
The variational parameters are `τ ∈ (0,1]` (or equivalently `α ≥ 0`) and `β` (a real number, typically `β < 0`).  You must perform a numerical two‑parameter minimization of `E_tot` for both lattice types, **separately for the normal state** (force `Δ = 0`) **and for the superconducting state** (allow `Δ ≥ 0`).

From the minimized values obtain:
- optimal parameters `τ_opt`, `β_opt`
- normal‑state energy `energy_normal = E_tot(τ_opt,β_opt) |_{Δ=0}`
- superconducting‑state energy `energy_superconducting = E_tot(τ_opt,β_opt) |_{Δ≥0}`
- superconducting gap `gap = Δ_opt` (the self‑consistent gap at the superconducting minimum)
- condensation energy `condensation_energy = energy_superconducting - energy_normal` (negative for a stable superconducting state).

Repeat the whole procedure for the square lattice and for the simple cubic lattice.  The only difference between the two cases is the dimension `d` appearing in the Brillouin‑zone integration for `[e^{±2β}]_{00}`.  (The effective half‑bandwidth `D_eff` is the same because it is defined through the box density of states, not through a tight‑binding bandwidth that would depend on dimension.)

### Physical parameters (fixed)

| parameter | value | meaning |
|-----------|-------|---------|
| `ħω`      | 0.08  | phonon energy |
| `J = g²/ħω` | 0.3   | electron‑phonon coupling strength |
| `U`       | 0.3   | on‑site Coulomb repulsion |
| `n`       | 0.8   | electron density per site |
| `D`       | 1     | bare half‑bandwidth (energy unit) |
| `E`       | 0     | bare local electron level |

From these: `U_e = U - 2J = -0.3`, and `J` is used internally for `E_e` and the hopping renormalization.

## Reproduction target
Compute the optimal variational parameters (τ, β) and the corresponding ground‑state energy per site for both the normal state (Δ₀ = 0) and the superconducting state (Δ₀ ≠ 0), the superconducting gap Δ₀, and the condensation energy δ. Perform this computation for two lattice types: a square lattice and a simple cubic lattice. Use the square density of states and the explicit equations given above. Report the results in two CSV files, one for each lattice.

## Assets
- Python 3 (runtime)
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute ground-state properties for square lattice
- Role: scored
- Action: Implement the variational energy minimization for the square lattice (dimension d=2). Use the square density of states and all equations provided in the Approach section. For the given parameters (ħω=0.08, J=0.3, U=0.3, n=0.8, D=1), minimize the ground-state energy per site over the variational parameters τ and β. At the optimal (τ,β) evaluate the superconducting (Δ₀≠0) and normal (Δ₀=0) energies, the gap Δ₀, and the condensation energy. Report the optimal parameters and the corresponding energies, gap, and condensation energy.
- Output file: `/app/outputs/results_square.csv`
- Format: csv
- Contract: Columns: τ_opt, β_opt, energy_normal, energy_superconducting, gap, condensation_energy. All numeric. Energies and gap in units of D=1.
- Scoring: scored by hidden verifier

### Step 2: Compute ground-state properties for simple cubic lattice
- Role: scored
- Action: Implement the same variational minimization for the simple cubic lattice (dimension d=3). The only change is the Brillouin‑zone integration for the phonon constant `C`. Output the optimal parameters and the same set of properties.
- Output file: `/app/outputs/results_cubic.csv`
- Format: csv
- Contract: Columns: τ_opt, β_opt, energy_normal, energy_superconducting, gap, condensation_energy. All numeric. Energies and gap in units of D=1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_square.csv`
- `/app/outputs/results_cubic.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_square.csv
- path: `/app/outputs/results_square.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed optimal variational parameters and ground-state properties for the square lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `τ_opt`, `β_opt`, `energy_normal`, `energy_superconducting`, `gap`, `condensation_energy`
  - `units`:
    - `energy_normal`: D=1
    - `energy_superconducting`: D=1
    - `gap`: D=1
    - `condensation_energy`: D=1

### results_cubic.csv
- path: `/app/outputs/results_cubic.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed optimal variational parameters and ground-state properties for the simple cubic lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `τ_opt`, `β_opt`, `energy_normal`, `energy_superconducting`, `gap`, `condensation_energy`
  - `units`:
    - `energy_normal`: D=1
    - `energy_superconducting`: D=1
    - `gap`: D=1
    - `condensation_energy`: D=1

Notes: The checker compares each column to hidden reference values derived from the paper's reported results. The optimal τ and β are sanity-checked but not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_square.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "τ_opt",
          "β_opt",
          "energy_normal",
          "energy_superconducting",
          "gap",
          "condensation_energy"
        ],
        "units": {
          "energy_normal": "D=1",
          "energy_superconducting": "D=1",
          "gap": "D=1",
          "condensation_energy": "D=1"
        }
      },
      "description": "Computed optimal variational parameters and ground-state properties for the square lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance."
    },
    {
      "file": "results_cubic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "τ_opt",
          "β_opt",
          "energy_normal",
          "energy_superconducting",
          "gap",
          "condensation_energy"
        ],
        "units": {
          "energy_normal": "D=1",
          "energy_superconducting": "D=1",
          "gap": "D=1",
          "condensation_energy": "D=1"
        }
      },
      "description": "Computed optimal variational parameters and ground-state properties for the simple cubic lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance."
    }
  ],
  "notes": "The checker compares each column to hidden reference values derived from the paper's reported results. The optimal τ and β are sanity-checked but not directly scored."
}
```

## How you are scored
A hidden verifier reads each of the two output CSV files and independently checks the computed quantities. For the ground‑state energies, a threshold‑or‑better policy is applied: an energy that meets or improves upon the reference value (lower is better) earns full credit, while a higher energy results in a reduced score. For the superconducting gap and the condensation energy, an exact‑match tolerance is used. The scores from both lattice results are combined by weight into a final reward between 0 and 1. Simply reporting the paper’s numbers without actually executing the variational minimization will not pass; the verifier expects a solution that is generated by a genuine numerical optimization run.