# Topological Invariants of 2D Chiral and Planar p-wave Superfluids

## Problem background
Andreev-Majorana bound states in two-dimensional p-wave superfluids are controlled by the topology of the bulk. For gapped chiral and time-reversal-invariant planar phases, the number of gapless edge modes is determined by integer topological invariants constructed from the single-particle Green's function. In the chiral A-phase, a TKNN-type invariant N counts the net number of chiral edge branches, while in the planar phase a symmetry-protected invariant N_K (involving a K matrix) characterizes the spin Hall response. Computing these invariants from the bulk Green's functions reveals how many edge states appear and whether the system is topologically trivial or nontrivial depending on the chemical potential. The derived spin Hall conductance is directly proportional to N_K.

## Approach
We implement the minimal Green's function models that capture the topology of the three phases: (i) spinless chiral A-phase, (ii) spinful chiral A-phase, and (iii) time-reversal-invariant planar phase. Each Green's function depends on momentum (p_x, p_y) and Matsubara frequency p_0. The chemical potential μ acts as a control parameter: μ > 0 corresponds to the topologically nontrivial regime, while μ < 0 is the trivial regime (for m>0, c>0). For the chiral phases we compute the TKNN invariant N by numerical integration of the trace formula over the three-dimensional momentum-frequency space. For the planar phase we compute the symmetry-protected invariant N_K using the same trace formula with an extra K matrix insertion (K = τ3 σz). Finally, the spin Hall conductance is obtained from the μ>0 value of N_K via σ_{xy}^{spin} = N_K/(4π). All integrations are performed with standard open-source numerical tools.

## Reproduction target
Produce two JSON files:

- `/app/outputs/topological_invariants.json`: contains the topological invariant N for the spinless and spinful chiral phases at μ > 0 and μ < 0 (four float values).
- `/app/outputs/planar_invariants.json`: contains the invariant N_K for the planar phase at μ > 0 and μ < 0, and the spin Hall conductance (three float values).

These numbers must be obtained by numerical integration of the appropriate Green's functions with m>0 and c>0. The invariants are integer-valued in the topological classification; the conductance is a derived physical quantity.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute chiral topological invariants
- Role: scored
- Action:
  Implement the Green's functions for the spinless and spinful chiral p‑wave superfluids.

  **Green's function inverses** (Pauli matrices τ act in Nambu space; σ act in spin space; I_n is the identity of dimension n):

  *Spinless:*  
  G⁻¹(p₀,p_x,p_y) = i p₀ τ₀ + τ₃ (p²/(2m)−μ) + c (τ₁ p_x + τ₂ p_y)   (2×2 matrices)

  *Spinful:*  
  G⁻¹(p₀,p_x,p_y) = i p₀ I₄ + (τ₃⊗I₂) (p²/(2m)−μ) + c σ_z (τ₁ p_x + τ₂ p_y)   (4×4 matrices)

  Here p² = p_x² + p_y². Choose m>0, c>0; the sign of μ distinguishes the topological regimes.  
  The Green's function matrix is G = (G⁻¹)⁻¹.

  **Topological invariant N** – TKNN‑type formula (Eq. (1) of the paper):

  N = (e_{ijk} / (24π²)) · Tr ∫ d³p  G(p) ∂_{p_i} G⁻¹(p)  G(p) ∂_{p_j} G⁻¹(p)  G(p) ∂_{p_k} G⁻¹(p)

  - p = (p₀, p_x, p_y) with p₀ being the Matsubara frequency.
  - e_{ijk} is the totally antisymmetric Levi‑Civita symbol with e₀₁₂ = +1.
  - ∂_{p_i} denotes partial derivative with respect to the i‑th component of p.
  - Tr runs over the full matrix space (2×2 for spinless, 4×4 for spinful).
  - The integral runs over all p₀, p_x, p_y from −∞ to +∞; in practice you can truncate the domain to a finite box (e.g., |p_i| ≤ p_max) and use a dense enough grid to achieve convergence.

  Numerically evaluate N for μ>0 (topological) and μ<0 (trivial) for both the spinless and the spinful model.  
  Write the four values as floats into `/app/outputs/topological_invariants.json`.

- Output file: `/app/outputs/topological_invariants.json`
- Format: json
- Contract: JSON object with keys: 'N_spinless_mu_positive', 'N_spinless_mu_negative', 'N_spinful_mu_positive', 'N_spinful_mu_negative', each a float.
- Scoring: scored by hidden verifier

### Step 2: Compute planar phase invariants and spin Hall conductance
- Role: scored
- Action:
  Implement the Green's function for the time‑reversal‑invariant planar phase.

  **Planar phase inverse Green's function** (4×4 matrices):

  G⁻¹(p₀,p_x,p_y) = i p₀ I₄ + (τ₃⊗I₂) (p²/(2m)−μ) + c τ₁ (σ_x p_x + σ_y p_y)

  Again G = (G⁻¹)⁻¹.

  **Symmetry‑protected invariant N_K** – same trace formula with an extra K‑matrix insertion (cf. Eq. (6) of the paper):

  N_K = (e_{ijk} / (24π²)) · Tr ∫ d³p  K · G(p) ∂_{p_i} G⁻¹(p)  G(p) ∂_{p_j} G⁻¹(p)  G(p) ∂_{p_k} G⁻¹(p)

  where K = τ₃ σ_z (a 4×4 matrix). The notation K·(…) means matrix multiplication; the trace is over the full 4‑dimensional space.

  Compute N_K for μ>0 and μ<0 by numerical integration, then derive the spin Hall conductance from the μ>0 value:

  σ_{xy}^{spin} = N_K(μ>0) / (4π)

  Write the two N_K values and the conductance as floats into `/app/outputs/planar_invariants.json`.

- Output file: `/app/outputs/planar_invariants.json`
- Format: json
- Contract: JSON object with keys: 'N_K_mu_positive', 'N_K_mu_negative', 'spin_Hall_conductance', each a float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/topological_invariants.json`
- `/app/outputs/planar_invariants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### topological_invariants.json
- path: `/app/outputs/topological_invariants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Integer topological invariants N for μ>0 and μ<0 in the spinless and spinful chiral p-wave superfluid models.
- schema:
  - `type`: object
  - `required`:
    - `N_spinless_mu_positive`: float
    - `N_spinless_mu_negative`: float
    - `N_spinful_mu_positive`: float
    - `N_spinful_mu_negative`: float
  - `description`: Topological invariants for spinless and spinful chiral phases

### planar_invariants.json
- path: `/app/outputs/planar_invariants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Symmetry-protected invariant N_K for μ>0 and μ<0, and the spin Hall conductance σ_{xy}^{spin}=N_K/(4π) evaluated at μ>0.
- schema:
  - `type`: object
  - `required`:
    - `N_K_mu_positive`: float
    - `N_K_mu_negative`: float
    - `spin_Hall_conductance`: float
  - `description`: Planar phase invariants and derived spin Hall conductance

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "topological_invariants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "N_spinless_mu_positive": "float",
          "N_spinless_mu_negative": "float",
          "N_spinful_mu_positive": "float",
          "N_spinful_mu_negative": "float"
        },
        "description": "Topological invariants for spinless and spinful chiral phases"
      },
      "description": "Integer topological invariants N for μ>0 and μ<0 in the spinless and spinful chiral p-wave superfluid models."
    },
    {
      "file": "planar_invariants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "N_K_mu_positive": "float",
          "N_K_mu_negative": "float",
          "spin_Hall_conductance": "float"
        },
        "description": "Planar phase invariants and derived spin Hall conductance"
      },
      "description": "Symmetry-protected invariant N_K for μ>0 and μ<0, and the spin Hall conductance σ_{xy}^{spin}=N_K/(4π) evaluated at μ>0."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your two JSON files and extracts the six reported numbers. Each invariant is compared to the correct value (the paper's reported integer) using an absolute tolerance; the μ<0 values must be near zero. The spin Hall conductance is compared to both the expected analytic value derived from the correct N_K and to a direct numeric reference. The final reward is a weighted combination of these checks. Reporting a number without performing the integration will not match the required tolerance.