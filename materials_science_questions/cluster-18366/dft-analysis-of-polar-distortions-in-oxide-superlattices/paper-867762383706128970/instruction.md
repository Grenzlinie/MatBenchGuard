# Self-consistent tight-binding and lattice relaxation model for SrTiO3 surface 2DEG

## Problem background
SrTiO₃ surfaces can host quasi-two-dimensional electron gases (2DEGs) when a large external electric field attracts carriers to the surface. The spatial distribution of the electrons is determined by a competition between quantum confinement and the host material's extremely strong, non-linear dielectric response. Understanding this distribution is crucial for interpreting experiments on superconductivity and magnetism in these systems. The goal is to compute how the electron density profile, subband energies, and confinement statistics vary with total 2D carrier density.

## Approach
We implement a self-consistent model that couples a tight-binding electronic Hamiltonian for the Ti t₂g orbitals with a non-linear lattice relaxation model for the soft optical phonon mode.

**Electronic model** – Each TiO₂ layer contributes three t₂g orbitals (yz, zx, xy) with spin. Intra-layer hopping is described by two parameters: t (strong) and t′ (weak). In the orbital basis {yz, zx, xy}, the single-layer Hamiltonian is diagonal: for yz the dispersion is –2t′cos(kₓ) –2t cos(k_y), for zx –2t cos(kₓ) –2t′cos(k_y), and for xy –2t cos(kₓ) –2t cos(k_y). Near the 2D Γ point this reduces to parabolic dispersions with appropriate light/heavy masses. Adjacent layers are coupled by a diagonal inter-layer hopping: t for yz and zx, t′ for xy. On-site terms include a tetragonal splitting Δ_T (raising the xy site energy relative to yz/zx) and atomic spin-orbit coupling Δ_SO that hybridizes the spin-orbital basis (6×6 matrix).

**Lattice relaxation** – The lattice energy is written as U = ½∑ᵢⱼ uᵢKᵢⱼuⱼ – Q∑ᵢEᵢuᵢ + (γ/4)∑ᵢuᵢ⁴, where uᵢ is the displacement of the soft mode in layer i, Eᵢ is the average electric field in the cell, Q an effective charge, and γ a non-linearity parameter. The dynamical matrix K(q) in momentum space is K(q) = (2π)²µ[ f₀² – f₁²exp(–α₁²(q+G)²/2) – f₂²exp(–α₂²(q+G)²/2) ] with parameters f₀, f₁, f₂, α₁, α₂. The polarization density is Pᵢ = (Q/a³) uᵢ.

**Electrostatics** – The electric field is obtained from the Poisson equation: ∇·E(z) = –(4πe/ε∞)∑ᵢ nᵢ δ(z–zᵢ) + 4π∑ᵢ ∇·Pᵢ, where ε∞ is the high-frequency dielectric constant and nᵢ is the layer-resolved electron areal density. The boundary conditions are: electric field above the surface fixed by the total 2D density n_T (E₀ = 4πe n_T/ε∞), and the field deep in the bulk is zero (grounded substrate).

**Self-consistent loop** – Starting from an initial guess for {uᵢ} and {nᵢ}, the procedure iterates: (1) solve Poisson's equation for E(z) and the layer-dependent potential Vᵢ, (2) minimize the lattice energy functional to obtain new displacements uᵢ, (3) build the 60‑layer Hamiltonian (360×360 matrix) with Vᵢ added to the on-site terms, (4) diagonalize to obtain the layer‑resolved densities nᵢ for the occupied subbands, (5) mix the new densities with the previous ones using an under-relaxation factor ≤1%, and repeat until convergence.

All parameters are taken from low‑temperature experimental data and are listed below.

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Lattice constant | a | 3.904 Å |
| Strong hopping | t | 236 meV |
| Weak hopping | t′ | 35 meV |
| Spin-orbit coupling | Δ_SO | 18 meV |
| Tetragonal splitting | Δ_T | 3.2 meV |
| Static dielectric constant (90 K) | ε₀ | 24408 |
| Intermediate dielectric constant | ε₁ | 1340 |
| High‑frequency dielectric constant | ε∞ | 5.5 |
| Effective charge | Q | 8.33 e |
| Non‑linear displacement scale | u_NL | 0.0034 Å |
| Dynamical: on‑site | f₀ | 4×10¹² s⁻¹ |
| Dynamical: first Gaussian | f₁ | 2.73×10¹² s⁻¹ |
| Dynamical: second Gaussian | f₂ | 0.97×10¹² s⁻¹ |
| Width first Gaussian | α₁ | 1.15 a |
| Width second Gaussian | α₂ | 5 a |

(µ is the reduced mass, set to 24 amu; γ is determined self‑consistently via γ = [2π(f₀ – f₁ – f₂)/u_NL]².)

## Reproduction target
For three total areal carrier densities n_T = 8.3×10¹² cm⁻², 2.0×10¹⁴ cm⁻², and 5.9×10¹⁴ cm⁻², perform the self-consistent calculation described above. From each converged solution, compute the following quantities and write them to `/app/outputs/step_01_results.json` following the output contract.

1. **Subband energies** – the lowest six doubly-degenerate subband energies (in meV) at the 2D Gamma point (k_∥ = 0).
2. **Layer-resolved density fractions** – for each of the 60 TiO₂ layers, the fraction of the total density n_i/n_T (values between 0 and 1).
3. **Average distance from surface** – ⟨z⟩ = Σ_i (z_i · n_i / n_T), where z_i is the layer index (1 to 60), using the first layer (z=1) as the surface.
4. **Standard deviation** – σ = sqrt[ Σ_i (z_i – ⟨z⟩)² · (n_i / n_T) ].

The JSON file must contain a top-level key `"densities"` with a list of three objects, one per density, each with fields `n_T`, `band_energies`, `layer_fractions`, `average_z`, and `sigma` as specified in the output contract.

## Assets

- Python scientific stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Self-consistent electronic-lattice solver
- Role: process
- Action: Implement the tight-binding Hamiltonians (single-layer, inter-layer, tetragonal splitting, spin-orbit), the lattice energy functional, and the Poisson equation as described in the approach. For three total carrier densities (8.3e12, 2.0e14, 5.9e14 cm^-2), perform the iterative self-consistent procedure: minimize lattice energy, solve Poisson equation, diagonalize the 60-layer electronic Hamiltonian, update layer-resolved densities with under-relaxation (≤1%) until convergence. Use a 60-unit-cell slab with grounded bulk boundary conditions. All numerical model parameters from the paper's Table I are to be used.
- Evidence: `/app/outputs/convergence_log.txt`

### Step 2: Compute confinement statistics and output results
- Role: scored (load-bearing)
- Action: From the converged solutions for the three total densities (8.3e12, 2.0e14, 5.9e14 cm^-2), extract the lowest six doubly-degenerate subband energies at the 2D Gamma point (k_parallel = 0). Compute the layer-resolved electron density fractions (n_i / n_T). Calculate the average distance from surface <z> = sum_i (z_i * n_i / n_T) and the standard deviation sigma = sqrt( sum_i ( (z_i - <z>)^2 * n_i / n_T ) ), where z_i is the layer index (1..60). Output all results as a JSON file.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: {"densities": [{"n_T": float (cm^-2), "band_energies": [float] (meV), "layer_fractions": [float] (0-1), "average_z": float (layers), "sigma": float (layers)}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Confinement statistics: for each of the three densities, provides the six lowest 2D subband energies, per-layer fractional occupancy, average depth and spread. The checker will verify internal consistency and structural trends (e.g., average_z decreasing and sigma decreasing as density increases, high-density peak at layer 0) against expected confinement regimes.
- schema:
  - `type`: object
  - `required`:
    - `densities`: array of objects each containing n_T, band_energies, layer_fractions, average_z, sigma
  - `items`:
    - `n_T`: float (cm^-2)
    - `band_energies`: array of 6 floats (meV)
    - `layer_fractions`: array of 60 floats (0-1)
    - `average_z`: float (layers)
    - `sigma`: float (layers)
  - `units`:
    - `n_T`: cm^-2
    - `band_energies`: meV
    - `layer_fractions`: dimensionless
    - `average_z`: layers
    - `sigma`: layers

Notes: The solver may exhibit run-to-run variations; the verifier uses relative trends and inequalities with moderate tolerances to accommodate legitimate implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "densities": "array of objects each containing n_T, band_energies, layer_fractions, average_z, sigma"
        },
        "items": {
          "n_T": "float (cm^-2)",
          "band_energies": "array of 6 floats (meV)",
          "layer_fractions": "array of 60 floats (0-1)",
          "average_z": "float (layers)",
          "sigma": "float (layers)"
        },
        "units": {
          "n_T": "cm^-2",
          "band_energies": "meV",
          "layer_fractions": "dimensionless",
          "average_z": "layers",
          "sigma": "layers"
        }
      },
      "description": "Confinement statistics: for each of the three densities, provides the six lowest 2D subband energies, per-layer fractional occupancy, average depth and spread. The checker will verify internal consistency and structural trends (e.g., average_z decreasing and sigma decreasing as density increases, high-density peak at layer 0) against expected confinement regimes."
    }
  ],
  "notes": "The solver may exhibit run-to-run variations; the verifier uses relative trends and inequalities with moderate tolerances to accommodate legitimate implementation spread."
}
```

## How you are scored
A hidden verifier reads your `step_01_results.json`, recomputes the average distance and standard deviation from the layer_fractions to check internal consistency, and verifies that the trends in these quantities across the three densities, as well as the subband energies, satisfy expected structural relationships (e.g., stronger confinement and larger subband splittings at higher densities, and physically sensible band ordering). The verifier does not require exact agreement with any particular reference number; it rewards solutions that correctly reproduce the physical evolution of the 2DEG profile as a function of density. The final reward is a weighted sum of the scores from each workflow step.
