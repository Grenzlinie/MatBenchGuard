# Compute Exchange Parameters and Frustration Condition for CdI₂ from Interatomic Potentials

## Problem background
Layered MX₂ crystals (e.g., CdI₂) exhibit polytypism—many stacking variants—arising from competition between interlayer interactions. A statistical-mechanical model, the alternated ANNNI model, describes the stacking energetics with exchange parameters J₁, J₂, K that are determined by interatomic potentials. The target is to compute these parameters from a partially ionic interatomic potential and then derive the condition for the frustration line that separates the ⟨1⟩ and ⟨2⟩ phases. This condition places a linear relation between the Born–Mayer repulsion constants, and from it an estimate of the equilibrium Cd–I bond length can be obtained.

## Approach
The interlayer potential is approximated as a sum of Coulomb (point charges), van der Waals (R⁻⁶), and Born–Mayer repulsion (R⁻¹²) contributions. For the CdI₂ compound, the effective charges and polarizabilities are taken from experimental data, and the van der Waals C constants are computed via the Slater–Kirkwood formula. The differences in interaction energy between layers in different stacking positions, ΔV_{ss'}(m) for specific distances m, are obtained analytically for the Coulomb part (using a rapidly converging series) and numerically via lattice sums over a triangular lattice for the van der Waals and repulsive parts. The exchange parameters J₁, J₂, K are then expressed as linear combinations of these ΔV terms. The condition J₁ − 2J₂ − K = 0 (frustration line between the ⟨1⟩ and ⟨2⟩ phases) is used to derive a linear relation between the repulsion constants B_XM, B_XX, B_MM. Finally, under the assumption that all B constants are of comparable magnitude, the equilibrium nearest-neighbour Cd–I distance R₀ is obtained from the interatomic potential by minimizing the energy with B_XM set to the leading constant α.

## Reproduction target
For CdI₂, using the given parameters:
- effective charges z*_I = -0.58, z*_Cd = 1.16
- polarizabilities α_I = 5.6×10⁻²⁴ cm³, α_Cd = 2.4×10⁻²⁴ cm³
- lattice constants a = 4.244 Å, c = 3.430 Å, γ = c/a = 0.808
- the computed van der Waals constants C_XX, C_XM, C_MM (from Slater–Kirkwood)
carry out the following:

1. **Compute the Coulomb-only exchange parameters** J₁, J₂/J₁, K/J₁ as an intermediate check.
2. **Assemble the full interlayer potential differences** from Coulomb, van der Waals, and repulsive contributions, then **derive the linear relation B_XM = α + β (B_XX + B_MM)** that results from imposing the frustration line condition J₁ − 2J₂ − K = 0. Save α and β.
3. **Assuming B_XX ≈ α (so B_XM ≈ α), find the equilibrium Cd–I bond length R₀** that minimizes the interatomic potential W(R) = (z*_Cd)(z*_I)/R + B_XM/R¹² + C_XM/R⁶.

The primary scored outputs are the coefficients α and β, and the equilibrium bond length R₀. The intermediate Coulomb-exchange parameters are also scored to verify the pipeline.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute van der Waals C constants
- Role: process
- Action: Using the given polarizabilities α_I = 5.6×10⁻²⁴ cm³, α_Cd = 2.4×10⁻²⁴ cm³, compute the van der Waals constants C_XX, C_XM, C_MM via the Slater–Kirkwood formula. Output these constants in atomic units.
- Evidence: `/app/outputs/c_constants.json`

### Step 2: Coulomb potential differences
- Role: process
- Action: Using the analytical formula ΔV_{ss'}^z(m) = - (9 z_s^* z_{s'}^*) / (c γ^3) [ exp(-4π/√3 γ m) + 1/2 exp(-8π/√3 γ m) + 2/√7 exp(-4π √(7/3) γ m) + ... ] (m in units of c; keep the first three terms for convergence), compute the Coulomb potential differences ΔV^z for the following interactions: X–M at m = 3/2, X–M at m = 5/2, X–X at m = 2, M–M at m = 2, and X–X at m = 3. Use effective charges z_I^* = -0.58, z_Cd^* = 1.16, lattice constants c = 3.430 Å, γ = c/a = 0.808. Express results in atomic units per atom.
- Evidence: `/app/outputs/deltaV_z.json`

### Step 3: van der Waals potential differences via lattice sums
- Role: process
- Action: Perform numeric lattice sums for the R⁻⁶ potential over a triangular lattice (lattice parameters a=4.244 Å, c=3.430 Å, γ=0.808) for the same four distances/interactions, using the computed C constants. Compute ΔV^C for each term.
- Evidence: `/app/outputs/deltaV_C.json`

### Step 4: Repulsive potential difference coefficients via lattice sums
- Role: process
- Action: Perform numeric lattice sums for the R⁻¹² potential to obtain the coefficients multiplying the Born–Mayer constants B_XX, B_XM, B_MM in ΔV^B for the same four distances.
- Evidence: `/app/outputs/deltaV_B_coeffs.json`

### Step 5: Compute Coulomb-only exchange parameters
- Role: scored
- Action: Using only the Coulomb ΔV^z values computed in Step 2, evaluate the exchange parameters J₁, J₂, and K according to:
  J₁ = ½ [ ΔV_{XM}(3/2) - ΔV_{XX}(2) - ½ ΔV_{MM}(2) + ΔV_{XX}(3) ]
  J₂ = ¼ ΔV_{XX}(3)
  K  = ¼ ΔV_{MM}(2) - ½ ΔV_{XM}(5/2)
  All ΔV are the Coulomb potential differences from Step 2, in atomic units per atom. Then output J₁, J₂/J₁, K/J₁.
- Output file: `/app/outputs/coulomb_exchange.json`
- Format: json
- Contract: {"J1": <float>, "J2_over_J1": <float>, "K_over_J1": <float>} (atomic units)
- Scoring: scored by hidden verifier

### Step 6: Derive frustration condition linear relation
- Role: scored (load-bearing)
- Action: Assemble the full ΔV = ΔV^z + ΔV^C + ΔV^B (keeping B_XX, B_XM, B_MM as variables) into J₁, J₂, K, impose the frustration line condition J₁ − 2J₂ − K = 0, and solve for the linear relation B_XM = α + β(B_XX + B_MM). Output α and β.
- Output file: `/app/outputs/linear_coefficients.json`
- Format: json
- Contract: {"alpha": <float>, "beta": <float>} (atomic units)
- Scoring: scored by hidden verifier

### Step 7: Compute equilibrium bond length from repulsion constant
- Role: scored
- Action: Assume B_XM ≈ α and set B_XM = α. Using the interatomic potential W(R) = (z*_Cd)(z*_I)/R + B_XM/R¹² + C_XM/R⁶, solve the equilibrium condition dW/dR = 0 to find the Cd–I bond length R₀. Output R₀ in atomic units as a plain number.
- Output file: `/app/outputs/bond_length.txt`
- Format: txt
- Contract: single float (atomic units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coulomb_exchange.json`
- `/app/outputs/linear_coefficients.json`
- `/app/outputs/bond_length.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coulomb_exchange.json
- path: `/app/outputs/coulomb_exchange.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Coulomb-only exchange parameters J₁, J₂/J₁, K/J₁.
- schema:
  - `type`: object
  - `required`:
    - `J1`: float (atomic units)
    - `J2_over_J1`: float (dimensionless)
    - `K_over_J1`: float (dimensionless)

### linear_coefficients.json
- path: `/app/outputs/linear_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Coefficients α, β of the linear relation B_XM = α + β(B_XX + B_MM).
- schema:
  - `type`: object
  - `required`:
    - `alpha`: float (atomic units)
    - `beta`: float (dimensionless)

### bond_length.txt
- path: `/app/outputs/bond_length.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Equilibrium Cd–I bond length R₀.
- schema:
  - `type`: text
  - `content`: single float (atomic units)

Notes: All physical quantities in atomic units unless noted. The scored outputs are checked by the hidden verifier; the exact gold values are not part of the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coulomb_exchange.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "J1": "float (atomic units)",
          "J2_over_J1": "float (dimensionless)",
          "K_over_J1": "float (dimensionless)"
        }
      },
      "description": "Coulomb-only exchange parameters J₁, J₂/J₁, K/J₁."
    },
    {
      "file": "linear_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha": "float (atomic units)",
          "beta": "float (dimensionless)"
        }
      },
      "description": "Coefficients α, β of the linear relation B_XM = α + β(B_XX + B_MM)."
    },
    {
      "file": "bond_length.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content": "single float (atomic units)"
      },
      "description": "Equilibrium Cd–I bond length R₀."
    }
  ],
  "notes": "All physical quantities in atomic units unless noted. The scored outputs are checked by the hidden verifier; the exact gold values are not part of the public contract."
}
```

## How you are scored
Your outputs are evaluated by a hidden verifier that compares your submitted values to reference values obtained from the same computational procedure, using tolerances that allow for typical differences between independent implementations of lattice sums. Each scored artifact contributes a weight to the final score. To succeed, you must faithfully implement the required calculations; simply reporting plausible numbers without computation is unlikely to pass.
