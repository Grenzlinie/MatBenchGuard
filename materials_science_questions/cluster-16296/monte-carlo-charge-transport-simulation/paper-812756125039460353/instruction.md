# Two-Band Polar Hole Transport: Effective Drift Mobility and Hall Factor from Boltzmann Equation

## Problem background
In p‑type polar semiconductors, the degenerate valence band (heavy‑ and light‑hole bands) and the symmetry properties of the hole wavefunctions influence carrier transport. Polar optical phonon scattering, especially the intervalley transitions between the two bands, strongly affects the drift mobility and the Hall coefficient. To investigate these effects theoretically, the present work solves the coupled two‑band Boltzmann equation to obtain the effective drift mobility, the light‑hole mobility, and the low‑field Hall factor as functions of the mass ratio and temperature.

## Approach
Implement a numerical solver for the two‑band Boltzmann transport equation with parabolic spherical bands. Include polar optical phonon scattering with both intra‑ and intervalley transitions, using the overlap factors that account for the p‑type symmetry of the hole wavefunctions. Solve the coupled difference equations for the distribution‑function corrections along x and y directions. From these solutions, compute the conductivity tensor components for heavy and light holes, then derive the reference heavy‑hole mobility μ₁, the effective drift mobility μ_eff, the light‑hole mobility μ₂, and the low‑field Hall factor r_H. The solver is run for a range of mass ratios r = m₁/m₂ and reduced temperatures γ = θ/T. The Hall factor calculation uses material parameters m₁=0.5m, m₂=0.068m, θ=418 K, κ∞=12.5, κ₀=10.9; the mobility ratios μ_eff/μ₁ and μ₂/μ₁ do not depend on the dielectric constants.

## Reproduction target
Compute three datasets: (a) the ratio μ_eff/μ₁ as a function of mass ratio r for reduced temperatures γ = 2, 3, 4, 5; (b) the ratio μ₂/μ₁ as a function of r at γ = 5; and (c) the low‑field Hall factor r_H as a function of γ for mass ratio r = 7.35. Output all curves in a single JSON file (`results.json`) with the structure described in the output contract.

## Assets

- Python 3: python3
- NumPy / SciPy: numpy scipy

## Workflow steps

### Step 1: Solve two-band Boltzmann transport model
- Role: process
- Action: Implement the coupled Boltzmann equation solver for a two-band model of holes with parabolic spherical bands. Include polar optical phonon scattering with intra- and intervalley overlap factors. Compute the distribution function corrections α_xi(ε), α_yi(ε) by solving the difference equations numerically, then compute conductivity components σ_xx, σ_xy for heavy and light holes, and derive the reference heavy-hole mobility μ_1, effective drift mobility μ_eff, light-hole mobility μ_2, and the low-field Hall factor r_H for a range of mass ratios r and reduced temperatures γ as required to produce the final tables. The material parameters for r_H are m1=0.5m, m2=0.068m, θ=418 K, κ∞=12.5, κ0=10.9; the mobility ratios μ_eff/μ_1 and μ_2/μ_1 are independent of dielectric constants.
- Evidence: none

### Step 2: Generate result curves
- Role: scored (load-bearing)
- Action: From the simulation results, compute and output the three datasets: (a) μ_eff/μ_1 as a function of r for γ=2,3,4,5, (b) μ_2/μ_1 as a function of r for γ=5, and (c) r_H as a function of γ for r=7.35 at low magnetic field. Write them as a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with three keys: 'mu_eff_mu1_vs_r' (list of objects with 'r', 'gamma', 'value'), 'mu2_mu1_vs_r' (list of objects with 'r', 'value' for gamma=5), 'rH_vs_gamma' (list of objects with 'gamma', 'value' for r=7.35).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Curves of effective drift mobility ratio, light-to-heavy hole mobility ratio, and Hall factor, computed from the two-band Boltzmann solver.
- schema:
  - `type`: object
  - `required`:
    - `mu_eff_mu1_vs_r`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `r`:
            - `type`: number
          - `gamma`:
            - `type`: number
          - `value`:
            - `type`: number
    - `mu2_mu1_vs_r`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `r`:
            - `type`: number
          - `value`:
            - `type`: number
    - `rH_vs_gamma`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `gamma`:
            - `type`: number
          - `value`:
            - `type`: number

Notes: The checker audits structural properties of the submitted curves (peak existence, monotonicity, asymptotic limits) against hidden tolerances derived from the paper's reported results; it does not recompute a numeric metric from the artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "mu_eff_mu1_vs_r": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "r": {
                  "type": "number"
                },
                "gamma": {
                  "type": "number"
                },
                "value": {
                  "type": "number"
                }
              }
            }
          },
          "mu2_mu1_vs_r": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "r": {
                  "type": "number"
                },
                "value": {
                  "type": "number"
                }
              }
            }
          },
          "rH_vs_gamma": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "gamma": {
                  "type": "number"
                },
                "value": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Curves of effective drift mobility ratio, light-to-heavy hole mobility ratio, and Hall factor, computed from the two-band Boltzmann solver."
    }
  ],
  "notes": "The checker audits structural properties of the submitted curves (peak existence, monotonicity, asymptotic limits) against hidden tolerances derived from the paper's reported results; it does not recompute a numeric metric from the artifact."
}
```

## How you are scored
A hidden verifier independently scores the artifact from each workflow stage and combines them by weight into a final reward. For `results.json`, the verifier reads your submitted arrays and compares them against reference curves derived from the original work. The comparison uses pointwise mean absolute error and checks structural properties such as the overall shape, monotonicity, and approximate magnitudes. Submissions that exhibit the correct physical behaviour earn full credit; the reward decreases as the deviation grows. Reporting the paper’s numbers without running the actual computation is not sufficient — the verifier checks that the submitted curves originate from a genuine implementation of the Boltzmann solver.
