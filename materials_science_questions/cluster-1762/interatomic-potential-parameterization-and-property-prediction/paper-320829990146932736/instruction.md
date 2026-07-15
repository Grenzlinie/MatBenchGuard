# Computation of Exchange Parameters and Frustration Line Condition for CdI2 via Alternated ANNNI Model and Interatomic Potentials

## Problem background
Layered crystals of the MX2 family, such as CdI2, display a large number of long-periodic polytypes whose stability arises from weak interactions between neighbouring three-layer X-M-X sandwiches. A microscopic understanding requires a Hamiltonian that captures these inter-sandwich couplings and the corresponding exchange parameters derived from interatomic potentials. The alternated ANNNI model, an extension of the ANNNI model with an alternating interaction term, has been proposed to account for the observed polytype sequences. The exchange parameters J1, J2, and K of this model depend on interlayer potential differences originating from Coulomb, van der Waals, and short-range repulsive forces. Determining these parameters is essential for explaining the observed polytype diversity and for testing whether the material is located on a special frustration line where many structures become degenerate.

## Approach
The interlayer energy is modelled by a partially ionic pair potential that includes Coulomb interactions between effective point charges, a Lennard-Jones-like R⁻¹² repulsive term (Born–Mayer), and a van der Waals R⁻⁶ attraction. Van der Waals constants are obtained from ionic polarizabilities via the Slater–Kirkwood formula. Interlayer potential differences ΔV_ss'(m) for anion–cation (XM), anion–anion (XX), and cation–cation (MM) pairs at specific inter-sandwich distances m are evaluated: the Coulomb contribution using an analytic exponential-formula derived from Madelung-type sums, and the van der Waals and repulsive contributions by performing numerical lattice sums over a triangular lattice. The exchange parameters J1, J2, K are then expressed as linear combinations of these potential differences. The frustration line condition J1 – 2J2 – K = 0 is imposed on the full potential (Coulomb + van der Waals + repulsive with unknown repulsive constants B_ss') to derive a linear relation B_XM = α + β (B_XX + B_MM). For the final exchange parameters it is assumed that B_XX = B_MM = α, and the equilibrium Cd–I bond length R₀ is determined from the vanishing derivative of the pair potential with the chosen constants.

## Reproduction target
For CdI₂ with effective charge z* = 0.58, polarizabilities α_I = 5.6×10⁻²⁴ cm³ and α_Cd = 2.4×10⁻²⁴ cm³, lattice constants a = 4.244 Å and c = 3.430 Å (γ = c/a = 0.808), perform the following computations and save the results in atomic units:
- Exchange parameters J1, J2, K and their ratios J2/J1, K/J1 using the Coulomb potential alone (coulomb_results.json).
- Exchange parameters J1, J2, K and their ratios J2/J1, K/J1 using the Coulomb plus van der Waals contributions, without repulsion (vdw_results.json).
- The frustration-line relation coefficients α and β, the final exchange parameters J1, J2, K and their ratios assuming B_XX = B_MM = α, as well as the equilibrium Cd–I bond length R₀ derived from the full pair potential (full_results.json).

## Assets
No external datasets, models, or pre‑trained artifacts are required. All physical constants (effective charges, polarizabilities, lattice parameters) are taken from the literature and are listed in the problem description and workflow steps. The agent needs a Python environment with standard scientific libraries (numpy, scipy) to perform the lattice sums and the one‑dimensional root‑finding for the bond length.

## Workflow steps

### Step 1: Compute van der Waals constants
- Role: process
- Action: Using the reported polarizabilities α_I=5.6×10⁻²⁴ cm³ and α_Cd=2.4×10⁻²⁴ cm³, compute the van der Waals constants C_XX, C_XM, C_MM (in atomic units) via the Slater–Kirkwood formula.
- Evidence: `/app/outputs/vdw_constants.json`

### Step 2: Compute Coulomb potential differences ΔVᶻ
- Role: process
- Action: Using effective charges z*_Cd=2z*, z*_I=-z* (z*=0.58) and lattice parameters a=4.244 Å, c=3.430 Å, γ=c/a=0.808, evaluate the analytic Coulomb potential differences ΔVᶻ_{ss'}(m) for distances m = 3/2, 5/2, 2 (XX and MM), and 3 (XX) via the leading exponential terms of the analytical Madelung-type formula.
- Evidence: `/app/outputs/coulomb_potentials.json`

### Step 3: Compute van der Waals potential differences ΔVᶜ by lattice sum
- Role: process
- Action: Perform numerical summation of the R⁻⁶ potential over a triangular lattice (up to ~2×10⁴ atoms per layer) for the distances m = 3/2, 5/2, 2, 3 using the van der Waals constants from step 0 and the lattice geometry. Obtain ΔVᶜ_{ss'}(m).
- Evidence: `/app/outputs/vdw_potentials.json`

### Step 4: Compute repulsive lattice-sum coefficients for ΔVᵇ
- Role: process
- Action: Perform numerical summation of the R⁻¹² potential over the same triangular lattice for the same m values to obtain the linear coefficients f_{ss'}(m) such that ΔVᵇ_{ss'}(m) = B_{ss'} × f_{ss'}(m).
- Evidence: `/app/outputs/repulsive_coeffs.json`

### Step 5: Compute exchange parameters (Coulomb only)
- Role: scored
- Action: From the Coulomb ΔVᶻ values obtained in step 1, compute J₁, J₂, K using the relation that expresses these exchange parameters as linear combinations of potential differences. Save the results together with the ratios J₂/J₁ and K/J₁.
- Output file: `/app/outputs/coulomb_results.json`
- Format: json
- Contract: object with number keys: J1_a.u., J2_a.u., K_a.u., J2_over_J1, K_over_J1
- Scoring: scored by hidden verifier

### Step 6: Compute exchange parameters (Coulomb + van der Waals)
- Role: scored
- Action: Combine the Coulomb ΔVᶻ (step 1) and van der Waals ΔVᶜ (step 2) contributions, then compute J₁, J₂, K via the same relation as in step 4. Save the parameters and the ratios J₂/J₁, K/J₁.
- Output file: `/app/outputs/vdw_results.json`
- Format: json
- Contract: object with number keys: J1_a.u., J2_a.u., K_a.u., J2_over_J1, K_over_J1
- Scoring: scored by hidden verifier

### Step 7: Derive frustration-line relation for Born–Mayer constants
- Role: process
- Action: Insert the full ΔV (Coulomb + vdW + repulsive with unknown B_{ss'}) into the frustration-line condition J₁−2J₂−K = 0. Solve for B_XM as a linear function of B_XX and B_MM, obtaining numerical coefficients α and β for CdI₂.
- Evidence: `/app/outputs/linear_relation.json`

### Step 8: Compute full exchange parameters and equilibrium bond length
- Role: scored (load-bearing)
- Action: Assume B_XX = B_MM = α (using α from step 6) and set B_XM = α. Evaluate the total ΔV (Coulomb+vdW+repulsive) using the coefficients from steps 1–3 to obtain the final J₁, J₂, K via the same relation as in step 4. Also compute the equilibrium Cd–I bond length R₀ from the condition dW/dR = 0 using the full pair potential W(R) with the chosen B_XM. Save all quantities.
- Output file: `/app/outputs/full_results.json`
- Format: json
- Contract: object with number keys: J1_a.u., J2_a.u., K_a.u., J2_over_J1, K_over_J1, alpha_a.u., beta_a.u., B_XX_au, B_MM_au, B_XM_au, R0_au
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coulomb_results.json`
- `/app/outputs/vdw_results.json`
- `/app/outputs/full_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coulomb_results.json
- path: `/app/outputs/coulomb_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Exchange parameters and their ratios when only the Coulomb component is included.
- schema:
  - `type`: object
  - `required`: `J1_a.u.`, `J2_a.u.`, `K_a.u.`, `J2_over_J1`, `K_over_J1`
  - `properties`:
    - `J1_a.u.`:
      - `type`: number
    - `J2_a.u.`:
      - `type`: number
    - `K_a.u.`:
      - `type`: number
    - `J2_over_J1`:
      - `type`: number
    - `K_over_J1`:
      - `type`: number

### vdw_results.json
- path: `/app/outputs/vdw_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Exchange parameters and their ratios when Coulomb and van der Waals interactions are included.
- schema:
  - `type`: object
  - `required`: `J1_a.u.`, `J2_a.u.`, `K_a.u.`, `J2_over_J1`, `K_over_J1`
  - `properties`:
    - `J1_a.u.`:
      - `type`: number
    - `J2_a.u.`:
      - `type`: number
    - `K_a.u.`:
      - `type`: number
    - `J2_over_J1`:
      - `type`: number
    - `K_over_J1`:
      - `type`: number

### full_results.json
- path: `/app/outputs/full_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Final exchange parameters including repulsion, the frustration-line coefficients α and β, the chosen Born–Mayer constants, and the derived equilibrium Cd–I bond length.
- schema:
  - `type`: object
  - `required`: `J1_a.u.`, `J2_a.u.`, `K_a.u.`, `J2_over_J1`, `K_over_J1`, `alpha_a.u.`, `beta_a.u.`, `B_XX_au`, `B_MM_au`, `B_XM_au`, `R0_au`
  - `properties`:
    - `J1_a.u.`:
      - `type`: number
    - `J2_a.u.`:
      - `type`: number
    - `K_a.u.`:
      - `type`: number
    - `J2_over_J1`:
      - `type`: number
    - `K_over_J1`:
      - `type`: number
    - `alpha_a.u.`:
      - `type`: number
    - `beta_a.u.`:
      - `type`: number
    - `B_XX_au`:
      - `type`: number
    - `B_MM_au`:
      - `type`: number
    - `B_XM_au`:
      - `type`: number
    - `R0_au`:
      - `type`: number

Notes: All quantities are in atomic units unless otherwise indicated. The verification recomputes each quantity from the same analytic formulas and lattice sums and compares relative error.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coulomb_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "J1_a.u.",
          "J2_a.u.",
          "K_a.u.",
          "J2_over_J1",
          "K_over_J1"
        ],
        "properties": {
          "J1_a.u.": {
            "type": "number"
          },
          "J2_a.u.": {
            "type": "number"
          },
          "K_a.u.": {
            "type": "number"
          },
          "J2_over_J1": {
            "type": "number"
          },
          "K_over_J1": {
            "type": "number"
          }
        }
      },
      "description": "Exchange parameters and their ratios when only the Coulomb component is included."
    },
    {
      "file": "vdw_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "J1_a.u.",
          "J2_a.u.",
          "K_a.u.",
          "J2_over_J1",
          "K_over_J1"
        ],
        "properties": {
          "J1_a.u.": {
            "type": "number"
          },
          "J2_a.u.": {
            "type": "number"
          },
          "K_a.u.": {
            "type": "number"
          },
          "J2_over_J1": {
            "type": "number"
          },
          "K_over_J1": {
            "type": "number"
          }
        }
      },
      "description": "Exchange parameters and their ratios when Coulomb and van der Waals interactions are included."
    },
    {
      "file": "full_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "J1_a.u.",
          "J2_a.u.",
          "K_a.u.",
          "J2_over_J1",
          "K_over_J1",
          "alpha_a.u.",
          "beta_a.u.",
          "B_XX_au",
          "B_MM_au",
          "B_XM_au",
          "R0_au"
        ],
        "properties": {
          "J1_a.u.": {
            "type": "number"
          },
          "J2_a.u.": {
            "type": "number"
          },
          "K_a.u.": {
            "type": "number"
          },
          "J2_over_J1": {
            "type": "number"
          },
          "K_over_J1": {
            "type": "number"
          },
          "alpha_a.u.": {
            "type": "number"
          },
          "beta_a.u.": {
            "type": "number"
          },
          "B_XX_au": {
            "type": "number"
          },
          "B_MM_au": {
            "type": "number"
          },
          "B_XM_au": {
            "type": "number"
          },
          "R0_au": {
            "type": "number"
          }
        }
      },
      "description": "Final exchange parameters including repulsion, the frustration-line coefficients α and β, the chosen Born–Mayer constants, and the derived equilibrium Cd–I bond length."
    }
  ],
  "notes": "All quantities are in atomic units unless otherwise indicated. The verification recomputes each quantity from the same analytic formulas and lattice sums and compares relative error."
}
```

## How you are scored
A hidden verifier independently implements the same analytic formulas and numerical lattice sums, recomputes the quantities requested in the scored output files, and compares them to the values you report. Each scored artifact contributes a weighted fraction to the total reward, with the final exchange parameters (full_results.json) carrying the largest weight. The comparison uses relative error metrics: the smaller the deviation from the reference, the higher the score. There is no penalty for results that are more accurate than required. Simply reporting a number from the paper without a genuine computation will fail because the verifier performs its own independent calculation.
