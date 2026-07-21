# Hard-Sphere Fluid-Solid Coexistence and Crystal Stability Using GELA

## Problem background
Classical density-functional theory describes the equilibrium thermodynamics of nonuniform systems such as crystalline solids. A key challenge is to predict the free energy and phase behavior of a crystal using only knowledge of the uniform fluid. The generalized effective liquid approximation (GELA) maps the excess thermodynamic properties of the solid onto those of an effective liquid, requiring only the direct correlation function of the uniform fluid as input. When applied to the hard-sphere system, this theory yields quantitative predictions for fluid–face-centered-cubic (fcc) solid coexistence and for the relative stability of body-centered-cubic (bcc) and simple-cubic (sc) crystals.

## Approach
The solid is described by a Gaussian-peak density profile on the lattice sites. The fluid direct correlation function is the analytic Percus–Yevick (PY) expression, and the uniform-fluid thermodynamics follow the Carnahan–Starling equation of state. The GELA excess free energy functional involves a double spatial integral of the density and the direct correlation function evaluated at a self-consistent effective density ρ̂. For computational tractability, the self-consistent GELA equations are approximated by the SCELA closure, ρ̂[λ ρ] ≈ λ ρ̂, which is known to yield results nearly identical to the full GELA for hard spheres. The effective density is determined iteratively by equating the excess free energy per particle of the solid to that of the effective liquid. The total free energies of the fcc, bcc, and sc crystals are minimized with respect to the Gaussian width α at each average solid density, and the fluid–fcc coexistence is located by a common-tangent construction.

## Reproduction target
Compute the fluid–fcc solid coexistence parameters for the hard-sphere system using the GELA/SCELA theory: the fluid and solid packing fractions η_F and η_S, the density change Δρ* = ρ*_S − ρ*_F, the reduced coexistence pressure P* = β P σ³, the entropy change per particle Δs/k_B, and the Lindemann parameter L. Additionally, determine the stability ordering of the fcc, bcc, and sc hard-sphere crystals, listing the phases from most stable to least stable near the solid coexistence density.

## Assets
- Percus–Yevick hard-sphere direct correlation function (explicit formula given below)
- Carnahan–Starling hard-sphere equation of state (explicit formula given below)

## Mathematical formalism

Use hard-sphere diameter σ = 1 for all calculations (densities are therefore expressed in units of σ⁻³). The thermal energy k_B T = 1/β. Whenever a de Broglie wavelength Λ appears it can be set to σ; it cancels in all coexistence quantities because it is common to the fluid and solid phases.

### 1. Gaussian density parameterization
The local number density of a solid phase is modeled as a sum of normalized Gaussians centered on the Bravais lattice vectors {R}:

ρ(r; α, ρ_S) = (α/π)^{3/2} ∑_R exp(-α |r − R|²) .

The lattice vectors and conventional cubic unit cells are:

- **fcc** (4 particles per cubic cell): lattice vectors (0,0,0), (0,1/2,1/2)a, (1/2,0,1/2)a, (1/2,1/2,0)a, with a = (4/ρ_S)^{1/3}. Nearest-neighbor distance d_nn = a/√2.
- **bcc** (2 particles per cubic cell): (0,0,0), (1/2,1/2,1/2)a, with a = (2/ρ_S)^{1/3}. d_nn = √3 a/2.
- **sc** (1 particle per cubic cell): (0,0,0), with a = (1/ρ_S)^{1/3}. d_nn = a.

### 2. Percus–Yevick hard-sphere direct correlation function
For a uniform hard-sphere fluid of density ρ and packing fraction η = (π/6) ρ σ³, the PY direct correlation function c(r; η) is zero for r ≥ σ and for r < σ:

c(r; η) = −λ₁ − 6η λ₂ (r/σ) − (1/2) η λ₁ (r/σ)³ ,

with  
λ₁ = (1 + 2η)² / (1 − η)⁴ ,  
λ₂ = −(1 + η/2)² / (1 − η)⁴ .

### 3. Carnahan–Starling equation of state
For a uniform hard-sphere fluid at packing fraction η:

Excess free energy per particle:  
 β φ_ex^CS(η) = (4η − 3η²) / (1 − η)² .

Compressibility factor:  
 Z(η) = β P^CS / ρ = (1 + η + η² − η³) / (1 − η)³ .

Excess chemical potential:  
 β μ_ex^CS(η) = (8η − 9η² + 3η³) / (1 − η)³ .

Total chemical potential (with de Broglie wavelength set to σ):  
 β μ^CS = ln(ρ σ³) + β μ_ex^CS(η) .

The total Helmholtz free energy per particle is β f^CS = ln(ρ σ³) − 1 + β φ_ex^CS(η).

### 4. Ideal free energy of the solid
The ideal free energy functional is (with Λ = σ)

β F_id[ρ] = ∫_V ρ(r) [ ln(ρ(r) σ³) − 1 ] d³r .

Because the integrand varies over many orders of magnitude, one may compute it on a fine grid inside the Wigner‑Seitz cell or the conventional cubic cell, using the known Gaussian superposition and a truncation radius large enough to capture all overlapping peaks. The free energy per particle is β f_id = β F_id / (ρ_S V).

### 5. Excess free energy functional (GELA with SCELA-like closure)
The GELA excess free energy is formally

β F_ex[ρ] = −∫ d³r ∫ d³r´ ρ(r) ρ(r´) ∫_0¹ dλ (1−λ) c(|r−r´|; ρ̂[λ ρ]) .

To make the computation tractable we adopt the closure ρ̂[λ ρ] ≈ λ ρ̂, which is the self-consistent effective liquid approximation (SCELA) and is known to reproduce the full GELA results for hard spheres to within a few percent. Then

β F_ex[ρ] = −½ ∫_V d³r ∫_V d³r´ ρ(r) ρ(r´) ∫_0¹ dλ (1−λ) c(|r−r´|; λ ρ̂) ,   (1)

where the factor ½ corrects for the double counting of pairs (the original GELA expression omitted a factor ½; using ½ yields correct excess free energies per particle).

The double spatial integral is over a periodic volume V that contains an integer number of primitive cells. Because c(|r|; η) is zero for r ≥ σ, the r´ integration can be restricted to a sphere of radius σ around r. The λ integral can be performed by one‑dimensional Gauss–Legendre quadrature with 4–6 points.

### 6. Effective density and self-consistency loop
The effective density ρ̂ is defined by equating the excess free energy per particle of the solid to that of the effective liquid:

φ_ex[ρ] = φ_ex^CS(η̂) ,   with η̂ = (π/6) ρ̂ σ³ .

Given α and the average solid density ρ_S, compute ρ̂ iteratively:

1. Initial guess: ρ̂ = ρ_S.
2. Evaluate φ_ex[ρ] = F_ex[ρ] / (ρ_S V) using Eq. (1) with the current ρ̂.
3. Solve φ_ex^CS(η̂_new) = φ_ex[ρ] for η̂_new (e.g., by a one‑dimensional root finder, using the monotonic CS function).
4. Update ρ̂ = (6/π) η̂_new / σ³.
5. Repeat until |ρ̂_new − ρ̂| < 10⁻⁶.

The converged effective density defines the solid’s excess free energy: F_ex = N φ_ex^CS(η̂). The total free energy of the solid is F = F_id + F_ex.

### 7. Lindemann parameter
The Lindemann parameter L is the root‑mean‑square displacement divided by the nearest‑neighbor distance. For the Gaussian profile (α/π)^{3/2} e^{−α r²}, the mean‑square displacement is ⟨u²⟩ = 3/(2α). Hence

L = √(⟨u²⟩) / d_nn = √(3/(2α)) / d_nn ,

with d_nn as given above for each crystal structure.

## Workflow steps

### Step 1: Numerical evaluation of GELA integrals
- Role: process
- Action: Implement the function that computes φ_ex[ρ] = F_ex/(ρ_S V) by evaluating Eq. (1) for given α, ρ_S, and ρ̂. Use a three‑dimensional grid on a conventional cubic cell containing several lattice sites (e.g., 4 for fcc, 2 for bcc, 1 for sc). For each grid point r, sum the Gaussian contributions from all lattice sites whose contributions are non‑negligible, then integrate over r´ inside the cutoff sphere |r−r´| ≤ σ. The λ integral is performed by a one‑dimensional quadrature. Test that the result is insensitive to the grid spacing and the truncation of the Gaussian tails.
- Evidence: (optional) Not scored, but you may save intermediate sanity checks.

### Step 2: Self-consistent determination of the effective density
- Role: process
- Action: For each (α, ρ_S) pair of interest (α is scanned, ρ_S is taken from a set of packing fractions), perform the iterative procedure described in Section 6 to obtain the converged ρ̂. Usually 5–15 iterations are enough. You may store the mapping (α, ρ_S, ρ̂) in a table for later use.
- Evidence: `/app/outputs/effective_density_table.csv` (optional, not scored)

### Step 3: Free energy and pressure of cubic crystals
- Role: process
- Action: For each crystal structure (fcc, bcc, sc) and a range of packing fractions η = (π/6) ρ_S σ³ (e.g., 0.46 – 0.56), minimize the total free energy per particle f(α) = f_id(α) + φ_ex^CS(η̂(α)) with respect to α. Use a golden‑section or Brent optimizer (the initial α guess can be, e.g., 100/σ²). Record the optimal α and the corresponding free energy per particle. Compute the pressure as P* = β P σ³ = ρ_S² ∂(f)/∂ρ_S evaluated numerically (e.g., by finite differences of f with respect to ρ_S at fixed α_eq).
- Evidence: `/app/outputs/free_energy_pressure.csv` (optional, not scored)

### Step 4: Fluid–fcc solid coexistence determination
- Role: scored (load-bearing)
- Action: Using the solid free energy and pressure from Step 3 (fcc) and the Carnahan‑Starling fluid thermodynamics (Section 3), find the two packing fractions η_F (fluid) and η_S (solid) that satisfy equal chemical potentials and pressures:
  μ^CS(η_F) = μ_solid(η_S) and P^CS(η_F) = P_solid(η_S).
  Extract the coexistence parameters:
  - η_F, η_S,
  - Δρ* = ρ_S − ρ_F = (6/π)(η_S − η_F)/σ³,
  - reduced pressure P* = β P σ³ at coexistence,
  - entropy change per particle Δs/k_B = (u_solid/T − u_fluid/T) + P*(1/ρ_S − 1/ρ_F), where the internal energy per particle u is obtained from the known CS and solid free energies,
  - Lindemann parameter L evaluated at the solid coexistence state (with α_eq from Step 3 at η_S).
  Write these six values to the output file.
- Output file: `/app/outputs/coexistence_parameters.json`
- Format: json
- Contract: JSON object with keys: eta_F (float), eta_S (float), Delta_rho_star (float), P_star (float), Delta_s_over_kB (float), L (float).
- Scoring: scored by hidden verifier

### Step 5: Phase stability ordering of cubic crystals
- Role: scored
- Action: From the free energy data obtained in Step 3, compare the equilibrium free energies of the fcc, bcc, and sc phases at a density near the solid coexistence (e.g., at η = η_S from Step 4). Determine the stability ordering (most stable → least stable) and output it as an ordered list.
- Output file: `/app/outputs/phase_stability.json`
- Format: json
- Contract: JSON object with key 'phase_order': array of strings in order of decreasing stability (most stable first).
- Scoring: scored by hidden verifier

## Output files
Only the two scored files are required for evaluation:
- `/app/outputs/coexistence_parameters.json`
- `/app/outputs/phase_stability.json`

The intermediate files mentioned in optional evidence (`analytic_integration_note.txt`, `effective_density_table.csv`, `free_energy_pressure.csv`) are **not** scored and need not be written; they are listed only as potential aids for your workflow.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coexistence_parameters.json
- path: `/app/outputs/coexistence_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fluid-fcc solid coexistence parameters (packing fractions, density change, coexistence pressure, entropy change per particle, Lindemann parameter) computed using the GELA theory. The checker compares each parameter to reference values with appropriate numerical tolerances.
- schema:
  - `type`: object
  - `required`:
    - `eta_F`: float
    - `eta_S`: float
    - `Delta_rho_star`: float
    - `P_star`: float
    - `Delta_s_over_kB`: float
    - `L`: float

### phase_stability.json
- path: `/app/outputs/phase_stability.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Ordered list of the cubic phases (fcc, bcc, sc) from most stable to least stable, as predicted by the GELA theory. The checker verifies the ordering.
- schema:
  - `type`: object
  - `required`:
    - `phase_order`: array of strings

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coexistence_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "eta_F": "float",
          "eta_S": "float",
          "Delta_rho_star": "float",
          "P_star": "float",
          "Delta_s_over_kB": "float",
          "L": "float"
        }
      },
      "description": "Fluid-fcc solid coexistence parameters computed using the GELA theory. The checker compares each parameter to reference values with appropriate numerical tolerances."
    },
    {
      "file": "phase_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "phase_order": "array of strings"
        }
      },
      "description": "Ordered list of the cubic phases (fcc, bcc, sc) from most stable to least stable, as predicted by the GELA theory. The checker verifies the ordering."
    }
  ]
}
```