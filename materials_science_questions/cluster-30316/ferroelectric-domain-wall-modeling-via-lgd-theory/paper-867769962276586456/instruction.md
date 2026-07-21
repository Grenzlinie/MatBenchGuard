# Domain Wall Energy Anisotropy in Uniaxial Trigonal Ferroelectrics

## Problem background
Uniaxial trigonal ferroelectrics lithium niobate (LiNbO₃) and lithium tantalate (LiTaO₃) exhibit 180° ferroelectric domain walls. The preferred orientations of these walls (y‑walls vs x‑walls) differ between stoichiometric and congruent compositions, but the intrinsic crystallographic contribution is not fully established. A phenomenological Ginzburg‑Landau‑Devonshire (GLD) theory for a single domain wall can predict the wall free energy as a function of orientation. This task is to compute the total free energy per unit volume for a 180° domain wall for 12 crystallographic orientations in both LiNbO₃ and LiTaO₃, and thereby determine which orientations constitute the global energy minima.

## Approach
The GLD free energy for a uniaxial trigonal ferroelectric (point group 3m) is constructed with the primary order parameter being the polarization along the crystallographic z‑axis, P_z. In the rotated coordinate system where the wall normal makes an angle θ with the x‑axis, the free energy density (including Landau, elastic, electrostrictive, and gradient terms) depends on θ. Minimization with respect to strain compatibility and mechanical equilibrium yields expressions for the secondary order parameters (in‑plane polarizations P_n, P_t and strain deviations Δε_n, ε̃_5, ε̃_6) as polynomial functions of P_z. The primary order parameter profile across the wall is approximated by a tanh kink: P_z(x) = P_h · tanh(x/x₀), where P_h is the spontaneous polarization and x₀ is a wall half‑width determined from the experimentally known upper bound of wall width (2x₀ = 0.28 nm) and the relation x₀² = 4g₁/ζ₁. The gradient coefficient g₁ is thus estimated. For each orientation θ, the total free energy per unit volume is obtained by integrating the free‑energy density across the wall window and adding the depolarization energy arising from the divergence of P_n. The computation is performed for both stoichiometric LiNbO₃ and LiTaO₃ using the room‑temperature material constants provided below.

Material constants (from published experimental measurements):

| Constant | LiTaO₃ value | LiNbO₃ value | Units |
|----------|--------------|--------------|-------|
| P_s (spontaneous polarization) | 0.50 – 0.55 | 0.70 – 0.75 | C/m² |
| ε₁₁ | 52.7 | 84.3 | – |
| ε₃₃ | 44.0 | 28.9 | – |
| C₁₁ | 2.3305×10¹¹ | 1.9886×10¹¹ | N/m² |
| C₁₂ | 0.4644×10¹¹ | 0.5467×10¹¹ | N/m² |
| C₁₃ | 0.8358×10¹¹ | 0.6726×10¹¹ | N/m² |
| C₃₃ | 2.7414×10¹¹ | 2.3370×10¹¹ | N/m² |
| C₁₄ | -1.067×10¹¹ | 0.0783×10¹¹ | N/m² |
| C₄₄ | 0.9526×10¹¹ | 0.5985×10¹¹ | N/m² |
| Q₃₁ | -0.00485 | -0.003 | m⁴/C² |
| Q₃₃ | 0.016 | 0.016 | m⁴/C² |
| Q₄₂ | 0.016 | -0.003 | m⁴/C² |
| Q₄₄ | 0.056 | 0.0375 | m⁴/C² |

Note: the spontaneous polarization P_s in the table gives a range; use P_s = 0.525 C/m² for LiTaO₃ and P_s = 0.725 C/m² for LiNbO₃ as representative central values.

## Reproduction target
Compute the total domain wall free energy per unit volume F_total(θ) = F_DW(θ) + F_d(θ) for both stoichiometric LiNbO₃ and LiTaO₃ at wall normal orientations θ = 0°, 30°, 60°, …, 330° (twelve orientations in 30° steps). Output the results in a CSV file `domain_wall_energies.csv` with columns `material`, `theta_deg`, `F_DW_J_m3`, `F_d_J_m3`, `F_total_J_m3` (all energy values rounded to six significant figures, units of J/m³). The hidden verifier will assess the structural energy landscape: which orientations give the global minima, how the average energy of one set of orientations compares to another, and whether symmetry‑equivalent orientations produce consistent energies.

## Assets
No external datasets or model files are required. All necessary material constants are listed in the Approach section above. The computational workflow requires only standard numerical and scientific libraries (e.g., Python 3 with NumPy, SciPy), which are publicly available.

## Workflow steps

### Step 1: Compute derived LGD coefficients and secondary-order parameters
- Role: process
- Action: Using the material constants provided in the instruction, compute the derived Landau-Ginzburg-Devonshire coefficients (α₁,α₂,α₃,β₁–β₆,γ₁–γ₄), the homogeneous spontaneous polarization Pₕ and homogeneous strains λ₁,λ₂. Then for each wall orientation angle θ = 0°,30°,…,330°, compute the auxiliary constants (ν_i, μ_ij), the matrices ρ_ij and φ_ij (polynomial expansions for in-plane polarizations and strain deviations), and the truncated Euler-Lagrange coefficients ζ₁,ζ₃. Save all coefficient arrays in a JSON file.
- Evidence: `/app/outputs/coefficients.json`

### Step 2: Compute primary-order parameter profile and secondary fields
- Role: process
- Action: Estimate the gradient coefficient g₁ from the experimentally known upper limit of wall width (2x₀ = 0.28 nm) and the relation x₀² = 4g₁/ζ₁. Construct the tanh kink profile P_z(xₙ) = Pₕ·tanh(xₙ/x₀) on a grid spanning [-2x₀, 2x₀] with at least 200 points. For each orientation θ, use the polynomial expansions from step1 to compute the secondary order parameters (Pₙ, Pₜ, Δεₙ, ε̃₅, ε̃₆) at each grid point. Save the grid and all field profiles to a JSON file.
- Evidence: `/app/outputs/wall_profile.json`

### Step 3: Compute domain wall energies and orientation preference
- Role: scored (load-bearing)
- Action: For each material (LiNbO₃, LiTaO₃) and each orientation θ, evaluate the total free-energy density (including gradient term) at every grid point from step2, numerically integrate across the wall window to obtain F_DW(θ) in J/m³. Compute the depolarization energy F_d(θ) from the Pₙ profile using F_d = (1/Δx)∫(Pₙ²/(2ε₀))dxₙ. Sum to obtain F_total = F_DW + F_d. Write the results to a CSV file with columns material, theta_deg, F_DW_J_m3, F_d_J_m3, F_total_J_m3, all values rounded to six significant figures.
- Output file: `/app/outputs/domain_wall_energies.csv`
- Format: csv
- Contract: CSV file with header: material,theta_deg,F_DW_J_m3,F_d_J_m3,F_total_J_m3. Each row corresponds to one orientation (0,30,…,330 degrees) for one material. All numeric columns are floating-point numbers in units of J/m³.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/domain_wall_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### domain_wall_energies.csv
- path: `/app/outputs/domain_wall_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Domain wall free energy per unit volume for LiNbO₃ and LiTaO₃ at 12 wall orientations (0° to 330° in 30° steps). Validates the structural property that y-walls are the global energy minima.
- schema:
  - `type`: table
  - `required_columns`: `material`, `theta_deg`, `F_DW_J_m3`, `F_d_J_m3`, `F_total_J_m3`
  - `units`:
    - `F_DW_J_m3`: J/m^3
    - `F_d_J_m3`: J/m^3
    - `F_total_J_m3`: J/m^3

Notes: The hidden checker verifies that the six global minima of F_total occur at θ = 0°,60°,120°,180°,240°,300° (y-wall normals), that the average F_total at these angles is lower than the average at the x-wall normals (30°,90°,…,330°), and that symmetry-related values are equal within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "domain_wall_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "theta_deg",
          "F_DW_J_m3",
          "F_d_J_m3",
          "F_total_J_m3"
        ],
        "units": {
          "F_DW_J_m3": "J/m^3",
          "F_d_J_m3": "J/m^3",
          "F_total_J_m3": "J/m^3"
        }
      },
      "description": "Domain wall free energy per unit volume for LiNbO₃ and LiTaO₃ at 12 wall orientations (0° to 330° in 30° steps). Validates the structural property that y-walls are the global energy minima."
    }
  ],
  "notes": "The hidden checker verifies that the six global minima of F_total occur at θ = 0°,60°,120°,180°,240°,300° (y-wall normals), that the average F_total at these angles is lower than the average at the x-wall normals (30°,90°,…,330°), and that symmetry-related values are equal within a tolerance."
}
```

## How you are scored
A hidden verifier will load your `domain_wall_energies.csv` and evaluate several structural criteria:
- Whether the six global minima of F_total appear at a specific set of wall orientations (y‑wall normals).
- Whether the average F_total over those orientations is lower than the average over the complementary set (x‑wall normals).
- Whether F_total values at symmetry‑related orientations (e.g., 0° and 60°) are equal within a tolerance.
Each criterion contributes a pre‑determined weight to a total score between 0 and 1. The verifier does not compare your computed absolute energy numbers to published values; it checks the orientation‑dependent energy landscape you produce. Merely reporting numbers that satisfy the structural properties is sufficient; no external data or model file is required beyond the constants provided in the instruction.
