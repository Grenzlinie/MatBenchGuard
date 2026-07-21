# Ferroelectric Domain Wall Energies and Activation Energies via LGD Theory

## Problem background
Ferroelectric domain walls are transition layers where the spontaneous polarization changes gradually from one orientation to the opposite. Understanding these walls requires three key quantities: the polarization profile, the energy needed to create the wall (domain wall energy), and the energy required to displace the wall from a lattice site (activation energy, also called the Peierls energy). This task studies these quantities using Landau-Ginzburg-Devonshire theory, which models the free energy as a sum of a local homogeneous part (a polynomial in polarization p) and a gradient term penalizing spatial variations. Two types of ferroelectric transitions are considered: second-order, described by a p^4 potential, and first-order, described by a p^6 potential. For each case, both continuum field theory and discrete lattice models are employed. The continuum approach yields closed-form expressions for the wall profile and energy, while the discrete model, which replaces derivatives with finite differences, must be solved numerically and gives distinct on-site and off-site wall configurations. The activation energy is then derived from the continuum energy density via the Poisson sum formula. Your job is to implement the necessary formulas and numerical solvers to compute these energies for a given set of material parameters.

## Approach
You will work with two potentials:

**p^4 (second-order transition):**
The free-energy density is
`f = (α/2)p² + (β/4)p⁴ + (κ/2)(dp/dx)²`,
with α < 0, β > 0, κ > 0. The equilibrium polarization far from the wall is p_s = √(−α/β). Minimising the total energy yields an Euler–Lagrange equation that can be integrated analytically. Its solution gives the polarization profile p(x) = p_s tanh(Kx) with K = √(−α/(2κ)). The domain wall energy is the integral of the excess energy density; you will evaluate the closed-form result for that integral.

For the discrete model, replace the derivative by a forward difference: (p_n − p_{n−1})/a, and minimise the resulting total energy
`F = a Σ_n [ (α/2)p_n² + (β/4)p_n⁴ + (κ/(2a²))(p_n − p_{n−1})² − f_0 ]`.
The Euler–Lagrange difference equation must be solved numerically. Two solutions exist: on‑site (p_n = −p_{−n}, p₀=0) and off‑site (p_n = −p_{−n+1}). For each you compute the discrete wall energy.

**p^6 (first-order transition):**
The free energy adds a p⁶ term:
`f = (α/2)p² + (β/4)p⁴ + (γ/6)p⁶ + (κ/2)(dp/dx)²`,
with α < 3β²/(16γ), β < 0, γ > 0. The equilibrium condition α + β p_s² + γ p_s⁴ = 0 determines p_s. The continuum polarization profile and wall energy have more complicated closed forms; you will implement these formulas. For the discrete case, the difference equation includes a p_n⁵ term, again solved numerically for on‑site and off‑site configurations.

**Activation energy:**
The activation energy ΔW is the difference between on‑site and off‑site wall energies. For thick walls it can be approximated analytically from the continuum energy density using the Poisson sum formula. You will evaluate the resulting asymptotic expressions for both the p⁴ and p⁶ potentials.

## Reproduction target
Implement the continuum and discrete models described above and compute the following quantities:

- For the p⁴ potential with parameters α=−1, β=1, κ=0.5, a=1:
  - continuum wall energy
  - discrete on‑site wall energy
  - discrete off‑site wall energy
  - activation energy (analytic asymptotics)

- For the p⁶ potential with parameters α=−1, β=−1, γ=1, a=1, and two gradient-coefficient values:
  - thick wall (κ=4): continuum wall energy, discrete on‑site and off‑site wall energies, activation energy
  - thin wall (κ=0.5): continuum wall energy, discrete on‑site and off‑site wall energies, activation energy

Assemble all twelve floating‑point values into a single JSON file `/app/outputs/computed_energies.json` with the fields: p4_continuum_wall_energy, p4_on_site_wall_energy, p4_off_site_wall_energy, p4_activation_energy, p6_thick_continuum_wall_energy, p6_thick_on_site_wall_energy, p6_thick_off_site_wall_energy, p6_thick_activation_energy, p6_thin_continuum_wall_energy, p6_thin_on_site_wall_energy, p6_thin_off_site_wall_energy, p6_thin_activation_energy.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Continuum p^4 wall energy
- Role: process
- Action: Compute the analytic continuum domain wall energy for the second-order (p^4) model using the Landau-Ginzburg-Devonshire free energy functional. Use parameters α=-1, β=1, κ=0.5. Derive or evaluate the closed-form expression for the wall energy (obtained from the polarization profile p=p_s tanh(Kx) and the energy density integral). Save the computed scalar value to evidence_p4_continuum.txt.
- Evidence: `/app/outputs/evidence_p4_continuum.txt`

### Step 2: Discrete p^4 on/off-site energies
- Role: process
- Action: Numerically solve the discrete difference equation for the p^4 model with lattice constant a=1, parameters α=-1, β=1, κ=0.5. Obtain on-site (odd symmetry, center on lattice point) and off-site (even symmetry, center between lattice points) polarization profiles, and compute the corresponding wall energies W(on-site) and W(off-site). Save both scalar values to evidence_p4_discrete.txt.
- Evidence: `/app/outputs/evidence_p4_discrete.txt`

### Step 3: Continuum p^6 wall energy
- Role: process
- Action: Compute the analytic continuum domain wall energy for the first-order (p^6) model using the free energy functional with parameters α=-1, β=-1, γ=1. Evaluate the closed-form wall energy expression for two gradient coefficient values: κ=4 (thick wall) and κ=0.5 (thin wall). Save both scalar values to evidence_p6_continuum.txt.
- Evidence: `/app/outputs/evidence_p6_continuum.txt`

### Step 4: Discrete p^6 on/off-site energies
- Role: process
- Action: Numerically solve the discrete difference equation for the p^6 model with a=1, α=-1, β=-1, γ=1, for κ=4 (thick wall) and κ=0.5 (thin wall). For each κ obtain the on-site and off-site wall profiles and compute the corresponding wall energies. Save all four scalar values to evidence_p6_discrete.txt.
- Evidence: `/app/outputs/evidence_p6_discrete.txt`

### Step 5: Analytical activation energy p^4
- Role: process
- Action: Evaluate the closed-form analytic expression for the activation energy (Peierls energy) of a thick p^4 domain wall, obtained from the Poisson sum formula applied to the continuum energy density. Use parameters α=-1, β=1, κ=0.5, a=1. Save the scalar activation energy to evidence_p4_act.txt.
- Evidence: `/app/outputs/evidence_p4_act.txt`

### Step 6: Analytical activation energy p^6
- Role: process
- Action: Evaluate the analytic activation energy expression for the p^6 model, including the oscillating factor originating from poles off the imaginary axis. Use parameters α=-1, β=-1, γ=1, a=1, and compute for both κ=4 (thick wall) and κ=0.5 (thin wall). Save both scalar activation energies to evidence_p6_act.txt.
- Evidence: `/app/outputs/evidence_p6_act.txt`

### Step 7: Assemble scored output
- Role: scored (load-bearing)
- Action: Read all evidence files from steps 1–6 and aggregate the numerical values into a single JSON file /app/outputs/computed_energies.json. The JSON must contain exactly the following floating-point fields: p4_continuum_wall_energy, p4_on_site_wall_energy, p4_off_site_wall_energy, p4_activation_energy, p6_thick_continuum_wall_energy, p6_thick_on_site_wall_energy, p6_thick_off_site_wall_energy, p6_thick_activation_energy, p6_thin_continuum_wall_energy, p6_thin_on_site_wall_energy, p6_thin_off_site_wall_energy, p6_thin_activation_energy.
- Output file: `/app/outputs/computed_energies.json`
- Format: json
- Contract: {"p4_continuum_wall_energy": float, "p4_on_site_wall_energy": float, "p4_off_site_wall_energy": float, "p4_activation_energy": float, "p6_thick_continuum_wall_energy": float, "p6_thick_on_site_wall_energy": float, "p6_thick_off_site_wall_energy": float, "p6_thick_activation_energy": float, "p6_thin_continuum_wall_energy": float, "p6_thin_on_site_wall_energy": float, "p6_thin_off_site_wall_energy": float, "p6_thin_activation_energy": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_energies.json
- path: `/app/outputs/computed_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated numeric results for ferroelectric domain wall energies and activation energies computed from the prescribed models and parameters. The hidden checker compares each field to the paper's reported value using relative tolerances appropriate for analytic continuum formulas and discrete/activation values.
- schema:
  - `type`: object
  - `required`: `p4_continuum_wall_energy`, `p4_on_site_wall_energy`, `p4_off_site_wall_energy`, `p4_activation_energy`, `p6_thick_continuum_wall_energy`, `p6_thick_on_site_wall_energy`, `p6_thick_off_site_wall_energy`, `p6_thick_activation_energy`, `p6_thin_continuum_wall_energy`, `p6_thin_on_site_wall_energy`, `p6_thin_off_site_wall_energy`, `p6_thin_activation_energy`
  - `properties`:
    - `p4_continuum_wall_energy`:
      - `type`: number
    - `p4_on_site_wall_energy`:
      - `type`: number
    - `p4_off_site_wall_energy`:
      - `type`: number
    - `p4_activation_energy`:
      - `type`: number
    - `p6_thick_continuum_wall_energy`:
      - `type`: number
    - `p6_thick_on_site_wall_energy`:
      - `type`: number
    - `p6_thick_off_site_wall_energy`:
      - `type`: number
    - `p6_thick_activation_energy`:
      - `type`: number
    - `p6_thin_continuum_wall_energy`:
      - `type`: number
    - `p6_thin_on_site_wall_energy`:
      - `type`: number
    - `p6_thin_off_site_wall_energy`:
      - `type`: number
    - `p6_thin_activation_energy`:
      - `type`: number

Notes: All values are dimensionless floating-point scalars arising from the given parameters (α=−1, β=1, κ=0.5, a=1 for p^4; α=−1, β=−1, γ=1, a=1, κ=4 or 0.5 for p^6). The checker applies tolerances sufficient to absorb numerical and implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "p4_continuum_wall_energy",
          "p4_on_site_wall_energy",
          "p4_off_site_wall_energy",
          "p4_activation_energy",
          "p6_thick_continuum_wall_energy",
          "p6_thick_on_site_wall_energy",
          "p6_thick_off_site_wall_energy",
          "p6_thick_activation_energy",
          "p6_thin_continuum_wall_energy",
          "p6_thin_on_site_wall_energy",
          "p6_thin_off_site_wall_energy",
          "p6_thin_activation_energy"
        ],
        "properties": {
          "p4_continuum_wall_energy": {
            "type": "number"
          },
          "p4_on_site_wall_energy": {
            "type": "number"
          },
          "p4_off_site_wall_energy": {
            "type": "number"
          },
          "p4_activation_energy": {
            "type": "number"
          },
          "p6_thick_continuum_wall_energy": {
            "type": "number"
          },
          "p6_thick_on_site_wall_energy": {
            "type": "number"
          },
          "p6_thick_off_site_wall_energy": {
            "type": "number"
          },
          "p6_thick_activation_energy": {
            "type": "number"
          },
          "p6_thin_continuum_wall_energy": {
            "type": "number"
          },
          "p6_thin_on_site_wall_energy": {
            "type": "number"
          },
          "p6_thin_off_site_wall_energy": {
            "type": "number"
          },
          "p6_thin_activation_energy": {
            "type": "number"
          }
        }
      },
      "description": "Aggregated numeric results for ferroelectric domain wall energies and activation energies computed from the prescribed models and parameters. The hidden checker compares each field to the paper's reported value using relative tolerances appropriate for analytic continuum formulas and discrete/activation values."
    }
  ],
  "notes": "All values are dimensionless floating-point scalars arising from the given parameters (α=−1, β=1, κ=0.5, a=1 for p^4; α=−1, β=−1, γ=1, a=1, κ=4 or 0.5 for p^6). The checker applies tolerances sufficient to absorb numerical and implementation differences."
}
```

## How you are scored
A hidden verifier will read your `computed_energies.json` and compare each individual field against independently known reference values (obtained from the same theoretical models). Each field that falls within an appropriate tolerance — which accounts for numerical and implementation differences — earns a portion of the total reward. The final score is the fraction of the twelve fields that pass this check, scaled to the [0,1] range. Only the numerical values matter; file-format errors or missing fields are penalised separately. The verifier does not require any additional files beyond this JSON output.
